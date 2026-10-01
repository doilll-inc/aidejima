---
{
  "title": "Googleが「Gemini 4 Argon」を公開、まず信頼できるサイバー防御者だけに提供",
  "description": "Google DeepMindが新しいフロンティアモデルGemini 4 Argonを発表した。出力は最大100万トークンに拡大し、導入価格は入力2ドル・出力10ドル。提供はFairwind Programのサイバー防御組織が先行する。",
  "date": "2026-10-01T15:20:00+09:00",
  "category": "models",
  "tags": ["Google", "Gemini 4 Argon", "セキュリティ", "ベンチマーク", "料金"],
  "summary": [
    "Gemini 4 ArgonはGoogleの約7か月ぶりのフロンティアモデルで、出力上限が64,000から100万トークンに拡大",
    "導入価格は100万トークンあたり入力2ドル・出力10ドルで、期間終了後は入力4ドル・出力20ドル",
    "サイバー能力が高いため、提供はFairwind Programの審査を通った防御組織から順に広げる"
  ],
  "sources": [
    {"title": "Gemini 4 Argon: our next era of frontier intelligence", "publisher": "Google DeepMind", "url": "https://deepmind.google/blog/gemini-4-argon-our-next-era-of-frontier-intelligence/"},
    {"title": "Gemini 4 Argon Model evaluation（Approach, methodology & results）", "publisher": "Google", "url": "https://storage.googleapis.com/deepmind-media/gemini/gemini_4_argon_model_evaluation.pdf"},
    {"title": "Fairwind Program", "publisher": "Google DeepMind", "url": "https://deepmind.google/fairwind-program/"},
    {"title": "Sundar Pichai の投稿", "publisher": "X @sundarpichai", "url": "https://x.com/sundarpichai/status/2105387952478277979"},
    {"title": "Artificial Analysis の投稿", "publisher": "X @ArtificialAnlys", "url": "https://x.com/ArtificialAnlys/status/2105392625788637299"},
    {"title": "Arena.ai の投稿", "publisher": "X @arena", "url": "https://x.com/arena/status/2105394855644139908"},
    {"title": "Google releases Gemini 4 Argon, called its most powerful model yet", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/09/30/google-releases-gemini-4-argon-called-its-most-powerful-model-yet/"},
    {"title": "Google announces Gemini 4 and says it’s so capable that only ‘trusted cyber defenders’ can have it right now", "publisher": "The Verge", "url": "https://www.theverge.com/tech/1002980/google-gemini-4-argon"},
    {"title": "Google Gemini 4 Argon closes the gap with OpenAI and Anthropic but doesn't take a clear lead", "publisher": "The Decoder", "url": "https://the-decoder.com/google-gemini-4-argon-closes-the-gap-with-openai-and-anthropic-but-doesnt-take-a-clear-lead/"},
    {"title": "Google Unveils Gemini 4 Argon, Pricing It Well Below Rivals", "publisher": "The Information", "url": "https://www.theinformation.com/briefings/google-unveils-gemini-4-argon-pricing-well-rivals"}
  ],
  "thumb_text": "Gemini 4 Argon",
  "share_text": "Googleが新フロンティアモデルGemini 4 Argonを公開。出力100万トークン、導入価格は入力$2・出力$10",
  "editor_note": ""
}
---
Google DeepMindは現地時間9月30日、新しいフロンティアモデル「Gemini 4 Argon」を発表しました。出力の上限を従来の64,000トークンから100万トークンへ広げた一方、サイバー攻撃に転用できる能力の高さから、提供はまず審査を通った防御組織に限られます。

## 何が発表されたか

Gemini 4 Argonは、実際のソフトウェア開発、法務や財務などの企業内ナレッジワーク、サイバー防御の3分野で最高水準の性能を出すとされる最上位モデルです。Googleがフロンティアモデルを出すのは、Gemini 3.1 Pro以来7か月ぶりになります。

:::quote https://deepmind.google/blog/gemini-4-argon-our-next-era-of-frontier-intelligence/ | Google DeepMind公式ブログ「Gemini 4 Argon: our next era of frontier intelligence」
> Today, we’re announcing our new frontier model, Gemini 4 Argon, which is rolling out to a set of trusted cyber defenders through our Fairwind Program.
本日、新しいフロンティアモデルGemini 4 Argonを発表します。Fairwind Programを通じて、信頼できるサイバー防御者の一団に提供を始めます。
:::

Fairwind Programは、政府機関や医療・通信などの重要インフラ事業者に先行してモデルを渡す枠組みで、現在650を超えるパートナーがいます。参加組織には脅威シミュレーションやマルウェア解析といった用途が許され、身元調査やフィッシング耐性のある多要素認証が条件です。Googleは信頼できる防御者と自社チームに対しては、サイバー関連の制限を外した状態でArgonを渡すとしています。

公式が示した主な評価結果は次のとおりです。いずれもGoogleの自己申告で、競合の数値は各社の公表値を引いたものです。

| ベンチマーク | Gemini 4 Argon | GPT-6 Astra | Claude Opus 5.5 |
|---|---|---|---|
| Vals Index（経済的な実務の総合） | 68.9% | 63.1% | 67.0% |
| DeepSWE v1.1（実務的な開発課題） | 77.9% | 74.1% | 74.2% |
| AutomationBench（業務フロー） | 51.3% | 41.4% | 42.5% |
| CWE-bench v1（脆弱性の修正） | 68.0% | 68.0% | 67.0% |
| Terminal-bench 4.0 | 57.4% | 58.2% | 66.4% |

Googleは社内での使用例も公開しました。Argonのエージェント群がデータセンターの計測データを分析して300TiB超のメモリを解放したこと、C/C++のコードをRustへ移す作業でFuchsiaのZirconカーネル80万行超に取り組んでいることなどです。動画デコーダーlibgav1では、既存のRust移植版の32,000行のSIMDコードを置き換え、2.7倍速くなったとしています。

料金は100万トークンあたり入力2ドル・出力10ドルの導入価格で、キャッシュした入力は入力単価の95%引きです。脚注では、導入期間が終わると入力4ドル・出力20ドルになると明記されています。The Informationは、この価格を競合より大幅に低いと報じています。

## 使えるのはいつからか

一般提供の時期は示されていません。Googleは米政府の自主的な事前提供プロセスに参加しながら段階的に広げるとし、開発者・企業・一般利用者への提供は、有料API顧客とGoogle AI Ultraの購読者から始めるとしています。前日のOpenAI DevDayでは[GPT-6.1 Solが即日提供](/news/20260930-openai-gpt-6-1-sol/)されており、出し方は対照的です。

## 反応と論点

ピチャイCEOは、次のモデルについて憶測が出ていたため早めに見せたとXに投稿しました。

{{x:https://x.com/sundarpichai/status/2105387952478277979}}

第三者評価では、Artificial AnalysisがIntelligence IndexでArgonを53点とし、GPT-6 Astra（最大設定）と同点、Claude Opus 5.5の58点には届かないと評価しました。1タスクあたりの費用は導入価格で1.99ドルと、Astraの3.26ドルの約6割です。

{{x:https://x.com/ArtificialAnlys/status/2105392625788637299}}

ただしArtificial Analysisによると、Argonは1タスクあたり平均62,000出力トークンを使い、Astraの27,000トークンの2倍以上です。単価の安さがそのまま総額の安さにはならない点は注意が必要です。人手による比較評価のArena.aiでは、Text Arenaで1,525点を取り1位になりました。

Hacker Newsの投稿は1,200ポイントを超えました。Rustへの大規模移行を評価する声がある一方、「結局また出せないモデルか」「発表だけで誰も試せない」といった不満も目立ちます。Google AI Ultraを契約していても当面使えないことへの指摘もありました。

## 日本のビジネスへの影響

日本の開発者や一般利用者は現時点で使えません。Fairwind Programは政府機関・重要インフラ・主要な技術基盤の運営者が優先で、応募には審査があります。日本語性能についての個別の発表はありません。

関係が深いのは、社内にセキュリティチームを持つ企業の情報システム部門と、法務・財務の文書業務を自動化したい部署です。前者はCWE-bench v1で首位タイという結果が、後者はVals Indexの首位という結果が判断材料になります。

いま急いでやることはありません。導入価格は期間限定で、終了後は2倍になります。現行のGemini 3.8 Flashや他社モデルで動かしている処理の費用と品質を記録しておき、一般提供が始まった時点で同じ条件で比べられるようにしておくのが実務的です。[AI API（LLM）の料金比較](/best/api/)も合わせて確認してください。

注意点は2つあります。出力トークンを多く使う傾向があるため、単価だけで費用を見積もると外れること。そして、サイバー防御の制限を外した版は一般には出ないため、脆弱性診断の自動化を期待して待つのは現実的ではないことです。
