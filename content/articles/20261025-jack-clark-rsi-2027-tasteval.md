---
{
  "title": "AIが自分でAIを改良し続ける時代は2027年にも、Anthropic共同創業者が予測を1年早める",
  "description": "Anthropic共同創業者のジャック・クラーク氏が、AIが人の手を借りずに次のAIを作り続ける「再帰的自己改善」の時期の予測を2028年から2027年に早めた。根拠の1つは、AIの研究の「目利き」が3か月ごとに倍になっているという新しい測定結果だ。",
  "date": "2026-10-25T22:25:00+09:00",
  "category": "research",
  "tags": ["Anthropic", "Jack Clark", "TasteVal", "Claude Opus 5.5", "安全性", "論文"],
  "summary": [
    "Anthropic共同創業者のジャック・クラーク氏は、AIが自分で次のAIを改良し続けられるようになる時期を、2028年から2027年の見込みに早めた",
    "根拠の1つは米P-Zero Researchの測定で、AIが研究の実験を設計し結果を読み解く力は2025年12月から3か月ごとに倍になっていた",
    "8つのAI開発の課題で、Claude Opus 5.5は人間の専門家24人の最高の結果を、半分以下の計算量で上回った。費用は専門家1回分の約30分の1だった"
  ],
  "sources": [
    {"title": "Import AI 476: Creativity and RSI; worse-than-China open weight models; AI goes to space", "publisher": "Import AI（Jack Clark）", "url": "https://jack-clark.net/2026/10/12/import-ai-476-creativity-and-rsi-worse-than-china-open-weight-models-ai-goes-to-space/", "kind": "公式サイト"},
    {"title": "Introducing TasteVal", "publisher": "P-Zero Research", "url": "https://pzeroresearch.com/work/tasteval/", "kind": "公式サイト"},
    {"title": "TasteVal: Measuring the Experimental Research Taste of AI Systems Against Human Experts", "publisher": "arXiv", "url": "https://arxiv.org/abs/2610.06824", "kind": "論文"},
    {"title": "Anthropic co-founder Jack Clark moves his prediction for self-improving AI forward to 2027", "publisher": "The Decoder", "url": "https://the-decoder.com/anthropic-co-founder-jack-clark-moves-his-prediction-for-self-improving-ai-forward-to-2027/", "kind": "報道"}
  ],
  "thumb_prompt": "A small robot arm carefully assembling a slightly larger robot arm on a workbench, which in turn is reaching toward an even larger unfinished arm, with a wall calendar in the background showing a single circled date.",
  "thumb_style": "diorama",
  "thumb_text": "AIがAIを作る",
  "share_text": "AIが自分でAIを改良し続ける時代は2027年にも。Anthropic共同創業者が予測を1年早めた根拠は「研究の目利き」が3か月で倍",
  "editor_note": ""
}
---
Claudeを開発するAnthropicの共同創業者ジャック・クラーク氏が、AIが人の手を借りずに次のAIを改良し続ける「再帰的自己改善」が可能になる時期の予測を、2028年から2027年に早めました。根拠の1つに挙げたのは、AIが研究の実験を組み立てる力が2025年12月から3か月ごとに倍になっているという、米P-Zero Researchの測定結果です。

## 何が起きたか

クラーク氏は、自身が毎週書いているAIの研究ニュースレター「Import AI」の476号（現地時間10月12日）で予測を改めました。ドイツのAI専門メディアThe Decoderが10月25日に取り上げ、改めて注目されています。

再帰的自己改善とは、AIが自分より優れたAIを作り、そのAIがさらに次のAIを作る、という改良の連鎖を人の手を借りずに回せる状態のことです。AIの安全性を議論する人たちの間では、AIの進歩が人間の監督の速さを超えかねない節目として扱われてきました。

:::quote https://jack-clark.net/2026/10/12/import-ai-476-creativity-and-rsi-worse-than-china-open-weight-models-ai-goes-to-space/ | Import AI 476（Jack Clark）
> I now think it's more likely we'll see full RSI become possible in 2027, whereas before I thought it was more likely in 2028.
いまは、完全な再帰的自己改善が可能になるのは2027年の可能性の方が高いと考えている。以前は2028年の可能性の方が高いと考えていた。
:::

クラーク氏はこれまで、AIがどれだけ速く自分を改良できるかを左右するのは「創造性」だと論じ、今年の時点ではAIはまだそれを大きく示していないと書いていました。今回は、その後にAIが数学で創造的に見える成果を次々に出していることと、AIの研究そのものでも腕が上がっている兆しが出てきたことを、考えを変えた理由に挙げています。

