---
{
  "title": "AIで作った他人の裸の画像を消さないアプリはApp Storeから削除、Appleが審査ルールを強化",
  "description": "Appleは10月16日、App Storeの審査ガイドラインを改め、AIで作られた本人の同意のない性的な画像を、アプリ側が自ら防いで削除することを明記した。審査後に機能を足す「すり替え」アプリは開発者登録ごと取り消す。昨年は15万本超のアプリを公開前に止めたという。",
  "date": "2026-10-18T00:55:00+09:00",
  "category": "policy",
  "tags": ["Apple", "App Store", "ディープフェイク", "安全性", "規制", "Grok"],
  "summary": [
    "Appleは10月16日、App Storeの審査ルールを改め、AIで作った同意のない性的な画像を防いで消す義務をアプリに課した",
    "審査に出した後で服を脱がせる機能などを足す「すり替え」アプリは、ストアから外し開発者の登録も取り消す",
    "Appleは昨年、安全上の問題がある15万本超のアプリを公開前に止め、19.3万超の開発者アカウントを停止したとしている"
  ],
  "sources": [
    {"title": "Strengthening App Review Guidelines against nonconsensual intimate imagery and bait-and-switch apps", "publisher": "Apple Developer News", "url": "https://developer.apple.com/news/?id=vvzx6cul", "kind": "公式発表"},
    {"title": "App Review Guidelines", "publisher": "Apple Developer", "url": "https://developer.apple.com/app-store/review/guidelines/", "kind": "公式ドキュメント"},
    {"title": "Apple announces changes to iOS in Japan", "publisher": "Apple Newsroom", "url": "https://www.apple.com/newsroom/2025/12/apple-announces-changes-to-ios-in-japan/", "kind": "公式発表"},
    {"title": "Apple updates App Store rules to ensure it doesn't offer AI nudify apps", "publisher": "Engadget", "url": "https://www.engadget.com/2289567/apple-updates-app-store-rules-ai-nudify-apps/", "kind": "報道"},
    {"title": "New App Store Rules Target AI Deepfakes and Nudify Apps", "publisher": "MacRumors", "url": "https://www.macrumors.com/2026/10/16/app-store-rules-deepfakes/", "kind": "報道"},
    {"title": "Apple and Google Hit With Demand to Pull AI 'Nudify' Apps", "publisher": "MacRumors", "url": "https://www.macrumors.com/2026/07/17/demand-to-pull-nudify-apps/", "kind": "報道"}
  ],
  "thumb_text": "App Store",
  "thumb_style": "photo",
  "thumb_prompt": "A smartphone lying on a desk whose app icons are being swept off the screen by a tiny janitor's broom, while one innocent-looking camera app icon hides a cracked mask behind it.",
  "share_text": "AIで他人の裸の画像を作れてしまうアプリ、防がなければApp Storeから削除へ。審査後の機能すり替えは開発者登録も取り消し",
  "editor_note": ""
}
---
Appleは現地時間10月16日、App Storeの審査ガイドライン（アプリを載せるための規則）を改め、AIで作られたものを含む「本人の同意のない性的な画像」を、アプリ側が自ら防いで削除しなければならないと明記しました。審査を通った後で裸にする機能などを出してくる「すり替え」アプリは、ストアから外したうえで開発者登録も取り消します。Appleは昨年だけで、安全上の問題がある15万本超のアプリを利用者に届く前に止めたとしています。

## 何が変わったか

対象は、他人の写真から裸の画像を作る、いわゆる「ヌーディファイ（脱衣）」アプリと、利用者が画像や動画を投稿できるアプリ全般です。Appleは開発者向けのお知らせで、変更点を3つに分けて説明しています。

| 規則の番号 | 変更の中身 |
|---|---|
| 1.2（利用者の投稿） | AIで作った画像を含む同意のない性的な画像を、アプリが自ら防ぎ、消すべきものと明記。対策が足りない、または通知後も直さない開発者はストアから外される |
| 2.5.19（新設） | 審査に出した版と違う機能を承認後に足すことを禁止。見つかればストアから削除し、開発者プログラムからも除名 |
| 5（法律） | 人身売買や子どもへの性的搾取に関わるアプリは、ストアからの削除に加え、App Store以外の配布経路でも配れなくする |

