---
{
  "title": "大量の仕事を最大1,000体のAIで手分け、Claudeの企業向け「Managed Agents」に新機能",
  "description": "Anthropicは10月9日、企業がClaudeでAIの代行役を作る基盤「Claude Managed Agents」に、まとめ役のAIが計画を立てて最大1,000体のAIに作業を配る「動的ワークフロー」を試験提供した。同時に動くのは最大64体で、費用は使った分だけ増える。",
  "date": "2026-10-10T19:10:00+09:00",
  "category": "dev",
  "tags": ["Anthropic", "Claude Managed Agents", "Claude", "エージェント", "API"],
  "summary": [
    "Anthropicが企業向けの基盤「Claude Managed Agents」に、まとめ役のAIが作業を多数のAIに配る機能を試験提供した",
    "1回の作業で使えるAIは延べ最大1,000体、同時に動くのは最大64体で、何百もの文書の点検のような大仕事を想定している",
    "機能そのものに追加料金はないが、動いたAIの数だけ利用料がかかるため、Anthropicは使う上限額の設定を勧めている"
  ],
  "sources": [
    {"title": "Claude Platform release notes（October 9, 2026）", "publisher": "Anthropic（Claude Platform Docs）", "url": "https://platform.claude.com/docs/en/release-notes/overview", "kind": "公式ドキュメント"},
    {"title": "Workflow runs", "publisher": "Anthropic（Claude Platform Docs）", "url": "https://platform.claude.com/docs/en/managed-agents/workflow-runs", "kind": "公式ドキュメント"},
    {"title": "Multiagent orchestration", "publisher": "Anthropic（Claude Platform Docs）", "url": "https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration", "kind": "公式ドキュメント"},
    {"title": "ClaudeDevs の投稿", "publisher": "X @ClaudeDevs", "url": "https://x.com/ClaudeDevs/status/2108591328732856655", "kind": "X投稿"},
    {"title": "Introducing dynamic workflows in Claude Code", "publisher": "Anthropic（Claude公式ブログ）", "url": "https://claude.com/blog/introducing-dynamic-workflows-in-claude-code", "kind": "公式発表"},
    {"title": "Anthropic's Claude can now orchestrate up to 1,000 AI agents in parallel through dynamic workflows", "publisher": "The Decoder", "url": "https://the-decoder.com/anthropics-claude-can-now-orchestrate-up-to-1000-ai-agents-in-parallel-through-dynamic-workflows/", "kind": "報道"},
    {"title": "Claude Dynamic Workflows Beta: Can It Beat One Agent?", "publisher": "Kingy AI", "url": "https://kingy.ai/blog/claude-managed-agents-dynamic-workflows-beta/", "kind": "報道"}
  ],
  "thumb_text": "Managed Agents",
  "thumb_style": "diorama",
  "thumb_prompt": "A miniature office floor seen from above where one tiny foreman figure at a central desk hands out paper slips to hundreds of identical tiny workers arranged in neat rows, a mountain of documents behind them.",
  "share_text": "Claudeのまとめ役AIが計画を立て、延べ最大1,000体のAIに作業を配る。企業向けのManaged Agentsに新機能",
  "editor_note": ""
}
---
Anthropicは現地時間10月9日、企業がClaudeを使ってAIの代行役（エージェント）を作り、自社のサービスに組み込むための基盤「Claude Managed Agents」に、「動的ワークフロー（dynamic workflows）」を試験提供（ベータ）として追加しました。まとめ役のAIが作業の計画を立て、1回の作業で延べ最大1,000体のAIに仕事を配って結果をまとめる機能です。何百もの文書の点検のように、1つのAIでは手に負えない量の仕事を想定しています。

## 何が発表されたか

Claude Managed Agentsとは、AIが作業するための計算環境や記録の仕組みをAnthropicが用意し、企業は「何をさせるか」を決めるだけでAIの代行役を動かせる開発者向けのサービスです。今回の動的ワークフローは、その上で動くまとめ役のAIが、仕事を分ける手順そのものを小さなプログラムとして書き、裏側で多数のAIを段階ごとに動かします。

