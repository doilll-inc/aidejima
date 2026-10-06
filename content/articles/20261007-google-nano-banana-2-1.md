---
{
  "title": "Googleの画像AI「Nano Banana 2.1」、文字や同じ人物の描き分けが向上しAPIは半額に",
  "description": "Googleが画像の生成・編集AI「Nano Banana 2.1」を公開した。画像内の文字や同じ人物の一貫性が改善し、開発者向けの料金は1枚$0.0336と前モデルの半額。旧モデルは10月29日に提供終了する。",
  "date": "2026-10-07T03:40:00+09:00",
  "category": "models",
  "tags": ["Google", "Nano Banana 2.1", "Gemini", "画像生成", "画像編集", "広告クリエイティブ"],
  "summary": [
    "Googleは10月6日、画像を作って直せるAI「Nano Banana 2.1」を公開し、Google検索のAIモードなどで順次使えるようにした",
    "Nano Banana 2.1は画像の中の文字、同じ人物を何枚も描き分ける一貫性、指示どおりに描く力が前の版より良くなったとGoogleは説明している",
    "開発者向けの料金は標準画質1枚$0.0336で前モデルの半額になり、前モデルは10月29日に提供を終える"
  ],
  "sources": [
    {"title": "Gemini API Release notes（October 6, 2026）", "publisher": "Google AI for Developers", "url": "https://ai.google.dev/gemini-api/docs/changelog", "kind": "公式ドキュメント"},
    {"title": "Gemini Nano Banana 2.1", "publisher": "Google AI for Developers", "url": "https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1", "kind": "公式ドキュメント"},
    {"title": "Gemini Developer API pricing", "publisher": "Google AI for Developers", "url": "https://ai.google.dev/gemini-api/docs/pricing", "kind": "公式ドキュメント"},
    {"title": "Google の投稿", "publisher": "X @Google", "url": "https://x.com/Google/status/2107501209154204148", "kind": "X投稿"},
    {"title": "Robby Stein の投稿", "publisher": "X @rmstein", "url": "https://x.com/rmstein/status/2107513543327412436", "kind": "X投稿"},
    {"title": "Nano Banana 2.1 Now In Google AI Mode In Search", "publisher": "Search Engine Roundtable", "url": "https://www.seroundtable.com/nano-banana-21-google-ai-mode-42246.html", "kind": "報道"},
    {"title": "Google Nano Banana 2.1 Released: Features, Speed Test, & Image Upgrades", "publisher": "Nokiapoweruser", "url": "https://nokiapoweruser.com/google-quietly-launches-nano-banana-2-1-image-model/", "kind": "報道"}
  ],
  "thumb_text": "Nano Banana 2.1",
  "thumb_style": "illustration",
  "thumb_prompt": "A cheerful shop-window poster being painted by a robotic arm holding a banana as a paintbrush, the same cartoon mascot character appearing identically on four different posters lined up along a street wall.",
  "share_text": "Googleの画像AIがNano Banana 2.1に。文字や同じ人物の描き分けが向上し、API料金は前モデルの半額",
  "editor_note": ""
}
---
Googleは現地時間10月6日、画像を作ったり手直ししたりできるAIの新版「Nano Banana 2.1」を公開しました。画像の中の文字や、同じ人物・キャラクターを何枚も同じ姿で描く力が上がったとしており、開発者向けの料金は標準画質1枚$0.0336と、これまでの「Nano Banana 2」の半額です。

## 何が発表されたか

Nano Banana 2.1とは、Googleの対話AI「Gemini」に組み込まれている画像の生成・編集モデルです。言葉で頼むと画像を作り、「背景だけ夜にして」のように会話で直していけます。2月に出たNano Banana 2（開発者向けの正式名はGemini 3.1 Flash Image）の改良版にあたります。

Google公式のXアカウントは、前のモデルを「全面的に上回る」とし、デザインの見た目、範囲を指定した部分修正、同じ被写体を保つ力で大きく伸びたと投稿しました。

