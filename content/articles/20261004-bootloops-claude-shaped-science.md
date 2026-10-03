---
{
  "title": "BootLoopsはClaudeに精密計算をさせる科学用OSS、ハーバード大教授が3カ月で論文36本",
  "description": "ハーバード大の物理学者マシュー・シュワルツ教授が、Claudeに精密な科学計算をさせるOSS「BootLoops」を公開した。Claude Codeを並行で動かし、3カ月で18分野・36本の論文原稿をまとめた。AIの弱点と付き合い方も具体的に記している。",
  "date": "2026-10-04T01:40:00+09:00",
  "category": "usecases",
  "tags": ["BootLoops", "Claude Code", "活用事例", "論文", "オープンソース", "エージェント"],
  "summary": [
    "BootLoopsは、AIエージェントに精密な科学計算の道具と検証の手順を渡すOSSで、MITライセンスで公開された",
    "ハーバード大のシュワルツ教授は、Claude Codeを並行で動かし、3カ月で18分野・36本の論文原稿を共著者19人とまとめた",
    "教授は、Claudeは計算は正確でも結論を誤ることがあり、自動チェックも信用しきれないとして、人が全部を見るよう勧めている"
  ],
  "sources": [
    {"title": "Claude-shaped science", "publisher": "Anthropic（Matthew Schwartz氏の寄稿）", "url": "https://www.anthropic.com/research/claude-shaped-science", "kind": "公式発表"},
    {"title": "BootLoops-ai/bootloops（README）", "publisher": "GitHub BootLoops-ai", "url": "https://github.com/BootLoops-ai/bootloops", "kind": "公式サイト"},
    {"title": "Anthropic の投稿（Schwartz氏の寄稿の紹介）", "publisher": "X @AnthropicAI", "url": "https://x.com/AnthropicAI/status/2105733864152858919", "kind": "X投稿"},
    {"title": "Open-source \"BootLoops\" harness supports AI models in performing precise scientific calculations", "publisher": "The Decoder", "url": "https://the-decoder.com/open-source-bootloops-harness-supports-ai-models-in-performing-precise-scientific-calculations/", "kind": "報道"}
  ],
  "thumb_text": "BootLoops",
  "share_text": "ハーバード大の物理学者がClaude Codeを並行で動かし、3カ月で18分野・36本の論文原稿。道具一式はBootLoopsとしてOSSで公開",
  "editor_note": ""
}
---
ハーバード大学の理論物理学者マシュー・シュワルツ教授が、AIエージェントに精密な科学計算をさせるためのオープンソースの道具一式「BootLoops」を公開しました。Anthropicの研究ブログに米国時間10月1日に載った寄稿によると、教授はClaude Codeを何本も並行で動かし、3カ月で18分野・36本の論文原稿をまとめました。共著者は19人で、検討した題材は約400件にのぼります。

## 何を作ったか

BootLoopsとは、Claudeなどの言語モデルに、厳密な数値計算のソフトウェアと「どうなれば完成か」を決めた検証の手順をまとめて渡すハーネス（AIを動かすための土台）です。GitHubではMITライセンスで公開され、積分の計算、証明付きの漸化式、ベイズ統計の厳密計算などの道具が入っています。手順書はマークダウンで書かれ、Claude Code以外のエージェントからも読めます。

READMEは、特定のモデルに縛られない設計だと説明しています。

:::quote https://github.com/BootLoops-ai/bootloops | BootLoops README
> The harness is independent of the model driving it: clone it, point whatever agent you use at it, and the agent gains instruments it can run.
このハーネスは、動かすモデルに依存しない。複製して、使っているエージェントに向けるだけで、そのエージェントは実行できる道具を手に入れる。
:::

なお、教授はこの期間にAnthropicの客員研究者を務めていました。寄稿の注記によると、BootLoopsはAnthropicのプロジェクトではなく、教授が所有して運営しています。

## どう作ったか

出発点は、昨年12月の試みでした。教授はClaude Opus 4.5を研究助手にして論文を1本仕上げましたが、AIの書いた文を1つずつ直す必要がありました。寄稿は、問題の根っこを次のようにまとめています。

:::quote https://www.anthropic.com/research/claude-shaped-science | Anthropic「Claude-shaped science」（Matthew Schwartz氏の寄稿）
> The core conflict, as I see it, is that although these models are brilliant, working like a human scientist is not what current LLMs do best.
私が見るところ、根本的な食い違いは、モデルは極めて優秀でも、人間の科学者のように働くのは今のLLMが最も得意とすることではない点にある。
:::

