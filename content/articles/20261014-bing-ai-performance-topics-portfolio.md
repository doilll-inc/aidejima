---
{
  "title": "CopilotなどAIの答えに自社サイトが出ない話題がわかる、Bingのサイト管理ツールに新機能",
  "description": "MicrosoftのBingが、サイト管理者向けのツールに、AIの回答で自社サイトがどの分野で引用されているかと、他社だけが引用されている質問の一覧を出す試験機能を加えた。集計は1〜3カ月の期間で見られる。",
  "date": "2026-10-14T11:20:00+09:00",
  "category": "marketing",
  "tags": ["Microsoft", "Bing Webmaster Tools", "Copilot", "SEO", "検索", "マーケティング"],
  "summary": [
    "MicrosoftのBingが10月13日、サイト管理ツールの「AI Performance」に新しい試験機能「Topics Portfolio」を加えた",
    "CopilotやBingのAIの答えで自社サイトが引用された質問を分野ごとにまとめ、分野の大きさや競合サイトの多さも示す",
    "他社のサイトは引用されているのに自社は引用されていない質問も一覧で出るため、次に書く記事の候補探しに使える"
  ],
  "sources": [
    {"title": "Introducing Topics Portfolio (beta) in AI Performance", "publisher": "Bing Webmaster Blog", "url": "https://blogs.bing.com/webmaster/2026/10/introducing-topics-portfolio-beta-in-ai-performance/", "kind": "公式発表"},
    {"title": "Introducing AI Performance in Bing Webmaster Tools Public Preview", "publisher": "Bing Webmaster Blog", "url": "https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview", "kind": "公式発表"},
    {"title": "Bing Webmaster Tools Sorts AI Search Queries Into Topics", "publisher": "Search Engine Journal", "url": "https://www.searchenginejournal.com/bing-webmaster-tools-topics-portfolio-ai-performance/592874/", "kind": "報道"}
  ],
  "thumb_prompt": "A large wall map of colorful islands representing topics, with a small flag planted on a few islands and many uncharted islands glowing faintly, while an anonymous marketer seen from behind points at an empty island.",
  "thumb_style": "photo",
  "thumb_text": "Bing AI Performance",
  "share_text": "CopilotなどAIの答えで、他社は引用されて自社は引用されない質問が一覧に。Bingのサイト管理ツールに試験機能",
  "editor_note": ""
}
---
MicrosoftのBingは現地時間10月13日、サイト管理者向けのツール「Bing Webmaster Tools」に、AIの回答の中で自社サイトがどんな分野で引用されているかを一覧にする試験機能「Topics Portfolio（トピック・ポートフォリオ）」を加えたと公式ブログで発表しました。他社のサイトは引用されているのに自社は引用されていない質問も、分野ごとに一覧で表示します。AIの答えに選ばれるかどうかが集客を左右し始めたいま、企業のWeb担当者が「次に何を書くか」を決める材料になります。

## 何が発表されたか

Topics Portfolioとは、AIが答えを作るときに使った検索語のうち、自社サイトが出典として引用されたものを「サッカー」「税金」のような大きな分野に自動でまとめて見せる機能です。Bingはこの検索語を「グラウンディング・クエリ」（AIが答えの根拠を探すために使った検索語）と呼んでいます。

:::quote https://blogs.bing.com/webmaster/2026/10/introducing-topics-portfolio-beta-in-ai-performance/ | Bing Webmaster Blog「Introducing Topics Portfolio (beta) in AI Performance」
> Below the topic table you will find Top Opportunity Queries: the strongest queries across your whole portfolio where other sites appear and yours does not.
分野の一覧の下には「Top Opportunity Queries」が表示されます。サイト全体の中で、他のサイトは出ているのに自社サイトは出ていない、有望な質問です。
:::

画面に出る主な項目は次のとおりです。

| 項目 | わかること |
|---|---|
| Topic | 自社サイトが引用された検索語をまとめた分野 |
| Topic Size | その分野で全サイトが引用された回数の概算。AIの答えでその分野がどれだけ求められているかの目安 |
| Sites Cited | その分野で引用されたサイト数の概算。競合の多さ |
| Queries | その分野に含まれる検索語の数の概算 |
| Opportunity Queries | 他社だけが引用されている検索語。引用回数は幅で表示 |

