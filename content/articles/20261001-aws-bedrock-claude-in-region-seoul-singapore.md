---
{
  "title": "Amazon BedrockのClaude、ソウルとシンガポールで推論を国内完結に",
  "description": "AWSはAmazon BedrockでClaude Opus 5などをソウルとシンガポールのリージョン内だけで処理できるようにした。東京でこの方式に対応するClaudeは2モデルで、最新のOpus 5.5は日本国内の連携方式で使える。",
  "date": "2026-10-01T15:40:00+09:00",
  "updated": "2026-10-01T18:51:00+09:00",
  "category": "dev",
  "tags": ["AWS", "Amazon Bedrock", "Anthropic", "クラウド", "個人情報", "API"],
  "summary": [
    "Amazon BedrockでClaude Opus 5とSonnet 5がソウル、Sonnet 5がシンガポールの中だけで処理可能に",
    "リージョン内推論は処理を他のリージョンに回さず、料金はそのリージョンの標準オンデマンド料金になる",
    "東京でリージョン内推論に対応するClaudeはOpus 4.8とHaiku 4.5で、Opus 5.5は国内連携方式で使える"
  ],
  "sources": [
    {"title": "Introducing Anthropic models on Amazon Bedrock for in-region inference in Seoul and Singapore", "publisher": "AWS", "url": "https://aws.amazon.com/blogs/machine-learning/introducing-anthropic-models-on-amazon-bedrock-for-in-region-inference-in-seoul-and-singapore/", "kind": "公式発表"},
    {"title": "Regional availability（Amazon Bedrock User Guide）", "publisher": "AWS", "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html", "kind": "公式ドキュメント"},
    {"title": "Claude Opus 5.5（Amazon Bedrock model card）", "publisher": "AWS", "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-opus-5-5.html", "kind": "公式ドキュメント"},
    {"title": "Claude Opus 5（Amazon Bedrock model card）", "publisher": "AWS", "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-opus-5.html", "kind": "公式ドキュメント"},
    {"title": "Newsroom", "publisher": "Anthropic", "url": "https://www.anthropic.com/news"}
  ],
  "thumb_text": "Amazon Bedrock",
  "share_text": "Amazon BedrockのClaudeがソウルとシンガポールでリージョン内推論に対応。東京でこの方式に対応するのはOpus 4.8とHaiku 4.5",
  "editor_note": ""
}
---
AWSは現地時間9月29日、Amazon BedrockでAnthropicのClaude Opus 5とClaude Sonnet 5をソウル・リージョン、Claude Sonnet 5をシンガポール・リージョンの「リージョン内推論」で使えるようにしたと公式ブログで発表しました。入力も出力も、呼び出したリージョンの中だけで処理されます。日本の東京・大阪リージョンでは、この2モデルは世界中のリージョンに処理を振り分ける方式でしか使えません。

## 何が発表されたか

リージョン内推論（in-region inference）とは、推論のリクエストを利用者が指定した1つのAWSリージョンだけで処理する方式です。AWSは、韓国やシンガポールで金融・医療・公共分野のようにデータを国内で処理する必要がある組織を想定しています。

:::quote https://aws.amazon.com/blogs/machine-learning/introducing-anthropic-models-on-amazon-bedrock-for-in-region-inference-in-seoul-and-singapore/ | AWS公式ブログ「Introducing Anthropic models on Amazon Bedrock for in-region inference in Seoul and Singapore」
> Amazon Bedrock processes inference requests and data within the Region you call. The processing does not leave the Region.
Amazon Bedrockは、推論リクエストとデータを呼び出したリージョンの中で処理します。処理がリージョンの外に出ることはありません。
:::

| リージョン | 対象モデル |
|---|---|
| ソウル（ap-northeast-2） | Claude Opus 5、Claude Sonnet 5 |
| シンガポール（ap-southeast-1） | Claude Sonnet 5 |

