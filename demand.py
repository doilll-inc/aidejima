"""検索需要（data/search_demand.json）の読み込みと、記事タグとの突き合わせ。

build.py が使う: 記事のタグから「検索される製品名」を見つけて、製品ごとのまとめページ（/tag/<slug>/）に束ね、
タイトルにその名前が無ければ注意を出す。

記者が使う: `python3 demand.py --todo` で、まだ答えていない検索語（「Claude Code 料金」など）を検索数の多い順に出す。
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).parent
DATA = ROOT / "data" / "search_demand.json"
JST = timezone(timedelta(hours=9))


def _default_slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def load(slug_fn=None) -> list[dict]:
    """トピック一覧。slug は明示があればそれ、無ければ build の tag_slug と同じ規則で作る（同名タグのページに束ねるため）"""
    if not DATA.exists():
        return []
    slug_fn = slug_fn or _default_slug
    topics = []
    for t in json.loads(DATA.read_text(encoding="utf-8"))["topics"]:
        topics.append({
            **t,
            "slug": t.get("slug") or slug_fn(t["name"]),
            "kind": t.get("kind", "product"),
            "_names": {t["name"].lower(), *(a.lower() for a in t.get("also", []))},
        })
    return topics


def matches(topic: dict, tag: str) -> bool:
    """タグがこの製品のものか。同名・別名のほか、名前で始まる版名（Nano Banana 2.1・Qwen3.8・Claude Opus 5.5）も含める"""
    t = tag.lower().strip()
    for n in topic["_names"]:
        if t == n or t.startswith(n + " ") or (t.startswith(n) and len(t) > len(n) and t[len(n)].isdigit()):
            return True
    return False


def topics_for(tags: list[str], topics: list[dict]) -> list[tuple[dict, int]]:
    """記事のタグに当たるトピックと、最初に当たったタグの位置（0始まり。小さいほど記事の主役）"""
    out = []
    for tp in topics:
        idx = next((i for i, tag in enumerate(tags) if matches(tp, tag)), None)
        if idx is not None:
            out.append((tp, idx))
    return out


def main_topic(tags: list[str], topics: list[dict], within: int = 2) -> dict | None:
    """記事の主役の製品（先頭 within 個のタグで最初に当たる製品。同じ位置なら名前の長い＝具体的なほう）。社名は除く"""
    hits = [(tp, i) for tp, i in topics_for(tags, topics) if i < within and tp["kind"] != "company"]
    if not hits:
        return None
    return min(hits, key=lambda h: (h[1], -len(h[0]["name"])))[0]


def title_has(title: str, name: str) -> bool:
    norm = lambda s: re.sub(r"\s+", "", s.lower())  # noqa: E731
    return norm(name) in norm(title)


def _read_articles() -> list[dict]:
    arts = []
    for p in sorted((ROOT / "content" / "articles").glob("*.md")):
        m = re.match(r"---\s*\n(.*?)\n---", p.read_text(encoding="utf-8"), re.S)
        if not m:
            continue
        try:
            meta = json.loads(m.group(1))
        except json.JSONDecodeError:
            continue
        arts.append({**meta, "slug": p.stem})
    return arts


def todo(limit: int = 15) -> None:
    topics = load()
    arts = _read_articles()
    today = datetime.now(JST).strftime("%Y%m%d")
    howto_today = [a["slug"] for a in arts if a.get("format") == "howto" and a["slug"].startswith(today)]
    print(f"今日（{today}）の「使い方・料金」型の記事: " + ("あり " + ", ".join(howto_today) if howto_today else "まだない"))

    by_topic = {tp["slug"]: [a for a in arts if topics_for(a.get("tags", []), [tp])] for tp in topics}
    rows = []
    for tp in topics:
        for word, vol in (tp.get("queries") or {}).items():
            done = [a["slug"] for a in by_topic[tp["slug"]] if title_has(a.get("title", ""), word)]
            if not done:
                rows.append((vol, tp, word))
    rows.sort(key=lambda r: -r[0])
    print(f"\nまだ答えていない検索語（月間検索数の多い順・上位{limit}）:")
    for vol, tp, word in rows[:limit]:
        n = len(by_topic[tp["slug"]])
        print(f"  {tp['name']} {word}\t月{vol:,}回\t（{tp['name']}の記事 {n}本）")

    empty = [tp for tp in topics if tp["kind"] != "company" and not by_topic[tp["slug"]]]
    empty.sort(key=lambda t: -t["volume"])
    print("\n記事が1本もない製品（月間検索数の多い順・新機能や料金の変更が候補にあれば優先）:")
    print("  " + "、".join(f"{t['name']}（月{t['volume']:,}）" for t in empty[:limit]))


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--todo", action="store_true", help="まだ答えていない検索語と、記事のない製品を出す")
    ap.add_argument("--limit", type=int, default=15)
    args = ap.parse_args(argv)
    if args.todo:
        todo(args.limit)
        return 0
    for tp in load():
        print(f"{tp['name']}\t{tp['volume']:,}\t/tag/{tp['slug']}/")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
