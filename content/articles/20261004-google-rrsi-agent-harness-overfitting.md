---
{
  "title": "RRSIはAIエージェントの自己改良で「試験の丸暗記」を防ぐ手法、Google Researchが論文とコード公開",
  "description": "Google Researchの研究者が、AIエージェントの指示文や手順を自動で改良するときに起きる「評価用の課題への過剰適合」を抑える手法RRSIを発表した。未知のベンチマークで最大4.7ポイント改善し、改良後の実行トークンは正則化なしより約30%少ない。",
  "date": "2026-10-04T22:55:00+09:00",
  "category": "research",
  "tags": ["Google Research", "RRSI", "エージェント", "論文", "ベンチマーク"],
  "summary": [
    "Google Researchの研究者14人が、AIエージェントの指示文・手順・道具の使い方を自動で改良する際の過剰適合を抑える手法RRSIを論文とコードで公開した",
    "RRSIは改良対象の課題で最大14.1ポイント、改良に使っていない5つのベンチマークで最大4.7ポイント成績を上げ、実行トークンは正則化なしの改良より約30%少ない",
    "従来の自動改良は改良に使った課題でだけ点が伸び、未知の課題では元の水準とほぼ変わらないか下回る例があったと論文は指摘している"
  ],
  "sources": [
    {"title": "RRSI: Regularized Recursive Self-Improvement of Agent Harnesses", "publisher": "arXiv", "url": "https://arxiv.org/abs/2609.24972", "kind": "論文"},
    {"title": "RRSI: Regularized Recursive Self-Improvement of Agent Harnesses（HTML版）", "publisher": "arXiv", "url": "https://arxiv.org/html/2609.24972v1", "kind": "論文"},
    {"title": "google-research/rrsi（README）", "publisher": "GitHub google-research", "url": "https://github.com/google-research/rrsi", "kind": "公式ドキュメント"},
    {"title": "Google researchers find a way to keep self-improving AI agents from memorizing their tests", "publisher": "The Decoder", "url": "https://the-decoder.com/google-researchers-find-a-way-to-keep-self-improving-ai-agents-from-memorizing-their-tests/", "kind": "報道"}
  ],
  "thumb_text": "RRSI",
  "share_text": "AIエージェントの自己改良は「試験の丸暗記」になりがち。Google ResearchのRRSIは未知の課題で最大4.7ポイント改善",
  "editor_note": ""
}
---
Google Researchの研究者14人が、AIエージェントを自動で改良するときに起きる「評価に使った課題の丸暗記」を抑える手法「RRSI」の論文を9月21日にarXivで公開し、コードもGitHubに置きました。改良に一度も使っていない5つのベンチマークで最大4.7ポイント成績が上がり、改良後のエージェントが使うトークンは、歯止めをかけずに改良した場合より約30%少なくなったと報告しています。

## 何が発表されたか

RRSI（Regularized Recursive Self-Improvement of Agent Harnesses）とは、エージェントの「ハーネス」を自動で書き換えていく際に、機械学習の正則化の考え方で歯止めをかける手法です。ハーネスは、中身のモデルを包む指示文・処理の流れ・道具の呼び出し・記憶・文脈の管理のことで、同じモデルでもハーネス次第で成績が大きく変わります。

最近は、AIにハーネスの改良案を出させ、課題を解かせて点が上がった案を採用する、という自動改良の手法がいくつも出ています。論文はこれを「エージェントの仕組みのレベルでの再帰的な自己改良」と位置づけたうえで、弱点を次のように書いています。

:::quote https://arxiv.org/abs/2609.24972 | arXiv「RRSI: Regularized Recursive Self-Improvement of Agent Harnesses」
> However, such recursive evolution may overfit by memorizing the training tasks, showing large in-distribution gains that shrink or even vanish on out-of-distribution benchmarks.
しかし、こうした再帰的な改良は改良に使った課題を暗記して過剰適合しやすく、同じ分布の課題では大きく伸びても、分布の外のベンチマークでは伸びが縮むか消えてしまうことがある。
:::

