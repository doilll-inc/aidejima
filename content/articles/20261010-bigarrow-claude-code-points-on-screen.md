---
{
  "title": "画面に大きな矢印を出して「ここを押して」、Claude Codeが操作を案内するMac用の無料ツール",
  "description": "Claude CodeやCodexが、Macの画面上に矢印と説明の札を重ねて「次に押すボタン」を指し示せる無料ツール「bigarrow」が公開された。Hacker Newsで378ポイントを集め、親への操作説明や手順書づくりに使えると反響を呼んでいる。",
  "date": "2026-10-10T11:50:00+09:00",
  "category": "usecases",
  "tags": ["bigarrow", "Claude Code", "Codex", "活用事例", "個人開発", "オープンソース"],
  "summary": [
    "Claude CodeやCodexが、Macの画面に大きな矢印と説明の札を出して、人に押してほしいボタンを指し示せる無料ツールが公開された",
    "ツールは指し示すだけで、クリックや入力、画面の撮影はしない。許可の確認や二段階認証など、人がやるべき操作を案内する",
    "作者は親にPDFの保存方法を教える例や、矢印入りの手順書PDFも公開し、Hacker Newsで378ポイントを集めた"
  ],
  "sources": [
    {"title": "big-arrow-on-the-screen（README）", "publisher": "GitHub franzenzenhofer", "url": "https://github.com/franzenzenhofer/big-arrow-on-the-screen", "kind": "公式サイト"},
    {"title": "Show HN: Let your AI agents paint big arrows, boxes and text on your screen", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=50018817", "kind": "コミュニティ"}
  ],
  "thumb_text": "bigarrow",
  "thumb_style": "3d",
  "thumb_prompt": "A giant glossy red 3D arrow bursting out of a laptop screen and pointing down at a tiny 'OK'-shaped blank button on the display, while an elderly person's hand hovers hesitantly over the trackpad.",
  "share_text": "Claude Codeが画面に矢印を出して「このボタンを押して」と教えてくれる。Mac用の無料ツールが話題",
  "editor_note": ""
}
---
AIに作業を任せていると、最後に「許可ボタンを押してください」とだけ表示されて、どこを押せばいいのか探す羽目になることがあります。そこで、Claude CodeやCodexがMacの画面いっぱいに大きな矢印と説明の札を出し、「このボタンです」と指し示せる無料ツール「bigarrow」が、現地時間10月9日に開発者向け掲示板のHacker Newsで紹介されました。投稿は378ポイント、165件のコメントを集めています。

## 何を作ったのか

bigarrowとは、Macの画面上のすべてのウィンドウの上に、透明な層を1枚重ねて矢印・枠・文字の札を描くツールです。GitHubの開発者franzenzenhofer氏が、MITライセンス（誰でも無料で使え、改変もできる条件）で公開しました。

AIエージェント（指示を受けて自分で作業を進めるAI）のClaude CodeやCodexに「技能」として組み込むと、AIが必要なときに自分で矢印を出します。たとえば「設定画面のこのスイッチをオンにして」「このタブです、ほかの13個ではありません」といった札を、対象のボタンのすぐ横に出せます。

作者はREADME（説明書き）で、作った理由を次のように書いています。

:::quote https://github.com/franzenzenhofer/big-arrow-on-the-screen | GitHub「big-arrow-on-the-screen」README
> What changed: agents now do real work on your Mac, and sooner or later hit a step **only a human may do**, or one the human wants to learn.
変わったのは、エージェントがMacで実際の仕事をするようになり、遅かれ早かれ「人にしかできない」操作や、人が覚えたい操作にぶつかるようになったことだ。
:::

## 何に使えるのか

わかりやすいのは、READMEに載っている母親への説明の例です。印刷画面に「PDFを押して、それからPDFとして保存」という札付きの矢印が出て、その横では小さな矢印が取り消しボタンを指し、「それじゃないよ」と添えています。家族のMacや画面共有での案内に、そのまま使える形です。

使い道は大きく2つに分かれます。1つは、AIが見つけても自分では押せない、押してはいけない操作です。権限の許可やログイン連携の同意、二段階認証や画像認証、支払いや署名がこれに当たり、確認コードやURLは札に付けたコピーボタンから貼り付けられます。もう1つは、人が操作を覚えたい場面です。3Dソフトなどの使い方を尋ねると、AIが押す場所を順に指していきます。READMEにはKeynoteでアニメーションを付ける3段階の例のほか、AIに矢印を描かせながら撮った画面で作った6ページの手順書PDFも公開されています。

## どう作られているか

本体は小さな1つのプログラムで、常駐する仕組みもアカウント登録もなく、作者は「中にAIは入っていない」と書いています。描くだけならMacの特別な許可は要りません。ボタンの名前やウィンドウの題名から位置を探すときだけ、アクセシビリティや画面収録の許可が必要です。

矢印はクリックを素通りさせ、入力中の文字を奪わず、時間が来るかAIの作業が終わると自動で消えます。104本の自動テストで確かめているとしています。

:::quote https://github.com/franzenzenhofer/big-arrow-on-the-screen | GitHub「big-arrow-on-the-screen」README
> It never clicks, types or captures. It only points.
クリックも入力も画面の撮影もしない。指し示すだけだ。
:::

## 反応と論点

Hacker Newsでは、電話で母親に書類のダウンロードや印刷を教えるときに役立ちそうだという声や、手順書の画面写真は「Xを押す」と書いてあっても結局Xを探すことになるので説明書づくりに向いている、という声がありました。

一方で、AIのためにボタンを押すだけなら最初から全権限を渡すのと変わらない、中身を理解せずに押すなら承認の意味がない、と人がAIの言いなりになることを懸念する意見も出ました。作者はREADMEで、AIが矢印で「拒否」ボタンを隠すといったいたずらについて、枠は輪郭だけで対象が見える、札が対象に重ならないよう配置するなどの対策をテストで確かめていると説明しています。

同じようにAIの使い方を個人が工夫した例として、[Codexに料理しながら話しかけて作業を進めた事例](/news/20261010-codex-voice-simon-willison-cooking/)も紹介しています。

## 日本のビジネスへの影響

- **必要なもの**: Mac（作者はmacOS 15・26・27で動作を確かめたとしています）と、Claude CodeかCodex。Homebrew（Macにソフトを入れる定番の道具）で入れ、付属の命令で技能をAIに組み込みます。札の文字は日本語でもAIに書かせられますが、日本語表示の見え方は作者が説明していないため、自分で試して確かめてください。
- **誰に効くか**: 社内のIT担当者や、社員向けの操作マニュアルを作る総務・人事の担当者です。AIに矢印を描かせながら画面を撮れば、手順書の画像づくりを短くできます。ソフトの営業やカスタマーサポートが、画面共有で顧客に操作を案内する場面にも向いています。
- **今すぐやれること**: すでにClaude Codeを使っている人は、まず「この設定画面のどこを押せばいいか矢印で教えて」と頼んでみると、使い勝手がわかります。Claude Codeの料金は[こちらの記事](/news/20261008-claude-code-pricing-plans/)で、ほかのコーディングAIとの比較は[コーディングAIのおすすめと料金比較](/best/coding/)でまとめています。
- **注意点**: Windowsには対応していません。また、AIが指したボタンをそのまま押す習慣がつくと、意味を確かめずに許可を出してしまうおそれがあります。作者によると技能は札に「押すと何が起きるか」を書かせる作りですが、権限の許可や支払いは画面の内容を自分で読んでから押すようにしてください。
