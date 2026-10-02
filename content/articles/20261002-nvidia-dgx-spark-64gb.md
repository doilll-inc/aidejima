---
{
  "title": "NVIDIAがDGX Sparkの64GB版を10月23日発売、2台つなぎで200Bモデルも",
  "description": "NVIDIAが机上のAI用小型機DGX Sparkに、メモリ64GBの構成を追加した。10月23日にAcerやDellなど6社から$4,999で発売し、2台をつなげば最大2000億パラメータのモデルを動かせる。",
  "date": "2026-10-02T23:42:00+09:00",
  "category": "hardware",
  "tags": ["NVIDIA", "DGX Spark", "ローカルLLM", "半導体", "エージェント"],
  "summary": [
    "NVIDIAは現地時間10月2日、小型AIマシンDGX Sparkのメモリ64GB版を10月23日に$4,999から発売すると発表した",
    "DGX Spark 64GB版は1台で最大1000億パラメータ、2台をつなぐと最大2000億パラメータのモデルを動かせる",
    "DGX Sparkの128GB版は発売時$3,999だったと報じられており、64GB版はメモリが半分でも価格は上回る"
  ],
  "sources": [
    {"title": "NVIDIA DGX Spark 64GB Gives Developers More Ways to Build and Scale Local AI", "publisher": "NVIDIA Blog", "url": "https://blogs.nvidia.com/blog/local-ai-dgx-spark-64gb-sync/", "kind": "公式発表"},
    {"title": "NVIDIA DGX Spark", "publisher": "NVIDIA", "url": "https://www.nvidia.com/en-us/products/workstations/dgx-spark/", "kind": "公式サイト"},
    {"title": "DGX Spark: NVIDIA's new mini supercomputer model has half the memory but still the same price", "publisher": "Aroged", "url": "https://www.aroged.com/2026/10/02/dgx-spark-nvidias-new-mini-supercomputer-model-has-half-the-memory-but-still-the-same-price/", "kind": "報道"},
    {"title": "NVIDIA DGX Spark 64GB: The Scale-Out Bet", "publisher": "FourWeekMBA", "url": "https://fourweekmba.com/ai-nvidia-dgx-spark-64gb-scale-out/", "kind": "報道"}
  ],
  "thumb_text": "DGX Spark 64GB",
  "share_text": "NVIDIAがDGX Sparkの64GB版を10月23日に$4,999で発売。2台つなぐと200Bモデルまで",
  "editor_note": ""
}
---
NVIDIAは現地時間10月2日、机の上に置ける小型のAI用コンピューター「DGX Spark」に、メモリを64GBにした構成を追加すると発表しました。10月23日（金）にAcer、ASUS、Dell、Gigabyte、HP、MSIの6社から、$4,999からの価格で発売します。1台で最大1000億パラメータのモデルを動かせ、2台をつなげば最大2000億パラメータまで広がります。

## 何が発表されたか

DGX Sparkとは、NVIDIAのGB10 Grace Blackwellチップと、CPUとGPUが共有する「ユニファイドメモリ」を15cm角の筐体に収めた、開発者向けの小型AIマシンです。これまでの構成はメモリ128GBでした。今回の64GB版は、チップ・専用OS（DGX OS）・ソフトウェア一式は128GB版と同じで、メモリだけを半分にしています。NVIDIAからの直販はなく、メーカー各社だけが売ります。

:::quote https://blogs.nvidia.com/blog/local-ai-dgx-spark-64gb-sync/ | NVIDIA Blog「NVIDIA DGX Spark 64GB Gives Developers More Ways to Build and Scale Local AI」
> The new 64GB configuration, available exclusively from manufacturer partners, keeps the platform at an accessible price point while retaining the GB10 Grace Blackwell Superchip, DGX OS and full NVIDIA AI software stack — same as the 128GB model.
新しい64GB構成はメーカー各社だけが販売し、手の届く価格を保ちながら、GB10 Grace Blackwellチップ、DGX OS、NVIDIAのAIソフトウェア一式を128GBモデルと同じく備えています。
:::

