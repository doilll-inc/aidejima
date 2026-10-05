# AIデジマ（AI DEJIMA）

海外のAIニュースを、日本語で最速に。— 海外に散らばるAIの一次情報（公式発表・公式ドキュメント・著名人のX投稿・論文）を毎日集め、日本のビジネスでの使いどころまで解説するニュースメディア。運営: 株式会社ドイル / 編集長: 田中智大。

- 公開URL: https://aidejima.doilll.com/（旧 https://doilll-inc.github.io/aidejima/ は自動で転送される）
- 編集方針・執筆ルール: [EDITORIAL.md](EDITORIAL.md)（人もAIも、記事を書く前に必ず読む）

## 仕組み

```
scripts/collect.py  公式サイト・RSS・Hacker News・HF Papers・X公式API（鍵があるとき）を収集 → data/candidates.json（一次情報を優遇した話題度順・既出は除外/印付け）
Claude Opus 5.5（GitHub Actions）  候補から最大2本選び、一次情報を読んで裏取りして content/articles/*.md を書く
        ↓
build.py  静的サイトを dist/ に生成（記事・カテゴリ・タグ・月別・AIモデル図鑑・RSS・sitemap・Googleニュース用sitemap・構造化データ・OG画像）
        ↓
GitHub Pages に公開 → scripts/notify.py で IndexNow と WebSub に通知
```

自動実行は `.github/workflows/publish.yml`。**1日4回（7:00・12:00・17:00・21:00 JST）**、収集して最大3本ずつ執筆し、**別の Opus が引用・転載の観点で校閲してから**公開する（1日の安全上限 `MAX_PER_DAY`。校閲の指示は `scripts/copyright_review_prompt.md`）。手動実行は Actions タブの「publish」→ Run workflow（本数・時間幅を指定可）。

用途別AIガイド（`/best/`）の点検は `.github/workflows/guides.yml`。毎日06:30 JSTに、点検日が古い順に2本ずつ公式ページを開き直して料金・条件・評価の根拠を更新する（約1週間で全ガイドを一巡）。記事を書いたときに料金や新モデルが分かれば、記者もその場でガイドを直す。

## ファイル

| パス | 役割 |
|---|---|
| `content/articles/*.md` | 記事（先頭にJSONのメタ情報、下にMarkdown本文）。URLは `/news/<ファイル名>/`。一次情報の埋め込み記法（`{{x:}}`・`:::quote`・`{{card:}}`・`{{youtube:}}`）は EDITORIAL.md §2 |
| `content/pages/*.md` | 固定ページ（編集方針・編集長プロフィール・プライバシー） |
| `data/site.json` | サイト設定（URL・編集長プロフィール・GA4・Search Console・IndexNow・タグページのnoindex閾値） |
| `data/taxonomy.json` | カテゴリ定義、日本語タグのURL用slug、情報源の種別判定（公式ドメイン一覧） |
| `data/sources.json` | 収集する海外ソースの一覧と、アクセス禁止ドメイン（Meta系。媒体を増やすならここ） |
| `data/x_watchlist.json` | X公式APIで監視する公式アカウント・著名人 |
| `data/models.json` | AIモデル図鑑（/models/）の元データ。記者が公式の料金・仕様を確認したときに更新 |
| `templates/` `static/style.css` | デザイン |
| `og.py` | OG画像・サムネイル・ロゴの自動生成（元記事の画像は使わない。16:9・4:3・1:1を出す） |
| `data/guides/*.json` | 用途別AIガイド（/best/）の元データ。事実は公式ページだけ・出典と確認日つき。定義と調査手順は `data/guides/SCHEMA.md`、設計は `docs/guides-design.md` |
| `guides.py` | ガイドデータの検証（`python3 guides.py check <slug>`）。build.py もこれでエラー判定する |
| `scripts/guide_refresh_prompt.md` | ガイド点検担当（guides.yml）への指示 |
| `scripts/x_check.py` | X投稿のURLが実在するかを無料で確かめる（埋め込む前に必ず使う） |
| `scripts/notify.py` | 公開後に IndexNow と WebSub へ通知 |

## 手元での作業

```bash
pip3 install -r requirements.txt
python3 scripts/collect.py --hours 24 --print 30   # 今の話題を見る（X は X_BEARER_TOKEN があるときだけ）
python3 scripts/collect.py --hours 24 --gate        # 速報に値する候補があるか（終了コード0=ある）
python3 build.py --serve                            # http://localhost:8000/ で確認
python3 scripts/list_articles.py                    # 既存記事の一覧
```

記事を手で足す・直すときは `content/articles/` を編集して main に push すれば自動で公開される。編集長のひとことは各記事の `editor_note` に書く（AIは書かない欄）。

## 秘密情報（GitHub Secrets）

| 名前 | 用途 |
|---|---|
| `CLAUDE_CODE_OAUTH_TOKEN` | Claude が記事を書くための認証 |
| `X_BEARER_TOKEN` | X公式API（読み取り従量課金）。未設定ならXの収集はスキップされる。値はリポジトリに置かない |

## 独自ドメインに移すとき

1. ドメインを取得し、DNSで `CNAME` を `doilll-inc.github.io` に向ける（サブドメインの場合。apex なら A レコード 185.199.108〜111.153 の4本。doilll.com のDNSは Cloudflare で、`~/sakukei/scripts/cf_dns.py add-cname` で入れられる）
2. `data/site.json` の `base_url` を `https://<ドメイン>`、`base_path` を `""` にする
3. リポジトリの Settings → Pages → Custom domain にドメインを入れる（github.io のURLは自動で新ドメインへ転送される）