そこで教授は、人間の科学者のまねをさせるのをやめ、AIが得意な仕事に絞りました。2026年夏にClaude Fable 5が出ると、まず自分の専門の散乱振幅の分野で、複数の論文や言語に散らばった計算手法を1つの枠組みに移し替えさせました。こうして溜まった道具が、ほかの分野の似た計算にも使えると分かってきます。数学や物理の手法を持ち込めば解ける問題を、教授は「Claude-shaped（Claude向きの）問題」と呼んでいます。

運用の構成は単純です。Google CloudのVM上でClaude Codeのセッションを題材ごとに立て、全体を調整して計算資源を配り、結果を検証する親のセッションを1つ置きます。計算は裏で動くサブエージェントに任せ、途中結果はマークダウンのファイルに残します。論文の執筆や、結果を意地悪な査読者の立場で点検する役も、別のセッションに分けています。費用の額は公表していませんが、計算資源とトークンを大量に使ったと書いています。

{{x:https://x.com/AnthropicAI/status/2105733864152858919}}

Anthropicも公式Xでこの寄稿を紹介し、AIと科学の間にある「インピーダンスの不整合」という教授の見立てを取り上げました。

## 成果（教授が公表した数字）

| 分野 | 成果 |
|---|---|
| 素粒子物理 | 楕円型のファインマン積分30個を計算（既知15個の再現、新規15個） |
| 生態学 | パナマのバロ・コロラド島の森で、樹種の入れ替わりが中立説の想定より4.5倍速いと算出 |
| 集団遺伝学 | 1000人ゲノム計画のデータで、近接する変異のペア57億組を分析し、遺伝子変換の証拠を確認 |
| 経済学 | 主要5誌の論文4,452本の再現用コードを有料ソフトからオープンなコードへ移植（約3万ルーチン）し、公表値と照合 |
| 言語学 | 6,072言語の語の強勢をまとめたデータベースと、音韻論の文献16万件の目録を作成 |

（出典：Anthropic研究ブログのSchwartz氏の寄稿）

ただし教授は、どの成果も各分野の専門家と組んで初めて価値が出たと強調しています。生態学の計算は技術的には正しかったものの、植物生物学の専門家からは、中立説が実際の森に合わないことは生態学者の間で定性的には知られていると指摘され、中立説からのずれに注目する形に問いを組み直しています。

## AIの弱点と付き合い方

寄稿は成果だけでなく、Claudeと組んで困った点も具体的に記しています。整理すると、課題は自己評価の甘さと、遠回りな解き方の2つです。

自己評価については、作業時間の見積もりが当てになりませんでした。実際は3日間の作業を、2年がかりの大仕事のように報告したこともあります。完成したと報告してきた証明に未証明の補題が1つ残っていて、それが証明の核心そのものだった例も挙げています。解き方では、道具を新しく作れば数分で済む計算を、何日もかけて力任せに進めようとする癖を指摘しています。

教授の対策は、最後の確認を人が担うことに尽きます。

- 自動の監視を組んでいても、図を出させて自分の目で確かめる
- 計算の正確さと、そこから引き出した結論の正しさは分けて疑う
- Claude向きの問題は無数に見つかるため、取り組む価値があるかは人が選ぶ

## 日本のビジネスへの影響

BootLoopsは無料で使えます。Python 3.12で動き、Linuxで検証されていますが、macOSは正式な対象外です。使うにはClaude Codeなどのコーディングエージェントと、そのモデルの利用料が別に要ります。READMEも寄稿も英語で、対象は数理の研究です。

関係が深いのは、研究開発部門やデータ分析の担当者です。とくに参考になるのは、計算そのものより運用の型です。題材ごとにセッションを分け、親のセッションで検証し、点検役のエージェントを別に立てます。「完成」の基準は先に文書で決めておきます。この型は、社内の分析や開発の仕事にもそのまま持ち込めます。

今すぐやれることは、社内で抱えている「手法さえ知っていれば解ける」分析の宿題を1件選ぶことです。コーディングエージェントに既存の論文やコードを移し替えさせ、結果は人が図で確かめます。エージェントの選び方は[コーディングAIのおすすめ](/best/coding/)にまとめています。

注意点は2つあります。教授自身が書くとおり、AIは完成を早めに宣言しがちで、計算が正しくても結論が誤ることがあります。社外に出す数字は、必ず人が検算してください。また、長時間の並行実行はトークンの消費が大きくなるため、題材を絞って費用の上限を決めてから始めるのが安全です。
