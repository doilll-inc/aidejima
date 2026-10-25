---
{
  "title": "AIエージェントは部署ごとに分けず1体に、Claudeの開発元が企業に勧める 速さは約2倍",
  "description": "Anthropicは、企業がClaudeで作るAIエージェントを、部署やチームごとの専門AIに分けず、1体のAIに必要な知識と道具をその都度読み込ませる形にまとめるよう勧める指針を公開した。比べた企業では処理が約2倍速くなったという。",
  "date": "2026-10-26T02:20:00+09:00",
  "category": "business",
  "tags": ["Anthropic", "Claude", "エージェント", "経営", "Claude Opus 5.5", "Claude Code"],
  "summary": [
    "Anthropicは、企業向けのAIエージェントを部署ごとの専門AIに分けず、1体にまとめて必要な知識を都度読ませる設計を勧めた",
    "部署ごとに分けると、AI同士の受け渡しで情報が抜け、各部署の指示が矛盾して口調もそろわないと指摘。1体にした企業は約2倍速くなった",
    "移行用の道具も無料公開した。ただし、同時に別々の作業を進めるときなどは、今も分けたほうがよいとしている"
  ],
  "sources": [
    {"title": "Building agents: When to fold subagents into your main agent loop", "publisher": "Claude by Anthropic", "url": "https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop", "kind": "公式発表"},
    {"title": "anthropics/single-agent-loop-kit", "publisher": "GitHub（Anthropic）", "url": "https://github.com/anthropics/single-agent-loop-kit", "kind": "公式ドキュメント"},
    {"title": "Anthropic says one AI agent beats many subagents now that models can handle complexity alone", "publisher": "The Decoder", "url": "https://the-decoder.com/anthropic-says-one-ai-agent-beats-many-subagents-now-that-models-can-handle-complexity-alone/", "kind": "報道"}
  ],
  "thumb_prompt": "A tiny office building cut open like a dollhouse, where a dozen small robots at separate department desks pass a single paper note hand to hand, while one larger robot in the lobby already holds the finished answer.",
  "thumb_style": "3d",
  "thumb_text": "AIは1体に",
  "share_text": "AIエージェントを部署ごとに分けると遅く、指示も矛盾する。Claudeの開発元Anthropicが「1体にまとめる」設計を企業に勧める",
  "editor_note": ""
}
---
Claudeを開発する米Anthropicは現地時間10月22日、企業が作るAIエージェント（指示を受けて自分で調べ、道具を使って作業を進めるAI）について、部署や業務ごとに専門のAIを分けて作るのをやめ、1体のAIにまとめる設計を勧める指針を公開しました。同社が比べた企業の例では、1体にした方が処理が約2倍速くなりました。移行を手伝う道具も無料で公開しています。

## 何が発表されたか

指針は、Anthropicの企業導入を支援するチーム（Applied AI）が、複数の企業での導入経験をまとめたものです。対象は、顧客対応や社内業務などのために、複数のAIを組み合わせて1つのエージェントを作っている企業です。

よくある作り方は、部署やチームがそれぞれ専門のAI（サブエージェント）を作り、その上に「どの専門AIに回すか」を決めるまとめ役のAIを置く形です。Anthropicはこれを、組織図をそのままAIに写したものだと指摘しています。

:::quote https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop | Claude by Anthropic「Building agents: When to fold subagents into your main agent loop」
> But too often we see enterprises give each team or problem type its own subagent, with the agent architecture becoming a copy of their org chart (Conway’s law at work).
しかし、企業がチームや問題の種類ごとに専用のサブエージェントを用意し、エージェントの構成が組織図の写しになっている例をあまりに多く見ます（コンウェイの法則が働いています）。
:::

コンウェイの法則とは、「組織が作るシステムは、その組織の構造に似る」という、ソフトウェア開発で知られる経験則です。

指針が挙げる、部署ごとに分けたときの問題は主に4つです。

- **受け渡しで情報が抜ける**: 専門AIからまとめ役へ結果を要約して返すたびに、細かい情報が落ちます。指針は、伝言ゲームのように少しずつ中身が変わると表現しています
- **指示が矛盾する**: 各チームがAIへの基本の指示文に1文ずつ書き足していき、ルール同士がぶつかり、口調もそろわなくなります。ある企業では、顧客向けのエージェントに十数体の専門AIを入れた結果、ブランドらしい一貫した応対を保つのが難しくなりました
- **増えすぎて持ち主がいない**: 各チームが専門AIを出し続け、重複した数百のAIが、決まった基準も責任者もないまま並ぶことがあります
- **遅くなる**: AI同士のやり取りが増える分、返事が遅れます

代わりに勧めるのは、1体のAIが会話の流れをすべて持ち、各部署の手順やルールは「スキル」（必要なときだけ読み込む手順書）、社内システムへの操作は「ツール」として渡す形です。AIは普段はスキルやツールの短い説明だけを見ていて、必要になったときに中身を読み込みます。

