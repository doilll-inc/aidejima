---
{
  "title": "部署がClaudeで何をしていくら使ったか、AIが報告書に Anthropicが会社向けに開始",
  "description": "Anthropicは企業向けのClaude Enterpriseで、部署ごとの仕事の中身と費用をAIがまとめる「スマートレポート」、社員アンケート、チームで共有する予算の3機能を正式に始めた。レポートは月10本まで無料で作れる。",
  "date": "2026-10-29T19:40:00+09:00",
  "category": "business",
  "tags": ["Anthropic", "Claude Enterprise", "Claude", "経営", "導入事例", "料金"],
  "summary": [
    "Anthropicは10月28日、会社向けのClaude Enterpriseで、部署がClaudeで何を作り、いくら使ったかをAIがまとめる報告書の機能を正式に始めた",
    "社員に「Claudeでいちばん役立った仕事」を聞くアンケートと、部署で1つの月額予算を分け合う仕組みも同時に始まった",
    "報告書は1社あたり月10本まで無料で、個人の評価や人事には使わないようにとAnthropicは明記している"
  ],
  "sources": [
    {"title": "Smart reports, surveys, and pooled group budgets for Claude Enterprise", "publisher": "Anthropic（claude.com）", "url": "https://claude.com/resources/articles/smart-reports-surveys-pooled-budgets", "kind": "公式発表"},
    {"title": "Get started with smart reports", "publisher": "Claude ヘルプセンター", "url": "https://support.claude.com/en/articles/16893491-get-started-with-smart-reports", "kind": "公式ドキュメント"},
    {"title": "Anthropic just launched tools to show companies what their AI spending is buying", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/10/28/anthropic-just-launched-tools-to-show-companies-what-their-ai-spending-is-buying/", "kind": "報道"}
  ],
  "thumb_prompt": "A glass office building cut open like a dollhouse, each floor's team desk glowing with a small floating receipt and a bar chart above it, while one manager figure on the top floor holds a magnifying glass over the whole building.",
  "thumb_style": "3d",
  "thumb_text": "Claude Enterprise",
  "share_text": "部署がClaudeで何を作り、いくら使ったかをAIが報告書に。会社向けClaude Enterpriseに新機能、月10本まで無料",
  "editor_note": ""
}
---
Anthropicは現地時間10月28日、企業向けプラン「Claude Enterprise」に、部署ごとの仕事の中身と費用をAIがまとめる「スマートレポート」など3つの機能を正式に追加しました。管理者は部署と期間を選ぶだけで、その部署がClaudeで何を作り、それにいくらかかったか、どこでつまずいたかを一覧にできます。レポートは1社あたり月10本まで無料です。

## 何が始まったか

Claude Enterpriseとは、AnthropicのAI「Claude」を会社全体で使うための法人向けプランです。今回加わったのは、スマートレポート、アプリ内アンケート、部署で共有する予算の3つ。どれも「AIにお金を払って、何が得られているのか」を会社が確かめ、うまくいっている使い方を広げるための機能です。

:::quote https://claude.com/resources/articles/smart-reports-surveys-pooled-budgets | Anthropic「Smart reports, surveys, and pooled group budgets for Claude Enterprise」
> Smart reports surface what a team gets done with Claude, and what that work costs.
スマートレポートは、チームがClaudeで何を成し遂げ、その仕事にいくらかかったかを示します。
:::

3つの機能の中身を整理します。

| 機能 | 何ができるか |
|---|---|
| スマートレポート | 部署・期間（最大で直近28日）・対象製品を選ぶと、Claudeが会話の記録の一部を読み、仕事を「業務の流れ」ごとに分類。それぞれの費用、できあがった成果物、つまずいた点（連携先が足りない、操作の失敗など）を示す |
| アプリ内アンケート | 社員がClaudeの返答を受け取った後に短いカードで質問を表示。回答は届いた順に一覧になり、表計算ソフトに書き出せる |
| 部署で共有する予算 | 部署に1つの月額予算を設定し、メンバーはそこから使う。個人の上限も残せて、どちらかに達した時点で止まる。予算の50%・75%・95%・100%で管理者にメールが届く |

レポートには、提案の一覧も付きます。たとえば、何度も繰り返されている作業を「スキル」（決まった手順をClaudeに覚えさせる仕組み）にまとめる、といった内容です。費用は定価で計算されます。予算が足りずに仕事が止まっている人がいれば、支払いの権限を持つ管理者がレポートの画面から上限を上げられます。

アンケートの標準の質問も、費用対効果を意識したものです。「最近Claudeでいちばん価値があった仕事は何か」「その仕事にかかる時間はどう変わったか」「同僚にまねしてほしい使い方は何か」「明日Claudeが使えなくなったら、何が最初に止まるか」の4つで、管理者が変えたり消したりできます。

## 個人の評価には使わない

社員の会話の記録をAIが読むと聞くと、監視の道具にならないかが気になります。公式ヘルプによると、スマートレポートは初期設定では無効で、会社の最上位の管理者が有効にしない限り動きません。報告書の中で個人の名前を出す設定も初期状態では切られていて、名前を表示するたびに記録が残ります。

健康、労働組合の活動、ハラスメントや内部通報、政治や宗教の考え、私生活、特定の人物への感情といった話題は、集計にだけ使われ、個別の要約は表示されません。管理者がこうした話題について独自の質問を立てることもできず、この制限は外せません。

:::quote https://support.claude.com/en/articles/16893491-get-started-with-smart-reports | Claude ヘルプセンター「Get started with smart reports」
> Smart reports are available on Claude Enterprise plans and are off by default.
スマートレポートはClaude Enterpriseプランで使え、初期設定では無効になっています。
:::

Anthropicは発表の中で、この報告書は導入状況の把握と投資の計画のためのもので、個人の成績の評価や雇用の判断に使うものではないと書いています。発表ページには、DoorDashやDocusignなど導入企業の担当者のコメントも並んでいます。

## 背景：AIの請求書が予想以上に増えている

TechCrunchによると、開発チームの分析を手がける米Jellyfishの調査では、AIにプログラムを書かせる道具への企業の支出は年初から10倍になり、技術部門の費用全体の約2%に達しました。同社の研究責任者は、多くの財務責任者が計画していなかった伸びだと話しています。

使う量が増えれば、経営側は「何に使われ、元が取れているのか」を知りたくなります。米Gartnerの調査でも、AIで大きな成果を出せた企業は13%にとどまっていました（[AIで大きな成果を出せた企業は13%だけ、差をつけたのは「やめる基準」](/news/20261023-gartner-cio-survey-ai-value-13-percent/)）。さらにOpenAIが値引きでClaudeの大口客を取りにいっていると報じられています（[OpenAIが大幅値引きでClaudeの大口客を奪う](/news/20261025-openai-discounts-poach-anthropic-claude-customers/)）。使い道と成果を見える形で示せるかは、契約を続けてもらううえでも大事になっています。

## 日本のビジネスへの影響

- **使えるか**: Claude Enterpriseを契約している会社なら、日本の会社でも使えます。発表はEnterprise向けで、小規模向けのTeamプランについては触れていません。暗号鍵を自社で管理する設定や、医療向けの設定にしている会社では使えない機能があると公式ヘルプに書かれています。
- **誰にどう効くか**: AI導入を任された情報システム部門やDX推進の担当者、AIの予算を握る経営企画に向いています。「どの部署が何に使い、いくらかかったか」を数字で説明できるので、経営会議での導入効果の報告や、来期の予算取りの材料になります。
- **今すぐやれること**: 契約中の会社は、まず1つの部署で直近28日分のレポートを作ってみて、繰り返し出てくる作業や、連携先が足りずに止まっている作業を確かめます。月10本の無料枠に収まる範囲で試せます。
- **注意点**: 社員の会話の記録をAIが読む仕組みなので、有効にする前に、社内のルールで目的（導入効果の把握であり、個人評価ではないこと）を社員に知らせておくのが安全です。費用は定価で計算されるため、値引き契約をしている会社では実際の請求額と合わないことがあります。ChatGPTやGeminiなど他社の法人向けプランとの比べ方は[チャットAIのガイド](/best/chat/)にまとめています。