分野を選ぶと、自社がすでに引用されている検索語と、まだ引用されていない検索語が2つの表に分かれて出ます。期間は1カ月・2カ月・3カ月から選べます。Bing Webmaster Toolsにログインし、「AI Performance」の画面に新しくできたタブから使います。ただしデータが十分にあるサイトにしか表示されず、小さなサイトでは分野が少ないか、タブ自体が出ないこともあるとBingは説明しています。

## どのAIの答えが対象か

元になっている「AI Performance」の画面は、2月10日に試験公開されたものです。Bingの2月の発表によると、Microsoftの対話AI「Copilot」、Bingの検索結果に出るAIの要約、一部の提携サービスの回答で、どのページが出典として引用されたかを集計しています。6月には検索語を目的や分野で分類する機能が加わり、今回はそれを「サイト全体の地図」として見せる形に広げました。

Bingは、数字はあくまで目安だとくぎを刺しています。分野の分類はAIが自動で行うため、意図と違う分野に入る検索語もあるといいます。

:::quote https://blogs.bing.com/webmaster/2026/10/introducing-topics-portfolio-beta-in-ai-performance/ | Bing Webmaster Blog「Introducing Topics Portfolio (beta) in AI Performance」
> Treat the numbers as directional signals for planning, not as a precise ledger.
数字は計画のための方向を示す目安として扱い、正確な帳簿とは考えないでください。
:::

ブログによると、他社のブランド名を含む検索語が「チャンス」として出ることもあります。例えば靴の分野で、競合ブランドの名前を含む検索語が自社の候補として並ぶ場合があるとしています。各行には「良い・悪い」を伝えるボタンがあり、利用者の反応を分類の改善に使います。

## 背景

AIの答えに引用されるかどうかは、検索順位と並ぶ新しい集客の指標になりつつあります。BingのAI Performanceは、検索エンジン自身が「どの質問で、どのページが引用されたか」を出す仕組みです。Googleの検索画面でもAIの要約が増えており、会社名の検索でも要約が先頭に出る例が急増しているという米国の調査を[以前の記事](/news/20261010-google-ai-overviews-brand-searches-surge/)で紹介しました。ChatGPTが出典に公的機関やメーカーの公式サイトを選ぶ傾向が強まっているという調査も[出ています](/news/20261013-chatgpt-citations-primary-sources-ahrefs/)。

業界誌Search Engine Journalは、今回の機能について、記事を書いた時点ではAI Performanceのヘルプページにまだ説明がなく、試験版を終える時期も示されていないと報じています。

## 日本のビジネスへの影響

- **使えるか**: Bing Webmaster Toolsは日本のサイトでも登録して使えます。ただし今回の発表は言語や地域ごとの対応には触れておらず、日本語の検索語でどこまで分野が出るかは、自社のサイトで開いて確かめる必要があります。日本ではBingやCopilotの利用者はGoogleより少ないため、件数そのものは控えめになりそうです
- **誰にどう効くか**: オウンドメディアやブログを運営するマーケターとWeb担当者に向く機能です。「他社は引用されているのに自社は引用されていない質問」は、そのまま記事の企画会議の材料になります。従来の検索順位の分析とは別に、AIに選ばれる記事を作る手がかりが公式のデータで得られます
- **今すぐやれること**: Bing Webmaster Toolsに自社サイトを登録していなければ登録し、AI Performanceの画面を開いてみることです。新しいタブが出ていれば、引用の多い分野から見て、上位のOpportunity Queriesに答えるページが自社にあるかを確かめます。AIをマーケティングに使う道具は[広告・マーケティング向けAIのおすすめ](/best/marketing/)にまとめています
- **注意点**: 数字は概算で、分類はAIが自動でつけたものです。1つの数字に合わせて記事を量産するより、方向を確かめる材料として使うのが安全です。Bingの結果がGoogleやChatGPTでも同じになるとは限りません
