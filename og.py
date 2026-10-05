"""記事ごとの画像を作る。元記事の画像は著作権上使えないので、自前で作る。

- content/thumbs/<slug>.webp（scripts/thumbs.py が Gemini で生成した写真・イラスト）があれば、それを切り抜いて使う
- 無ければ、社名・製品名を大きく置いた文字カードを作る（生成に失敗した記事・キーが無い環境の予備）

出力（dist/og/<slug>.*）
  .jpg       1200x630  SNSシェア用（左上にロゴとカテゴリ）
  .eye.webp  1200x675  記事ページのアイキャッチ（16:9）
  .webp       640x360  一覧のサムネイル（16:9。スマホの一覧では 4:3 に切り抜いて見せる）
  .4x3.webp            構造化データ用（Googleは16:9・4:3・1:1の3種を推奨）
  .1x1.webp            同上
同じ内容の画像は .cache/og/ から再利用する（CIでは actions/cache で持ち越す）。
GitHub Pages は公開サイト全体で1GBまでなので、写真は1記事あたり約0.4MBに抑える。
"""
from __future__ import annotations

import hashlib
import json
import math
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
FONTS = ROOT / "fonts"
THUMBS = ROOT / "content" / "thumbs"
DESIGN_VERSION = "7"  # カードのデザインを変えたら上げる（キャッシュを捨てるため）

INK = (17, 20, 24)
PAPER = (255, 255, 255)
ORANGE = (255, 106, 26)
MUTED = (138, 147, 160)
TITLE = (61, 68, 78)
SUB = (107, 115, 128)


def mix(c, other, t: float) -> tuple[int, int, int]:
    """c に other を t の割合で混ぜる（t=0.9 なら other 寄り）"""
    return tuple(round(a * (1 - t) + b * t) for a, b in zip(c, other))  # type: ignore[return-value]


def palette(cat: dict) -> dict:
    """カテゴリ色から、明るいカードの配色を作る（白地に近い淡い色＋濃い文字。黒地は読みにくいので使わない）"""
    c = hex_rgb(cat["color"])
    return {"bg": mix(c, PAPER, 0.9), "mark": mix(c, PAPER, 0.8), "accent": c, "label": mix(c, INK, 0.3)}
VARIANTS = {"eye.webp": (1200, 675), "webp": (640, 360), "4x3.webp": (1200, 900), "1x1.webp": (1200, 1200)}
# 写真のときは元画像（1376x768）より大きく引き伸ばさない。Googleの構造化データは5万画素以上あればよい
PHOTO_VARIANTS = {"eye.webp": (1200, 675), "webp": (640, 360), "4x3.webp": (960, 720), "1x1.webp": (720, 720)}


def font(weight: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONTS / f"GenShinGothic-{weight}.ttf"), size)


def hex_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def fan_polygons(cx: float, cy: float, r_out: float, r_in: float, spread: float = 100, panels: int = 3, gap: float = 4) -> list[list[tuple[float, float]]]:
    """出島の扇形（＝電波マークにも見える）を、扇子のように数枚のパネルに割った多角形で返す。上向き"""
    polys = []
    start = -90 - spread / 2
    step = spread / panels
    for i in range(panels):
        a0 = math.radians(start + i * step + gap / 2)
        a1 = math.radians(start + (i + 1) * step - gap / 2)
        n = 24
        outer = [(cx + r_out * math.cos(a0 + (a1 - a0) * k / n), cy + r_out * math.sin(a0 + (a1 - a0) * k / n)) for k in range(n + 1)]
        inner = [(cx + r_in * math.cos(a1 - (a1 - a0) * k / n), cy + r_in * math.sin(a1 - (a1 - a0) * k / n)) for k in range(n + 1)]
        polys.append(outer + inner)
    return polys


def draw_fan(d: ImageDraw.ImageDraw, x: float, y: float, size: float, color=ORANGE) -> None:
    """(x, y) を左上、幅 size の箱に扇を描く"""
    r_out = size * 0.66
    for poly in fan_polygons(x + size / 2, y + size * 0.86, r_out, r_out * 0.36, spread=100, panels=3, gap=5):
        d.polygon(poly, fill=color)


def fit_font(text: str, weight: str, max_w: int, start: int, min_size: int) -> ImageFont.FreeTypeFont:
    size = start
    while size > min_size:
        f = font(weight, size)
        if f.getlength(text) <= max_w:
            return f
        size -= 4
    return font(weight, min_size)


