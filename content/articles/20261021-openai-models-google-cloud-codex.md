---
{
  "title": "OpenAIのAIがライバルGoogleのクラウドでも使えるように、Codexもつながり請求はGoogleに一本化",
  "description": "OpenAIとGoogle Cloudは10月21日、GPT-6 Astraなど3モデルをGoogle Cloudで提供すると発表した。まず一部の企業向けの限定公開で、利用料はGoogle Cloudの請求書1枚にまとまる。Codexも同日からつなげられる。",
  "date": "2026-10-21T22:55:00+09:00",
  "category": "business",
  "tags": ["OpenAI", "Google Cloud", "GPT-6 Astra", "Codex", "Antigravity"],
  "summary": [
    "OpenAIのAIモデル3種（GPT-6 Astra・GPT-6.1 Sol・GPT-6 Luna）が、GoogleのクラウドサービスGoogle Cloudで使えるようになる",
    "まず一部の大企業への限定公開から始まり、利用料はGoogle Cloudの請求書にまとまり、すでに約束した利用額からも払える",
    "OpenAIのプログラミング用AI「Codex」もGoogle側の基盤につなげられ、今後はGoogleの開発ツールAntigravityにも入る"
  ],
  "sources": [
    {"title": "Google Cloud expands model choice and flexibility, bringing OpenAI models to customers", "publisher": "Google Cloud Blog", "url": "https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-brings-openai-models-to-customers", "kind": "公式発表"},
    {"title": "OpenAI models are coming to Google Cloud", "publisher": "OpenAI", "url": "https://openai.com/index/openai-models-google-cloud/", "kind": "公式発表"},
    {"title": "OpenAI models are coming to Google Cloud（OpenAI Developer Community の告知）", "publisher": "OpenAI Developer Community", "url": "https://community.openai.com/t/openai-models-are-coming-to-google-cloud/1408440", "kind": "公式発表"},
    {"title": "OpenAI brings its frontier models to rival Google Cloud", "publisher": "Axios（Yahoo Finance転載）", "url": "https://finance.yahoo.com/technology/ai/articles/openai-brings-frontier-models-rival-120007827.html", "kind": "報道"},
    {"title": "OpenAI to offer its AI models and Codex tools on Google Cloud", "publisher": "Quartz", "url": "https://qz.com/openai-google-cloud-ai-models-codex-coming-weeks-102126", "kind": "報道"}
  ],
  "thumb_prompt": "Two rival skyscrapers in different colors at dusk, connected for the first time by a glowing glass sky bridge, with a single delivery cart rolling across the bridge carrying a small glowing cube.",
  "thumb_style": "photo",
  "thumb_text": "OpenAI × Google Cloud",
  "share_text": "OpenAIのAIがGoogle Cloudでも使えるように。3大クラウドすべてにOpenAIが乗り、請求はGoogleにまとめられる",
  "editor_note": ""
}
---
OpenAIとGoogle Cloudは現地時間10月21日、OpenAIの最新AIモデルをGoogleのクラウドサービス「Google Cloud」で提供すると発表しました。対象はGPT-6 Astra・GPT-6.1 Sol・GPT-6 Lunaの3つで、まずは選ばれた大企業への限定公開から始まります。

## 何が発表されたか

Google Cloudは、企業がサーバーやデータ保管、AIをネット越しに借りて使うサービスです。その中に、各社のAIモデルを選んで使える売り場「Model Garden（モデルガーデン）」があり、ここにOpenAIのモデルが並びます。Google側の発表を書いたのは、Gemini担当のプロダクトマネジメント責任者マイケル・ガーステンハーバー氏です。

並ぶ3モデルの位置づけは、Googleの説明では次のとおりです。

| モデル | Googleの説明（要約） |
|---|---|
| GPT-6 Astra | プログラミング、パソコン操作、専門的な仕事、科学研究などの重い作業向け |
| GPT-6.1 Sol | Astraに近い賢さを、より安い費用で |
| GPT-6 Luna | 日々の大量の作業向けの、速くて安いモデル |

提供の段階と範囲については、Googleがこう書いています。

:::quote https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-brings-openai-models-to-customers | Google Cloud Blog「Google Cloud expands model choice and flexibility, bringing OpenAI models to customers」
> OpenAI’s GPT-6 Astra, GPT-6.1 Sol, and GPT-6 Luna models are rolling out now in private preview to select enterprise customers in Google Cloud’s model garden, with more coming soon.
OpenAIのGPT-6 Astra、GPT-6.1 Sol、GPT-6 Lunaは、Google Cloudのモデルガーデンで一部の企業顧客向けに限定公開として提供を始めており、今後さらに広げる。
:::

