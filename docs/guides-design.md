# 用途別AIガイド（/best/）設計書

作成 2026-09-30。担当分担: この設計書・`data/guides/`・`EDITORIAL.md`・`scripts/*_prompt.md`・`.github/workflows/guides.yml` は設計担当。**ページの表示（`build.py`・`templates/`・`static/`）は実装担当がこの設計書をもとに作る。** 製品データの中身は調査担当が `data/guides/SCHEMA.md` の手順で埋める。

## 0. 何を作るか（1段落）

「画像生成・動画生成・コーディング・音声・調べもの…の用途ごとに、いま何が最新で、いくらかかるのか」を答える常設ページ群。ニュース記事が「点」なら、ガイドは記事から自動で更新され続ける「面」。各ページは **目的別の答え → 比較表 → 選び方 → 評価の根拠 → 最近の変更（記事から自動）→ FAQ → 情報源** の順で、すべての事実に **確認日と出典URL（公式ページ）** が付く。「どれが一番いいか」は根拠（公式発表・第三者評価の名前と日付）付きでしか書かない。更新は「毎時の記事執筆でついでに直す」＋「毎日2本ずつの総点検で全ガイドを週1で一巡する」の2系統。

## 1. ページ一覧とURL・タイトル

URLは `/best/<slug>/`、ハブは `/best/`。`best` にした理由: 検索語「〇〇AI おすすめ」に対応する英語慣習（best-x）で短く、`/news/`・`/models/` と並べても意味が明確。

`<title>`・H1 は **`title` ＋【YYYY年M月版】** を build.py が付ける（→ §5.2。手書きしない）。

| 優先 | slug | title（build が【月版】を付ける） | 対象・境界 |
|---|---|---|---|
| 1 | `chat` | チャットAIのおすすめと料金比較（ChatGPT・Claude・Gemini など） | 汎用の対話AI。Web/アプリで使う個人〜企業プラン。音声会話モードもここ |
| 1 | `image-generation` | 画像生成AIのおすすめと料金比較 | 生成＋編集（インペイント・背景差し替え）。動画は含まない |
| 1 | `video-generation` | 動画生成AIのおすすめと料金比較 | テキスト/画像→動画、リップシンク、アバター動画 |
| 1 | `coding` | コーディングAIのおすすめと料金比較（エージェント・IDE・CLI） | コーディングエージェント・IDE補完・CLI・クラウド開発環境 |
| 1 | `research` | 調べもの・リサーチに強いAIのおすすめ：検索AIと情報の正確さの比較 | 検索AI・ディープリサーチ・引用の正確さ・ハルシネーション対策 |
| 1 | `api` | AI API（LLM）の料金比較と選び方 | プロバイダ単位（無料枠・バッチ/キャッシュ割引・日本リージョン・データ扱い）。モデル単価は `/models/` を埋め込む（→ §1.1） |
| 2 | `writing` | 文章作成AIのおすすめと料金比較（ビジネス文書・記事・メール） | 文章の生成・校正・要約。翻訳は別ページ |
| 2 | `translation` | AI翻訳のおすすめと料金比較 | 文書・Web・会話の翻訳。専用サービスと汎用LLMの両方 |
| 2 | `text-to-speech` | 音声合成・AI読み上げのおすすめと料金比較 | 読み上げ・ナレーション・音声クローン・リアルタイム音声会話API |
| 2 | `transcription` | AI文字起こし・議事録ツールのおすすめと料金比較 | 会議の文字起こし・要約・話者分離・翻訳字幕 |
| 2 | `marketing` | 広告・マーケティング向けAIのおすすめ：広告クリエイティブ・SNS・LP制作 | 広告バナー/動画CR・SNS投稿・LP・媒体側のAI機能。**独立ページにする**（このメディアの強みで、製品群が基盤モデルと異なる） |
| 3 | `slides` | AI資料作成・スライド生成のおすすめと料金比較 | スライド・提案書。日本のビジネス検索で需要が大きい |
| 3 | `local-llm` | ローカルLLM・オープンウェイトモデルのおすすめ | 手元で動かすモデルと実行環境。開発者向け |

