---
{
  "title": "Metaの新AIが手元のMac 2台で動く、Appleと組んで中身を無料公開",
  "description": "Metaが10月15日、AIモデル「Muse Spark Open」の中身を無料で公開した。AppleのMac Studio 2台で動くよう最適化され、外部のサーバーを使わず社内で動かせる。総パラメーター数は8,160億で、米国製の公開モデルとしては最高性能だとしている。",
  "date": "2026-10-16T17:40:00+09:00",
  "category": "models",
  "tags": ["Meta", "Muse Spark Open", "Muse", "Apple", "オープンウェイト", "ローカルLLM"],
  "summary": [
    "Metaは10月15日、AIモデル「Muse Spark Open」の中身を公開し、誰でも自分の機械で動かせるようにした",
    "Appleと組み、高性能なデスクトップ機Mac Studio 2台で動くよう調整した。必要なメモリーは約1TBと報じられている",
    "商用利用もできるが、製品に「Built with Muse Spark Open」と表示する決まりがあり、日本語の性能は公表されていない"
  ],
  "sources": [
    {"title": "Muse-Spark-Open-816B-A42B（モデルカード）", "publisher": "Hugging Face / Meta Superintelligence Labs", "url": "https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B", "kind": "公式ドキュメント"},
    {"title": "Muse Spark Open（モデル一覧）", "publisher": "Hugging Face / Meta Superintelligence Labs", "url": "https://huggingface.co/collections/meta-models/muse-spark-open", "kind": "公式ドキュメント"},
    {"title": "Mark Zuckerberg の投稿", "publisher": "X @finkd", "url": "https://x.com/finkd/status/2110778025629347999", "kind": "X投稿"},
    {"title": "Meta's Muse Spark Open now available in Amazon SageMaker JumpStart", "publisher": "AWS Machine Learning Blog", "url": "https://aws.amazon.com/blogs/machine-learning/metas-muse-spark-open-now-available-in-amazon-sagemaker-jumpstart/", "kind": "公式発表"},
    {"title": "Meta built a huge open-weight AI model for Macs, but you'll need 1TB of RAM to run it", "publisher": "Engadget", "url": "https://www.engadget.com/2287833/meta-built-a-huge-open-weight-ai-model-for-macs-but-youll-need-1tb-of-ram-to-run-it/", "kind": "報道"},
    {"title": "Meta launches an open-weight AI model that runs on Macs", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/10/15/meta-launches-an-open-weight-model-that-runs-on-macs/", "kind": "報道"}
  ],
  "thumb_prompt": "Two compact aluminum desktop computers stacked on an ordinary office desk next to a potted plant, with a glowing thread of light connecting them to a tiny model of a huge data center that fits in the palm of an anonymous hand.",
  "thumb_style": "diorama",
  "thumb_text": "Muse Spark Open",
  "share_text": "Metaが新AI「Muse Spark Open」の中身を無料公開。AppleのMac Studio 2台で動き、社外にデータを出さずに使える",
  "editor_note": ""
}
---
Metaは現地時間10月15日、AIモデル「Muse Spark Open」の中身（学習済みの重み）を無料で公開しました。Appleと協力して、デスクトップ機のMac Studio 2台で動くように調整してあり、クラウドに頼らず手元の機械だけで大型のAIを動かせます。

## 何が発表されたか

Muse Spark Openとは、Metaの研究組織Meta Superintelligence Labsが作った、プログラミングや複数の手順をこなす仕事（エージェント）向けのAIモデルです。中身が公開されている「オープンウェイト」と呼ばれる形式で、AIの共有サイトHugging Faceから入手できます。文章・画像・動画・音声を読み取り、文章で答えます。

:::quote https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B | Hugging Face「Muse-Spark-Open-816B-A42B」モデルカード（Meta Superintelligence Labs）
> Muse Spark Open is an 816B total/42B active parameter open weights model with a context window of 1M tokens.
Muse Spark Openは、総パラメーター数8,160億・1回の処理で使うのは420億のオープンウェイトモデルで、一度に100万トークンを読み込める。
:::

パラメーターはAIの規模を表す数で、8,160億は公開モデルの中でも最大級です。ただ、質問ごとに働くのはその一部だけなので、規模の割に速く動く仕組みになっています。トークンはAIが文章を細かく区切って数える単位で、100万トークンあれば長い契約書や報告書を何本もまとめて読み込めます。

Metaのザッカーバーグ最高経営責任者（CEO）はXで、AppleのJohn Ternus氏らと協力した結果、新しいMac Studioでよく動くと投稿しました。

{{x:https://x.com/finkd/status/2110778025629347999}}

モデルカードにも、Appleの機械学習の仕組み「MLX」を使い、最上位チップM5 Ultraを積んだMac Studio 2台で動くよう最適化したと書かれています。

:::quote https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B | Hugging Face「Muse-Spark-Open-816B-A42B」モデルカード（Meta Superintelligence Labs）
> It is also optimized to run on two Mac Studios with M5 Ultra using MLX.
MLXを使い、M5 Ultraを搭載したMac Studio 2台で動くようにも最適化されている。
:::

## 動かすのに何が必要か

手元で動かすハードルは低くありません。米Engadgetは、動かすにはメモリーが約1TB必要で、メモリー512GBのMac Studioを2台つなぐか、256GBの機種を4台（合計約3万8,000ドル）使う形になると報じています。512GBの機種は10月下旬に出る予定で、価格はまだ発表されていないとしています。

データを小さく圧縮した版でも、モデルカードでは700GB以上のメモリーが必要とされています。社内に置くなら「パソコン1台」ではなく「小さなサーバー室1つ分」の投資と考えたほうが実態に近いです。

自前で用意しない方法もあります。Amazonのクラウドは同じ日に、企業向けのAI基盤「SageMaker JumpStart」で提供を始めました。開始時点で使えるのは米国東部の2地域だけです。

## 性能と利用条件

Metaはこのモデルを米国製のオープンウェイトモデルで最も高性能だとしています。モデルカードの比較表を見ると、外部のツールを使いこなす試験（MCP-Atlas）では比較した8モデルの中で最高の89.2点でした。

一方、第三者の評価サイトArtificial Analysisの総合指数は39点で、中国の「GLM 5.3」（45点）や「Kimi K3」（44点）を下回ります。「米国製で最高」と「公開モデル全体で最高」は別の話です。

利用条件（Muse Model License）は、改変や商用利用を広く認めています。ただし、使った製品や資料に「Built with Muse Spark Open」と目立つように表示する義務があります。また、このモデルを他社向けのサービスとして提供し、直近12カ月の売上高が2,000万ドルを超える場合は、Metaに知らせて別の契約を結ぶ必要があります。社内利用や研究、自社製品への組み込みはこの対象外です。18歳未満の利用は想定していません。

## 背景

Metaは10月12日に、より高性能な非公開のモデル「Muse Wonder」を出したばかりです（[Metaが新AI「Muse Wonder」を公開](/news/20261013-meta-muse-wonder-frontier-models/)）。最上位は自社のサービスで有料提供し、一段下のモデルは中身ごと配って開発者や企業を取り込む、という二段構えです。

公開モデルの分野では、今回の比較表でも総合指数の上位を中国勢が占めています。米国勢ではNVIDIAや米Reflection AIも公開モデルを出しており（[NVIDIAがReflection AIの買収を協議と報道](/news/20261011-nvidia-reflection-ai-acquisition-talks/)）、Metaは「動かす場所」をAppleのMacにも広げることで差をつけようとしています。

## 日本のビジネスへの影響

- **使えるか**: Hugging Faceからは日本でも入手できます。学習には100以上の言語のデータを使ったとされますが、日本語の性能は公表されていません。日本語で使うなら、自社の文書で試してから判断する必要があります
- **誰に効くか**: 顧客情報や設計図など、外部のAIサービスに送れないデータを扱う企業の情報システム部門や経営者です。データを社外に出さずに大型のAIを動かす選択肢が、Mac数台という形で現実的になりました
- **今すぐやれること**: すぐに機械を買う必要はありません。まずは手元の機械で動く小型の公開モデルで、社内文書の要約や検索がどこまでできるかを試しておくと、Muse Spark Openに切り替える価値があるかを判断しやすくなります。選び方は[ローカルLLMの用途別ガイド](/best/local-llm/)にまとめています
- **注意点**: 報道どおりなら、必要な機材は約3万8,000ドル規模になります。「Built with Muse Spark Open」の表示義務や、売上高による契約の条件もあるため、自社サービスに組み込む前に法務部門と利用条件を確認してください
