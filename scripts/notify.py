#!/usr/bin/env python3
"""新しく公開・更新した記事のURLを IndexNow（Bing・Yandex等）に通知し、RSSの更新を WebSub ハブに知らせる。

直近 --hours 時間以内に公開・更新された記事と、トップ・新着一覧を送る。
IndexNow は同じURLを何度送っても問題ない。キーは data/site.json の indexnow_key（公開前提の値）。
WebSub（pubsubhubbub.appspot.com）に ping すると、購読しているフィードリーダーやニュースアグリゲータが即座にRSSを取りに来る。
"""
import argparse
import json
import re
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = json.loads((ROOT / "data" / "site.json").read_text(encoding="utf-8"))

ap = argparse.ArgumentParser()
ap.add_argument("--hours", type=float, default=6)
args = ap.parse_args()

base = SITE["base_url"].rstrip("/")
cutoff = datetime.now(timezone.utc) - timedelta(hours=args.hours)
urls = [f"{base}/", f"{base}/news/"]
for f in (ROOT / "content" / "articles").glob("*.md"):
    m = re.match(r"---\s*\n(.*?)\n---\s*\n", f.read_text(encoding="utf-8"), re.S)
    if not m:
        continue
    meta = json.loads(m.group(1))
    latest = max(datetime.fromisoformat(d) for d in (meta.get("date"), meta.get("updated")) if d)
    if latest >= cutoff:
        urls.append(f"{base}/news/{f.stem}/")

# WebSub: RSS が更新されたことをハブに知らせる（無料・登録不要）
try:
    body = urllib.parse.urlencode({"hub.mode": "publish", "hub.url": f"{base}/feed.xml"}).encode()
    req = urllib.request.Request("https://pubsubhubbub.appspot.com/", data=body, headers={"Content-Type": "application/x-www-form-urlencoded"})
    with urllib.request.urlopen(req, timeout=20) as r:
        print(f"WebSub {r.status}")
except Exception as e:  # noqa: BLE001
    print(f"WebSub 失敗: {e}")

key = SITE.get("indexnow_key")
if not key:
    raise SystemExit("indexnow_key が未設定なのでスキップ")

host = base.split("://", 1)[1].split("/", 1)[0]
body = json.dumps({"host": host, "key": key, "keyLocation": f"{base}/{key}.txt", "urlList": urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, headers={"Content-Type": "application/json; charset=utf-8"})
try:
    with urllib.request.urlopen(req, timeout=20) as r:
        print(f"IndexNow {r.status}: {len(urls)} URL")
except urllib.error.HTTPError as e:
    # 422 等はキー確認前（初回デプロイ直後）に起こりうる。公開を止めるほどではないので警告だけ
    print(f"IndexNow {e.code}: {e.read()[:200]!r}")
