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
import math
import re
import shutil
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

import og

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
CONTENT = ROOT / "content" / "articles"
PAGES = ROOT / "content" / "pages"
JST = timezone(timedelta(hours=9))
WEEKDAYS = "月火水木金土日"
REQUIRED = ("title", "description", "date", "category", "tags", "summary", "sources")

SITE = json.loads((ROOT / "data" / "site.json").read_text(encoding="utf-8"))
TAXO = json.loads((ROOT / "data" / "taxonomy.json").read_text(encoding="utf-8"))
CATS = {c["slug"]: c for c in TAXO["categories"]}
BASE_PATH = SITE["base_path"].rstrip("/")
BASE_URL = SITE["base_url"].rstrip("/")


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


def fmt_ago(d: datetime, now: datetime) -> str:
    mins = int((now - d).total_seconds() // 60)
    if mins < 60:
        return f"{max(mins, 1)}分前"
    if mins < 60 * 24:
        return f"{mins // 60}時間前"
    return f"{d.month}月{d.day}日"


# ---------- 記事の読み込み ----------

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
    if errs:
        return None, errs

    slug = path.stem
    body_md = m.group(2).strip()
    body_html, toc = render_body(body_md)
    updated = datetime.fromisoformat(meta["updated"]) if meta.get("updated") else None
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
        "chars": len(re.sub(r"\s", "", re.sub(r"<[^>]+>", "", body_html))),
        "thumb_text": meta.get("thumb_text") or meta["tags"][0],
        "publishers": list(dict.fromkeys(s.get("publisher", "") for s in meta["sources"] if s.get("publisher"))),
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


def related(a: dict, arts: list[dict], n: int = 4) -> list[dict]:
    tags = set(a["tags"])
    scored = []
    for b in arts:
        if b is a:
            continue
        s = 2.0 * len(tags & set(b["tags"])) + (1.0 if b["category"] == a["category"] else 0)
        if s <= 0:
            continue
        days = abs((a["date"] - b["date"]).total_seconds()) / 86400
        scored.append((s - 0.05 * days, b))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [b for _, b in scored[:n]]


# ---------- 構造化データ ----------

def org_ld() -> dict:
    return {
        "@type": "NewsMediaOrganization",
        "@id": abs_url("/#org"),
        "name": SITE["site_name"],
        "alternateName": SITE["site_name_en"],
        "url": abs_url("/"),
        "logo": {"@type": "ImageObject", "url": abs_url("/assets/logo-600.png"), "width": 600, "height": 120},
        "parentOrganization": {"@type": "Organization", "name": SITE["operator"]["name"], "url": SITE["operator"]["url"]},
        "publishingPrinciples": abs_url("/about/#policy"),
        "correctionsPolicy": abs_url("/about/#corrections"),
    }


def editor_ld() -> dict:
    e = SITE["editor"]
    return {
        "@type": "Person",
        "@id": abs_url("/about/editor/#person"),
        "name": e["name"],
        "alternateName": e["name_en"],
        "jobTitle": e["title"],
        "url": abs_url("/about/editor/"),
        "worksFor": {"@type": "Organization", "name": SITE["operator"]["name"], "url": SITE["operator"]["url"]},
        "alumniOf": {"@type": "CollegeOrUniversity", "name": "東京大学"},
        "sameAs": e["same_as"],
    }


def article_ld(a: dict) -> list[dict]:
    img = abs_url(f"/og/{a['slug']}.png")
    return [
        {
            "@context": "https://schema.org",
            "@type": "NewsArticle",
            "headline": a["title"],
            "description": a["description"],
            "image": [img],
            "datePublished": a["date"].isoformat(),
            "dateModified": (a["updated"] or a["date"]).isoformat(),
            "author": {"@type": "Organization", "name": f"{SITE['site_name']}編集部", "url": abs_url("/about/")},
            "editor": editor_ld(),
            "publisher": org_ld(),
            "mainEntityOfPage": abs_url(a["path"]),
            "articleSection": a["cat"]["name"],
            "keywords": a["tags"],
            "inLanguage": "ja",
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
    tag_names: dict[str, str] = {}
    for a in arts:
        by_cat[a["category"]].append(a)
        for t in a["tag_items"]:
            by_tag[t["slug"]].append(a)
            tag_names[t["slug"]] = t["name"]
    top_tags = sorted(by_tag.items(), key=lambda kv: (-len(kv[1]), tag_names[kv[0]]))[:24]

    env.globals.update(
        site=SITE,
        cats=TAXO["categories"],
        u=u,
        abs_url=abs_url,
        fmt_dt=fmt_dt,
        fmt_date=fmt_date,
        ago=lambda d: fmt_ago(d, now),
        v=asset_version(),
        now=now,
        year=now.year,
        top_tags=[{"slug": s, "name": tag_names[s], "count": len(v)} for s, v in top_tags],
        latest_update=arts[0]["date"] if arts else now,
        cat_counts={k: len(v) for k, v in by_cat.items()},
    )

    def render(tpl: str, **ctx) -> str:
        return env.get_template(tpl).render(**ctx)

    # 画像（OG兼サムネイル）
    og_stats = og.render_all(arts, CATS, DIST / "og", ROOT / ".cache" / "og")
    og.render_brand(DIST / "assets", SITE)

    # 記事ページ
    for i, a in enumerate(arts):
        write(
            a["path"],
            render(
                "article.html",
                a=a,
                related=related(a, arts),
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

    # 一覧（全記事・カテゴリ・タグ）
    def list_pages(base: str, items: list, title: str, desc: str, crumbs: list, heading: str) -> None:
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
                    days=group_by_day(chunk),
                    page=n,
                    pages=len(pages),
                    base=base,
                    canonical=path,
                    ld=[breadcrumb_ld(crumbs)],
                    noindex=not chunk,
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
            f"{name}に関する海外の最新ニュースを日本語でまとめています。公式発表・論文・海外メディアの報道をもとに、ビジネスへの影響まで解説します。",
            [("ホーム", "/"), (f"#{name}", f"/tag/{slug}/")], f"#{name}",
        )
    write("/tag/", render("tags.html", tags=sorted(({"slug": s, "name": tag_names[s], "count": len(v)} for s, v in by_tag.items()), key=lambda t: (-t["count"], t["name"])), canonical="/tag/", ld=[]))

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
        [{"t": a["title"], "d": a["description"], "u": u(a["path"]), "c": a["cat"]["name"], "g": a["tags"], "p": a["date"].strftime("%Y/%m/%d")} for a in arts],
        ensure_ascii=False, separators=(",", ":"),
    ))
    write("/feed.xml", rss(arts[:40], now))
    write("/sitemap.xml", sitemap(arts, by_cat, by_tag, now))
    write("/news-sitemap.xml", news_sitemap(arts, now))
    write("/robots.txt", robots())
    write("/llms.txt", llms(arts))
    if SITE.get("indexnow_key"):
        write(f"/{SITE['indexnow_key']}.txt", SITE["indexnow_key"])
    write("/.nojekyll", "")

    total = sum(1 for _ in DIST.rglob("index.html"))
    print(f"ビルド完了: 記事 {len(arts)} 本・{total} ページ（画像 新規{og_stats['new']}/再利用{og_stats['cached']}）→ dist/")
    warn_quality(arts)


def warn_quality(arts: list[dict]) -> None:
    """ビルドは止めないが、編集方針から外れているものを知らせる"""
    for a in arts:
        w = []
        if not 20 <= len(a["title"]) <= 60:
            w.append(f"titleが{len(a['title'])}字")
        if not 70 <= len(a["description"]) <= 140:
            w.append(f"descriptionが{len(a['description'])}字")
        if a["chars"] < 1200:
            w.append(f"本文が{a['chars']}字と短い")
        if a["tag_items"] and any(t["slug"].startswith("t-") for t in a["tag_items"]):
            w.append("未登録の日本語タグ: " + ", ".join(t["name"] for t in a["tag_items"] if t["slug"].startswith("t-")))
        if "日本のビジネスへの影響" not in a["body"]:
            w.append("「日本のビジネスへの影響」の見出しがない")
        if w:
            print(f"  注意 {a['slug']}: " + " / ".join(w))


def rss(arts: list[dict], now: datetime) -> str:
    items = []
    for a in arts:
        items.append(
            f"""<item><title>{xml_escape(a['title'])}</title><link>{abs_url(a['path'])}</link><guid isPermaLink="true">{abs_url(a['path'])}</guid>
<pubDate>{a['date'].strftime('%a, %d %b %Y %H:%M:%S %z')}</pubDate><category>{xml_escape(a['cat']['name'])}</category>
<description>{xml_escape(a['description'])}</description><enclosure url="{abs_url('/og/' + a['slug'] + '.png')}" type="image/png" length="0"/></item>"""
        )
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel>
<title>{xml_escape(SITE['site_name'])}</title><link>{abs_url('/')}</link><description>{xml_escape(SITE['tagline'])}</description><language>ja</language>
<lastBuildDate>{now.strftime('%a, %d %b %Y %H:%M:%S %z')}</lastBuildDate><atom:link href="{abs_url('/feed.xml')}" rel="self" type="application/rss+xml"/>
{''.join(items)}
</channel></rss>
"""


def sitemap(arts: list[dict], by_cat: dict, by_tag: dict, now: datetime) -> str:
    urls = [(abs_url("/"), now), (abs_url("/news/"), now)]
    urls += [(abs_url(a["path"]), a["updated"] or a["date"]) for a in arts]
    urls += [(abs_url(f"/category/{c}/"), v[0]["date"]) for c, v in by_cat.items()]
    urls += [(abs_url(f"/tag/{t}/"), v[0]["date"]) for t, v in by_tag.items() if len(v) >= 2]
    urls += [(abs_url(p), None) for p in ("/about/", "/about/editor/", "/privacy/")]
    body = "".join(
        f"<url><loc>{xml_escape(loc)}</loc>" + (f"<lastmod>{d.isoformat()}</lastmod>" if d else "") + "</url>" for loc, d in urls
    )
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{body}</urlset>\n'


def news_sitemap(arts: list[dict], now: datetime) -> str:
    """Googleニュース用サイトマップ（直近48時間の記事だけ）"""
    cutoff = now - timedelta(hours=SITE["news_sitemap_hours"])
    body = "".join(
        f"""<url><loc>{xml_escape(abs_url(a['path']))}</loc><news:news><news:publication><news:name>{xml_escape(SITE['site_name'])}</news:name><news:language>ja</news:language></news:publication><news:publication_date>{a['date'].isoformat()}</news:publication_date><news:title>{xml_escape(a['title'])}</news:title></news:news></url>"""
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


def llms(arts: list[dict]) -> str:
    lines = [
        f"# {SITE['site_name']}（{SITE['site_name_en']}）",
        "",
        f"> {SITE['description']}",
        "",
        f"運営: {SITE['operator']['name']}（{SITE['operator']['url']}） / 編集長: {SITE['editor']['name']}",
        f"編集方針: {abs_url('/about/')}",
        "",
        "## 最新記事",
        "",
    ]
    lines += [f"- [{a['title']}]({abs_url(a['path'])}): {a['description']}" for a in arts[:50]]
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
