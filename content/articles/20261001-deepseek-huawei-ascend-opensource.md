---
{
  "title": "DeepSeekがHuawei Ascend向け基盤ソフトを公開、CUDA依存を外す動き",
  "description": "DeepSeekがHuaweiのAscend向けに、カーネル記述言語TileLangや通信ライブラリなど6点の基盤ソフトをオープンソース公開した。NVIDIA向けの既存部品と一対一で対応し、Huaweiも開発を全面支援した。",
  "date": "2026-10-01T16:05:00+09:00",
  "category": "hardware",
  "tags": ["DeepSeek", "TileLang", "Huawei", "半導体", "オープンソース", "中国AI"],
  "summary": [
    "DeepSeekがHuawei Ascend向けにTileLang・DeepGEMM・DeepEPなど6点の基盤ソフトをオープンソース公開した",
    "各部品はNVIDIA向けに公開済みのものと一対一で対応し、同じAPIのまま両方の環境で使える",
    "密行列演算はAscend 950DT上でハードウェア上限の最大99.8%に達したとDeepSeekは公表している"
  ],
  "sources": [
    {"title": "DeepGEMM Ascend", "publisher": "GitHub deepseek-ai", "url": "https://github.com/deepseek-ai/DeepGEMM-Ascend", "kind": "公式ドキュメント"},
    {"title": "DeepEP-Ascend", "publisher": "GitHub deepseek-ai", "url": "https://github.com/deepseek-ai/DeepEP-Ascend", "kind": "公式ドキュメント"},
    {"title": "TileLang", "publisher": "GitHub tile-ai", "url": "https://github.com/tile-ai/tilelang", "kind": "公式ドキュメント"},
    {"title": "开源面向华为昇腾算力平台的基础设施组件（DeepSeek公式WeChat）", "publisher": "DeepSeek", "url": "https://mp.weixin.qq.com/s/X41mKH4Ds-VXUAnK6M8Eww", "kind": "公式発表"},
    {"title": "China's AI industry closes ranks as Deepseek ships open-source software for Huawei's Ascend chips", "publisher": "The Decoder", "url": "https://the-decoder.com/chinas-ai-industry-closes-ranks-as-deepseek-ships-open-source-software-for-huaweis-ascend-chips/"},
    {"title": "DeepSeek Open-Sources Software Tools for Huawei AI Chips", "publisher": "The Information", "url": "https://www.theinformation.com/briefings/deepseek-open-sources-software-tools-huawei-ai-chips"}
  ],
  "thumb_text": "TileLang",
  "share_text": "DeepSeekがHuawei Ascend向けの基盤ソフト6点をオープンソース公開。NVIDIA向けと一対一対応",
  "editor_note": ""
}
---
DeepSeekは現地時間9月30日、HuaweiのAIチップ「Ascend」向けの基盤ソフトをまとめてオープンソース公開しました。NVIDIA向けに同社が公開してきた部品と一対一で対応する構成で、中核はカーネル記述言語のTileLangです。

## 何が公開されたか

公開されたのは6点です。TileLangのAscend版に加え、行列演算のDeepGEMM-Ascend、分散通信のDeepEP-Ascend、ベクトル演算とメモリアクセスのTileKernels、疎なアテンションのFlashMLA、上位k件の選択を担うDeepSelectが同時に出ました。DeepSeekは公式WeChatで、各部品がNVIDIA向けの既存の公開物と一対一で対応すると説明しています。

カーネルとは、GPUやNPUの上で実際に計算を回す小さなプログラムのことです。モデルの性能はここの書き方で大きく変わります。

:::quote https://github.com/deepseek-ai/DeepGEMM-Ascend | DeepSeek公式リポジトリ「DeepGEMM Ascend」README
> DeepGEMM Ascend is a port of DeepGEMM to the HUAWEI Ascend platform. It is fully API-compatible with DeepGEMM and supports BF16, FP8, FP4 GEMM, MQA logits, and MegaMoE.
DeepGEMM AscendはDeepGEMMをHUAWEI Ascendプラットフォームへ移したものです。DeepGEMMと完全にAPI互換で、BF16・FP8・FP4のGEMM、MQAロジット、MegaMoEに対応します。
:::

