---
{
  "title": "Diffusion ControllerはGoogleの画像生成を制御する新理論、小さな部品でLoRA超え",
  "description": "Google Researchは画像生成AIの調整手法を一つの数理の枠組みにまとめるDiffusion Controllerを解説した。本体を固定したまま約1,200万パラメータの部品を足し、2つの学習方式で人の好みの指標がLoRAを上回った。",
  "date": "2026-10-01T18:39:00+09:00",
  "category": "research",
  "tags": [
    "Google Research",
    "Diffusion Controller",
    "画像生成",
    "論文",
    "広告クリエイティブ"
  ],
  "summary": [
    "Google ResearchのDiffusion Controllerは、画像生成の過程を一つの制御問題として扱い、ばらばらだった調整手法をまとめる",
    "本体モデルを固定し、途中の出力を見て軌道を補正する小さな追加部品で、2つの学習方式で人の好みの指標がLoRAを上回った",
    "実験は旧世代のStable Diffusion v1.4で、コードや製品への搭載は発表されていない。広告制作で使えるのはまだ先"
  ],
  "sources": [
    {
      "title": "How Diffusion Controller unifies and simplifies AI image generation",
      "publisher": "Google Research Blog",
      "url": "https://research.google/blog/how-diffusion-controller-unifies-and-simplifies-ai-image-generation/",
      "kind": "公式発表"
    },
    {
      "title": "Diffusion Controller: Framework, Algorithms and Parameterization",
      "publisher": "arXiv（Tong Yang ほか）",
      "url": "https://arxiv.org/abs/2603.06981",
      "kind": "論文"
    },
    {
      "title": "Diffusion Controller（HTML版・実験結果の表）",
      "publisher": "arXiv",
      "url": "https://arxiv.org/html/2603.06981v1",
      "kind": "論文"
    }
  ],
  "thumb_text": "Diffusion Controller",
  "share_text": "Google ResearchのDiffusion Controller。画像生成の調整手法を一つの理論にまとめ、小さな追加部品でLoRAを上回った",
  "editor_note": ""
}
---
Google Researchは現地時間9月29日、画像生成AIを狙いどおりに動かすための調整手法を一つの数理の枠組みにまとめる「Diffusion Controller」を公式ブログで解説しました。本体のモデルを固定したまま約1,200万パラメータの小さな追加部品を足し、人の好みの指標で一般的な追加学習手法のLoRAを上回る場面があったとしています。論文は3月にarXivで公開されたもので、ブログはその研究の紹介です。

## 何が発表されたか

画像生成AIの多くは、ノイズの画像から少しずつノイズを取り除いて絵を仕上げる「拡散モデル」です。これを思いどおりに動かす方法は、これまで大きく2系統に分かれていました。生成時にプロンプトの効き具合を調整する方法と、LoRA（本体の一部に小さな学習用の層を足す手法）や強化学習でモデルそのものを追加学習する方法です。

Diffusion Controllerとは、このノイズを取り除く過程全体を、確率的な「制御問題」として扱い直す枠組みです。各ステップで本来の進み方を少しずつ重み付けし直し、目標（好みの画風やプロンプトへの忠実さ）に近づけつつ、元のモデルから離れすぎないよう罰則をかけます。

:::quote https://research.google/blog/how-diffusion-controller-unifies-and-simplifies-ai-image-generation/ | Google Research公式ブログ「How Diffusion Controller unifies and simplifies AI image generation」
> Instead of treating image generation as a rigid sequence of isolated steps, Diffusion Controller reframes the entire denoising process as a smooth, continuous control problem.
画像生成を、互いに切り離された固定の手順の連なりとして扱うのではなく、Diffusion Controllerはノイズ除去の過程全体を、滑らかで連続した制御問題として捉え直します。
:::

この枠組みから、研究チームは2つの学習方法を導いています。1つは、一度に大きく変わりすぎないよう歯止めをかけながら少しずつ調整する強化学習（PPO型）です。もう1つは、評価の高い生成結果ほど重く学習する方式です。

さらに、理論上の最適な形は「固定した元のモデル＋小さな補正」に分けられることを示しました。ブログはこの補正部品を、バイクに後付けする「ステアリングダンパー」にたとえています。補正部品は生成途中の出力を見ながら進路を直すので、本体の中身に手を入れなくて済みます。論文はこれを、本体は非公開でも途中の出力だけは受け取れる「グレーボックス」の状況で使える形だと位置づけています。

## 実験の結果

実験は画像生成モデルのStable Diffusion v1.4で行い、人の好みを予測するスコアHPS-v2で、元のモデルに勝つ割合（勝率）を比べました。

| 手法 | 学習するパラメータ数 | 教師あり学習 | 評価重み付け学習 | PPO |
|---|---|---|---|---|
| Diffusion Controller（本体は固定） | 約1,200万 | 66.7% | 68.2% | 69.6% |
| LoRA（本体の中に追加） | 約1,700万 | 57.7% | 61.1% | 90.5% |
| Diffusion Controller（本体も同時に学習） | 約1,600万 | 69.6% | 65.6% | 93.5% |

本体を固定した版は、少ないパラメータで、2つの学習方式でLoRAを上回りました。PPOではLoRAが強く、本体も学習する版が93.5%で最も高い勝率でした。ブログが「90%の勝率」と書いているのはこの本体も学習する版のことです。50人を超える評価者による人手の評価も行っています。

生成時には、補正の強さを1つの数値で上げ下げできます。プロンプトへの忠実さを、画像を崩さずに細かく調整できるとしています。

## 反応と論点

ブログは、この仕組みで閉じた商用モデルも制御できると強調しています。

:::quote https://research.google/blog/how-diffusion-controller-unifies-and-simplifies-ai-image-generation/ | Google Research公式ブログ「How Diffusion Controller unifies and simplifies AI image generation」
> This allows engineers to perfectly control and customize even tightly locked, closed-source models without ever touching the underlying code.
これにより、エンジニアは厳重に閉じたクローズドソースのモデルでも、元のコードに一切触れずに制御・カスタマイズできます。
:::

ただし論文の前提は、各ステップの途中出力（ノイズの予測値など）を外から受け取れることです。完成画像だけを返す通常の画像生成APIで、そのまま使えるわけではありません。実験もPPOではLoRAに負けており、すべての場面で上回るわけではない点も押さえておく必要があります。今後の課題として、個人に合わせた調整、有害な画像を防ぐ安全策、動画モデルへの応用が挙がっています。

## 日本のビジネスへの影響

現時点では研究段階です。ブログと論文には、コードの公開やGoogleの製品への搭載の予定は書かれていません。日本の企業が明日から使える技術ではありません。

関係が深いのは、画像生成サービスを作る開発者と、広告クリエイティブの制作会社です。実用化されれば、ブランドの好みに寄せる調整を、本体を作り直さずに小さな部品で後付けできるようになります。案件ごとに部品を差し替え、「ブランドらしさ」と「指示への忠実さ」を1つの数値で調整する使い方が想定できます。

今すぐやれることは、Stable Diffusion系のモデルをLoRAで追加学習している開発チームが、論文の評価重み付け学習を自社の評価データで試すくらいです。それ以外は様子見でかまいません。注意点は、実験が旧世代のモデルと、好みを予測する1つのスコア中心の評価だということです。今の画像生成AIの選び方は[画像生成AIのおすすめ](/best/image-generation/)にまとめています。
