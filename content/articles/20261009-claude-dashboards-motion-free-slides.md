---
{
  "title": "無料版のClaudeでもスライドや資料作りが可能に、社内データの集計画面や解説アニメも登場",
  "description": "Anthropicは10月8日、Claudeの資料・スライド・デザイン作成機能を無料版を含む全プランで正式提供にした。社内データから自動更新の集計画面を作る「Dashboards」と、30秒ほどの解説アニメを作る「Motion」も試験提供を始めた。",
  "date": "2026-10-09T11:05:00+09:00",
  "category": "products",
  "tags": ["Claude", "Claude Dashboards", "Claude Motion", "Anthropic", "資料作成", "新機能"],
  "summary": [
    "Claudeの文書・スライド・デザインを作る機能が10月8日に試験版を卒業し、無料版を含む全プランで使えるようになった",
    "有料版では、社内のデータベースや営業管理ツールにつなぎ、言葉で頼むだけで自動更新の集計画面を作る「Dashboards」が試験提供に",
    "法人向けプランでは、報告書から短い解説アニメを作りMP4で書き出す「Motion」も始まった。動画生成AIではなく、人物の映像は作らない"
  ],
  "sources": [
    {"title": "Build live dashboards and animate explainers with Claude", "publisher": "Claude（Anthropic）", "url": "https://claude.com/resources/articles/dashboards-and-motion", "kind": "公式発表"},
    {"title": "Claude Design 移行ガイド", "publisher": "Claude ヘルプセンター", "url": "https://support.claude.com/en/articles/17440474", "kind": "公式ドキュメント"},
    {"title": "Claude can now generate animated explainer videos and live data dashboards from text prompts", "publisher": "The Decoder", "url": "https://the-decoder.com/claude-can-now-generate-animated-explainer-videos-and-live-data-dashboards-from-text-prompts/", "kind": "報道"}
  ],
  "thumb_text": "Claude Dashboards",
  "thumb_style": "3d",
  "thumb_prompt": "A conference room table where a stack of plain paper reports is morphing into a glowing, animated bar chart that rises off the page like a pop-up book, while a laptop beside it plays a short colorful explainer animation.",
  "share_text": "Claudeのスライド・資料作成が無料版でも正式に。社内データの集計画面や30秒の解説アニメを作る新機能も",
  "editor_note": ""
}
---
Anthropicは現地時間10月8日、対話AI「Claude」で文書・スライド・デザインを作る機能を試験版から正式版にし、無料版を含むすべてのプランで使えるようにしました。あわせて、会社のデータから自動で更新される集計画面（ダッシュボード）を作る「Claude Dashboards」と、短い解説アニメを作る「Claude Motion」の試験提供を始めました。Anthropicによると、これまでにClaudeで作られた文書・スライド・デザインは4,500万件を超えています。

## 何が発表されたか

発表は3つに分かれます。誰が使えるかがそれぞれ違うので、表にまとめます。

| 機能 | 何ができるか | 使えるプラン |
|---|---|---|
| Docs・Slides・Design | 会話の中で文書、スライド、デザインを作って編集する | 無料版を含む全プラン（正式版） |
| Claude Dashboards | 社内のデータにつなぎ、言葉で頼むと集計画面を作り、データの変化に合わせて更新する | 有料プラン（試験提供） |
| Claude Motion | 報告書やグラフから短い解説アニメを作り、MP4の動画で書き出す | Team・Enterprise（試験提供） |

### 集計画面を「頼むだけ」で作るDashboards

Claude Dashboardsとは、BigQuery・Snowflake・Databricksといった企業のデータ基盤や、Salesforceのような営業管理ツールにClaudeをつなぎ、「今週の登録者数を先月と比べて」と普通の言葉で聞くと、グラフ入りの集計画面を作る機能です。画面はデータが変わるたびに最新の数字に更新され、各グラフにはいつ更新したかが表示されます。

数字の根拠を確かめられる点も特徴です。公式発表によると、画面上のどの数字をクリックしても、その数字を出すためにClaudeが書いたデータベースへの問い合わせ文（SQL）が見られ、Claudeに意味を説明させることもできます。もっと深い分析をしたいときは、AmplitudeやMixpanel、Hexなどの分析ツールへ画面ごと送れます。LookerやTableau、monday.comにも近く対応するとしています。

### 報告書を30秒のアニメにするMotion

Claude Motionは、四半期の報告を全社集会向けの30秒の解説にする、役員会の資料のグラフに動きを付ける、といった用途を想定した機能です。できたアニメは短い動画のように再生され、編集画面で直すか、Claudeに直しを頼んだあと、MP4の動画ファイルとしてダウンロードできます。

