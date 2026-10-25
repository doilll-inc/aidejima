---
{
  "title": "n8nの使い方と料金、アプリ同士をつないで仕事を自動で回すツール 14日間無料で有料は月20ユーロから",
  "description": "n8nは、メールや表計算、チャット、AIなど500以上のサービスをつないで、決まった作業を自動で回すツール。料金は「自動処理を何回動かしたか」で決まり、年払いなら月20ユーロから。自社のサーバーで動かす版は無料。10月26日時点の公式情報で整理した。",
  "date": "2026-10-26T01:40:00+09:00",
  "category": "products",
  "format": "howto",
  "tags": ["n8n", "n8n Assistant", "使い方", "料金", "業務自動化", "エージェント"],
  "summary": [
    "n8nは、メールや表計算、チャット、AIなど500以上のサービスをつないで、決まった仕事を自動で回すツール",
    "料金は自動処理を動かした回数で決まり、ネット版は年払いで月20ユーロ（月2,500回）から。14日間は無料で試せる",
    "自社のサーバーで動かす無料版もあり、チャットで頼むと自動化の手順を組み立てる「n8n Assistant」も試験提供中"
  ],
  "sources": [
    {"title": "Plans and Pricing", "publisher": "n8n", "url": "https://n8n.io/pricing/", "kind": "公式ドキュメント"},
    {"title": "Choose how to use n8n", "publisher": "n8n Docs", "url": "https://docs.n8n.io/choose-how-to-use-n8n", "kind": "公式ドキュメント"},
    {"title": "Try free then choose a plan", "publisher": "n8n Docs", "url": "https://docs.n8n.io/deploy/use-n8n-cloud/start-your-free-trial", "kind": "公式ドキュメント"},
    {"title": "Build your first workflow", "publisher": "n8n Docs", "url": "https://docs.n8n.io/build-your-first-workflow", "kind": "公式ドキュメント"},
    {"title": "Use n8n Assistant", "publisher": "n8n Docs", "url": "https://docs.n8n.io/build/ways-of-building-workflows/n8n-assistant", "kind": "公式ドキュメント"},
    {"title": "Gateway credits", "publisher": "n8n Docs", "url": "https://docs.n8n.io/deploy/use-n8n-cloud/gateway-credits", "kind": "公式ドキュメント"},
    {"title": "Assistant credits", "publisher": "n8n Docs", "url": "https://docs.n8n.io/deploy/use-n8n-cloud/assistant-credits", "kind": "公式ドキュメント"},
    {"title": "n8n.io", "publisher": "n8n", "url": "https://n8n.io/", "kind": "公式サイト"}
  ],
  "thumb_prompt": "An office desk where colorful cardboard pipes connect an envelope, a spreadsheet printout and a chat bubble cushion, with small paper cards rolling through the pipes on their own while the chair stands empty.",
  "thumb_style": "illustration",
  "thumb_text": "n8n 使い方",
  "share_text": "n8nの使い方と料金。メールや表計算、AIをつないで仕事を自動で回すツール、14日間無料で有料は月20ユーロから",
  "editor_note": ""
}
---
n8n（エヌエイトエヌ）とは、メール・表計算・チャット・顧客管理・AIなど500以上のサービスをつなぎ、「この条件が来たら、これをして、次にこれをする」という決まった仕事を自動で回すためのツールです。ネット上で使う有料版は、年払いなら月20ユーロ（月払いは24ユーロ）から。14日間の無料体験があり、自社のサーバーに入れて動かす版は無料で使えます。この記事では、10月26日時点のn8nの公式料金ページと公式ドキュメントをもとに、何ができて、いくらかかり、どう始めるかを整理します。

## 何ができるか

n8nでは、自動化したい仕事の流れを「ワークフロー」と呼びます。画面上で四角い部品（ノード）を線でつないで組み立てる方式で、プログラムを書かなくても形にできます。必要なら、部品の中にJavaScriptやPythonのコードを入れることもできます。

主にできることは次の4つです。

- **サービス同士の連携**: 「問い合わせフォームに入力があったら、表計算に1行足し、担当者のチャットに通知する」といった流れを作れます。公式サイトによると、標準で用意された連携先は500以上あります
- **決まった時刻の実行**: 「毎朝8時にデータを集めて表にまとめる」のように、時刻を決めて自動で動かせます
- **AIの組み込み**: OpenAI（ChatGPTの開発元）、Anthropic（Claude）、Google（Gemini）などのAIを部品として入れ、メールの分類や要約、返信の下書きを流れの途中でさせられます。AIが自分で道具を選んで作業を進める「AIエージェント」も作れます
- **チャットで組み立てる**: 「n8n Assistant」に文章で頼むと、ワークフローを計画して作り、試しに動かして、エラーの直し方まで手伝います。現在は試験提供（プレビュー）です

:::quote https://docs.n8n.io/build/ways-of-building-workflows/n8n-assistant | n8n Docs「Use n8n Assistant」
> The result is a normal n8n workflow. You can open it, inspect it, edit it, test it, and publish it like any other workflow.
できあがるのは普通のn8nのワークフローです。ほかのワークフローと同じように、開いて中身を確かめ、編集し、試し、公開できます。
:::

AIが作った手順を、人が部品ごとに開いて確かめられるのがn8nの特徴です。公式も、試験提供中のAssistantは間違えることがあるので、本番で使う前に必ず中身を見直すよう呼びかけています。

