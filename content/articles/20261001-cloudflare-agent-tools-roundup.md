---
{
  "title": "cf CLIやAuto Routerなど、Cloudflareがエージェント向けの新機能を相次ぎ発表",
  "description": "Cloudflareは9月28〜30日、AIエージェントが使う前提の新機能を相次いで発表した。全APIの3,000超の操作を扱う新CLI「cf」、起動を6倍速くしたContainers、モデルを自動で選ぶAI GatewayのAuto Routerなど5本をまとめる。",
  "date": "2026-10-01T18:32:00+09:00",
  "category": "dev",
  "tags": ["Cloudflare", "cf", "AI Gateway", "エージェント", "開発者", "クラウド"],
  "summary": [
    "Cloudflareの新CLI「cf」は全APIの3,000超の操作に対応し、出力は既定でJSON。オープンベータで公開された",
    "Containersは起動の中央値が4.049秒から648ミリ秒になり、作業環境のスナップショット保存もベータで始まった",
    "AI GatewayのAuto Routerは依頼ごとにモデルを選び、社内評価で1回の成功あたりの費用をOpus 5.5の約4割に抑えた"
  ],
  "sources": [
    {"title": "Introducing cf: the agentic CLI for the entire Cloudflare API", "publisher": "Cloudflare Blog", "url": "https://blog.cloudflare.com/cloudflare-cf-cli-launch/", "kind": "公式発表"},
    {"title": "Cloudflare Containers, rebuilt to scale agent sandboxes", "publisher": "Cloudflare Blog", "url": "https://blog.cloudflare.com/faster-agent-sandboxes/", "kind": "公式発表"},
    {"title": "Cut your AI spend with AI Gateway's Auto Router", "publisher": "Cloudflare Blog", "url": "https://blog.cloudflare.com/auto-router/", "kind": "公式発表"},
    {"title": "Identify AI model overuse with User Insights", "publisher": "Cloudflare Blog", "url": "https://blog.cloudflare.com/ai-model-overuse-user-insights/", "kind": "公式発表"},
    {"title": "Simplifying domains for people and agents", "publisher": "Cloudflare Blog", "url": "https://blog.cloudflare.com/simplifying-domains/", "kind": "公式発表"},
    {"title": "Auto Router（AI Gateway docs）", "publisher": "Cloudflare Docs", "url": "https://developers.cloudflare.com/ai-gateway/features/auto-router/", "kind": "公式ドキュメント"}
  ],
  "thumb_text": "cf CLI",
  "share_text": "Cloudflareがエージェント向け新機能を相次ぎ発表。全APIを扱う新CLI「cf」、6倍速いContainers、モデル自動選択のAuto Routerなど",
  "thumb_style": "3d",
  "thumb_prompt": "A shiny orange toolbox opened wide with many glowing new tools inside, and a small robot hand reaching in to pick one.",
  "editor_note": ""
}
---
Cloudflareは現地時間9月28日から30日にかけて、AIエージェントが使うことを前提にした新機能を公式ブログで相次いで発表しました。Cloudflareの全APIを扱える新しいコマンドラインツール「cf」、起動を6倍速くしたContainers、依頼ごとにAIモデルを自動で選ぶAI Gatewayの「Auto Router」などです。同じ週に発表した、AIが記事を使うたびにサイトへ対価を払う仕組みは「[Pay Per Use](/news/20261001-cloudflare-pay-per-use-beta/)」の記事で扱っています。

## 開発：新しいCLI「cf」（9月28日）

cfは、Cloudflareの全サービスをコマンドで操作するためのCLI（コマンドラインツール）です。これまでのCLI「Wrangler」で扱える操作は約280でしたが、cfはAPIの定義から自動でコマンドを作り、3,000を超える操作をカバーします。開発のきっかけは、エージェントによる利用の急増でした。

:::quote https://blog.cloudflare.com/cloudflare-cf-cli-launch/ | Cloudflare公式ブログ「Introducing cf: the agentic CLI for the entire Cloudflare API」
> In March 2026, agents were responsible for a quarter of Wrangler use, up from single-digit percentages the year prior. Last week, agent usage reached 48%.
2026年3月には、Wranglerの利用の4分の1をエージェントが占めていました。前年は1桁の割合でした。先週、エージェントによる利用は48%に達しました。
:::

