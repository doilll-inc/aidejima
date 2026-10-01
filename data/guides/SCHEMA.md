# data/guides/ — 用途別AIガイドのデータ定義と調査手順

`/best/<slug>/` の元データ。1ガイド＝1ファイル `data/guides/<slug>.json`。一覧と並び順は `_index.json`。設計の全体は `docs/guides-design.md`、編集ルールは `EDITORIAL.md` §7。

**このファイルを読む人**: 中身を埋める調査担当、記事のついでに直す記者（`scripts/writer_prompt.md`）、点検担当（`scripts/guide_refresh_prompt.md`）。人でもAIでも同じ。

## 0. 3つの約束

1. **事実は公式ページで確認できたものだけ書く。** 料金は公式料金ページ、商用利用は公式利用規約・FAQ、日本語対応は公式ヘルプ、日本での提供は公式の提供地域ページ。報道・比較サイト・まとめ記事・自分の記憶は出典にしない。開けなかったページの値は書かない
2. **fact には必ず `source_url` と `checked`（確認日）を付ける。** 出典のない料金・条件はビルドが止まる
3. **順位付け（今の答え）には根拠を付ける。** 第三者評価か公式の評価結果の、名前・URL・確認日・要点。根拠がなければ「編集部の判断」と明示して理由を書く。星や点数は作らない

## 1. ファイル全体

```jsonc
{
  "slug": "image-generation",            // ファイル名と同じ。URL /best/<slug>/
  "status": "draft",                     // draft=ビルドしない / published=公開
  "priority": 1,                         // 調査の順番（1が先）
  "created": "2026-09-30",               // 骨組みを作った日
  "updated": "2026-09-30",               // データを変えた日（記者・点検担当が更新）
  "last_reviewed": "2026-09-30",         // 全 fact を再確認した日（点検担当だけが更新）
  "title": "画像生成AIのおすすめと料金比較",   // 【】と年は書かない（build が【YYYY年M月版】を付ける）
  "short_name": "画像生成",              // ナビ・OG画像用（全角8字まで）
  "seo": {
    "description": "",                   // 全角90〜120字。製品名を2〜3個。年は入れない
    "keywords": ["画像生成AI", "おすすめ", "料金"]
  },
  "intro": "",                           // リード2〜3文。1文目が結論（Markdown可）
  "scope": "",                           // 何を含み、何を含まないか（1〜2文）
  "audience": ["マーケター", "デザイナー"],
  "segments": [],                        // 表の分割（任意）。{id, name, desc}
  "verdicts": [],                        // 今の答え（→ §2）
  "products": [],                        // 製品行（→ §3）
  "criteria": [],                        // 選び方（→ §4）
  "benchmarks": [],                      // 評価の根拠（→ §5）
  "faq": [],                             // {q, a} 3〜6問
  "related": { "tags": [], "guides": [], "articles": [] },   // 記事の自動連携（→ §6）
  "changelog": [],                       // 更新履歴（→ §7）
  "editor_note": "",                     // 編集長が書く欄。AIは書かない
  "embed_models": false,                 // api だけ true（/models/ の表を埋め込む）
  "research_plan": {                     // 調査メモ。表示しない。published にする前に空にする
    "candidates": [], "verdict_questions": [], "notes": ""
  }
}
```

日付はすべて `YYYY-MM-DD`（JST）。未来日は不可。

## 2. verdicts（今の答え）

```jsonc
{
  "id": "best-quality",                  // 下の標準IDから。独自IDも可（英小文字とハイフン）
  "question": "最高品質で選ぶなら",
  "pick": "midjourney",                  // products[].id
  "runner_up": ["gpt-image"],            // 次点（任意）
  "answer": "……。",                      // 1〜2文。なぜそれか。数字があれば入れる
  "evidence": [
    {
      "kind": "third_party",             // official=公式の評価結果 / third_party=第三者評価 / editorial=編集部の判断
      "name": "Artificial Analysis Text-to-Image Arena",
      "url": "https://…",                // 開いたページ
      "date": "2026-10-01",              // 開いた日
      "note": "ELOで1位（2026-10-01時点）"  // そのページで読めた要点
    }
  ]
}
```