後回しの候補（骨組みは作らない）: 音楽生成、AIエージェント／業務自動化、カスタマーサポートAI、ノート・議事録以外のメモ系。記事の蓄積と検索クエリを見て追加する。

### 1.1 `/models/`（AIモデル図鑑）との関係

- `/models/` はモデル単位の仕様カタログ（100万トークン単価・コンテキスト・提供開始日）。**モデル単価の正本は `data/models.json` だけ**。ガイドはこれを複製しない
- `/best/api/` は「選び方」のページ。行はプロバイダ（OpenAI API・Anthropic API・Gemini API・Bedrock・Azure・Mistral・DeepSeek・xAI…）で、無料枠・バッチ割引・キャッシュ割引・レート制限の段階・日本リージョン/データレジデンシー・円建て/支払い方法・入力データの学習利用の有無を持つ。ページ中ほどに `data/models.json` の `status=current` を提供元別に並べた表を埋め込み、`/models/` へリンクする（`embed_models: true`）
- 他のガイド（chat・coding 等）の製品行は `model_slugs` で `/models/<slug>/` にリンクできる
- 週次点検で `api` を点検する回は、`data/models.json` の `status=current` の単価も公式料金ページで再確認し、各モデルに `"checked": "YYYY-MM-DD"` を足す（build.py は未知のキーを無視するので追加は安全。表示に出すかは実装担当の判断）

## 2. 各ページの構成（上から順）

テンプレートは `templates/guide.html`（新規）と `templates/guides.html`（ハブ、新規）を想定。文脈変数は §4 のJSONをそのまま渡してよい（build.py で派生値を足す）。

| # | ブロック | 出どころ | 表示の要点 |
|---|---|---|---|
| 0 | パンくず | ホーム › 用途別AIガイド › ページ名 | BreadcrumbList |
| 1 | 見出しとリード | `title`＋【月版】、`intro` | H1 の下に「最終更新 M月D日 ／ 最終点検 M月D日（毎週点検）」。`intro` の1文目が結論になるよう調査担当が書く |
| 2 | **今の答え（目的別）** | `verdicts[]` | 1行1問「最高品質なら → 製品名（根拠: 第三者評価名・日付）」。`pick` の製品カードへページ内リンク。根拠が `editorial` だけの答えは「編集部の判断」と表示 |
| 3 | **比較表** | `products[]`（`status=featured`） | 列: 製品（最新モデル名）／提供元／強み／料金（無料枠・最安有料）／日本語／商用利用／確認日。各行末に「出典」トグルで fact ごとの出典URLと確認日を展開。`segments` があれば表を分割。スマホは横スクロール（`table-wrap`）か、カード縦積み（実装担当の判断） |
| 4 | その他の選択肢 | `products[]`（`status=listed`） | 名前・提供元・一言・出典だけの簡易リスト。`retired` は取り消し線＋`retired_note` |
| 5 | **選び方** | `criteria[]` | 観点ごとに「なぜ重要か」「確認方法」。ここは製品名を出さない（表と答えに任せる） |
| 6 | **評価の根拠** | `benchmarks[]` | 使った第三者評価・公式評価の一覧: 名前／運営／何を測るか／確認日時点の要点（`snapshot`）／URL |
| 7 | **最近の変更** | 自動＋`changelog[]` | (a) 記事から自動: `related.tags`・各製品の `tags`・製品名がタグかタイトルに含まれる記事を新しい順に8本（90日以内）。(b) このページの更新履歴: `changelog` を新しい順に（10件超は折りたたみ）。記事に紐づく変更は記事へリンク |
| 8 | 編集長ひとこと | `editor_note` | 記事と同じ。**人が書く欄**。空なら非表示 |
| 9 | よくある質問 | `faq[]` | 3〜6問。FAQPage 構造化データ |
| 10 | **情報源** | fact の `source_url` から自動集約＋`benchmarks[].url` | 公式ページを「公式料金」「公式利用規約」「公式ドキュメント」「公式発表」に分類し、ホスト名と確認日を添える。第三者評価は別見出し。**報道は載せない**（ガイドの事実は公式ページだけ） |
| 11 | 関連ガイド・図鑑 | `related.guides`＋`embed_models` | 隣接する用途への導線。`api` は `/models/` へ |
| 12 | 注記 | 固定文 | 「料金・仕様は変わります。表の確認日を見て、利用前に公式ページで確かめてください。当サイトはアフィリエイトリンクを使っていません」（使うようになったら書き換える） |