もともとApp Storeはポルノを禁じており、脱衣アプリも以前から規則違反でした。今回の変更は「作るアプリを禁止する」から一歩進み、画像を投稿できる普通のアプリにも、見張って消す責任を負わせた点が大きな違いです。

:::quote https://developer.apple.com/news/?id=vvzx6cul | Apple Developer News「Strengthening App Review Guidelines against nonconsensual intimate imagery and bait-and-switch apps」
> Content moderation requirements now explicitly cover nonconsensual intimate imagery — including imagery generated using AI tools — as content that apps must proactively prevent and remove from their platforms.
投稿内容の管理に関する要件は、AIツールで生成されたものを含む同意のない性的な画像を、アプリが自ら防ぎ、プラットフォームから削除すべきコンテンツとして明確に対象に含めるようになった。
:::

規則の全文は、Appleの審査ガイドラインのページで公開されています。

{{card:https://developer.apple.com/app-store/review/guidelines/|App Review Guidelines|Apple Developer}}

## なぜ「すり替え」を名指ししたのか

Appleによると、問題のアプリの多くは、審査のときには無害な写真加工アプリなどを装い、承認された後で脱衣機能を有効にしていました。Appleはこれを「bait-and-switch（おとり商法）」と呼び、一部は組織的な詐欺グループによるものだと説明しています。昨年は安全上の問題で15万本超のアプリの公開を止め、不正や悪用を理由に19.3万超の開発者アカウントを停止したといいます。

背景には、この1年で続いた外からの圧力があります。MacRumorsは、米サンフランシスコ市の検事局が7月、AppleとGoogleに対し、顔を入れ替えて裸の画像を作れるアプリ計13本（App Store 8本、Google Play 5本）の削除と、アプリ内課金の手数料を受け取るのをやめるよう求める書面を送ったと報じています。Appleはこのうち3本を削除して開発者アカウントを止め、ほかの4つの開発者にも是正を求めたと同誌に説明していました。

MacRumorsはまた、AppleがxAIの対話AI「Grok」で性的なディープフェイク（本物に見える偽の画像）が作られていた問題を受け、4月にxAIへ「対策しなければApp Storeから外す」と伝えていたとも報じています。Grokは対策を加えた版が承認されています。今回の1.2の変更がGrokのような汎用のAIアプリも念頭に置いているかについて、Appleは名指ししていません。

## 反応と論点

MacRumorsの記事についた読者のコメントでは、脱衣アプリはWebでも簡単に見つかるのでApp Storeだけ締めても効果は限られるという指摘と、Appleのストアに置くこと自体がお墨付きに見えるので厳しくして当然だという意見に分かれています。

論点は、画像を投稿・生成できる一般のアプリにどこまで監視を求めるかです。1.2の文言は「自ら防ぐ（proactively prevent）」とあり、通報を待つだけでは足りないと読めます。画像生成AIを組み込んだアプリやSNS型のアプリは、生成時と投稿時の両方でフィルターを設ける必要が出てきます。一方、どの程度の対策なら「十分」とみなされるのか、具体的な基準はお知らせには書かれていません。

## 日本のビジネスへの影響

- **使えるか**: 審査ガイドラインは世界共通で、日本のApp Storeにもそのまま適用されます。日本では2025年12月からスマホ新法に合わせてApp Store以外の配布（代替アプリマーケットプレイス）も認められており、5の変更は、そうした経路でも子どもの性的搾取に関わるアプリを配らせないという意味を持ちます。
- **誰にどう効くか**: 画像生成AIを使ったアプリや、写真投稿機能のあるアプリを出している企業のアプリ担当者・プロダクト責任者に直接関係します。広告やキャンペーン用に「写真を変身させる」アプリを作る代理店やマーケターも、利用者が他人の写真を悪用できない設計かを問われます。
- **今すぐやれること**: 自社アプリに画像の生成・加工・投稿の機能があれば、性的な画像を作らせない・載せさせないフィルター、通報ボタン、相手をブロックする機能の3つがそろっているかを確認します。審査後に機能を出し分ける仕組み（遠隔で機能を切り替える設定など）を使っている場合は、審査に出した版と食い違わないかも点検しておくと安全です。
- **注意点**: 「十分な対策」の線引きは公表されておらず、違反の通知を受けてから直す余裕がない可能性もあります。外部の画像生成AIをつないでいる場合も、責任はアプリを出した側にある点に注意が必要です。画像生成AIの選び方は[画像生成AIのガイド](/best/image-generation/)にまとめています。
