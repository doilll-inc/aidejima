---
{
  "title": "ClaudeのiPhoneアプリに「楽しく」と頼んだら3時間考えて木の間違い探しゲームが完成",
  "description": "米国の著名開発者Simon Willison氏が、スマホのClaudeアプリに数行の指示を出し、3時間7分かけて立体の木の間違い探しゲーム「Tree Appreciator」を作らせた。音楽や得点、図鑑まで付き、ブラウザで誰でも遊べる。",
  "date": "2026-10-15T17:55:00+09:00",
  "category": "usecases",
  "tags": ["Claude", "Tree Appreciator", "Claude Opus 5.5", "活用事例", "個人開発", "ゲーム"],
  "summary": [
    "米国の開発者Simon Willison氏は10月14日、ClaudeのiPhoneアプリに頼んで作らせた木の間違い探しゲームを公開した",
    "指示は数行で「楽しくて美しいものに」と添えただけ。Claudeは3時間7分考え続け、音楽や得点、集めた木の図鑑まで付けた",
    "Willison氏は9月の講演で「楽しいゲームはまだAIに作れない」と話していたが、「楽しく」と頼むと気まずいほどうまくいったと書いた"
  ],
  "sources": [
    {"title": "Tree Appreciator", "publisher": "Simon Willison's Weblog", "url": "https://simonwillison.net/2026/Oct/14/tree-appreciator/", "kind": "公式サイト"},
    {"title": "Tree Appreciator（ゲーム本体）", "publisher": "tools.simonwillison.net", "url": "https://tools.simonwillison.net/tree-appreciator", "kind": "公式サイト"},
    {"title": "2026 in LLMs so far", "publisher": "Simon Willison's Weblog", "url": "https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/", "kind": "公式サイト"}
  ],
  "thumb_prompt": "Two nearly identical miniature trees on a smartphone screen lying on a cafe table, one of them with a single tiny red bird hidden in its branches and a magnifying glass resting beside the phone.",
  "thumb_style": "diorama",
  "thumb_text": "Tree Appreciator",
  "share_text": "ClaudeのiPhoneアプリに数行頼んだら3時間考えて木の間違い探しゲームが完成。音楽も図鑑も付いていた",
  "editor_note": ""
}
---
AIの検証ブログで知られる米国の開発者Simon Willison氏は現地時間10月14日、スマートフォンのClaudeアプリに頼んで作らせたブラウザゲーム「Tree Appreciator（木を愛でる人）」を公開しました。指示は数行で、「楽しくて美しいものにするにはどうすればいいか、よく考えて」と添えただけです。Claudeは3時間7分かけて、音楽や得点、図鑑まで付いた間違い探しゲームを仕上げました。

## 何を作ったか

Tree Appreciatorは、ほとんど同じ2本の木を見比べて、違うところを探すゲームです。木はプログラムで毎回自動的に生えてくるので、同じ問題は二度と出ません。枝が1本ない、片方にだけ鳥がとまっている、ひと枝だけ早く紅葉している、といった違いを見つけてタップします。

木は立体で描かれていて、指でなぞると回せます。裏側に回らないと見えない違いもあり、ただの絵の間違い探しより探しがいがあります。ほかにも次のような要素がそろっています。

- 見つけるたびに100点、速さや連続正解でボーナス。外すと少し減点
- ヒントを使わず、ミスも少なく解くと「葉っぱ3枚」の評価
- 3組ごとに「どちらの木が高いか」を目で見て答える特別な回
- 解いた木は標本集に、見つけた違いの種類は図鑑に記録される
- 効果音と音楽、進み具合はブラウザに保存

