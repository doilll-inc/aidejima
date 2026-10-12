---
{
  "title": "Copilotを動かすAI半導体をMicrosoftが自社製に、新型「Maia 300」は来年から本格導入",
  "description": "Microsoftが現地時間10月12日、自社開発のAI半導体「Maia 300」を発表した。2027年から自社の製品・サービスでAIを動かす主力にし、原子力発電所数基分にあたる数ギガワット規模で導入する。電力あたりの処理量は他社の主要なGPUより40%多いと主張する。",
  "date": "2026-10-13T04:00:00+09:00",
  "category": "hardware",
  "tags": ["Microsoft", "Maia 300", "Copilot", "半導体", "データセンター", "NVIDIA"],
  "summary": [
    "Microsoftは10月12日、自社開発のAI半導体「Maia 300」を発表し、2027年から自社サービスのAIを動かす主力にすると明らかにした",
    "Maia 300は同じ電力で、他社の主要なGPU（AI計算用の半導体）を使う仕組みより40%多くの文章を生成できるとMicrosoftは主張する",
    "前の世代のMaia 200はすでに米国・欧州・豪州でCopilotを動かしており、年内に開発者向けサービスにも広げる"
  ],
  "sources": [
    {"title": "Microsoft to expand Azure Maia system to multi-gigawatt deployments", "publisher": "Official Microsoft Blog（Scott Guthrie）", "url": "https://blogs.microsoft.com/blog/2026/10/12/microsoft-to-expand-azure-maia-system-to-multi-gigawatt-deployments/", "kind": "公式発表"},
    {"title": "Satya Nadella の投稿", "publisher": "X @satyanadella", "url": "https://x.com/satyanadella/status/2109631106404487523", "kind": "X投稿"},
    {"title": "Microsoft's latest custom chip: Maia 300", "publisher": "Microsoft Source", "url": "https://news.microsoft.com/maia-2026/", "kind": "公式発表"},
    {"title": "Deep dive into Azure Maia 300 architecture", "publisher": "Microsoft Azure Blog", "url": "https://azure.microsoft.com/en-us/blog/deep-dive-into-azure-maia-300-architecture/", "kind": "公式ドキュメント"},
    {"title": "Microsoft plans to scale its own Maia AI chips to gigawatt levels by 2027", "publisher": "The Decoder", "url": "https://the-decoder.com/microsoft-plans-to-scale-its-own-maia-ai-chips-to-gigawatt-levels-by-2027/", "kind": "報道"},
    {"title": "Microsoft is ordering 300,000+ Maia 300 AI chips from TSMC as it races to reduce its dependence on Nvidia", "publisher": "The Next Web", "url": "https://thenextweb.com/news/microsoft-maia-300-chip-tsmc-production-boost-nvidia", "kind": "報道"}
  ],
  "thumb_prompt": "A miniature data center hall with rows of tiny server racks, where tiny workers in hard hats are carefully lowering one giant shiny square computer chip into place with a toy crane, while an old pile of green graphics cards waits on the side.",
  "thumb_style": "diorama",
  "thumb_text": "Maia 300",
  "share_text": "MicrosoftがCopilotなどを動かすAI半導体を自社製の「Maia 300」へ。2027年から数ギガワット規模で導入",
  "editor_note": ""
}
---
Microsoftは現地時間10月12日、自社で開発したAI用の半導体「Maia 300」を発表しました。2027年から、CopilotなどMicrosoftの製品・サービスでAIを動かす主力の仕組みを自社製のMaiaに切り替え、数ギガワット規模で導入するとしています。

## 何が発表されたか

Maia 300とは、Microsoftのデータセンターで、AIが質問に答えたり文章を作ったりする処理（推論）を専門に担う半導体です。Maiaシリーズの3代目にあたります。クラウド部門を率いるスコット・ガスリー氏は公式ブログで、今後の方針を次のように書いています。

:::quote https://blogs.microsoft.com/blog/2026/10/12/microsoft-to-expand-azure-maia-system-to-multi-gigawatt-deployments/ | Official Microsoft Blog「Microsoft to expand Azure Maia system to multi-gigawatt deployments」
> We will scale our Azure Maia family to multi-gigawatt deployments starting in 2027, making Maia the primary inference system for Microsoft products and services.
2027年からAzure Maiaシリーズを数ギガワット規模に広げ、Microsoftの製品とサービスでAIを動かす主力の仕組みにする。
:::