標準ID（該当するものだけ使う。順番もこの順で）:

| id | question |
|---|---|
| `best-quality` | 最高品質で選ぶなら |
| `best-value` | コスパで選ぶなら |
| `free` | 無料で使うなら |
| `japanese` | 日本語重視なら |
| `commercial` | 商用利用（広告・納品物）なら |
| `business` | 会社で安全に使うなら（入力が学習に使われない・管理機能） |
| `developer` | APIで組み込むなら |
| `beginner` | 初めて使うなら |
| `voice` | 音声で会話するなら（chat だけ） |

ルール:
- `best-quality` の evidence は `official` か `third_party` が1つ以上必要（`editorial` だけは不可）
- `best-value`・`free`・`japanese`・`commercial`・`business` は、答えの根拠が表の fact（料金・規約）にあるので、evidence にはその fact の `source_url` を `kind: official` で入れる
- 根拠のページが第三者評価の場合、`note` にそのページで読めた順位・数値と「〜時点」を書く。順位は変わるので日付が必須
- `answer` に「最強」「圧倒的」等の煽り語は使わない。数字と根拠で書く

## 3. products（製品行）

```jsonc
{
  "id": "midjourney",                    // 英小文字とハイフン。ファイル内で一意
  "name": "Midjourney",                  // 公式表記
  "vendor": "Midjourney, Inc.",          // 提供元の公式表記
  "url": "https://www.midjourney.com/",  // 公式トップ
  "status": "featured",                  // featured=比較表 / listed=その他の選択肢 / watch=調査中（非表示） / retired=終了（取り消し線）
  "rank": 1,                             // 表の並び（小さいほど上）。同順なら name 順
  "segment": "",                         // segments[].id（任意）
  "tags": ["Midjourney"],                // 当サイトの記事タグ（記事の自動連携用。EDITORIAL の表記に合わせる）
  "model_slugs": [],                     // data/models.json の slug（/models/ へリンク）
  "latest": { "name": "Midjourney V8", "released": "2026-08-01", "source_url": "https://…", "checked": "2026-10-01" },
  "access": ["web", "discord", "api"],   // 提供形態: web / app(iOS・Android) / desktop / api / discord / ide / cli / extension
  "strengths": ["…", "…"],               // 2〜3個、各30字以内。公式ページか根拠のある評価で言えることだけ
  "weaknesses": ["…"],                   // 1〜2個。同上
  "editorial_take": "",                  // 編集部の一言（1〜2文）。根拠のない主観は書かない
  "pricing": {
    "free": { "available": true, "detail": "1日〇回まで", "source_url": "https://…/pricing", "checked": "2026-10-01" },
    "plans": [
      { "name": "Basic", "amount": 10, "currency": "USD", "per": "month", "as_shown": "$10/month（annual: $8/month）", "detail": "月200枚相当", "source_url": "https://…/pricing", "checked": "2026-10-01" }
    ],
    "usage": { "unit": "1画像", "amount": 0.04, "currency": "USD", "as_shown": "$0.04 / image", "detail": "API・標準品質", "source_url": "https://…", "checked": "2026-10-01" },
    "jpy_official": false,               // 公式ページに円建て表示があるか（あれば plans の currency を JPY にして as_shown に原文）
    "note": ""                           // 補足（年払い割引・税の扱い等）
  },
  "japanese": { "ui": "yes", "output": "yes", "note": "画像内の日本語文字は不得手（公式ヘルプに記載）", "source_url": "https://…", "checked": "2026-10-01" },
  "commercial_use": { "value": "conditional", "note": "有料プランのみ商用可（利用規約 4条）", "source_url": "https://…/terms", "checked": "2026-10-01" },
  "data_policy": { "training_default": "opt_out_available", "note": "設定で学習利用を拒否できる", "source_url": "https://…", "checked": "2026-10-01" },
  "availability_japan": { "value": "yes", "note": "", "source_url": "https://…", "checked": "2026-10-01" },
  "checked": "2026-10-01",               // この行の全 fact を最後に確認した日（点検担当が更新）
  "retired_note": ""                     // status=retired のとき、いつ・何に置き換わったか
}
```

