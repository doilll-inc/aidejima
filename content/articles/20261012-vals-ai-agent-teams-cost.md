---
{
  "title": "ClaudeやGPTを5体のチームで働かせても成績はほぼ同じ、費用は最大5倍に 米Vals AIが検証",
  "description": "AIの性能を測る米Vals AIが、Claude Opus 5.5とGPT-6 Solを1体で働かせた場合と、まとめ役が最大5体に仕事を配るチームにした場合を比べた。チームの費用は1.8〜5.1倍に増えたが、成績の差がはっきり出たのは4つの条件のうち1つだけだった。",
  "date": "2026-10-12T02:40:00+09:00",
  "category": "research",
  "tags": ["Vals AI", "Claude Opus 5.5", "GPT-6 Sol", "エージェント", "Claude Code", "料金"],
  "summary": [
    "米Vals AIが、AIを1体で働かせる場合と、まとめ役のAIが最大5体に仕事を配るチームにする場合を、50本のアプリ作りで比べた",
    "チームにすると費用は1.8〜5.1倍に増えたが、成績の差がはっきり出たのはGPT-6 Solを中くらいの考える量で使った1条件だけだった",
    "Claude Opus 5.5は、1体で中くらいの設定が1本4.08ドルで91.5%と、122ドルかけた最上位の設定とほぼ同じ成績だった"
  ],
  "sources": [
    {"title": "Do Agent Teams Pay Off? A Case Study on Vibe Code Bench", "publisher": "Vals AI", "url": "https://www.vals.ai/blogs/multi-agent-vibe-code-bench", "kind": "論文"},
    {"title": "AI agent teams waste massive tokens for barely measurable quality gains, research finds", "publisher": "The Decoder", "url": "https://the-decoder.com/ai-agent-teams-waste-massive-tokens-for-barely-measurable-quality-gains-research-finds/", "kind": "報道"}
  ],
  "thumb_prompt": "Five identical small robots crowded around one tiny laptop, all trying to type at once, while a single robot at the next desk calmly finishes the same work alone; a tall stack of coins sits behind the crowded desk and a short stack behind the lone robot.",
  "thumb_style": "3d",
  "thumb_text": "AIのチーム作業",
  "share_text": "ClaudeやGPTを5体のチームにしても成績はほぼ同じで費用は最大5倍。米Vals AIが50本のアプリ作りで比べた",
  "editor_note": ""
}
---
AIの性能を測る米国の評価会社Vals AIは現地時間10月9日、AIを1体で働かせる場合と、まとめ役のAIが最大5体の部下に仕事を配る「チーム」にした場合を比べた結果を公表しました。チームにすると費用は1.8〜5.1倍に増えた一方、成績の差がはっきり出たのは4つの条件のうち1つだけでした。

## 何を比べたか

対象はAnthropicの「Claude Opus 5.5」とOpenAIの「GPT-6 Sol」です。課題は、Vals AIが作った試験「Vibe Code Bench」から選んだ50本のウェブアプリ作りです。仕様書を渡して、データベースから画面までをAIに一通り作らせ、できたアプリを別のAIがブラウザで実際に操作して、動く機能の割合を点数にします。

チームの組み方は単純です。まとめ役のAIが仕事を分け、同時に最大5体の部下（サブエージェント）に配り、戻ってきた成果をつなげて確かめます。部下がさらに部下を作ることはできません。両社とも、まとめ役が部下を呼び出す機能を標準で用意しており、Vals AIは「それで何が得られ、いくらかかるのか」を確かめるのが狙いだと説明しています。

AIが考える量の設定（推論の強さ）を「中」と「最大」の2通りにし、モデル2つ×1体かチームか×設定2通りの計8パターンを1回ずつ走らせました。Claudeは開発者向けの「Claude Code」から、GPTはOpenAIの開発者向けの仕組みから動かしており、Vals AIはモデルどうしの比較には動かし方の違いも混ざると断っています。

## 結果：費用は増え、成績は変わらないことが多い

アプリ1本あたりの平均費用と成績は次のとおりです（Vals AIの公表値から編集部で作成）。

| モデルと設定 | 1体の成績 | チームの成績 | 1体の費用 | チームの費用 |
|---|---|---|---|---|
| GPT-6 Sol・中 | 77.6% | 84.9% | 1.22ドル | 3.07ドル |
| GPT-6 Sol・最大 | 89.0% | 90.4% | 4.82ドル | 8.54ドル |
| Claude Opus 5.5・中 | 91.5% | 91.2% | 4.08ドル | 9.10ドル |
| Claude Opus 5.5・最大 | 89.8% | 93.2% | 23.77ドル | 122ドル |