:::quote https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop | Claude by Anthropic「Building agents: When to fold subagents into your main agent loop」
> One customer that evaluated their multi-agent harness against a single agent loop saw a roughly 2x faster runtime with the latter.
複数のエージェントを組み合わせた仕組みと、1体のエージェントで回す仕組みを比べたある顧客では、後者の方が処理時間がおよそ2倍速くなりました。
:::

あわせてAnthropicは、移行の手順をまとめた道具一式「single-agent-loop-kit」をGitHubで無料公開しました。今ある専門AIを1つずつ点検し、「まとめる」「1つに統合する」「道具として呼ぶ形で残す」「そのまま残す」のどれにするかを判定し、移行前後の出来を比べる手順が入っています。

{{card:https://github.com/anthropics/single-agent-loop-kit|anthropics/single-agent-loop-kit|GitHub（Anthropic）}}

## なぜ今「まとめる」のか

理由としてAnthropicが挙げるのは、AIそのものの性能向上です。指針によると、Claude Opus 4.5のころから、1体のAIで扱える仕事の量がほとんどのチームの想定を超えるようになりました。最近のClaudeは、作業の途中で進み具合を自分で説明し、結果を確かめながら進めるため、これまで人が外側に作り込んでいた仕組みの一部が要らなくなったといいます。同社は、開発ツールClaude Codeでも、新しいモデル向けの基本の指示文を8割以上短くしたと説明しています。

ただし、Anthropic自身も複数のAIを組み合わせる方式を捨てたわけではありません。同社は10月、企業向けの基盤で、まとめ役のAIが最大1,000体のAIに仕事を配る機能を試験提供しています（「[大量の仕事を最大1,000体のAIで手分け、Claudeの企業向け「Managed Agents」に新機能](/news/20261010-claude-managed-agents-dynamic-workflows/)」）。指針でも、次の3つの場合は今も分けた方がよいとしています。

- 1体に情報を詰め込みすぎて、出来が目に見えて落ちたとき
- 互いに関係の薄い作業を、同時並行で進めたいとき
- 1体では使う道具を選び間違える、または指示同士が矛盾してしまうとき

## 反応と論点

「AIを増やせば良くなる」という考えへの疑問は、ほかの検証でも出ています。AIの性能を測る米Vals AIは10月、Claude Opus 5.5などを1体で働かせた場合と、最大5体のチームにした場合を比べ、チームにすると費用は最大5.1倍に増えたのに、成績の差がはっきり出たのは一部の条件だけだったと公表しました（「[ClaudeやGPTを5体のチームで働かせても成績はほぼ同じ、費用は最大5倍に](/news/20261012-vals-ai-agent-teams-cost/)」）。独メディアThe Decoderは、OpenAIの開発者からも、AIを大量に並べる方式は多くの場合お金の無駄だという声が出ていると伝えています。

一方で、まとめることの落とし穴も指針自身が示しています。Anthropicが試しに顧客サポートのエージェントで2体を1体にまとめたところ、返事は速くなりましたが、それまでできていた処理が1つ壊れました。注文の問い合わせに答える際、配送担当のAIに届け日を確かめずに答えてしまったのです。この失敗は2回試したうち1回しか出なかったため、指針は同じテストを複数回繰り返すよう勧めています。

運用の面では、AIの基本の指示文と全体の品質は小さな中央チームが持ち、各部署は自分たちの手順書（スキル）や社内システムとの接続（ツール）を作って提供する、という役割分担を提案しています。渡す道具は30〜50個を超えると選び間違いが増えるため、1つのシステムに1つずつではなく、利用者がしたいことの単位でまとめるよう求めています。

## 日本のビジネスへの影響

- **使えるか**: 指針と移行用の道具は誰でも読めて、道具は無料です（英語）。ClaudeのAPIを使っている企業はそのまま試せます。考え方自体は、ほかの会社のAIで作るエージェントにも当てはまります
- **誰に効くか**: 社内でAIエージェントの導入を進める経営者・DX担当者と、顧客対応のAIを作るカスタマーサポートの責任者です。「各部署に自分のAIを作らせ、あとでつなぐ」という進め方は日本企業でも選ばれやすいため、計画段階で見直す価値があります。API料金の比較は[API料金のガイド](/best/api/)にまとめています
- **今すぐやれること**: 社内で動いている、または計画中のAIの数と、それぞれの持ち主を一覧にしてください。次に、よく使われる問い合わせを10件ほど選んで「正しく答えられたか」を確かめるテストを作ります。Anthropicも、まずは10件程度の手本から始めればよいとしています
- **注意点**: 1体にまとめると、基本の指示文やルールを誰が管理するかがはっきりしていないと、かえって混乱します。また、まとめた直後は一見うまく動いても、まれにしか出ない誤りが残ることがあります。切り替えは1体ずつ、同じテストを何度か回して確かめながら進めるのが安全です
