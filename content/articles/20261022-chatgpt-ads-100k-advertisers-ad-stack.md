---
{
  "title": "ChatGPTの広告主が8か月で10万社超に、会話の流れを読んで広告を選ぶ仕組みをOpenAIが公開",
  "description": "OpenAIはChatGPTの広告を新たに26か国へ広げ、提供国は89か国、出稿した広告主は10万社を超えたと発表した。あわせて、会話の流れから広告を選ぶAIの仕組みを技術ブログで公開し、広告が答えに影響しない設計を説明した。",
  "date": "2026-10-22T02:30:00+09:00",
  "category": "marketing",
  "tags": ["ChatGPT", "ChatGPT Ads", "OpenAI", "広告", "マーケティング", "Codex"],
  "summary": [
    "OpenAIはChatGPTの広告を26か国に広げ、提供国は89か国、出稿した広告主は開始から約8か月で10万社を超えた",
    "広告は無料版と月額の安い「Go」だけに出て、有料のPlus・Pro・企業向けには出ない。日本の企業も自分で出稿できる",
    "OpenAIは会話の流れを読んで広告を選ぶ専用AIの仕組みも公開し、広告を選ぶ処理はChatGPTの答えと切り離していると説明した"
  ],
  "sources": [
    {"title": "ChatGPT Ads expands to 26 new countries as over 100,000 advertisers have used the platform", "publisher": "OpenAI", "url": "https://openai.com/index/chatgpt-ads-expands-26-new-countries/", "kind": "公式発表"},
    {"title": "How we built ChatGPT’s novel ad stack for user trust and relevance", "publisher": "OpenAI", "url": "https://openai.com/index/building-chatgpt-ad-stack/", "kind": "公式発表"},
    {"title": "Ads Manager Availability", "publisher": "OpenAI Help Center", "url": "https://help.openai.com/en/articles/20001245-ads-manager-availability", "kind": "公式ドキュメント"},
    {"title": "OpenAI expands ChatGPT ads to 26 more countries in bid to boost revenue", "publisher": "Reuters（Investing.com）", "url": "https://www.investing.com/news/stock-market-news/openai-expands-chatgpt-ads-to-26-more-countries-in-bid-to-boost-revenue-4963176", "kind": "報道"},
    {"title": "OpenAI Expands ChatGPT Ads to 26 More Countries, Says It Has More Than 100,000 Advertisers", "publisher": "The Information", "url": "https://www.theinformation.com/briefings/openai-expands-chatgpt-ads-26-countries-says-100-000-advertisers", "kind": "報道"}
  ],
  "thumb_prompt": "A cozy kitchen table at night where a smartphone shows a long chat about marathon training, and a tiny shop clerk figurine stands politely at the bottom edge of the phone screen holding a small pair of running shoes on a tray, waiting for its turn.",
  "thumb_style": "photo",
  "thumb_text": "ChatGPT Ads",
  "share_text": "ChatGPTの広告主が8か月で10万社超、提供は89か国に。OpenAIは会話から広告を選ぶAIの仕組みも公開",
  "editor_note": ""
}
---
OpenAIは現地時間10月21日、ChatGPTの広告を新たに26か国で始め、提供国が89か国になったと発表しました。約8か月前に広告を始めてから、ChatGPTに出稿した広告主は10万社を超えたといいます。同じ日に、会話の流れを読んでどの広告を出すかを決める専用AIの仕組みも技術ブログで公開しました。

## 何が発表されたか

利用者から見ると、広告が出るかどうかは契約しているプランで決まります。対象は無料版と低価格の「Go」で、Plus・Pro・企業向けのEnterpriseでは広告は表示されません。出稿する企業は、自分で申し込める管理画面「Ads Manager」を使うか、OpenAIと組む広告技術会社を経由します。

今回の対象は、ナイジェリアや南アフリカ、セルビア、ウクライナ、カンボジア、バングラデシュ、パキスタンなどと、アルゼンチン・チリ・コロンビア・ペルーを含む中南米14か国です。中南米ではメキシコとブラジルが先行していました。欧州、東南アジア・台湾への拡大に続く動きで、OpenAIは今後、広告の形式や目的の種類、買い方、効果測定の機能を増やすとしています。

## 広告はどう選ばれるのか