def wrap(text: str, f: ImageFont.FreeTypeFont, max_w: int, max_lines: int) -> list[str]:
    """日本語は1文字単位で折り返す（英単語の途中では切らない）"""
    tokens = []
    buf = ""
    for ch in text:
        if ch.isascii() and ch not in " 　":
            buf += ch
            continue
        if buf:
            tokens.append(buf)
            buf = ""
        tokens.append(ch)
    if buf:
        tokens.append(buf)
    lines, cur = [], ""
    for t in tokens:
        if f.getlength(cur + t) <= max_w:
            cur += t
            continue
        lines.append(cur)
        cur = t.lstrip()
        if len(lines) == max_lines:
            break
    else:
        lines.append(cur)
        return [ln for ln in lines if ln][:max_lines]
    last = lines[max_lines - 1]
    while f.getlength(last + "…") > max_w and last:
        last = last[:-1]
    lines[max_lines - 1] = last + "…"
    return lines[:max_lines]


def chip(d: ImageDraw.ImageDraw, x: int, y: int, text: str, f: ImageFont.FreeTypeFont, bg, pad_x: int, h: int) -> int:
    w = int(f.getlength(text)) + pad_x * 2
    d.rounded_rectangle((x, y, x + w, y + h), radius=h // 2, fill=bg)
    d.text((x + pad_x, y + h / 2), text, font=f, fill=PAPER, anchor="lm")
    return w


def watermark(d: ImageDraw.ImageDraw, W: int, H: int, color=(24, 28, 34)) -> None:
    """右下の角から立ち上がる大きな扇（ブランドの透かし）"""
    s = H / 630
    for poly in fan_polygons(W - 60 * s, H + 150 * s, 600 * s, 230 * s, spread=100, panels=3, gap=4):
        d.polygon(poly, fill=color)


def cover(im: Image.Image, W: int, H: int) -> Image.Image:
    """中央を基準に、W x H を埋めるように拡大・切り抜く"""
    s = max(W / im.width, H / im.height)
    im = im.resize((max(W, round(im.width * s)), max(H, round(im.height * s))), Image.LANCZOS)
    x, y = (im.width - W) // 2, (im.height - H) // 2
    return im.crop((x, y, x + W, y + H))


def render_og_photo(src: Image.Image, cat: dict, out: Path) -> None:
    """SNSシェア用（写真＋左上にロゴとカテゴリ）。タイトルはSNS側が画像の外に出すので入れない（GIGAZINEなどと同じ）"""
    W, H = 1200, 630
    im = cover(src, W, H).convert("RGBA")
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x, y, h = 28, 28, 60
    lf = font("Heavy", 30)
    w = int(66 + lf.getlength("AIデジマ") + 22)
    d.rounded_rectangle((x, y, x + w, y + h), radius=h // 2, fill=(255, 255, 255, 238))
    draw_fan(d, x + 18, y + 9, 38)
    d.text((x + 64, y + h / 2), "AIデジマ", font=lf, fill=INK, anchor="lm")
    cf = font("Bold", 24)
    cx = x + w + 10
    cw = int(cf.getlength(cat["name"]) + 36)
    d.rounded_rectangle((cx, y + 7, cx + cw, y + h - 7), radius=(h - 14) // 2, fill=hex_rgb(cat["color"]) + (245,))
    d.text((cx + 18, y + h / 2), cat["name"], font=cf, fill=PAPER, anchor="lm")
    im = Image.alpha_composite(im, layer).convert("RGB")
    ImageDraw.Draw(im).rectangle((0, H - 8, W, H), fill=ORANGE)
    im.save(out, "JPEG", quality=84, optimize=True, progressive=True)


def render_og(a: dict, cat: dict, out: Path) -> None:
    """SNSシェア用（タイトル入り）"""
    W, H = 1200, 630
    pal = palette(cat)
    im = Image.new("RGB", (W, H), pal["bg"])
    d = ImageDraw.Draw(im)
    watermark(d, W, H, pal["mark"])
    draw_fan(d, 64, 52, 56)
    d.text((132, 80), "AIデジマ", font=font("Heavy", 40), fill=INK, anchor="lm")
    chip(d, 64, 150, cat["name"], font("Bold", 26), pal["accent"], 22, 50)
    y = 300
    if a.get("thumb_kicker"):
        d.text((64, 236), a["thumb_kicker"], font=font("Bold", 34), fill=SUB, anchor="lm")
    kw = fit_font(a["thumb_text"], "Heavy", 1070, 124, 60)
    d.text((60, y), a["thumb_text"], font=kw, fill=INK, anchor="lm")
    tf = font("Bold", 40)
    for i, line in enumerate(wrap(a["title"], tf, 1070, 3)):
        d.text((64, 400 + i * 58), line, font=tf, fill=TITLE)
    d.text((W - 64, H - 44), a["date"].strftime("%Y.%m.%d"), font=font("Medium", 26), fill=SUB, anchor="rm")
    d.rectangle((0, H - 10, W, H), fill=ORANGE)
    im.save(out, "JPEG", quality=90, optimize=True)


def render_card(a: dict, cat: dict, W: int = 1200, H: int = 675) -> Image.Image:
    """サイト内で使うカード（タイトルは画像の外に出るので入れない。社名を小さく、製品名を大きく）"""
    pal = palette(cat)
    im = Image.new("RGB", (W, H), pal["bg"])
    d = ImageDraw.Draw(im)
    watermark(d, W, H, pal["mark"])
    color = pal["accent"]
    s = min(W, H) / 675  # 4:3・1:1 は縦が伸びるので、短辺基準で拡大
    bar = int(18 * s)
    d.rectangle((0, 0, bar, H), fill=color)
    pad = int(78 * s)
    d.text((pad, int(96 * s)), cat["name"], font=font("Bold", int(42 * s)), fill=pal["label"], anchor="lm")
    cy = H / 2 + 20 * s
    if a.get("thumb_kicker"):
        d.text((pad - 4 * s, cy - 92 * s), a["thumb_kicker"], font=font("Bold", int(46 * s)), fill=SUB, anchor="lm")
    kw = fit_font(a["thumb_text"], "Heavy", int(W - pad - 60 * s), int(176 * s), int(64 * s))
    d.text((pad - 6 * s, cy), a["thumb_text"], font=kw, fill=INK, anchor="lm")
    draw_fan(d, pad, H - 120 * s, 52 * s)
    d.text((pad + 64 * s, H - 90 * s), "AIデジマ", font=font("Heavy", int(34 * s)), fill=SUB, anchor="lm")
    return im


def render_all(arts: list[dict], cats: dict, out_dir: Path, cache_dir: Path) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    cache_dir.mkdir(parents=True, exist_ok=True)
    stats = {"new": 0, "cached": 0}
    for a in arts:
        cat = cats[a["category"]]
        photo = THUMBS / f"{a['slug']}.webp"
        photo_hash = hashlib.sha1(photo.read_bytes()).hexdigest()[:16] if photo.exists() else ""
        key = hashlib.sha1(
            json.dumps(
                [DESIGN_VERSION, photo_hash, a["thumb_text"], a.get("thumb_kicker", ""), a["title"], cat["slug"], cat["color"], a["date"].strftime("%Y%m%d")],
                ensure_ascii=False,
            ).encode()
        ).hexdigest()[:16]
        files = {"jpg": cache_dir / f"{key}.jpg", **{ext: cache_dir / f"{key}.{ext}" for ext in VARIANTS}}
        if all(f.exists() for f in files.values()):
            stats["cached"] += 1
        elif photo_hash:
            src = Image.open(photo).convert("RGB")
            render_og_photo(src, cat, files["jpg"])
            for ext, (w, h) in PHOTO_VARIANTS.items():
                cover(src, w, h).save(files[ext], "WEBP", quality=80, method=6)
            stats["new"] += 1
        else:
            render_og(a, cat, files["jpg"])
            for ext, (w, h) in VARIANTS.items():
                if ext == "webp":
                    render_card(a, cat, 1200, 675).resize((w, h), Image.LANCZOS).save(files[ext], "WEBP", quality=84, method=6)
                else:
                    render_card(a, cat, w, h).save(files[ext], "WEBP", quality=82, method=6)
            stats["new"] += 1
        for ext, f in files.items():
            shutil.copyfile(f, out_dir / f"{a['slug']}.{ext}")
    return stats


def render_brand(assets: Path, site: dict) -> None:
    """構造化データ用ロゴ・ファビコン・デフォルトOG画像"""
    # ロゴ 600x120（白地）
    im = Image.new("RGB", (600, 120), PAPER)
    d = ImageDraw.Draw(im)
    draw_fan(d, 16, 14, 92)
    d.text((124, 62), site["site_name"], font=font("Heavy", 64), fill=INK, anchor="lm")
    im.save(assets / "logo-600.png", "PNG", optimize=True)
    # アイコン（墨地に扇）
    for size, name in ((180, "apple-touch-icon.png"), (512, "icon-512.png"), (48, "favicon-48.png")):
        ic = Image.new("RGB", (size, size), INK)
        draw_fan(ImageDraw.Draw(ic), size * 0.14, size * 0.08, size * 0.72)
        ic.save(assets / name, "PNG", optimize=True)
    # サイト全体のデフォルトOG
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), (255, 246, 240))
    d = ImageDraw.Draw(im)
    for poly in fan_polygons(1010, 420, 520, 190, spread=100, panels=3, gap=4):
        d.polygon(poly, fill=(255, 226, 208))
    draw_fan(d, 72, 150, 120)
    d.text((72, 360), site["site_name"], font=font("Heavy", 120), fill=INK, anchor="ls")
    d.text((76, 440), site["tagline"], font=font("Bold", 44), fill=TITLE, anchor="ls")
    d.rectangle((0, H - 10, W, H), fill=ORANGE)
    im.save(assets / "og-default.png", "PNG", optimize=True)