## 料金とプラン

n8nの料金は、使う人数ではなく「ワークフローを最初から最後まで何回動かしたか（実行回数）」で決まります。途中の手順がいくつあっても1回と数えます。

:::quote https://n8n.io/pricing/ | n8n「Plans and Pricing」
> All plans include unlimited users & workflows and every integration. Pricing is based on monthly workflow executions, regardless of complexity.
どのプランも、利用者数とワークフローの数は無制限で、すべての連携先を使えます。料金は、ワークフローの複雑さに関係なく、毎月の実行回数で決まります。
:::

10月26日時点の公式料金ページ（ユーロ表示）では、次のとおりです。

| プラン | 年払い（月あたり） | 月払い | 月の実行回数 | 置き場所 |
|---|---|---|---|---|
| Starter | 20ユーロ | 24ユーロ | 2,500回 | n8nのネット版 |
| Pro | 50ユーロ | 60ユーロ | 1万回 | n8nのネット版 |
| Business | 667ユーロ | 800ユーロ | 4万回 | 自社のサーバーのみ |
| Enterprise | 個別見積もり | 個別見積もり | 個別 | どちらも可 |
| Community版 | 無料 | 無料 | ― | 自社のサーバー |

{{card:https://n8n.io/pricing/|Plans and Pricing|n8n}}

料金を選ぶときに押さえたい点は4つです。

- **回数の目安**: 公式の説明では、1日1回動かす流れは月30〜31回、5分ごとに動かす流れは月8,600〜8,900回になります。まずは1日数回の流れを数本、という使い方ならStarterの2,500回に収まります
- **無料体験は14日間**: カード登録なしで、Pro相当の機能を実行1,000回まで試せます。期限までに有料にしないと作業場所は削除されますが、作ったワークフローは90日以内ならダウンロードできます
- **AIの料金は別枠**: Assistantで組み立てる分は、プランに毎月付く「Assistantクレジット」（Starterは1,600、Proは4,000か9,600）を使います。ワークフローの中でChatGPTなどを動かす分は、各社と自分で契約して鍵（APIキー）を入れるか、n8nにお金を前払いして使う「Gatewayクレジット」で払います
- **小さな会社の割引**: 従業員20人未満なら、Businessプランが半額になるStart-up Planを申し込めます

無料のCommunity版は、公式ドキュメントで「ほぼすべての機能を無料で使える」と説明されています。ただし、サーバーの用意や更新、障害対応は自分たちで行います。公式も、技術に詳しい人がいない場合はネット版を勧めています。

## 始め方

ネット版で始める場合、公式の手順に沿うと最初の1本は次の5ステップです。

1. **無料体験を申し込む**: 料金ページの「Start free trial」から登録します。カードは不要です
2. **ワークフローを作る**: 「Create workflow」を選び、名前を付けます
3. **きっかけを決める**: 「毎日8時」などの時刻、フォームの送信、メールの受信など、流れを動かす合図（トリガー）の部品を置きます
4. **手順をつなぐ**: データを取ってくる部品、整える部品、表に書き込む部品などを線でつなぎます。最初はテンプレートを元にするか、Assistantに「〇〇したい」と頼んで下書きを作らせると早く進みます
5. **試して公開する**: 「Execute workflow」で試しに動かし、結果を確かめてから「Publish」で本番の自動実行に切り替えます

## 仕事での使いどころ

- **マーケター**: 広告やSNSの数字を毎朝集めて表にまとめ、前日から大きく動いた項目だけをチャットに通知する。問い合わせフォームの内容をAIで分類し、営業向けと採用向けに振り分ける
- **営業・カスタマーサポート**: 届いたメールをAIに要約させ、顧客管理の記録に貼り付けて、返信の下書きまで用意する。最終的な送信は人が確かめてから行う流れにできます
- **経営者・管理部門**: 請求書や申請のメールを集めて一覧にし、期日が近いものを週1回まとめて知らせる。人数で料金が増えないので、部署をまたいで同じ仕組みを共有しやすくなります

## 日本のビジネスへの影響

- **使えるか**: 日本からも申し込めます。料金はユーロ表示で、ネット版のデータはドイツ・フランクフルトのサーバーに保存されると公式に書かれています。説明書と画面は英語が基本です
- **誰に効くか**: 毎日同じ手作業をしているマーケターや営業事務、管理部門の担当者です。AIそのものより「AIを日々の仕事の流れに組み込む」部分を担うツールなので、ChatGPTやClaudeを個別に使うだけでは減らせなかった転記や通知の手間に効きます。AIで集客や広告運用をする方法は[マーケティングAIのガイド](/best/marketing/)にまとめています
- **今すぐやれること**: 14日間の無料体験で、毎日5分以上かけている「コピーして貼る」作業を1つ選び、Assistantに文章で頼んで自動化してみてください。月に何回動くかを数えれば、Starterで足りるかも判断できます
- **注意点**: 顧客情報や社内の資料を流す場合は、データがEUのサーバーに置かれることを社内の規程と照らし合わせてください。AIを組み込むと、n8nの月額とは別にAIの利用料がかかります。Assistantは試験提供中で間違えることがあるため、作られた手順は部品ごとに開いて確かめてから本番に切り替えるのが安全です
