---
{
  "title": "ChatGPTやGrokなどAIチャット9種で会話のURLや題名が広告企業に、研究者が報告",
  "description": "スペインのIMDEA Networksなどの研究者が、ChatGPT、Claude、Grokなど9つのAIチャットの通信を調べた。Web版9つのうち6つで、会話のURLや自動で付く題名、入力文が広告・計測企業に送られていた。",
  "date": "2026-10-01T18:39:00+09:00",
  "category": "policy",
  "tags": [
    "IMDEA Networks",
    "ChatGPT",
    "プライバシー",
    "広告",
    "論文",
    "個人情報"
  ],
  "summary": [
    "研究者が9つのAIチャットを調べ、全サービスが少なくとも1つの広告・計測サービスを組み込んでいることを確認した",
    "Web版9つのうち6つ、Android版8つのうち3つで、会話のURLや題名、入力文などが第三者に送られていた",
    "Grokは会話のリンクが初期設定で誰でも読め、研究者が会話に仕込んだURLは14か国からアクセスされた"
  ],
  "sources": [
    {
      "title": "Prompt like a Butterfly, Sting like a Tracker: A Privacy Analysis of Web and Mobile Conversational AI Agents",
      "publisher": "Oliveira ほか（IMDEA Networks など）",
      "url": "https://jorgegarciaherrero.com/wp-content/interactivos/20260916-Prompt-like-a-butterfly-sting-like-a-tracker-(clean).pdf",
      "kind": "論文"
    },
    {
      "title": "LeakyLM — AI Assistants Are Leaking Your Conversations",
      "publisher": "LeakyLM（研究チームのサイト）",
      "url": "https://leakylm.github.io/",
      "kind": "論文"
    },
    {
      "title": "La Agencia promueve ante las autoridades europeas de protección de datos que se estudie si algunos sistemas de IA permiten a terceros acceder a las conversaciones",
      "publisher": "スペインデータ保護庁（AEPD）",
      "url": "https://www.aepd.es/prensa-y-comunicacion/notas-de-prensa/la-agencia-promueve-ante-las-autoridades-europeas-proteccion-estudie-ia",
      "kind": "公式発表"
    },
    {
      "title": "外部送信規律",
      "publisher": "総務省",
      "url": "https://www.soumu.go.jp/main_sosiki/joho_tsusin/d_syohi/gaibusoushin_kiritsu.html",
      "kind": "公式ドキュメント"
    },
    {
      "title": "A Privacy Analysis of Web and Mobile Conversational AI Agents [pdf]",
      "publisher": "Hacker News",
      "url": "https://news.ycombinator.com/item?id=49890226",
      "kind": "報道"
    }
  ],
  "thumb_text": "AIチャットの追跡",
  "share_text": "AIチャット9種の通信を調べた研究。会話のURLや自動で付く題名が広告・計測企業に送られていた",
  "editor_note": ""
}
---
スペインの研究機関IMDEA Networksなどの研究者が、ChatGPT、Claude、Grokなど9つのAIチャットについて、会話の情報が広告や計測の企業にどう流れているかを調べた論文を9月に公開しました。Web版9つのうち6つで、会話のURLや自動で付く会話の題名、入力文などが第三者に送られていました。論文は9月29日にHacker Newsで紹介され、422ポイントを集めています。

## 何を調べたか

対象は、ChatGPT、Claude、Grok、DeepSeek、Perplexity、Gemini、Microsoft Copilot、Mistral（Le Chat）、Meta AIの9つです。Web版は9つすべて、Android版はアプリがある8つを調べました。実験は2026年5月にスペインで行い、ログインの有無、Cookieの同意・拒否、無料と有料のプランを組み合わせて、ブラウザやスマートフォンから外に出る通信を記録しています。

研究者は、従来のWeb追跡とは違う点として「会話から生まれる情報」に注目しました。会話ごとに付く固定のURL（パーマリンク）、AIが内容を要約して自動で付ける会話の題名、入力文、共有時の画面画像などです。

:::quote https://jorgegarciaherrero.com/wp-content/interactivos/20260916-Prompt-like-a-butterfly-sting-like-a-tracker-(clean).pdf | 論文「Prompt like a Butterfly, Sting like a Tracker」要旨
> We also find that some providers publicly expose conversation permalinks without access controls, allowing trackers to read the entire conversation.
また、一部の事業者は会話のパーマリンクをアクセス制限なしで公開しており、追跡事業者が会話全体を読める状態にあることも分かりました。
:::

