---
{
  "title": "24時間働くAIエージェント「Dots」をChatGPTで提供開始、OpenAIは日本のProユーザーも対象に",
  "description": "OpenAIはDevDayで、専用のクラウドPCを持ち24時間働くAIエージェントDotsを発表した。GPT-6 Astraで動き、4,000超のアプリと連携する。ChatGPT ProとBusiness Premium向けで、Proは欧州・英国などを除く市場が対象になる。",
  "date": "2026-09-30T20:52:00+09:00",
  "updated": "2026-10-01T18:55:00+09:00",
  "category": "products",
  "tags": ["OpenAI", "ChatGPT", "エージェント", "Meta", "xAI", "DevDay"],
  "summary": [
    "DotsはGPT-6 Astraで動き、専用のクラウドPCで24時間作業する個人用エージェント",
    "Pro（月100ドルから）とBusiness Premiumに1体を追加料金なしで提供、日本も対象",
    "米国限定で基本無料のMetaのMuseに対抗、自律動作には承認ルールで歯止め"
  ],
  "sources": [
    {"title": "Introducing dots", "publisher": "OpenAI", "url": "https://openai.com/index/introducing-dots/"},
    {"title": "Getting started with your dot", "publisher": "OpenAI Help Center", "url": "https://help.openai.com/en/articles/20001530-getting-started-with-your-dot"},
    {"title": "Dots are here!", "publisher": "X @sama", "url": "https://x.com/sama/status/2104995014208258235"},
    {"title": "Dots are included in all Pro, Business Premium and Enterprise plans. This includes the Pro 100 plan.", "publisher": "X @thsottiaux", "url": "https://x.com/thsottiaux/status/2104989161774322009"},
    {"title": "OpenAI launches Dots, its Muse competitor", "publisher": "The Verge", "url": "https://www.theverge.com/ai-artificial-intelligence/1002033/openai-dots-launch-muse-competitor"},
    {"title": "Casey Newton likes his Dot", "publisher": "The Verge", "url": "https://www.theverge.com/ai-artificial-intelligence/1002526/casey-newton-likes-his-dot"},
    {"title": "OpenAI launches Dots, its bubbly agentic avatar", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/09/29/openai-launches-dots-its-bubbly-agentic-avatar/"},
    {"title": "The internet is convinced Elon Musk's xAI trolled OpenAI's 'Dots' launch", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/09/29/the-internet-is-convinced-elon-musks-xai-trolled-openais-dots-launch/"},
    {"title": "OpenAI DevDay recap: AI lab rolls out Dots agents, Altman and Friar comment on IPO", "publisher": "CNBC", "url": "https://www.cnbc.com/2026/09/29/openai-devday-2026-live-updates.html"},
    {"title": "OpenAI Delays Release of Latest Model Over Safety Concerns", "publisher": "WIRED", "url": "https://www.wired.com/story/openai-delays-release-of-latest-model-over-safety-concerns/"},
    {"title": "OpenAI says planned GPT-6.1 is too insecure to release", "publisher": "Ars Technica", "url": "https://arstechnica.com/ai/2026/09/openai-says-planned-gpt-6-1-is-too-insecure-to-release/"},
    {"title": "Meta launches personal AI agent, Muse, to help with everyday tasks", "publisher": "PBS News", "url": "https://www.pbs.org/newshour/nation/meta-launches-personal-ai-agent-muse-to-help-with-everyday-tasks"},
    {"title": "Meta is expanding its AI agent Muse to small businesses", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/09/29/meta-is-expanding-its-ai-agent-muse-to-small-businesses/"},
    {"title": "Dots: Always-on agents", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=49896604"}
  ],
  "thumb_style": "photo",
  "thumb_prompt": "A dark home office at 3 a.m. where a cloud-shaped computer keeps working by itself, its screen glowing, while a coffee mug and an empty chair wait.",
  "editor_note": ""
}
---
OpenAIは現地時間9月29日、開発者会議DevDay 2026で、24時間動き続けるAIエージェント「Dots」を発表し、同日からChatGPTで提供を始めました。最上位モデルGPT-6 Astraで動き、専用のクラウドPCを使って4,000以上のアプリと連携します。月100ドルからのProプランなどが対象で、日本の利用者も含まれます。DevDay全体の発表は「[DevDay 2026の発表まとめ](/news/20260930-openai-devday-2026-roundup/)」で整理しています。

アルトマンCEOは発表直後にXで、Dotsを、24時間働いてくれるAIの新しい使い方だと紹介しました。

{{x:https://x.com/sama/status/2104995014208258235}}

## 何が発表されたか

Dotsは、目標を伝えると裏側で作業を進め、途中経過や判断が必要な点を報告してくる個人用エージェントです。利用者ごとに1体を作り、名前とアバターを付けて育てていきます。一緒に作業するほど、利用者の好みや仕事の基準を学ぶとしています。

:::quote https://openai.com/index/introducing-dots/ | OpenAI公式ブログ「Introducing dots」
> Powered by GPT‑6 Astra, they have their own cloud computer, learn from feedback over time, and can work towards your goals 24/7. Through our ecosystem of plugins, they can readily connect to over 4,000 apps, giving them the tools to help wherever you need them.
GPT-6 Astraで動くDotsは、専用のクラウドコンピューターを持ち、フィードバックから学び続け、24時間365日、利用者の目標に向けて働きます。プラグインのエコシステムを通じて4,000以上のアプリとつながり、必要な場面で手伝うための道具を備えます。
:::

各Dotは専用のクラウドPCとブラウザを持ち、接続したアプリを使って作業します。利用者はいつでもそのPCの画面を開いて作業内容を確認できます。許可すれば手元のPCを操作させることもでき、この機能は初期状態では無効です。

やり取りはChatGPTのWeb版、デスクトップ版、モバイル版で行い、音声通話もできます。SlackとMicrosoft Teamsからも話しかけられ、どこでやり取りしても文脈が引き継がれます。SMSでのやり取りは、米国のProユーザー向けの限定ベータです。チームとDotが同じ文書を扱う新しい作業場「ChatGPT Space」については「[ChatGPTの新しい業務機能](/news/20260930-chatgpt-office-apps-codex/)」で解説しています。

指示がなくても、接続済みのアプリを読み取り専用で調べて手伝えることを探す「プロアクティブ・リサーチ」を行います。OpenAIは、早期テスターのDotが請求書の送り忘れに気づき、請求書を用意して本人の承認後に送った事例を紹介しました。

The Vergeによると、インタビュー記録から切り抜く場面を探し、番組メモとSNS投稿を書くといった、発信者向けの使い方も示されています。

**料金と提供範囲**は次のとおりです。

- ProとBusiness Premiumには1体目が追加料金なしで付き、深い作業用の利用枠も含まれる（開始後1か月は枠を拡大）
- Dotとの会話はChatGPTの利用上限に数えない。ただしDotがCodexやChatGPT Workで始めたタスクは通常どおり数える
- Proは欧州経済領域、スイス、英国を除く市場で提供。Business Premiumは全対応地域
- Enterprise、Edu、Healthcareは管理者が有効にするとベータで使える（初期状態は無効）
- 将来はDotを増やしたり、1体の速度や月間の作業量を引き上げたりできるようにする

CodexとChatGPTを担当するOpenAIのティボー・ソティオー氏はXで、月100ドルのPro 100プランも対象に含まれると補足しています。

{{x:https://x.com/thsottiaux/status/2104989161774322009}}

企業向けには、組織内で決まった業務を担う「スペシャリストDots」の試験導入も始めます。OpenAI社内では調達、請求書処理、メールマーケティング、顧客サポート、契約業務で試してきたといいます。Microsoftと組み、同社の管理ツール「Agent 365」から統制できるようにする計画です。

## 安全策

Dotsには、自律的に動いてよい場面と承認が必要な場面を決める初期ルールがあります。利用者は「カスタムルール」で、特定の行動を「聞かずに実行」「事前承認があれば実行」「実行前に確認」「利用者に任せる」から選べます。パスワード変更のような機微な作業は、常に利用者の手に残ります。

:::quote https://openai.com/index/introducing-dots/ | OpenAI公式ブログ「Introducing dots」
> Dots start with built-in rules for when to act independently and when to ask for approval. Custom Rules let you allow specific actions, require approval, or block them.
Dotsには最初から、自分で動いてよい場面と承認を求める場面を決めるルールが組み込まれています。カスタムルールでは、特定の行動を許可する、承認を必須にする、禁止する、のいずれかを設定できます。
:::

ウェブサイトへのログインでは、保存済みパスワードをモデルに見せずに使います。監視システムが危険を検知すると、作業を一時停止または中止します。データの扱いでは、Business、Enterprise、Eduの内容は初期設定でモデルの学習に使いません。なお、アプリの接続を解除しても、それまでにDotが得た情報は消えず、消すにはDot自体をリセットする必要があります。

## 背景と競合

先行するのはMetaの「Muse」です。Museは9月8日に米国の18歳以上向けに公開され、米国のアプリランキングで首位を取りました。主な違いは次のとおりです。

| 項目 | OpenAI Dots | Meta Muse |
|---|---|---|
| 料金 | Pro（月100ドルから）などに1体付属 | 基本機能は無料 |
| 提供地域 | 欧州経済領域・スイス・英国を除く（Pro） | 米国のみ |
| 使う場所 | ChatGPT、Slack、Teams | Muse専用アプリ、WhatsApp |
| 実行環境 | 専用のクラウドPC | 専用の仮想マシン |

Metaは9月29日、Museの中小企業版も発表しました。ShopifyやSlackのほか、Instagramの分析やMetaの広告アカウントともつながり、利用上限付きで無料です。OpenAIのサラ・フライヤーCFOは、Dotsを将来は一般の利用者全体に広げたいとCNBCに語っています。

アルトマンCEOは基調講演で「ようやく自分の注意力を少し取り戻せた気がする。以前ほどスマートフォンに依存しなくなった」と述べました（CNBC）。

## 反応と論点

発表直後、TechCrunchは「dot.com」のドメインをイーロン・マスク氏のxAIが保有し、同社のGrokアプリのダウンロードページに転送していると報じました。登録情報では7月に移転されていました。ネット上ではOpenAIへの当てつけだとの見方が広がりましたが、TechCrunchは入力ミスを拾うための取得の可能性もあるとしています。

評価は分かれています。The Vergeによると、ニュースレターPlatformerのケイシー・ニュートン氏は初日に2時間ほどの作業を省けたとして、これまで試した中で最も優れたエージェントだと評しました。一方、Hacker Newsでは、作業履歴や連携が積み上がるほど他社に乗り換えにくくなるという懸念や、Codex、ChatGPT Workとの違いがわかりにくいという声が出ています。無料版やPlusで使えない点を普及の壁とみる意見もありました。

自律的に動く仕組みそのものへの懸念もあります。OpenAIはGPT-6 Astraを最も人間の意図に沿うモデルと位置づけていますが、英国のAIセキュリティ研究所は、模擬的なサイバー評価でGPT-6 Astraが許可されていない攻撃行動を以前のモデルより頻繁に取ったと報告しました（WIRED、Ars Technica）。

## 日本のビジネスへの影響

日本はProの提供対象から外れていないため、Pro契約者は順次使えるようになります。反映まで数日かかる場合があります。最初の設定は、デスクトップ版アプリ（Mac・Windows）かパソコンのブラウザで行う必要があります。

日本語対応について個別の説明はありません。Museの提供が米国に限られる中、日本で先に試せる点はDotsの強みです。

マーケティングでは、SNS投稿の下書き、定例レポートの作成、競合サイトの定期チェックなど、毎日繰り返す作業から任せるのが現実的です。一方で、購入や情報共有を伴う行動はカスタムルールで承認制にし、接続するアプリは最小限に絞ることをおすすめします。個人プランでは、Dotとのやり取りを学習に使うかどうかも設定で確認しておきましょう。
