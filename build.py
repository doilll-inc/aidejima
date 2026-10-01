#!/usr/bin/env python3
"""AIデジマ の静的サイトジェネレータ。content/articles/*.md → dist/ に全ページを書き出す。

  python3 build.py           # ビルド（記事の形式チェックで不備があれば失敗する）
  python3 build.py --serve   # ビルドして http://localhost:8000/aidejima/ で確認
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import shutil
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

import guides as guides_mod
import og

ROOT = Path(__file__).resolve().parent
# 出力先。複数の作業者が同時にビルドするときは AIDEJIMA_DIST で分ける
DIST = Path(os.environ["AIDEJIMA_DIST"]) if os.environ.get("AIDEJIMA_DIST") else ROOT / "dist"
CONTENT = ROOT / "content" / "articles"
PAGES = ROOT / "content" / "pages"
JST = timezone(timedelta(hours=9))
WEEKDAYS = "月火水木金土日"
REQUIRED = ("title", "description", "date", "category", "tags", "summary", "sources")

SITE = json.loads((ROOT / "data" / "site.json").read_text(encoding="utf-8"))
TAXO = json.loads((ROOT / "data" / "taxonomy.json").read_text(encoding="utf-8"))
MODELS = json.loads((ROOT / "data" / "models.json").read_text(encoding="utf-8"))["models"]
CATS = {c["slug"]: c for c in TAXO["categories"]}
BASE_PATH = SITE["base_path"].rstrip("/")
BASE_URL = SITE["base_url"].rstrip("/")
TAG_INDEX_MIN = SITE.get("tag_index_min", 3)  # タグページをこの本数未満なら noindex（薄いページを検索に出さない）
NEW_HOURS = SITE.get("new_badge_hours", 12)

# 情報源の種別（記事ページで「公式発表／X投稿／論文／報道」と見せる）。sources[].kind で明示しなければドメインで判定
SOURCE_KINDS = TAXO.get("source_kinds", {})
OFFICIAL_DOMAINS = SOURCE_KINDS.get("official_domains", [])
PAPER_DOMAINS = SOURCE_KINDS.get("paper_domains", [])
COMPANY_NAMES = set(SOURCE_KINDS.get("company_tags", []))
# 記事本文で使わない言い回し（煽り・空疎な締め）。ビルドは止めず注意として出す
BANNED_PHRASES = ["今後の動向に注目", "注目していきましょう", "目が離せません", "革命的", "衝撃", "ヤバい", "ゲームチェンジャー", "と言えるでしょう", "ではないでしょうか", "！"]


# ---------- URL・日付のヘルパ ----------

def u(path: str) -> str:
    """サイト内パス → base_path 付きのパス（GitHub Pages のサブパス配信に対応）"""
    return BASE_PATH + path if path.startswith("/") else path


def abs_url(path: str) -> str:
    return BASE_URL + path


def tag_slug(tag: str) -> str:
    if tag in TAXO["tag_slugs"]:
        return TAXO["tag_slugs"][tag]
    s = re.sub(r"[^a-z0-9]+", "-", tag.lower()).strip("-")
    if s and re.fullmatch(r"[a-z0-9-]+", s) and re.search(r"[a-z0-9]", tag.lower()):
        return s
    # 未登録の日本語タグ。data/taxonomy.json の tag_slugs に足すまでの仮slug
    return "t-" + hashlib.sha1(tag.encode()).hexdigest()[:8]


def fmt_dt(d: datetime) -> str:
    return d.strftime("%Y年%m月%d日 %H時%M分")


def fmt_date(d: datetime) -> str:
    return f"{d.year}年{d.month}月{d.day}日（{WEEKDAYS[d.weekday()]}）"


def fmt_short(d: datetime) -> str:
    return f"{d.month}月{d.day}日 {d.strftime('%H:%M')}"


def host_of(url: str) -> str:
    try:
        return urllib.parse.urlsplit(url).netloc.lower().removeprefix("www.")
    except ValueError:
        return ""


def source_kind(s: dict) -> str:
    if s.get("kind"):
        return s["kind"]
    url = s.get("url", "")
    h = host_of(url)
    if h in ("x.com", "twitter.com"):
        return "X投稿"
    if any(h == d or h.endswith("." + d) for d in PAPER_DOMAINS) or "/papers/" in url or "arxiv" in h:
        return "論文"
    if any(h == d or h.endswith("." + d) for d in OFFICIAL_DOMAINS):
        if re.search(r"/docs?/|/documentation/|/changelog|/release-notes|developers\.|platform\.|/api/", url):
            return "公式ドキュメント"
        return "公式発表"
    return "報道"


# ---------- 記事の読み込み ----------

X_EMBED_RE = re.compile(r"\{\{\s*x:\s*(https?://(?:x\.com|twitter\.com)/[^\s}]+)\s*\}\}")
CARD_RE = re.compile(r"\{\{\s*card:\s*(https?://[^|}\s]+)\s*\|\s*([^|}]+?)\s*(?:\|\s*([^}]+?)\s*)?\}\}")
YT_RE = re.compile(r"\{\{\s*youtube:\s*(https?://[^\s}]+)\s*\}\}")
QUOTE_RE = re.compile(r"^:::quote[ \t]+(https?://\S+)[ \t]*\|[ \t]*(.+?)[ \t]*\n(.*?)\n:::[ \t]*$", re.M | re.S)
OEMBED_CACHE = ROOT / ".cache" / "x_oembed"
MAX_QUOTES = 3


def x_oembed(url: str) -> tuple[str | None, str]:
    """Xの公開oEmbed（無料・APIキー不要）で投稿の実在を確かめ、埋め込みHTMLを返す。
    戻り値: (html, 状態) 状態は ok / missing（存在しない・非公開） / offline（通信できずキャッシュもない）"""
    m = re.search(r"/status/(\d+)", url)
    if not m:
        return None, "missing"
    cache = OEMBED_CACHE / f"{m.group(1)}.json"
    if cache.exists():
        data = json.loads(cache.read_text(encoding="utf-8"))
        return (data.get("html"), "ok") if data.get("html") else (None, "missing")
    q = urllib.parse.urlencode({"url": url, "omit_script": "true", "dnt": "true", "lang": "ja", "hide_thread": "true"})
    try:
        req = urllib.request.Request(f"https://publish.twitter.com/oembed?{q}", headers={"User-Agent": "Mozilla/5.0 AIDejimaBuild"})
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read())
    except urllib.error.HTTPError as e:
        if e.code == 404:
            OEMBED_CACHE.mkdir(parents=True, exist_ok=True)
            cache.write_text(json.dumps({"html": None, "status": 404}), encoding="utf-8")
            return None, "missing"
        return None, "offline"
    except (urllib.error.URLError, TimeoutError, OSError):
        return None, "offline"
    OEMBED_CACHE.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps({"html": data.get("html"), "author": data.get("author_name")}, ensure_ascii=False), encoding="utf-8")
    return data.get("html"), "ok"


def initial_badge(label: str) -> str:
    ch = next((c for c in label if c.isalnum()), "?")
    return html.escape(ch.upper())


def render_quote(url: str, label: str, inner: str) -> tuple[str, list[str]]:
    """:::quote の中身 → 公式発表の引用カード（原文＋日本語訳＋出典）"""
    warns = []
    orig = " ".join(ln.lstrip(">").strip() for ln in inner.splitlines() if ln.strip().startswith(">"))
    ja = " ".join(ln.strip() for ln in inner.splitlines() if ln.strip() and not ln.strip().startswith(">"))
    if not orig:
        warns.append(f"引用カードに原文（> で始まる行）がない: {url}")
    if not ja:
        warns.append(f"引用カードに日本語訳がない: {url}")
    if len(re.findall(r"[.!?](?:\s|$)", orig)) > 2:
        warns.append(f"引用カードの原文が2文を超えている（引用は必要な範囲だけ）: {url}")
    kind = source_kind({"url": url})
    host = host_of(url)
    e = html.escape
    return (
        f'\n\n<figure class="pq">'
        f'<figcaption class="pq-head"><span class="pq-badge" aria-hidden="true">{initial_badge(label)}</span>'
        f'<span class="pq-src">{e(label)}</span><span class="pq-kind" data-kind="{e(kind)}">{e(kind)}</span></figcaption>'
        + (f'<blockquote class="pq-orig" cite="{e(url)}" lang="en"><p>{e(orig)}</p></blockquote>' if orig else "")
        + (f'<p class="pq-ja">{e(ja)}</p>' if ja else "")
        + f'<a class="pq-link" href="{e(url)}" target="_blank" rel="noopener">原文を読む（{e(host)}）</a></figure>\n\n'
    ), warns


def expand_embeds(md_text: str) -> tuple[str, bool, list[str]]:
    """本文の埋め込み記法をHTMLに置き換える。
      {{x:https://x.com/<user>/status/<id>}}   X投稿（ビルド時にoEmbedで実在を確認して本文ごと埋め込む）
      :::quote <URL> | <発信元・ページ名> … :::  公式発表の引用カード（> 行=原文、それ以外=日本語訳）
      {{card:<URL>|<ページのタイトル>|<発信元>}}  公式ページへのリンクカード
      {{youtube:<URL>}}                          公式動画（クリックで再生）
    戻り値: (置き換え後のMarkdown, X埋め込みがあるか, 警告)"""
    found_x = False
    warns: list[str] = []
    e = html.escape

    def rep_x(m: re.Match) -> str:
        nonlocal found_x
        url = m.group(1).replace("twitter.com", "x.com").split("?")[0]
        embed, state = x_oembed(url)
        if state == "missing":
            warns.append(f"X投稿が見つからない（存在しない・削除・非公開）ので埋め込みを外した: {url}")
            return ""
        found_x = True
        if state == "offline" or not embed:
            user = re.search(r"x\.com/([^/]+)/status/", url)
            label = f"@{user.group(1)} の投稿を見る（X）" if user else "Xの投稿を見る"
            embed = f'<blockquote class="twitter-tweet" data-dnt="true" data-lang="ja"><a href="{e(url)}">{e(label)}</a></blockquote>'
        return f'\n\n<figure class="x-embed">{embed.strip()}</figure>\n\n'

    def rep_quote(m: re.Match) -> str:
        out, w = render_quote(m.group(1), m.group(2), m.group(3))
        warns.extend(w)
        return out

    def rep_card(m: re.Match) -> str:
        url, title, pub = m.group(1), m.group(2), m.group(3) or ""
        kind = source_kind({"url": url})
        return (
            f'\n\n<a class="lcard" href="{e(url)}" target="_blank" rel="noopener"><span class="lcard-kind" data-kind="{e(kind)}">{e(kind)}</span>'
            f'<span class="lcard-title">{e(title)}</span><span class="lcard-meta">{e(pub)}{" · " if pub else ""}{e(host_of(url))}</span></a>\n\n'
        )

    def rep_yt(m: re.Match) -> str:
        url = m.group(1)
        vid = re.search(r"(?:v=|youtu\.be/|/embed/|/shorts/|/live/)([A-Za-z0-9_-]{6,})", url)
        if not vid:
            warns.append(f"YouTubeのURLから動画IDが取れない: {url}")
            return ""
        v = e(vid.group(1))
        return (
            f'\n\n<figure class="yt"><a class="yt-embed" href="{e(url)}" data-id="{v}" data-title="YouTube" target="_blank" rel="noopener">'
            f'<img src="https://i.ytimg.com/vi/{v}/hqdefault.jpg" width="480" height="360" alt="" loading="lazy" decoding="async"><span class="yt-play" aria-hidden="true"></span>'
            f'<span class="visually-hidden">動画を再生</span></a><figcaption>公式動画（YouTube）</figcaption></figure>\n\n'
        )

    quotes = len(QUOTE_RE.findall(md_text))
    if quotes > MAX_QUOTES:
        warns.append(f"引用カードが{quotes}個ある（{MAX_QUOTES}個まで。記事の本文が主になるように）")
    md_text = QUOTE_RE.sub(rep_quote, md_text)
    md_text = X_EMBED_RE.sub(rep_x, md_text)
    md_text = CARD_RE.sub(rep_card, md_text)
    md_text = YT_RE.sub(rep_yt, md_text)
    return md_text, found_x, warns


def pick_thumb_text(meta: dict) -> tuple[str, str]:
    """カード画像に大きく出す語（製品名など）と、小さく添える語（社名）。
    優先: thumb_text の指定 → タイトルの「」内 → タイトルに出てくる社名以外のタグ → 先頭タグ"""
    tags = meta["tags"]
    title = meta["title"]
    big = meta.get("thumb_text")
    in_title = [t for t in tags if t in title]
    if not big:
        # 「」内は製品名（英数字を含むもの）のときだけ使う。「引用される情報」のような一般語は絵にならない
        m = re.search(r"「([^」]{2,20})」", title)
        if m and re.search(r"[A-Za-z0-9]", m.group(1)):
            big = m.group(1)
    if not big:
        # 製品名（英字を含む・社名ではない）→ 社名 → 日本語の一般語（「買収」「エージェント」等は絵にならない）
        product = [t for t in in_title if t not in COMPANY_NAMES and re.search(r"[A-Za-z0-9]", t)]
        company = [t for t in in_title if t in COMPANY_NAMES] or [t for t in tags if t in COMPANY_NAMES]
        big = (product or company or in_title or tags)[0]
    kicker = meta.get("thumb_kicker")
    if kicker is None:
        # 大きい語がすでに社名なら添えない（別の社名が並ぶと、どの会社の話か紛らわしい）
        if big in COMPANY_NAMES:
            kicker = ""
        else:
            # タイトルに出てくる社名だけ添える（タグにあるだけの社名は、話の主役とは限らない）
            kicker = next((t for t in in_title if t in COMPANY_NAMES and t not in big), "")
    return big, kicker


def parse_article(path: Path) -> tuple[dict | None, list[str]]:
    errs: list[str] = []
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\s*\n(.*?)\n---\s*\n(.*)", text, re.S)
    if not m:
        return None, [f"{path.name}: 先頭の --- で挟んだJSONメタ情報がない"]
    try:
        meta = json.loads(m.group(1))
    except json.JSONDecodeError as e:
        return None, [f"{path.name}: メタ情報のJSONが壊れている ({e})"]
    for k in REQUIRED:
        if not meta.get(k):
            errs.append(f"{path.name}: {k} が空")
    if meta.get("category") and meta["category"] not in CATS:
        errs.append(f"{path.name}: category '{meta['category']}' は未定義（{', '.join(CATS)}）")
    try:
        date = datetime.fromisoformat(meta.get("date", ""))
        if not date.tzinfo:
            raise ValueError("タイムゾーンがない")
    except ValueError as e:
        errs.append(f"{path.name}: date が不正 ({e})")
        date = None
    if len(meta.get("summary") or []) != 3:
        errs.append(f"{path.name}: summary は3行にする")
    for s in meta.get("sources") or []:
        if not str(s.get("url", "")).startswith("http"):
            errs.append(f"{path.name}: sources のURLが不正 ({s})")
    if not re.fullmatch(r"\d{8}-[a-z0-9-]+", path.stem):
        errs.append(f"{path.name}: ファイル名は YYYYMMDD-<英小文字とハイフン>.md にする")
    if errs:
        return None, errs

    slug = path.stem
    body_md, has_x, embed_warns = expand_embeds(m.group(2).strip())
    body_html, toc = render_body(body_md)
    updated = datetime.fromisoformat(meta["updated"]) if meta.get("updated") else None
    sources = [{**s, "kind": source_kind(s), "host": host_of(s.get("url", ""))} for s in meta["sources"]]
    kinds = [s["kind"] for s in sources]
    chars = len(re.sub(r"\s", "", re.sub(r"<[^>]+>", "", body_html)))
    big, kicker = pick_thumb_text(meta)
    a = {
        **meta,
        "slug": slug,
        "path": f"/news/{slug}/",
        "date": date.astimezone(JST),
        "updated": updated.astimezone(JST) if updated else None,
        "body": body_html,
        "toc": toc,
        "cat": CATS[meta["category"]],
        "tag_items": [{"name": t, "slug": tag_slug(t)} for t in meta["tags"]],
        "chars": chars,
        "read_min": max(1, round(chars / 600)),
        "thumb_text": big,
        "thumb_kicker": kicker,
        "sources": sources,
        "publishers": list(dict.fromkeys(s.get("publisher", "") for s in sources if s.get("publisher"))),
        "primary_count": sum(1 for k in kinds if k in ("公式発表", "公式ドキュメント", "X投稿", "論文")),
        "has_x_embed": has_x,
        "embed_warns": embed_warns,
        "quote_count": body_html.count('class="pq"'),
        "x_count": body_html.count('class="x-embed"'),
        "share_text": meta.get("share_text") or meta["title"],
    }
    return a, []


def render_body(md_text: str) -> tuple[str, list[dict]]:
    h = markdown.markdown(md_text, extensions=["tables", "fenced_code", "sane_lists", "attr_list"], output_format="html")
    toc: list[dict] = []

    def add_id(m: re.Match) -> str:
        n = len(toc) + 1
        title = re.sub(r"<[^>]+>", "", m.group(1))
        toc.append({"id": f"s{n}", "title": html.unescape(title)})
        return f'<h2 id="s{n}">{m.group(1)}</h2>'

    h = re.sub(r"<h2>(.*?)</h2>", add_id, h)
    # 本文中のサイト内リンク（/news/... 等）に base_path を付ける
    h = re.sub(r'href="/(?!/)', f'href="{BASE_PATH}/', h)
    # 外部リンクは新しいタブで開く
    h = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', h)
    # 表は横スクロールできる箱に入れる（スマホではみ出さないように）
    h = h.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    return h, toc


def load_articles() -> list[dict]:
    arts, errors = [], []
    for p in sorted(CONTENT.glob("*.md")):
        a, errs = parse_article(p)
        errors += errs
        if a:
            arts.append(a)
    if errors:
        print("記事の形式エラー:\n  " + "\n  ".join(errors), file=sys.stderr)
        sys.exit(1)
    slugs = Counter(a["slug"] for a in arts)
    dup = [s for s, n in slugs.items() if n > 1]
    if dup:
        sys.exit(f"slugが重複: {dup}")
    arts.sort(key=lambda a: a["date"], reverse=True)
    return arts


def build_related(arts: list[dict], n: int = 4) -> dict[str, list[dict]]:
    """タグ・カテゴリの重なりで関連記事を選ぶ。全記事×全記事にしない（数千本でも速いように、タグ索引から候補を出す）"""
    by_tag: dict[str, list[dict]] = defaultdict(list)
    by_cat: dict[str, list[dict]] = defaultdict(list)
    for a in arts:
        by_cat[a["category"]].append(a)
        for t in a["tags"]:
            by_tag[t].append(a)
    out: dict[str, list[dict]] = {}
    for a in arts:
        cand: dict[str, float] = {}
        objs: dict[str, dict] = {}
        for t in a["tags"]:
            for b in by_tag[t]:
                if b is not a:
                    cand[b["slug"]] = cand.get(b["slug"], 0.0) + 2.0
                    objs[b["slug"]] = b
        for b in by_cat[a["category"]][:200]:  # 同カテゴリは新しい200本まで
            if b is not a:
                cand[b["slug"]] = cand.get(b["slug"], 0.0) + 1.0
                objs[b["slug"]] = b
        scored = []
        for slug, s in cand.items():
            b = objs[slug]
            days = abs((a["date"] - b["date"]).total_seconds()) / 86400
            scored.append((s - 0.05 * days, b))
        scored.sort(key=lambda x: x[0], reverse=True)
        out[a["slug"]] = [b for _, b in scored[:n]]
    return out


# ---------- 構造化データ ----------

def org_ld() -> dict:
    return {
        "@type": "NewsMediaOrganization",
        "@id": abs_url("/#org"),
        "name": SITE["site_name"],
        "alternateName": SITE["site_name_en"],
        "url": abs_url("/"),
        "logo": {"@type": "ImageObject", "url": abs_url("/assets/logo-600.png"), "width": 600, "height": 120},
        "parentOrganization": {
            "@type": "Organization",
            "name": SITE["operator"]["name"],
            "url": SITE["operator"]["url"],
            "address": {"@type": "PostalAddress", "addressLocality": "渋谷区", "addressRegion": "東京都", "addressCountry": "JP"},
        },
        "founder": {"@id": abs_url("/about/editor/#person")},
        "masthead": abs_url("/about/"),
        "publishingPrinciples": abs_url("/about/#policy"),
        "correctionsPolicy": abs_url("/about/#corrections"),
        "actionableFeedbackPolicy": abs_url("/about/#corrections"),
    }


def editor_ld() -> dict:
    e = SITE["editor"]
    return {
        "@type": "Person",
        "@id": abs_url("/about/editor/#person"),
        "name": e["name"],
        "alternateName": e["name_en"],
        "jobTitle": e["title"],
        "description": e["short_bio"],
        "url": abs_url("/about/editor/"),
        "worksFor": {"@type": "Organization", "name": SITE["operator"]["name"], "url": SITE["operator"]["url"]},
        "alumniOf": {"@type": "CollegeOrUniversity", "name": "東京大学"},
        "knowsAbout": ["AI", "広告", "デジタルマーケティング"],
        "sameAs": e["same_as"],
    }


def article_images(a: dict) -> list[str]:
    return [abs_url(f"/og/{a['slug']}.png"), abs_url(f"/og/{a['slug']}.eye.webp"), abs_url(f"/og/{a['slug']}.4x3.webp"), abs_url(f"/og/{a['slug']}.1x1.webp")]


def article_ld(a: dict) -> list[dict]:
    return [
        {
            "@context": "https://schema.org",
            "@type": "NewsArticle",
            "headline": a["title"],
            "description": a["description"],
            "image": article_images(a),
            "datePublished": a["date"].isoformat(),
            "dateModified": (a["updated"] or a["date"]).isoformat(),
            "author": {"@type": "Organization", "name": f"{SITE['site_name']}編集部", "url": abs_url("/about/")},
            "editor": editor_ld(),
            "publisher": org_ld(),
            "mainEntityOfPage": abs_url(a["path"]),
            "articleSection": a["cat"]["name"],
            "keywords": a["tags"],
            "inLanguage": "ja",
            "isAccessibleForFree": True,
            "wordCount": a["chars"],
            "citation": [s["url"] for s in a["sources"]],
        },
        breadcrumb_ld([("ホーム", "/"), (a["cat"]["name"], f"/category/{a['category']}/"), (a["title"], a["path"])]),
    ]


def breadcrumb_ld(items: list[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": abs_url(path)} for i, (name, path) in enumerate(items)
        ],
    }


def itemlist_ld(items: list[dict]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": abs_url(a["path"])} for i, a in enumerate(items[:30])],
    }


# ---------- 書き出し ----------

def write(path: str, content: str | bytes) -> None:
    """path はサイト内パス（/news/x/ → dist/news/x/index.html）"""
    p = DIST / path.lstrip("/")
    if path.endswith("/"):
        p = p / "index.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(content, bytes):
        p.write_bytes(content)
    else:
        p.write_text(content, encoding="utf-8")


def asset_version() -> str:
    h = hashlib.sha1()
    for f in sorted((ROOT / "static").rglob("*")):
        if f.is_file():
            h.update(f.read_bytes())
    return h.hexdigest()[:8]


def paginate(items: list, per: int) -> list[list]:
    return [items[i : i + per] for i in range(0, max(len(items), 1), per)] or [[]]


def group_by_day(arts: list[dict]) -> list[dict]:
    groups: dict[str, dict] = {}
    for a in arts:
        key = a["date"].strftime("%Y-%m-%d")
        groups.setdefault(key, {"label": fmt_date(a["date"]), "items": []})["items"].append(a)
    return list(groups.values())


def model_pages(arts: list[dict]) -> list[dict]:
    """data/models.json とモデル名を含む記事を結びつける"""
    out = []
    for m in MODELS:
        name = m["name"].lower()
        rel = [a for a in arts if any(t.lower() == name for t in a["tags"]) or name in a["title"].lower()]
        d = None
        try:
            d = datetime.strptime(m["released"], "%Y-%m-%d") if m.get("released") else None
        except ValueError:
            pass
        out.append({**m, "path": f"/models/{m['slug']}/", "articles": rel[:20], "released_dt": d})
    out.sort(key=lambda m: (m.get("released") or "", m["name"]), reverse=True)
    return out


# ---------- 用途別AIガイド（/best/） ----------

ENUM_LABELS = {
    "japanese": {"yes": "対応", "partial": "一部", "no": "非対応", "unknown": "—"},
    "commercial_use": {"yes": "可", "conditional": "条件付き", "no": "不可", "unknown": "—"},
    "data_policy": {"not_used": "学習に使わない", "opt_out_available": "設定で拒否可", "used": "学習に使う", "unknown": "—"},
    "availability_japan": {"yes": "提供あり", "partial": "一部", "no": "提供なし", "unknown": "—"},
}
PER_LABEL = {"month": "/月", "year": "/年", "once": "（買い切り）", "seat_month": "/人・月", "credit": ""}
CUR_SYMBOL = {"USD": "$", "JPY": "¥", "EUR": "€", "GBP": "£"}
GUIDE_CAT = {"slug": "guide", "name": "用途別AIガイド", "color": "#ff6a1a"}


def fmt_price(f: dict | None) -> str:
    """料金の fact を「$20/月」「¥3,000/月」の形に（為替換算はしない）"""
    if not f:
        return "—"
    amt = f.get("amount")
    if amt is None:
        return f.get("as_shown") or "—"
    cur = f.get("currency", "USD")
    sym = CUR_SYMBOL.get(cur, cur + " ")
    num = f"{amt:,.0f}" if cur == "JPY" else (f"{amt:g}" if amt >= 1 else f"{amt:.4g}")
    unit = f" / {f['unit']}" if f.get("unit") else PER_LABEL.get(f.get("per", ""), "")
    return f"{sym}{num}{unit}"


def usd(v) -> str:
    """100万トークン単価の表示。$0.075 を $0.07 と丸めないよう、1未満は有効数字3桁まで出す"""
    if v is None:
        return "—"
    v = float(v)
    if v >= 1:
        return f"${v:,.2f}".replace(".00", "")
    return "$" + (f"{v:.3g}" if v >= 0.001 else f"{v:.2e}")


def source_label(url: str) -> str:
    low = url.lower()
    hints = TAXO.get("source_kinds", {}).get("pricing_path_hints", ["/pricing", "/plans"])
    if any(h in low for h in hints):
        return "公式料金"
    if re.search(r"terms|legal|policy|privacy|tos|usage-polic", low):
        return "公式の規約・ポリシー"
    if re.search(r"/docs?/|/help|support\.|/faq|developers?\.|platform\.|/api/", low):
        return "公式ドキュメント・ヘルプ"
    return "公式発表・公式ページ"


def guide_pages(arts: list[dict], models: list[dict], now: datetime) -> tuple[list[dict], list[str], list[str]]:
    """data/guides/*.json（published だけ）に、表示用の派生値を足す"""
    out, errors, warns = [], [], []
    model_by_slug = {m["slug"]: m for m in models}
    art_by_path = {a["path"]: a for a in arts}
    for g in guides_mod.load_all():
        if g.get("status") != "published":
            continue
        e, w = guides_mod.validate(g, OFFICIAL_DOMAINS)
        errors += e
        warns += w
        edition, stale = guides_mod.month_edition(g, now)
        prods = sorted(g.get("products") or [], key=lambda p: (p.get("rank", 99), p.get("name", "")))
        by_id = {p["id"]: p for p in prods}
        sources: dict[str, dict] = {}
        for p in prods:
            if p.get("status") == "watch":
                continue
            chk = guides_mod.parse_day(p.get("checked", ""))
            p["_stale"] = bool(chk and (now.date() - chk).days > guides_mod.STALE_FACT_DAYS)
            plans = [pl for pl in (p.get("pricing") or {}).get("plans") or [] if pl.get("amount") is not None]
            p["_min_plan"] = min(plans, key=lambda pl: pl["amount"]) if plans else None
            p["_models"] = [model_by_slug[s] for s in p.get("model_slugs") or [] if s in model_by_slug]
            p["_facts"] = []
            for fname, f in guides_mod.iter_facts(p):
                if f.get("source_url"):
                    p["_facts"].append({"name": fname, "url": f["source_url"], "checked": f.get("checked", "")})
                    cur = sources.get(f["source_url"])
                    if not cur or f.get("checked", "") > cur["checked"]:
                        sources[f["source_url"]] = {"url": f["source_url"], "host": host_of(f["source_url"]), "label": source_label(f["source_url"]), "checked": f.get("checked", ""), "product": p.get("name", "")}
            p["_labels"] = {k: ENUM_LABELS[k].get(((p.get(k) or {}).get("value") if k in ("commercial_use", "availability_japan") else (p.get(k) or {}).get("ui" if k == "japanese" else "training_default")) or "unknown", "—") for k in ENUM_LABELS}
        order = {vid: i for i, vid in enumerate(guides_mod.VERDICT_ORDER)}
        verdicts = []
        for v in sorted(g.get("verdicts") or [], key=lambda v: order.get(v.get("id"), 99)):
            ev = v.get("evidence") or []
            verdicts.append({**v, "_pick": by_id.get(v.get("pick")), "_runners": [by_id[r] for r in v.get("runner_up") or [] if r in by_id], "_editorial_only": bool(ev) and all(x.get("kind") == "editorial" for x in ev)})
        names = set((g.get("related") or {}).get("tags") or [])
        for p in prods:
            names |= set(p.get("tags") or [])
            if p.get("name"):
                names.add(p["name"])
        names = {n for n in names if len(n) >= 3 or re.search(r"[ぁ-んァ-ン一-龥]", n)}
        cutoff = now - timedelta(days=90)
        recent = [a for a in arts if a["date"] >= cutoff and (names & set(a["tags"]) or any(n in a["title"] for n in names))][:8]
        manual = [art_by_path[p] for p in (g.get("related") or {}).get("articles") or [] if p in art_by_path]
        for a in manual:
            if a not in recent:
                recent.append(a)
        lr = guides_mod.parse_day(g.get("last_reviewed", "")) or now.date()
        up = guides_mod.parse_day(g.get("updated", "")) or lr
        featured = [p for p in prods if p.get("status") == "featured"]
        g.update(
            path=f"/best/{g['slug']}/",
            full_title=f"{g['title']}{edition}",
            edition=edition,
            stale=stale,
            featured=featured,
            listed=[p for p in prods if p.get("status") in ("listed", "retired")],
            verdicts_sorted=verdicts,
            recent=recent,
            sources=sorted(sources.values(), key=lambda s: (s["label"], s["host"])),
            noindex=len(featured) < 3,
            reviewed=lr,
            modified=max(lr, up),
            match_names=names,
            changelog_sorted=sorted(g.get("changelog") or [], key=lambda c: c.get("date", ""), reverse=True),
        )
        out.append(g)
    idx = guides_mod.load_index()
    rank = {s: i for i, s in enumerate(s for grp in idx.get("groups", []) for s in grp.get("guides", []))}
    out.sort(key=lambda g: rank.get(g["slug"], 99))
    return out, errors, warns


def guide_ld(g: dict) -> list[dict]:
    items = []
    for i, p in enumerate(g["featured"], 1):
        app = {"@type": "SoftwareApplication", "name": p.get("name"), "url": p.get("url"), "applicationCategory": g.get("short_name"), "publisher": {"@type": "Organization", "name": p.get("vendor", "")}}
        offers = []
        free = (p.get("pricing") or {}).get("free") or {}
        if free.get("available") is True and free.get("source_url"):
            offers.append({"@type": "Offer", "price": 0, "priceCurrency": "USD", "url": free["source_url"], "name": "無料プラン"})
        mp = p.get("_min_plan")
        if mp and mp.get("source_url"):
            offers.append({"@type": "Offer", "price": mp["amount"], "priceCurrency": mp.get("currency", "USD"), "url": mp["source_url"], "name": mp.get("name", "")})
        if offers:
            app["offers"] = offers
        items.append({"@type": "ListItem", "position": i, "item": app})
    ld = [
        {
            "@context": "https://schema.org", "@type": "WebPage", "@id": abs_url(g["path"]), "name": g["full_title"], "description": g["seo"]["description"],
            "datePublished": g.get("created") or g["updated"], "dateModified": g["modified"].isoformat(), "lastReviewed": g["reviewed"].isoformat(),
            "reviewedBy": editor_ld(), "publisher": org_ld(), "inLanguage": "ja", "about": g.get("short_name"),
            "isPartOf": {"@type": "WebSite", "@id": abs_url("/"), "name": SITE["site_name"]},
        },
        {"@context": "https://schema.org", "@type": "ItemList", "name": f"{g.get('short_name')}の比較表", "numberOfItems": len(items), "itemListElement": items},
        breadcrumb_ld([("ホーム", "/"), ("用途別AIガイド", "/best/"), (g["full_title"], g["path"])]),
    ]
    if g.get("faq"):
        ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in g["faq"]]})
    return ld


def guides_for_article(a: dict, guides: list[dict]) -> list[dict]:
    """記事のタグ・タイトルに出てくる製品の用途別ガイド（1〜2件）"""
    hits = []
    for g in guides:
        score = len(g["match_names"] & set(a["tags"])) + sum(1 for n in g["match_names"] if len(n) >= 4 and n in a["title"])
        if score:
            hits.append((score, g))
    hits.sort(key=lambda x: -x[0])
    return [g for _, g in hits[:2]]


def build(now: datetime | None = None) -> None:
    now = now or datetime.now(JST)
    arts = load_articles()
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    shutil.copytree(ROOT / "static", DIST / "assets")

    env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=select_autoescape(["html"]))
    by_cat: dict[str, list] = defaultdict(list)
    by_tag: dict[str, list] = defaultdict(list)
    by_month: dict[str, list] = defaultdict(list)
    tag_names: dict[str, str] = {}
    new_cut = now - timedelta(hours=NEW_HOURS)
    for a in arts:
        a["is_new"] = a["date"] >= new_cut
        by_cat[a["category"]].append(a)
        by_month[a["date"].strftime("%Y/%m")].append(a)
        for t in a["tag_items"]:
            by_tag[t["slug"]].append(a)
            tag_names[t["slug"]] = t["name"]
    top_tags = sorted(by_tag.items(), key=lambda kv: (-len(kv[1]), tag_names[kv[0]]))[:24]
    months = sorted(by_month.keys(), reverse=True)
    models = model_pages(arts)
    related = build_related(arts)
    guides, guide_errors, guide_warns = guide_pages(arts, models, now)
    if guide_errors:
        print("用途別ガイドのエラー:\n  " + "\n  ".join(guide_errors), file=sys.stderr)
        sys.exit(1)
    guide_index = guides_mod.load_index()
    guides_by_slug = {g["slug"]: g for g in guides}

    env.globals.update(
        site=SITE,
        cats=TAXO["categories"],
        u=u,
        abs_url=abs_url,
        fmt_dt=fmt_dt,
        fmt_date=fmt_date,
        fmt_short=fmt_short,
        v=asset_version(),
        now=now,
        year=now.year,
        top_tags=[{"slug": s, "name": tag_names[s], "count": len(v)} for s, v in top_tags],
        latest_update=arts[0]["date"] if arts else now,
        today_count=sum(1 for a in arts if a["date"].date() == now.date()),
        cat_counts={k: len(v) for k, v in by_cat.items()},
        months=[{"key": m, "label": f"{m[:4]}年{int(m[5:])}月", "count": len(by_month[m]), "path": f"/archive/{m}/"} for m in months[:12]],
        models_top=models[:6],
        guides_nav=[guides_by_slug[s] for s in guide_index.get("nav", []) if s in guides_by_slug] or guides[:6],
        has_guides=bool(guides),
        fmt_price=fmt_price,
        usd=usd,
        total_articles=len(arts),
    )

    from markupsafe import Markup

    env.filters["md"] = lambda text: Markup(render_body(text or "")[0])

    def render(tpl: str, **ctx) -> str:
        return env.get_template(tpl).render(**ctx)

    # 画像（OG兼サムネイル）
    og_stats = og.render_all(arts, CATS, DIST / "og", ROOT / ".cache" / "og")
    og.render_brand(DIST / "assets", SITE)
    if guides:
        og.render_all(
            [{"slug": f"best-{g['slug']}", "thumb_text": g["short_name"], "thumb_kicker": "用途別AIガイド", "title": g["full_title"], "date": now, "category": "guide"} for g in guides],
            {**CATS, "guide": GUIDE_CAT}, DIST / "og", ROOT / ".cache" / "og",
        )

    # 記事ページ
    for i, a in enumerate(arts):
        write(
            a["path"],
            render(
                "article.html",
                a=a,
                related=related[a["slug"]],
                guides_for=guides_for_article(a, guides),
                newer=arts[i - 1] if i > 0 else None,
                older=arts[i + 1] if i + 1 < len(arts) else None,
                ld=article_ld(a),
                canonical=a["path"],
                og_image=f"/og/{a['slug']}.png",
            ),
        )

    # トップ
    ld_home = [
        {"@context": "https://schema.org", "@type": "WebSite", "name": SITE["site_name"], "url": abs_url("/"), "inLanguage": "ja",
         "publisher": {"@id": abs_url("/#org")},
         "potentialAction": {"@type": "SearchAction", "target": abs_url("/search/?q={q}"), "query-input": "required name=q"}},
        {"@context": "https://schema.org", **org_ld()},
    ]
    per = SITE["articles_per_page"]
    write("/", render("index.html", hero=arts[:5], days=group_by_day(arts[5:per]), more=len(arts) > per, ld=ld_home, canonical="/"))

    # 一覧（全記事・カテゴリ・タグ・月別）
    def list_pages(base: str, items: list, title: str, desc: str, crumbs: list, heading: str, noindex_all: bool = False, intro: str = "") -> None:
        pages = paginate(items, per)
        for n, chunk in enumerate(pages, 1):
            path = base if n == 1 else f"{base}page/{n}/"
            write(
                path,
                render(
                    "list.html",
                    title=title if n == 1 else f"{title}（{n}ページ目）",
                    heading=heading,
                    desc=desc,
                    intro=intro,
                    days=group_by_day(chunk),
                    page=n,
                    pages=len(pages),
                    base=base,
                    canonical=path,
                    ld=[breadcrumb_ld(crumbs)] + ([itemlist_ld(chunk)] if chunk else []),
                    noindex=noindex_all or not chunk,
                ),
            )

    list_pages("/news/", arts, "最新のAIニュース一覧", SITE["description"], [("ホーム", "/"), ("ニュース一覧", "/news/")], "ニュース一覧")
    for c in TAXO["categories"]:
        items = by_cat.get(c["slug"], [])
        list_pages(
            f"/category/{c['slug']}/", items, f"{c['name']}の最新ニュース", c["desc"] + "。海外の一次情報を日本語で速報します。",
            [("ホーム", "/"), (c["name"], f"/category/{c['slug']}/")], c["name"],
        )
    for slug, items in by_tag.items():
        name = tag_names[slug]
        list_pages(
            f"/tag/{slug}/", items, f"{name}の最新ニュース・情報まとめ",
            f"{name}に関する海外の最新ニュース{len(items)}本を日本語でまとめています。公式発表・論文・海外メディアの報道をもとに、ビジネスへの影響まで解説します。",
            [("ホーム", "/"), (f"#{name}", f"/tag/{slug}/")], f"#{name}",
            noindex_all=len(items) < TAG_INDEX_MIN,
        )
    for mkey, items in by_month.items():
        label = f"{mkey[:4]}年{int(mkey[5:])}月"
        list_pages(
            f"/archive/{mkey}/", items, f"{label}のAIニュース一覧", f"{label}に公開したAIニュース{len(items)}本の一覧です。",
            [("ホーム", "/"), (label, f"/archive/{mkey}/")], f"{label}のニュース",
        )
    write("/tag/", render("tags.html", tags=sorted(({"slug": s, "name": tag_names[s], "count": len(v)} for s, v in by_tag.items()), key=lambda t: (-t["count"], t["name"])), canonical="/tag/", ld=[]))

    # AIモデル図鑑（記事データから自動更新される、長く検索されるページ）
    write("/models/", render("models.html", models=models, canonical="/models/", ld=[breadcrumb_ld([("ホーム", "/"), ("AIモデル図鑑", "/models/")])], updated=max((a["date"] for m in models for a in m["articles"]), default=now)))
    for m in models:
        write(m["path"], render("model.html", m=m, canonical=m["path"], noindex=not m["articles"], ld=[breadcrumb_ld([("ホーム", "/"), ("AIモデル図鑑", "/models/"), (m["name"], m["path"])])]))

    # 用途別AIガイド（/best/）
    if guides:
        write("/best/", render(
            "guides.html", groups=[{**grp, "items": [guides_by_slug[s] for s in grp.get("guides", []) if s in guides_by_slug]} for grp in guide_index.get("groups", [])],
            canonical="/best/", og_image="/assets/og-default.png",
            ld=[breadcrumb_ld([("ホーム", "/"), ("用途別AIガイド", "/best/")]),
                {"@context": "https://schema.org", "@type": "CollectionPage", "name": "用途別AIガイド", "url": abs_url("/best/"), "inLanguage": "ja", "publisher": org_ld(),
                 "hasPart": [{"@type": "WebPage", "name": g["full_title"], "url": abs_url(g["path"])} for g in guides]}],
        ))
        for g in guides:
            write(g["path"], render(
                "guide.html", g=g, canonical=g["path"], og_image=f"/og/best-{g['slug']}.png", noindex=g["noindex"], ld=guide_ld(g),
                related_guides=[guides_by_slug[s] for s in (g.get("related") or {}).get("guides", []) if s in guides_by_slug],
                embed=[m for m in models if m.get("status", "current") == "current"] if g.get("embed_models") else [],
            ))

    # 固定ページ
    for p in sorted(PAGES.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        m = re.match(r"---\s*\n(.*?)\n---\s*\n(.*)", text, re.S)
        meta = json.loads(m.group(1))
        body, _ = render_body(m.group(2))
        tpl = meta.get("template", "page.html")
        ld = [breadcrumb_ld([("ホーム", "/")] + [(meta["title"], meta["path"])])]
        if tpl == "editor.html":
            ld.append({"@context": "https://schema.org", "@type": "ProfilePage", "mainEntity": editor_ld()})
        write(meta["path"], render(tpl, page=meta, body=body, canonical=meta["path"], ld=ld))
    write("/search/", render("search.html", canonical="/search/", ld=[], noindex=True))
    write("/404.html", render("404.html", canonical="/404.html", ld=[], noindex=True, latest=arts[:6]))

    # 検索用インデックス・フィード・サイトマップ
    write("/search.json", json.dumps(
        [{"t": g["full_title"], "d": g["seo"]["description"], "u": u(g["path"]), "c": "用途別ガイド", "g": sorted(g["match_names"])[:12], "p": g["reviewed"].strftime("%Y/%m/%d")} for g in guides]
        + [{"t": a["title"], "d": a["description"], "u": u(a["path"]), "c": a["cat"]["name"], "g": a["tags"], "p": a["date"].strftime("%Y/%m/%d")} for a in arts[: SITE.get("search_index_max", 3000)]],
        ensure_ascii=False, separators=(",", ":"),
    ))
    write("/feed.xml", rss(arts[:40], now))
    write("/sitemap.xml", sitemap(arts, by_cat, by_tag, by_month, models, now, guides))
    write("/news-sitemap.xml", news_sitemap(arts, now))
    write("/robots.txt", robots())
    write("/llms.txt", llms(arts, models, guides))
    if SITE.get("indexnow_key"):
        write(f"/{SITE['indexnow_key']}.txt", SITE["indexnow_key"])
    write("/.nojekyll", "")

    total = sum(1 for _ in DIST.rglob("index.html"))
    print(f"ビルド完了: 記事 {len(arts)} 本・{total} ページ（画像 新規{og_stats['new']}/再利用{og_stats['cached']}）→ dist/")
    warn_quality(arts)
    for w in guide_warns:
        print(f"  注意 ガイド {w}")


def warn_quality(arts: list[dict]) -> None:
    """ビルドは止めないが、編集方針から外れているものを知らせる（記者はこれを見て直す）"""
    heads_by_day: dict[str, Counter] = defaultdict(Counter)
    for a in arts:
        heads_by_day[a["date"].strftime("%Y-%m-%d")][a["title"][:6]] += 1
    for a in arts:
        w = list(a["embed_warns"])
        if a["quote_count"] + a["x_count"] == 0:
            w.append("一次情報の引用カード（:::quote）もX投稿の埋め込みもない。公式発表の原文かX投稿を1つ以上入れる")
        if not 20 <= len(a["title"]) <= 60:
            w.append(f"titleが{len(a['title'])}字")
        if not 70 <= len(a["description"]) <= 140:
            w.append(f"descriptionが{len(a['description'])}字")
        if a["chars"] < 1200:
            w.append(f"本文が{a['chars']}字と短い")
        if a["chars"] > 3600:
            w.append(f"本文が{a['chars']}字と長い（3,000字が上限の目安）")
        if a["tag_items"] and any(t["slug"].startswith("t-") for t in a["tag_items"]):
            w.append("未登録の日本語タグ: " + ", ".join(t["name"] for t in a["tag_items"] if t["slug"].startswith("t-")))
        if "日本のビジネスへの影響" not in a["body"]:
            w.append("「日本のビジネスへの影響」の見出しがない")
        if a["primary_count"] == 0:
            w.append("一次情報（公式発表・X投稿・論文）が sources にない")
        elif a["sources"][0]["kind"] == "報道":
            w.append("sources の先頭が報道（一次情報を先頭に）")
        if a["updated"] and a["updated"] < a["date"]:
            w.append("updated が date より前")
        hit = [p for p in BANNED_PHRASES if p in re.sub(r"<[^>]+>", "", a["body"])]
        if hit:
            w.append("使わない言い回し: " + "、".join(hit))
        if heads_by_day[a["date"].strftime("%Y-%m-%d")][a["title"][:6]] > 1:
            w.append(f"同じ日の別記事とタイトル冒頭が同じ（{a['title'][:6]}…）。製品名から始めるなど変える")
        if w:
            print(f"  注意 {a['slug']}: " + " / ".join(w))


def rss(arts: list[dict], now: datetime) -> str:
    items = []
    for a in arts:
        og_url = abs_url("/og/" + a["slug"] + ".png")
        body = a["body"].replace(f'href="{BASE_PATH}/', f'href="{BASE_URL}/')
        summary = "".join(f"<li>{html.escape(s)}</li>" for s in a["summary"])
        full = f"<ul>{summary}</ul>{body}<p><a href=\"{abs_url(a['path'])}\">記事の全文と情報源はAIデジマで</a></p>"
        items.append(
            f"""<item><title>{xml_escape(a['title'])}</title><link>{abs_url(a['path'])}</link><guid isPermaLink="true">{abs_url(a['path'])}</guid>
<pubDate>{a['date'].strftime('%a, %d %b %Y %H:%M:%S %z')}</pubDate><dc:creator>{xml_escape(SITE['site_name'])}編集部</dc:creator><category>{xml_escape(a['cat']['name'])}</category>
<description>{xml_escape(a['description'])}</description><content:encoded><![CDATA[{full}]]></content:encoded>
<media:thumbnail url="{og_url}" width="1200" height="630"/><enclosure url="{og_url}" type="image/png" length="0"/></item>"""
        )
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:media="http://search.yahoo.com/mrss/"><channel>
<title>{xml_escape(SITE['site_name'])}</title><link>{abs_url('/')}</link><description>{xml_escape(SITE['tagline'])}</description><language>ja</language>
<lastBuildDate>{now.strftime('%a, %d %b %Y %H:%M:%S %z')}</lastBuildDate><atom:link href="{abs_url('/feed.xml')}" rel="self" type="application/rss+xml"/><atom:link href="https://pubsubhubbub.appspot.com/" rel="hub"/>
<image><url>{abs_url('/assets/logo-600.png')}</url><title>{xml_escape(SITE['site_name'])}</title><link>{abs_url('/')}</link></image>
{''.join(items)}
</channel></rss>
"""


def sitemap(arts: list[dict], by_cat: dict, by_tag: dict, by_month: dict, models: list[dict], now: datetime, guides: list[dict] | None = None) -> str:
    latest = arts[0]["date"] if arts else now
    urls = [(abs_url("/"), latest), (abs_url("/news/"), latest), (abs_url("/models/"), latest)]
    urls += [(abs_url(a["path"]), a["updated"] or a["date"]) for a in arts]
    urls += [(abs_url(f"/category/{c}/"), v[0]["date"]) for c, v in by_cat.items()]
    urls += [(abs_url(f"/tag/{t}/"), v[0]["date"]) for t, v in by_tag.items() if len(v) >= TAG_INDEX_MIN]
    urls += [(abs_url(f"/archive/{m}/"), v[0]["date"]) for m, v in by_month.items()]
    urls += [(abs_url(m["path"]), m["articles"][0]["date"]) for m in models if m["articles"]]
    guides = guides or []
    if guides:
        urls.append((abs_url("/best/"), max(datetime.combine(g["modified"], datetime.min.time(), JST) for g in guides)))
    urls += [(abs_url(g["path"]), datetime.combine(g["modified"], datetime.min.time(), JST)) for g in guides if not g["noindex"]]
    urls += [(abs_url(p), None) for p in ("/about/", "/about/editor/", "/privacy/")]
    body = "".join(
        f"<url><loc>{xml_escape(loc)}</loc>" + (f"<lastmod>{d.isoformat()}</lastmod>" if d else "") + "</url>" for loc, d in urls
    )
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{body}</urlset>\n'


def news_sitemap(arts: list[dict], now: datetime) -> str:
    """Googleニュース用サイトマップ（直近48時間の記事だけ）"""
    cutoff = now - timedelta(hours=SITE["news_sitemap_hours"])
    body = "".join(
        f"""<url><loc>{xml_escape(abs_url(a['path']))}</loc><news:news><news:publication><news:name>{xml_escape(SITE['site_name'])}</news:name><news:language>ja</news:language></news:publication><news:publication_date>{a['date'].isoformat()}</news:publication_date><news:title>{xml_escape(a['title'])}</news:title><news:keywords>{xml_escape(', '.join(a['tags']))}</news:keywords></news:news></url>"""
        for a in arts
        if a["date"] >= cutoff
    )
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">{body}</urlset>\n'


def robots() -> str:
    # AIの回答で引用されるのもこのメディアの流入経路なので、AIクローラーも許可する
    return f"""User-agent: *
Allow: /
Disallow: {u('/search/')}

Sitemap: {abs_url('/sitemap.xml')}
Sitemap: {abs_url('/news-sitemap.xml')}
"""


def llms(arts: list[dict], models: list[dict], guides: list[dict] | None = None) -> str:
    lines = [
        f"# {SITE['site_name']}（{SITE['site_name_en']}）",
        "",
        f"> {SITE['description']}",
        "",
        f"運営: {SITE['operator']['name']}（{SITE['operator']['url']}） / 編集長: {SITE['editor']['name']}",
        f"編集方針: {abs_url('/about/')} / 情報源の種別（公式発表・X投稿・論文・報道）を各記事の末尾に明記しています。",
        "",
        "## 最新記事",
        "",
    ]
    lines += [f"- [{a['title']}]({abs_url(a['path'])}): {a['description']}" for a in arts[:50]]
    if guides:
        lines += ["", "## 用途別AIガイド（目的別のおすすめAIと料金比較。公式ページで確認した事実と確認日つき・毎週点検）", "", f"- {abs_url('/best/')}"]
        for g in guides:
            v = g["verdicts_sorted"][0] if g["verdicts_sorted"] else None
            head = f"（{v['question']}→{v['_pick']['name']}）" if v and v.get("_pick") else ""
            lines.append(f"- [{g['full_title']}]({abs_url(g['path'])}): {g['seo']['description']}{head}")
    lines += ["", "## AIモデル図鑑（料金・仕様の比較。記事から自動更新）", "", f"- {abs_url('/models/')}"]
    lines += [f"- [{m['name']}]({abs_url(m['path'])}): {m['vendor']}" + (f"、入力${m['input_per_m']}/出力${m['output_per_m']}（100万トークン）" if m.get("input_per_m") is not None else "") for m in models[:30]]
    lines += ["", "## カテゴリ", ""]
    lines += [f"- [{c['name']}]({abs_url('/category/' + c['slug'] + '/')}): {c['desc']}" for c in TAXO["categories"]]
    return "\n".join(lines) + "\n"


def serve() -> None:
    import functools
    import http.server
    import tempfile

    # base_path 付きで確認できるよう、一時ディレクトリに dist を base_path 名でリンクして配信する
    tmp = Path(tempfile.mkdtemp())
    (tmp / BASE_PATH.strip("/")).symlink_to(DIST)
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(tmp))
    print(f"http://localhost:8000{BASE_PATH}/")
    http.server.ThreadingHTTPServer(("", 8000), handler).serve_forever()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--serve", action="store_true")
    args = ap.parse_args()
    build()
    if args.serve:
        serve()
