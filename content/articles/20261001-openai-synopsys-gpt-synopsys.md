---
{
  "title": "GPT-Synopsysを共同開発、OpenAIとSynopsysが半導体設計AIで複数年提携",
  "description": "半導体設計ソフト大手SynopsysとOpenAIが、設計ツールを熟練技術者のように操る専用モデルGPT-Synopsysを共同開発する複数年の提携を結んだ。収益は両社で分け合い、Synopsysは2027年度に約15%の増収を見込む。",
  "date": "2026-10-01T15:09:00+09:00",
  "updated": "2026-10-01T18:54:00+09:00",
  "category": "hardware",
  "tags": ["Synopsys", "GPT-Synopsys", "OpenAI", "半導体", "EDA", "提携"],
  "summary": [
    "SynopsysとOpenAIは、チップ設計に特化したモデルGPT-Synopsysを共同開発する複数年契約を結んだ",
    "モデルがSynopsysの設計ツールを直接操作し、性能・消費電力・面積の最適化や検証を繰り返して技術者に返す",
    "顧客の設計データは学習に使わず暗号化して扱い、収益は両社で分け合う。提供時期と価格は未発表"
  ],
  "sources": [
    {"title": "OpenAI and Synopsys Announce GPT-Synopsys: Frontier Intelligence to Revolutionize Chip Design", "publisher": "Synopsys", "url": "https://news.synopsys.com/2026-09-30-OpenAI-and-Synopsys-Announce-GPT-Synopsys-Frontier-Intelligence-to-Revolutionize-Chip-Design", "kind": "公式発表"},
    {"title": "Synopsys Details Growth Strategy and Long-term Financial Model at 2026 Investor Day", "publisher": "Synopsys（PR Newswire）", "url": "https://www.prnewswire.com/news-releases/synopsys-details-growth-strategy-and-long-term-financial-model-at-2026-investor-day-302894684.html", "kind": "公式発表"},
    {"title": "Synopsys Announces Synopsys.ai Copilot, Breakthrough GenAI Capability to Accelerate Chip Design", "publisher": "Synopsys", "url": "https://news.synopsys.com/2023-11-15-Synopsys-Announces-Synopsys-ai-Copilot,-Breakthrough-GenAI-Capability-to-Accelerate-Chip-Design", "kind": "公式発表"},
    {"title": "We’ve designed and built our first AI chip: Jalapeño.", "publisher": "X @OpenAI", "url": "https://x.com/OpenAI/status/2069770172802773292"},
    {"title": "Synopsys, OpenAI strike deal to develop AI model for chip design work", "publisher": "Reuters（Global Banking & Finance Review掲載）", "url": "https://www.globalbankingandfinance.com/synopsys-openai-strike-deal-develop-ai-model-chip-design/", "kind": "報道"},
    {"title": "OpenAI and Synopsys team up to build an AI model that designs chips like a seasoned engineer", "publisher": "The Decoder", "url": "https://the-decoder.com/openai-and-synopsys-team-up-to-build-an-ai-model-that-designs-chips-like-a-seasoned-engineer/"},
    {"title": "Why Synopsys Stock Soared Nearly 5% Higher Today", "publisher": "The Motley Fool", "url": "https://fool.com/investing/2026/09/30/why-synopsys-stock-soared-nearly-5-higher-today"}
  ],
  "thumb_text": "GPT-Synopsys",
  "share_text": "SynopsysとOpenAIが半導体設計の専用モデルGPT-Synopsysを共同開発。設計ツールをAIが直接操作",
  "thumb_style": "photo",
  "thumb_prompt": "An extreme close-up of a computer chip being designed, glowing circuit patterns drawn by a robotic pen arm on a silicon wafer, blue and gold light.",
  "editor_note": ""
}
---
半導体設計ソフト大手の米Synopsysと米OpenAIは現地時間9月30日、チップ設計に特化したAIモデル「GPT-Synopsys」を共同開発する複数年の戦略提携を発表しました。モデルがSynopsysの設計ツールを熟練技術者のように直接操作し、設計を繰り返し改善することを目指します。収益は両社で分け合います。

## 何が発表されたか

Synopsysは、EDA（電子設計自動化）の大手です。EDAとは、回路の記述から検証、トランジスタの配置まで、半導体の設計をコンピューターで進めるソフトの総称です。GPT-Synopsysは、このEDAツールの扱いに特化して調整する専用モデルで、開発のためにOpenAIがSynopsysのツールのライセンスを受けます。

両社の説明では、今のAI活用は汎用モデルを設計ツールにつなぐ段階にとどまっています。今回はその先として、モデル自体をツールの熟練した使い手に育てる考えです。

:::quote https://news.synopsys.com/2026-09-30-OpenAI-and-Synopsys-Announce-GPT-Synopsys-Frontier-Intelligence-to-Revolutionize-Chip-Design | Synopsys・OpenAI共同発表「OpenAI and Synopsys Announce GPT-Synopsys」
> The next leap, with this partnership, is to make frontier models experts in using EDA tools: learning to run the tools as expert engineers, interpreting their outputs, and iteratively optimizing designs using the tools.
この提携による次の飛躍は、最先端モデルをEDAツールの使い手の専門家にすることです。熟練技術者のようにツールを動かし、出力を読み解き、ツールを使って設計を繰り返し最適化することを学ばせます。
:::