API互換という点が実務上の肝です。同じ関数呼び出しのまま、NVIDIAとAscendのどちらでも同じ開発手順を使えます。性能についてDeepSeekは、Ascend 950DTとCANN 9.20の環境で、密な行列演算がハードウェア上限の最大99.8%に達したとリポジトリで公表しています。通信ライブラリ側は、専門家並列8構成でdispatchが毎秒373〜375GBとされています。

中核のTileLangは、もともと北京大学の研究者が作った言語で、DeepSeekは約1年前から使ってきました。NVIDIAの成熟した環境で先に検証し、いまはV4系モデルの学習で大半の演算子実装を担っているとしています。DeepSeekは、CUDAに比べて記述が簡単で開発効率が上がる一方、チップの特性を引き出して性能上限まで到達できる点を利点に挙げています。

:::quote https://github.com/tile-ai/tilelang | TileLang公式リポジトリ README「Latest News」
> TileLang now officially supports Huawei Ascend 950 NPUs with native code generation, automatic scheduling and synchronization, SIMD/SIMT vector programming, etc.
TileLangはHuawei Ascend 950 NPUを正式にサポートしました。ネイティブのコード生成、自動スケジューリングと同期、SIMD/SIMTのベクトルプログラミングなどに対応します。
:::

## 背景

NVIDIAの強さはチップ設計だけでなく、CUDAという開発環境と、そこに積み上がった開発者の数にあります。中国の国産チップが伸び悩んできた理由も、ハードよりソフトにあるとされてきました。今回の動きは、そのソフト側を自前で埋めにいくものです。モデルの性能面では、[中国GLM-5.3の評価](/news/20260930-anthropic-glm-5-3-cyber-capabilities/)のように国外からも実力が認められる例が出てきており、残る差が基盤ソフトに集中していました。

DeepSeekによると、Huaweiは開発を全面的に支援し、Ascend 950を128枚束ねた「スーパーノード」の構成や、計算と通信の最適化を両社で共同で進めました。The Decoderは、Huaweiが2週間前に新しいAIプロセッサとスーパーノード製品を公表していたと伝え、今回の公開を中国AI業界が結束する動きと位置づけています。The Informationも同日、DeepSeekがHuawei向けのソフトをオープンソース化したと報じました。

## 論点

ただし、公開された資料は現時点の限界も率直に書いています。DeepEP-Ascendの計測値は、DeepSeekに提供された検証用のハードウェア構成で取ったもので、一般に配布されている版ではありません。同リポジトリは、Huaweiが10月中旬に公開を予定するAtlas 850E向けの商用リリースを、公開環境での基準にするよう勧めています。つまり、同じ数字をすぐ再現できる組織はまだ限られます。

機能面でも、パイプライン並列やバケット集合通信は実験段階と明記されています。「NVIDIAの代替が完成した」という段階ではなく、代替を作るための足場が公開された、という読み方が正確です。

## 日本のビジネスへの影響

ソースコードはGitHubで公開されており、多くがMITライセンスです。日本からも読めますし、TileLang自体はNVIDIAやAMDのGPU、CPUにも対応しているため、Ascendを持っていなくても試せます。一方で、今回のAscend版を動かすにはAscend 950のNPUとCANNの環境が要るため、日本国内で実機検証に進める企業はごく一部です。

関係が深いのは、推論基盤を自前で持ち、カーネルをCUDAで直接書いている開発チームです。TileLangのような中間言語を挟んでおくと、将来チップを替えるときの書き直しが減ります。調達の観点では、NVIDIA以外の選択肢が増えるほど価格交渉の材料になりますが、今回の成果がそのまま日本の調達環境に効くわけではありません。

今すぐやれることがあるとすれば、自社のカーネル資産がどれだけCUDAに固定されているかを棚卸しすることです。注意点は輸出管理と調達方針で、中国製チップ向けの最適化を前提にした構成は、取引先の要求によっては採れません。自前でモデルを動かす選択肢の全体像は[ローカルLLM・オープンウェイトモデルのおすすめ](/best/local-llm/)で整理しています。
