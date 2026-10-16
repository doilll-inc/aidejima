---
{
  "title": "スマホ2台が「音」でつながる対戦ゲーム、Claude Codeに一文頼んだらWi-Fiなしで動いた",
  "description": "米国の開発者サイモン・ウィリソン氏が10月15日、スマホ2台が音で通信して遊ぶ対戦ゲーム「Chirp Pong」を公開した。Claude Codeへの一文の依頼から作ったもので、Wi-FiもBluetoothも使わず、1秒に80ビットの情報を音でやり取りする。",
  "date": "2026-10-16T18:40:00+09:00",
  "category": "usecases",
  "tags": ["Claude Code", "Chirp Pong", "Claude Opus 5.5", "活用事例", "個人開発", "ゲーム"],
  "summary": [
    "米国の開発者サイモン・ウィリソン氏が、スマホ2台が「ピロピロ」という音で通信して遊ぶ対戦ゲームをClaude Codeで作った",
    "Wi-FiもBluetoothもアカウントも使わず、ブラウザーで開くだけで遊べる。2台のスマホを数センチ離して置く",
    "依頼は英語の1文だけで、ゲームは約2,900行のWebページ1枚にまとまっている。誰でも無料で遊べる"
  ],
  "sources": [
    {"title": "Chirp Pong", "publisher": "Simon Willison's Weblog", "url": "https://simonwillison.net/2026/Oct/15/chirp-pong/", "kind": "公式サイト"},
    {"title": "Chirp Pong（ゲーム本体）", "publisher": "tools.simonwillison.net", "url": "https://tools.simonwillison.net/chirp-pong", "kind": "公式サイト"}
  ],
  "thumb_prompt": "Two smartphones lying top to top on a café table, a glowing ping-pong ball flying between their screens, with visible colorful sound waves arcing from one phone's speaker to the other instead of any cables or wireless symbols.",
  "thumb_style": "photo",
  "thumb_text": "Chirp Pong",
  "share_text": "Claude Codeに一文頼んだら、Wi-Fiを使わず音でつながるスマホ対戦ゲームが完成。米開発者のウィリソン氏が公開",
  "editor_note": ""
}
---
米国の開発者サイモン・ウィリソン氏は現地時間10月15日、スマホ2台が音で情報をやり取りして遊ぶ対戦ゲーム「Chirp Pong」をブログで公開しました。AnthropicのプログラミングAI「Claude Code」に英語で1文の依頼を出して作ったもので、Wi-FiもBluetoothも使いません。

## 何を作ったか

Chirp Pongは、昔ながらのテニスゲーム「ポン」を2人で遊べるようにしたものです。それぞれのスマホが卓球台の半分になり、画面の上の端から出たボールが相手のスマホの画面に飛び込みます。通信には、スピーカーから鳴らす「チャープ」（鳥のさえずりのような短い音）と、相手のマイクを使います。

ウィリソン氏はブログで、作った狙いと結果を次のように書いています。

:::quote https://simonwillison.net/2026/Oct/15/chirp-pong/ | Simon Willison's Weblog「Chirp Pong」
> I wanted to see if it was feasible to have a two player game on two separate phones running in static HTML where the networking code uses chirps sent via the microphone. It seems to work!
別々のスマホ2台で、通信にはマイクで拾うチャープ音を使う2人対戦ゲームを、サーバーのいらないWebページだけで作れるか試したかった。どうやら動くようだ。
:::

遊び方は簡単です。2台で同じページを開き、音量を上げてマナーモードを切り、スマホの上の端どうしを数センチ離して置きます。片方が「Call」を押すと、もう片方が自動で応答して試合が始まります。アプリのインストールもアカウント登録もいりません。

ただのポンではありません。ボールに回転をかけたり、上にはじいてスマッシュしたりできます。ラリーが6回続けば得点が2倍、12回なら3倍になり、ゲージがたまると相手のコートに爆弾を落とせます。1人で練習できるコンピューター対戦もあります。