ゲームは[Willison氏のサイト](https://tools.simonwillison.net/tree-appreciator)で公開されていて、パソコンでもスマホでも、最新のブラウザがあれば無料で遊べます。

## どう作ったか

Willison氏が使ったのは、iPhoneの標準のClaudeアプリです。プログラミング用の「Claude Code」ではなく、普段の会話の画面で、AnthropicのモデルClaude Opus 5.5に頼みました。

指示の中身は、「Tree appreciator」という名前のゲームを作ってほしいこと、2本の自動生成された木を見せて違いを味わうのが遊び方であること、そして楽しさと美しさをどう両立させるかよく考えてほしいこと、の3点だけです。Claudeは3時間7分考え続け、完成したゲームを返してきました。会話の全文は共有ページで公開されています。

{{card:https://simonwillison.net/2026/Oct/14/tree-appreciator/|Tree Appreciator|Simon Willison's Weblog}}

## 「楽しいゲームはAIには無理」と話した直後だった

Willison氏は9月27日の講演で、AIの作るゲームについて厳しい見方を示していました。見た目がゲームらしいものはAIで簡単に作れるが、遊び続けたくなるものは別だ、という指摘です。

:::quote https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/ | Simon Willison's Weblog「2026 in LLMs so far」
> Building a game that’s fun, has a good gameplay loop, and is challenging and interesting and keeps people coming back for more... that’s still beyond me, and beyond any of the agents I’ve tried.
楽しくて、遊びの流れがよくできていて、手応えがあって面白く、何度も戻ってきたくなるゲームを作るのは……まだ私にも、私が試したどのAIにもできない。
:::

それから3週間足らずで、本人がこう書いています。

:::quote https://simonwillison.net/2026/Oct/14/tree-appreciator/ | Simon Willison's Weblog「Tree Appreciator」
> Somewhat embarrassingly given my recent talk, I've found that telling Opus 5.5 "make sure it is fun" works uncomfortably well.
先日の講演を思うと少し気まずいが、Opus 5.5に「必ず楽しいものにして」と伝えると、居心地が悪いほどうまくいくとわかった。
:::

Willison氏は今回のゲームを「遊んでみるとかなり引き込まれる」と評価しています。同氏は10月上旬にも、Claudeにゲーム音楽を6曲作らせた実験を公開しており（[関連記事](/news/20261007-scrimshaw-jukebox-claude-game-music/)）、Claudeに遊びの要素を作らせる試みを続けています。

## 日本で真似するなら

**必要なもの**: Claudeのアプリ（スマホでもパソコンでも可）と、何を作りたいかの数行の説明です。プログラムを書く知識は必須ではありません。ただし、3時間も考え続けるような重い依頼は、無料プランの利用上限の範囲で終わらない可能性があります。プランごとの違いは「[Claudeとは](/news/20261013-claude-what-is-plans/)」の記事にまとめています。

**手順の目安**: ①作りたいものの名前と、遊び方を1〜2文で書く ②「楽しくて美しいものにするにはどうすればいいか、よく考えて」のように、仕上がりの質を求める一言を添える ③できあがったものを実際に触り、気になった点を追加で頼む、の順です。

**注意点**: Willison氏はAIの扱いに慣れた開発者で、同じ指示で同じ品質のものが毎回できるとは限りません。作ったものを社外に公開する場合は、使われている素材や音楽の権利も確かめてください。

## 日本のビジネスへの影響

**使えるか**: Claudeのアプリは日本語に対応していて、日本からも使えます。指示も日本語で書けます。

**誰にどう効くか**: 販促用のミニゲームや、研修・クイズの教材を作りたいマーケターや教育担当者に関係します。これまで外注していた「ちょっとした遊べるもの」の試作品を、会話だけで作れる段階に来ています。

**今すぐやれること**: 自社の商品や業務を題材にした簡単な間違い探しやクイズを、Claudeに「楽しくなるようによく考えて」と添えて頼んでみてください。試作品があれば、社内で企画を通す材料になります。仕事に使う対話AIの選び方は「[チャットAIのおすすめと料金比較](/best/chat/)」にまとめています。

**注意点**: AIに長く考えさせるほど、利用上限や費用を多く使います。本番で公開するものは、表示の崩れや不具合を人が確認してから出す必要があります。
