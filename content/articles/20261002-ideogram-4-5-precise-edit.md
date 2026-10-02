---
{
  "title": "Ideogram 4.5は何度直しても崩れにくい画像編集モデル、広告の差し替え作業に照準",
  "description": "Ideogramが画像編集モデルIdeogram 4.5を公開した。編集を重ねても色ずれや画質の劣化がたまりにくい設計で、APIでは触れていない画素を元画像からそのまま写す。料金は1枚0.8〜22セントと報じられている。",
  "date": "2026-10-02T12:10:00+09:00",
  "category": "models",
  "tags": ["Ideogram", "Ideogram 4.5", "画像編集", "画像生成", "広告クリエイティブ", "API"],
  "summary": [
    "Ideogramは現地時間9月30日、編集を何度重ねても画質が崩れにくい画像編集モデルIdeogram 4.5を公開した",
    "Ideogram 4.5のAPIの精密編集では、変更していない画素を元画像からそのまま写し、出力サイズも元画像に合わせる",
    "Ideogram 4.5は自社サービス・API・Kreaなど提携先で使え、重みの公開も「近く」と予告している"
  ],
  "sources": [
    {"title": "Ideogram 4.5: The most precise edit model.", "publisher": "Ideogram", "url": "https://ideogram.ai/models/4.5/", "kind": "公式サイト"},
    {"title": "API Overview（Ideogram API v2）", "publisher": "Ideogram Documentation", "url": "https://developer.ideogram.ai/ideogram-api/api-overview", "kind": "公式ドキュメント"},
    {"title": "Precise Edit with Ideogram 4.5（API Reference）", "publisher": "Ideogram Documentation", "url": "https://developer.ideogram.ai/api-reference/images/precise-edit/ideogram-4-5", "kind": "公式ドキュメント"},
    {"title": "Ideogram の投稿（Ideogram 4.5の発表）", "publisher": "X @ideogram_ai", "url": "https://x.com/ideogram_ai/status/2105327223431737780"},
    {"title": "Ideogram の投稿（他モデルとの比較）", "publisher": "X @ideogram_ai", "url": "https://x.com/ideogram_ai/status/2105327258466693238"},
    {"title": "Justine Moore の投稿", "publisher": "X @venturetwins", "url": "https://x.com/venturetwins/status/2105329105373900933"},
    {"title": "Krea の投稿", "publisher": "X @krea_ai", "url": "https://x.com/krea_ai/status/2105334175939395641"},
    {"title": "Ideogram 4.5 vs GPT Image 2.5: which version to use when", "publisher": "Picsart", "url": "https://picsart.com/blog/ideogram-4-5-vs-gpt-image-2-5/", "kind": "公式サイト"},
    {"title": "Ideogram says its new model can edit part of an image without messing up the rest", "publisher": "The Decoder", "url": "https://the-decoder.com/ideogram-says-its-new-model-can-edit-part-of-an-image-without-messing-up-the-rest/", "kind": "報道"},
    {"title": "Ideogram 4.5 introduces multi-turn editing at native 2K", "publisher": "AlternativeTo", "url": "https://alternativeto.net/news/2026/10/ideogram-4-5-introduces-multi-turn-editing-at-native-2k/", "kind": "報道"}
  ],
  "thumb_text": "Ideogram 4.5",
  "share_text": "Ideogram 4.5は編集を重ねても色ずれや劣化がたまりにくい画像編集モデル。広告の差し替え向き",
  "editor_note": ""
}
---
画像生成AIのIdeogramは現地時間9月30日、画像編集に特化した新モデル「Ideogram 4.5」を公開しました。売りは、同じ画像に何度も手直しを重ねても、色のずれや細部の崩れがたまっていかない点です。自社のサービスとAPIに加え、KreaやPicsartなどの提携先でも使えるようになっています。

## 何が発表されたか

Ideogram 4.5とは、指示した部分だけを変え、それ以外を元の画像のまま残すことを狙った画像編集モデルです。画像生成AIで「色だけ変えて」「背景だけ差し替えて」と何度もやりとりすると、指示していない部分の画素が少しずつずれ、色味が変わり、質感が荒れていくことがあります。Ideogramはこの「編集のたびにたまる劣化」を主な課題に据えました。

:::quote https://ideogram.ai/models/4.5/ | Ideogram公式「Ideogram 4.5: The most precise edit model.」
> With each edit, image models can introduce pixel shifts, color changes, and texture artifacts. Ideogram 4.5 reduces this drift, preserving details across multi-turn edits.
画像モデルは編集のたびに、画素のずれ、色の変化、質感の乱れを持ち込むことがあります。Ideogram 4.5はこのずれを抑え、何度編集しても細部を保ちます。
:::

