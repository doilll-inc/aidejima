---
{
  "title": "Cloudflareが「Pay Per Use」を開始、AIが記事を使うたびにサイトへ対価",
  "description": "Cloudflareは、AI企業がサイトの記事を回答の引用などに実際に使った分だけ対価を払う仕組みPay Per Useのベータ版を始めた。価格はAI企業が提示し、運営者は受けるかを選ぶ。支払いは毎月で、設定はダッシュボードで完結する。",
  "date": "2026-10-01T18:00:00+09:00",
  "category": "marketing",
  "tags": [
    "Cloudflare",
    "Pay Per Use",
    "パブリッシャー",
    "SEO",
    "エージェント"
  ],
  "summary": [
    "CloudflareのPay Per Useは、AI企業が記事を回答などに使った回数に応じてサイト運営者に支払う仕組み",
    "AI企業が利用の定義と価格を提示し、運営者はダッシュボードで受けるか選ぶ。精算は毎月Cloudflareが代行",
    "利用回数はAI企業の自己申告で、参加するAI企業名や単価、支払実績はまだ公表されていない"
  ],
  "sources": [
    {
      "title": "Pay Per Use: when AI uses your work, you should get paid",
      "publisher": "Cloudflare Blog",
      "url": "https://blog.cloudflare.com/pay-per-use/",
      "kind": "公式発表"
    },
    {
      "title": "The Internet has a second audience",
      "publisher": "Cloudflare Blog",
      "url": "https://blog.cloudflare.com/agentic-web/",
      "kind": "公式発表"
    },
    {
      "title": "Monetization Gateway beta: charge AI agents for consumption with HTTP 402",
      "publisher": "Cloudflare Blog",
      "url": "https://blog.cloudflare.com/monetization-gateway-beta",
      "kind": "公式発表"
    },
    {
      "title": "What is Pay Per Crawl?",
      "publisher": "Cloudflare Docs",
      "url": "https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/",
      "kind": "公式ドキュメント"
    },
    {
      "title": "Cloudflare Moves Monetization Gateway & Pay Per Use Into Beta",
      "publisher": "Search Engine Journal",
      "url": "https://www.searchenginejournal.com/cloudflare-moves-monetization-gateway-pay-per-use-into-beta/591719/",
      "kind": "報道"
    }
  ],
  "thumb_text": "Pay Per Use",
  "share_text": "CloudflareがPay Per Useを開始。AIが記事を回答に使った分だけ、サイト運営者に毎月支払う",
  "thumb_style": "illustration",
  "thumb_prompt": "A small robot reading a newspaper at a café table and dropping a coin into a tip jar shaped like a website window each time it turns a page.",
  "editor_note": ""
}
---
Cloudflareは現地時間9月30日、AI企業がサイトの記事を実際に使った分だけ対価を払う仕組み「Pay Per Use」のベータ版を始めました。AI検索での引用などの利用をAI企業が1件ずつ報告し、Cloudflareが請求と支払いをまとめて代行します。サイト運営者への支払いは毎月です。

## 何が発表されたか

Pay Per Useとは、AI企業（買い手）が「何を利用とみなすか」と価格を決めて申し出て、サイト運営者が受けるかどうかを選ぶ仕組みです。2025年に始めた「Pay Per Crawl」は、AIのクローラー（自動でページを集めるプログラム）がページを取得するたびに課金します。今回はその先の「使われたとき」に支払いが発生する点が違います。

:::quote https://blog.cloudflare.com/pay-per-use/ | Cloudflare公式ブログ「Pay Per Use: when AI uses your work, you should get paid」
> Pay Per Crawl, which we launched in 2025, charges for access. Pay Per Use pays for what happens next.
2025年に始めたPay Per Crawlはアクセスに課金します。Pay Per Useは、その後に起きることに対して支払います。
:::

流れは4段階です。

1. AI企業がクローラーを登録し、支払い対象の利用と価格、支払い口座を設定する
2. 運営者はダッシュボードの「Monetize → Pay Per Use」で、AI企業名・対象の利用・提示価格を見て受けるか決める。参加はいつでもやめられ、サーバーの改修や各社との個別連携はいらない
3. AI企業は、利用1件ごとに日時・元のURL・イベントIDをAPIで報告する
4. Cloudflareが集計して買い手に請求し、運営者には毎月支払う

