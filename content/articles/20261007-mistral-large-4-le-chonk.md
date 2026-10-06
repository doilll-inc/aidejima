---
{
  "title": "フランスのMistralが新AI「Mistral Large 4」、月末に中身を無料公開し他社が断るセキュリティ作業も",
  "description": "フランスのMistral AIが新モデルMistral Large 4のプレビューを公開した。パラメーター1兆の大型モデルで、10月末に中身（重み）を公開する。価格は入力100万トークン$1.36で、プレビュー中は半額。",
  "date": "2026-10-07T00:00:00+09:00",
  "category": "models",
  "tags": ["Mistral AI", "Mistral Large 4", "オープンウェイト", "セキュリティ", "ソブリンAI"],
  "summary": [
    "フランスのMistral AIが10月6日、新しい大型AIモデル「Mistral Large 4」のプレビューを開発者向けに公開した",
    "Mistralは10月末にモデルの中身を公開する予定で、誰でも自社のサーバーで動かせるようになる",
    "Mistral AIは、ClaudeやGPTが断る脆弱性の再現作業で82%を記録したと公表し、欧州で完結する運用も売りにしている"
  ],
  "sources": [
    {"title": "Introducing Mistral Large 4", "publisher": "Mistral AI", "url": "https://mistral.ai/news/mistral-large-4/", "kind": "公式発表"},
    {"title": "Mistral Large 4（モデルカード）", "publisher": "Mistral AI Docs", "url": "https://docs.mistral.ai/models/mistral-large-4-0", "kind": "公式ドキュメント"},
    {"title": "Mistral AI の投稿", "publisher": "X @MistralAI", "url": "https://x.com/MistralAI/status/2107457414387622310", "kind": "X投稿"},
    {"title": "Guillaume Lample の投稿", "publisher": "X @GuillaumeLample", "url": "https://x.com/GuillaumeLample/status/2107461898127954001", "kind": "X投稿"},
    {"title": "Mistral Large 4 is Europe's trillion-parameter answer to US models that refuse security work", "publisher": "The Decoder", "url": "https://the-decoder.com/mistral-large-4-is-said-to-be-the-most-powerful-open-ai-model-from-europe-and-the-u-s/", "kind": "報道"},
    {"title": "Mistral's new 1T model aims to leapfrog closed and open rivals", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/10/06/mistrals-new-1t-model-aims-to-leapfrog-closed-and-open-rivals/", "kind": "報道"}
  ],
  "thumb_text": "Mistral Large 4",
  "thumb_style": "photo",
  "thumb_prompt": "A huge, fluffy, very round orange cat sitting calmly inside a European server room between rows of glowing server racks, one paw resting on a heavy steel vault door that stands slightly open.",
  "share_text": "フランスのMistralが1兆パラメーターの新AIを公開。月末に中身も無料公開、他社が断るセキュリティ作業もこなす",
  "editor_note": ""
}
---
フランスのAI企業Mistral AIは現地時間10月6日、新しい大型モデル「Mistral Large 4」のプレビュー版を公開しました。モデルの規模を示すパラメーター数は1兆で、10月末にはモデルの中身（重み）を公開し、企業が自社のサーバーで動かせるようにします。

## 何が発表されたか

Mistral Large 4とは、文章と画像を最初から一緒に学習した、Mistral AIで最大の汎用AIモデルです。「Le Chonk（ぽっちゃりさん）」という愛称も付いています。今は開発者向けの「Mistral Studio」からAPI（ほかのソフトからAIを呼び出す窓口）で試せる段階で、重みは月末に公開すると公式ブログに書いています。

仕組みは「MoE（専門家の混合）」と呼ばれる方式です。全体は1兆パラメーターありますが、1回の回答で実際に働くのはそのうち490億だけなので、規模のわりに動かす費用を抑えられます。モデルカードによると、一度に読み込める長さは100万トークンで、長い契約書や報告書を何本もまとめて読ませられる長さです。

:::quote https://mistral.ai/news/mistral-large-4/ | Mistral AI公式ブログ「Introducing Mistral Large 4」
> ML4 was trained from scratch on 3,800 NVIDIA Grace Blackwell GPUs in Mistral's own datacenters in Europe.
ML4は、欧州にあるMistral自身のデータセンターで、NVIDIAのGrace Blackwell GPU 3,800基を使ってゼロから学習した。
:::

料金は次のとおりです（100万トークンあたり）。

| | 入力 | 出力 |
|---|---|---|
| Mistral Large 4（通常価格） | $1.36 | $4.18 |
| Mistral Large 4（プレビュー期間中） | $0.68 | $2.09 |
| 前の上位モデル Mistral Medium 3.5 | $1.50 | $7.50 |
| 参考：Claude Opus 5.5 | $4.00 | $20.00 |

通常価格は公式ブログ、プレビュー価格はモデルカードの表示です。上位モデルとしては、前のMedium 3.5より入力も出力も安くなりました。

{{card:https://docs.mistral.ai/models/mistral-large-4-0|Mistral Large 4（モデルカード・料金）|Mistral AI Docs}}

## 売りは「他社が断る仕事」と「欧州で完結」

公式ブログが特に強調しているのはセキュリティの分野です。ソフトの弱点（脆弱性）が本当に悪用できるかを再現する試験で、Mistral Large 4は82%を記録したといいます。守る側にとって、弱点が本物かを確かめる作業は対策の第一歩になります。

:::quote https://mistral.ai/news/mistral-large-4/ | Mistral AI公式ブログ「Introducing Mistral Large 4」
> Several leading closed models, including Claude Opus 5.5 and GPT-6 Astra, score near zero on the same test because they refuse to perform the task.
Claude Opus 5.5やGPT-6 Astraなど主要な非公開モデルの多くは、同じ試験でほぼ0点だった。作業そのものを拒否するためだ。
:::

法律と金融の業務を試す評価でもGPT-6 Astraを上回ったとしています。もう1つの売りは置き場所です。Mistralは、欧州の法律のもとで、ほかのクラウド会社に頼らず自社で運用する欧州向けの提供を用意すると書いています。学習データは160以上の言語にまたがり、EUの公用語はすべて含むといいます。

## 反応と論点

Mistral AIは公式Xで「米国か欧州で作られた公開型モデルでは、総合の評価で最も高い」と発表しました。

{{x:https://x.com/MistralAI/status/2107457414387622310}}

共同創業者のギヨーム・ランプル氏もXで、Mistral Large 4は公開型モデルの最先端にあると投稿しています。

{{x:https://x.com/GuillaumeLample/status/2107461898127954001}}

一方で、最先端との差は残ります。The Decoderは、第三者の評価機関Artificial Analysisの総合指数でMistral Large 4は38点で、前のLarge 3の9点から大きく伸びたものの、Claude Opus 5.5（最大設定）の58点には20点届かないと報じています。比べる相手も「米国と欧州の公開型」に限られており、中国のDeepSeekやQwenを含めた順位ではありません。

TechCrunchは、Mistralの幹部が学習に使ったGPUの数は中国の競合の2〜3分の1だと説明したと報じています。他社が断る攻撃寄りの作業をこなす点は、守る側にとっては利点ですが、悪用の心配と裏表です。The Decoderによると、Mistralのアルチュール・メンシュCEOは仏議会で、欧州がサイバー防衛を米国のモデルに頼る危うさを訴えていました。欧州発のAIをめぐっては、ドイツのAleph Alphaも自社で動かせるモデルを出しています（[既報](/news/20261005-aleph-alpha-chinese-llm-party-line-benchmark/)）。

## 日本のビジネスへの影響

- **使えるか**: APIは世界の複数地域で提供するとしており、日本からもMistral Studioで試せます。ただし日本の地域でデータを処理するという記載はありません。月末に重みが公開されれば自社のサーバーでも動かせますが、ライセンスの条件はまだ発表されていません
- **誰にどう効くか**: 社外のAIにデータを渡せない金融・製造・官公庁向けの情報システム部門や、脆弱性診断を手がけるセキュリティ担当者に関係が深い話です。米国のAIが断る作業も任せられる選択肢が増えます
- **今すぐやれること**: プレビュー期間中は通常の半額なので、社内の文書要約や契約書チェックなど、いま使っているAIでこなしている作業を数件流し、品質と費用を比べておくとよいです
- **注意点**: プレビュー版なので仕様や価格が変わる可能性があります。日本語の性能について公式の評価結果は出ていません。総合の性能ではClaudeやGPTの最上位にまだ届かないという第三者評価もあり、置き換えは試してから判断してください

各社のAIをAPIで使うときの料金の比較は、[AI APIのおすすめと料金比較](/best/api/)にまとめています。