1ギガワットは、大型の原子力発電所1基の出力にほぼ相当します。それを数基分、自社製の半導体だけで動かす計画です。

公式発表で示された主な数字は次のとおりです。

- **電力あたりの処理量**: 同じ電力で、他社の主要なGPU（AI計算に使われる半導体。NVIDIA製が代表）を使う仕組みより40%多くの文章を生成できる見込み
- **前の世代との比較**: 96個を載せた1台の棚（ラック）で、Maia 200の最大7倍の処理量
- **記憶装置**: 1個あたり288GBの高速メモリを積み、長い資料を読ませる処理や、何段階も作業を続けるAIエージェントに向く
- **製造**: 計算部分は台湾TSMCの最先端の製造技術（N2P）で作る
- **導入時期**: 2027年から本番の運用を始める

{{card:https://azure.microsoft.com/en-us/blog/deep-dive-into-azure-maia-300-architecture/|Deep dive into Azure Maia 300 architecture（技術の詳細）|Microsoft Azure Blog}}

## すでにCopilotを動かしている

今回の発表で目を引くのは、前の世代のMaia 200がすでに実際のサービスを動かしている点です。ガスリー氏のブログによると、Maia 200は米国・欧州・オーストラリアのデータセンターに導入が進み、Microsoft Copilotの処理を担っています。年内には、プログラミング支援のGitHub Copilotと、企業がAIアプリを作るためのMicrosoft Foundryにも広げる予定です。

Maia 200の上では、OpenAIのモデル、Microsoft自社のMAIモデル、公開されている主なモデルがすでに動いています。Teams・Copilot・CoworkといったサービスのAI機能では、主要なGPUを使う場合より電力あたり最大1.7倍の処理ができているとしています。

## 背景

AI用の半導体は、NVIDIAのGPUがほぼ独占してきました。GoogleやAmazonも自社製の半導体を作っていますが、MicrosoftのMaiaは他社に比べて成熟していないと見られてきたと、The Next Webは報じています。Maia 200の展開が始まったのは今年1月です。

今回、自社製を「主力」と言い切ったことで、NVIDIAへの依存を減らす方針がはっきりしました。米The Informationは8月、Microsoftが2027年の納入分としてMaia 300を30万個超つくれる生産枠をTSMCと交渉していると報じています。

## 反応と論点

サティア・ナデラCEOはXで、今回の発表を自社製の半導体への「これまでで最大の賭け」と表現しました。2027年からMaiaを自社製品の主力にし、Maia 300で電力あたりの効率を高めると投稿しています。

{{x:https://x.com/satyanadella/status/2109631106404487523}}

一方で、注意すべき点もあります。40%という数字はMicrosoft自身の見込みで、どのGPUと、どんな処理で比べたのかは公式発表では詳しく示されていません。技術の詳細は、11月17〜20日に開く年次イベント「Microsoft Ignite 2026」で追加で説明するとしています。NVIDIAとの関係も続き、Microsoftは複数の種類の半導体とAIモデルを組み合わせる方針だと強調しています。

## 日本のビジネスへの影響

- **使えるか**: Maia 300は社外に売る製品ではなく、Microsoftのデータセンターの中で使われます。Maia 200の導入先として挙がっているのは米国・欧州・オーストラリアで、日本のデータセンターへの導入は発表されていません
- **誰にどう効くか**: CopilotやMicrosoft 365を全社で導入している企業の情報システム部門と経営者です。AIを動かす費用が下がれば、Copilotの料金や使える量に影響する可能性がありますが、値下げの発表はまだありません
- **今すぐやれること**: 今は様子見でよい段階です。Azureで自社のAIアプリを動かしている開発担当者は、年内にMicrosoft FoundryでMaia 200が使えるようになる予定なので、提供が始まったら費用と速さを今のGPUと比べる準備をしておくと判断が早くなります
- **注意点**: 自社製の半導体への切り替えで、応答の速さや品質が変わるかどうかは、利用者からは見えにくい部分です。Copilotの使い心地が変わったと感じたら、社内で記録を残しておくと、料金の見直しや他社との比較の材料になります。各社のAIの料金を比べるなら[AI APIの料金比較](/best/api/)が参考になります
