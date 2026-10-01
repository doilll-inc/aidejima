---
{
  "title": "モデル蒸留を狙う組織的攻撃をOpenAIが阻止、中核はKimi開発元の関係者と判断",
  "description": "OpenAIは、自社モデルの隠れた推論を引き出す組織的な「蒸留」攻撃を7月28日までに遮断したと公表した。関連する動きは1万5000人超の利用者群に及び、中核はKimiを開発するMoonshot AIの関係者によるものとしている。",
  "date": "2026-10-01T15:06:00+09:00",
  "updated": "2026-10-01T18:54:00+09:00",
  "category": "policy",
  "tags": [
    "OpenAI",
    "Kimi",
    "Moonshot AI",
    "セキュリティ",
    "中国AI",
    "蒸留"
  ],
  "summary": [
    "OpenAIは、モデルの隠れた推論を無断で引き出す「敵対的蒸留」の組織的攻撃を7月28日までに遮断したと公表",
    "7月24〜25日には4,000人超の利用者から1万6,000件の要求が集中し、関連の利用者群は1万5,000人を超えた",
    "OpenAIは中核をKimi開発元Moonshot AIの関係者と判断し、業界団体と政府に情報を共有した"
  ],
  "sources": [
    {
      "title": "Disrupting a coordinated model-distillation campaign",
      "publisher": "OpenAI",
      "url": "https://openai.com/index/disrupting-a-coordinated-model-distillation-campaign"
    },
    {
      "title": "Stealing Reasoning Traces from Proprietary LLM APIs",
      "publisher": "arXiv",
      "url": "https://arxiv.org/abs/2608.09867"
    },
    {
      "title": "We can finally talk about it: We found a way to extract hidden reasoning of frontier models",
      "publisher": "X @kotekjedi_ml",
      "url": "https://x.com/kotekjedi_ml/status/2087147042888114428"
    },
    {
      "title": "AI race heats up as OpenAI flags alleged model-copying campaign",
      "publisher": "CNBC",
      "url": "https://www.cnbc.com/2026/10/01/openai-chinas-moonshot-ai-kimi.html"
    },
    {
      "title": "OpenAI Accuses Moonshot AI of Coordinated Model Distillation",
      "publisher": "BankInfoSecurity",
      "url": "https://www.bankinfosecurity.com/openai-accuses-moonshot-ai-coordinated-model-distillation-a-32982"
    }
  ],
  "thumb_text": "モデル蒸留攻撃",
  "share_text": "OpenAIがモデル蒸留を狙う組織的攻撃を阻止。中核はKimi開発元Moonshot AIの関係者と判断",
  "editor_note": ""
}
---
OpenAIは現地時間9月30日、自社モデルの隠れた推論を組織的に引き出そうとする攻撃を検知し、7月28日までに遮断したと公式ブログで公表しました。関連する動きは1万5,000人を超える利用者群に及び、OpenAIはその中核を、中国の対話AI「Kimi」を開発するMoonshot AIの関係者によるものと判断しています。

## 何が起きたか

OpenAIが公表した経過は次のとおりです。

- 7月1日：活動が始まる（当初は少量）
- 7月24〜25日：4,000人超の利用者から、抜き取りの型に沿った要求が1万6,000件集中
- その後の調査：似た指示の型を使う1万5,000人超の利用者群を特定
- 7月28日：この利用者群を完全に遮断

関わった全員が同じ主体かどうかはわからない、とOpenAIは断っています。そのうえで、中核の集団をMoonshot AIの関係者によるものと判断しました。

OpenAIはこの行為を「敵対的蒸留」と位置づけています。蒸留とは、あるモデルの出力を教材にして別のモデルを育てる手法で、相手の了解があれば広く使われています。許可なく組織的に行えば、他社が多額の投資で作ったモデルの能力を安く写し取れてしまうことが問題です。

:::quote https://openai.com/index/disrupting-a-coordinated-model-distillation-campaign | OpenAI公式ブログ「Disrupting a coordinated model-distillation campaign」
> This activity is consistent with adversarial distillation: the systematic and unauthorized use of one model’s outputs or reasoning to help train, reproduce, or improve another model.
この活動は敵対的蒸留、つまりあるモデルの出力や推論を体系的かつ無断で使い、別のモデルの学習・再現・改良に役立てる行為と一致します。
:::

## 手口：暗号化された推論の使い回し

狙われたのは「保護された推論」、つまりモデルが答えを出す前に内部で積み上げる思考の記録です。最終回答には出さない情報を含むため、各社は中身を利用者に見せていません。arXivの論文によると、大手各社はこの推論をサーバーに保存せず、暗号化したかたまりとして利用者側に返し、次の要求のたびに送り返させています。

