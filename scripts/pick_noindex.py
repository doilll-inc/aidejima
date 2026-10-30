#!/usr/bin/env python3
"""検索に載せないページ（data/noindex.json）を、Search Console の実データから選ぶ。

2026-10-22〜23 にサイトごと Google の登録から外れた（トップ・/best/・/news/ が「クロール済み - インデックス未登録」）。
1日12本の量産と見られた見立てなので、検索で読まれた実績のあるページだけを残し、ほかは noindex,follow にする
（サイト内のリンクと読む人への表示はそのまま）。

  残す: ニュース記事・タグ・月別アーカイブは、落ちる前（9/25〜10/20）の表示が1回以上
        トップ・ニュース一覧・カテゴリ・用途別ガイド・モデル図鑑・固定ページは全部残す
  外す: それ以外のニュース記事・タグ・月別アーカイブ（10/21 以降の記事も、実績が無いので外す）

  python3 scripts/pick_noindex.py           data/noindex.json を書き直す
  python3 scripts/pick_noindex.py --dry-run  件数だけ出す

認証: ~/.sakukei-google-token.json（refresh_token）と ~/.gmail-mcp/gcp-oauth.keys.json（サクッと計算と共通）
"""
import argparse
import json
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKEN = Path.home() / ".sakukei-google-token.json"
KEYS = Path.home() / ".gmail-mcp/gcp-oauth.keys.json"
START, END = "2026-09-25", "2026-10-20"  # 登録から外れる前
JUDGED = ("news", "tag", "archive")  # 実績で決める区分。ほかは全部残す


def access_token() -> str:
    tok = json.loads(TOKEN.read_text())
    keys = json.loads(KEYS.read_text())["installed"]
    data = urllib.parse.urlencode({"client_id": keys["client_id"], "client_secret": keys["client_secret"],
                                   "refresh_token": tok["refresh_token"], "grant_type": "refresh_token"}).encode()
    with urllib.request.urlopen(urllib.request.Request("https://oauth2.googleapis.com/token", data=data), timeout=30) as r:
        return json.load(r)["access_token"]


def impressions(site: str) -> dict[str, int]:
    url = f"https://www.googleapis.com/webmasters/v3/sites/{urllib.parse.quote(site + '/', safe='')}/searchAnalytics/query"
    body = {"startDate": START, "endDate": END, "dimensions": ["page"], "rowLimit": 5000}
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST",
                                 headers={"Authorization": f"Bearer {access_token()}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return {row["keys"][0].replace(site, ""): int(row["impressions"]) for row in json.load(r).get("rows", [])}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    site = json.loads((ROOT / "data/site.json").read_text())["base_url"].rstrip("/")
    imp = impressions(site)

    # いまのページの一覧はサイトマップから取る（noindex の一覧を外して作り直す）
    noindex_file = ROOT / "data/noindex.json"
    saved = noindex_file.read_text() if noindex_file.exists() else None
    noindex_file.unlink(missing_ok=True)
    try:
        subprocess.run([sys.executable, "build.py"], cwd=ROOT, check=True, capture_output=True)
    finally:
        if saved is not None:
            noindex_file.write_text(saved)
    paths = [re.sub(r"^https?://[^/]+", "", u) for u in re.findall(r"<loc>(.*?)</loc>", (ROOT / "dist/sitemap.xml").read_text())]

    out, kept = [], 0
    for p in paths:
        seg = p.strip("/").split("/")
        if len(seg) != 2 or seg[0] not in JUDGED:
            continue
        if imp.get(p, 0) >= 1:
            kept += 1
        else:
            out.append(p)

    print(f"ページ {len(paths)}・外す {len(out)}・残す（ニュース・タグ・月別） {kept}")
    if not args.dry_run:
        noindex_file.write_text(json.dumps({
            "note": f"検索に載せないページ。scripts/pick_noindex.py が {START}〜{END} の表示回数で選んだ（ニュース記事・タグ・月別アーカイブで表示0回）",
            "paths": sorted(out),
        }, ensure_ascii=False, indent=1) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
