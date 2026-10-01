#!/usr/bin/env python3
"""海外のAIニュースを集めて、まだ記事にしていない話題を「話題度」順に並べる。

出力: data/candidates.json（記事を書く側が読む候補リスト）
  - 一次情報（公式発表・公式ドキュメント・著名人のX投稿・論文）を優遇し、報道は裏取り用に also_reported_by へ
  - 同じ話題を複数の媒体が報じていれば1件にまとめ、also_reported_by に並べる
  - すでに記事の sources に入っているURLは候補から外す。既存記事と同じ話題らしい候補には possibly_covered_by を付ける
  - 社内ルールで直接アクセス禁止のドメイン（Meta系）は収集せず、候補に混ざったら access="blocked" を付ける
依存: 標準ライブラリのみ（CIでも手元でもそのまま動く）

使い方:
  python3 scripts/collect.py                 # 直近72時間
  python3 scripts/collect.py --hours 24 --print 20
  python3 scripts/collect.py --hours 6 --gate # 速報に値する候補があれば終了コード0、なければ1（CIで執筆を起動するかの判定）
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
import os
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "data" / "sources.json"
X_WATCHLIST = ROOT / "data" / "x_watchlist.json"
OUT = ROOT / "data" / "candidates.json"
ARTICLES = ROOT / "content" / "articles"
CACHE = ROOT / ".cache"

# ボット名のUAだと403/429を返す媒体があるため、一般的なブラウザのUAで取りに行く
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
JST = timezone(timedelta(hours=9))

# AI関連の判定。強い語が1つ、または弱い語（AI以外でも使う語）が2つ以上でAI関連とみなす
AI_STRONG_RE = re.compile(
    r"\b(ai|a\.i\.|llm|llms|gpt|gpt-\d|chatgpt|openai|anthropic|claude|gemini|deepmind|copilot|mistral|llama|"
    r"qwen|deepseek|grok|xai|perplexity|midjourney|sora|veo|kling|runway|chatbot|machine learning|genai|"
    r"generative|hugging ?face|multimodal|foundation model|agentic|nvidia|large language)\b",
    re.I,
)
AI_WEAK_RE = re.compile(
    r"\b(model|models|agent|agents|neural|inference|reasoning|transformer|diffusion|gpu|gpus|rag|embedding|"
    r"benchmark|training|tokens?|prompt|prompts|hallucination|alignment|robotics?|autonomous)\b",
    re.I,
)
# 大きな発表らしさ（新モデル・新機能・資金調達・規制）
BOOST_RE = re.compile(
    r"\b(launch|launches|launched|release|releases|released|introduc\w+|announc\w+|unveil\w*|now available|"
    r"open[- ]?source|open weights|raises|raised|funding|valuation|acquir\w+|acquisition|"
    r"lawsuit|sues|ban|regulat\w+|executive order|benchmark|state[- ]of[- ]the[- ]art|sota|"
    r"pricing|price|preview|generally available|\bga\b|deprecat\w+)\b",
    re.I,
)
STOP = set(
    """a an the and or of to in on for with by from at as is are was were be been this that these those
    it its into over after before new now how why what when who will can could would should may might
    than more most about up out just not no yes you your we our they their he she his her i my me us
    says said say report reports via using use uses make makes made get gets got one two three first
    ai llm model models here today""".split()
)
# 同じ話題かどうかの判定で「それだけでは同一とみなさない」語（動詞・社名）
GENERIC_TOKENS = set(
    """launch launches launched release releases released introduces introducing introduce announces announced
    announcing unveils unveiled reveals rolls rolling out update updates adds new says plans wants
    now available preview beta official version""".split()
)
COMPANY_TOKENS = set(
    """openai google anthropic microsoft meta apple nvidia amazon aws xai mistral deepseek alibaba qwen
    perplexity hugging tesla samsung intel amd ibm oracle salesforce adobe github""".split()
)
PRIMARY_TYPES = {"primary", "expert", "x", "research"}
KIND_LABEL = {"primary": "公式発表", "x": "X投稿", "research": "論文", "expert": "著名人", "media": "報道", "marketing": "報道", "community": "コミュニティ"}


def fetch(url: str, timeout: int = 20, headers: dict | None = None) -> bytes:
    h = {"User-Agent": UA, "Accept": "*/*", "Accept-Encoding": "gzip"}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, headers=h)
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


MONTHS = {m: i for i, m in enumerate("jan feb mar apr may jun jul aug sep oct nov dec".split(), 1)}


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
        pass
    # "Sep 28, 2026" / "September 28, 2026"
    m = re.match(r"([A-Za-z]{3})[a-z]*\.? (\d{1,2}),? (\d{4})", s)
    if m and m.group(1).lower() in MONTHS:
        return datetime(int(m.group(3)), MONTHS[m.group(1).lower()], int(m.group(2)), 12, 0, tzinfo=timezone.utc)
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


def host_of(u: str) -> str:
    try:
        return urllib.parse.urlsplit(u).netloc.lower().removeprefix("www.")
    except ValueError:
        return ""


def is_blocked(u: str, blocked: list[str]) -> bool:
    h = host_of(u)
    return any(h == b or h.endswith("." + b) for b in blocked)


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


# ---------- 収集（種類ごと） ----------

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


def parse_html_list(data: bytes, src: dict) -> list[dict]:
    """RSSのない公式ページ。item_re（名前付きグループ url と body）でリンクごとに拾い、
    body 内の <time> を日付、いちばん長いテキストをタイトルにする"""
    text = data.decode("utf-8", "replace")
    items, seen = [], set()
    for m in re.finditer(src["item_re"], text, re.S):
        url = urllib.parse.urljoin(src["url"], m.group("url"))
        if url in seen:
            continue
        body = m.group("body")
        tm = re.search(r"<time[^>]*>(.*?)</time>", body, re.S)
        if not tm:
            continue  # 日付のないリンク（ナビゲーション等）は記事ではない
        body_wo_time = re.sub(r"<time[^>]*>.*?</time>", " ", body, flags=re.S)
        chunks = [c for c in (clean_text(c, 300) for c in re.split(r"<[^>]+>", body_wo_time)) if c]
        head = re.search(r"<h[1-4][^>]*>(.*?)</h[1-4]>", body_wo_time, re.S)
        title = clean_text(head.group(1), 300) if head else max(chunks, key=len, default="")
        if len(title) < 8:
            continue
        summary = max((c for c in chunks if c != title), key=len, default="")
        seen.add(url)
        items.append({"title": title, "url": url, "published": parse_date(clean_text(tm.group(1))), "summary": summary})
    return items


def parse_changelog(data: bytes, src: dict) -> list[dict]:
    """日付見出し（<h2 id=.. data-text="September 22, 2026">）ごとに1件。URLはページ#見出しID"""
    text = data.decode("utf-8", "replace")
    heads = list(re.finditer(r'<h2 id="(?P<id>[^"]+)"[^>]*data-text="(?P<date>[^"]+)"', text))
    items = []
    for i, m in enumerate(heads[:8]):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        body = clean_text(text[m.end():end], 600)
        items.append({
            "title": f"{src['name']} ({m.group('date')}): {body[:140]}",
            "url": f"{src['url']}#{m.group('id')}",
            "published": parse_date(m.group("date")),
            "summary": body,
        })
    return items


