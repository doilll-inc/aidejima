#!/usr/bin/env python3
"""海外のAIニュースを集めて、まだ記事にしていない話題を「話題度」順に並べる。

出力: data/candidates.json（記事を書く側が読む候補リスト）
  - 同じ話題を複数の媒体が報じていれば1件にまとめ、also_reported_by に並べる
  - すでに記事の sources に入っているURLは候補から外す
依存: 標準ライブラリのみ（CIでも手元でもそのまま動く）

使い方:
  python3 scripts/collect.py            # 直近72時間
  python3 scripts/collect.py --hours 24 --print 20
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import email.utils
import gzip
import hashlib
import html
import json
import math
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "data" / "sources.json"
OUT = ROOT / "data" / "candidates.json"
ARTICLES = ROOT / "content" / "articles"

# ボット名のUAだと403/429を返す媒体があるため、一般的なブラウザのUAで取りに行く
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
JST = timezone(timedelta(hours=9))

AI_RE = re.compile(
    r"\b(ai|a\.i\.|llm|llms|gpt|chatgpt|openai|anthropic|claude|gemini|deepmind|copilot|mistral|llama|"
    r"qwen|deepseek|grok|xai|perplexity|midjourney|sora|veo|kling|runway|diffusion|transformer|"
    r"agent|agents|agentic|chatbot|machine learning|neural|genai|generative|inference|reasoning|"
    r"model|models|nvidia|gpu|hugging face|rag|embedding|multimodal|foundation model)\b",
    re.I,
)
# 大きな発表らしさ（新モデル・新機能・資金調達・規制）
BOOST_RE = re.compile(
    r"\b(launch|launches|launched|release|releases|released|introduc\w+|announc\w+|unveil\w*|"
    r"open[- ]?source|open weights|raises|raised|funding|valuation|acquir\w+|acquisition|"
    r"lawsuit|sues|ban|regulat\w+|act|executive order|benchmark|state[- ]of[- ]the[- ]art|sota)\b",
    re.I,
)
STOP = set(
    """a an the and or of to in on for with by from at as is are was were be been this that these those
    it its into over after before new now how why what when who will can could would should may might
    than more most about up out just not no yes you your we our they their he she his her i my me us
    says said say report reports via using use uses make makes made get gets got one two three first
    ai llm model models""".split()
)


def fetch(url: str, timeout: int = 20) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*", "Accept-Encoding": "gzip"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = r.read()
    # Content-Encoding を付けずに gzip で返してくる媒体がある（DeepMind等）
    return gzip.decompress(data) if data[:2] == b"\x1f\x8b" else data


def clean_text(s: str | None, limit: int = 400) -> str:
    if not s:
        return ""
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"\s+", " ", s).strip()
    return s[:limit]


def parse_date(s: str | None) -> datetime | None:
    if not s:
        return None
    s = s.strip()
    try:
        d = email.utils.parsedate_to_datetime(s)
        if d:
            return d if d.tzinfo else d.replace(tzinfo=timezone.utc)
    except (TypeError, ValueError):
        pass
    try:
        d = datetime.fromisoformat(s.replace("Z", "+00:00"))
        return d if d.tzinfo else d.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def norm_url(u: str) -> str:
    """utm等の計測パラメータと末尾スラッシュを落として比較用に正規化する"""
    try:
        p = urllib.parse.urlsplit(u.strip())
    except ValueError:
        return u
    q = [(k, v) for k, v in urllib.parse.parse_qsl(p.query) if not k.lower().startswith(("utm_", "ref", "fbclid", "gclid"))]
    path = p.path.rstrip("/") or "/"
    return urllib.parse.urlunsplit((p.scheme.lower(), p.netloc.lower().removeprefix("www."), path, urllib.parse.urlencode(q), ""))


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def parse_feed(data: bytes) -> list[dict]:
    root = ET.fromstring(data)
    items = []
    for el in root.iter():
        t = local(el.tag)
        if t not in ("item", "entry"):
            continue
        rec: dict = {}
        for c in el:
            ct = local(c.tag)
            if ct == "title":
                rec["title"] = clean_text("".join(c.itertext()), 300)
            elif ct == "link":
                href = c.get("href")
                rel = c.get("rel", "alternate")
                if href and rel == "alternate":
                    rec.setdefault("url", href)
                elif (c.text or "").strip():
                    rec.setdefault("url", c.text.strip())
            elif ct in ("pubDate", "published", "updated", "date") and "published" not in rec:
                rec["published"] = parse_date(c.text)
            elif ct in ("description", "summary", "content", "encoded") and "summary" not in rec:
                rec["summary"] = clean_text("".join(c.itertext()))
        if rec.get("title") and rec.get("url"):
            items.append(rec)
    return items


def collect_feed(src: dict, since: datetime) -> tuple[str, list[dict], str | None]:
    try:
        entries = parse_feed(fetch(src["url"]))
    except Exception as e:  # noqa: BLE001 — 1媒体の失敗で全体を止めない
        return src["name"], [], f"{type(e).__name__}: {e}"
    out = []
    for e in entries:
        pub = e.get("published")
        if pub and pub < since:
            continue
        text = f"{e['title']} {e.get('summary', '')}"
        if src.get("ai_only") and not AI_RE.search(text):
            continue
        out.append(
            {
                "title": e["title"],
                "url": e["url"],
                "source": src["name"],
                "source_type": src.get("type", "media"),
                "weight": src.get("weight", 1.0),
                "published": pub,
                "summary": e.get("summary", ""),
            }
        )
    return src["name"], out, None


def collect_hn(cfg: dict, since: datetime) -> tuple[str, list[dict], str | None]:
    ts = int(since.timestamp())
    url = (
        "https://hn.algolia.com/api/v1/search_by_date?tags=story&hitsPerPage=200"
        f"&numericFilters=created_at_i>{ts},points>{cfg.get('min_points', 100)}"
    )
    try:
        hits = json.loads(fetch(url))["hits"]
    except Exception as e:  # noqa: BLE001
        return "Hacker News", [], f"{type(e).__name__}: {e}"
    out = []
    for h in hits:
        title = h.get("title") or ""
        if not AI_RE.search(title):
            continue
        hn_url = f"https://news.ycombinator.com/item?id={h['objectID']}"
        out.append(
            {
                "title": title,
                "url": h.get("url") or hn_url,
                "source": "Hacker News",
                "source_type": "community",
                "weight": cfg.get("weight", 1.5),
                "published": datetime.fromtimestamp(h["created_at_i"], timezone.utc),
                "summary": "",
                "hn": {"points": h.get("points", 0), "comments": h.get("num_comments", 0), "url": hn_url},
            }
        )
    return "Hacker News", out, None


def collect_hf_papers(cfg: dict, since: datetime) -> tuple[str, list[dict], str | None]:
    try:
        papers = json.loads(fetch("https://huggingface.co/api/daily_papers?limit=50"))
    except Exception as e:  # noqa: BLE001
        return "Hugging Face Papers", [], f"{type(e).__name__}: {e}"
    papers.sort(key=lambda p: p.get("paper", {}).get("upvotes", 0), reverse=True)
    out = []
    for p in papers[: cfg.get("max", 8)]:
        paper = p.get("paper", {})
        pub = parse_date(p.get("publishedAt") or paper.get("publishedAt"))
        if pub and pub < since - timedelta(days=2):
            continue
        out.append(
            {
                "title": clean_text(paper.get("title") or p.get("title"), 300),
                "url": f"https://huggingface.co/papers/{paper.get('id')}",
                "source": "Hugging Face Papers",
                "source_type": "research",
                "weight": cfg.get("weight", 0.9),
                "published": pub,
                "summary": clean_text(paper.get("summary")),
                "upvotes": paper.get("upvotes", 0),
            }
        )
    return "Hugging Face Papers", out, None


def tokens(title: str) -> set[str]:
    words = re.findall(r"[A-Za-z0-9][A-Za-z0-9.\-+]*", title.lower())
    return {w.strip(".-") for w in words if len(w) >= 3 and w not in STOP}


def covered_urls() -> set[str]:
    """公開済み記事の sources に入っているURL（=もう書いた話題）"""
    urls: set[str] = set()
    for f in ARTICLES.glob("*.md"):
        text = f.read_text(encoding="utf-8")
        m = re.match(r"---\s*\n(.*?)\n---\s*\n", text, re.S)
        if not m:
            continue
        try:
            meta = json.loads(m.group(1))
        except json.JSONDecodeError:
            continue
        for s in meta.get("sources", []):
            if s.get("url"):
                urls.add(norm_url(s["url"]))
    return urls


def score(item: dict, now: datetime) -> float:
    pub = item.get("published") or now - timedelta(hours=12)
    age_h = max(0.0, (now - pub).total_seconds() / 3600)
    s = item["weight"] * math.exp(-age_h / 36)  # 36時間で約1/e
    if BOOST_RE.search(item["title"]):
        s += 0.6
    if "hn" in item:
        s += min(2.0, math.log10(max(item["hn"]["points"], 1)) - 1.5)
    if "upvotes" in item:
        s += min(1.0, item["upvotes"] / 100)
    return s


def cluster(items: list[dict]) -> list[dict]:
    """タイトルの単語の重なりで同じ話題をまとめる（貪欲法。媒体をまたいだ同一ニュースの検出用）"""
    items = sorted(items, key=lambda x: x["_score"], reverse=True)
    groups: list[dict] = []
    for it in items:
        tk = tokens(it["title"])
        best, best_sim = None, 0.0
        for g in groups:
            inter = len(tk & g["_tokens"])
            if inter < 2:
                continue
            sim = inter / max(1, min(len(tk), len(g["_tokens"])))
            if sim > best_sim:
                best, best_sim = g, sim
        if best is not None and best_sim >= 0.5:
            best["also_reported_by"].append({"source": it["source"], "title": it["title"], "url": it["url"]})
            best["_sources"].add(it["source"])
            if "hn" in it and "hn" not in best:
                best["hn"] = it["hn"]
            continue
        g = dict(it)
        g["also_reported_by"] = []
        g["_tokens"] = tk
        g["_sources"] = {it["source"]}
        groups.append(g)
    for g in groups:
        g["score"] = round(g["_score"] + 0.9 * (len(g["_sources"]) - 1), 3)
        g["source_count"] = len(g["_sources"])
    groups.sort(key=lambda g: g["score"], reverse=True)
    return groups


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hours", type=int, default=72)
    ap.add_argument("--limit", type=int, default=80)
    ap.add_argument("--print", type=int, default=0, dest="print_n", help="上位N件を表示")
    args = ap.parse_args()

    cfg = json.loads(SOURCES.read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc)
    since = now - timedelta(hours=args.hours)

    jobs = [lambda s=s: collect_feed(s, since) for s in cfg["feeds"]]
    jobs.append(lambda: collect_hn(cfg.get("hn", {}), since))
    jobs.append(lambda: collect_hf_papers(cfg.get("hf_papers", {}), since))

    raw: list[dict] = []
    status: dict[str, str] = {}
    with cf.ThreadPoolExecutor(max_workers=12) as ex:
        for name, got, err in ex.map(lambda j: j(), jobs):
            status[name] = f"ERROR {err}" if err else f"{len(got)}件"
            raw.extend(got)

    seen = covered_urls()
    uniq: dict[str, dict] = {}
    for it in raw:
        key = norm_url(it["url"])
        if key in seen:
            continue
        it["_score"] = score(it, now)
        if key not in uniq or uniq[key]["_score"] < it["_score"]:
            uniq[key] = it

    groups = cluster(list(uniq.values()))
    # まとめた話題のどれかのURLがもう記事になっていれば、その話題ごと外す
    groups = [g for g in groups if not any(norm_url(a["url"]) in seen for a in g["also_reported_by"])]

    out_items = []
    for g in groups[: args.limit]:
        rec = {
            "id": hashlib.sha1(norm_url(g["url"]).encode()).hexdigest()[:10],
            "title": g["title"],
            "url": g["url"],
            "source": g["source"],
            "source_type": g["source_type"],
            "published": g["published"].astimezone(JST).isoformat(timespec="minutes") if g.get("published") else None,
            "score": g["score"],
            "source_count": g["source_count"],
            "summary": g.get("summary", ""),
            "also_reported_by": g["also_reported_by"][:6],
        }
        if "hn" in g:
            rec["hn"] = g["hn"]
        out_items.append(rec)

    OUT.write_text(
        json.dumps(
            {
                "generated_at": now.astimezone(JST).isoformat(timespec="minutes"),
                "window_hours": args.hours,
                "feed_status": status,
                "items": out_items,
            },
            ensure_ascii=False,
            indent=1,
        )
        + "\n",
        encoding="utf-8",
    )
    errors = [k for k, v in status.items() if v.startswith("ERROR")]
    print(f"候補 {len(out_items)} 件（収集 {len(raw)} 件・除外済み {len(seen)} URL）→ {OUT.relative_to(ROOT)}")
    if errors:
        print("取得失敗:", ", ".join(f"{k}({status[k][6:60]})" for k in errors), file=sys.stderr)
    for it in out_items[: args.print_n]:
        more = f" +{it['source_count'] - 1}媒体" if it["source_count"] > 1 else ""
        print(f"{it['score']:5.2f} [{it['source']}{more}] {it['title']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
