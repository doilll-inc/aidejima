---
{
  "title": "LiveRampがChatGPT広告で自社顧客データの配信を可能に、OpenAIとの提携を拡大",
  "description": "LiveRampが、CRMや会員データから作った顧客リストをChatGPT広告の配信先の指定や除外に使える連携を11の主要市場で始めた。配信先の指定には一致ユーザー2万5000人以上が必要で、まずは既存顧客の除外から試すのが現実的だ。",
  "date": "2026-10-01T15:08:00+09:00",
  "updated": "2026-10-01T18:55:00+09:00",
  "category": "marketing",
  "tags": ["LiveRamp", "ChatGPT", "OpenAI", "広告", "提携"],
  "summary": [
    "LiveRampはOpenAIとの提携を広げ、共通ID「RampID」で企業の顧客データをChatGPT広告に使えるようにした",
    "連携はまず11の主要市場で提供し、ChatGPT広告が提供される全市場へ順次広げるとLiveRampは説明している",
    "OpenAIの規定では、配信対象の指定と入札調整には一致ユーザー2万5000人以上が必要で、それ未満は除外にだけ使える"
  ],
  "sources": [
    {"title": "Bringing the Power of RampID Globally to Custom Audiences in ChatGPT Ads", "publisher": "LiveRamp", "url": "https://liveramp.com/blog/bringing-the-power-of-rampid-globally-to-custom-audiences-in-chatgpt-ads", "kind": "公式発表"},
    {"title": "Set up Custom Audiences for your Campaign", "publisher": "OpenAI Help Center", "url": "https://help.openai.com/en/articles/20001346-set-up-custom-audiences-for-your-campaign", "kind": "公式ドキュメント"},
    {"title": "Ads Manager Availability", "publisher": "OpenAI Help Center", "url": "https://help.openai.com/en/articles/20001245-ads-manager-availability", "kind": "公式ドキュメント"},
    {"title": "Unlocking better performance optimization and measurement for marketers in ChatGPT", "publisher": "LiveRamp", "url": "https://liveramp.com/blog/unlocking-better-performance-optimization-and-measurement-for-marketers-in-chatgpt", "kind": "公式発表"},
    {"title": "Publicis to acquire LiveRamp to accelerate data co-creation for smarter agents", "publisher": "LiveRamp", "url": "https://liveramp.com/news/publicis-to-acquire-liveramp-to-accelerate-data-co-creation-for-smarter-agents", "kind": "公式発表"},
    {"title": "LiveRamp Expands OpenAI Deal With First-Party Data Targeting", "publisher": "Search Engine Journal", "url": "https://www.searchenginejournal.com/liveramp-expands-openai-partnership-chatgpt-ads/591510/"},
    {"title": "LiveRamp Expands Partnership with OpenAI", "publisher": "destinationCRM", "url": "https://www.destinationcrm.com/Articles/CRM-News/CRM-Across-the-Wire/LiveRamp-Expands-Partnership-with-OpenAI-176774.aspx"},
    {"title": "LiveRamp CEO dishes on OpenAI partnership, looming Publicis acquisition", "publisher": "Marketing Dive", "url": "https://www.marketingdive.com/news/liveramp-ceo-dishes-on-openai-partnership-looming-publicis-acquisition/823481/"}
  ],
  "thumb_text": "ChatGPT広告",
  "thumb_kicker": "LiveRamp",
  "share_text": "LiveRampがChatGPT広告に顧客データ連携を追加。CRMや会員データで配信先の指定・除外が可能に",
  "editor_note": ""
}
---
データ連携サービス大手のLiveRampは現地時間9月28日、OpenAIとの提携を拡大し、企業が自社で集めた顧客データ（ファーストパーティデータ）をChatGPTの広告配信に使えるようにしたと発表しました。LiveRampの識別子「RampID」を通じて、CRM（顧客管理システム）や会員プログラムのデータから作った顧客リストを、配信先の指定や除外に使えます。まず11の主要市場で提供します。

## 何が発表されたか

LiveRampは今回、ChatGPT広告の「テクノロジーパートナー」になりました。RampIDとは、端末や媒体、取引先をまたいで同じ顧客のデータをつなぐためにLiveRampが提供する識別子です。広告主はCRM、会員プログラム、サイトやアプリの行動データなどをRampIDでまとめ、ChatGPT広告の「カスタムオーディエンス」（自社の顧客リストから作る配信対象の集団）として使えます。提供範囲について、LiveRampは次のように説明しています。

:::quote https://liveramp.com/blog/bringing-the-power-of-rampid-globally-to-custom-audiences-in-chatgpt-ads | LiveRamp公式ブログ「Bringing the Power of RampID Globally to Custom Audiences in ChatGPT Ads」
> This integration is now available in 11 major markets and over time will be expanded to every market where ChatGPT Ads are available.
この連携はいま11の主要市場で使え、今後はChatGPT広告が提供されるすべての市場に広げます。
:::

