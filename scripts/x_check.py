#!/usr/bin/env python3
"""X投稿のURLが実在するかを確かめ、投稿者と本文を表示する（Xの公開oEmbedを使う。無料・APIキー不要）。

記事に {{x:URL}} で埋め込む前、X投稿を引用する前に必ず使う。存在しないURLを記事に書かないため。
  python3 scripts/x_check.py https://x.com/sama/status/1234567890
"""
import html
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

for url in sys.argv[1:]:
    q = urllib.parse.urlencode({"url": url, "omit_script": "true", "dnt": "true", "lang": "ja"})
    try:
        req = urllib.request.Request(f"https://publish.twitter.com/oembed?{q}", headers={"User-Agent": "Mozilla/5.0 AIDejima"})
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read())
    except urllib.error.HTTPError as e:
        print(f"NG {e.code}（存在しない・削除・非公開）: {url}")
        continue
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        print(f"確認できず（通信エラー {e}）: {url}")
        continue
    body = re.search(r"<p[^>]*>(.*?)</p>", data.get("html", ""), re.S)
    text = html.unescape(re.sub(r"<[^>]+>", "", body.group(1))) if body else ""
    date = re.findall(r">([^<>]+)</a></blockquote>", data.get("html", ""))
    print(f"OK {data.get('author_name')}（{data.get('author_url')}） {date[-1] if date else ''}\n  {text}\n  {url}")
