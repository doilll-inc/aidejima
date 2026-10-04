---
{
  "title": "PULSAR-ASMは5KBの機械語でGemma-2Bを動かす推論エンジン、AIと組んでアセンブリで自作",
  "description": "個人開発者2人が、GoogleのGemma-2B-ITを5,268バイトのx86-64機械語だけで推論するPULSAR-ASMを公開した。普通のPCのCPUで毎秒4.0〜4.4トークン。開発にはAntigravityを相棒に使った。",
  "date": "2026-10-04T23:05:00+09:00",
  "category": "usecases",
  "tags": ["PULSAR-ASM", "Gemma", "Antigravity", "活用事例", "個人開発", "ローカルLLM"],
  "summary": [
    "PULSAR-ASMは、20億パラメーターのGemma-2B-ITをFP16のまま、5,268バイトのx86-64アセンブリ製の機械語でCPU推論するエンジン",
    "作者の計測では、DDR4-2666のデュアルチャネル機で毎秒4.04〜4.41トークンを出し、メモリ帯域18.5GB/sのほぼ上限まで使い切っている",
    "作者のKuo Ting TsaiとShin Rung Tsaiは、GoogleのAntigravityを「AIペアプログラマー」としてクレジットしている"
  ],
  "sources": [
    {"title": "tomtsai28/PULSAR-ASM（README）", "publisher": "GitHub tomtsai28", "url": "https://github.com/tomtsai28/PULSAR-ASM", "kind": "公式ドキュメント"},
    {"title": "PULSAR-ASM 工程復盤與技術檢討報告", "publisher": "GitHub tomtsai28", "url": "https://github.com/tomtsai28/PULSAR-ASM/blob/main/doc/pulsar_asm_cpu_limit_retrospective.md", "kind": "公式ドキュメント"},
    {"title": "[Discussion] A 5KB pure x86-64 assembly engine for Gemma-2B (FP16, 4.6 tok/s on CPU)", "publisher": "Reddit r/LocalLLaMA", "url": "https://www.reddit.com/r/LocalLLaMA/comments/1wx5x1p/discussion_a_5kb_pure_x8664_assembly_engine_for/", "kind": "コミュニティ"}
  ],
  "thumb_text": "PULSAR-ASM",
  "share_text": "5,268バイトの機械語だけでGemma-2Bを動かすPULSAR-ASM。開発者2人がAIと組んでアセンブリで書いた",
  "editor_note": ""
}
---
開発者のKuo Ting TsaiさんとShin Rung Tsaiさんが、GoogleのオープンモデルGemma-2B-ITを、わずか5,268バイトの機械語で動かす推論エンジン「PULSAR-ASM」をGitHubで公開しました。リポジトリは米国時間10月3日に作られ、10月4日にr/LocalLLaMAで紹介されています。普通のPCのCPUで毎秒4.0〜4.4トークンを出し、開発にはGoogle DeepMindの「Antigravity」をAIの相棒として使ったとクレジットしています。

## 何を作ったか

PULSAR-ASMとは、20億パラメーターのGemma-2B-ITを、FP16（16ビット浮動小数点）の元の精度のままCPUで推論する、x86-64アセンブリ製のエンジンです。リポジトリの説明文は次の2文です。

:::quote https://github.com/tomtsai28/PULSAR-ASM | tomtsai28「PULSAR-ASM」（GitHub）
> Pure x86-64 assembly LLM engine for Gemma-2B in 5KB flat machine code. Zero runtimes, memory-saturating AVX2+F16C execution.
5KBのフラットな機械語で書いた、Gemma-2B用の純粋なx86-64アセンブリのLLMエンジン。ランタイムなしで、メモリ帯域を使い切るAVX2とF16Cの命令で実行する。
:::

推論の中核は3,716バイトのエンジン本体と、1,552バイトの行列演算の部品で、合わせて5,268バイトです。Cの標準ライブラリにも外部のライブラリにも頼りません。一方、Hugging Faceから落とした重みの変換と、対話の画面はPythonのスクリプトが受け持ちます。つまり「5KB」は、計算の心臓部だけを指す数字です。