「—」は「公式ページで確認できていない」の意味で統一（`/models/` と同じ）。空欄にしない。

### 2.1 ハブ `/best/`

- title「用途別AIガイド：目的別のおすすめAIと料金比較（毎週点検）」
- `_index.json` の `groups` 順にカード表示: ガイド名、`summary`（1行）、「今の答え」の先頭1つ（例: 最高品質なら Midjourney V8）、最終点検日
- `status=draft` のガイドは出さない

### 2.2 記事側の変更（実装担当）

- **記事 → ガイド**: 記事のタグ・タイトルが、いずれかのガイドの `related.tags` か製品 `tags`／製品名に一致するとき、記事の「情報源」の上に「この製品の用途別ガイド: 画像生成AIのおすすめと料金比較」を1〜2件自動で出す（`_macros.html` に `guide_box`）。記者は本文でも「日本のビジネスへの影響」からガイドへ1本リンクする（EDITORIAL §7）
- **情報源の見せ方**（実装済み）: `kind=報道` の情報源は「参考にした報道（折りたたみ）」として一次情報の下に分離表示される。一次情報（公式発表・公式ドキュメント・X投稿・論文）が主、報道が従
- **引用カード等の記法**（実装済み）: `:::quote`・`{{card:}}`・`{{youtube:}}`・`{{x:}}`。X は build 時に公開 oEmbed で実在確認し、無い投稿は外して「注意」に出す。引用カードは1記事3つまで・原文2文超で「注意」。引用カードもX埋め込みも無い記事は「注意」。記者は埋め込む前に `python3 scripts/x_check.py <URL>` で確かめる。書き方ルールは EDITORIAL §2 に反映済み

## 3. SEO・内部リンク・構造化データ

### 3.1 タイトル・説明文

- `<title>`: `{title}【{YYYY}年{M}月版】 - AIデジマ`。H1 も同じ文字列。OG title も同じ
- `description`: JSON の `seo.description`（全角90〜120字、製品名を2〜3個含める。「2026年」等の年は入れない＝陳腐化防止）
- 【】の扱い: **記事タイトルの【】禁止はそのまま。ガイドだけ例外**で、build.py が付ける。理由は (1) 「おすすめ 2026」系の検索意図には月版表記が読者にとっての鮮度の合図になる、(2) 生成なので手書きの不整合・陳腐化が起きない、(3) 記事は日付が表示されるので不要だがガイドは常設なので必要。JSON の `title` に【】や年を手書きしたら build エラー（→ §5.3）

### 3.2 内部リンク

| 向き | 仕組み |
|---|---|
| 記事 → ガイド | 自動の `guide_box`（§2.2）＋記者の本文リンク |
| ガイド → 記事 | 「最近の変更」の自動一覧＋`changelog[].article` |
| ガイド → モデル図鑑 | 製品行の `model_slugs` → `/models/<slug>/`。`api` は `embed_models` で表を埋め込み |
| ガイド ↔ ガイド | `related.guides` と、ハブ |
| ナビ | `catnav` の「モデル図鑑」の隣に「用途別ガイド」（`/best/`）。フッターにも。トップページのサイドバー `models_box` の下にガイド一覧の小箱 |
| llms.txt | 「## 用途別AIガイド」節を足し、各ガイドの URL・title・今の答え（先頭）を1行で |
| sitemap | `/best/`・各 published ガイド。`lastmod = max(updated, last_reviewed)`。news-sitemap には入れない（ニュースではない） |
| 検索 | `search.json` にガイドを含める（`c: "用途別ガイド"`） |

