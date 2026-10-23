---
{
  "title": "ChatGPTとClaudeを職員のPCから遮断、スウェーデン政府 代わりに安全対策を強めたCopilotを使わせる",
  "description": "スウェーデン政府官房が10月26日から職員の業務用パソコンでChatGPTとClaudeを使えなくすると現地メディアが報じた。代わりに安全対策を強めたCopilotを使わせる。契約のないAIは情報の安全を損ないうるとの判断だ。",
  "date": "2026-10-24T03:10:00+09:00",
  "category": "policy",
  "tags": ["スウェーデン政府", "ChatGPT", "Claude", "Copilot", "セキュリティ", "規制"],
  "summary": [
    "スウェーデンの政府官房は10月26日から、職員の業務用パソコンでChatGPTとClaudeを使えなくすると、現地の公共ラジオが報じた",
    "代わりに使うのはMicrosoftのCopilotで、政府官房が審査し安全対策を強めたという。生成AIそのものを禁じるわけではない",
    "一部の職員は政府官房が自前で作ったAIの窓口を通じて、引き続きChatGPTとClaudeを使える"
  ],
  "sources": [
    {"title": "Enterprise data protection in Microsoft Copilot and Microsoft Copilot Chat", "publisher": "Microsoft Learn", "url": "https://learn.microsoft.com/en-us/microsoft-365/copilot/enterprise-data-protection", "kind": "公式ドキュメント"},
    {"title": "Swedish government offices to ban ChatGPT and Claude", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=50207405", "kind": "コミュニティ"},
    {"title": "Regeringskansliet spärrar ChatGPT och Claude", "publisher": "Sejfer", "url": "https://www.sejfer.se/nyheter/nyheter/2026/10/23/regeringskansliet-sparrar-chatgpt-claude/", "kind": "報道"},
    {"title": "Regeringskansliet spärrar ChatGPT och Claude", "publisher": "Bulletin", "url": "https://bulletin.nu/regeringskansliet-sparrar-chatgpt-och-claude", "kind": "報道"}
  ],
  "thumb_text": "ChatGPT 遮断",
  "thumb_style": "3d",
  "thumb_prompt": "A row of identical office laptops on long government desks in a calm Scandinavian office, each screen showing a small closed padlock, while one single laptop at the end glows softly with an open, friendly chat window.",
  "share_text": "スウェーデン政府官房が職員PCからChatGPTとClaudeを遮断、10月26日から。代わりは安全対策を強めたCopilot",
  "editor_note": ""
}
---
スウェーデンの政府官房（首相府と各省をまとめた組織）が、10月26日（月）から職員の業務用パソコンでChatGPTとClaudeを使えなくすると、同国の公共ラジオSveriges Radioの報道番組Ekotが現地時間10月23日に報じました。職員には代わりに、政府官房が審査して安全対策を強めたMicrosoftのCopilotを使うよう求めます。理由は情報の安全を守るためと説明されています。

## 何が起きたか

Ekotが入手した内部の情報をもとに、現地のニュースサイトSejferやBulletinなどが伝えた内容をまとめると、次のとおりです。

- **対象**: 政府官房の職員が使う業務用パソコンから、ChatGPTとClaudeに直接つなげなくなる
- **時期**: 10月26日（月）から
- **代わり**: MicrosoftのCopilot。政府官房が審査したうえで、安全対策を強めたとされます。どんな対策かは、報道官室が「安全上の理由」で明らかにしていません
- **例外**: 一部の職員は、政府官房が自前で作ったAIアシスタントの窓口を通じて、引き続きChatGPTとClaudeを使えます
- **範囲**: 生成AIをすべて禁止するわけではありません

デジタル化を担当するミカエル・ヴェッテルクランツ氏はEkotの取材を断り、職員向けの社内サイトで、契約を結んでいないAIサービスを使うと情報の安全に影響しうると注意を呼びかけたと報じられています。政府官房は以前から、中国のAI「DeepSeek」の利用を制限していました。

スウェーデンでは、税務庁や、少年の保護施設などを運営する国の機関でも同じような遮断がすでに始まり、債権の取り立てを担う執行庁も検討していると、Sejferは報じています。

## なぜCopilotは残るのか

報道からわかる判断の軸は「AIの性能」ではなく「契約があるかどうか」です。職員が個人の判断でChatGPTやClaudeのサイトを開いて文書を貼り付けると、そのデータをどう扱うかを組織として相手と取り決めていない状態になります。

Copilotは、メールのExchangeやファイル置き場のSharePointと同じ企業向けの契約で守られる、とMicrosoftは公式ドキュメントで説明しています。入力した指示やAIの答えについて、次のように書いています。

:::quote https://learn.microsoft.com/en-us/microsoft-365/copilot/enterprise-data-protection | Microsoft Learn「Enterprise data protection in Microsoft Copilot and Microsoft Copilot Chat」
> With EDP, prompts and responses are protected by the same contractual terms and commitments widely trusted by our customers for their emails in Exchange and their files in SharePoint.
企業向けデータ保護（EDP）のもとで、指示とAIの答えは、顧客がExchangeのメールやSharePointのファイルで信頼している契約条件と約束によって守られる。
:::

同じ文書は、Copilotでの指示や答えが土台のAIモデルの学習には使われないとも明記しています。すでにMicrosoftの製品を使っている役所にとっては、新しい契約を一から結ばずに済むという事情もありそうです。

## 反応と論点

この話題は米国の技術系掲示板Hacker Newsでも300ポイントを集めて注目されました。コメント欄では「組織が使ってよいAIを決めるのは普通のことで、大きな話ではない」という声がある一方、「目を引くのは禁止そのものより、Copilotを選んだことだ」という指摘も目立ちました。

論点は主に2つです。

- **契約が守りになる**: Microsoftには長年の企業向けのデータ処理の契約と実績があり、役所として説明しやすいという見方
- **米国企業である点は変わらない**: 米国の「CLOUD法」は、米国企業が持つデータを、保管場所が欧州でも米当局が提出させうる仕組みです。ChatGPTやClaudeを外しても、米国企業への依存は変わらないという指摘です。欧州で独自のクラウドやAIを持つべきだという意見も出ました

もう1つ見落としやすい点があります。Microsoftの同じ文書によると、Copilotの中ではAnthropicのモデル（Claude）が使われる場合があり、そのモデルはEUのデータを域内で処理する約束（EU Data Boundary）の対象外とされています。「Claudeを禁止してCopilotにする」としても、設定次第ではCopilotの中でClaudeが動くことになります。政府官房がその設定をどうしたかは報じられていません。

米国でも10月、国土安全保障省が中国のDeepSeekを連邦政府から締め出しました（[DeepSeek締め出しの記事](/news/20261020-dhs-deepseek-federal-agencies-ban/)）。そちらが「どの国のAIか」で線を引いたのに対し、スウェーデンは「契約を結んだAIかどうか」で線を引いた形です。

## 日本のビジネスへの影響

- **使えるか**: 日本の会社に直接の影響はありません。ただ、取引先の官公庁や大企業が同じ考え方で「契約のあるAIだけ」に絞ると、共同作業で使うAIを相手に合わせる必要が出てきます
- **誰に効くか**: 社内のAI利用ルールを作る情報システム部門や総務、法務の担当者です。「どのAIが便利か」より先に「どのAIと契約を結んでいるか」を軸に、使ってよいAIの一覧を作るという考え方の参考になります。ChatGPT・Claude・Copilotなどの法人プランの違いは[チャットAIのガイド](/best/chat/)にまとめています
- **今すぐやれること**: 社員が個人の無料アカウントで業務の文書をAIに貼り付けていないかを確かめ、使わせるなら法人向けプラン（入力を学習に使わない契約のもの）に寄せることです。ChatGPTやClaudeにも法人向けプランがあり、スウェーデンのように一律に遮断するのが唯一の答えではありません
- **注意点**: 遮断すると、社員が私物のスマートフォンで同じAIを使う「隠れ利用」が増えるおそれがあります。禁止と同時に、代わりに使える道具と、どこまでの情報なら入れてよいかを示すことが欠かせません