:::quote https://platform.claude.com/docs/en/release-notes/overview | Claude Platform リリースノート（2026年10月9日）
> For work with many pieces, such as reviewing hundreds of documents, the agent can write a workflow. A workflow is a program that runs many agents in phases and combines their results.
何百もの文書の点検のように多くの部分からなる仕事では、エージェントがワークフローを書けます。ワークフローとは、多数のエージェントを段階ごとに動かし、その結果をまとめるプログラムです。
:::

公式ドキュメントに書かれた上限は次のとおりです。報道には1,000体が同時に動くかのように受け取れる見出しもありますが、ドキュメント上は、1,000体は1回の作業全体で起動できる延べの数で、同時に動くのは最大64体です。

| 項目 | 上限 |
|---|---|
| 1回の作業で起動できるAI（延べ） | 1,000体 |
| 同時に動くAI | 64体（変わる可能性あり） |
| 1回の作業の時間 | 既定で24時間 |
| 1つの会話で同時に開ける作業 | 既定で10件 |

ドキュメントが挙げる用途は、点検（監査）、システムの移行、深い調査、突き合わせ確認です。料金について、ドキュメントは「1回の作業そのものに価格はない」とし、動いたAIそれぞれが使った分を通常の料金で請求すると説明しています。予算の上限を決めておくと、そこで作業が一時停止します。

{{card:https://platform.claude.com/docs/en/managed-agents/workflow-runs|Workflow runs（上限と予算の説明）|Claude Platform Docs}}

## 背景

同じ名前の機能は、5月28日にプログラミング支援ツールのClaude Codeに先に入っています。こちらは「1回の作業で数十〜数百のAIを並行して動かす」もので、AnthropicはBunという開発ツールをZigからRustという別のプログラミング言語に書き直す作業に使い、約75万行を11日で移した例を紹介していました。今回はこの仕組みを、企業が自社の製品や業務システムに組み込めるManaged Agents側でも使えるようにした形です。

Managed Agentsでは以前から、まとめ役のAIが部下役のAIに仕事を頼む「サブエージェント」の仕組みがありました。こちらは同時に25体までで、まとめ役が一つずつ報告を読んで次を指示します。動的ワークフローは、まとめ役がその都度指示を出すのではなく、最初に段取りを書いて自動で回す点が違います。

## 反応と論点

開発者向けの公式アカウント「ClaudeDevs」は、最も野心的な仕事のための新しい形の連携だと紹介しています。

{{x:https://x.com/ClaudeDevs/status/2108591328732856655}}

ドイツのAI専門メディアThe Decoderは、AIを1体で動かすより多くの不具合を見つけたとするAnthropic側の試験結果を伝えつつ、AIを大量に並べる手法は費用に見合わないという開発者の異論もあると報じています。試験とは別の種類の仕事でも同じ効果が出るとは限らないので、自分の仕事で試して確かめるべきだという指摘です。

AI関連の情報サイトKingy AIも、2体目のAIが1体目と同じ間違いをすることがあり、作業が「完了」と表示されても全員が成功したとは限らないと注意を促しています。Anthropic自身も、多くのAIを使う分だけ利用量が増えるとして、範囲を絞った作業から始めるよう勧めています。

## 日本のビジネスへの影響

- **使えるか**：Claude Managed Agentsは日本からも契約できる開発者向けのサービスで、今回の機能は試験提供の段階です。ChatGPTのような画面で使うものではなく、自社のシステムにプログラムで組み込む前提です。普段使いのClaudeアプリの機能ではありません
- **誰にどう効くか**：契約書や規程、商品ページ、問い合わせ記録などを何百件単位で点検したい企業の、業務改革や情報システムの担当者に関係します。1件ずつAIに頼むと何日もかかる作業を、まとめ役のAIに分担させて短くできる可能性があります
- **今すぐやれること**：答えがわかっている小さめの点検作業（例えば過去に人が確認済みの文書50件）を選び、AI1体の場合と動的ワークフローの場合で、見落としの数と費用を比べてみることです。AIを業務システムに組み込む際の各社の料金は[API比較ガイド](/best/api/)にまとめています
- **注意点**：動いたAIの数だけ料金が増えるので、予算の上限は必ず設定してください。上限に達しても、動いている各AIが処理中の1回分は追加でかかります。試験提供中のため、仕様や上限の数字は変わる可能性があります

Claudeの使い方全般の料金は、[Claude Codeの料金と選び方の記事](/news/20261008-claude-code-pricing-plans/)も参考になります。