## 根拠になった「研究の目利き」の測定

クラーク氏が取り上げたのは、米P-Zero Researchのオリー・ジャッフェ氏とデーン・シャーバーン氏が10月に公開した「TasteVal」という評価です。研究者の世界で「センスがいい」と言われる力を、AIでも測ろうとしたものです。

P-Zeroは研究のセンスを「面白い問題を選ぶ」「実験を設計する」「結果を読み解く」の3つに分け、TasteValではあとの2つを測ります。課題は、AIの学習データの選び方や、悪意ある指示への強さを上げる工夫など、AI開発の現場に近い8つ。プログラムを書く作業は別のAIが一律に担当し、評価されるAIは「次に何を試すか」と「結果から何がわかるか」だけを考えます。

:::quote https://pzeroresearch.com/work/tasteval/ | P-Zero Research「Introducing TasteVal」
> A model that reaches the experts' score with half the experimental compute has twice their experimental research taste.
専門家と同じ点数に半分の実験用の計算量で届くモデルは、専門家の2倍の実験の目利きがある、とみなす。
:::

結果は次のとおりです。

| 項目 | 結果 |
|---|---|
| 比べた人間 | OpenAI、Google DeepMind、NVIDIA、Microsoft Researchなどで最近まで働いていた専門家24人（各課題で2人以上）の最高の結果 |
| 最も成績のよかったAI | AnthropicのClaude Opus 5.5。専門家の約2.3倍の効率（統計的な幅は1.15〜4.37倍） |
| 費用 | Claude Opus 5.5の1回の挑戦にかかった費用は、専門家1回分の平均の約30分の1 |
| 伸びの速さ | 最先端のAIの目利きは2025年12月以降、3.0か月ごとに倍（幅は1.7〜5.0か月）。それ以前の伸びはずっと緩やかだった |

言い換えると、最上位のAIは、同じ課題でトップクラスの人間の専門家と同じ成果を、半分以下の実験量で出せたということです。

## 反応と論点

P-Zero自身は、結果が実態より速い伸びに見えている可能性を認めています。課題はすぐに答え合わせができるもので、AI企業が最も鍛えやすい種類であること、比べた人間に世界トップの研究者は含まれていないことが理由です。また「どの問題に取り組むべきか」を選ぶ力は測っていません。逆に、AIへの指示の工夫は控えめにしたため、実力を低く見ている可能性もあるとしています。

数字の幅が広い点にも注意が要ります。2.3倍という結果も、統計的には1.15倍から4.37倍までありえる範囲です。クラーク氏自身もTasteValの結果を「いくつかの兆し」と表現しており、2027年と決めつけているわけではありません。

The Decoderは、クラーク氏が5月に書いた文章では、AIが自力でより強い後継を育てる確率を2027年末までに約30%、2028年末までに約60%と見積もっていたと報じています。開発を手がける当の企業の幹部が自ら時期を早めたことは、規制や安全対策の議論にも影響しそうです。一方で、こうした予測は人によって大きく割れており、AIは若手研究者の代わりにはなっても、長期の研究の方向を決める力はまだないという見方もあると同メディアは伝えています。

AIの安全性をめぐっては、OpenAIが社内のAIの作業の一部が監視の外にあったと外部の専門家の点検で指摘されたばかりです（[OpenAI社内のAIの作業、最大4分の1が見張りの外に](/news/20261024-metr-redwood-openai-monitoring-audit/)）。AIがAIを作る速さが上がるほど、人間がどう点検するかが問われます。

## 日本のビジネスへの影響

- **使えるか**: 研究者の予測と評価の結果で、新しいサービスの発表ではありません。測定で最も成績がよかったClaude Opus 5.5は、日本からもClaudeの有料プランやAPI（他社のシステムからAIを呼び出す仕組み）で使えます
- **誰にどう効くか**: AIへの投資や中期計画を決める経営者・経営企画の担当者に関係します。AIの性能が数か月単位で倍になる前提に立つと、3年がかりのシステム開発計画や、人の採用・育成の計画は途中で前提が崩れる可能性があります
- **今すぐやれること**: 社内でAIを使っている業務を1つ選び、半年前のAIと今のAIで出来がどれだけ変わったかを記録しておくと、自社にとっての伸びの速さを実感で測れます。AIの選び方は[チャットAIのおすすめと料金比較](/best/chat/)にまとめています
- **注意点**: 「2027年」は1人の研究者の見立てで、根拠のTasteValも8課題・小さな規模の測定です。数字だけを切り取って「2027年にAIが人間を超える」と社内外に説明すると誤解を招きます
