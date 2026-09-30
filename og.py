"""記事ごとのOG画像（SNSシェア用 1200x630 PNG）と一覧用サムネイル（640x336 WebP）、ロゴ画像を作る。

元記事の画像は著作権上使えないので、社名・製品名を大きく置いた文字のカードを自動生成する。
同じ内容の画像は .cache/og/ から再利用する（CIでは actions/cache で持ち越す）。
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
DESIGN_VERSION = "4"  # カードのデザインを変えたら上げる（キャッシュを捨てるため）

INK = (17, 20, 24)
PAPER = (255, 255, 255)
ORANGE = (255, 106, 26)
MUTED = (138, 147, 160)
TITLE = (214, 218, 224)


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


def render_og(a: dict, cat: dict, out: Path) -> None:
    """SNSシェア用（タイトル入り）"""
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(im)
    watermark(d, W, H)
    draw_fan(d, 64, 52, 56)
    d.text((132, 80), "AIデジマ", font=font("Heavy", 40), fill=PAPER, anchor="lm")
    chip(d, 64, 150, cat["name"], font("Bold", 26), hex_rgb(cat["color"]), 22, 50)
    kw = fit_font(a["thumb_text"], "Heavy", 1070, 132, 64)
    d.text((60, 300), a["thumb_text"], font=kw, fill=PAPER, anchor="lm")
    tf = font("Bold", 40)
    for i, line in enumerate(wrap(a["title"], tf, 1070, 3)):
        d.text((64, 400 + i * 58), line, font=tf, fill=TITLE)
    d.text((W - 64, H - 44), a["date"].strftime("%Y.%m.%d"), font=font("Medium", 26), fill=MUTED, anchor="rm")
    d.rectangle((0, H - 10, W, H), fill=ORANGE)
    im.save(out, "PNG", optimize=True)


def render_card(a: dict, cat: dict) -> Image.Image:
    """サイト内で使うカード（タイトルは画像の外に出るので入れない。社名・製品名を大きく）"""
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(im)
    watermark(d, W, H)
    color = hex_rgb(cat["color"])
    d.rectangle((0, 0, 18, H), fill=color)
    d.text((78, 96), cat["name"], font=font("Bold", 42), fill=color, anchor="lm")
    kw = fit_font(a["thumb_text"], "Heavy", 1040, 176, 72)
    d.text((72, H / 2 + 20), a["thumb_text"], font=kw, fill=PAPER, anchor="lm")
    draw_fan(d, 78, H - 120, 52)
    d.text((142, H - 90), "AIデジマ", font=font("Heavy", 34), fill=(150, 157, 168), anchor="lm")
    return im


def render_all(arts: list[dict], cats: dict, out_dir: Path, cache_dir: Path) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    cache_dir.mkdir(parents=True, exist_ok=True)
    stats = {"new": 0, "cached": 0}
    for a in arts:
        cat = cats[a["category"]]
        key = hashlib.sha1(
            json.dumps([DESIGN_VERSION, a["thumb_text"], a["title"], cat["slug"], cat["color"], a["date"].strftime("%Y%m%d")], ensure_ascii=False).encode()
        ).hexdigest()[:16]
        files = {"png": cache_dir / f"{key}.png", "eye.webp": cache_dir / f"{key}.eye.webp", "webp": cache_dir / f"{key}.webp"}
        if all(f.exists() for f in files.values()):
            stats["cached"] += 1
        else:
            render_og(a, cat, files["png"])
            card = render_card(a, cat)
            card.save(files["eye.webp"], "WEBP", quality=84, method=6)
            card.resize((640, 336), Image.LANCZOS).save(files["webp"], "WEBP", quality=84, method=6)
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
    im = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(im)
    for poly in fan_polygons(1010, 420, 520, 190, spread=100, panels=3, gap=4):
        d.polygon(poly, fill=(26, 30, 36))
    draw_fan(d, 72, 150, 120)
    d.text((72, 360), site["site_name"], font=font("Heavy", 120), fill=PAPER, anchor="ls")
    d.text((76, 440), site["tagline"], font=font("Bold", 44), fill=TITLE, anchor="ls")
    d.rectangle((0, H - 10, W, H), fill=ORANGE)
    im.save(assets / "og-default.png", "PNG", optimize=True)
