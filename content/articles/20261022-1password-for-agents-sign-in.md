---
{
  "title": "AIに予約や買い物を任せてもパスワードは見せない、1Passwordが代わりにログインする仕組みを開始",
  "description": "1Passwordが、AIがログイン画面に来ると本人の承認を取って代わりに入力する新機能を公開した。AIはパスワードを見ない。Claude Duetなど6つのAIと連携し、個人・ファミリー向けは追加料金なし。",
  "date": "2026-10-22T22:50:00+09:00",
  "category": "products",
  "tags": ["1Password", "1Password for Agents", "エージェント", "セキュリティ", "Claude Duet", "ChatGPT Work"],
  "summary": [
    "パスワード管理の1Passwordが、AIに代わって本人のパスワードを入力する新機能「1Password for Agents」を公開した",
    "AIはログイン画面で止まって許可を求め、本人が承認すると1Passwordがサイトに直接入力するため、AI自身はパスワードを見ない",
    "Claude DuetやChatGPT Workなど6つのAIと連携予定で、1Passwordの個人・ファミリー向けプランなら追加料金はかからない"
  ],
  "sources": [
    {"title": "Introducing 1Password for Agents", "publisher": "1Password", "url": "https://1password.com/blog/1password-for-ai-agents", "kind": "公式発表"},
    {"title": "1Password will let you hand your data security over to your preferred AI agent", "publisher": "Engadget", "url": "https://www.engadget.com/2293844/1password-opens-up-ai-agents-muse-dots-grok/", "kind": "報道"},
    {"title": "1Password lets AI agents use your passwords without seeing them", "publisher": "The Verge", "url": "https://www.theverge.com/ai-artificial-intelligence/1016399/1password-ai-agent-password-sign-in", "kind": "報道"}
  ],
  "thumb_prompt": "A small polite robot butler stands in front of a locked front door holding an empty tray, while a human hand behind a frosted glass panel slides a glowing key directly into the lock so the robot never touches it.",
  "thumb_style": "illustration",
  "thumb_text": "1Password for Agents",
  "share_text": "AIに予約や買い物を任せても、パスワードはAIに渡さない。1Passwordが承認制で代わりにログインする新機能",
  "editor_note": ""
}
---
パスワード管理ソフトの1Passwordは現地時間10月22日、AIエージェント（利用者の代わりにWebサイトを操作して予約や買い物まで進めるAI）がログインするとき、パスワードをAIに渡さずに1Passwordが代わりに入力する新しい仕組み「1Password for Agents」を発表しました。AIはログイン画面で止まって本人の許可を求め、本人が承認したときだけ1Passwordがそのサイトに直接入力します。1Passwordの個人・ファミリー向けプランなら追加料金はかかりません。

## 何が発表されたか

1Password for Agentsとは、AIエージェントと、利用者のパスワードを保管する1Passwordの「金庫」とのあいだに立つ、ログイン専用の窓口です。AIは金庫の中身を見られず、必要なログイン情報を「使わせてほしい」と頼むことしかできません。

公式ブログに書かれた流れは次のとおりです。

1. 使っているAIエージェントを1Passwordにつなぐ
2. AIが作業の途中でログイン画面に着くと、そこで止まり、必要なログイン情報を求める
3. 利用者は、どのサイトのどのログイン情報が求められているかを1Passwordで確かめて承認する
4. 1Passwordがサイトにパスワードとワンタイムコード（2段階認証で届く数字）を直接入力し、AIはそのまま作業を続ける

核心は最後の段階です。公式ブログはこう説明しています。

:::quote https://1password.com/blog/1password-for-ai-agents | 1Password公式ブログ「Introducing 1Password for Agents」
> Now, with 1Password for Agents, your agent can request to use a credential from your vault, and if you approve the request, 1Password directly auto-fills the credentials in the destination site so the agent doesn’t have access to the credentials.
1Password for Agentsでは、エージェントは金庫にあるログイン情報の利用を求められます。承認すると1Passwordがログイン先のサイトに直接入力するため、エージェントはその情報に触れません。
:::

AIに使わせるのは承認したログイン情報だけで、金庫のほかの中身には届きません。つないだAIとの連携は、いつでも切れます。Engadgetは、許可はその作業の1回分だけで次に持ち越されないと報じています。

## どのAIで使えるか

