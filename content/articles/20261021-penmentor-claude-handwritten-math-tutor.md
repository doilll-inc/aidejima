---
{
  "title": "手書きの数式をClaudeが先生のように赤ペン添削、答えは言わずにヒントだけ 個人が自作して無料公開",
  "description": "ペンタブレットで解いている数学の答案に、Claudeなどが先生のように丸やチェックを書き込む道具「Penmentor」を個人開発者が10月20日に公開した。答えは教えずヒントを4段階で出し、図の動きで考え方も見せる。無料で、AIの月額プランの範囲で動く。",
  "date": "2026-10-21T18:10:00+09:00",
  "category": "usecases",
  "tags": ["Claude", "Penmentor", "Claude Code", "活用事例", "教育", "個人開発"],
  "summary": [
    "個人開発者のアブドゥラ・アルハリリ氏が、手書きの数学の答案をClaudeなどが画面上で添削する道具「Penmentor」を無料で公開した",
    "キー1つで最初の間違いに丸を付け、正しい行にはチェック。答えは教えず、軽いヒントから4段階で手助けを強める",
    "囲んだ式は動く図にして見せる。今はLinuxのパソコン専用で、利用者が契約しているClaudeなどのプランの範囲で動く"
  ],
  "sources": [
    {"title": "penmentor（README）", "publisher": "GitHub @AbdullahAlhariri", "url": "https://github.com/AbdullahAlhariri/penmentor", "kind": "公式サイト"},
    {"title": "penmentor: the full guide", "publisher": "GitHub @AbdullahAlhariri", "url": "https://github.com/AbdullahAlhariri/penmentor/blob/main/docs/guide.md", "kind": "公式サイト"},
    {"title": "Show HN: Penmentor – Claude marks up your handwritten math like a teacher", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=50167604"}
  ],
  "thumb_prompt": "A handwritten calculus page on a tablet screen with a stylus resting beside it, where a glowing red ink circle and green tick marks appear to be drawn by an invisible teacher's hand floating above the page.",
  "thumb_style": "illustration",
  "thumb_text": "Penmentor",
  "share_text": "手書きの数学の答案に、Claudeが先生のように丸とチェックを書き込む。答えは言わずヒントだけ出す道具を個人が無料公開",
  "editor_note": ""
}
---
個人開発者のアブドゥラ・アルハリリ氏は現地時間10月20日、ペンタブレットで手書きした数学の答案を、AnthropicのClaudeなどのAIが先生のように画面上で添削する道具「Penmentor（ペンメンター）」を、開発者向け掲示板Hacker Newsで公開しました。キーを1つ押すと最初の間違いに丸が付き、答えそのものは教えずにヒントだけを出します。

## 何を作ったか

Penmentorとは、手書きのノートアプリで数学を解いている途中に呼び出す「家庭教師役」の道具です。AIは文章で長々と説明する代わりに、画面に直接、色ペンで書き込むように答えます。

- **添削**: 最初の本当の間違いを丸で囲んで直し方を添え、正しい行にはチェック、その間違いを引きずった後の行には下線を引く
- **ヒントの段階**: 「軽い一押し」→「使う解き方の名前」→「次の1行をうっすら見せる」→「完全な修正」と、頼むたびに1段ずつ手助けを強める
- **復習**: 自分の答案の大事な1〜2か所について質問を出す、似た問題に間違いを1つ仕込んで見つけさせる、どの解き方が合うかを選ばせる
- **動く図**: 式を四角で囲むと、数学解説で人気のYouTubeチャンネル「3Blue1Brown」が使っている作図の仕組みで、動かせる図を作る。区間をドラッグすると面積の近似が変わる様子などを見られる

書き込みは、そのまま書き続けても画面に残り、Escキーで消えます。アルハリリ氏はREADME（説明書き）の冒頭で、この道具を次のように紹介しています。

:::quote https://github.com/AbdullahAlhariri/penmentor | GitHub「penmentor」README
> Press a key while you work by hand: Claude, Gemini or GPT marks your work on the screen like a teacher with coloured pens, gives you hints instead of answers, and shows the idea as a 3Blue1Brown-style animation.
手で解いている途中にキーを押すと、Claude、Gemini、GPTが色ペンを持った先生のように画面上であなたの答案に印を付け、答えの代わりにヒントを出し、考え方を3Blue1Brown風の動く図で見せてくれる。
:::

{{card:https://github.com/AbdullahAlhariri/penmentor|penmentor|GitHub}}

## どう作ったか

きっかけは、アルハリリ氏自身の勉強の不便さでした。微積分をペンタブレットで解きながら、答案をスクリーンショットしてClaudeに送り、返ってくる長い文章を読む、という使い方を繰り返していたといいます。READMEでは、欲しかったのは「肩越しにのぞき込んで、間違いに丸を付け、合っている所にチェックを付けてくれる先生」だったと書いています。

仕組みは次のとおりです。キーを押すと、画面のスクリーンショットと、手書きノートアプリ「Xournal++」で開いているページ全体がAIに送られます。AIは「何を読み取ったか」「判定」「印を付ける場所」を決まった形式で返し、Penmentorがその印を手書きの線に合わせて画面に重ねて描きます。

AIには、利用者がすでに契約しているサービスを使います。設定で選べるのは、AnthropicのClaude Code、OpenAIのCodex、GoogleのAntigravityの3つで、利用者がすでに持っている契約の範囲で動きます。Penmentor自体は自由に使えるMITライセンスで、無料です。説明書きによると、質問の合間に裏で何かを送ることはないとしています。

## 反応と論点

Hacker Newsでは60ポイント超を集めました。「仕組みがきれい」「図の機能がすばらしい」といった感想のほか、「ホームスクーリング（家庭での学習）に使ってみたい」という声もありました。

一方で、すぐに誰でも使える段階ではありません。動くのはLinuxというOSのパソコンだけで、さらに画面の管理方式にも条件があります。作者自身も掲示板で、自分のパソコン環境に強く合わせた作りだと認め、ほかの環境で使いたい人に希望を尋ねていました。対応するAIを増やせないかという質問には「まだだが、あるとよい機能」と答えています。

公開されているデモ動画も、録画を毎回同じにするため、ペンの動きとAIの答えは用意した例だと注記されています。実際の添削の正確さを示す数字は公開されていません。

AIデジマでは、Claudeに短い依頼をして遊べるものが仕上がった例も紹介してきました（[ClaudeのiPhoneアプリで木の間違い探しゲームが完成](/news/20261015-claude-iphone-tree-appreciator-game/)）。今回は「作る」ではなく「教わる」側の使い方で、AIに答えを言わせない設計にしている点が違います。

## 日本で真似するなら

- **必要なもの**: Linuxのパソコンとペンタブレット、Claude Code（Claudeの月20ドルのPro以上で使える）、Codex、Antigravityのいずれかにログインした状態。WindowsやMacでは今のところ動きません
- **普段のClaudeで同じ考え方を試す**: 手書きの答案の写真をClaudeのアプリに送り、「答えは言わず、最初の間違いの場所だけ教えて」「ヒントは1段ずつ」と頼めば、Penmentorの「答えより先にヒント」という教え方に近い形を試せます
- **注意点**: 画面全体のスクリーンショットがAIに送られるため、ほかのウィンドウに個人情報や社外秘の資料を開いたまま使わないことです

## 日本のビジネスへの影響

- **使えるか**: Penmentorは日本からも無料で入手できますが、Linux専用で、設定にはパソコンの知識が要ります。説明書きでは画面に映っている数式なら何でも読むとしており、日本の数学の答案でも試す余地があります
- **誰に効くか**: 学習塾や通信教育の企画担当者、社内研修の担当者です。「答えを教えずに、間違いの場所と段階的なヒントだけ返す」という設計は、AIを使った学習サービスの考え方としてそのまま参考になります
- **今すぐやれること**: 自社の教材の問題を1問選び、Claudeなどに「最初の間違いだけ指摘し、ヒントは4段階で」と指示して、生徒役の誤答に対する返し方を確かめてみることです。道具選びは[AIチャットの用途別ガイド](/best/chat/)を参考にしてください
- **注意点**: AIの添削が正しいとは限りません。作者も正確さの数字は示していないので、教材として出す前に、先生が確かめる工程を必ず残す必要があります。生徒の答案をAIに送る場合は、保護者への説明や利用規約の確認も必要です
