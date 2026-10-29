---
{
  "title": "Geminiの新しい最上位AI「Gemini 4 Carbon」が性能首位に、まずはセキュリティの専門家だけ",
  "description": "Googleは現地時間10月28日、新しい最上位AI「Gemini 4 Carbon」を発表した。第三者の総合評価で59点の首位。ただし当面はサイバー防御の専門家だけが使え、一般向けの提供日は未定。料金は前作Argonと同じ入力100万トークン2ドルから。",
  "date": "2026-10-29T19:20:00+09:00",
  "category": "models",
  "tags": ["Gemini", "Gemini 4 Carbon", "Google", "セキュリティ", "ベンチマーク", "料金"],
  "summary": [
    "Googleが新しい最上位AI「Gemini 4 Carbon」を発表、AIの性能を比べる第三者の総合評価で59点の首位になった",
    "当面使えるのはサイバー攻撃を防ぐ組織の専門家だけで、一般の利用者や企業への提供は「近く」とされ日付は未定",
    "企業が使う場合の料金は前作のGemini 4 Argonと同じ導入価格で、ソフトの欠陥探しや何日も続く作業が得意"
  ],
  "sources": [
    {"title": "Gemini 4 Carbon: our next frontier model", "publisher": "Google", "url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/", "kind": "公式発表"},
    {"title": "Fairwind Program", "publisher": "Google DeepMind", "url": "https://deepmind.google/fairwind-program/", "kind": "公式発表"},
    {"title": "Google AI の投稿", "publisher": "X @GoogleAI", "url": "https://x.com/GoogleAI/status/2115489593818816591", "kind": "X投稿"},
    {"title": "Google の投稿", "publisher": "X @Google", "url": "https://x.com/Google/status/2115489522603466766", "kind": "X投稿"},
    {"title": "Gemini 4 Carbon（Hacker Newsの議論）", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=50276792"},
    {"title": "Google Deepmind releases Gemini 4 Carbon just two weeks after Argon with gains across the board", "publisher": "The Decoder", "url": "https://the-decoder.com/google-deepmind-releases-gemini-4-carbon-just-two-weeks-after-argon-with-gains-across-the-board/", "kind": "報道"},
    {"title": "Google launches Gemini 4 Carbon with a ‘significant leap’ in cybersecurity", "publisher": "The Verge", "url": "https://www.theverge.com/tech/1021339/google-gemini-4-carbon-cybersecurity-frontier", "kind": "報道"},
    {"title": "Gemini 4 Carbon AI Model Puts Google Back on Top, But Only Cyber Defenders Can Use It For Now", "publisher": "WinBuzzer", "url": "https://winbuzzer.com/2026/10/28/gemini-4-carbon-ai-leads-test-for-fixing-vulnerable-code-xcxwbn/", "kind": "報道"}
  ],
  "thumb_text": "Gemini 4 Carbon",
  "thumb_prompt": "A miniature diorama of a tiny glowing black carbon crystal displayed on a pedestal inside a glass vault, with miniature security guards in hard hats inspecting it while a long queue of tiny office workers waits behind a rope outside.",
  "thumb_style": "diorama",
  "share_text": "Geminiの新しい最上位AI「Gemini 4 Carbon」が性能首位に。ただし当面はセキュリティの専門家だけが使える",
  "editor_note": ""
}
---
Googleは現地時間10月28日、Geminiの新しい最上位モデル「Gemini 4 Carbon」を発表しました。AIの性能を比べる第三者の総合評価で59点の首位になった一方、当面はサイバー攻撃を防ぐ組織の専門家だけに提供し、一般の利用者や企業が使える日は決まっていません。

## 何が発表されたか

Gemini 4 Carbonとは、Googleが「これまでで最も強い」とするAIモデルで、ソフトウェアの欠陥（脆弱性。攻撃者に悪用されうる穴）を見つけて直す力と、何日もかかる長い作業を最後までやり通す力を特に伸ばしたものです。9月30日に発表した前作「Gemini 4 Argon」から、約1か月での世代交代になります。

:::quote https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/ | Google公式ブログ「Gemini 4 Carbon: our next frontier model」
> Carbon ranks #1 on the recently updated v5.0 of Artificial Analysis Intelligence Index at 59.
Carbonは、先ごろ更新されたArtificial Analysis Intelligence Index v5.0で59点の1位になりました。
:::

Artificial Analysisは、各社のAIを同じ条件で試験して点数を公開している独立の評価機関です。Googleが公式ブログで示した主な数字は次のとおりです。

| 項目 | Gemini 4 Carbon | 補足 |
|---|---|---|
| Artificial Analysisの総合評価 | 59点（1位） | The Decoderによると前作Argonは50点 |
| 脆弱性を見つける試験（SEC-bench Pro） | 88.2% | Googleは「最高水準」としている |
| 欠陥を修正する試験（CWE-bench） | 71.0% | 前作Argonは68.0% |
| 外部から仕込まれた命令への耐性 | 攻撃成功率0.0% | 前作Argonは0.7% |

最後の項目は、Webページやメールに紛れ込ませた「この指示に従え」という不正な命令に、AIがだまされた割合です。AIにメールや資料を読ませて仕事を任せる使い方では、ここが安全性を左右します。Googleは、社内で作業を任せた際の重大な不具合の警告が8割近く減ったことや、根拠のない主張がArgonの約半分になったことも挙げています。

## 誰がいつ使えるか

Googleは、まず「Fairwind Program」に参加するサイバー防御の組織に限って今週から提供を始めると説明しています。Fairwind Programは、政府機関や重要インフラの事業者などに新しいモデルを先に渡す枠組みです。

{{x:https://x.com/GoogleAI/status/2115489593818816591}}

Google AIの公式アカウントも、Carbonは自律的なプログラミングとサイバー防御で強いと投稿し、まず防御者に提供すると伝えています。

開発者・企業・一般の利用者に向けては「できるだけ早く」とするだけで、日付は示していません。Googleは、米国政府が任意で行う公開前のモデル試験にも参加しているとしています。

企業がシステムに組み込んで使う場合の料金は、Argonと同じ導入価格です。AIが読み書きする文章量の単位である100万トークンあたり入力2ドル・出力10ドルで、導入期間が終わると入力4ドル・出力20ドルになると脚注に書かれています。導入期間がいつまでかは、発表ページに書かれていません。

{{card:https://deepmind.google/fairwind-program/|Fairwind Program|Google DeepMind}}

## 背景

前作のArgonも、最初は同じように防御者だけに提供され、約2週間後の10月13日にGeminiアプリと検索のAIモードで有料プランの加入者が使えるようになりました（[GeminiアプリでGemini 4 Argonが利用可能に](/news/20261014-gemini-4-argon-gemini-app-ai-mode/)）。Carbonも同じ順番をたどるとみられますが、Googleは時期を約束していません。

ソフトの穴を見つける力が強いAIは、攻撃者が使えば危険な道具にもなります。Googleは、最初に使う防御者の意見を集め、安全のための制限を調整してから提供を広げると説明しています。

## 反応と論点

第三者の評価は「総合では首位だが、すべてで勝ったわけではない」という内容です。The Decoderは、プログラミングを任せる評価ではAnthropicのClaude Opus 5.5が62点で、Carbonの59点を上回ったと報じています。仕事の資料作りなどを比べる評価でも、中国のKimi K3.1 Proなどが上位でした。一方で、1つの作業にかかる費用はClaude Opus 5.5より安いとの評価も紹介しています。

懸念もあります。同じ報道によると、Artificial Analysisの試験で「わからないのに答えてしまう」割合は、Argonの4%から11%に上がりました。税務や財務の作業ではArgonの2倍以上の時間がかかったとしています。Googleが示したセキュリティの数字は安全のための制限を外した状態で測ったもので、外部からは検証できません。

Hacker Newsでは、モデルの性能より「どのプランで、どのアプリから使えるのかがわかりにくい」という不満が多く見られました。有料プランでも利用回数の上限にすぐ達するという声もあります。

## 日本のビジネスへの影響

- **使えるか**: 現時点で、日本の一般の利用者や企業は使えません。日本の組織がFairwind Programに参加しているかどうかも公表されていません。今、Geminiアプリで使える最上位はArgonです
- **誰にどう効くか**: 社内システムの保守を外注している企業の情報システム担当者や、セキュリティ事業者に関係が深い話です。AIが自社のソフトの欠陥を見つけて直す作業の精度と速さが上がっていくことになります
- **今すぐやれること**: 今は様子見でよい段階です。Geminiを使っている会社は、Argonで試している業務（長い資料の読み込みや社内文書の確認など）を記録しておくと、Carbonが一般公開されたときに同じ課題で比べられます
- **注意点**: 第三者評価では、わからないことを答えてしまう割合が前作より上がりました。公開後も、数字や事実を含む出力は人が確認する運用を続けるべきです。料金は導入価格の終了後に2倍になります

ほかのAIとの料金や使い分けは、[AIチャット・アシスタントの選び方](/best/chat/)にまとめています。