攻撃者が突いたのはこの仕組みでした。ある会話で受け取った暗号化済みの推論を別の会話に持ち込み、モデル自身に解読して書き出させたのです。暗号が破られたわけではなく、データベースや保存された会話への侵入もなかったとOpenAIは説明しています。

全体像をつかむうえでは、独立した研究者からの責任ある開示（修正前に企業へ非公開で知らせること）も役立ちました。報告されたのは、別のモデルや会話の要約機能を経由して推論が漏れる弱点で、OpenAIは攻撃経路が実在することを確かめています。

## OpenAIの対策

OpenAIが挙げた対策を、分野ごとに整理すると次のようになります。

| 分野 | 主な対策 |
|---|---|
| アカウント | 不正アカウントの停止・制限、登録手続きとインフラの管理強化、関連ネットワークの監視拡大 |
| 推論の保護 | 他人の暗号化済み推論を送り直して中身を取り出す経路の封鎖、推論を漏らしそうなストリーミング出力の検知と保留 |
| 外部との連携 | 外部サービスを経由した動きへの事業者と共同の対処、AI大手の業界団体Frontier Model Forumと政府の情報共有の枠組みでの共有 |

公表の前には影響範囲を調べて対策を済ませ、研究者や業界の意見も聞いたといいます。クラウド事業者経由の提供にも同じ守りを広げる作業が残っており、OpenAIは対策を続けるとしています。

## 背景

OpenAIが特に問題視するのは、抜き取った推論で学習したモデルには元のモデルの安全策が引き継がれない点です。安全への投資を省いたまま高い能力だけが広がれば、軍事にも民生にも使える分野では国家安全保障上のリスクになるとの立場です。

中国勢への疑いは今回が初めてではありません。CNBCとBankInfoSecurityによると、Anthropicも9月、Moonshot AIを含む中国の開発企業がClaudeを無断で学習に使ったと指摘しています。BankInfoSecurityは、米国のサイバーセキュリティ・インフラ安全保障庁（CISA）も、米国製モデルからデータや推論を抜き取っているとみる組織の一つにMoonshot AIを挙げたと報じています。中国製モデルの能力をめぐっては「[GLM-5.3の攻撃コード作成力](/news/20260930-anthropic-glm-5-3-cyber-capabilities/)」の記事も参照してください。

## 反応と論点

OpenAIが言及した研究者の論文は、8月にarXivで公開されています。暗号化された推論のかたまりが、同じ会社の別の会話・利用者・モデルの間でそのまま通用する点に目を付け、守りの弱いモデルに解読させる手法です。OpenAI・Anthropic・Googleの3社で推論を取り出せたとしています。

著者の一人Alexander Panfilov氏はXで、全フロンティアAI企業のAPIにある弱点を使って隠れた推論を取り出せたと投稿しました。

{{x:https://x.com/kotekjedi_ml/status/2087147042888114428}}

論文の報告はそれだけではありません。開発者が公開した作業ログから31万5,320個の推論のかたまりを解読したところ、個人情報367件と認証情報182件が見つかったといいます。推論の抜き取りは、蒸留だけでなく情報漏えいの入り口にもなり得るということです。

一方、OpenAIの発表は、抜き取った推論が実際にKimiの学習に使われたかどうかまでは示していません。執筆時点で、Moonshot AIが今回の発表に反論した声明は確認できませんでした。

## 日本のビジネスへの影響

今回の件で、OpenAIの製品やAPIの使い方がすぐに変わるわけではありません。ただ、推論を漏らしそうな出力を止める確認が加わっており、正規の利用で応答にどう影響するかは示されていません。

関係が深いのは、推論モデルをAPIで使う開発者と情報システム担当者です。論文が示したとおり、暗号化された推論のかたまりは「読めないから安全」ではありません。今すぐやれるのは、GitHubや社外向け資料にエージェントの実行ログをそのまま載せていないか確認し、載せていた場合は削除して、含まれていた可能性のある認証情報を差し替えることです。

注意点として、他社モデルの出力を自社モデルの学習に使う場合は、利用規約で認められているかを必ず確かめてください。OpenAIは今回の行為を利用規約違反と位置づけています。Kimiなど中国製モデルの採用を検討する企業は、米国企業が相次いで名指ししている状況も判断材料に入れておくべきです。API選びの比較は「[AI APIの料金比較と選び方](/best/api/)」にまとめています。
