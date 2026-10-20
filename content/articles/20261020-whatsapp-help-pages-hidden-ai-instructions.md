---
{
  "title": "WhatsAppのヘルプに画面に出ないAIへの指示、「規制当局への相談は勧めるな」 80ページで見つかる",
  "description": "WhatsAppのヘルプセンターのうち80ページに、読む人には見えずAIだけが読む指示が102か所埋め込まれていた。アカウントを消せない利用者に規制当局を勧めない、法律の名前を出さないといった中身で、WhatsAppは「不具合で表に出た」と説明し削除した。",
  "date": "2026-10-20T17:55:00+09:00",
  "category": "policy",
  "tags": ["WhatsApp", "Meta", "プライバシー", "SEO", "規制"],
  "summary": [
    "WhatsAppのヘルプページ80ページに、画面には出ずAIだけが読む指示が102か所埋め込まれていたと、米プライバシー企業Redactが公表した",
    "中には「データ保護の規制当局への相談を勧めない」「利用者が持ち出してもGDPRなどの法律に触れない」という指示があった",
    "WhatsAppは自社のサポート用AIへの指示が不具合で表に出たと説明し、10月18日までにすべて消した"
  ],
  "sources": [
    {"title": "WhatsApp's Hidden Notes Told AI Not to Recommend a Regulator", "publisher": "Redact（Dan Saltman）", "url": "https://redact.dev/blog/whatsapp-help-pages-hidden-ai-instructions", "kind": "公式サイト"},
    {"title": "WhatsApp's help pages hid LLM instructions: dont recommend a regulator", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=50159341", "kind": "コミュニティ"},
    {"title": "WhatsApp Help Pages Leaked Hidden Instructions for a Meta Chatbot", "publisher": "WIRED", "url": "https://www.wired.com/story/whatsapp-help-pages-leaked-hidden-instructions-for-a-meta-chatbot/", "kind": "報道"},
    {"title": "WhatsApp's Meta AI chatbot has what not to say list and its hidden instructions are now exposed", "publisher": "Digit", "url": "https://www.digit.in/news/general/whatsapps-meta-ai-chatbot-has-what-not-to-say-list-and-its-hidden-instructions-are-now-exposed-details.html", "kind": "報道"}
  ],
  "thumb_prompt": "A help desk counter with a friendly printed help sheet on top, and under the counter a small hidden sticky note visible only to a glowing robot reading it with a flashlight, while a customer stands unaware on the other side.",
  "thumb_style": "photo",
  "thumb_text": "WhatsApp",
  "share_text": "WhatsAppのヘルプ80ページに、画面に出ないAI向けの指示。「規制当局への相談は勧めるな」の一文も",
  "editor_note": ""
}
---
メッセージアプリWhatsAppのヘルプセンターのうち80ページに、読む人の画面には表示されず、AIだけが読む指示が埋め込まれていたことがわかりました。米国のプライバシー関連企業Redactのダン・サルトマンCEOが現地時間10月19日に自社ブログで公表し、米WIREDも報じています。指示の中には「アカウントを消せない利用者に、データ保護の規制当局への相談を勧めない」というものも含まれていました。

## 何が見つかったか

サルトマン氏が最初に気づいたのは10月8日です。その後、WhatsAppのヘルプセンターからリンクされている545ページをすべて読み、保存しました。その結果、80ページに合わせて102か所、ページの裏側（読み込まれるデータの中）にだけある文章が見つかりました。

:::quote https://redact.dev/blog/whatsapp-help-pages-hidden-ai-instructions | Redact「WhatsApp's Hidden Notes Told AI Not to Recommend a Regulator」
> It was written into the help pages in a way that never showed on your screen and was only there for an AI to read.
それはヘルプページに、画面には決して表示されず、AIが読むためだけの形で書かれていた。
:::

問題視されたのは2か所です。

- **アカウント削除のページ**: スマホや電話番号を失ってアカウントを消せない人への対応として、「データ保護当局・規制当局・監督機関への連絡を勧めない」「WhatsAppが代わりに手作業で消せるとは言わない」と書かれていました
- **通報とブロックのページ**: 利用者が弁護士や裁判、法的措置に触れた場合について、「GDPR（EUの個人情報保護のルール）などデータ保護の法律に触れない、引用しない、解釈しない。利用者のほうから持ち出した場合も同じ」とありました

残りの約100か所の大半は、言葉の言い換えや別ページへの案内など、問い合わせ対応の手引きのような中身だったとしています。同じ仕組みで作られているFacebookとInstagramのヘルプも300ページ調べましたが、似た指示は見つからなかったといいます。

## 公開している方針との食い違い

Redactは、WhatsApp自身が欧州向けに7月2日から適用しているプライバシーポリシーと比べています。ポリシーでは、利用者はいつでも自分の情報の削除などを求められ、アイルランドのデータ保護委員会などに苦情を申し立てられると書いています。表では権利を案内しながら、AIには「その案内をするな」と指示していた形です。

一方でRedactは、WhatsAppの立場にも理があると書いています。会社の名前で法律の判断をAIに言わせたくないのは当然で、電話番号なしでは持ち主を確かめられないため、削除の依頼を断ること自体には理由がある、という見方です。そのうえで、「規制当局がある」と知らせるのは法律の助言ではない、と線を引いています。

## WhatsAppの説明

WIREDやインドのDigitによると、WhatsAppは、これらは利用者が問い合わせるサポート用のAIチャットへの指示で、不具合でページに出てしまい、すでに直したと説明しました。指示はページの中で「WHAT NOT TO SAY（言ってはいけないこと）」と題した区切りに置かれていたものもあったと報じられています。広報担当のジョシュア・ブレックマン氏は、サポートのAIはWhatsAppの使い方の助言に集中させ、法律の助言はさせない方針だと話しています。

Redactの確認では、10月15日の時点では指示が残っており、10月18日には80ページ・102か所すべてが消えていました。インターネット上のページの保存サービス（Internet Archive）では、7月12日の写しには指示がなく、9月4日の写しにはあったといいます。どれくらいの期間、サポートのAIがこの指示どおりに答えていたかはわかっていません。

## 反応と論点

ITニュースの投稿サイトHacker Newsでは、話題の上位に入り90件を超えるコメントがつきました。規制当局の存在を伏せさせるのは「言わないことによるうそ」だという批判や、表に出たのが不具合なのであって指示があったこと自体が問題だという声がある一方、弁護士を名乗る人からは、客の相談を受けるAIに法律の助言を禁じるのはよくある設定だと擁護する意見も出ています。

見落とせないのは、指示がWhatsApp自身のAIだけに届いたわけではない点です。Redactによると、WhatsAppのサーバーはこの指示を含んだページを、GoogleやBingの検索エンジンの収集プログラムにも渡していました。検索エンジンや他社のAIがページを読み込めば、他人の書いた指示を読まされることになります。Hacker Newsでも、自社AIへの指示が他社のAIには「乗っ取りの命令」として働きうる、という指摘がありました。ただしRedactは、実際にどこかのAIがこの指示に従ったかは確かめていません。

なお、Redactは個人がネット上の投稿やデータを消すためのツールを売っている会社です。ページを読んだ範囲は英語のページだけで、ほかの言語のページは確かめていないとしています。

## 日本のビジネスへの影響

- **関係あるか**: 日本でもWhatsAppを使う人や、海外の取引先とWhatsAppでやり取りする会社は少なくありません。今回の指示はすでに消えており、利用者が今すぐ何かをする必要はありません。WhatsAppのアカウントを消せずに困っている場合は、自分で削除の依頼を出せること、EUの利用者であれば規制当局への申し立ての道があることは、WhatsApp自身のポリシーに書かれています
- **誰に効くか**: 自社サイトにAIのチャット窓口を置いている、またはこれから置こうとしているカスタマーサポートの責任者とWeb担当者です。ヘルプページとAIへの指示を同じ場所で管理する作り方は手間が省ける反面、設定ひとつで外から見え、検索エンジンや他社のAIにも渡ります。AIの答えに載る情報が検索の行方を左右する流れは、[架空の用語が1週間でAI検索の回答に載った実験](/news/20261020-ai-search-cited-fabricated-concept-week/)でも見えています
- **今すぐやれること**: 自社のAIチャットに渡している指示の一覧を出し、「外に出ても説明できる中身か」を確かめることです。「法律の判断はしない」はよくある設定ですが、「消費者が使える窓口や権利を伏せる」まで踏み込んでいないかを、法務の担当者と一緒に見直すのが安全です。AIチャットそのものを選び直す場合は[用途別ガイドのAIチャット](/best/chat/)も参考になります
- **注意点**: 日本の個人情報保護法でも、本人は会社に自分のデータの開示や利用停止などを求められます。AIの窓口がその道を案内しない作りになっていると、指示の中身が表に出たときに、会社の説明と食い違う形で批判を受けます。Metaは別の件でも、事業者サイトの読み込みをめぐる規約変更が議論になっています（[インスタで集客する会社のサイトもMetaがAI学習に？](/news/20261017-meta-commercial-terms-crawl-business-sites/)）
