---
{
  "title": "ネット通販10万店にAI専用の売り場、買い物を頼まれたAIがボタンを探さずに商品をカートへ",
  "description": "BigCommerceなどを運営する米Commerceは10月21日、Cloudflareと組み、約10万のネット通販サイトにAIが直接使える「検索」「カートに入れる」の機能を一斉に用意したと発表した。店主はコードを書かずに済み、断ることもできる。",
  "date": "2026-10-21T23:30:00+09:00",
  "category": "marketing",
  "tags": ["Cloudflare", "WebMCP", "Commerce", "BigCommerce", "EC", "エージェント"],
  "summary": [
    "米CloudflareとBigCommerceの運営会社Commerceは、約10万のネット通販サイトでAIが使える専用の操作窓口を一斉に有効にした",
    "AIは画面のボタンを推測して押す代わりに「商品を探す」「カートに入れる」を直接呼び出せ、速く確実に買い物を進められる",
    "支払いの確定は人が自分で押す仕組みで、店主は管理画面のスイッチ1つでこの機能を断ることもできる"
  ],
  "sources": [
    {"title": "How Commerce.com and Cloudflare are getting storefronts ready for AI agents", "publisher": "Cloudflare Blog", "url": "https://blog.cloudflare.com/webmcp-commerce/", "kind": "公式発表"},
    {"title": "WebMCP is available for early preview", "publisher": "Chrome for Developers", "url": "https://developer.chrome.com/blog/webmcp-epp", "kind": "公式ドキュメント"},
    {"title": "Commerce", "publisher": "Commerce", "url": "https://www.commerce.com/", "kind": "公式サイト"},
    {"title": "Storefront MCP Is Now Live: Here's What You Can Build with It", "publisher": "BigCommerce", "url": "https://www.bigcommerce.com/blog/storefront-mcp/", "kind": "公式発表"},
    {"title": "Agentic Commerce", "publisher": "Cloudflare", "url": "https://www.cloudflare.com/solutions/agentic-commerce/", "kind": "公式ドキュメント"},
    {"title": "Google Releases Early Preview Of WebMCP", "publisher": "Search Engine Roundtable", "url": "https://seroundtable.com/google-webmcp-40918.html", "kind": "報道"}
  ],
  "thumb_prompt": "A miniature online-store shop counter where a tiny friendly robot shopper skips past a maze of confusing buttons and walks through a neat dedicated side door labeled only with a shopping-cart shape, carrying a small pair of running shoes.",
  "thumb_style": "diorama",
  "thumb_text": "WebMCP",
  "share_text": "ネット通販10万店に「AI専用の売り場」。AIはボタンを探さず商品を探してカートへ、支払いだけは人が押す",
  "editor_note": ""
}
---
ネット通販の構築サービス「BigCommerce」などを運営する米Commerceと米Cloudflareは現地時間10月21日、Commerceの約10万のドメインで動くネット通販サイトに、AIが直接使える買い物用の機能を一斉に用意したと発表しました。使ったのは、Googleが提案しているWebの新しい仕組み「WebMCP」です。

## 何が起きたか

いまのAIの「代わりに買い物をしてくれる機能」は、人と同じように画面を見て、どのボタンが何かを推測しながらクリックしています。Cloudflareは発表の冒頭で、この弱点をこう書いています。

:::quote https://blog.cloudflare.com/webmcp-commerce/ | Cloudflare Blog「How Commerce.com and Cloudflare are getting storefronts ready for AI agents」
> AI can write code and pass the bar exam, but it still struggles to buy a pair of shoes online.
AIはプログラムを書き、司法試験にも受かるのに、ネットで靴を1足買うのにはまだ苦労している。
:::

画面の推測に頼ると、時間がかかるうえ、AIの利用料もかさみます。サイトのデザインを少し変えただけで動かなくなることもあります。

