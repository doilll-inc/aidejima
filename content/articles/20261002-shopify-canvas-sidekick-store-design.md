---
{
  "title": "Shopifyが「Canvas」を公開、AIのSidekickと会話しながらストア全体を作り直せる",
  "description": "Shopifyは10月1日、ストアの全ページを1枚の作業画面に並べ、AIエージェントのSidekickと会話しながらデザインできる「Canvas」を発表した。Sidekickは2026年上半期だけでテーマを2,500万回以上編集している。数日かけて順次提供する。",
  "date": "2026-10-02T03:55:00+09:00",
  "category": "marketing",
  "tags": ["Shopify", "Canvas", "Sidekick", "EC", "エージェント", "LP"],
  "summary": [
    "ShopifyはストアのデザインをAIのSidekickと進める新しい編集画面Canvasを発表し、数日かけて順次提供する",
    "Canvasは全ページを1枚に並べ、プレビューではなく実際のテーマのコードを表示する。Sidekickはコードを直接書き換える",
    "公開時点では他社製テーマ、アプリのブロック、Markets、翻訳に非対応で、Canvasで編集したテーマは更新を受け取れない"
  ],
  "sources": [
    {"title": "Introducing Canvas: Opening the aperture on online store design", "publisher": "Shopify", "url": "https://www.shopify.com/news/introducing-canvas", "kind": "公式発表"},
    {"title": "Design a fully bespoke store with Canvas", "publisher": "Shopify Changelog", "url": "https://changelog.shopify.com/posts/design-a-fully-bespoke-store-with-canvas", "kind": "公式ドキュメント"},
    {"title": "Meet Canvas: a new way for merchants to design their online store with Sidekick.", "publisher": "Shopify Developer Community Forums", "url": "https://community.shopify.dev/t/meet-canvas-a-new-way-for-merchants-to-design-their-online-store-with-sidekick/38212", "kind": "公式ドキュメント"},
    {"title": "Shopify debuts Canvas, a way to build online stores by chatting with AI", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/10/01/shopify-debuts-canvas-a-way-to-build-online-stores-by-chatting-with-ai/", "kind": "報道"}
  ],
  "thumb_text": "Shopify Canvas",
  "share_text": "ShopifyがCanvasを公開。全ページを1枚に並べ、AIのSidekickと会話しながら実際のテーマのコードを書き換える",
  "thumb_style": "illustration",
  "thumb_prompt": "An online shop's pages laid out like paper cards on one large canvas table, with a friendly little robot assistant holding a paintbrush and rearranging them.",
  "editor_note": ""
}
---
Shopifyは現地時間10月1日、ネットショップのデザインをAIエージェント「Sidekick」と会話しながら進める新しい編集画面「Canvas」を発表しました。ストアの全ページを1枚の作業画面に並べ、Sidekickが実際のテーマのコードを書き換えていく仕組みで、数日かけて既存のストアに順次提供します。Sidekickは2026年上半期だけで、テーマの編集を2,500万回以上こなしてきたといいます。

## 何が発表されたか

Canvasとは、Shopifyのネットショップの全ページを並べて見渡し、手作業とAIの両方で作り込めるデザイン用の作業画面です。拡大・縮小しながら全体の雰囲気と細部を行き来できます。部品をクリックして直接直すこともでき、設定画面を探す代わりにSidekickに頼むこともできます。Sidekickの変更はその場でCanvasに反映されます。

画面に出るのは静止画のプレビューではありません。

:::quote https://www.shopify.com/news/introducing-canvas | Shopify公式「Introducing Canvas」
> In Canvas, Merchants aren’t editing a static preview, but a render of the real code behind the store they’re building with Sidekick.
Canvasで販売者が編集しているのは静止したプレビューではなく、Sidekickと作っているストアの実際のコードを描画したものです。
:::

このため、動きやアニメーションまで含めて確認でき、商品やコレクション、画面サイズを切り替えて主要なページを見比べられます。

Sidekickの側にも手が入りました。テーマのファイルを直接編集し、ストア作りのための指示とスキルに沿って作業します。Shopifyはテーマの構造自体も単純にし、Sidekickが理解・変更しやすくしました。作業中は自分の書いたコードを検証し、Canvasのスクリーンショットを撮って仕上がりを確かめ、直してから販売者に返します。好みやそれまでのデザイン判断も覚えていて、同じ説明を繰り返さずに済むといいます。

Shopifyのプロダクトディレクターで、アパレルブランドKotnの共同創業者でもあるBen Sehl氏は、12年前にKotnの粗い試作を作るのに2週間かかったのに対し、今は20分で完全にオリジナルのストアを作れると述べています。

## 何ができないか

Shopifyは公開時点の制限をはっきり書いています。変更履歴（Changelog）によると、Canvasは次の機能にまだ対応していません。

- Shopifyテーマストアの他社製テーマ
- Markets（国・地域ごとの出し分け）、ロールアウト、翻訳
- アプリのブロックと埋め込み（app blocks / app embeds）

さらに、Canvasで編集したテーマはテーマの更新を受け取れなくなります。使い始めるには、管理画面の「オンラインストア」→「テーマ」から、新しいテーマを作るか既存のテーマを複製します。

{{card:https://changelog.shopify.com/posts/design-a-fully-bespoke-store-with-canvas|Design a fully bespoke store with Canvas|Shopify Changelog}}

Sehl氏も公式発表の中で、Canvasはまだ既存の編集画面（テーマエディター）の置き換えではなく、埋めるべき穴があると認めています。TechCrunchは、当初はパソコンでのみ使えると報じています。

## 背景

これまでShopifyで独自のデザインを作るには、自分でコードを書くか、制作会社に頼むか、細かな設定画面と格闘するしかありませんでした。Sidekickは以前からアプリやテーマの部品を作ってきましたが、ストア全体の作り直しには、テンプレートとファイルをまたいだ一貫した変更と、その結果の確認が必要でした。CanvasはSidekickを、そこまで担える「コマース向けのコーディングエージェント」にする試みです。

設計面では、AIに良いデザインを選ばせることが難しかったようです。デザインディレクターのAustin Knight氏は、コードを書かせるのは簡単だったが、良いデザイン判断に導くには多くの時間がかかったと説明しています。テーマごとにデザインの決まりと、使える型の一覧、評価用のデータを用意したといいます。

## 反応と論点

開発者の受け止めは割れています。Shopifyは開発者フォーラムで、Canvasで作ったり複製したりしたテーマではアプリのブロックと埋め込みが使えず、アプリ側がテーマ一覧を取ってもそのテーマは出てこないと告知しました。これに対し、アプリ開発者からは「販売者に警告は出るのか」「アプリが動かないという問い合わせが殺到する」と心配する書き込みが続きました。Shopifyの担当者は、数週間のうちにテーマのアプリ拡張に対応する予定だと答えています。

テーマの更新を受け取れない点も、長く運用するストアには重い制約です。会話で作ったコードがどこまで保守しやすいかは、まだ誰にも分かりません。

## 日本のビジネスへの影響

- **使えるか**：既存のストアに順次提供すると発表されていますが、提供地域やプラン、日本語での会話の精度は公式発表に書かれていません。日本の販売者の管理画面に出るかは、各自で確認する必要があります
- **誰に効くか**：自社ECをShopifyで運営するマーケターと、制作会社に頼まずに季節ごとの特集ページを作りたい担当者です。Shopifyのテーマ制作やアプリ開発を請け負う制作会社にとっては、仕事の中身が変わる可能性があります
- **今すぐやれること**：本番のテーマには触らず、Canvasで既存テーマを複製して特集ページを1枚作り直し、従来の制作にかかる時間と比べてみてください。LP制作に使える他のAIツールは[広告・マーケティング向けAIのガイド](/best/marketing/)で比べています
- **注意点**：アプリのブロックで動くレビューや定期購入などの機能は、Canvasのテーマでは表示されません。複数の国向けに出し分けているストアや、多言語のストアも、対応を待つ方が安全です