- 出力は既定でJSON。エージェントが必要な項目だけを抜き出しやすくした
- `cf cli search`で、やりたいことを自然な文で書くと合うコマンドを探せる
- 設定ファイルは型付きのTypeScript（`cloudflare.config.ts`）に。`cf migrate`で移行できる
- 開発サーバーは既定でVite。インストールは`npm i -g cf`で、オープンベータ。ソースも公開
- ベータ終了後もWranglerは18か月間保守される

## 実行環境：Containersを作り直し（9月30日）

エージェントが作業ごとに使い捨てのLinux環境（サンドボックス）を作る使い方に合わせ、Containersの仕組みを作り直しました。新しい設定では、起動のたびにコードからイメージとマシンの大きさを選べます。第三者のComputeSDKの測定では、100個を同時に起動したときの中央値が4.049秒から648ミリ秒になりました。社内の予備試験では、1アカウントで10万個を6拠点に5.387秒で起動しています。

- 作業環境のファイルを保存して後で再開できるスナップショットをパブリックベータで開始
- Node.js入りの既製イメージ`cloudflare/debian-trixie`で、Dockerfileなしでも起動できる
- 従来の`Container`クラスなどの更新は2026年12月31日まで（既存の環境はその後も動く）。新機能は新しいAPIだけで使える

## AIの費用：Auto RouterとUser Insights（9月30日）

Auto Routerは、モデル名に`cloudflare/auto`を指定すると、依頼の内容を見て十分に賢く、安いモデルへ自動で振り分ける機能です。依頼を14の作業分類と、複雑さ・あいまいさ・重要度・文脈への依存の4項目で判定します。会話の途中でモデルを替えるとキャッシュ（再利用できる計算結果）が無駄になるため、その費用も計算に入れます。ベータの間は無料です。

| 社内のベンチマーク（291回） | 成功率 | 費用の合計 | 成功1回あたり |
|---|---|---|---|
| cloudflare/auto | 86.6% | $2.10 | $0.0084 |
| Claude Opus 5.5 | 96.6% | $5.91 | $0.0210 |
| GPT-6 Sol | 84.2% | $2.64 | $0.0108 |

メールや予定表、Slack、ファイルなどを使う日常業務97題を各3回解かせた結果で、Cloudflare自身の評価です。ブログは「パブリックベータ」としていますが、同じ日のUser Insightsの記事では「クローズドベータ」と書かれており、表記が揃っていません。

User Insightsは、AI Gatewayを通る社内のAI利用を分析する画面です。今回、作業に対して性能が高すぎるモデルが使われている会話と、その利用者やエージェントを示す表示が加わりました。作業の種類別の内訳や、終わるまでの往復回数も見られます。AI Gatewayの利用者は無料で使えますが、集計は約1日遅れます。

{{card:https://developers.cloudflare.com/ai-gateway/features/auto-router/|Auto Router（対象モデルと指定方法）|Cloudflare Docs}}

## ドメイン：検索と購入をエージェント対応に（9月30日）

ドメイン登録サービスCloudflare Registrarの検索を作り直し、対応する420以上の末尾（.comや.devなど）すべてで、入力した名前をそのまま表示するようにしました。登録用のAPIには、実際に買わずに試せるサンドボックスや、他社からの移管も加わりました。cfやMCP経由で、エージェントに空き確認から購入まで頼めます。

## 日本のビジネスへの影響

今回の発表に提供地域の制限は書かれておらず、日本のアカウントでも試せる見込みです。ただしcfはオープンベータ、Containersのスナップショット機能とAuto Routerもベータの段階です。

関係が深いのは、Cloudflare上でサービスを動かす開発者と、社内のAI利用費を管理する情報システム部門です。AI Gatewayを使っているなら、まずUser Insightsで性能が高すぎるモデルに流れている作業を確かめるのが手軽です。そのうえで社内ツール1つに`cloudflare/auto`を試し、品質と費用を今のモデルと比べてください。選ばれるモデルは`cf-aig-allowed-models`ヘッダーで社内で認めたものに絞れます。

注意点は、Auto Routerの成功率がClaude Opus 5.5より10ポイント低いことです。品質が重要な業務では、振り分け先を限るか対象から外す判断が要ります。データを保存しないモデルだけに絞る機能はまだなく、今後の予定とされています。各社APIの料金は「[AI API（LLM）の料金比較](/best/api/)」で比べられます。