def is_ai(text: str) -> bool:
    return bool(AI_STRONG_RE.search(text)) or len(set(w.lower() for w in AI_WEAK_RE.findall(text))) >= 2


def collect_feed(src: dict, since: datetime) -> tuple[str, list[dict], str | None]:
    kind = src.get("kind", "rss")
    try:
        data = fetch(src["url"])
        if kind == "html":
            entries = parse_html_list(data, src)
        elif kind == "changelog":
            entries = parse_changelog(data, src)
        else:
            entries = parse_feed(data)
    except Exception as e:  # noqa: BLE001 — 1媒体の失敗で全体を止めない
        return src["name"], [], f"{type(e).__name__}: {e}"
    out = []
    for e in entries:
        pub = e.get("published")
        if pub and pub < since:
            continue
        text = f"{e['title']} {e.get('summary', '')}"
        if src.get("ai_only") and not is_ai(text):
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
        if not is_ai(title):
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


def collect_hn_show(cfg: dict, since: datetime) -> tuple[str, list[dict], str | None]:
    """Show HN / Launch HN（開発者が自作を公開する投稿）。活用事例（usecases）の候補。通常のHNより低いポイントでも拾う"""
    ts = int(since.timestamp())
    url = (
        "https://hn.algolia.com/api/v1/search_by_date?tags=show_hn&hitsPerPage=200"
        f"&numericFilters=created_at_i>{ts},points>{cfg.get('min_points', 40)}"
    )
    try:
        hits = json.loads(fetch(url))["hits"]
    except Exception as e:  # noqa: BLE001
        return "Show HN", [], f"{type(e).__name__}: {e}"
    out = []
    for h in hits:
        title = h.get("title") or ""
        if not is_ai(title + " " + (h.get("story_text") or "")[:400]):
            continue
        hn_url = f"https://news.ycombinator.com/item?id={h['objectID']}"
        out.append(
            {
                "title": title,
                "url": h.get("url") or hn_url,
                "source": "Show HN",
                "source_type": "builder",
                "weight": cfg.get("weight", 1.6),
                "published": datetime.fromtimestamp(h["created_at_i"], timezone.utc),
                "summary": clean_text(h.get("story_text") or ""),
                "hn": {"points": h.get("points", 0), "comments": h.get("num_comments", 0), "url": hn_url},
                "usecase": True,
            }
        )
    return "Show HN", out, None


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


