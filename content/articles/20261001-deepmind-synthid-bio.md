---
{
  "title": "SynthID BioをGoogle DeepMindが発表、AI設計タンパク質に消えない透かし",
  "description": "Google DeepMindがAIで設計したタンパク質に電子透かしを埋め込むSynthID Bioを発表した。3種類の標的でのウェット実験で結合力を落とさず、論文はNatureに掲載。コードと重みは研究者向けに公開する。",
  "date": "2026-10-01T15:35:00+09:00",
  "category": "research",
  "tags": ["Google DeepMind", "SynthID Bio", "論文", "安全性", "医療"],
  "summary": [
    "SynthID BioはAIが設計したタンパク質の配列と予測構造に検出可能な透かしを埋め込む手法",
    "VEGF-Aなど3つの標的を使ったウェット実験で、透かし入りの設計は結合力も当たり率も落ちなかった",
    "狙いはDNA合成受託のスクリーニング支援で、コードとデータ、モデルの重みを研究コミュニティに公開する"
  ],
  "sources": [
    {"title": "Introducing SynthID Bio", "publisher": "Google DeepMind", "url": "https://deepmind.google/blog/introducing-synthid-bio/"},
    {"title": "SynthID Bio watermarks AI-designed proteins", "publisher": "Google", "url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/synthid-bio/"},
    {"title": "Function-preserving watermarking of AI-generated proteins", "publisher": "Nature", "url": "https://www.nature.com/articles/s41586-026-10965-y"},
    {"title": "Demis Hassabis の投稿", "publisher": "X @demishassabis", "url": "https://x.com/demishassabis/status/2105348732464070823"},
    {"title": "Google figures out how to watermark AI-designed proteins", "publisher": "Ars Technica", "url": "https://arstechnica.com/science/2026/09/google-figures-out-how-to-watermark-ai-designed-proteins/"}
  ],
  "thumb_text": "SynthID Bio",
  "share_text": "Google DeepMindがAI設計タンパク質への電子透かし「SynthID Bio」を発表。Natureに掲載、コードも公開",
  "editor_note": ""
}
---
Google DeepMindは現地時間9月30日、AIが設計したタンパク質に電子透かしを埋め込む「SynthID Bio」を発表しました。3つの標的を使った実験室での検証で、透かしを入れた設計も入れない設計と同じだけ結合したとしています。論文はNatureに掲載されました。

## 何が発表されたか

SynthID Bioは、画像や文章に使われてきたGoogleの透かし技術SynthIDを、合成生物学に持ち込んだものです。デジタルのファイルではなく、合成されたタンパク質そのものから検出できる点が特徴です。

:::quote https://deepmind.google/blog/introducing-synthid-bio/ | Google DeepMind公式ブログ「Introducing SynthID Bio」
> Today, we’re introducing SynthID Bio to bring watermarking technology to synthetic biology.
本日、透かし技術を合成生物学に持ち込むSynthID Bioを発表します。
:::

手法は2系統です。配列側は、広く使われるタンパク質設計ツールProteinMPNNに、SynthID-textの「トーナメント方式」の選び方を組み込みます。アミノ酸を1つずつ決めていく過程で、タンパク質として成立する選択肢が複数あるときに、秘密鍵から決まる側を選ぶ仕組みです。構造側は、AlphaFold 3の拡散部分を微調整し、予測した3D座標そのものに署名が乗るようにモデルの重みへ埋め込みます。

検証はAlphaProteoで設計した結合タンパク質（他のタンパク質に狙って貼りつく分子）で行われました。標的はVEGF-A、新型コロナウイルスのスパイクタンパク質の受容体結合領域、PD-L1の3つです。公式発表によると、透かし入りの設計は、当たり率・結合親和性・配列の多様性のいずれも透かしなしの版と同等でした。構造側は、論文によれば偽陽性率0.1%の条件で真陽性率99.8%超を保ちつつ、構造予測の精度指標は落ちていません。

Googleは手法の論文に加えて、コードと試験管内の実験データを公開し、モデルの重みも研究コミュニティに提供するとしています。同社は同じ日に[フロンティアモデルGemini 4 Argon](/news/20261001-google-gemini-4-argon/)も発表しており、能力の高いモデルを出すのと並行して安全側の仕組みを示す形になりました。

{{x:https://x.com/demishassabis/status/2105348732464070823}}

ハサビス氏はXで、バイオセキュリティはAI時代で最も急を要する課題の一つだとし、ツールのオープンソース化に触れました。

## なぜ必要か

問題は、DNA合成の受託事業者が行う審査にあります。注文された配列が既知の毒素やウイルスに似ていれば止められますが、AIが設計した配列は既知のどれにも似ていないことがあります。従来なら「まだ知られていない天然の配列だろう」と流せましたが、いまはその前提が崩れています。

ここで透かしが効けば、審査側は「信頼できるモデルから出た設計かどうか」を自動で判定でき、人手の精査をそれ以外に集中させられます。DNA合成大手Twist Bioscienceのジェームズ・ディガンズ氏は公式発表で、透かしはスクリーニングを強化し、精査が必要な配列に資源を集中させうると述べています。Protein Data BankやUniProt、GenBankといった公開データベースに、AI生成物が誤った扱いで混ざるのを防ぐ用途も挙げられています。

## 限界と論点

Googleは概念実証だとしており、運用には業界全体の調整と標準化が要るとしています。論文も、ProteinMPNNで作り直す「再配列化」攻撃では透かしがほぼ消えると報告しています。既知の結合体から出発した場合、構造フィルターを併用した攻撃では当たり率が66〜97%残る一方、フィルターなしでは3〜33%まで落ちるという試算です。

Ars Technicaは、仕組み全体が鍵の配布と管理の安全性に依存すること、短いタンパク質では十分な信号を埋め込めないこと、天然の蛍光タンパク質などを後ろにつなげると透かしが薄まりうることを指摘しています。ProteinMPNNを使わない設計ツールには、そのままでは適用できません。同誌は、実用になるかは明らかでないとしつつ、成立すること自体が興味深いと評しています。

## 日本のビジネスへの影響

日本からも使えます。論文は公開され、コードと重みは研究コミュニティに提供されるため、大学や創薬スタートアップが自分の設計パイプラインで試せます。ただし製品ではなく、業界標準でもありません。

関係が深いのは、タンパク質設計を外注または内製している創薬・バイオのR&D部門と、合成の受託側です。前者は、自社の設計が「信頼できる出所」として扱われるかどうかが、将来の発注のスムーズさに関わってきます。

いま急ぐ必要はありませんが、DNA合成を外注している企業は、受託先が透かしや由来情報をどう扱う方針かを一度確認しておく価値があります。注意点は、透かしが抑止力であって防御壁ではないことです。悪意ある側は設計をやり直せば透かしを外せるため、既存の審査を置き換えるものとしては扱えません。論文の読み解きにAIを使うなら[調べもの・リサーチに強いAIのおすすめ](/best/research/)も参考にしてください。