| 項目 | DGX Spark 64GB版 |
|---|---|
| 発売日・価格 | 10月23日、$4,999から |
| 販売元 | Acer、ASUS、Dell、Gigabyte、HP、MSI |
| 1台で動かせるモデル | 最大1000億パラメータ |
| 2台接続時 | メモリ計128GB、最大2000億パラメータ、1台比で最大1.7倍の性能 |
| 標準で使えるソフト | NVIDIA Agent Toolkit、Nemotron、Ollama、vLLM、PyTorch など |

### 2台をつなぐ「Sync Cluster Assistant」

発表のもう1つの柱が、複数台をつなぐ設定を自動化するソフトです。DGX Sparkには最初から200Gbpsのネットワークカード（ConnectX-7）が載っており、2台をケーブル1本で直結できます。管理アプリ「NVIDIA Sync」のCluster Assistantが、つながった機体を見つけてネットワークを設定します。NVIDIAの試験では、Qwen 3.8 27Bを2台で動かすと1台の最大1.7倍の性能が出たといいます。

10月末には「Sync Model Launcher」も出ます。数回のクリックでQwen3.8 27Bをダウンロードして起動し、手元のノートPCから使えるようにするものです。コーディング用のOpenCodeもこのモデルを使うよう設定され、ブラウザからすぐ書き始められるとしています。

{{card:https://www.nvidia.com/en-us/products/workstations/dgx-spark/|NVIDIA DGX Spark|NVIDIA}}

## 背景

NVIDIAがこの構成を出す背景には、AI向けメモリの値上がりがあります。メモリ大手Micronは前日、AI需要でメモリが足りず値上げが続いていると決算で示しました（[Micronの決算の記事](/news/20261001-micron-q4-fy2026-hbm-ai-memory/)）。Arogedは、DGX Sparkは発売時に$3,999で売られていたが、その後$4,699、$4,999と値上がりしたと報じています。FourWeekMBAも、64GB版の$4,999は128GB版の当初価格より$1,000高いと指摘しています。

一方で、手元で動かせるモデルの性能は上がり続けています。64GBのMacで大型のQwenを動かすOSSも話題になったばかりです（[Slipstreamの記事](/news/20261002-slipstream-qwen38-flash-next-64gb-mac/)）。NVIDIAは「大きいメモリを1台で買う」より「必要な分から始めて、足りなくなったら台数を足す」使い方を勧める方向に、売り方を切り替えた形です。

## 反応と論点

メモリが半分になったのに価格は当初の128GB版を上回るため、報道の見出しはそろって価格に注目しています。発表文が「手の届く価格」をうたう一方で、実際の店頭価格はメーカーごとの構成で決まり、$4,999は最低価格にすぎない点も指摘されています。

NVIDIAが示した1.7倍という数字は、自社の1モデルでの試験結果です。メモリ帯域は1台あたり273GB/s（公式の仕様）で、大きなモデルを動かすときは帯域が速度の上限を決めます。2台構成の効果がほかのモデルや長い文脈でどこまで出るかは、第三者の測定を待つ必要があります。

## 日本のビジネスへの影響

- **使えるか**: 現時点で、64GB版の日本での発売時期や円の価格は発表されていません。NVIDIAの発表は米国での$4,999という価格だけで、国内では販売元各社の案内を待つことになります
- **誰にどう効くか**: 社内データを外に出さずにAIを試したい**開発者・情報システム部門**に関係します。顧客情報や設計資料を扱うエージェントを、クラウドに送らず社内の1台で常時動かす検証機として使えます
- **今すぐやれること**: 社内で使いたいモデルが64GBに収まるかを先に確かめます。Qwen3.8 27Bクラスなら1台に収まりますが、それより大きなモデルを使うなら、最初から128GB版か2台構成で見積もるほうが安く済む場合があります
- **注意点**: 64GB版を2台そろえると最低でも$9,998で、128GB版1台より高くつく可能性があります。接続ケーブルと設置場所も要ります。「小さく始めて足す」は、メモリ価格が下がらない限り割高になりやすい点を織り込んでおきます

手元のPCで動かすモデルとアプリの選び方は、[ローカルLLMのガイド](/best/local-llm/)にまとめています。
