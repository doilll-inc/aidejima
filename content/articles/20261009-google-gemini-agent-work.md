---
{
  "title": "Gemini agentは目的を伝えるだけで数日がかりの仕事も進める、Googleが企業向けに発表",
  "description": "Google Cloudは10月8日、仕事を丸ごと任せられる企業向けAI「Gemini agent」を発表した。GmailやSlackから頼め、自分のメールアドレスを持つ「AIの同僚」も作れる。日本の保険大手SOMPOは社員3万4,000人で1万超のAIを作ったという。",
  "date": "2026-10-09T02:00:00+09:00",
  "category": "products",
  "tags": ["Google", "Gemini agent", "Gemini Enterprise", "Gemini", "エージェント", "Claude"],
  "summary": [
    "Google Cloudは10月8日、質問への回答から資料作成、プログラム作成まで1つで担う企業向けのAI「Gemini agent」を発表した",
    "指示ではなく目的を渡すと、AIが作業を分けて何時間、何日もかけて進める。GmailやSlack、Microsoft 365からも頼める",
    "役割を説明すると、自分のメールアドレスと予定表を持つ「AIの同僚」を作れる。現在は一部企業向けの先行提供と報じられている"
  ],
  "sources": [
    {"title": "Welcome to Gemini at Work 2026: Introducing the Gemini agent", "publisher": "Google Cloud公式ブログ", "url": "https://cloud.google.com/blog/products/ai-machine-learning/welcome-to-gemini-at-work-2026", "kind": "公式発表"},
    {"title": "Google Cloud announces 'Gemini agent' as 'universal agent for work'", "publisher": "9to5Google", "url": "https://9to5google.com/2026/10/08/gemini-agent-google-cloud/", "kind": "報道"},
    {"title": "Google is launching a one-stop Gemini agent for your work tasks", "publisher": "The Verge", "url": "https://www.theverge.com/tech/1007904/google-gemini-ai-agent-enterprise", "kind": "報道"},
    {"title": "Google Cloud Gemini Agent: Universal Work Agent", "publisher": "TbreakMedia", "url": "https://tbreak.com/google-cloud-gemini-agent-universal-work/", "kind": "報道"}
  ],
  "thumb_text": "Gemini agent",
  "thumb_style": "photo",
  "thumb_prompt": "An empty office desk at night with the lights off and a laptop closed, yet a row of sticky notes on the monitor is being neatly checked off by themselves and a fresh stack of printed slides sits finished in the tray.",
  "share_text": "Googleが企業向けAI「Gemini agent」を発表。目的を伝えれば数日がかりの仕事も進め、自分のメールを持つAI同僚も作れる",
  "editor_note": ""
}
---
Google Cloudは現地時間10月8日、企業向けの催し「Gemini at Work 2026」で、仕事を丸ごと任せられるAI「Gemini agent」を発表しました。質問への回答、資料作成、画像の生成、プログラムの作成と実行までを1つの入力欄から頼めるのが特徴で、作業は何時間、何日にもわたって続けられます。

## 何が発表されたか

Gemini agentとは、企業の社員が日々の仕事を任せるための、Googleの汎用のAIエージェント（人の代わりに複数の手順をこなすAI）です。Google Cloudのトーマス・クリアンCEOの基調講演をもとにした公式ブログは、使い方の考え方を次のように説明しています。

:::quote https://cloud.google.com/blog/products/ai-machine-learning/welcome-to-gemini-at-work-2026 | Google Cloud公式ブログ「Welcome to Gemini at Work 2026」
> You give it objectives, not instructions. You delegate an outcome and come back to finished work.
指示ではなく目的を渡す。欲しい成果を任せ、戻ってきたら仕事が終わっている。
:::

公式ブログの説明を、使う側から見て整理すると次の4点になります。

- **社内のデータを使える**: Salesforce、ServiceNow、Jira、Confluence、BigQueryなどの業務システムや、パソコン内のファイルにつないで作業する
- **頼む場所を選ばない**: GmailやドキュメントといったGoogleのアプリに加え、Microsoft 365やSlack、スマートフォンとパソコンのアプリ、Webからも同じエージェントを呼び出せる
- **人が離れても進む**: 処理はクラウド側で続くので、ノートPCを閉じても数日がかりの作業は止まらない。別の端末から続きを確かめても、前提を説明し直す必要はない
- **手分けする**: 大きな仕事は、その場限りの補助エージェントを複数立ち上げて同時に進める

使い方の例として公式ブログが挙げるのは会議の調整です。相手の名前やアドレスを並べずに「いつものメンバーと来週打ち合わせ」と頼んでも、Geminiがチャットの参加者や過去のやりとりから相手を割り出し、社外の人も含めて日程を調整するメールを送るところまで進めるとしています。Gemini側から仕事を引き取る提案もあり、たとえば上司から進捗をスライドにまとめるよう求めるメールが届くと、それをGeminiに任せるボタンが表示されます。