Cloudflareは利用の例として、検索サービスが記事の抜粋を利用者に返したとき、買い物エージェントがレビューを推薦の判断に使ったときを挙げています。後者は、買い物客がレビューを読まなくても支払いが発生します。学習への利用を制限するかどうかなども、プログラムごとの規約で決まります。ダッシュボードでは、AI企業別・ドメイン別に利用回数と見込みの収益を確認できます。

{{card:https://blog.cloudflare.com/pay-per-use/|Pay Per Use: when AI uses your work, you should get paid|Cloudflare Blog}}

同じ日には、APIやデータへのリクエストごとにAIエージェントへ課金する「Monetization Gateway」も、米国の売り手と買い手に限ったクローズドベータとして始まりました。3つの仕組みの違いは次のとおりです。

| 仕組み | 支払いのきっかけ | 価格を決める側 | 提供状況 |
|---|---|---|---|
| Pay Per Crawl | ページの取得ごと | サイト運営者 | クローズドベータ |
| Pay Per Use | AIが実際に使ったとき | AI企業（運営者は受けるか選ぶ） | ベータ |
| Monetization Gateway | APIなどへのリクエストごと | 売り手 | 米国限定のクローズドベータ |

## 背景

Cloudflareは同日の別の投稿で、AIエージェントからの1日あたりのリクエストが過去1年で1,700%超増え、今年初めてインターネットの通信の半分以上が人間以外になったと説明しました。AI学習を目的とするクローラーのリクエストは、2025年春の22%から2026年6月には52%に増えています。よくクロールされる小売やソフトウェアなどの分野では、人間の訪問が1年足らずで最大40%減ったといいます。

2023年以降、パブリッシャーとAI企業の契約は50件を超えましたが、ほとんどが大手同士の個別契約です。Pay Per Useは、個別契約を結べない多数のサイトに支払いの経路を作る狙いです。Cloudflareは7月、AIクローラーへの設定を「検索」「エージェント」「学習」に分け、無料プランを含む全プランで使えるようにしました。GoogleもAI回答への対価を試験的に払い始めていますが、対象は約100社にとどまると報じられています（[関連記事](/news/20260930-google-ai-overviews-publisher-payments/)）。

## 反応と論点

最大の論点は、利用回数の数え方です。Cloudflareは報告の仕組みを次のように説明しています。

:::quote https://blog.cloudflare.com/pay-per-use/ | Cloudflare公式ブログ「Pay Per Use: when AI uses your work, you should get paid」
> Usage is self-reported: the program terms require complete reporting, and Cloudflare checks that each reported use maps to an enrolled publisher.
利用は自己申告です。プログラムの規約は漏れのない報告を求めており、Cloudflareは報告された各利用が登録済みのパブリッシャーに対応しているかを確認します。
:::

Search Engine Journalは、Cloudflareがベータに参加するAI企業の名前を明かしておらず、取引件数や支払額も公表していないと報じています。価格を決めるのはAI企業側で、運営者が値段を逆提案したり、新しい記事と古い記事で価格を変えたりする機能は今後の課題とされています。

## 日本のビジネスへの影響

公式ブログには、Pay Per Useに参加できる国や料金プランの条件が書かれていません。米国限定と明記されているのはMonetization Gatewayのほうです。Cloudflareを使う日本のサイトなら、まずダッシュボードに「Monetize → Pay Per Use」と申し出が出ているかを確かめるのが第一歩です。

関係が深いのは、ニュースや専門情報を出すメディアと、オウンドメディアやSEOの担当者です。今すぐできるのは、AI Crawl Controlでどのクローラーが何を取得しているかを見たうえで、「検索は許可、学習は拒否」のように3種類の設定を決めておくことです。

注意点は、価格も利用回数もAI企業側が出す数字だということです。受ける前に、規約で学習への利用がどう扱われるかを必ず読んでください。円での受け取りや手数料も発表されていません。AI検索の比較は[調べもの・リサーチに強いAIのおすすめ](/best/research/)にまとめています。