もう1本の技術ブログは、検索広告とChatGPTの広告の違いから説明しています。検索なら「キーワードを入れた瞬間」に広告を選べますが、ChatGPTでは相談が何往復も続き、何を買いたいかが後から固まっていきます。OpenAIの例では、マラソンの練習の話から始まり、何回かやりとりした後に靴の話になります。最初の質問だけで広告を選ぶと的外れになる、というわけです。

そこでOpenAIは、広告選びを担当する専用のAI（社内では「オーケストレーター」と呼ぶ）を作りました。このAIは会話を短い要約に直し、広告の候補を広く集め、予算や出稿条件で絞り、関連度や押されやすさを点数にして、最後にオークション（入札）にかけます。ヨセミテ旅行の相談の途中で靴のブランドの新作を聞いた人なら、「ハイキング向けの靴」と「旅行に合うそのブランドの新作」の2つの意図に分けて探す、という例が示されています。

{{card:https://openai.com/index/building-chatgpt-ad-stack/|How we built ChatGPT’s novel ad stack for user trust and relevance|OpenAI}}

設計で強調しているのは、広告とChatGPTの答えを切り離している点です。広告を選ぶ処理は答えを作る処理とは別のサーバー・別のモデル・別のプログラムで動き、答えができる前に広告が間に合わなければ、その回は広告を出しません。

:::quote https://openai.com/index/building-chatgpt-ad-stack/ | OpenAI技術ブログ「How we built ChatGPT’s novel ad stack」
> Returning no ad is an ordinary, successful outcome.
広告を出さないことも、普通の、うまくいった結果である。
:::

広告は答えの下に「スポンサー」と明記して表示され、なぜその広告が会話に関係するのかを説明する短い前置きが添えられます。この前置きもAIが中立な言い方で書き、広告主の文面とは分けて扱うといいます。

## 背景

OpenAIは8月に、広告事業の年換算の売上が10億ドルに達したと公表していました。技術ブログによると、開始から200日足らずでの到達です。ロイターは今回の拡大について、株式上場もにらんで広告で売上を伸ばす動きだと報じています。

技術ブログは、1年前には広告の仕組みがなく、担当者も数人だったとも明かしています。開発には自社のプログラミング用AI「Codex」を最初から使い、短期間で作り上げたと説明しています。

## 反応と論点

広告を出す側にとっては、検索広告のような「キーワード」ではなく「相談の中身」で広告が選ばれる点が新しいところです。一方で、OpenAIが利用者の過去の会話を広告選びにどこまで使うのかは、利用者側の関心が高い点です。OpenAIは、広告主に会話の中身は渡さずデータも売らないとし、広告のパーソナライズを利用者がオンにした場合に限り、過去の会話のうち機微でない情報を参考にすると書いています。

また、広告を選ぶAIの性能を、より賢い自社のAIに採点させて鍛える仕組みも紹介しています。仕組みが自分で改善していく分、何が評価されて広告が出たのかは外から見えにくくなります。広告の質や公平さをどう検証するかは、今後の論点になりそうです。

## 日本のビジネスへの影響

- **使えるか**: 日本はすでに広告の提供国で、OpenAIのヘルプページでも、日本の企業がAds Managerから自分で出稿できる国に入っています（10月22日時点）。広告を目にするのは、無料版とGoを使っている日本の利用者です
- **誰に効くか**: 広告運用の担当者とEC・旅行・ソフトウェアなど「比べて選ぶ」商材のマーケターです。ChatGPTの広告は、検索語ではなく相談の流れで選ばれるため、「誰がどんな悩みの途中で自社を知ると良いか」という場面の設計が効きます
- **今すぐやれること**: 自社の商品について、顧客がChatGPTにどんな順番で相談しそうかを3〜4往復の会話として書き出し、その会話の最後に出したい広告文を試しに作ってみることです。少額でAds Managerを試すかどうかの判断材料になります。広告に使えるAIの比較は[広告・マーケティング向けAIのガイド](/best/marketing/)にまとめています
- **注意点**: 広告を出すかどうかはOpenAI側のAIが判断し、「出さない」ことも普通の結果とされています。予算を入れても表示が伸びない可能性があり、検索広告と同じ感覚で配信量を見込むのは危険です。ChatGPTの広告の別の形式については、[画像生成の待ち時間に出る写真広告の記事](/news/20261006-chatgpt-visual-ads-image-generation/)も参考になります