### 3.3 構造化データ（JSON-LD、1ページに4つ）

1. `WebPage`（`@id`＝ページURL）: `name`（月版付きタイトル）、`description`、`datePublished`（`created`）、`dateModified`（`max(updated, last_reviewed)`）、`lastReviewed`（`last_reviewed`）、`reviewedBy`（`editor_ld()`）、`publisher`（`org_ld()`）、`isPartOf`（WebSite `@id`）、`inLanguage: ja`、`about`（用途名）。ハブは `CollectionPage`
2. `ItemList`（比較表）: `name`「{用途}の比較表」、`numberOfItems`、`itemListElement[]` に `ListItem(position, item)`。`item` は `SoftwareApplication`（`name`、`url`、`applicationCategory`、`publisher`＝`vendor`）。料金は **数値が公式ページで確認できた行だけ** `offers: {"@type":"Offer","price","priceCurrency","url"(=料金の source_url)}` を付ける（無料枠は `price: 0`）。`aggregateRating` は付けない（評価点を持たないため。捏造しない）
3. `FAQPage`（`faq` がある場合）
4. `BreadcrumbList`

`NewsArticle` は使わない。OG画像は `og.py` の既存スタイルで `thumb_text=short_name`、kicker「用途別AIガイド」。

### 3.4 noindex・除外

- `status=draft` → ビルドしない（sitemap・ナビ・ハブにも出さない）
- `status=published` でも `products` の `featured` が3行未満なら noindex（薄いページを検索に出さない。`/tag/` の `tag_index_min` と同じ思想）

## 4. データの形（`data/guides/<slug>.json`）

正本の定義は `data/guides/SCHEMA.md`（調査担当・記者・週次点検が読む）。ここでは表示に必要な項目を実装担当向けに要約する。

```
guide
├ slug, status(draft|published), priority(1|2|3), created, updated, last_reviewed
├ title, short_name, seo{description, keywords[]}, intro, scope, audience[]
├ segments[]{id, name, desc}                  … 表の分割（任意）
├ verdicts[]{id, question, pick(product id), runner_up[], answer, evidence[]{kind, name, url, date, note}}
├ products[]{id, name, vendor, url, status(featured|listed|watch|retired), rank, segment, tags[], model_slugs[],
│            latest{name, released, source_url, checked},
│            access[], strengths[], weaknesses[], editorial_take,
│            pricing{free{available, detail, source_url, checked},
│                    plans[]{name, amount, currency, per, as_shown, detail, source_url, checked},
│                    usage{unit, amount, currency, as_shown, detail, source_url, checked},
│                    jpy_official(bool), note},
│            japanese{ui, output, note, source_url, checked},
│            commercial_use{value, note, source_url, checked},
│            data_policy{training_default, note, source_url, checked},
│            availability_japan{value, note, source_url, checked},
│            checked, retired_note}
├ criteria[]{name, why, how_to_check}
├ benchmarks[]{id, name, operator, url, what, snapshot, checked}
├ faq[]{q, a}
├ related{tags[], guides[], articles[]}
├ changelog[]{date, text, article, by}
├ editor_note                                     … 人が書く
├ embed_models(bool)                              … api だけ true
└ research_plan{candidates[], verdict_questions[], notes}   … 調査担当のメモ。表示しない
```

fact（`{value/…, note, source_url, checked}` の形）の表示規則:

