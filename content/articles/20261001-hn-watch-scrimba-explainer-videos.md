---
{
  "title": "HN.watchはHacker Newsの記事を解説動画に、Scrimbaがクリックから数秒で生成",
  "description": "プログラミング学習のScrimbaが、Hacker Newsのトップページの記事を解説動画で見られるHN.watchを公開した。動画はHTMLのスライドとAI音声で組み立て、数秒で再生が始まる。ナレーションは日本語を含む33言語に対応する。",
  "date": "2026-10-01T18:32:00+09:00",
  "category": "usecases",
  "tags": ["Scrimba", "HN.watch", "活用事例", "動画生成", "音声合成", "教育"],
  "summary": [
    "HN.watchは、Hacker Newsのトップページの全記事に短い解説動画を付けたサイトで、Scrimbaが運営する",
    "HN.watchの動画はHTMLのスライドとAI音声で作り、最初に開かれたときに数秒で生成して全員で共有する",
    "基盤のScrimba ExplainはMCPやChrome拡張からも使え、ナレーションは日本語を含む33言語に対応する"
  ],
  "sources": [
    {"title": "Show HN: HN.watch – Videos of all Hacker News posts（作者の投稿）", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=49879401", "kind": "公式発表"},
    {"title": "hn.watch", "publisher": "Scrimba Docs", "url": "https://docs.scrimba.com/explain/hn-watch", "kind": "公式ドキュメント"},
    {"title": "What is Scrimba Explain?", "publisher": "Scrimba Docs", "url": "https://docs.scrimba.com/explain/introduction", "kind": "公式ドキュメント"},
    {"title": "Limits and plans", "publisher": "Scrimba Docs", "url": "https://docs.scrimba.com/explain/limits-and-plans", "kind": "公式ドキュメント"},
    {"title": "Languages", "publisher": "Scrimba Docs", "url": "https://docs.scrimba.com/explain/languages", "kind": "公式ドキュメント"},
    {"title": "Chrome extension", "publisher": "Scrimba Docs", "url": "https://docs.scrimba.com/explain/chrome-extension", "kind": "公式ドキュメント"},
    {"title": "Introducing Explain by Scrimba", "publisher": "YouTube @Scrimba", "url": "https://www.youtube.com/watch?v=k6rbHmBxSEs", "kind": "公式発表"}
  ],
  "thumb_text": "HN.watch",
  "share_text": "Hacker Newsの全記事を数秒で解説動画にするHN.watch。動画はHTMLのスライドとAI音声で組み立てる",
  "editor_note": ""
}
---
プログラミング学習サービスScrimbaの創業者Per Borgen氏は現地時間9月28日、Hacker News（HN）の記事を解説動画で見られるサイト「HN.watch」をShow HNで公開しました。動画は画像を描くAIではなくHTMLのスライドとAIの音声で組み立てるため、クリックから数秒で再生が始まると説明しています。投稿は215ポイントを集めました。

## 何を作ったか

HN.watchとは、HNのトップページを5分ごとに写し取り、全記事に短い解説動画を付けたサイトです。動画は記事ごとに1本で、最初にクリックした人のときに作られ、2人目以降はできあがったものを見ます。

解説の材料は記事本文とHNのコメント欄の2つだけで、ウェブ検索はしません。コメントが10件以上あれば、最後に「HNではこう言われている」という章が付き、意見が一致する点、割れる点、最も強い反論をまとめます。コメントした人の名前は出しません。記事が読めないときはコメント欄だけで作り、最初のスライドでそう断ります。

下はScrimbaの公式チャンネルにある、基盤の機能「Explain」の紹介動画です。

{{youtube:https://www.youtube.com/watch?v=k6rbHmBxSEs}}

## どう作ったか

HN.watchは、Scrimbaの解説動画の生成機能「Scrimba Explain」のデモです。Scrimbaはこの10年、HTMLで作る独自の動画形式でプログラミングを教えてきた会社で、そこにLLMをつないだとBorgen氏は説明しています。Explainの動画は画面録画ではなく、コードや差分、図、アニメーションをデータのまま並べたスライドにナレーションを重ねたものです。

使っているモデルはGemini、GPT、Inworld、ElevenLabsなどです。記事の取得にはFirecrawlを使い、読めないページはHNのコメントをAlgoliaのAPIで取って補います。アプリはCTOが作ったプログラミング言語Imbaと自社製の同期エンジンで組んでおり、学習データに少ない自社技術でもLLMはうまくコードを書けたといいます。

:::quote https://news.ycombinator.com/item?id=49879401 | Per Borgen氏のShow HN投稿（Hacker News）
> Our hypothesis is that if video creation goes from “dollars and minutes” to “cents and seconds”, a bunch of new use cases will be unlocked.
私たちの仮説は、動画づくりが「何ドル・何分」から「何セント・何秒」になれば、新しい使い道が一気に開けるというものです。
:::

## 成果（作者の公表値）

1本あたりの原価は、投稿本文では約0.04ドル（画像生成を除く）ですが、コメント欄では約0.4ドルと書いており、表記が揃っていません。目標は1分の動画を1セント・待ち時間1秒で作ることで、そのため高価なClaude Opus 5.5は使っていないとしています。社内では全てのプルリクエストに解説動画を付けているそうです。

Explain本体は、Web画面、ChatGPTのプラグイン、Chrome拡張、MCPサーバー（AIエージェントから呼び出す口）、プルリクエストに動画を付けるGitHub Actionから使えます。アカウントに残せる本数は、無料アカウントが通算10本、Proが月100本です。エージェントが台本を書くMCP経由の下書きは、何本作っても無料です。

## 反応と論点

HNの評価は割れました。運転中や自転車に乗る間にHNを追えて便利だという声や、教材設計の仕事で真似したいという声がある一方、文章で読める内容をAIの動画にする必要はない、型どおりの構成と声ですぐ単調に感じるという批判も目立ちました。Borgen氏は、声の選び方と見た目にはまだ改善の余地があると認めています。

## 日本のビジネスへの影響

ナレーションは日本語を含む33言語に対応し、英語で頼んでも「in Japanese」と付ければ日本語で作られます。Proの料金は公式ドキュメントに記載がありません。

関係が深いのは、製品資料やヘルプページを作るマーケターと、開発チームの責任者です。既存の記事を数秒で解説動画にできれば、LPや社内マニュアルに動画を添える手間が大きく減ります。プルリクエストの解説動画は、レビュー担当への説明にも使えます。

今すぐやれることは、自社ブログの記事1本を動画にして、日本語ナレーションの質と内容の正確さを確かめることです。注意点は公開範囲です。Web画面の初期設定は「公開」で、Chrome拡張で作った動画も公開になるため、社外秘の資料では作る前に限定公開か非公開を選んでください。Chrome拡張はページの最初の約1万2000字しか読みません。音声の選び方は[音声合成AIの比較](/best/text-to-speech/)にまとめています。