WebMCPとは、Webサイトが「商品を探す」「カートに入れる」といった操作を、AI向けの決まった形の機能として用意しておける仕組みです。AIはボタンを探す代わりに、その機能を直接呼び出します。Cloudflareの例では「防水のトレイルランニングシューズを140ドル以下、サイズ10で探してカートに入れて」と頼むと、AIは「商品を探す」と「カートに入れる」の2回の呼び出しで済みます。クッキーの同意画面やサイズの選択欄、ロボット判定でつまずくことがなくなります。

### 店主は何もしなくてよい

今回の特徴は、店ごとの作業がいらない点です。CloudflareはCommerceのサイトの配信を担っており、ページを届ける途中で小さなプログラムを自動で差し込みます。店主がサイトのデザインを直したり、コードを書いたりする必要はありません。

一方で、全店に一律で入れると、望まない店も出てきます。そこでCloudflareは、Commerceの管理画面で店主が「使わない」をオンにすると、その店ではこの機能を外す仕組みを新たに作りました。外した店では表示速度も変わらないとしています。

### 支払いは人が押す

AIの操作は、買い物をする人自身のブラウザーの中で、その店のサイト上で行われます。AIが見る価格やカートは本人が見るものと同じで、ログイン情報などは第三者に渡りません。最後の購入ボタンは人が自分で押す設計です。

CommerceのプロダクトマネジメントディレクターのKristina Pototska氏は、店主から「AIによる買い物にどう追いつけばいいか」とよく聞かれると説明しています。客との関係と決済の主導権を手放さず、サイトを作り直さずに、AIの答えの中に自分の店が出るようにしたいという要望に応えたものだとしています。

## 背景

WebMCPは、Googleが2026年2月にChromeで試験提供を始めた提案中の仕組みです。現時点では、Chromeの試験用の設定や開発者向けの試験枠、一部のAIブラウザーでしか動きません。Cloudflareも「まだ初期の試験段階」と明記しています。

Commerceはこれとは別に、AIのサービスが店に直接つなぐ窓口（サーバー側の仕組み）もBigCommerceで提供しています。ブラウザーの中で動くAIにはWebMCP、外から店を回るAIにはサーバー側の窓口と、同じ買い物機能を2つの入口で用意する形です。

## 反応と論点

AIに買い物を任せる流れには、逆向きの動きもあります。AIデジマでは、米国の航空会社や銀行が「代理のAI」を締め出し始めた動きを[以前の記事](/news/20261019-websites-banks-block-ai-agents/)で伝えました。AIを入れたい店と、入れたくない店に分かれつつあります。

今回の仕組みが広く効くかは、利用者側のブラウザーやAIがWebMCPに対応するかにかかっています。標準として固まる前の仕組みなので、仕様が変わる可能性もあります。また、AIが店の用意した機能だけで商品を選ぶようになると、どの店の機能が使いやすいかで売れ行きが変わることも考えられます。

## 日本のビジネスへの影響

- **使えるか**: 今回の対象店の国や地域の内訳は発表に書かれておらず、日本の店がどれだけ含まれるかはわかりません。WebMCPに対応したブラウザーもまだ試験段階で、日本の買い物客が今すぐ恩恵を受ける段階ではありません。
- **誰にどう効くか**: EC担当者とWebマーケターに関係します。検索結果で上位を狙うSEOと同じように、「AIが使いやすい店かどうか」が集客を左右する時代の入口です。ShopifyやBigCommerceなど、使っている構築サービスがAI向けの窓口をどこまで用意しているかが、店側の差になります。
- **今すぐやれること**: 自社の通販サイトの構築サービスや配信サービスに、AI向けの機能（MCPやWebMCP）への対応予定を問い合わせておきましょう。あわせて、商品名・サイズ・価格・在庫といった商品データが正確にそろっているかを点検しておくと、AIに正しく選ばれやすくなります。
- **注意点**: 一律に有効にされる仕組みは、店主が知らないうちに入ることもあります。AI経由の注文が増えたときの不正注文の見分け方や、返品の扱いも事前に決めておくと安心です。

広告やマーケティングでのAIの選び方は、[用途別ガイド「広告・マーケティング向けAI」](/best/marketing/)にまとめています。