{{card:https://github.com/tomtsai28/PULSAR-ASM|tomtsai28/PULSAR-ASM|GitHub}}

## どう作ったか

READMEと技術報告によると、速さを稼ぐ工夫は4つです。

- **F16Cでの展開**: CPUに備わる命令で、FP16の重み8個を1命令でFP32に広げる。メモリから運ぶ量は半分のまま、計算は32ビットで行う
- **待たない並列処理**: OSのスケジューラーを使わず、4コアを待機させたまま共有の旗を見張らせる。作者の計測では起動の遅れは60ナノ秒未満
- **キャッシュを汚さない読み込み**: 4.67GBの重みを、キャッシュに残さない先読み命令で流し込み、計算途中の値を高速なキャッシュに残す
- **プロンプトのまとめ読み**: 入力文は複数コアで行列をまとめて計算し、毎秒6〜8トークンで読み込む

対応するのは、AVX2とF16Cの命令を持つIntelの第4世代Core（2013年のHaswell）以降と、AMDのRyzen全般です。OSはWindows 10・11の64ビット版で、メモリは8GB以上が条件です。アセンブリを書き換えたときは、同梱の117KBのアセンブラーFASMで0.1秒ほどで機械語を作り直せます。

作者は2人をアーキテクトとして記し、別枠で「AI Pair Programmer」としてGoogle DeepMindのAntigravityを挙げています。どこまでをAIが書いたのかの内訳は書かれていません。

## 成果（作者の公表値）

| 項目 | 作者の計測 |
|---|---|
| 生成速度（重みを削らない状態） | 毎秒4.04〜4.41トークン |
| メモリ帯域の使用 | 18.5GB/s（DDR4-2666デュアルチャネルの理論値の94%超） |
| メモリがシングルチャネルの場合 | 毎秒約2.2トークン |
| 一部の重みを削った実験 | 毎秒7.32トークン |

（出典：PULSAR-ASMのREADMEと技術報告）

面白いのは、作者自身が「これ以上は速くならない」と計算で示している点です。1トークンを作るたびに4.67GBの重みを全部読む必要があり、18.5GB/sで割ると1トークンあたり約0.25秒かかります。理論上の上限が毎秒3.96〜4.40トークンなので、コードはその95%以上に達しており、壁は計算ではなくメモリの通り道だと結論づけています。

## 反応と論点

READMEは、一般的なCPU向けの仕組みより3〜4倍速いとしていますが、どのソフトのどの設定と比べたのかは書かれていません。また、ローカルLLMでは重みを4ビットなどに縮める量子化で速度を稼ぐのが一般的ですが、PULSAR-ASMはあえて圧縮せず、元の精度で動かす前提で数字を出しています。

作者は先の計画として、補助モデルに先読みさせる投機的デコードや4ビット量子化を挙げ、いずれ毎秒20〜35トークンを目指すとしています。動機として掲げるのは、AIをクラウドから家電やドローン、マイコンへ広げることです。ただ、マイコン向けは構想の段階で、今動くのはx86-64のWindowsだけです。リポジトリにはライセンスの表記がなく、10月4日時点でスターは1つです。

## 日本のビジネスへの影響

日本で今すぐ業務に使う道具ではありません。モデルは2Bの小型で、日本語の性能についての記載もなく、速度も毎秒4トークン台です。一方で、「AIと組めば、アセンブリのような低い層のコードも個人で書き切れる」実例としては参考になります。

関係が深いのは、組み込み機器やエッジ端末のメーカーで、端末の中でAIを動かしたい開発者です。今すぐやれることは、技術報告の「1トークンごとに重みを全部読む」計算を自社の端末に当てはめ、メモリ帯域とモデルサイズから出せる速度の上限を見積もることです。この割り算だけで、その端末で載せられるモデルの大きさの目安がつきます。

注意点は2つあります。ライセンスの表記がないため、コードを製品に流用することはできません。また、同梱の実行ファイルやアセンブラーをそのまま動かすことになるので、試すなら業務用でないPCにとどめます。手元のPCでAIを動かす現実的な選択肢は[ローカルLLM・オープンウェイトモデルのおすすめ](/best/local-llm/)で比べています。