{{x:https://x.com/Google/status/2107501209154204148}}

開発者向けの変更履歴では、改善点をもう少し具体的に挙げています。

:::quote https://ai.google.dev/gemini-api/docs/changelog | Google AI for Developers「Gemini API Release notes」
> Released Gemini Nano Banana 2.1 (gemini-nano-banana-2.1), the latest high-efficiency image generation and conversational editing model.
軽くて速い画像生成・対話型編集モデルの最新版、Gemini Nano Banana 2.1を公開した。
:::

同じページによると、良くなったのは画質、指示への忠実さ、何度もやり取りしても人物の見た目が変わらない一貫性、文字の描画の4点です。新たに1:8や8:1といった極端に横長・縦長の画像も作れるようになり、解像度は1K・2K・4Kから選べます。

## 料金は半額に、旧モデルは23日後に終了

開発者がシステムに組み込んで使う「Gemini API」の料金表では、Nano Banana 2.1の1枚あたりの価格は次のとおりです。

| 解像度 | Nano Banana 2.1 | Nano Banana 2 |
|---|---|---|
| 1K | $0.0336 | $0.067 |
| 2K | $0.0504 | $0.101 |
| 4K | $0.0756 | $0.151 |

どの解像度でもほぼ半額です。急がない処理をまとめて頼む「Batch」ならさらに半額で、1K画像は$0.0168になります。API経由の画像生成に無料枠はありません。

{{card:https://ai.google.dev/gemini-api/docs/pricing|Gemini Developer API pricing|Google AI for Developers}}

一方で、Nano Banana 2（gemini-3.1-flash-image）は非推奨になり、10月29日に提供を終えると変更履歴に書かれています。すでに組み込んでいる企業は、23日のうちにモデルを切り替える必要があります。

## どこで使えるか

Google検索の製品担当副社長Robby Stein氏はXで、検索の「AIモード」でNano Banana 2.1の提供を始めたと投稿しました。Googleアプリの検索窓の下にあるバナナのアイコンから使えるとしています。

{{x:https://x.com/rmstein/status/2107513543327412436}}

Nokiapoweruserは、AIモードのほかにGeminiアプリや動画制作ツールのFlowにも順次広がっていると報じています。Search Engine Roundtableは、検索結果の上に出る「AIによる概要」ではまだ古い版が使われているようだと伝えています。どの国から使えるかについて、Googleの説明は見当たりません。

## 背景

画像生成AIでは、ここ数週間で各社の新モデルが相次いでいます。広告向けの部分修正に強みを持たせたIdeogram 4.5（[既報](/news/20261002-ideogram-4-5-precise-edit/)）や、配置を枠で指定できるFLUX 3 Image（[既報](/news/20261002-black-forest-labs-flux-3-image/)）が出たばかりです。Googleは今回、性能の向上と同時に価格を下げ、大量に画像を作る企業の利用を取り込もうとしています。

なお、無料版のGeminiアプリは10月9日から軽量モデルのみの提供に変わり、画像生成も軽量版のNano Banana 2 Liteになります（[既報](/news/20261004-gemini-free-flash-lite-only/)）。Nano Banana 2.1がアプリの無料版でどこまで使えるかは、Googleから説明が出ていません。

## 日本のビジネスへの影響

- **使えるか**: Gemini APIのNano Banana 2.1は公開済みで、日本からも使えます。アプリや検索のAIモードでの日本での提供状況は、現時点で発表されていません。料金はドル建てです
- **誰にどう効くか**: バナーやSNS投稿の画像を大量に作る広告運用者・EC担当者に効きます。同じ人物やキャラクターを崩さずに何パターンも作れること、画像内の文字がきれいになることは、そのまま差し替え作業の手間の削減につながります
- **今すぐやれること**: Nano Banana 2をAPIで使っている場合は、モデル名を `gemini-nano-banana-2.1` に替えて同じ指示で出力を比べ、10月29日までに切り替えてください。費用はほぼ半分になります
- **注意点**: 画像内の日本語の文字がどこまで正確になったかは、Googleは具体的に示していません。広告に使う前に、商品名や価格の表記を必ず人の目で確かめてください

画像生成AIの選び方と料金は、[画像生成AIのおすすめと料金比較](/best/image-generation/)にまとめています。
