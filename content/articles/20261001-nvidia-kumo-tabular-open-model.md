---
{
  "title": "NVIDIAが表データ予測の「Kumo Tabular」を公開、学習なしで解約や需要を予測",
  "description": "NVIDIAは表データの予測モデルKumo Tabularを公開した。ラベル付きの行を渡すだけで、追加学習なしに新しい行の分類や数値を予測する。2,800万〜2億1,500万パラメータの3サイズで、商用利用できる。",
  "date": "2026-10-01T18:39:00+09:00",
  "updated": "2026-10-01T18:55:00+09:00",
  "category": "research",
  "tags": [
    "NVIDIA",
    "Kumo Tabular",
    "オープンウェイト",
    "商用利用",
    "ベンチマーク"
  ],
  "summary": [
    "NVIDIAのKumo Tabularは、表のラベル付きの行を手本に新しい行を予測する基盤モデルで、追加学習も特徴量の作り込みも要らない",
    "人工的に作った表だけで学習し、3サイズを公開。NVIDIAによると表データの4つのベンチマークで1位になった",
    "重みはOpenMDW-1.1で商用利用でき、ライブラリはApache 2.0。数値とカテゴリの列が対象で、NVIDIAのGPU前提で動かす"
  ],
  "sources": [
    {
      "title": "NVIDIA Kumo Tabular Sets a New Accuracy-Efficiency Frontier for Tabular Prediction",
      "publisher": "Hugging Face Blog（NVIDIA）",
      "url": "https://huggingface.co/blog/nvidia/kumo-tabular",
      "kind": "公式発表"
    },
    {
      "title": "nvidia/Kumo-Tabular（モデルカード）",
      "publisher": "Hugging Face",
      "url": "https://huggingface.co/nvidia/Kumo-Tabular",
      "kind": "公式ドキュメント"
    },
    {
      "title": "NVIDIA/structured-data-models",
      "publisher": "GitHub",
      "url": "https://github.com/NVIDIA/structured-data-models",
      "kind": "公式ドキュメント"
    },
    {
      "title": "OpenMDW License Agreement, version 1.1",
      "publisher": "OpenMDW",
      "url": "https://openmdw.ai/license/1-1/",
      "kind": "公式ドキュメント"
    }
  ],
  "thumb_text": "Kumo Tabular",
  "share_text": "NVIDIAが表データ予測モデルKumo Tabularを公開。学習なしで解約や需要を予測、商用利用もできる",
  "editor_note": ""
}
---
NVIDIAは現地時間9月29日、表形式のデータで分類や数値の予測をする基盤モデル「Kumo Tabular」をHugging Faceで公開しました。ラベル付きの行を手本として渡すだけで、追加の学習なしに新しい行の答えを返します。重みは商用利用できるOpenMDW-1.1ライセンスで、2,800万〜2億1,500万パラメータの3サイズがあります。

## 何が発表されたか

Kumo Tabularは、答えの分かっている行と予測したい行をまとめて渡すと、その場で答えを返すTransformerモデルです。解約するか、いくらで売れるかといった表データの予測では、課題ごとに勾配ブースティング木（表データの予測で20年にわたり主流の手法）などを学習させ直すのが一般的で、その手間を省けるのが売りです。大規模言語モデルがプロンプト内の例から答えを出す「文脈内学習」を表に持ち込んだ形で、NVIDIAの構造化データ向けモデル群「NVIDIA Kumo Structured」の1つに位置づけられています。

:::quote https://huggingface.co/blog/nvidia/kumo-tabular | NVIDIA（Hugging Face Blog）「NVIDIA Kumo Tabular Sets a New Accuracy-Efficiency Frontier for Tabular Prediction」
> Given a table of labeled rows, it predicts the labels of new rows in a single forward pass, with no training, no tuning, and no feature engineering, for both classification and regression.
ラベル付きの行からなる表を渡すと、新しい行のラベルを1回の計算で予測します。学習もパラメータ調整も特徴量の作り込みも要らず、分類と回帰の両方に対応します。
:::