チームが統計的にはっきり上回ったのは、GPT-6 Solを「中」で使った場合の7.3ポイントだけです。残る3つの差は、偶然の範囲を出ませんでした。

:::quote https://www.vals.ai/blogs/multi-agent-vibe-code-bench | Vals AI「Do Agent Teams Pay Off? A Case Study on Vibe Code Bench」
> Teams cost 1.8 to 5.1 times as much as single agents, and only one difference in score was statistically significant.
チームの費用は1体の場合の1.8〜5.1倍で、成績の差が統計的に意味のある大きさだったのは1つだけだった。
:::

目を引くのはClaudeの数字です。1体・設定「中」の91.5%（1本4.08ドル）に対し、チーム・設定「最大」は93.2%で最高点でしたが、費用は122ドルと約30倍です。その1.6ポイントの差も、統計的には意味のある差ではないとされました。GPTでは、チームにするより、1体のまま考える量を「最大」に上げたほうが点数の伸びは大きくなりました。

## なぜ高くつくのか

Vals AIによると、増えた費用の大半は、部下のAIがそれぞれ仕様書や作業の途中経過を抱え、AIを呼び出すたびに読み直す分です。最大設定のClaudeでは、部下が読み直した量の中央値がアプリ1本あたり2億2,400万トークン（トークンはAIが文章を数える単位）で、1体で作業した場合の5,500万トークンの4倍を超えました。

速さも、必ずしも増しません。GPTのチームは最初の数分で仕事を割り振って並行に進め、最大設定では作業時間が38分から28分に縮みました。一方、Claudeのまとめ役は、先に部品どうしのつなぎ方の取り決めを書いてから順番に仕事を配る進め方で、最大設定では1体の2.3倍の時間がかかっています。

## 論点：「数を増やせば賢くなる」わけではない

AI各社は、まとめ役のAIが多数のAIに仕事を配る機能を相次いで出しています。Anthropicは10月9日、企業向けの基盤で延べ最大1,000体のAIに作業を配る機能を試験提供しました（[既報](/news/20261010-claude-managed-agents-dynamic-workflows/)）。今回の結果は、少なくともアプリ作りでは、体数を増やすことが品質の向上に直結しないことを数字で示しています。

ただし、Vals AI自身が結果の範囲を限っています。各パターンは1回ずつの実行で、課題も1種類だけです。

:::quote https://www.vals.ai/blogs/multi-agent-vibe-code-bench | Vals AI「Do Agent Teams Pay Off? A Case Study on Vibe Code Bench」
> These observations come from one benchmark of full-stack web apps and may not carry over to other kinds of work.
これらの観察は、ウェブアプリを丸ごと作る1つの試験から得たもので、別の種類の仕事には当てはまらない可能性がある。
:::

調べ物のように、互いに関係の薄い作業へきれいに分けられる仕事なら、チームの方が速く終わる余地はあります。逆に、部品どうしのつなぎ目で不具合が出やすい仕事では、まとめ役の調整の手間が費用として表に出やすいと読めます。

## 日本のビジネスへの影響

- **使えるか**: Claude CodeやOpenAIの開発向けの仕組みなど、日本から使える開発ツールにはすでに部下のAIに仕事を配る機能があり、使った分だけ費用が増えます。今回の試験は特定の製品の評価ではなく、設定の選び方の参考になるデータです
- **誰にどう効くか**: AIエージェントで業務の自動化を進める情報システム部門や開発会社の責任者です。社内で「AIを何体も並べれば早く良くなる」という期待があるなら、費用対効果を説明する材料になります
- **今すぐやれること**: いま使っている自動化の仕事を1つ選び、1体・推論の強さ「中」を基準に、チームにした場合と強さを上げた場合の費用と出来を並べて比べてください。差が小さければ、最も安い設定に戻すだけで毎月の請求が数分の1になる可能性があります
- **注意点**: 試験はアプリ作りだけで、調べ物や文書の点検などでは結果が変わりえます。チームの機能を使うときは、Anthropicも勧めているように利用額の上限を先に決めておくと、想定外の請求を防げます。開発向けAIの料金の比較は[コーディングAIのガイド](/best/coding/)にまとめています
