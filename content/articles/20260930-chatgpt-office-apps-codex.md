---
{
  "title": "ChatGPTに共同編集の文書とSpace、アプリ型プラグインや月500ドルのProも登場",
  "description": "OpenAIはDevDayでChatGPTの業務機能を大きく広げた。チームとAIが共同編集する文書Pagesと作業場Space、近く出るスライド、アプリのように動くプラグイン、Codexの再利用できるクラウド環境、月500ドルのPro 500の中身を整理する。",
  "date": "2026-09-30T20:46:00+09:00",
  "category": "products",
  "tags": ["OpenAI", "ChatGPT", "Codex", "Microsoft", "DevDay"],
  "summary": [
    "ChatGPT SpaceとPagesでチームとAIが同じ文書を共同編集、スライドは数週間内に",
    "プラグインがサイドバーや操作パネルを持つアプリ型に進化し、イベント起点の自動化も",
    "月500ドルのPro 500はPlusの25倍の枠と高速モード付き、Pro 200は新規の枠が半減"
  ],
  "sources": [
    {"title": "DevDay 2026 Recap", "publisher": "OpenAI", "url": "https://openai.com/index/devday-2026-recap/"},
    {"title": "About ChatGPT Pro tiers", "publisher": "OpenAI Help Center", "url": "https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers"},
    {"title": "ChatGPT Space", "publisher": "OpenAI", "url": "https://chatgpt.com/features/space/"},
    {"title": "OpenAI takes on Microsoft with the launch of what feels a whole lot like ChatGPT's own office suite", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/09/29/openai-takes-on-microsoft-with-the-launch-of-what-feels-a-whole-lot-like-chatgpts-own-office-suite/"},
    {"title": "OpenAI expands ChatGPT's plug-ins with app-like interfaces and automations", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/09/29/openai-expands-chatgpts-plugins-with-app-like-interfaces-and-automations/"},
    {"title": "OpenAI gives Codex reusable cloud environments that work across devices", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/09/29/openai-gives-codex-reusable-cloud-environments-that-work-across-devices/"},
    {"title": "OpenAI's latest features take direct aim at the app store model", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/09/29/openais-latest-features-take-direct-aim-at-the-app-store-model/"},
    {"title": "OpenAI adds $500 Pro subscription, nerfs its existing $200 tier", "publisher": "Engadget", "url": "https://www.engadget.com/2272106/openai-adds-dollar500-pro-subscription-nerfs-its-existing-dollar200-tier/"}
  ],
  "editor_note": ""
}
---
OpenAIは現地時間9月29日の開発者会議DevDay 2026で、ChatGPTを仕事の場にするための機能をまとめて発表しました。チームとAIが同じ文書を編集する「Pages」と作業場「ChatGPT Space」、アプリのように動くプラグイン、Codexのクラウド環境、月500ドルの新プラン「Pro 500」が柱です。DevDay全体の発表は「[DevDay 2026の発表まとめ](/news/20260930-openai-devday-2026-roundup/)」をご覧ください。

## 何が発表されたか

### 文書・スライドとチーム機能

| 機能 | できること | 対象プラン | 状況 |
|---|---|---|---|
| ChatGPT Space | チーム、ChatGPT、Dotがファイルと文脈を共有する作業場 | Pro、Business、Enterprise | 提供開始 |
| Pages | 文章、調査、グラフ、画像を1つの文書で共同編集。接続したツールから内容を自動更新 | 同上 | 提供開始 |
| 共同編集スライド | 会話や自社テンプレートから作成し、PowerPointやGoogleスライドに書き出し | 同上 | 数週間内 |
| チームタスク | 週次報告などを定期実行、または新着メールやSlackの投稿を合図に実行 | Business、Enterprise | 提供開始 |
| Slack・Teamsの@ChatGPT | チャンネルで呼び出し、ライセンスのない同僚も会話に参加 | Business、Enterprise | 提供開始 |
| Meetingsプラグイン | 会議メモと次のアクションをSpaceに保存。音声はメモ作成後に削除 | Pro、Business | macOS版でベータ |

Pro、Business、Enterpriseでは、従来の「ライブラリ」がSpaceに置き換わります。作成と編集はWeb版とデスクトップ版が対象で、モバイルは当面、閲覧と共有のみです。共同編集できる表計算も近く加わります。Spaceで人と一緒に働くエージェント「Dots」については「[OpenAIが常時稼働エージェント「Dots」を開始](/news/20260930-openai-dots-always-on-agents/)」で解説しています。

### アプリ型プラグインと自動化

全プランで「プラグイン拡張」が使えるようになりました。外部のサービスがChatGPTのサイドバーに常駐し、会話の横で操作するパネルや独自形式のファイルを表示するビューアーを作れます。基調講演ではFigmaやAdobeの連携が紹介されました。

会話の流れに合わせてプラグインを薦める機能や、開発者が審査状況を追える新しい申請手順も加わります。接続先のアプリで起きた出来事を合図に自動処理を始める「MCP Events」にも対応しました。ChatGPTで作る簡易サイト「Sites」にもプラグインを載せられ、同僚が自分のデータと権限で使えます（Business、Enterprise、Edu、Healthcare）。

### Codexのクラウド環境

コーディングエージェントCodexは、手元のPC、スマートフォンからの遠隔操作、クラウドのどこでも動くようになりました。リポジトリや依存関係を設定した開発環境を保存して使い回せ、チームで承認済みの設定と権限を共有できます。各タスクは独立した作業領域で動き、PCがスリープ中でも作業を続けます。対象はPlus、Pro、Business、Enterprise、Edu、Healthcareです。

あわせて、音声で指示できるCLI、ChatGPTデスクトップ版でのコードレビュー、GitHubのリポジトリを定期スキャンして修正案まで用意する「Codex Security Cloud」も発表しました。

### Pro 500と料金プランの変更

| プラン | 月額 | Codexなどの利用枠（Plus比） | Ultrafast |
|---|---|---|---|
| Pro 100 | 100ドル | 5倍 | なし |
| Pro 200 | 200ドル | 10倍（既存契約者は10月29日まで20倍） | なし |
| Pro 500 | 500ドル | 25倍 | あり |

Ultrafastは、GPT-6 AstraをCodexで最大8倍（毎秒300トークン）の速さで動かす高速モードです。プランの利用枠を先に使い、使い切るとクレジット残高から引かれます。Pro 200は停止していた新規受付を再開しましたが、新規契約の利用枠は従来の半分になりました。Pro 100とPro 200の倍率は、OpenAIでCodexやChatGPTの製品責任者を務めるティボー・ソティオー氏がXで説明したもので、Pro 200の変更はEngadgetも報じています。

## 背景

TechCrunchは、PagesがGoogleドキュメントやWord、スライドがPowerPointに相当するとして、提携先のMicrosoftの主力事業に踏み込む動きだと指摘しました。別の記事では、ChatGPTの週12億人の利用者を足場に、アプリを見つけて使う場をChatGPTに移す狙いがあると分析しています。ただし、アプリストアのような課金・収益分配の仕組みは発表されていません。

## 反応と論点

アルトマンCEOは基調講演で、プラグイン拡張は「ChatGPTの中でネイティブに感じられる、実質的にアプリそのもの」だと説明しました（CNBC）。

Hacker Newsでは、Pro 500の発表スレッドで批判が目立ちました。月500ドルでも利用枠の上限があいまいなことや、Pro 200の枠の縮小に不満が集まっています。一方、月200ドルの契約を複数抱えるヘビーユーザーには1契約にまとめられて便利だという声もありました。DevDay全体のスレッドでは、文書やサイトまで1社に任せたくないとして、AI企業がアプリ層まで取り込むことを警戒する意見も出ています。

## 日本のビジネスへの影響

Space、Pages、プラグイン拡張について、地域を限る説明はありません。スライドはPowerPointやGoogleスライドに書き出せるため、Microsoft 365やGoogle Workspaceを使う日本企業でも既存の資料運用と両立しやすい設計です。一方、Meetingsプラグインは現時点でmacOS版アプリのみです。

マーケティング部門なら、接続ツールのデータで自動更新されるPagesを使った定例レポートや、週次報告のチームタスク化から試すのが現実的です。会議メモの自動作成を使う場合は、参加者への事前告知など社内ルールを整えておく必要があります。

Pro 200の契約者は、旧来の利用枠が保証される10月29日までに、Pro 500への移行も含めてプランを見直す必要があります。Proは月払いのみで、年払いはありません。
