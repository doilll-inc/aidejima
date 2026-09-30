# AIデジマ（AI DEJIMA）

海外のAIニュースを、日本語で最速に。— 海外に散らばるAIの一次情報を毎日集め、日本のビジネスでの使いどころまで解説するニュースメディア。運営: 株式会社ドイル / 編集長: 田中智大。

- 公開URL: https://doilll-inc.github.io/aidejima/
- 編集方針・執筆ルール: [EDITORIAL.md](EDITORIAL.md)（人もAIも、記事を書く前に必ず読む）

## 仕組み

```
scripts/collect.py  海外30媒体＋Hacker News＋HF Papers を収集 → data/candidates.json（話題度順・既出は除外）
        ↓
Claude（GitHub Actions・Fable 5.1、使えない回は Opus 5.5）  候補から最大2本選び、一次情報を読んで裏取りして content/articles/*.md を書く
        ↓
build.py  静的サイトを dist/ に生成（記事・カテゴリ・タグ・RSS・sitemap・Googleニュース用sitemap・構造化データ・OG画像）
        ↓
GitHub Pages に公開 → scripts/notify.py で IndexNow に通知
```

自動実行は `.github/workflows/publish.yml`。1日4回（7:30 / 12:30 / 17:30 / 22:30 JST）。手動実行は Actions タブの「publish」→ Run workflow（本数を指定可）。

## ファイル

| パス | 役割 |
|---|---|
| `content/articles/*.md` | 記事（先頭にJSONのメタ情報、下にMarkdown本文）。URLは `/news/<ファイル名>/` |
| `content/pages/*.md` | 固定ページ（編集方針・編集長プロフィール・プライバシー） |
| `data/site.json` | サイト設定（URL・編集長プロフィール・GA4・Search Console・IndexNow） |
| `data/taxonomy.json` | カテゴリ定義と日本語タグのURL用slug |
| `data/sources.json` | 収集する海外ソースの一覧（媒体を増やすならここ） |
| `templates/` `static/style.css` | デザイン |
| `og.py` | OG画像・サムネイル・ロゴの自動生成（元記事の画像は使わない） |

## 手元での作業

```bash
pip3 install -r requirements.txt
python3 scripts/collect.py --print 30   # 今の話題を見る
python3 build.py --serve                # http://localhost:8000/aidejima/ で確認
python3 scripts/list_articles.py        # 既存記事の一覧
```

記事を手で足す・直すときは `content/articles/` を編集して main に push すれば自動で公開される。編集長のひとことは各記事の `editor_note` に書く（AIは書かない欄）。

## 独自ドメインに移すとき

1. ドメインを取得し、DNSで `CNAME` を `doilll-inc.github.io` に向ける
2. `data/site.json` の `base_url` を `https://<ドメイン>`、`base_path` を `""` にする
3. リポジトリの Settings → Pages → Custom domain にドメインを入れる（github.io のURLは自動で新ドメインへ転送される）