列挙値:

| 項目 | 値 |
|---|---|
| `per` | `month` / `year` / `once` / `seat_month`（1人あたり月額）/ `credit`（クレジット制。`detail` に換算） |
| `japanese.ui` / `output` | `yes` / `partial` / `no` / `unknown` |
| `commercial_use.value` | `yes` / `conditional`（有料のみ等。`note` に条件）/ `no` / `unknown` |
| `data_policy.training_default` | `not_used`（学習に使わない）/ `opt_out_available`（既定は使うが拒否できる）/ `used`（拒否不可）/ `unknown` |
| `availability_japan.value` | `yes` / `partial`（一部機能）/ `no` / `unknown` |

ルール:
- **`unknown` は「公式ページに記載を見つけられなかった」の意味。** その場合も `source_url` に探したページ（規約やヘルプ）を入れ、`note` に「記載なし」と書く
- 料金の `amount` は税抜/税込を公式表記のままにし、`as_shown` に原文を残す。**為替換算しない**。円建てが公式にある場合は円で書く（`jpy_official: true`）
- 法人プラン（Enterprise）で価格非公開のものは `amount` を省略し `as_shown: "要問い合わせ"`
- `strengths` に「使いやすい」「高品質」のような根拠のない語を書かない。「画像内の英字テキストを正確に描く（公式発表 2026-xx-xx）」のように何で言えるかが分かる書き方にする
- 1ガイドの `featured` は **5〜10行**。それ以外は `listed`。`watch` は表に出ないので、記者が新製品を見つけたときの仮置きに使う
- Meta 系（Meta AI・Llama 等）は公式ドメインを開けない社内ルールのため、`status: "watch"` で名前と `note` だけ置く。fact は入れない

## 4. criteria（選び方）

```jsonc
{ "name": "画像内の文字（日本語）", "why": "広告バナーやサムネイルでは文字の正確さが実用性を決める", "how_to_check": "同じプロンプトで商品名を日本語で入れて出力を比べる" }
```

3〜6個。製品名を書かない（製品は表と答えに任せる）。骨組みJSONに初期案が入っている。調査で気づいた観点があれば足す。

## 5. benchmarks（評価の根拠）

```jsonc
{
  "id": "aa-t2i-arena",
  "name": "Artificial Analysis Text-to-Image Arena",
  "operator": "Artificial Analysis",
  "url": "https://…",
  "what": "人間の一対比較によるELO",
  "snapshot": "1位 〇〇、2位 △△（2026-10-01時点）",   // 開いたページで読めた要点
  "checked": "2026-10-01"
}
```

使ってよい根拠: 公式のモデルカード・システムカード・発表内の評価結果、継続運営の公開リーダーボード（例: LMArena、Artificial Analysis、SWE-bench、Scale SEAL、HELM、各 Arena）。個人ブログ・SNS の感想・アフィリエイトサイトの順位は使わない。`verdicts[].evidence` から参照する根拠は必ずここにも載せる。

## 6. related（記事との自動連携）

```jsonc
{ "tags": ["画像生成", "Midjourney", "Nano Banana"], "guides": ["video-generation", "marketing"], "articles": ["/news/20260930-xxx/"] }
```

- build.py は `tags` と各製品の `tags`・`name` を、記事の `tags`・`title` と照合し、「最近の変更」に新しい順で並べる（90日以内・8本）。`articles` は手動で必ず出したい記事
- タグ表記は `data/taxonomy.json` の `tag_slugs` と既存記事に合わせる（同じ製品に別表記を作らない）

## 7. changelog（更新履歴）

```jsonc
{ "date": "2026-10-01", "text": "Midjourney の Basic プランを $10 に更新", "article": "/news/20260930-xxx/", "by": "writer" }
```

- `by`: `researcher`（初回調査）/ `writer`（記事のついで）/ `reviewer`（点検）/ `editor`（人）
- 事実が変わったときだけ書く。点検で変更が無かった回は `last_reviewed` だけ更新して changelog に書かない
- 公開されるので読者向けの文で（「〇〇の料金を更新」「〇〇を表に追加」「〇〇を終了扱いに」）