- `checked` が今日から **45日より古い行は「要再確認」印**（薄い黄）。ガイド全体は `last_reviewed` が **35日より古いと** 上部に「この情報は M月D日 に確認したものです」バナー
- `source_url` のホストは `data/taxonomy.json` の `official_domains` か製品の `url` と同じ登録ドメインであること（違えば build 警告）
- 料金は通貨をそのまま表示（`$20/月`、`¥3,000/月`）。為替換算しない。`as_shown`（公式ページの表記そのまま）をツールチップに

## 5. 最新に保つ運用

### 5.1 誰が・いつ・何を

| 系統 | 頻度 | 実行者 | やること |
|---|---|---|---|
| **毎時の記事執筆**（`publish.yml`） | gate を通った回 | 記者（Claude Opus） | 記事で確認した **料金・新モデル・新プラン・無料枠・商用条件・日本提供** を、該当ガイドの製品行に反映（確認した fact だけ `checked` と `source_url` を更新）。`changelog` に記事パス付きで1行。`updated` を更新。**`last_reviewed` と `verdicts` は触らない**（根拠を再確認していないため）。ガイドに無い新製品は `status: "watch"` で最小限の行を追加。手順は `scripts/writer_prompt.md` 7b |
| **総点検**（`guides.yml`） | **毎日 06:30 JST に2本**（`last_reviewed` が古い順）→ 全13本が約1週間で一巡 | 点検担当（Claude Opus） | 対象ガイドの全 fact を `source_url` を開いて再確認、差分を直す。ベンチマークURLを開いて `snapshot` を更新し、首位が変われば `verdicts` を根拠付きで更新。各ベンダーの公式ニュース/変更履歴で `last_reviewed` 以降の新製品・値下げを探す。最後に `last_reviewed` を今日に。手順は `scripts/guide_refresh_prompt.md` |
| 手動 | 随時 | 編集長・調査担当 | Actions の「guides」→ Run workflow で slug 指定。`editor_note` を書く。新ガイド追加は `_index.json` と骨組みJSONを作ってから調査 |
| 表示の鮮度 | 毎時 | build.py | 【月版】は build 時刻から算出（§5.2）。総点検が止まると自動で「M月D日に確認」バナーが出て陳腐化が見える |

「週1回の総点検」を「毎日2本」に分けた理由: 13ガイド×10製品×数URLを1回で開くと Claude の1実行（max-turns・タイムアウト）に収まらず途中で落ちる。小さく回して確実に一巡させる。

### 5.2 【月版】の算出

- `d = build時刻(JST) − last_reviewed` が **35日以内** → build 月（例: 10月1日のビルドで 9月28日点検なら「2026年10月版」）
- 35日超 → `last_reviewed` の月を表示し、build 警告「点検が止まっている」＋ページにバナー
- 未来の月にはならない（build 時刻の月が上限）

### 5.3 build.py の検証（実装担当）

エラー（ビルド停止）:
- 必須キー欠落（`slug` `status` `title` `short_name` `seo.description` `updated` `last_reviewed`）、`slug` とファイル名の不一致
- `title` に `【` `】` または `20\d\d` を含む
- `verdicts[].pick` が `products[].id` に無い。`products[].id` の重複
- `pricing.plans[].amount` があるのに `source_url`／`checked` が無い（**出典のない料金は載せない**）。`commercial_use`・`japanese` も同様
- `checked`／日付が `YYYY-MM-DD` でない、未来日
- `status=published` なのに `verdicts` か `products(featured)` が空

警告（ビルドは通す）:
- fact の `source_url` のホストが公式ドメインでない／製品 `url` と一致しない
- `verdicts[].evidence` が空、または `editorial` だけ
- `benchmarks[].checked`／製品 `checked` が45日超、`last_reviewed` が35日超
- `research_plan` に候補が残っている published ガイド（調査漏れ）
- `faq` が3問未満、`criteria` が3つ未満

### 5.4 ワークフロー `guides.yml`（新規、追加済み）