def collect_x(cfg: dict, since: datetime) -> tuple[str, list[dict], str | None]:
    """X公式API v2（recent search）。X_BEARER_TOKEN が無ければ何もしない。
    読み取り件数に課金されるので、前回の since_id 以降だけ取る（.cache/x/since_id）"""
    token = os.environ.get("X_BEARER_TOKEN")
    if not token:
        return "X", [], "skipped (X_BEARER_TOKEN 未設定)"
    if not X_WATCHLIST.exists():
        return "X", [], "skipped (data/x_watchlist.json が無い)"
    accounts = json.loads(X_WATCHLIST.read_text(encoding="utf-8"))["accounts"]
    state = CACHE / "x" / "since_id"
    since_id = state.read_text().strip() if state.exists() else ""
    handles = [a["handle"] for a in accounts]
    names = {a["handle"].lower(): a["name"] for a in accounts}
    out: list[dict] = []
    newest = since_id
    # クエリは512字までなので10アカウントずつ
    for i in range(0, len(handles), 10):
        q = "(" + " OR ".join(f"from:{h}" for h in handles[i : i + 10]) + ") -is:retweet -is:reply"
        params = {
            "query": q,
            "max_results": "100",
            "tweet.fields": "created_at,public_metrics,author_id,entities",
            "expansions": "author_id",
            "user.fields": "username,name",
        }
        if since_id:
            params["since_id"] = since_id
        else:
            params["start_time"] = since.strftime("%Y-%m-%dT%H:%M:%SZ")
        url = "https://api.x.com/2/tweets/search/recent?" + urllib.parse.urlencode(params)
        try:
            data = json.loads(fetch(url, headers={"Authorization": f"Bearer {token}"}))
        except Exception as e:  # noqa: BLE001
            return "X", out, f"{type(e).__name__}: {e}"
        users = {u["id"]: u for u in data.get("includes", {}).get("users", [])}
        for t in data.get("data", []):
            u = users.get(t.get("author_id"), {})
            handle = u.get("username", "")
            likes = t.get("public_metrics", {}).get("like_count", 0)
            post_url = f"https://x.com/{handle}/status/{t['id']}"
            text = clean_text(t.get("text", ""), 500)
            # 投稿内の外部リンク（発表ページ等）があれば候補の also に付ける
            links = [
                x.get("expanded_url") for x in t.get("entities", {}).get("urls", [])
                if x.get("expanded_url") and "x.com/" not in x.get("expanded_url", "") and "t.co/" not in x.get("expanded_url", "")
            ]
            if t["id"] > newest:
                newest = t["id"]
            if likes < cfg.get("min_likes", 0):
                continue
            out.append(
                {
                    "title": f"{names.get(handle.lower(), u.get('name', handle))}: {text[:160]}",
                    "url": post_url,
                    "source": f"X @{handle}",
                    "source_type": "x",
                    "weight": cfg.get("weight", 2.0),
                    "published": parse_date(t.get("created_at")),
                    "summary": text,
                    "x": {"likes": likes, "reposts": t.get("public_metrics", {}).get("retweet_count", 0), "links": links[:3]},
                }
            )
    if newest and newest != since_id:
        state.parent.mkdir(parents=True, exist_ok=True)
        state.write_text(newest)
    return "X", out, None