:::quote https://claude.com/resources/articles/dashboards-and-motion | Claude公式「Build live dashboards and animate explainers with Claude」
> It doesn’t use a video generation model, so there’s no generated footage and no AI-generated people.
動画生成モデルは使わないので、AIが生成した映像も、AIが生成した人物も出てこない。
:::

つまりMotionは、文字・数字・図形・画像をプログラムで動かす仕組みで、どの言葉、どの数字、どのタイミングも後から変えられます。仕上げをしたいときは、AdobeやDescript、HeyGen、Runwayなどの動画編集ツールで開けます（CanvaとCaptionsにも近く対応）。

{{card:https://claude.com/resources/articles/dashboards-and-motion|Build live dashboards and animate explainers with Claude|Claude（Anthropic）}}

## 正式版になった資料作りの変更点

Docs・Slides・Designは、9月16日からClaudeのすべての会話の中で使えるようになっていました。今回「試験版」の表示を外し、あわせて次の点を改めたとしています。

- PowerPointとPDFの書き出しが、編集画面での見た目どおりになる。スライドはGoogleスライドに編集できる形で送れる
- チームのメンバーとClaudeが、同じ文書やスライドを一緒に編集できる
- 管理者が許せば、社外の人やリンクを知っている人にも共有できる
- スマートフォンのClaudeアプリから文書やスライドを直せる

一方、もともと専用のページ（claude.ai/design）で提供していた「Claude Design」は、Claude本体に統合して12月14日に閉じます。移行ガイドによると、専用ページでのClaudeとの会話やコメントは引き継がれず、専用ページの作品の公開リンクもその時点で使えなくなります。

## 背景

Anthropicは資料作りの機能を急いで広げています。10月6日にはGoogleドキュメント・スプレッドシート・スライドとの連携を発表し、10月7日には安い小型モデル「Claude Haiku 5.5」も出しました（[既報](/news/20261008-anthropic-claude-haiku-5-5/)）。今回の発表は、チャットで答えを返すAIから、そのまま会議に出せる成果物を作るAIへ、という流れの続きです。GoogleもGeminiに仕事を丸ごと任せる企業向けの仕組みを前日に発表しています（[既報](/news/20261009-google-gemini-agent-work/)）。

## 反応と論点

公式発表は、Dashboardsを「ちょっとした疑問をその場で調べる」ための機能と位置づけ、本格的な分析は既存の分析ツールに渡す前提で設計しています。数字ごとに問い合わせ文を見せるのも、AIの集計をそのまま信じず、人が確かめられるようにするためです。

Motionで動画生成AIを使わないと明言したことには、意味があります。社内の報告や営業資料に、実在しない人物や作り物の映像が紛れ込む心配がありません。半面、映画のような映像や人物が話す動画はMotionでは作れないので、その用途は別の動画AIを使うことになります。

企業の管理者向けには、DashboardsとMotionは初期設定で「オフ」になっており、組織の設定から有効にする必要があります。Docs・Slides・Designは10月15日に自動で有効になります。

## 日本のビジネスへの影響

- **使えるか**: Claudeは日本でも提供されており、資料・スライド作成は無料版から使えます。Dashboardsは有料プラン、MotionはTeam・Enterpriseプラン限定で、どちらも試験提供です。料金はドル建てで、Proは月20ドル（年払いなら月17ドル相当）です
- **誰にどう効くか**: 毎週の数字報告に追われるマーケターや営業企画の担当者は、Dashboardsで「先週の問い合わせ数を地域別に」と頼むだけで、更新され続ける集計画面を持てます。広報や経営企画は、決算や事業計画の説明をMotionで短いアニメにして、社内向けの説明会や採用説明に使えます
- **今すぐやれること**: 無料版のClaudeで、来週の会議資料のメモを貼り「この内容で5枚のスライドに」と頼み、PowerPointに書き出して自社の形式にどこまで合うかを試してください。Claude Designを専用ページで使っている人は、12月14日までに会話やコメントを手元に残しておく必要があります
- **注意点**: Dashboardsは社内のデータ基盤に接続するため、情報システム部門の許可と、どのデータをClaudeに見せるかの線引きが先に必要です。AIが作った集計は、数字をクリックして根拠を確かめてから共有してください

スライド作成AIの料金や向き不向きは、[AI資料作成・スライド生成のおすすめと料金比較](/best/slides/)にまとめています。
