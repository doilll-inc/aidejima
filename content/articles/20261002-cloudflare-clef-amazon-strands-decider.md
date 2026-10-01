---
{
  "title": "Cloudflareが判断モデル「Clef」を公開、Jev互換で画像も判定しAmazonも2B版",
  "description": "Cloudflareは10月1日、AIエージェントの分岐を確率付きで決める判断モデル「Clef」と軽量版を公開した。Jevと同じAPIで呼べ、軽量版の応答の中央値は38.8ミリ秒。同日にAmazonも2Bの「Strands Decider」を公開している。",
  "date": "2026-10-02T03:40:00+09:00",
  "category": "dev",
  "tags": ["Cloudflare", "Clef", "Strands Decider", "オープンウェイト", "エージェント", "API"],
  "summary": [
    "Cloudflareは判断モデルClefとClef-flashを公開し、Workers AIで提供、重みもApache 2.0でHugging Faceに置いた",
    "ClefはJevと同じAPIで呼べ、画像の判定と64kの文脈に対応する。料金は入力100万トークンあたり0.24ドル",
    "AWSのStrands Labsも同日に2Bの判断モデルStrands Decider 2Bを公開し、学習データとスクリプトまで出した"
  ],
  "sources": [
    {"title": "Introducing Clef: our open-source decision models, and new RL fine-tuning platform", "publisher": "Cloudflare Blog", "url": "https://blog.cloudflare.com/clef-decision-models/", "kind": "公式発表"},
    {"title": "clef（Workers AI models）", "publisher": "Cloudflare Docs", "url": "https://developers.cloudflare.com/workers-ai/models/clef/", "kind": "公式ドキュメント"},
    {"title": "Pricing（Workers AI）", "publisher": "Cloudflare Docs", "url": "https://developers.cloudflare.com/workers-ai/platform/pricing/", "kind": "公式ドキュメント"},
    {"title": "Introducing Strands Decider 2B: a small, open source, decision model", "publisher": "Strands Agents Blog（AWS）", "url": "https://strandsagents.com/blog/introducing-strands-decider/", "kind": "公式発表"},
    {"title": "Introducing System One Models & Jev", "publisher": "TypeSafe AI", "url": "https://typesafe.ai/blog/introducing-system-one-models-and-jev", "kind": "公式発表"},
    {"title": "michelle（Cloudflare）の投稿", "publisher": "X @michellechen", "url": "https://x.com/michellechen/status/2101091012559151480", "kind": "X投稿"},
    {"title": "Amazon releases its own Jev clone as decision models flood the web", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/10/01/amazon-releases-its-own-jev-clone-as-decision-models-flood-the-web/", "kind": "報道"}
  ],
  "thumb_text": "Clef",
  "share_text": "Cloudflareが判断モデルClefを公開。Jev互換で画像も判定、軽量版は中央値38.8ミリ秒。Amazonも2B版を公開",
  "editor_note": ""
}
---
Cloudflareは現地時間10月1日、AIエージェントが「次にどうするか」を確率付きで決める判断モデル「Clef」と軽量版「Clef-flash」を公開しました。TypeSafe AIの「Jev」と同じAPIで呼べ、軽量版の応答時間の中央値は38.8ミリ秒と、Jevの524.1ミリ秒の約13分の1です。同じ日にはAWSのStrands Labsも2B（20億パラメーター）の判断モデル「Strands Decider 2B」を公開し、9月に始まった判断モデルの競争に大手クラウドが2社そろって加わりました。

## 何が発表されたか

判断モデルとは、状況の説明と選択肢を受け取り、選択肢ごとの確率を返すAIモデルです。文章は生成しません。「この問い合わせは緊急か」「どのチームに回すか」「影響は4段階のどれか」といった問いに、決まった形の答えを返します。プログラムの分岐にそのまま使えるのが特徴で、Jevが話題を集めた経緯は[JeffとJeevesの記事](/news/20261001-jeff-jeeves-open-decision-models/)で紹介しました。

:::quote https://blog.cloudflare.com/clef-decision-models/ | Cloudflare公式ブログ「Introducing Clef」
> A decision model makes classifications to help agents decide how to act, based on certain probabilities.
判断モデルは分類を行い、確率に基づいてエージェントがどう動くかを決める手助けをします。
:::

Clefは、Cloudflare Workers AIのチームが初めて自社で学習させたモデルです。土台はAlibabaのQwenで、ClefはQwen3.8-27B、Clef-flashはQwen3.5-9Bを固定したまま、判断用の部品と追加の小さな重み（LoRA）だけを学習しました。答えを1語ずつ生成せず、選択肢を並行して採点する仕組みのため速く動きます。

Jevとの違いとして、Cloudflareは3点を挙げています。

- **画像を判定できる**：画像を読み込む部品を備え、1回に4枚まで画像を渡せる。Jevは現時点で文章だけ
- **長い入力**：文脈は65,536トークン（64k）で、Jevの32kの2倍
- **同じAPI**：JevのAPI（System One API）と互換で、呼び出し先を替えるだけで試せる

提供はWorkers AIでの従量課金と、Hugging Faceでの重みの公開（Apache 2.0ライセンス）の両方です。Workers AIの料金は、Clefが入力100万トークンあたり0.24ドル、Clef-flashが0.09ドルで、出力の料金は表にありません。TypeSafeが公表するJevの料金は入力0.042ドル（出力は無料）なので、単価ではClefが約6倍、Clef-flashが約2倍です。

{{card:https://developers.cloudflare.com/workers-ai/models/clef/|clef（Workers AI models）|Cloudflare Docs}}

## 性能の数字

Cloudflareが公表した比較では、ツール呼び出しの正確さを測るBFCLでClefが98.47、Clef-flashが98.76、Jevが95.75でした。銀行の問い合わせ分類（BANKING77）はClefが94.20、Jevが79.74です。一方、ツールを呼ぶべきかの判断（When2Call）は、Jevの80.97に対してClefは72.37にとどまりました。全10項目で常に勝つわけではありません。

社内では、脅威情報チームがWebサイトの分類にClefを使い、取得から判定まで2.2秒でした。汎用LLMのgpt-oss-120bでは4.7秒かかったといいます。

あわせて、Clefを自社の用途向けに鍛え直す強化学習（RL）の調整サービスも始めました。まずはCloudflareの技術者が伴走する形で提供し、後から自分で再学習できる仕組みを出す予定です。料金と開始時期は書かれていません。

## AmazonのStrands Decider 2B

AWSのStrands Labsが同日公開したStrands Decider 2Bは、Qwen3.5-2Bをもとにした小型の判断モデルです。文章を生成する最後の層を外し、選択肢を採点する100万パラメーター強の部品に置き換えています。GitHubでコードと重みに加え、学習に使ったデータとスクリプトまで公開しました。

:::quote https://strandsagents.com/blog/introducing-strands-decider/ | Strands Agents公式ブログ「Introducing Strands Decider 2B」
> It’s a 2 billion parameter model, suitable for running on a local CPU or GPU, which can return answers to meaningful questions in tens of milliseconds.
20億パラメーターのモデルで、手元のCPUやGPUで動かせ、意味のある問いに数十ミリ秒で答えを返せます。
:::

公表値では、JevBenchの公開問題の精度と確率の確かさを合わせた評価で、2B級33モデル中3位でした。応答時間の中央値はNVIDIA RTX 3090で約115ミリ秒です。AWSは、複雑な問題では推論モデルに大きく劣り、コーディングや要約には使えないと弱点も書いています。

## 背景

TechCrunchによると、Strands Deciderは、AmazonのディスティングイッシュトエンジニアのMarc Brooker氏が、9月のJev公開後に個人的に作った試作から始まりました。同紙は、TypeSafeのDiogo Almeida CEOが、続々と出る模倣モデルを「ML技術者が面白い構造を試したいだけ」と評したことも伝えています。

Cloudflareにとっては、9月中旬からの流れの続きです。CloudflareのMichelle Chen氏はJevの公開直後、公開モデルとトークンの確率を使ってJevを再現する試みをXで紹介していました。今回のClefはその発展版にあたります。

{{x:https://x.com/michellechen/status/2101091012559151480}}

## 反応と論点

利点は、毎回LLMに考えさせるほどではない分岐を任せ、待ち時間と費用を減らせることです。AWSも、モデルの振り分けやツールの選択、ガードレール（安全のための入出力チェック）で使われ始めていると書いています。

懸念は、比較の数字がどれも開発元の公表値で、載せる項目も開発元が選んでいることです。速さと画像対応の代わりに、入力単価がJevより高い点も見ておく必要があります。

## 日本のビジネスへの影響

- **使えるか**：ClefはWorkers AIの従量課金で使え、重みはApache 2.0なので商用でも自社サーバーで動かせます。Strands Deciderも重みが公開されており、手元のPCで試せます。日本語の精度は、どちらも公式には示されていません
- **誰に効くか**：問い合わせの振り分け、広告の審査前チェック、商品画像の分類などを自動化している開発者です。画像も判定できるClefは、EC事業者が商品画像の不備を見つける用途とも相性が良いはずです
- **今すぐやれること**：いまLLMに「はい/いいえ」や分類を答えさせている処理を1つ選び、日本語の過去データ100件ほどでClef-flashやStrands Deciderと正答率・応答時間・費用を比べてみてください
- **注意点**：When2Callのように苦手な項目もあり、難しい判断は推論モデルに残すのが前提です。確率が低いときは人に回す設計にしておくと安全です。オープンなモデルの選び方は[ローカルLLMのガイド](/best/local-llm/)にまとめています