開発者向けのAPIでは、「Precise Edit（精密編集）」という専用の窓口が用意されました。公式ドキュメントによると、仕組みは次のとおりです。

- 編集で実質的に変わらなかった画素は、元の画像からそのままコピーする
- 出力は、元画像と同じ幅と高さで返す（最大25MB、縦横比は1:6〜6:1）
- マスクを付ければ、編集する範囲を一部に絞れる
- 商品や素材、作風の見本として、参照画像を最大4枚まで渡せる
- 品質は段階的に選べ、最も速く安い `very_low` から、時間がかかり高価な `high` まである

:::quote https://developer.ideogram.ai/ideogram-api/api-overview | Ideogram API ドキュメント「API Overview」
> With Precise Edit, pixels the edit doesn't touch are copied exactly from your image, and the result comes back at your image's own width and height.
Precise Editでは、編集が触れない画素はあなたの画像から正確にコピーされ、結果は元画像と同じ幅と高さで返ります。
:::

公式ページでは、色や照明の調整、デザインの中の文字の書き換え、商品写真、室内の模様替え、古い写真の修復、ラフスケッチからの画像化といった使い方を例示しています。高解像度の画像を縮小せずに一部だけ編集し、元の画像に継ぎ目なく戻せるとも説明しています。

料金について、The Decoderは品質4段階で1枚0.8〜22セント、すべてネイティブの2K解像度だと報じています。APIの料金表は公式サイトにありますが、今回の確認では金額を読み取れませんでした。

{{card:https://developer.ideogram.ai/api-reference/images/precise-edit/ideogram-4-5|Precise Edit with Ideogram 4.5（API Reference）|Ideogram}}

## 他社モデルとの比べ方

Ideogramは発表に合わせ、同じ編集の手順をOpenAIのGPT Image 2.5 Sunburst、GoogleのNano Banana ProとNano Banana 2でも試した比較を出しました。

{{x:https://x.com/ideogram_ai/status/2105327258466693238}}

投稿では、GPT ImageとNano Bananaの出力は数回の編集で使えなくなる一方、Ideogram 4.5は編集を重ねてもきれいなままだと主張しています。ただしこれは発表元による比較で、編集の回数や指示の中身を第三者が同じ条件で検証した結果ではありません。

提携先からの見方もあります。Picsartは自社ブログで、新しい画像を作りながら手直しするならIdeogram 4.5、既存の画像の一部を直すならIdeogram 4.5 Precise Edit、速さ優先の試作ならGPT Image 2.5 Flare、4Kまでの細部重視ならGPT Image 2.5 Sunburst、という使い分けを示しました。1つのモデルですべてを済ませるより、作業ごとに選ぶ前提です。

## 反応と論点

投資家のジャスティン・ムーア氏は、飲料ブランドの広告画像に細かい修正を何度も重ねて試し、制作チームがバリエーションを出したり地域向けに作り替えたりする作業に近い使い方で、ゆがみやノイズが出なかったとXに投稿しました。

{{x:https://x.com/venturetwins/status/2105329105373900933}}

画像・動画生成サービスのKreaも、発表当日にIdeogram 4.5の提供を始めています。一方で、評価はまだ発表元と提携先、早期の試用者の声が中心です。重みの公開について、Ideogramは発表の投稿で「近く」とだけ書いており、時期やライセンスは示していません。前の世代のIdeogram 4.0は、2026年5〜6月にHugging Faceで重みが公開されています。

## 日本のビジネスへの影響

- **使えるか**: Ideogram 4.5はWebのIdeogramとAPIで使えます。公式ページは、デザインの中の文字をそのまま書き換えたり別の言語に訳したりする編集を例示しています。円建ての料金はなく、日本からの提供条件は公式に明示されていません。料金プランと商用利用の条件は[画像生成AIのガイド](/best/image-generation/)にまとめています。
- **誰にどう効くか**: 関係が深いのは、広告のバナーやEC商品画像を大量に作り直す広告運用者・EC担当者と、画像の差し替えを自動化したい開発者です。色違い、背景違い、季節の文言違いといった派生を、元の構図を崩さずに量産できるかが実務での評価軸になります。
- **今すぐやれること**: いま使っている商品画像を1枚選び、「色を変える→背景を変える→文字を変える」の3回の編集をIdeogram 4.5と普段のツールで同じ手順でかけ、3回目の画像を並べて比べます。APIなら `dry_run` を付けると、生成せずに料金の見積もりだけを返せます。
- **注意点**: 比較画像は発表元が用意したもので、自社の素材で同じ結果になるとは限りません。人物の写真や他社のロゴを含む画像を編集する場合は、肖像権や商標の確認が別に必要です。重みの公開時期は未定なので、自社サーバーで動かす前提の計画はまだ立てないほうが安全です。