# ---------- 既出判定・スコア・クラスタリング ----------

def tokens(title: str) -> set[str]:
    words = re.findall(r"[A-Za-z0-9][A-Za-z0-9.\-+]*", title.lower())
    return {w.strip(".-") for w in words if len(w) >= 3 and w not in STOP}


def similarity(a: set[str], b: set[str]) -> float:
    """タイトル語の重なり。動詞・社名だけの重なりは同一話題とみなさない"""
    inter = a & b
    strong = [t for t in inter if t not in GENERIC_TOKENS and t not in COMPANY_TOKENS]
    if len(inter) < 2 or not strong:
        return 0.0
    w = sum(0.4 if t in GENERIC_TOKENS or t in COMPANY_TOKENS else 1.0 for t in inter)
    base = min(sum(0.4 if t in GENERIC_TOKENS or t in COMPANY_TOKENS else 1.0 for t in s) for s in (a, b))
    return w / max(base, 1.0)


def covered() -> tuple[set[str], list[tuple[str, list[set[str]]]]]:
    """公開済み記事の sources のURL（=もう書いた話題）と、記事ごとの情報源タイトルの英語語（続報判定用）。
    直近30日の記事だけ見る（数千本になっても遅くならないように）"""
    urls: set[str] = set()
    titles: list[tuple[str, list[set[str]]]] = []
    recent = (datetime.now(timezone.utc) - timedelta(days=30)).strftime("%Y%m%d")
    for f in ARTICLES.glob("*.md"):
        text = f.read_text(encoding="utf-8")
        m = re.match(r"---\s*\n(.*?)\n---\s*\n", text, re.S)
        if not m:
            continue
        try:
            meta = json.loads(m.group(1))
        except json.JSONDecodeError:
            continue
        sets: list[set[str]] = []
        for s in meta.get("sources", []):
            if s.get("url"):
                urls.add(norm_url(s["url"]))
            tk = tokens(s.get("title", ""))
            if len(tk) >= 2:
                sets.append(tk)
        if f.stem[:8] >= recent:
            titles.append((f"/news/{f.stem}/", sets))
    return urls, titles


def score(item: dict, now: datetime) -> float:
    pub = item.get("published") or now - timedelta(hours=12)
    age_h = max(0.0, (now - pub).total_seconds() / 3600)
    s = item["weight"] * math.exp(-age_h / 36)  # 36時間で約1/e
    if item["source_type"] in PRIMARY_TYPES and item["weight"] >= 1.8 and age_h <= 3:
        s += 0.8  # 大手の一次情報の出たて＝速報の価値
    if BOOST_RE.search(item["title"]):
        s += 0.6
    if "hn" in item:
        s += min(2.0, math.log10(max(item["hn"]["points"], 1)) - 1.5)
    if "upvotes" in item:
        s += min(1.0, item["upvotes"] / 100)
    if "x" in item:
        s += min(1.5, math.log10(max(item["x"]["likes"], 1)) - 2)
    return s


