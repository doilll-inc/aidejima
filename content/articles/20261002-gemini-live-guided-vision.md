---
{
  "title": "Gemini Liveに視覚障害者向けの「Guided Vision」、カメラの向きも声で指示",
  "description": "GoogleはGemini Liveに、カメラに映るものを声で説明し、撮り方も「右へゆっくり」などと指示するGuided Visionを追加した。Android 9以降が対象で、日本の視覚障害者コミュニティも開発時の検証に加わった。",
  "date": "2026-10-02T11:50:00+09:00",
  "category": "products",
  "tags": ["Google", "Gemini Live", "Guided Vision", "アクセシビリティ", "新機能", "スマートフォン"],
  "summary": [
    "GoogleはGemini Liveに、カメラ映像を声で説明するGuided Visionを10月1日から提供した",
    "Guided Visionは映りが悪いと「右へ」「下へ傾けて」などと撮り直しを声で促し、Android 9以降で使える",
    "開発ではAiraと組み、1,000人超の試験者が検証した。Googleは移動の補助には使えないと明記している"
  ],
  "sources": [
    {"title": "Guided Vision in Gemini Live: built for accessibility", "publisher": "Google", "url": "https://blog.google/innovation-and-ai/products/gemini-app/guided-vision-gemini-live/", "kind": "公式発表"},
    {"title": "Guided Vision（Android ユーザー補助ヘルプ）", "publisher": "Google ヘルプ", "url": "https://support.google.com/accessibility/android/answer/18365638?hl=en", "kind": "公式ドキュメント"},
    {"title": "Gemini Live's camera just became much more useful for accessibility", "publisher": "Android Authority", "url": "https://www.androidauthority.com/gemini-live-guided-vision-launch-3718122/", "kind": "報道"},
    {"title": "Google's new Guided Vision feature can help you read the fine print", "publisher": "The Verge", "url": "https://www.theverge.com/ai-artificial-intelligence/1003756/google-gemini-live-guided-vision", "kind": "報道"}
  ],
  "thumb_text": "Guided Vision",
  "share_text": "Gemini Liveに視覚障害者向けGuided Vision。映った物を説明し、撮り方も声で指示",
  "thumb_style": "photo",
  "thumb_prompt": "A person seen from behind holding a smartphone up in a sunny street, the phone camera view shown with glowing guiding arrows pointing to the right, a white cane resting in their other hand.",
  "editor_note": ""
}
---
Googleは現地時間10月1日、AIと音声で会話する「Gemini Live」に、カメラに映るものをリアルタイムに声で説明する「Guided Vision」を追加しました。目の見えない人やロービジョン（弱視）の人を主な対象にした機能で、Android 9以降の端末で使えます。映りが悪いときは、Geminiのほうから「ゆっくり右へ」「少し下に傾けて」と撮り方を声で指示するのが特徴です。

## 何が発表されたか

Guided Visionとは、Gemini Liveでカメラを共有すると、周りの様子を声で説明し、追加の質問に答え、見たいものが画面の中央に来るよう声で誘導する機能です。Googleの公式ブログは、Gemini Liveの担当シニアプロダクトマネージャーであるイシャ・シェス氏の名前で公開されました。

:::quote https://blog.google/innovation-and-ai/products/gemini-app/guided-vision-gemini-live/ | Google公式ブログ「Guided Vision in Gemini Live: built for accessibility」
> Today, we’re launching Guided Vision in Gemini Live across compatible Android devices — bringing voice-forward, real-time visual interpretation to people who are blind, have low vision, or want intuitive visual assistance.
本日、対応するAndroid端末のGemini LiveでGuided Visionの提供を始めます。目の見えない人、ロービジョンの人、直感的な視覚の手助けがほしい人に、声を中心にしたリアルタイムの視覚の解釈を届けます。
:::

Googleが挙げた使いみちは4つです。

| 用途 | 公式ブログの例 |
|---|---|
| 細かい文字を読む | 食品の栄養成分表示、洗濯機のダイヤル、暗い店内のメニュー |
| 物を探す | 床に落ちたイヤホン、混み合った棚の中のこしょう |
| 色や柄を確かめる | 縞のシャツとズボンが合うか、上着の色 |
| 周りを把握する | 初めての部屋の配置、テーブルに置かれた物 |