使うときは、NVIDIAのPythonライブラリ「structured-data-models」で表をGPU上のデータに変え、手本の行（特徴量とラベル）と予測したい行（特徴量だけ）をモデルに渡します。モデルカードのサンプルでは、乳がんの診断データのうち300行を手本にして、残りの行の分類確率を出しています。重みは初めて使うときにHugging Faceから自動で読み込まれます。

## 仕組みと学習データ

学習に使った表は、すべて人工的に作ったものです。Small・Medium・Largeはそれぞれ約3,500万・7,100万・1億3,700万個の表を見ており、学習の後半では最大6万行・100列の大きさまで扱いました。表は原因と結果の関係をランダムに組み立てて自動生成し、欠損値や、同じ条件なのにラベルが食い違う行といった実データの乱れもわざと混ぜています。学習手順とデータの生成器は近く公開する予定です。

モデルの中では、列ごとに値がその列の中でどんな位置にあるかをつかみ、1行の中で列どうしの関係を読み取ったうえで、手本の行と予測したい行を照らし合わせます。この組み立ては、先行するTabICLやTabPFNで提案された仕組みを土台にしています。回帰（数値の予測）では999個の分位点を出すため、予測値と一緒に不確かさの幅も得られます。

## 性能（NVIDIAの発表）

NVIDIAによると、Kumo Tabularは表データのベンチマークTabArena、BeyondArena、TALENT、ScoringBenchの4つで1位になりました。TabArenaでは、調整済みの勾配ブースティング木や自動機械学習のAutoGluon、他の表データ基盤モデルを抑え、総合でElo 1950を記録したといいます。同じ条件（GPUのRTX 6000 Pro 1枚）で、競合のLimiX-2より高速に動いたとしています。

{{card:https://huggingface.co/nvidia/Kumo-Tabular|nvidia/Kumo-Tabular|Hugging Face}}

| 項目 | 内容 |
|---|---|
| サイズ | Small・Medium・Large（2,800万〜2億1,500万パラメータ） |
| 重みのライセンス | OpenMDW-1.1（無償・商用可） |
| ライブラリ | structured-data-models（Apache 2.0、Python 3.11以上） |
| 対象の列 | 数値とカテゴリ（文章・画像・日時は前処理で変換） |
| 分類の上限 | 1回の計算で10クラスまで（ライブラリで拡張可） |

## ライセンスと動かす環境

OpenMDW-1.1は、モデルと関連資料を無償で制限なく扱えるライセンスです。配布するときはライセンス文と著作権表示を残す必要があり、このモデルが特許や著作権を侵害していると訴えた場合は権利を失います。モデルの出力の使い方には制限を設けていません。

ライブラリはGPUでの処理を前提に作られており、READMEやモデルカードのサンプルコードもCUDA（NVIDIAのGPU）で動かす形です。同じライブラリには、TabICLv2やGoogle ResearchのTabFMも収録されています。NVIDIA自身も限界を明記しており、学習した範囲を大きく超える表や、手本の行と予測したい行の傾向が違う場合は精度が落ちることがあるとして、本番で使う前に手元の検証データで精度を確かめるよう求めています。

## 日本のビジネスへの影響

重みはHugging Faceから誰でも入手でき、日本企業も商用で使えます。社内のGPUで動かせば、顧客データを外部のAPIに送らずに済みます。

関係が深いのは、マーケティングのデータ分析担当と経営企画です。解約しそうな会員の予測、広告経由の顧客のLTV（生涯価値）予測、店舗別の売上予測などで、モデルを一から作る前の「たたき台」を短時間で作れます。分位点が出るので、在庫や予算を「予測の幅」で考えたいときにも向いています。

今すぐできるのは、いま勾配ブースティング木で動かしている予測（解約予測など）と同じ検証データで、Kumo Tabularの精度を比べることです。過去の実績行を手本に、直近の行を予測させるだけで試せます。

注意点は3つあります。日付や文章の列はライブラリの前処理で特徴量に変えて使う仕組みなので、需要予測では曜日や前週の売上といった情報を自分で列として用意したほうが確実です。NVIDIAのGPUがない環境では、まず動作を確かめてください。顧客の個人データを使うときは、利用目的の範囲内かを確認してから入れてください。オープンウェイトのモデル全般は[ローカルLLM・オープンウェイトモデルのおすすめ](/best/local-llm/)にまとめています。
