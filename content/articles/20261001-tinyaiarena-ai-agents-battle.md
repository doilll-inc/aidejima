---
{
  "title": "TinyAIArenaはAI同士が戦う観戦サイト、成績表ではClaude Sonnet 5が首位",
  "description": "開発者のhp6が、4つのAIモデルが8×8マスの盤上で最後の1体になるまで戦うTinyAIArenaを公開した。43試合の成績ではClaude Sonnet 5がElo 1063で首位、DeepSeek V4 Flashは勝ちがない。",
  "date": "2026-10-01T18:29:00+09:00",
  "updated": "2026-10-01T18:49:00+09:00",
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
  "thumb_style": "diorama",
  "thumb_prompt": "A tiny chessboard-like arena of eight by eight squares with four small toy robots of different colors facing off in the middle, one robot raising its arm in victory.",
  "editor_note": ""
}
---
GitHubでhp6を名乗る開発者は現地時間9月27日、AIモデル同士を戦わせて観戦できるサイト「TinyAIArena」をHacker NewsのShow HNで公開しました。10月1日時点のサイトの成績表では、43試合を終えてAnthropicのClaude Sonnet 5がレーティング（Elo）1063で首位に立っています。

## 何を作ったか

TinyAIArenaとは、4つのAIモデルが8×8マスの盤上で最後の1体になるまで戦う様子を、1コマずつ再生して見られるサイトです。「アリーナ」と名の付くAI評価サイトを開いても点数表しか出てこない、という不満が出発点だと作者は書いています。人間は操作せず、観戦するだけです。

勝ち条件は、最後の1体として生き残ることです。強くなる手段は、盤上に1枚だけ置かれる金貨を取るか、敵を倒すかの2つで、どちらも毎ターン使える行動ポイント（AP）が以後ずっと1増えます。倒した側は体力も50回復します。

行動は隣のマスへの移動か、隣の敵への攻撃（15〜24のダメージ）か、待機で、いずれもAPを1使います。盤には通れない岩が4つ置かれ、手番の順は毎ラウンド入れ替わります。

各モデルは1ターンに50字までチャットを送れます。直近の6件は全員の指示文に入るので、挑発や駆け引きが盤面と一緒に流れます。

## どう作ったか

各モデルは、盤面と取れる行動の一覧、敵との距離、最近のチャットを受け取り、1ターン分の行動を1回の呼び出しでまとめて答えます。答えは決められたJSON形式に縛られ、1回の待ち時間は90秒です。

行動の判定はすべてサーバー側が受け持ち、反則の行動は何も起こさずにAPだけを消費させます。返答が空や壊れた形なら1回だけやり直し、それでもだめなら待機扱いになり、人間やプログラムが代わりに指すことはありません。

AIの呼び出しには、複数社のモデルを1つの窓口で使えるOpenRouterを使い、7モデルから毎試合4つを抽選します。サーバーはExpressとSQLite、観戦画面はゲーム用ライブラリのPhaser 4です。

全ての行動を1コマとして保存するため、再生は正確で、サーバーを再起動しても試合が残ります。公開サイトは手元で走らせた試合の記録を書き出した静的なページで、APIキーを外に出さずに済みます。リポジトリには開発AIのClaude Code向けの説明ファイル（CLAUDE.md）も置かれています。

成績の付け方には工夫があります。Eloは勝った1体にだけ与え、勝者が残り3体それぞれに勝ったとみなして計算し、2位も最下位も同じ扱いです。

:::quote https://github.com/hp6/ai-arena/blob/master/CLAUDE.md | Tiny AI Arena GitHub「CLAUDE.md」
> Placement is deliberately not used for rating, because a fighter that does nothing gets carried up the finishing order while the others eliminate each other.
最終順位はあえてレーティングに使っていません。何もしない戦士でも、ほかの戦士がつぶし合う間に順位だけは上がってしまうからです。
:::

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

HNの利用者から、首位がClaude Sonnet 5では「知能を測るには怪しい」と指摘されると、作者はベンチマークとしては不十分だと認めました。試合数を大幅に増やし、運と実力を切り分け、ゲームを複雑にする必要があるものの、それでは楽しさが失われると答えています。

## 反応

HNの利用者からは「Fableはほかの戦士が削り合うのを待ち、1体ずつ仕留めた」など、戦い方の違いを面白がる声が出ました。一方、チャットが決まり文句ばかりで味気ないとの指摘もあり、50字の上限や、JSONの中で台詞を書かせる形式が原因ではないかと議論になりました。

## 日本のビジネスへの影響

観戦はブラウザだけででき、登録も要りません。画面は英語です。自分で試合を走らせるにはNode.jsの環境とOpenRouterのAPIキーが要り、費用は呼んだモデルの従量料金です。作者は1試合あたりの費用を公表していません。リポジトリにはライセンスの記載がなく、コードを流用してよい条件は示されていません。

関係が深いのは、AIエージェントを業務に組み込む開発者です。複数のモデルに同じルールで判断させ、不正な出力はサーバー側で弾き、全ての呼び出しを記録する構成は、エージェントを比べる検証環境の小さな手本になります。マーケターにとっては、モデル同士の対戦を見せる演出がイベントやSNSの素材になり得ます。

今すぐやれることは、気になるモデルの試合をいくつか再生し、ゲームログとチャットから判断の癖をつかむことです。注意点は、試合数が少ないため、ここでの勝敗をモデル選びの根拠にしないことです。APIの料金は[AI APIの料金比較](/best/api/)で確認できます。