共同発表とロイターの取材をもとに、設計の現場での役割分担を整理すると次のようになります。

| 担い手 | 役割 |
|---|---|
| 技術者 | PPA（消費電力・性能・面積）の最適化や、タイミング・検証の収束といった設計目標をAIに任せ、最後に結果を確認する |
| GPT-Synopsys | Synopsysのツールを動かし、結果を解釈して変更を加え、検証済みの結果に近づける |
| 従来型の検証ツール | AIの設計結果が物理的に成り立つかを改めて確かめる（Ghazi CEOがロイターに説明） |

提供は、モデル・計算資源・ツールのライセンスを一体にした形です。モデルはOpenAIのインフラで動き、顧客が使うエージェントの仕組みと組み合わせられるほか、Synopsysの「Synopsys.ai」と「Synopsys Autopilot」に深く組み込まれます。大手半導体企業との初期の技術検証はすでに始まっていますが、提供開始の時期と価格は発表されていません。

設計データの扱いについては、学習に使わないことと暗号化をはっきり約束しました。

:::quote https://news.synopsys.com/2026-09-30-OpenAI-and-Synopsys-Announce-GPT-Synopsys-Frontier-Intelligence-to-Revolutionize-Chip-Design | Synopsys・OpenAI共同発表「OpenAI and Synopsys Announce GPT-Synopsys」
> Customer data is not used to train the model, is encrypted at rest and in transit, and can be managed through configurable retention, audit and permission controls.
顧客のデータはモデルの学習に使わず、保存時も通信時も暗号化します。保存期間、監査、権限は設定で管理できます。
:::

## 収益の分け方と両社の狙い

発表の場は、同日のSynopsysの投資家向け説明会でした。同社は2027年度の売上高が前年度比約15%増の111億5,000万ドル（予想の中央値）になると見込みます。ロイターによると、アナリスト予想の11.19%を上回り、株価は一時7%上昇しました。同じ日には、Amazonとの複数年の半導体設計資産（IP）契約も発表しています。

GPT-Synopsysは、両社が研究開発と販売で協力し、収益を分け合う枠組みで世界の顧客に届けます。Ghazi CEOがロイターに語ったところでは、分け方は2段階です。まずOpenAIが、ツールの使い方を学ぶための学習用のサブスクリプション料金をSynopsysに払い、顧客が使い始めてからは、モデルが設計をどれだけ改善したかに応じて収益を分けます。

Ghazi氏は、自社の既存事業を食い合わない形に契約を組んだとも話しています。OpenAIのGreg Brockman社長は共同発表で「AIを動かすシステムを改善するために、最先端の技術を使っている」と述べ、より良いチップがより良いAIにつながるとしています。

## 背景

SynopsysとOpenAIの技術の組み合わせは初めてではありません。2023年には、MicrosoftのAzure OpenAI Serviceを使った対話型の設計支援「Synopsys.ai Copilot」を発表しています。今回はOpenAIと直接組み、ツールを操作する専用モデルまで作る点で一歩進みました。

OpenAI自身も半導体に踏み込んでいます。6月にはBroadcomと製造した初の自社AIチップ「Jalapeño」を発表しました。

{{x:https://x.com/OpenAI/status/2069770172802773292}}

The Decoderも、OpenAIがすでにBroadcomとAI専用チップを開発している点に触れています。半導体企業がAIモデルの開発側に踏み込む動きは、[AMDによるWorld Labsの買収](/news/20260930-amd-acquires-world-labs/)にも表れています。

## 訂正（10月1日）

The Decoderの記事の紹介で、同誌が書いていない見方（OpenAIが提携を自社チップの開発に生かす）を同誌の見方として記していました。同誌の記事にある内容（OpenAIがすでにBroadcomとAI専用チップを開発している点）に改めました。

## 日本のビジネスへの影響

GPT-Synopsysは世界の顧客向けに提供する計画ですが、現時点の検証は大手半導体企業に限られます。日本での提供時期や日本語対応は発表されていません。

関係が深いのは、国内の半導体設計者と、Synopsysのツールを使う電機・自動車メーカーの設計部門です。設計の試行回数を増やせれば、少人数の設計チームでも性能や消費電力を詰めやすくなります。

今すぐやれるのは、設計データを社外のAI基盤で扱えるかを社内規程で確認しておくことです。モデルはOpenAIのインフラで動くため、処理する地域や保存期間を契約時に確かめる必要があります。

注意点として、半導体の設計データは外為法の輸出管理や顧客との守秘契約の対象になりえます。両社が示した暗号化や学習不使用の約束とは別に、自社側の確認が要ります。コーディング用のAIエージェントの比較は「[コーディングAIのおすすめと料金比較](/best/coding/)」にまとめています。
