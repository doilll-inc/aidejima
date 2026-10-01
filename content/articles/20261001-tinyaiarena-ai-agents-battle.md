---
{
  "title": "TinyAIArenaはAI同士が戦う観戦サイト、成績表ではClaude Sonnet 5が首位",
  "description": "開発者のhp6が、4つのAIモデルが8×8マスの盤上で最後の1体になるまで戦うTinyAIArenaを公開した。43試合の成績ではClaude Sonnet 5がElo 1063で首位、DeepSeek V4 Flashは勝ちがない。",
  "date": "2026-10-01T18:29:00+09:00",
  "category": "usecases",
  "tags": ["TinyAIArena", "OpenRouter", "活用事例", "個人開発", "エージェント", "ゲーム"],
  "summary": [
    "TinyAIArenaは、7種のAIモデルから選ばれた4体が8×8マスの盤上で最後の1体になるまで戦う観戦サイト",
    "TinyAIArenaの43試合ではClaude Sonnet 5が首位、DeepSeek V4 Flashは勝ちなし",
    "作者は試合数が少なく運の要素も切り分けていないため、本格的なベンチマークとしては不十分だと認めている"
  ],
  "sources": [
    {"title": "Tiny AI Arena（README）", "publisher": "GitHub hp6", "url": "https://github.com/hp6/ai-arena", "kind": "公式ドキュメント"},
    {"title": "CLAUDE.md（設計の説明）", "publisher": "GitHub hp6", "url": "https://github.com/hp6/ai-arena/blob/master/CLAUDE.md", "kind": "公式ドキュメント"},
    {"title": "AgentConfig.ts（出場モデルの一覧）", "publisher": "GitHub hp6", "url": "https://github.com/hp6/ai-arena/blob/master/server/src/ai/AgentConfig.ts", "kind": "公式ドキュメント"},
    {"title": "Tiny AI Arena（成績表と試合の再生）", "publisher": "tinyaiarena.com", "url": "https://tinyaiarena.com/", "kind": "公式発表"},
    {"title": "Show HN: TinyAIArena watch AI agents battle it out（作者の投稿）", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=49867775", "kind": "公式発表"}
  ],
  "thumb_text": "TinyAIArena",
  "share_text": "AIモデル4体が8×8マスで戦う様子を観戦できるTinyAIArena。43試合の成績ではClaude Sonnet 5が首位",
  "editor_note": ""
}
---
GitHubでhp6を名乗る開発者は現地時間9月27日、AIモデル同士を戦わせて観戦できるサイト「TinyAIArena」をHacker NewsのShow HNで公開しました。10月1日時点のサイトの成績表では、43試合を終えてAnthropicのClaude Sonnet 5がレーティング（Elo）1063で首位に立っています。

## 何を作ったか

TinyAIArenaとは、4つのAIモデルが8×8マスの盤上で最後の1体になるまで戦う様子を、1コマずつ再生して見られるサイトです。作者は、「アリーナ」と名の付くAI評価サイトが点数表ばかりなのを物足りなく思い、本当に戦う姿を見せたかったと説明しています。

:::quote https://github.com/hp6/ai-arena | Tiny AI Arena GitHub README
> Did you ever click on an "AI Arena" expecting glorious battle and instead get a boring benchmark? If so, this project is for you: proper life-or-death fights between four models on a picturesque 8×8 grid.
「AIアリーナ」を開いて壮絶な戦いを期待したのに、退屈なベンチマークが出てきたことはありませんか。そんな人のためのプロジェクトです。絵のような8×8の盤で、4つのモデルが命がけで戦います。
:::

毎ラウンド、順番を入れ替えて各自が1ターンずつ動きます。行動は1マスの移動、隣の敵への攻撃（15〜24のダメージ）、待機のいずれかで、1回ごとに行動ポイント（AP）を1使います。盤上の金貨を取るか敵を倒すと毎ターンのAPが1増え、倒せば体力も50回復します。各モデルは1ターンに50字までチャットを送れ、直近6件が全員への指示文に入ります。

## どう作ったか

サーバーはExpressとSQLite、観戦画面はゲーム用ライブラリのPhaser 4で作られています。AIは、複数社のモデルを1つの窓口で呼べるOpenRouter経由で呼び出し、7モデルから毎試合4つを抽選します。各モデルには盤面と取れる行動の一覧を渡し、決められたJSON形式で1ターン分の行動をまとめて答えさせます。

不正な行動はサーバーが判定して無効にし、APだけを消費させます。返答が壊れていれば1回だけやり直し、それでもだめなら待機扱いです。公開サイトは手元で走らせた試合の記録を書き出した静的なページで、APIキーを公開せずに済む作りです。リポジトリには開発AIのClaude Code向けの説明ファイル（CLAUDE.md）も置かれています。

:::quote https://github.com/hp6/ai-arena/blob/master/CLAUDE.md | Tiny AI Arena GitHub「CLAUDE.md」
> Placement is deliberately not used for rating, because a fighter that does nothing gets carried up the finishing order while the others eliminate each other.
最終順位はあえてレーティングに使っていません。何もしない戦士でも、ほかの戦士がつぶし合う間に順位だけは上がってしまうからです。
:::

Eloは勝った1体にだけ与え、勝者が残り3体それぞれに勝ったとみなして計算します。

{{card:https://tinyaiarena.com/|Tiny AI Arena（試合の再生と成績表）|hp6}}

## 成果（サイトの成績表）

10月1日時点の成績表（43試合）は次の通りです。

| モデル | Elo | 勝ち／試合 |
|---|---|---|
| Claude Sonnet 5 | 1063 | 9／21 |
| Claude Fable 5.1 | 1037 | 8／25 |
| Grok 4.6 | 1030 | 10／29 |
| Gemini 3.6 Flash | 1029 | 7／22 |
| GPT-5.6 Luna Pro | 1008 | 7／28 |
| Kimi K2.6 | 949 | 2／21 |
| DeepSeek V4 Flash | 890 | 0／25 |

首位がClaude Sonnet 5だったことに「知能を測るには怪しい」と指摘されると、作者はベンチマークとしては不十分だと認めました。試合数を大幅に増やし、運と実力を切り分け、ゲームを複雑にする必要があるものの、それでは楽しさが失われると答えています。

## 反応

HNでは「Fableはほかの戦士が削り合うのを待ち、1体ずつ仕留めた」など、戦い方の違いを面白がる声が出ました。一方、チャットが決まり文句ばかりで味気ないとの指摘もあり、50字の上限や、JSONの中で台詞を書かせる形式が原因ではないかと議論になりました。

## 日本のビジネスへの影響

観戦はブラウザだけででき、登録も要りません。画面は英語です。自分で試合を走らせるにはNode.jsの環境とOpenRouterのAPIキーが要り、費用は呼んだモデルの従量料金です。作者は1試合あたりの費用を公表していません。リポジトリにはライセンスの記載がなく、コードを流用してよい条件は示されていません。

関係が深いのは、AIエージェントを業務に組み込む開発者です。複数のモデルに同じルールで判断させ、不正な出力はサーバー側で弾き、全ての呼び出しを記録する構成は、エージェントを比べる検証環境の小さな手本になります。マーケターにとっては、モデル同士の対戦を見せる演出がイベントやSNSの素材になり得ます。

今すぐやれることは、気になるモデルの試合をいくつか再生し、ゲームログとチャットから判断の癖をつかむことです。注意点は、試合数が少ないため、ここでの勝敗をモデル選びの根拠にしないことです。APIの料金は[AI APIの料金比較](/best/api/)で確認できます。