## 8. 調査担当の手順（骨組みを埋めるとき）

対象ガイドの `research_plan` を読んでから始める。**1ガイドずつ**終わらせる（途中で止まっても中途半端なページが残らないように、`status` は最後まで `draft`）。

1. `TZ=Asia/Tokyo date` で今日の日付を確認する（`checked` に使う）
2. `research_plan.candidates` の製品ごとに、公式サイトを開いて **現行の製品名・最新モデル名** を確認する。候補は編集部の初期案なので、公式サイトで見つからない・終了している製品は外し、公式発表や `python3 scripts/list_articles.py --all` で見つかる新しい製品を足す
3. 製品ごとに次の公式ページを WebFetch で開き、読めた値だけを fact にする（`source_url` は開いたURL、`checked` は今日）:
   - 料金ページ（`/pricing` `/plans` 等）→ `pricing`
   - 利用規約・商用利用のFAQ → `commercial_use`
   - データの扱い（プライバシーポリシー・学習利用の設定ページ）→ `data_policy`
   - ヘルプの対応言語・提供地域 → `japanese` `availability_japan`
   - 最新モデルの発表ページ・変更履歴 → `latest`
   ページが開けない（403・ログイン必須）ときは WebSearch で公式ドメイン内の別URLを探す。**それでも開けなければ書かない**（推測で埋めない）
4. 評価の根拠: この用途で継続運営されている公開リーダーボードを開き、`benchmarks` に `snapshot` と `checked` を書く。公式の評価結果（モデルカード）があれば `kind: official` として使う
5. `verdicts` を標準IDの順に書く。`best-quality` は §2 の根拠ルールを守る。答えられない質問は入れない（無理に埋めない）
6. `criteria` を見直し、`faq` を3〜6問書く（答えは表の fact か根拠で裏付けられることだけ）
7. `intro`・`scope`・`seo.description` を書く。`intro` の1文目は「この用途でいま何を選ぶべきか」の結論
8. `related.tags` を既存記事のタグ表記に合わせて書き、各製品の `tags` も入れる
9. `changelog` に `{"date": 今日, "text": "初回公開", "by": "researcher"}`。`updated`・`last_reviewed` を今日に。`research_plan` を空にする（`candidates: []`、`verdict_questions: []`、`notes: ""`）
10. `status` を `published` にして `python3 build.py`。エラー・注意を直す。**published の条件**: `featured` が3行以上、`verdicts` が1つ以上、全 fact に出典と確認日
11. コミット: `feat(guides): <title> を公開`（`data/guides/<slug>.json` と、タグを足したなら `data/taxonomy.json`）。push は指示があるときだけ

やってはいけないこと: 記憶で料金を書く／報道や比較サイトを出典にする／Meta 系ドメインを開く／点数や星を作る／`editor_note` を書く／製品の良し悪しを根拠なく断定する。

## 9. 記者が記事のついでに直すとき（要点。手順は `scripts/writer_prompt.md` 7b）

- 記事で公式ページを開いて確認した fact だけ更新し、その fact の `source_url`・`checked` を今日にする
- `changelog` に記事パス付きで1行、`updated` を今日に。**`last_reviewed`・`verdicts`・製品行の `checked` は触らない**
- 新製品でガイドに行が無ければ `status: "watch"` で `id` `name` `vendor` `url` `latest` `tags` だけ足す（点検担当が評価して featured/listed にする）

## 10. 点検担当が週次で見るとき（要点。手順は `scripts/guide_refresh_prompt.md`）

- 全 fact の `source_url` を開いて値を照合し、変わっていれば更新（`checked` を今日に）。変わっていなくても `checked` を今日にする
- `benchmarks` を開き直して `snapshot`・`checked` を更新。首位が変われば `verdicts` を根拠付きで更新
- `watch` の行を評価して `featured`/`listed`/`retired` に振り分ける
- 最後に製品行の `checked` と `last_reviewed` を今日に
