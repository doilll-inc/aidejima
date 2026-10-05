#!/usr/bin/env python3
"""記事・ガイドのサムネイル写真を Gemini で生成し、content/thumbs/<slug>.webp に保存する。

tomo指示 2026-10-05「文字だけのサムネは単調で読みたくならない。GIGAZINEなどを参考に、記事のサムネはGeminiで毎回生成したい」。
- 1記事につき1回だけ作り、リポジトリにコミットして使い回す（ビルドのたびには作らない。1枚 約$0.067）
- 絵の中身は記事の thumb_prompt（記者が英語で書く場面の説明）と thumb_style。無ければタイトルと説明文から組み立てる
- 画風・禁止事項（文字・商標・実在人物）・スマホでの見え方は ART_RULES に集約。記者は「何を写すか」だけ書けばよい
- 失敗しても止めない。画像が無い記事は og.py が従来の文字カードを作る

  python3 scripts/thumbs.py                 # 未生成の記事・ガイドを作る（1回の上限 --max 枚）
  python3 scripts/thumbs.py --slug <slug>   # 指定のものだけ（作り直すときは --force）
  python3 scripts/thumbs.py --dry-run       # 送るプロンプトを表示するだけ（課金なし）
"""
from __future__ import annotations

import argparse
import base64
import io
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "content" / "articles"
GUIDES = ROOT / "data" / "guides"
OUT = ROOT / "content" / "thumbs"
GUIDE_PROMPTS = ROOT / "data" / "thumb_prompts.json"  # ガイドなど記事以外の絵の指定（slug → {style, prompt}）
MODEL = os.environ.get("GEMINI_IMAGE_MODEL", "gemini-3.1-flash-image-preview")  # Nano Banana 2
SIZE = (1376, 768)  # 1K の 16:9。4:3・1:1 に切り抜く余地を残すため縮めずに保存する

# 記事ごとに画風を変えて、一覧が単調にならないようにする（記者が thumb_style で選ぶ）
STYLES = {
    "photo": (
        "Make it a striking editorial news photograph, shot on a full-frame camera with a 35mm lens, natural directional light, "
        "shallow depth of field and rich true-to-life color, the kind of image that leads a feature story in a major technology magazine."
    ),
    "3d": (
        "Make it a polished high-end 3D render with soft studio lighting, gentle shadows, a mix of glossy and matte materials, "
        "a bold saturated color palette and a clean seamless backdrop, like conceptual cover art for a technology magazine."
    ),
    "illustration": (
        "Make it a bold editorial illustration with flat shapes, a limited vivid palette, subtle paper grain and a strong graphic composition, "
        "like the opinion-page art of a leading newspaper or the graphic style of a modern tech news site."
    ),
    "diorama": (
        "Make it a playful tilt-shift photograph of a handmade miniature diorama, a small stage with only a few tiny figures and props, "
        "warm light, shallow depth of field and crisp model-making detail."
    ),
}
DEFAULT_STYLE = "photo"

# 全部の絵に共通の決まり。構造化した箇条書きにすると Gemini が関数呼び出しと誤解して画像を返さないことがあるので、地の文で書く
ART_RULES = (
    "The picture must contain no readable text at all: no letters, words, numbers, captions, signs, company emblems, trademarks or user-interface labels, "
    "and any screen in the scene shows only abstract shapes, charts without labels or soft blurred color. "
    "Do not depict any real, identifiable person; people, when they appear, are anonymous, seen from behind, in silhouette or out of focus. "
    "Compose it for a phone screen first: one clear main subject that fills a large part of the frame, at most two or three elements in total and no busy clutter, "
    "strong contrast against a simple uncluttered background, "
    "still readable as a tiny thumbnail, with the subject centered and nothing important near the left and right edges so the image also works cropped to a square. "
    "It should feel concrete and a little surprising, so that someone scrolling past wants to tap it."
)


