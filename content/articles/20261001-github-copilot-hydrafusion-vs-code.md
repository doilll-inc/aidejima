---
{
  "title": "HydraFusionがVS CodeとCopilotアプリに、複数のAIモデルで下書きと点検を分担",
  "description": "GitHubはCopilotの研究プレビュー機能HydraFusionを、CLIに続きVS CodeとGitHub Copilotアプリでも使えるようにした。作業ごとに複数のモデルを組み合わせ、GitHubの評価ではOpus 5に近い品質のまま費用を36〜67%抑えた。",
  "date": "2026-10-01T18:32:00+09:00",
  "category": "dev",
  "tags": ["GitHub", "GitHub Copilot", "HydraFusion", "コーディング", "エージェント", "新機能"],
  "summary": [
    "GitHub CopilotのHydraFusionが、CLIに加えてVS Code（1.140以降）とGitHub Copilotアプリで使えるようになった",
    "HydraFusionは作業ごとに1モデル・段階的な格上げ・別モデルによる点検の3通りから進め方を選び、複数モデルを組み合わせる",
    "対象はCopilot Pro・Pro+・Business・Enterprise。追加料金はなく、使ったモデルごとの標準料金でAIクレジットを消費する"
  ],
  "sources": [
    {"title": "HydraFusion in VS Code and the GitHub Copilot app", "publisher": "GitHub Changelog", "url": "https://github.blog/changelog/2026-09-30-hydrafusion-in-vs-code-and-the-github-copilot-app", "kind": "公式ドキュメント"},
    {"title": "Using HydraFusion", "publisher": "GitHub Docs", "url": "https://docs.github.com/en/early-access/copilot/hydrafusion", "kind": "公式ドキュメント"},
    {"title": "Project HydraFusion: Frontier quality via multi-model orchestration", "publisher": "GitHub Blog", "url": "https://github.blog/ai-and-ml/github-copilot/project-hydrafusion-frontier-quality-via-multi-model-orchestration/", "kind": "公式発表"},
    {"title": "GitHub Copilot のプラン", "publisher": "GitHub", "url": "https://github.com/features/copilot/plans", "kind": "公式ドキュメント"}
  ],
  "thumb_text": "HydraFusion",
  "share_text": "GitHub CopilotのHydraFusionがVS Codeとアプリに。複数モデルで下書きと点検を分担し、追加料金はなし",
  "editor_note": ""
}
---
GitHubは現地時間9月30日、GitHub Copilotの研究プレビュー機能「HydraFusion」を、Visual Studio Code（VS Code）とGitHub Copilotアプリでも使えるようにしたとChangelogで発表しました。これまではCopilot CLIだけでした。対象はCopilot Pro・Pro+・Business・Enterpriseで、HydraFusion自体の追加料金はありません。

## 何が発表されたか

HydraFusionとは、作業ごとに進め方と使うモデルを選び、複数のAIモデルを組み合わせて1つの回答を返す仕組みです。モデルの選択欄に並びますが、それ自体は1つのモデルではありません。

:::quote https://github.blog/changelog/2026-09-30-hydrafusion-in-vs-code-and-the-github-copilot-app | GitHub Changelog「HydraFusion in VS Code and the GitHub Copilot app」
> HydraFusion appears in the model picker, but rather than being a single model, it orchestrates multiple models.
HydraFusionはモデルの選択欄に表示されますが、1つのモデルではなく、複数のモデルを組み合わせて動かします。
:::

推論・コード生成・デバッグ・ツール操作の得意不得意をもとに、品質の基準を満たす一番効率のよい進め方を、次の3つから選びます。

| 進め方 | 中身 |
|---|---|
| Single | 選んだ1つのモデルがそのまま解く |
| Cascade | 軽いモデルが下書きし、合格しなければ強いモデルに引き継ぐ |
| Critique | 1つのモデルが下書きし、別の系統のモデルが読むだけの立場で点検、最初のモデルが1回直す |

VS Codeでは、バージョン1.140以降（またはInsiders版）で`chat.copilot.hydraFusion.enabled`をオンにすると、Copilot Chatのモデル選択欄に現れます。Copilotアプリでは、設定の「Experimental」でオンにします。今回の更新では、各段階で何をしているかの表示と、長い作業中の進み具合の表示も改善しました。

## 料金と対象プラン

公式ドキュメントによると、使った各モデルの標準料金でAIクレジット（Copilotの利用量の単位）を消費し、HydraFusionの別料金はありません。ただし1つの作業で複数のモデルを使うため、1モデルより多くクレジットを使うことがあります。モデルを1つ自動で選ぶ「Auto」には有料プランで割引がありますが、HydraFusionには適用されません。

BusinessとEnterpriseでは、管理者がプレビュー機能を許可する必要があります。使うのは契約中のプランと組織のルールで認められたモデルだけで、利用者が組み合わせを指定することはできません。研究プレビューのため、SLA（稼働の保証）はなく、本番の業務向けではないと明記しています。

## GitHubが公表した性能

GitHubが9月4日に公開した研究ブログでは、3つのコーディング評価でClaude Opus 5と比べています。ターミナル上の作業を解くTerminalBench 2.1では、推定費用を67%抑えながら正答の割合が4.9ポイント上がりました。

| 評価 | 費用（Opus 5比） | 品質（Opus 5比） |
|---|---|---|
| TerminalBench 2.1 | 67%減 | +4.9ポイント |
| DeepSWE | 36%減 | −1.5ポイント |
| CheckpointBench（社内） | 65%減 | −0.1ポイント |

いずれもGitHub自身による、最も成績のよい設定でのオフライン評価で、推論の深さはすべてのモデルで中程度にそろえています。第三者の再計測ではなく、実際の開発作業で同じ結果が出るかを研究プレビューで確かめるとしています。

## Autoとの違いと注意点

Autoは依頼ごとにモデルを1つ選びます。HydraFusionは、1回のやり取りの中で進め方を選び、複数のモデルを連携させる点が違います。公式ドキュメントは、日常の作業にはAuto、複数ファイルにまたがる修正のような大きめで範囲のはっきりした作業にはHydraFusion、と使い分けを勧めています。

注意点として、HydraFusionが下書きを捨てても、その下書きがすでに加えたファイルの変更は自動では元に戻りません。作業に合わせてモデルを自動で選び、費用を抑える考え方は、Cloudflareが同じ日に出した[Auto Router](/news/20261001-cloudflare-agent-tools-roundup/)にも共通します。

## 日本のビジネスへの影響

GitHub Copilotは日本からも契約でき、Proは月10ドルです。HydraFusionの対象に無料プランは含まれず、今回の発表と公式ドキュメントに日本語での性能の説明はありません。

関係が深いのは、開発チームのリードと、会社のCopilotを管理する担当者です。ProやPro+の利用者は、設定をオンにして、範囲のはっきりしたバグ修正を1つ任せ、Autoで解いた場合と結果と消費クレジットを比べるのが手早い試し方です。BusinessやEnterpriseの管理者は、稼働の保証がない点を踏まえてプレビュー機能を許可するかを決め、許可する場合も当面は検証用の作業に使うよう社内で決めておくと安全です。

注意点は、作業によってはクレジットを多く使うこと、捨てられた下書きの変更が残ることです。コミット前に必ず差分を確かめてください。性能の数字はGitHubの社内評価です。Copilotと他のコーディングAIの料金は「[コーディングAIのおすすめと料金比較](/best/coding/)」で比べられます。