{{card:https://github.com/google-research/rrsi|google-research/rrsi|GitHub}}

## 歯止めの中身

RRSIの歯止めは、改良案を「出す側」と「採る側」の両方にかかります。

- **出す側**: 1回の改良案に含められる変更の数に上限を設け、回を重ねるほど上限を絞ります。過去に試して効かなかった仮説は記録に残し、同じ案を繰り返させません。行き詰まったときは、まだ手を付けていない部品に改良の枠を割きます
- **採る側**: 評価の前に別のAIが改良案を点検し、課題名や答えを書き込むなど特定のベンチマークにしか効かない案をはじきます。点の伸びが誤差の範囲なら採らず、伸びに見合わないほどコストを増やす案も退けます。一定期間、効果が測れなかった部品は削除します

改良案を出すAIも点検役のAIもClaude Opus 4.8で、改良される側のエージェントも同じモデルです。READMEによると、既定の設定ではVertex AI経由でClaude Opus 4.8を呼び出します。ライセンスはApache 2.0ですが、READMEには「Googleの公式製品ではない」と明記されています。

## 成果の数字

試験は8つのベンチマークで、改良に使う課題と、一度も見せない課題を分けています。コーディングではTerminal-Bench 2.1で改良し、SWE-bench Verifiedで確かめました。業務系では法務の課題集Harvey LABで改良し、JobBench・GDPval・APEX-Agentsで確かめています。設計系はEngDesignで改良し、Frontier-Engで確かめました。

業務系の結果（論文の表1・表2から）を並べると、傾向がはっきりします。

| 方式 | 改良に使った課題 | 見せていない3ベンチマークの平均 | 1回あたりのトークン |
|---|---|---|---|
| 改良なし | 89.4 | 39.7 | 156万 |
| 歯止めなしの改良 | 92.8 | 40.3 | 380万 |
| RRSI | 90.5 | 43.6 | 242万 |

歯止めなしの改良は、改良に使った課題では最高点を取る一方、見せていない課題では改良なしとほぼ同じで、トークンは2倍超に膨らみました。RRSIは改良に使った課題の点を2.3ポイント譲る代わりに、未知の課題で3.3ポイント上回っています。先行する4つの自動改良手法とも比べ、改良に使った課題で最も高かったMeta-Harnessも、未知の課題ではRRSIを下回りました。

モデルを替えても効果は出ています。Gemini 3.5 FlashでTerminal-Bench 2.1を改良すると64.6から78.7へ14.1ポイント上がり、見せていないSWE-bench Verifiedでも2.2ポイント伸びました。そのハーネスを、改良に一度も参加していない小型のGemini 3.1 Flash Liteにそのまま使うと、11.2から14.6に上がっています。

## 反応と論点

The Decoderは、RRSIが未知の課題で一度も改良前の水準を下回らなかった点を、比較した他の手法との違いとして報じています。NVIDIAなども、エージェントのトークン消費を減らす手法を相次いで発表していると伝えました。

一方で限界もあります。論文自身が挙げるように、モデルの重みは固定したままの手法で、結果は限られた改良用の課題と設定値に左右されます。表の数字が示すとおり、RRSIのハーネスも改良前よりトークンは多く使います。また、OpenAIでは社内のAIが評価中に想定外の行動を取った事例が報告されており（[関連記事](/news/20261003-openai-misalignment-reports-shutdown-slack/)）、「AIがAIを改良する」仕組みに歯止めをどう組み込むかは、性能だけでなく安全面の論点にもなっています。

## 日本のビジネスへの影響

RRSIは研究用のコードで、製品として提供されているわけではありません。動かすにはGoogle CloudのVertex AIの認証と、各ベンチマークの環境が必要です。日本語の課題での評価は論文にありません。

関係が深いのは、社内向けにAIエージェントを作っている開発者と、そのプロンプトを調整しているチームです。手作業でも自動でも、「手元の評価用の質問で点が上がったから採用」を繰り返すと、同じことが起きます。今すぐやれることは、評価用の質問を「改良に使う分」と「最後まで見ない分」に分け、プロンプトを変えたら見ない分の点とトークン数も記録することです。課題名や想定回答をプロンプトに書き込んでいないかの点検も、RRSIの点検役と同じ考え方で人がすぐにできます。

注意点は、自動改良を回すとそれ自体のAPI費用がかさむことです。論文の設定では改良案を出す側にも点検役にもClaude Opus 4.8を使っており、同じ規模で試すと費用は小さくありません。エージェントを動かすツールの選び方は[コーディングAIのおすすめ](/best/coding/)で比べています。