## 何が分かったか

論文が示した主な数字は次のとおりです。

| 項目 | 結果 |
|---|---|
| 組み込まれていた第三者の組織 | 44。全サービスが広告・計測サービスを1つ以上利用 |
| 会話のURL・題名・入力文などを第三者に送信 | Web版9つ中6つ、Android版8つ中3つ |
| 会話の題名を送信 | Web版9つ中3つ。送り先はMeta、TikTok、DoubleClickなど9社 |
| Cookieを拒否しても第三者が情報を収集（無料プラン） | 9サービス中4つ |

Cookieを拒否しても、Perplexity、DeepSeek、Gemini、Copilot、ChatGPT、ClaudeのWeb版はGoogle Adsに接続していました。無料と有料のプランで、接続先の顔ぶれはほとんど変わりませんでした。

サービス別にも具体的な指摘があります。Claudeは同意後、ユーザーの行動データを自社のサーバーから11の広告プラットフォームへ直接転送する設定を読み込んでいました。ブラウザを通らないため、広告ブロッカーでは止められません。拒否すればこの転送は止まります。Grokは同意後、会話のURLと題名をサーバー経由でMetaとTikTokの広告計測に送っていました。Perplexityはメールアドレスをハッシュ化（復元しにくい形に変換）した値を計測会社に送っていました。ただ、ハッシュ値は既知のアドレスと照合できるため、本人の特定に使えると論文は指摘しています。

最も深刻とされたのはGrokです。会話のリンクが初期設定で誰でも読める状態で、研究者が会話に仕込んだ追跡用のURLには、数時間から数日のあいだに14か国の70のIPアドレスからアクセスがありました。Perplexityはゲスト利用時の会話を常に公開していましたが、2026年4月3日にMetaへのURL送信をやめています。

## 反応と論点

研究チームは4月に欧州と英国のデータ保護当局に結果を伝え、xAIにもGrokの問題を通知しましたが、9月10日時点で返答はないとしています。スペインのデータ保護庁（AEPD）は5月27日、この研究を欧州データ保護会議（EDPB）に共有し、6月の全体会合で取り上げるよう求めたと発表しました。OpenAIは8月15日にChatGPTのプライバシーポリシーを改め、第三者の追跡ツールについて明記しましたが、研究との関係は確認できないと論文は書いています。

Hacker Newsでは「漏えいではなく意図して売っているのでは」という声の一方、URLに推測しにくい文字列を入れるだけで非公開扱いにする設計への批判も出ました。ChatGPTが広告を始めた流れ（[関連記事](/news/20261001-liveramp-chatgpt-ads-first-party-data/)）を考えると、会話と広告の距離は縮まりつつあります。

## 日本のビジネスへの影響

実験はスペインで行われ、論文も地域によって結果が変わりうると断っています。法人向けプランも対象外です。ただ、日本の企業にとって重要なのは、自社でAIチャットを出す側の問題でもあることです。

:::quote https://jorgegarciaherrero.com/wp-content/interactivos/20260916-Prompt-like-a-butterfly-sting-like-a-tracker-(clean).pdf | 論文「Prompt like a Butterfly, Sting like a Tracker」8章
> Consequently, these concerns extend beyond consumer B2C services to the broader ecosystem of LLM-powered web applications, custom customer-support chatbots, and third-party AI wrappers that rely on identical web and mobile analytics pipelines.
したがって、こうした懸念は消費者向けサービスにとどまらず、同じWeb・アプリの計測の仕組みを使うLLMアプリ、独自の問い合わせ対応チャットボット、AIを組み込んだ他社製サービスにまで及びます。
:::

関係が深いのは、自社サイトやアプリに問い合わせ・商品相談のAIチャットを載せるWeb担当者と、計測タグを入れるマーケターです。今すぐできるのは、チャット画面に載っているタグを洗い出し、会話のURL、ページタイトル、入力文が外に送られていないかをブラウザの開発者ツールで確かめることです。研究者も同じ方法で調べています。会話の画面では広告タグを外すか、URLとタイトルを送らない設定にし、共有リンクは初期設定で非公開にしてください。

注意点として、総務省の外部送信規律では、対象の事業者はタグで送る利用者情報の内容と送信先を通知・公表する必要があります。自社のチャットが対象かどうかは提供形態によるため、総務省のフローチャートで確認してください。各社チャットAIの比較は[チャットAIのおすすめ](/best/chat/)にまとめています。
