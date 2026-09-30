#!/usr/bin/env python3
"""公開済み記事の一覧（新しい順）。同じ話題を二重に書かないための確認用。

  python3 scripts/list_articles.py          # 直近60本
  python3 scripts/list_articles.py --all
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ap = argparse.ArgumentParser()
ap.add_argument("--all", action="store_true")
args = ap.parse_args()

rows = []
for f in (ROOT / "content" / "articles").glob("*.md"):
    m = re.match(r"---\s*\n(.*?)\n---\s*\n", f.read_text(encoding="utf-8"), re.S)
    if not m:
        continue
    meta = json.loads(m.group(1))
    rows.append((meta.get("date", ""), f.stem, meta.get("title", ""), meta.get("tags", []), [s.get("url") for s in meta.get("sources", [])]))
rows.sort(reverse=True)
for date, slug, title, tags, urls in rows if args.all else rows[:60]:
    print(f"{date[:16]} | /news/{slug}/ | {title} | tags: {', '.join(tags)}")
print(f"（全{len(rows)}本）")