def read_meta(path: Path) -> dict | None:
    m = re.match(r"---\s*\n(.*?)\n---\s*\n", path.read_text(encoding="utf-8"), re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError:
        return None


def build_prompt(scene: str, style: str) -> str:
    return f"Create a wide 16:9 cover image for a Japanese technology news article. {scene.strip()} {STYLES.get(style, STYLES[DEFAULT_STYLE])} {ART_RULES}"


def fallback_scene(title: str, description: str) -> str:
    """記者が thumb_prompt を書かなかったときの場面。記事の要旨を渡して、何を写すかは Gemini に任せる"""
    return (
        "Show one concrete, visual scene that captures the core of this news story, using objects, places or anonymous people rather than abstract symbols. "
        f"The story (in Japanese) is: {title}. {description}"
    )


def jobs() -> list[dict]:
    """生成の候補（新しい順）。記事＋ガイド"""
    out = []
    for p in sorted(ARTICLES.glob("*.md"), reverse=True):
        meta = read_meta(p)
        if not meta:
            continue
        scene = meta.get("thumb_prompt") or fallback_scene(meta.get("title", ""), meta.get("description", ""))
        out.append({"slug": p.stem, "style": meta.get("thumb_style") or DEFAULT_STYLE, "scene": scene, "auto": not meta.get("thumb_prompt")})
    extra = json.loads(GUIDE_PROMPTS.read_text(encoding="utf-8")) if GUIDE_PROMPTS.exists() else {}
    for p in sorted(GUIDES.glob("*.json")):
        if p.stem.startswith("_"):
            continue
        g = json.loads(p.read_text(encoding="utf-8"))
        slug = f"best-{g.get('slug') or p.stem}"
        spec = extra.get(slug) or {}
        name = g.get("short_name") or g.get("title") or p.stem
        scene = spec.get("prompt") or f"Show a concrete scene of someone using AI tools for this purpose: {name}."
        out.append({"slug": slug, "style": spec.get("style") or DEFAULT_STYLE, "scene": scene, "auto": not spec.get("prompt")})
    return out


def generate(prompt: str, key: str) -> Image.Image:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"], "imageConfig": {"aspectRatio": "16:9", "imageSize": "1K"}},
    }
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={"Content-Type": "application/json", "x-goog-api-key": key})
    with urllib.request.urlopen(req, timeout=180) as r:
        res = json.load(r)
    for cand in res.get("candidates") or []:
        for part in (cand.get("content") or {}).get("parts") or []:
            data = (part.get("inlineData") or part.get("inline_data") or {}).get("data")
            if data:
                return Image.open(io.BytesIO(base64.b64decode(data))).convert("RGB")
    reason = [c.get("finishReason") for c in res.get("candidates") or []] or res.get("promptFeedback")
    raise RuntimeError(f"画像が返らなかった（{reason}）")


def cover(im: Image.Image, size: tuple[int, int]) -> Image.Image:
    W, H = size
    s = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x, y = (im.width - W) // 2, (im.height - H) // 2
    return im.crop((x, y, x + W, y + H))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", action="append", help="この slug だけ作る（複数可）")
    ap.add_argument("--force", action="store_true", help="既にあっても作り直す")
    ap.add_argument("--max", type=int, default=int(os.environ.get("THUMBS_MAX", "12")), help="1回で作る上限（課金の安全弁）")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    todo = [j for j in jobs() if (not args.slug or j["slug"] in args.slug) and (args.force or not (OUT / f"{j['slug']}.webp").exists())]
    if not todo:
        print("サムネイル: 新しく作るものはない")
        return 0
    todo = todo[: args.max]
    key = os.environ.get("GEMINI_API_KEY", "")
    if not key and not args.dry_run:
        print("サムネイル: GEMINI_API_KEY が無いので作らない（文字カードのまま）")
        return 0
    OUT.mkdir(parents=True, exist_ok=True)
    made = 0
    for j in todo:
        prompt = build_prompt(j["scene"], j["style"])
        if args.dry_run:
            print(f"--- {j['slug']} [{j['style']}{' / 自動' if j['auto'] else ''}]\n{prompt}\n")
            continue
        for attempt in range(3):
            try:
                im = generate(prompt, key)
                cover(im, SIZE).save(OUT / f"{j['slug']}.webp", "WEBP", quality=84, method=6)
                made += 1
                print(f"サムネイル: {j['slug']} を作った（{j['style']}）")
                break
            except (urllib.error.URLError, RuntimeError, OSError) as e:
                detail = e.read().decode()[:300] if isinstance(e, urllib.error.HTTPError) else str(e)
                print(f"サムネイル: {j['slug']} 失敗 {attempt + 1}/3: {detail}", file=sys.stderr)
                time.sleep(5 * (attempt + 1))
    if not args.dry_run:
        print(f"サムネイル: {made}/{len(todo)} 枚を作った（モデル {MODEL}）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