def cluster(items: list[dict]) -> list[dict]:
    """タイトルの単語の重なりで同じ話題をまとめる（貪欲法。媒体をまたいだ同一ニュースの検出用）。
    代表は一次情報を優先し、報道は also_reported_by に回す"""
    items = sorted(items, key=lambda x: (x["source_type"] in PRIMARY_TYPES, x["_score"]), reverse=True)
    groups: list[dict] = []
    for it in items:
        tk = tokens(it["title"])
        best, best_sim = None, 0.0
        for g in groups:
            sim = similarity(tk, g["_tokens"])
            if sim > best_sim:
                best, best_sim = g, sim
        if best is not None and best_sim >= 0.5:
            best["also_reported_by"].append({"source": it["source"], "kind": KIND_LABEL.get(it["source_type"], "報道"), "title": it["title"], "url": it["url"]})
            best["_sources"].add(it["source"])
            best["_tokens"] |= tk
            best["_score"] = max(best["_score"], it["_score"])
            if "hn" in it and "hn" not in best:
                best["hn"] = it["hn"]
            continue
        g = dict(it)
        g["also_reported_by"] = []
        g["_tokens"] = set(tk)
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
    ap.add_argument("--limit", type=int, default=60)
    ap.add_argument("--print", type=int, default=0, dest="print_n", help="上位N件を表示")
    ap.add_argument("--gate", action="store_true", help="書く価値のある新しい候補があるときだけ終了コード0（CIの執筆起動判定）")
    ap.add_argument("--gate-score", type=float, default=2.6, help="--gate で「書く価値あり」とみなすスコア")
    args = ap.parse_args()

    cfg = json.loads(SOURCES.read_text(encoding="utf-8"))
    blocked = cfg.get("blocked_domains", [])
    now = datetime.now(timezone.utc)
    since = now - timedelta(hours=args.hours)

    feeds = [s for s in cfg["feeds"] if not is_blocked(s["url"], blocked)]
    jobs = [lambda s=s: collect_feed(s, since) for s in feeds]
    jobs.append(lambda: collect_hn(cfg.get("hn", {}), since))
    if cfg.get("hn_show"):
        jobs.append(lambda: collect_hn_show(cfg["hn_show"], since))
    jobs.append(lambda: collect_hf_papers(cfg.get("hf_papers", {}), since))
    jobs.append(lambda: collect_x(cfg.get("x", {}), since))

    raw: list[dict] = []
    status: dict[str, str] = {}
    with cf.ThreadPoolExecutor(max_workers=12) as ex:
        for name, got, err in ex.map(lambda j: j(), jobs):
            status[name] = f"ERROR {err}" if err and not err.startswith("skipped") else (err or f"{len(got)}件")
            raw.extend(got)

    seen, existing = covered()
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
            "kind": KIND_LABEL.get(g["source_type"], "報道"),
            "published": g["published"].astimezone(JST).isoformat(timespec="minutes") if g.get("published") else None,
            "age_hours": round((now - g["published"]).total_seconds() / 3600, 1) if g.get("published") else None,
            "score": g["score"],
            "source_count": g["source_count"],
            "summary": g.get("summary", ""),
            "also_reported_by": g["also_reported_by"][:8],
        }
        if is_blocked(g["url"], blocked):
            rec["access"] = "blocked"  # 記者は開かない。also_reported_by の報道から書く
        # 既存記事と同じ話題らしければ印を付ける（続報なら新記事ではなく追記）
        best_slug, best_sim = None, 0.0
        for slug, sets in existing:
            sim = max((similarity(g["_tokens"], tk) for tk in sets), default=0.0)
            if sim > best_sim:
                best_slug, best_sim = slug, sim
        if best_slug and best_sim >= 0.5:
            rec["possibly_covered_by"] = best_slug
        if "hn" in g:
            rec["hn"] = g["hn"]
        if "x" in g:
            rec["x"] = g["x"]
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
        flag = " [既出?]" if it.get("possibly_covered_by") else ""
        flag += " [アクセス禁止ドメイン]" if it.get("access") == "blocked" else ""
        print(f"{it['score']:5.2f} {it['kind']:<5}[{it['source']}{more}]{flag} {it['title'][:110]}")

    if args.gate:
        worthy = [it for it in out_items if it["score"] >= args.gate_score and not it.get("possibly_covered_by")]
        print(f"gate: 閾値{args.gate_score}以上の新しい候補 {len(worthy)} 件 → {'執筆する' if worthy else '今回は書かない'}")
        return 0 if worthy else 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