使いたい企業は申し込みフォームから登録します。誰でも使える一般提供は「数週間以内」の予定だと米Axiosが報じています。料金はどちらの発表にも書かれていません。

### 請求はGoogle Cloudにまとまる

企業にとって大きいのは支払いの仕組みです。OpenAIのモデルはGoogle Cloudの「Marketplace（マーケットプレイス）」を通じて買う形になり、利用料はGoogle Cloudの請求書1枚に載ります。Google Cloudと事前に約束した年間の利用額（コミットメント）を取り崩して払うこともできます。OpenAIと別に契約を結び直す必要がありません。

データの扱いについてGoogleは、利用者が入力した指示や資料、AIの回答は指定した範囲の中にとどまり、AIの学習には使わないとしています。データをまったく残さない設定（ZDR）や、処理中のデータも暗号で守る仕組みは「近日対応」です。

### CodexやAntigravityにも

OpenAIのプログラミング用AI「Codex」は、発表当日から、手元のパソコンで使うCodexの計算部分をGoogle Cloud側に向けられるようになりました。さらに今後、Googleの開発ツール「Antigravity」と、企業向けGeminiの中でもOpenAIのモデルを選べるようになるとしています。

{{card:https://openai.com/index/openai-models-google-cloud/|OpenAI models are coming to Google Cloud|OpenAI}}

## 背景

OpenAIは長くMicrosoftのクラウド「Azure」と強く結びついてきました。Axiosによると、Microsoftとの契約が見直されたことで他社のクラウドにも出せるようになり、OpenAIは2026年に入ってAmazonのAWSでもモデルの提供を始めています。今回のGoogle Cloudで、米国の3大クラウドすべてにOpenAIのモデルが並ぶことになります。

Google側から見ると、自社のGeminiと真っ向から競合するモデルを自分の売り場に置く判断です。Googleはこれで、主要な非公開型モデル（中身を公開していないAI）3つをすべて扱う唯一の大手クラウドになったとし、200を超えるモデルを1つの基盤で使えると強調しています。AnthropicのClaudeはすでにGoogle Cloudで提供されており、Antigravityでも使えます。

## 反応と論点

Axiosの取材に、米調査会社Moor Insights & Strategyのアナリスト、マイク・レオーネ氏は、Google Cloudの顧客の多くがデータを動かさずにOpenAIのモデルを使いたがっていたと指摘しています。どのクラウドでも有力なモデルが使えるようになれば、差がつくのはデータの管理や統制、費用の面になるという見方も示しました。

一方で、同じ売り場にGeminiやClaudeが並ぶため、OpenAIは企業に自社のモデルを選んでもらう必要が残ります。AWSでの提供がどれだけの売上になったかは、両社とも公表していません。Google Cloud上の料金がOpenAIのAPI（プログラムから直接呼び出す窓口）と同じになるかも、現時点では示されていません。

## 日本のビジネスへの影響

- **使えるか**: 今回はまず一部の大企業向けの限定公開で、日本の企業が対象になるかや、使えるデータセンターの地域は発表に書かれていません。料金も未公表です。申し込みフォームから登録して案内を待つ段階です。
- **誰にどう効くか**: すでにGoogle Cloudを使っている会社の情報システム部門やDX担当者に効きます。これまでChatGPTやOpenAIのAPIを使うには、OpenAIかMicrosoftとの別契約や社内の審査が必要でした。Google Cloudの契約と請求の中で済めば、稟議や支払いの手間が減ります。
- **今すぐやれること**: Google Cloudの担当者か代理店に、限定公開の対象になるか、日本の地域で動くかを問い合わせておくとよいでしょう。社内で「GeminiとOpenAIのどちらを使うか」を決めかねているなら、同じ契約の中で両方を試せるようになるかもしれません。
- **注意点**: データを残さない設定などはまだ「近日対応」です。社外秘の資料を扱う業務に使う前に、どの機能が使える状態かを必ず確かめてください。

開発者向けのAIの窓口を選ぶときの比較は、[用途別ガイド「AIのAPI」](/best/api/)にまとめています。OpenAIの3モデルの違いは[GPT-6.1 Solの記事](/news/20260930-openai-gpt-6-1-sol/)も参考になります。