{{card:https://tools.simonwillison.net/chirp-pong|Chirp Pong|tools.simonwillison.net}}

## どう作ったか

ウィリソン氏がClaude Codeに出した依頼は、ブログに載っている英語の1文だけです。2人がスマホを近くに置き、ゲームの状態をWebのマイク機能が聞き取れる音で送り合うポン風の対戦ゲームを作ること、そのうえで見た目と遊び方にひねりを加えてポンよりずっと楽しくすること、という中身です。使ったモデルは「Claude Opus 5.5」で、作業の記録も公開しています。

できあがったゲームは、約2,900行のWebページ1枚にまとまっています。AIデジマがページの中身を確かめたところ、音でのやり取りは次のような仕組みでした。

- **2人の声域を分ける**: 1人目は約1,400〜3,000ヘルツ、2人目は約3,400〜5,000ヘルツの音を使い、同時に鳴らしても混ざらないようにしている
- **18種類の音で文字を作る**: 17の音で情報を、残り1つの音で「ここから始まる」という合図を表す。50ミリ秒ごとに音を切り替え、1秒に80ビットを送る
- **聞き間違いを見つける**: 1回分の情報の最後に確認用の数字を付け、周りの雑音で音を聞き違えたら捨てる

1秒80ビットは、昔の電話回線の通信と比べてもずっと遅い速さです。それでもボールの位置や得点のような小さな情報なら十分で、その制約の中で遊べるゲームの形まで、AIが組み立てたことになります。

## 背景

ウィリソン氏は、AIを使った小さな道具やゲームを作ってはブログで公開している開発者です。10月10日には、料理をしながらOpenAIのCodexに話しかけてブログの新機能を作った様子も紹介しました（[Codexに料理しながら話しかけてブログの新機能を完成](/news/20261010-codex-voice-simon-willison-cooking/)）。

AIデジマでは前日にも、ClaudeのiPhoneアプリに「楽しく」と頼んだら木の間違い探しゲームが完成した例を紹介しています（[ClaudeのiPhoneアプリで木の間違い探しゲームが完成](/news/20261015-claude-iphone-tree-appreciator-game/)）。短い依頼から、遊べるものが1回で出てくるのは珍しくなくなってきました。

## 日本で真似するなら

- **必要なもの**: Claude Codeは、Claudeの有料プラン（月20ドルのPro以上）で使えます。料金の詳細は「[Claude Codeの料金は月20ドルのProから](/news/20261008-claude-code-pricing-plans/)」にまとめています。作ったWebページを置く場所も必要ですが、静的なページなら無料の公開サービスで足ります
- **依頼の出し方**: 今回の依頼は「何を作るか」「どんな制約で作るか（音で通信）」「どこまで凝るか（ずっと楽しく）」の3つが1文に入っていました。日本語で同じように書いても試せます
- **注意点**: 音を使うので、静かな場所でないと聞き取りに失敗しやすくなります。また、ウィリソン氏自身も「どうやら動く」と書いているように、試作品です。お客さま向けに使うなら、さまざまな機種で動くか確かめる必要があります

## 日本のビジネスへの影響

- **使えるか**: ゲームは日本からもブラウザーで無料で遊べます。Claude Codeも日本から使えます
- **誰に効くか**: 店頭イベントや展示会の企画担当者、販促キャンペーンを考えるマーケターです。「スマホを2台近づけると遊べる」「アプリ不要」といった仕掛けを、外注せずに試作できます
- **今すぐやれること**: まず2台のスマホでChirp Pongを遊んでみて、音で通信する仕掛けが会場の騒がしさでどこまで使えるかを確かめることです。自社の企画で試すなら、Claude Codeに「目的・制約・凝り具合」を1文で伝えるところから始められます。道具の選び方は[コーディングAIの用途別ガイド](/best/coding/)を参考にしてください
- **注意点**: マイクを使うページは、ブラウザーが利用者に許可を求めます。イベントで使うなら、マイクの許可を求める理由を画面で説明しておくと、来場者が戸惑いません