- `schedule: "30 21 * * *"`（= 06:30 JST 毎日）、`workflow_dispatch`（`guides`＝slug をカンマ区切り／`all`、`max_guides`）
- 対象選定は Python の数行（published のうち `last_reviewed` 昇順で `MAX_GUIDES` 本）。Claude に選ばせない
- `concurrency.group: publish` で `publish.yml` と直列化（同時 push を避ける）
- Claude 実行後に **`python3 build.py` を通ってから** `git push origin HEAD:main`。push で `publish.yml` が走り、ビルド・デプロイ・IndexNow 通知は既存の流れに乗る（`guides.yml` はデプロイしない）
- `publish.yml` は変更していない

## 6. 事実と根拠のルール（要点。正本は EDITORIAL §7 と SCHEMA.md）

1. **事実は公式ページだけ**。料金→公式料金ページ、商用利用→公式利用規約/FAQ、日本語→公式ヘルプ/対応言語一覧、日本提供→公式の提供地域ページ。報道・比較サイト・まとめ記事は fact の出典にしない
2. **行ごとに確認日と出典URL**。fact 単位で `source_url` と `checked`。開けなかったページの値は書かない（古い値を残す場合は `checked` を更新しない）
3. **「一番いい」は根拠付き**。`verdicts[].evidence` に第三者評価（LMArena・Artificial Analysis・SWE-bench など）か公式の評価結果の **名前・URL・確認日・要点** を書く。根拠が無い順位付けはしない。編集部の判断は `kind: editorial` と明示し、理由を書く
4. **記憶で埋めない**。モデル名・価格・日付は開いたページの文字列から転記（`as_shown` に原文を残す）
5. **Meta系ドメインは開かない**（社内ルール）。Meta の製品は `status: "watch"` で名前だけ置き、fact は入れない
6. **数値評価を作らない**。星・点数・aggregateRating は使わない

## 7. 実装担当への引き継ぎ（チェックリスト）

- [ ] `build.py`: `data/guides/*.json` 読み込み・検証（§5.3）・派生値（月版・stale・関連記事・出典集約・ItemList）・`/best/` と `/best/<slug>/` の書き出し・sitemap・llms.txt・search.json・`guide_box`
- [ ] `templates/guide.html` `templates/guides.html` `_macros.html`（`guide_box`・`fact_source`）、`static/style.css`（表・要再確認印・バナー）
- [ ] `base.html` のナビとフッターに「用途別ガイド」
- [ ] 記事の「情報源」で報道を「参考にした報道」に分離表示
- [ ] `og.py`: ガイド用OG（`thumb_text=short_name`、kicker「用途別AIガイド」）
- [ ] `README.md` の「ファイル」表に `data/guides/` と `scripts/guide_refresh_prompt.md`、「仕組み」に `guides.yml` を1行ずつ足す（README は設計担当の編集範囲外なので未反映）
- [ ] `data/models.json` の各モデルに `checked` を足す運用を許容（未知キー）

## 8. 決めたこと・見送ったこと

- **音声を2ページに分割**（`text-to-speech` と `transcription`）: 検索意図が別（「文字起こし」は議事録需要、「読み上げ」は制作需要）。音声会話は `chat` の答えの1つ＋`text-to-speech` のセグメント「リアルタイム音声会話API」で扱う
- **文章作成と翻訳を分割**: 「AI翻訳」は専用サービスとの比較になり製品群が違う
- **マーケ用途は独立**: メディアの強み。媒体側のAI機能（広告プラットフォームの自動生成）も行にできるよう `segments` を用意
- **エージェント／業務自動化は見送り**: 用途としての境界がまだ曖昧。`chat`・`coding` の中で扱い、記事が溜まったら独立
- **アフィリエイトリンクは使わない**（現時点）。使う場合は行に `affiliate_url` を足し、ページ末の注記を「PR」表記に変える。事実の選び方には影響させない
