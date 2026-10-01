---
{
  "title": "RedditがRSSを11月13日で終了、公開APIも2027年3月に閉じ自動取得を締め出す",
  "description": "Redditは、大規模なスクレイピングの入り口になっているとしてRSSフィードを11月13日で終了し、外部アプリ向けの公開データAPIも2027年3月にすべて閉じると発表した。ソーシャルリスニングや口コミ収集の仕組みは見直しが必要になる。",
  "date": "2026-10-01T15:09:00+09:00",
  "updated": "2026-10-01T18:55:00+09:00",
  "category": "marketing",
  "tags": ["Reddit", "API", "SNS", "開発者", "マーケティング"],
  "summary": [
    "RedditはRSSフィードを2026年11月13日で終了し、モデレーター以外の用途には代わりの手段がないと説明した",
    "公開データAPIは10月31日に新規申請を締め切り、2027年1月12日から未登録のアプリを順に止め、3月に全面終了する",
    "外部アプリはReddit上で動く開発者プラットフォームへの移行が必要で、登録済みは1万4000件を超えた"
  ],
  "sources": [
    {"title": "Continuing our infrastructure updates: What’s changing in the coming months", "publisher": "Reddit（r/modnews）", "url": "https://www.reddit.com/r/modnews/comments/1wubgvt/continuing_our_infrastructure_updates_whats/", "kind": "公式発表"},
    {"title": "Moving Data API Apps to the Developer Platform: migration dates and next steps", "publisher": "Reddit（r/redditdev）", "url": "https://www.reddit.com/r/redditdev/comments/1wubcvf/moving_data_api_apps_to_the_developer_platform/", "kind": "公式発表"},
    {"title": "Our Plans for the Future of Reddit’s Public Data API and the Developer Platform", "publisher": "Reddit（r/redditdev）", "url": "https://www.reddit.com/r/redditdev/comments/1vgbm9c/our_plans_for_the_future_of_reddits_public_data/", "kind": "公式発表"},
    {"title": "Protecting communities from scrapers and platform abuse", "publisher": "Reddit（r/modnews）", "url": "https://www.reddit.com/r/modnews/comments/1tq9vxo/protecting_communities_from_scrapers_and_platform/", "kind": "公式発表"},
    {"title": "Reddit Reports Second Quarter 2026 Results", "publisher": "Reddit Investor Relations", "url": "https://investor.redditinc.com/news-events/news-releases/news-details/2026/Reddit-Reports-Second-Quarter-2026-Results/default.aspx", "kind": "公式発表"},
    {"title": "Reddit is killing RSS feeds and ending public API access because of AI bots", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/09/30/reddit-is-killing-rss-feeds-ending-public-api-access-because-of-ai-bots/"}
  ],
  "thumb_text": "RSSと公開API",
  "thumb_kicker": "Reddit",
  "share_text": "RedditがRSSを11月13日で終了、公開APIも2027年3月に全面終了。口コミ収集やソーシャルリスニングは見直しが必要に",
  "editor_note": ""
}
---
Redditは現地時間9月30日、RSSフィードの提供を11月13日で終了し、外部のアプリやツールが使ってきた公開データAPIも2027年3月にすべて閉じると発表しました。RSSが大規模なスクレイピング（プログラムによる自動収集）と不正利用の入り口になっていることを理由に挙げています。外部アプリには、Reddit上で動く開発者プラットフォームへの移行を求めます。

## 何が発表されたか

発表は、モデレーター（各コミュニティの管理人）向けのr/modnewsと、開発者向けのr/redditdevへの公式投稿で行われました。RSSとは、サイトの新着をアプリで購読するための標準的な配信形式です。Redditは終了の理由を次のように説明しています。

:::quote https://www.reddit.com/r/modnews/comments/1wubgvt/continuing_our_infrastructure_updates_whats/ | Reddit公式投稿（r/modnews）「Continuing our infrastructure updates: What’s changing in the coming months」
> Because RSS is now a common surface for large-scale scraping and automated abuse, we'll stop supporting RSS feeds on November 13, 2026 while preserving moderation workflows that depend on it through supported alternatives.
RSSは大規模なスクレイピングと自動化された不正利用によく使われる入り口になったため、2026年11月13日でRSSフィードの提供を終えます。RSSに頼るモデレーション作業は、公式に対応した代わりの手段で引き続き支えます。
:::

モデレーターの通知用途には、Discordへ転送するアプリ「Discord Relay」を勧めています。一方、自分が管理していないコミュニティの購読など、それ以外の用途には代わりの手段はないと明言しました。

公開データAPIは段階的に閉じます。

| 日付 | 内容 |
|---|---|
| 2026年10月31日 | 公開APIの新規利用申請の受付を終了 |
| 2026年11月30日 | 移行支援の報奨金プログラムの登録締め切り |
| 2027年1月12日 | 未登録・連絡のないアプリと利用者からアクセスを順に停止 |
| 2027年3月 | 残るすべての公開APIアクセスを終了 |

移行先の開発者プラットフォーム（Devvit）は、アプリをRedditの基盤の上で動かす仕組みです。これまでに1万4000件超のアプリとボットが登録しました。Redditは総額100万ドルの移行支援を用意し、移行を終えた対象アプリに1件1,000ドルを払います。

このほか、旧デザインの「Old Reddit」は、数か月以内にモデレーターと、過去6か月以内に使ったログイン中の利用者だけに絞ります。TechCrunchによると、この期間は当初90日とされ、発表の直前に6か月へ延びました。新しく作られたコミュニティや自動モデレーション機能を使ったことのないコミュニティでは、その取り締まり操作を無効にします。

## 背景

Redditは段階的に外部からの機械的なアクセスを絞ってきました。5月にはログインせずにJSON形式でデータを取得できる窓口を閉じると告知し、RSSの使い道をモデレーターに尋ねていました。8月5日には、公開データAPIは今の規模や不正利用、商用目的の収集を想定して作られていないとして、外部アプリを開発者プラットフォームへ移す方針を示しています。

背景にはデータの価値があります。7月の決算では、総売上が前年比61%増の8億500万ドルで、広告以外の「その他の売上」は24%増の4300万ドルでした。TechCrunchはこの数字を挙げ、掲示板にたまった投稿がAI企業へのデータ提供契約を通じて収益源になっていると説明しています。お金になるデータを無料の窓口から持ち出させないことが、今回の措置の経済的な意味だと編集部は見ています。AIによる要約と元の情報源の関係は、[GoogleのAI回答への対価を巡る記事](/news/20260930-google-ai-overviews-publisher-payments/)でも扱いました。

## 反応と論点

影響を受けるのは、大きく分けて3つの層です。1つ目はモデレーターで、5月にRSS終了の可能性が示された時点で、管理が立ち行かなくなるという不満が出ていたとTechCrunchは伝えています。2つ目はRSSリーダーでRedditを読んできた一般の利用者で、こちらには代わりの手段が用意されません。

3つ目が、公開APIでRedditの会話を取り込んできた外部のサービスです。TechCrunchは、ソーシャルリスニング（SNS上の評判分析）製品、研究者向けのツール、Redditを参照して答えるAIアシスタントを挙げ、今後はRedditとの商用契約が必要になると報じています。無料の取得口を閉じて有料の契約へ誘導する点で、背景にあるデータ提供事業と同じ方向の動きです。

## 日本のビジネスへの影響

今回の変更は全世界が対象で、日本の企業や利用者にもそのまま当てはまります。影響が大きいのは、Redditの英語圏の口コミを集めて海外向けの商品開発や評判分析に使っているマーケターと、SNS監視ツールを運用する担当者です。

今すぐやるべきは棚卸しです。RSSリーダーやSlack、Feedlyなどで購読しているRedditのフィードは、11月13日に止まります。Redditの投稿を取り込むソーシャルリスニングツールを使っているなら、提供元がRedditと正式なデータ契約を結んでいるか、2027年3月以降も取得できるかを確認してください。自社でAPIを使うツールを作っている場合は、1月12日より前にアプリを登録する必要があります。

注意点として、RSSやAPIの代わりにページを機械的に読み取る方法は避けるべきです。Redditは5月にサイト利用のルールを改め、自動化された不正利用やAPIの不正使用を違反の対象として明記しています。なお、検索結果でのRedditの表示について、今回の発表は触れていません。SNS運用に使えるAIツールの比較は、[広告・マーケティング向けAIのおすすめ](/best/marketing/)にまとめています。