起動の方法は3通りあります。Geminiアプリのプロフィール設定で「Use Guided Vision in Live」をオンにしてGemini Liveでカメラを共有する方法、Androidのユーザー補助のショートカット（フローティングボタン、2本指のスワイプ、音量キーの同時押し）に割り当てる方法、画面読み上げのTalkBackのメニューから選ぶ方法です。Googleのヘルプページによると、提供は時間をかけて少しずつ広げるとしています。

{{card:https://support.google.com/accessibility/android/answer/18365638?hl=en|Guided Vision（Android ユーザー補助ヘルプ）|Google ヘルプ}}

## どう作られたか

開発には、視覚障害者向けに遠隔で視覚の通訳をするサービスのAiraが協力しました。公式ブログによると、Airaは数万時間分のデータを視覚の観点から解釈し、Airaの試験者ネットワークの1,000人以上が日常の場面で機能を試して改善しました。Airaの専門家は、安全のための制限の設計と評価にも加わっています。

多言語での検証も強調しています。インド、ブラジル、シンガポール、インドネシア、日本などの視覚障害者コミュニティによる試験と意見を反映し、説明や撮り直しの指示、答えが自然に聞こえるようにしたとしています。Android Authorityによると、Googleは9月にこの機能を先行して見せ、「近日提供」としていました。

## 限界と注意書き

Googleは使ってはいけない場面をはっきり書いています。

:::quote https://blog.google/innovation-and-ai/products/gemini-app/guided-vision-gemini-live/ | Google公式ブログ「Guided Vision in Gemini Live: built for accessibility」
> It is not a medical device, mobility aid, or white cane replacement, and it’s not intended for navigation, safe-travel guidance, or obstacle detection.
これは医療機器でも移動の補助具でも白杖の代わりでもなく、道案内や安全な移動の誘導、障害物の検知を目的としたものでもありません。
:::

生成AIは見間違いをします。文字の読み取りや色の判定はおおむね任せられても、薬の用量や賞味期限のように間違いが許されない場面では、人や専用の機器で確かめる運用が前提になります。公式ブログもヘルプページも、誤りがありうると明記しています。

## 背景

Gemini Liveは、カメラや画面を共有しながらAIと声で話せる機能として広がってきました。今回の新しさは、その中に「撮り方の指示」と「会話での追加の質問」を1つの流れとして組み込んだ点です。AIが今見えているものを判断し、利用者にカメラを動かしてもらうやりとりは、画面を見られない人にとって特に意味があります。公式ブログは、高齢の人や読み書きが苦手な人、暗い場所で小さな文字を読みたい人にも役立つとしています。

GeminiはAIデジマでも、よく使う指示を保存して呼び出せる「スキル」の追加を伝えたばかりです（[Geminiに「スキル」が登場](/news/20261001-gemini-skills/)）。Googleは、アプリの機能追加を毎週のように重ねています。

## 日本のビジネスへの影響

- **使えるか**: 公式ブログは「Gemini Liveが提供されている地域と言語で使える」としています。開発時の検証には日本のコミュニティも加わり、ヘルプページの言語の選択肢にも日本語があります。ただし提供は段階的なので、すぐに設定に出ない端末もあります。料金の案内はなく、iPhone版の予定も公式には示されていません。
- **誰にどう効くか**: 関係が深いのは、店舗・飲食・メーカーのアクセシビリティ担当と商品パッケージの担当者です。視覚障害のある客が自分のスマホのAIで成分表示やメニューを読む場面が増えると、文字の小ささやコントラスト、光沢のある包材の反射が読み取りやすさを左右します。
- **今すぐやれること**: 自社の商品パッケージ、店内メニュー、取扱説明書をGuided Visionで読ませて、正しく読めるか試します。読み間違いが出た箇所は、文字の大きさや配色を見直す材料になります。チャットAI全体の選び方は[チャットAIのガイド](/best/chat/)にまとめています。
- **注意点**: 社内の支援策として紹介する場合も、Googleが明記しているとおり、移動の誘導や安全確認には使わない前提を伝えます。職場で使う場合は、Geminiアプリのデータの扱いを確認したうえで、顧客情報や社内資料を映さないルールを決めておくと安全です。