公式ブログが連携先に挙げたのは、MetaのMuse、AnthropicのClaude Duet、OpenAIのChatGPT WorkとDots、SpaceXSIのGrok Bot、TownのTownieの6製品です。このうちMuseとGrok Botは「数日のうちに全プラットフォームで順次提供」とされ、ほかは提供の準備中です。さらに、AI検索のPerplexity、法人カードのRamp、AIにブラウザーを操作させる基盤のBrowserbaseやBrowser Useなど9社との連携も予定されています。

対象は1Password.comで作った個人・ファミリー向けのアカウントで、欧州向けの1Password.euとカナダ向けの1Password.caのアカウントはまだ対象外です。使える機能や対応する端末は連携先ごとに異なり、安全対策の中身も連携先によって違うと公式ブログは断っています。

{{card:https://1password.com/blog/1password-for-ai-agents|Introducing 1Password for Agents|1Password}}

## なぜパスワード管理ソフトがAIに関わるのか

予約や買い物を任せるAIは、ほぼ必ずどこかでログイン画面にぶつかります。そこで利用者が取れる手は2つしかありませんでした。AIの作業を止めて自分で入力するか、パスワードをチャット欄に貼ってAIに渡すかです。前者は手間がかかり、後者はAIやその運営会社にパスワードを預けることになります。

ブラウザーにパスワードを保存している人も、この問題は避けられません。1Passwordは公式ブログでこう指摘しています。

:::quote https://1password.com/blog/1password-for-ai-agents | 1Password公式ブログ「Introducing 1Password for Agents」
> Browser-password managers aren’t designed to let an agent sign in on your behalf.
ブラウザーのパスワード管理機能は、エージェントが本人に代わってログインすることを想定して作られていません。
:::

この秋、AnthropicのClaude Duet、OpenAIのDots、MetaのMuseと、各社が「頼まれる前から動く個人向けAI」を相次いで出しました。10月21日に発表されたClaude Duetの記事でも、パスワード管理ソフトとの連携を不安視する声を紹介しました（[Claude Duetの記事](/news/20261022-claude-duet-proactive-agent/)）。1Passwordは7月にClaude向けの連携を先に出しており、今回はそれを複数のAIに広げた形です。

## 反応と論点

Engadgetによると、1Passwordの最高製品責任者アシシュ・トリパティ氏は、エージェントは頼まれた仕事をこなせればよく、アカウントへの常時のアクセスを持つ必要はないという考えを示しました。パスワードを「渡す」のではなく「その場で使わせる」という発想です。

一方で、ログインの問題が片付いても、AIそのものの失敗は防げません。Engadgetは、注文の間違いや取り消せない予約のような失敗は起こりうるので、買い物や旅行を任せるときは注意が必要だと指摘しています。また、AIを受け入れるかどうかはサイト側の判断です。米国では航空会社や銀行が代理のAIを締め出す動きもあり（[AIエージェント締め出しの記事](/news/20261019-websites-banks-block-ai-agents/)）、ログインできてもその先で弾かれる場面は残ります。

## 日本のビジネスへの影響

- **使えるか**: 10月22日時点で、1Password.comの個人・ファミリー向けアカウントなら追加料金なしで対象になります。ただし連携先のAIのほうが日本で使えるかは製品ごとに異なり、Claude Duetは米国のPro・Max契約者だけの試験公開です。会社で契約する法人向けプランについて、公式ブログは触れていません
- **誰にどう効くか**: 予約サイトや通販サイト、業務用のSaaSにAIでログインさせたい個人事業主や小さな会社の経営者に関係します。経理や総務の担当者にとっては、「AIにパスワードを教える」運用を避けながら、請求書の取得や備品の発注をAIに任せる道が開けます
- **今すぐやれること**: いまAIのチャット欄にパスワードを貼って作業させている人は、それをやめるのが先です。そのうえで、AIに任せたい作業ごとに「どのサイトのログインが必要か」を書き出しておくと、連携先のAIが日本で使えるようになったときにすぐ試せます。チャットAIそのものの選び方は[チャットAIのおすすめと料金比較](/best/chat/)にまとめています
- **注意点**: 承認の通知が頻繁に来ると、中身を読まずに押す癖がつきがちです。どのサイトのログインを求められているかを毎回確かめる必要があります。社員が個人の1PasswordとAIで会社のアカウントにログインさせることの可否も、社内の規程で先に決めておくべきです