11市場がどの国かは明らかにしていません。最初の導入例は、代理店のAllegiance Group & Pursuant（AGP）が非営利団体の顧客向けに進めている実装です。AGPの担当者は、寄付者との接点としてChatGPT広告の存在感が増しているため、他の媒体と合わせて効果を見たいと話しています。

## 顧客データを入れる2つの道

実は、カスタムオーディエンスはLiveRampを通さなくても作れます。OpenAIのヘルプページと今回の発表を並べると、違いは次のとおりです。

| | 広告管理画面（Ads Manager）に直接アップロード | LiveRamp経由 |
|---|---|---|
| 元になるデータ | メールアドレス、電話番号、それらをハッシュ化（元に戻せない形に変換）した値、Androidの広告IDを含むCSVやTXT | CRM、会員プログラム、サイトやアプリの行動データなどをRampIDでまとめたもの |
| 向いている広告主 | 手元の顧客リストで小さく試したい企業 | すでにRampIDで他の媒体に顧客データを流している企業 |

どちらの道でも、使い方のルールはOpenAIの仕様で決まります。キャンペーン単位でリストの人だけに配信するか、リストの人を外すかを選べ、広告グループ単位ではリストに一致した人への上限入札額を0.1倍〜10倍に変えられます。アップロードしたファイルは処理後、通常24時間以内に削除されます。

規模の下限には注意が要ります。

:::quote https://help.openai.com/en/articles/20001346-set-up-custom-audiences-for-your-campaign | OpenAIヘルプセンター「Set up Custom Audiences for your Campaign」
> Note that inclusion audiences and audience bid adjustments require at least 25,000 matched users. Audiences below 25,000 matched users can be used for exclusions.
配信対象としての指定と入札の調整には、一致したユーザーが2万5000人以上必要です。2万5000人未満のオーディエンスは除外に使えます。
:::

OpenAIは、配信対象や入札調整には10万人以上を推奨しています。

## 背景

両社の提携は計測から始まりました。LiveRampは6月10日、広告を見た人がその後どこで購入や申し込みをしたかを、ブラウザを介さずサーバー間の通信で広告側に返す「コンバージョンAPI」の仕組みをChatGPT広告に対応させました。今回はそこに、配信先を決めるためのデータ連携が加わった形です。

LiveRamp自身も転機にあります。仏広告大手のPublicis Groupeは5月17日、LiveRampを企業価値約22億ドル、1株38.50ドルの全額現金で買収することで合意し、2026年末までの完了を見込んでいます。Marketing Diveは、特定の広告会社グループの傘下に入ることで、LiveRampの中立性を疑問視する声が同業から出ていると報じています。

## 論点

顧客リストで配信先を絞る、外す、入札額を変えるという機能の組み合わせは、GoogleやMetaの顧客リスト機能とよく似ています。Search Engine Journalも、広告主には見慣れた操作になると指摘しています。ただし、ChatGPT広告では会話の文脈も配信に影響するため、他の媒体で得た経験則がそのまま通用するとは限りません。

成果の裏付けもまだ薄い状態です。OpenAIはカスタムオーディエンスの成果を他の配信方法と比べたデータを公開しておらず、LiveRampも導入した広告主の結果は近く共有するとしている段階です。Search Engine Journalは、成果を測りやすい除外の用途から試すのが妥当との見方を示しています。

費用については、OpenAIのヘルプにカスタムオーディエンス専用の料金の記載はありません。ただ、入札の倍率を上げれば1件あたりの単価は上がりえます。クリック単価の高い安いだけで判断せず、成約率や顧客の生涯価値まで含めて、他の配信方法より得かどうかを見る必要があります。

## 日本のビジネスへの影響

OpenAIの提供国一覧では、日本はセルフサーブ型のAds Managerが使える国に入っており、カスタムオーディエンスの直接アップロードなら日本の広告主も試せます。LiveRamp経由の連携が日本で使えるかは、11市場の内訳が公表されていないため、LiveRamp日本法人への確認が必要です。

影響が大きいのは、CRMや会員データを持つEC・通販、サブスク、金融の広告運用者と、複数の媒体に顧客データを流している代理店です。今すぐできるのは、既存顧客のリストで「除外」を設定し、新規獲得キャンペーンの無駄な配信を減らすことです。日本の電話番号は「+81」から始まる国際形式（E.164）でないと受け付けられない点に注意してください。

注意点は2つあります。1つは規模で、配信対象として使うには一致ユーザー2万5000人以上が必要なため、顧客数が少ない企業は当面除外にしか使えません。もう1つは個人情報の扱いで、顧客リストを外部の広告媒体に渡す前に、プライバシーポリシーでの説明や同意の取り方を法務と確認しておくべきです。広告クリエイティブやSNS運用に使えるAIツールの比較は、[広告・マーケティング向けAIのおすすめ](/best/marketing/)にまとめています。