### 自分のメールアドレスを持つ「AIの同僚」

チームで使う場合は、必要な役割を説明すると、その役を担う「同僚エージェント」をGeminiが作ります。

:::quote https://cloud.google.com/blog/products/ai-machine-learning/welcome-to-gemini-at-work-2026 | Google Cloud公式ブログ「Welcome to Gemini at Work 2026」
> Coworker agents have dedicated identities including their own @agents.company.com emails, their own persistent storage, and only have access to the context that you or your team members provide.
同僚エージェントは専用のIDを持ち、@agents.company.com形式の自分のメールアドレスと保存領域を持つ。アクセスできるのは、利用者やチームのメンバーが渡した情報だけだ。
:::

作られた同僚エージェントには、Workspaceのアカウントとして予定表やドライブも割り当てられます。人の同僚と同じように、チャットで@を付けて呼んだり、ドキュメントのコメントで作業を頼んだりでき、編集の履歴にもそのエージェントの名前が残ります。

### 中で動くAIはGeminiとClaudeから選ぶ

Gemini agentは、仕事ごとに合うAIモデルを選んで動かします。公式ブログによると、現時点ではGoogleのGeminiのほか、AnthropicのClaudeも使い、ほかの企業やオープンなモデルにも今後広げます。Googleが自社の看板製品の中で競合のAIを動かすと明記した点は目を引きます。

費用の管理では、部署やプロジェクトごとに使う金額の上限を決められ、上限に達するとそのプロジェクトのエージェントが止まり、1クリックで再開できます。

## いつ、誰が使えるか

公式ブログは提供時期と料金を示していません。9to5GoogleやTbreakMediaは、現在は一部の企業に限った先行提供（プライベートプレビュー）で、Google Workspaceの一部のBusinessプランとEnterpriseプランの利用者に近く広く提供する予定だと報じています。

同じ発表では、金融と法務の業界向けの機能も先行提供を始め、行政・医療・小売り向けも近く出すとしています。

## 背景

Googleは企業向けのAIを「Gemini Enterprise」の名前でまとめて売り込んでおり、公式ブログによるとフォーチュン100社の90%近くが使っています。今回のGemini agentは、その入口を1つのAIにまとめる位置づけです。

ほかの会社も、AIに「答えさせる」から「仕事を任せる」へ軸足を移しています。前日にはMicrosoftが、Windowsのパソコン内のファイルを読んで整理や不具合対応まで代行するCopilotの新機能を発表しました（[既報](/news/20261008-microsoft-copilot-windows-hybrid-intelligence/)）。Googleは個人向けのGeminiアプリでも、よく使う指示を保存して呼び出せる「スキル」を始めています（[既報](/news/20261001-gemini-skills/)）。

## 反応と論点

日本企業の事例も紹介されました。公式ブログによると、保険大手のSOMPOは社員3万4,000人で1万を超えるAIエージェントを作り、文書の検索や要約を自動化しました。NTTドコモはデータ分析用のエージェントで、2週間かかっていた分析をすぐに出せるようにし、年45万時間を浮かせたといいます。

一方で、AIが自分のメールアドレスを持ち、何日も自律して動くことには、管理の難しさが伴います。Googleもこの点を意識しており、エージェントごとに身元を割り当てて権限を最小限にし、すべての操作を記録し、外とのやりとりを検査する仕組みを用意したと説明しています。料金や、AIが誤って社外に送ったメールの責任をどう扱うかは、今回の発表では示されていません。

## 日本のビジネスへの影響

- **使えるか**: 現時点では一部企業向けの先行提供で、日本での提供時期や料金は発表されていません。Google WorkspaceのBusiness・Enterpriseプランを使っている会社が、最初の対象になる見込みです
- **誰に効くか**: 会議の調整や資料づくりなど、メールとチャットを行き来する仕事が多い営業企画・管理部門と、社内のAI導入を担う情報システム部門です。同僚エージェントは、定型の報告書作りや問い合わせの一次対応を任せる使い方が考えられます
- **今すぐやれること**: Workspaceを使っている会社は、Googleの営業担当や販売代理店に先行提供の対象になるか確認し、「AIに任せたい定型業務」を3つ書き出しておく。任せる範囲を先に決めておくと、提供が始まったときに試しやすくなります
- **注意点**: AIに自分のメールアドレスと社内システムへの権限を持たせる以上、何を見せ、何をさせないかの社内ルールが要ります。数日かけて動く作業は費用も読みにくいため、上限額の設定を前提に試すのが安全です

チャットAIの選び方と料金は、用途別ガイド「[チャットAIのおすすめと料金比較](/best/chat/)」にまとめています。
