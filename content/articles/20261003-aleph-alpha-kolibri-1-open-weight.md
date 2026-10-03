---
{
  "title": "Aleph AlphaがKolibri-1を公開、78Bで稼働3.46BのMoEを自社GPUで動かせる",
  "description": "ドイツのAleph Alphaが独英2言語に絞ったオープンウェイトのMoEモデル「Kolibri-1」を公開した。総パラメータ78Bのうち1トークンで動くのは3.46Bで、最大100万トークンを扱える。Apache 2.0で商用利用でき、H200なら1枚で動く。",
  "date": "2026-10-03T22:40:00+09:00",
  "category": "dev",
  "tags": ["Aleph Alpha", "Kolibri-1", "オープンウェイト", "ローカルLLM", "ソブリンAI"],
  "summary": [
    "ドイツのAleph Alphaは10月3日、独英2言語に特化したMoEモデルKolibri-1の重みをApache 2.0でHugging Faceに公開した",
    "Kolibri-1は総パラメータ78Bのうち1トークンあたり3.46Bだけを動かし、学習時の文脈長は26万トークン、検証済みの上限は100万トークン",
    "Kolibri-1の対応言語はドイツ語と英語のみで日本語は対象外。日本企業には自社GPUで閉じて動かすMoEの比較対象として意味がある"
  ],
  "sources": [
    {"title": "Aleph-Alpha/Kolibri-1（モデルカード）", "publisher": "Hugging Face（Aleph Alpha）", "url": "https://huggingface.co/Aleph-Alpha/Kolibri-1", "kind": "公式ドキュメント"},
    {"title": "Kolibri Has Landed: A Sovereign Open-Weight Model", "publisher": "Aleph Alpha", "url": "https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/", "kind": "公式発表"},
    {"title": "Aleph Alpha の投稿", "publisher": "X @Aleph__Alpha", "url": "https://x.com/Aleph__Alpha/status/2106306840657297814", "kind": "X投稿"},
    {"title": "Kolibri Has Landed: A Sovereign Open-Weight Model", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=49942706", "kind": "コミュニティ"},
    {"title": "Aleph-Alpha/Kolibri-1 · Hugging Face - 78B parameters. 3.46B active.", "publisher": "Reddit r/LocalLLaMA", "url": "https://www.reddit.com/r/LocalLLaMA/comments/1wwl7y6/alephalphakolibri1_hugging_face_78b_parameters/", "kind": "コミュニティ"},
    {"title": "Aleph Alpha launches Kolibri, a sovereign German AI model for government use", "publisher": "Startup Fortune", "url": "https://startupfortune.com/aleph-alpha-launches-kolibri-a-sovereign-german-ai-model-for-government-use/", "kind": "報道"}
  ],
  "thumb_text": "Kolibri-1",
  "share_text": "独Aleph AlphaがKolibri-1を公開。78Bのうち稼働3.46B、独英特化でApache 2.0",
  "editor_note": ""
}
---
ドイツのAI企業Aleph Alphaは現地時間10月3日、ドイツ語と英語に特化したオープンウェイトのモデル「Kolibri-1」を公開しました。総パラメータは78B（780億）ですが、1トークンの処理で動くのは3.46Bだけで、重みはApache 2.0ライセンスでHugging Faceから入手できます。公開日はドイツ統一の日に合わせたと同社は説明しています。

## 何が公開されたか

Kolibri-1とは、Aleph Alphaが政府・産業向けに作った推論（リーズニング）対応の言語モデルです。MoE（Mixture-of-Experts。質問ごとに一部の「専門家」層だけを動かす構造）を採用し、1層あたり384の専門家から共有1つと選択6つを使います。思考の深さを `none` から `high` まで切り替える推論モードと、ツール呼び出しに対応しています。

モデルカードで確認できた主な仕様は次のとおりです。

| 項目 | Kolibri-1 |
|---|---|
| パラメータ | 総78.1B／稼働3.46B |
| 対応言語 | ドイツ語・英語 |
| 文脈長 | 学習時26万2,144トークン、検証済みの上限104万8,576トークン |
| 必要なGPU（最小） | A100 80GB×2、H100 SXM5×2、H200×1、B200×1 など |
| 重みのメモリ | 約78GB（FP8） |
| 知識の締め日 | 2026年6月18日 |
| ライセンス | Apache 2.0 |

学習データは20兆トークンで、内訳は英語約62.5%、ドイツ語約23.9%、コード約13.6%です。事前学習にはNVIDIA B200を768基使い、21日かかったとしています。動かすにはvLLM用のプラグイン `aleph-alpha-inference` が必要で、OpenAI互換のAPIとして社内から呼び出せます。

{{card:https://huggingface.co/Aleph-Alpha/Kolibri-1|Aleph-Alpha/Kolibri-1|Hugging Face}}

性能について、同社は公式ブログで稼働パラメータが自社の4倍ある他社モデルと肩を並べると主張しています。

:::quote https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/ | Aleph Alpha公式ブログ「Kolibri Has Landed」
> Across math, coding, grounding, and long-context tasks, Kolibri matches models with up to four times its active parameter count, such as Nemotron 3 Super.
数学・コーディング・根拠付け・長文脈の各タスクで、Kolibriは稼働パラメータが最大4倍あるNemotron 3 Superのようなモデルに並ぶ。
:::

モデルカードの総合スコア（追加学習後）を抜き出すと、英語で75.5、ドイツ語で70.8でした。同じ表のQwen3.5 35B-A3Bは英語74.7・ドイツ語69.8、GPT-OSS 120Bは72.3・70.2、Nemotron 3 Super 120B-A12Bは73.0・67.9です。ただしこれはAleph Alpha自身の測定で、同じ表で参考値として灰色表示されたQwen3.8 27B（密なモデル）は英語80.2と上回っています。ツール呼び出しのBFCL v4ではQwen3.5 35B-A3Bの70.5に対しKolibri-1は61.4で、得意・不得意ははっきり分かれます。

## 背景

Aleph Alphaは「ソブリン（主権）AI」を掲げるドイツの会社です。今回もドイツで開発し、ドイツとフィンランドの計算基盤で学習したと説明しています。EUのAI法、汎用AIの行動規範、GDPRを設計段階から意識したとも書き、同社はEUの行動規範（Code of Practice）の署名企業です。

公式ブログによると、Kolibri-1の前に総30B・稼働3Bで文脈6.5万トークンの「Kolibri Origin」を作り、学習の仕組みを検証しました。一方でモデルカードは、自動で動かし続ける用途ではなく、人が出力を確認してから使う業務支援を想定すると明記しています。文書処理、社内資料への質問応答、調査ツールが主な用途です。

同社のサイトでは、最高責任者の交代（Reto Spörri氏の退任とIlhan Scheer氏のCEO継続）と、カナダのCohereとの「大西洋をまたぐソブリンAI」の提携も告知されています。米中の大手モデルに頼らない選択肢を欧州の公共機関や製造業に示す狙いが読み取れます。

## 反応と論点

Aleph Alphaは公式Xで「重みはあなたのもの。自分のハードウェアで動かせる」と呼びかけました。

{{x:https://x.com/Aleph__Alpha/status/2106306840657297814}}

r/LocalLLaMAでは、公開から間もなく「78Bで稼働3.46B、最大100万トークン、Apache 2.0」という仕様の組み合わせが話題になりました。Hacker Newsでは、稼働3Bで本来は安い機材でも速く回せる設計なのに、推奨構成が4ビットや8ビットの量子化を前提にせず高価なGPUを挙げている点を指摘する声がありました。

論点は2つあります。1つは、稼働パラメータは小さくても78B分の重みをすべてメモリに載せる必要があることです。モデルカード自身が「代償はメモリ」と認めています。もう1つは対応言語の狭さで、同社は2言語に絞ったのは「広さより深さ」を選んだ意図的な判断だと説明しています。

## 日本のビジネスへの影響

- **使えるか**: 重みは誰でもダウンロードでき、Apache 2.0なので商用利用も可能です。ただし対応言語はドイツ語と英語だけで、日本語は学習の対象に入っていません。日本語の業務文書にそのまま使うのは避けるべきです。
- **誰にどう効くか**: 社内GPUでLLMを動かす開発者・情報システム部門には、「H200が1枚あれば100万トークン級のMoEを社外に出さず動かせる」という比較材料になります。ドイツや英語圏の取引先との契約書・技術文書を扱う製造業や商社の現地法人には、独英の文書処理に絞った候補になります。
- **今すぐやれること**: 欧州拠点で英語・ドイツ語の文書を扱っているなら、vLLMの検証環境で英文の社内文書を使い、いま使っているQwen系やGPT-OSSと回答の質と速度を比べてみてください。日本語中心なら、ローカルで動かすモデルの選び方は[ローカルLLMのガイド](/best/local-llm/)を参照してください。
- **注意点**: 性能の数字はすべてAleph Alphaの自己申告です。量子化版の公式提供はなく、最小構成でも80GB級のGPUが2枚要るため、手元のPCやMacで試せる規模ではありません。
