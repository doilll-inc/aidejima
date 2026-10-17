---
{
  "title": "AIの点検でバグが見つかりすぎた、データベース「PostgreSQL」新版が機能を外して公開も延期",
  "description": "無料のデータベース「PostgreSQL」の新版19から、ほぼ完成していた機能が8〜10個外された。中心開発者はAIによるコード点検で細かな不具合が一度に約40件見つかり、直す時間が足りなかったと説明する。公開予定日も11月19日に延びた。",
  "date": "2026-10-17T17:00:00+09:00",
  "category": "dev",
  "tags": ["PostgreSQL", "PostgreSQL 19", "オープンソース", "開発者", "コーディング"],
  "summary": [
    "企業の業務システムで広く使われる無料のデータベース「PostgreSQL」の新版19から、主な機能が8〜10個外された",
    "中心開発者は、AIによるプログラムの点検で古い機能の細かな不具合が一度に約40件見つかり、期限までに直しきれなかったと説明している",
    "開発チームは修正の量が多いとして、10月を予定していた正式公開を11月19日に延ばした"
  ],
  "sources": [
    {"title": "The reverts will continue until morale improves", "publisher": "Peter Eisentraut", "url": "https://peter.eisentraut.org/blog/2026/10/09/the-reverts-will-continue-until-morale-improves", "kind": "公式サイト"},
    {"title": "Updated PostgreSQL RC / GA dates", "publisher": "PostgreSQL（pgsql-hackers）", "url": "https://www.postgresql.org/message-id/f161fbb7-e193-42eb-bec7-4cfc1af74a50%40postgresql.org", "kind": "公式ドキュメント"},
    {"title": "PostgreSQL 19 RC 1 Released!", "publisher": "PostgreSQL", "url": "https://www.postgresql.org/about/news/postgresql-19-rc-1-released-3409/", "kind": "公式発表"},
    {"title": "Roadmap", "publisher": "PostgreSQL", "url": "https://www.postgresql.org/developer/roadmap/", "kind": "公式ドキュメント"},
    {"title": "Postgres 19 delayed after AI reviewers find more bugs than humans can fix", "publisher": "The Register", "url": "https://www.theregister.com/databases/2026/10/16/postgres-19-delayed-after-ai-reviewers-find-more-bugs-than-humans-can-fix/5303471", "kind": "報道"},
    {"title": "Hacker News のスレッド", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=50119991", "kind": "コミュニティ"}
  ],
  "thumb_prompt": "A small team of tired workers in a repair shop staring at a conveyor belt where a tireless robot inspector keeps stamping red tags on hundreds of nearly finished machines, the pile of tagged machines growing taller than the workers.",
  "thumb_style": "illustration",
  "thumb_text": "PostgreSQL 19",
  "share_text": "AIの点検でバグが見つかりすぎて直す人が足りない。PostgreSQL 19が機能を8〜10個外して公開を延期",
  "editor_note": ""
}
---
企業の業務システムやWebサービスの裏側で広く使われている無料のデータベース「PostgreSQL（ポストグレスキューエル）」の新版19で、ほぼ完成していた機能が8〜10個まとめて外されました。中心開発者の1人は、AIを使ったプログラムの点検で細かな不具合が一気に見つかり、直す時間が足りなかったことが理由の1つだと説明しています。正式公開の予定日も11月19日に延びました。

## 何が起きたか

PostgreSQLとは、顧客名簿や受注データなどを保存・検索するための「データベース」と呼ばれるソフトで、世界中の有志と企業が共同で開発し、誰でも無料で使えます。毎年秋に大きな新版を出しており、今年は19の番です。

開発に長く関わるピーター・アイゼントラウト氏（PostgreSQLの支援企業EDBの幹部）は、現地時間10月9日に自身のブログで、新版19の試用版（ベータ版）が出たあとに外された機能が「数え方にもよるが8〜10個」にのぼると明かしました。例年なら1回の開発で1つ外れるかどうかで、今回は試用期間の終盤に外れたものもあるといいます。同氏自身も、外された機能のいくつかの開発者や取りまとめ役でした。

外された理由は1つではありません。設計の根本に欠陥があり、試用期間中に直すのが難しかった機能もありました。ただ同氏は、それとは別に「害の小さい、珍しい条件のときだけ起きる不具合」が大量に見つかったことを挙げ、その原因をAIの点検に結びつけています。

:::quote https://peter.eisentraut.org/blog/2026/10/09/the-reverts-will-continue-until-morale-improves | Peter Eisentraut「The reverts will continue until morale improves」
> But with LLM-assisted code review, these kinds of things can get found much faster, and then you’re staring at a list of like forty defect reports. And even if each of them requires only a three-line fix on average, there is a fixed overhead to dealing with each of these, and then you run out of time.
しかしAIを使ったコード点検では、こうした問題がずっと速く見つかり、気づけば40件ほどの不具合の一覧を前にしている。1件あたり平均3行で直せるとしても、1件ごとに決まった手間がかかり、時間が尽きてしまう。
:::

以前なら、こうした不具合は公開後に少しずつ見つかり、5年ほどかけて順に直していたといいます。外された機能の多くはAIの点検が今ほど役に立たなかった時期に書かれたもので、同氏は「書いたあとで合格の基準が上がった」状態だと表現しています。

## 公開日も延びた

PostgreSQLの公開を取りまとめるチームは10月10日、開発者向けの連絡網で正式公開を11月19日に動かすと伝えました。公式の予定表では「2026年10月」の公開とされていました。理由は、過去の版にも当てた修正が多く、それを含めた2回目の公開前の最終確認版を11月12日に出してから正式版に進みたいためです。

:::quote https://www.postgresql.org/message-id/f161fbb7-e193-42eb-bec7-4cfc1af74a50%40postgresql.org | PostgreSQL公開チーム「Updated PostgreSQL RC / GA dates」
> We know this has been an atypical major release cycle, but we want to ensure we keep delivering a PostgreSQL that's stable and reliable, and we've made these decisions around that goal.
今回の開発が異例だったことは承知しているが、安定して信頼できるPostgreSQLを届け続けることを目標に、これらの判断をした。
:::

公開前の最終確認版（RC1）は予定どおり10月15日に出ています。公式の発表は、問題が見つからなければ11月19日に正式公開するとしています。

{{card:https://www.postgresql.org/about/news/postgresql-19-rc-1-released-3409/|PostgreSQL 19 RC 1 Released!|PostgreSQL}}

## AIのせいだけではない

アイゼントラウト氏は、AIに書かせた雑なプログラム（いわゆる「バイブコーディング」）が原因ではないとも書いています。問題の機能は、そうした書き方ができるようになる前に作られたものだからです。

ほかの事情も挙げています。4月から8月にかけて、ベテランの開発者の多くがセキュリティの弱点の修正に追われ、新機能を試用期間中に念入りに確かめる余裕がなかったこと。PostgreSQLは「何でも何とでも組み合わせて動く」作りのため、条件の組み合わせが膨大で、人の手ではすべてを試せないこと。後者について同氏は、AIで大量の入力を自動で試す手法がこうした問題を素早く見つけられるとして、今後は機能の開発そのものに組み込むべきだとしています。

一方で、PostgreSQL 19は外された機能を除いても「素晴らしい新版になる」とし、外した機能の多くは遠からず戻ってくると見ています。ここまで厳しく調べられた分、とても頑丈な版になるとも書いています。

## 反応と論点

この件を伝えた英The Registerの記事は、「AIの点検役が人間の直せる量を超えるバグを見つけた」という見出しで報じ、米Hacker Newsでは200近いポイントを集めました。

コメント欄では評価が割れています。自分のプログラムでAIの点検が本物の不具合を見つけてくれるという声がある一方、見つかった指摘が本当に不具合かを人が確かめる「仕分け」こそが足りない、という指摘もあります。AIの直し方が必要以上に広い範囲を書き換え、新しい不具合を生むという経験談や、そもそも製品として「どう動くべきか」という判断はAIには決められない、という意見も出ています。

なお、公開チームの連絡は延期の理由を修正の量としており、AIには直接触れていません。AIの点検との関係は、アイゼントラウト氏の個人ブログでの見立てです。

## 日本のビジネスへの影響

**使えるか**: PostgreSQLは日本でも多くの企業の業務システムやクラウドのデータベースサービスで使われており、新版19は11月19日の正式公開予定です。今回外れた機能を待っていた場合は、翌年の新版20以降になります。

**誰にどう効くか**: 社内システムの担当者や、システム開発を外部に発注している経営者・事業責任者に関係します。AIでプログラムを点検すると、これまで見過ごしていた不具合がまとめて見つかります。その結果、直す人手が追いつかず、公開の時期や機能の範囲を見直す判断が必要になる、という例がはっきり示されました。

**今すぐやれること**: 開発会社や社内の開発チームにAIの点検を導入するなら、「見つかった指摘を誰が仕分けて、どこまで直すか」の基準と、修正に使う時間を、点検を始める前に計画に入れておくのが現実的です。AIを使った開発の道具選びは[コーディングAIのガイド](/best/coding/)にまとめています。

**注意点**: AIの点検は指摘を増やしますが、直すのは人です。指摘の件数の多さをそのまま品質の悪さと受け取ったり、公開直前に初めて導入したりすると、今回のように予定が崩れます。AIで作業の進め方が変わった別の例として、[ゲームの中身の復元をAIがこなせるようになり、有志のサイトが受け付けをやめた件](/news/20261016-decomp-dev-sunsetting-ai-game-decompilation/)もあります。