使い方は、ふだんのオンデマンドの呼び出しとほとんど変わりません。`bedrock-runtime`のエンドポイントに`anthropic.claude-opus-5`のような接頭辞のないモデルIDを指定すればよく、AnthropicのMessages APIのほか、BedrockのInvokeModel・Converse APIにも対応します。入出力の安全フィルター「Guardrails」も併用できます。料金は呼び出したリージョンの標準オンデマンド料金で、CloudWatchの指標やCloudTrailのログもそのリージョンに記録されます。

その代わり、混雑したときに処理を別のリージョンへ逃がす仕組みはありません。処理能力はそのリージョンの容量が上限で、リージョンごとの利用上限（クォータ）もかかります。

## 3つの処理方式

Bedrockの公式ドキュメントは、Claudeの呼び出し方を3つに分けています。

| 方式 | 処理される場所 | 料金 |
|---|---|---|
| リージョン内 | 指定した1リージョンだけ | そのリージョンの標準料金 |
| 地域内（Geo） | 米国・EU・日本・オーストラリア・インドなど決められた地域の中 | 呼び出し元リージョンの料金 |
| グローバル | 世界中の商用リージョン | 同上。モデルによっては地域内より安い |

モデルIDの先頭に付く`jp.`や`global.`が方式の目印で、接頭辞のないIDがリージョン内推論です。

{{card:https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html|Regional availability（モデルごとの対応リージョン）|Amazon Bedrock ユーザーガイド}}

## 日本（東京・大阪）ではどうか

AIデジマ編集部が10月1日にこのドキュメントで確かめた、東京・大阪での主なClaudeの対応状況です。

| モデル | 東京のリージョン内 | 日本国内（Geo） | グローバル |
|---|---|---|---|
| Claude Opus 5.5 | × | ○ | ○ |
| Claude Sonnet 5.5 | × | × | ○ |
| Claude Opus 5・Sonnet 5 | × | × | ○ |
| Claude Fable 5.1・Mythos 5.1 | × | × | ○ |
| Claude Opus 4.8 | ○ | ○ | ○ |
| Claude Haiku 4.5 | ○ | ○（東京から） | ○ |

データを日本国内にとどめて新しい世代を使うなら、日本国内のリージョンで処理するGeo方式のClaude Opus 5.5（`jp.anthropic.claude-opus-5-5`）が現時点の選択肢です。東京の1リージョンで完結させたい場合は、Claude Opus 4.8かClaude Haiku 4.5に限られます。

## 論点

今回の発表からは、リージョン内推論の対象が最新モデルより遅れて広がることも読み取れます。ソウルで対応したのはOpus 5とSonnet 5で、9月に出たOpus 5.5とSonnet 5.5は、ソウルとシンガポールではグローバル方式でしか使えません。データの置き場所に厳しい組織ほど、最新モデルを待つ時間が長くなる構図です。

もう一つは処理能力とのトレードオフです。複数のリージョンに振り分けられない分、利用が集中したときの余裕は小さくなります。AWSも、処理能力はそのリージョンの容量に縛られると明記しています。

## 日本のビジネスへの影響

今回の対象は韓国とシンガポールで、日本のデータを国内で処理したい企業に直接の変化はありません。ただし、韓国やシンガポールの顧客データを扱う日本企業の現地拠点にとっては、現地で処理を完結させる選択肢が増えました。

関係が深いのは、金融機関・医療機関・自治体向けのシステムにClaudeを組み込む開発者と、情報システム部門です。今すぐできるのは、自社のアプリが呼んでいるモデルIDの接頭辞を確かめることです。`global.`なら処理は海外のリージョンでも行われます。社内規程や顧客との契約で国内処理を求められているなら、`jp.`のOpus 5.5か、東京のリージョン内推論に対応したモデルへの切り替えを検討してください。Opus 5.5の使い方は「[Claude Opus 5.5のプロンプトの書き方](/news/20260930-claude-opus-5-5-prompting-guide/)」にまとめています。

注意点は、リージョン内やGeoの方式は処理能力や利用上限の面でグローバルより窮屈になりやすく、モデルによってはグローバルの方が1トークンあたり安いことです。対応状況は頻繁に変わるため、本番に入れる前に公式ドキュメントで確認してください。各社APIの料金は「[AI API（LLM）の料金比較](/best/api/)」で比べられます。
