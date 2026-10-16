---
{
  "title": "ChatGPTがChromeで開いているタブを見て作業まで、拡張機能が更新 予約フォームの入力や予定の登録も",
  "description": "OpenAIはChatGPTのChrome拡張機能を10月15日に更新した。開いているタブの中身を比べたり、エージェントの「Work」に複数のタブをまたいでフォーム入力や予定の登録を任せたりできる。利用者は約700万人で、どのプランでも使えると報じられている。",
  "date": "2026-10-17T01:50:00+09:00",
  "category": "products",
  "tags": ["ChatGPT", "ChatGPT Work", "OpenAI", "Google Chrome", "エージェント", "ブラウザ"],
  "summary": [
    "OpenAIは現地時間10月15日、ChatGPTのChrome拡張機能を更新し、ブラウザの横でChatGPTの会話履歴ごと使えるようにした",
    "開いている複数のタブを読ませて商品を比べたり、作業を代行するWorkにフォーム入力やカレンダー登録を任せたりできる",
    "初期設定では新しいサイトを操作する前に毎回許可を求める。ストアの評価は5点満点で2.2と、使い勝手への不満も多い"
  ],
  "sources": [
    {"title": "ChatGPT の投稿", "publisher": "X @ChatGPT", "url": "https://x.com/ChatGPT/status/2110823740309401654", "kind": "X投稿"},
    {"title": "Chrome extension", "publisher": "OpenAI（ChatGPT公式ドキュメント）", "url": "https://learn.chatgpt.com/docs/chrome-extension.md", "kind": "公式ドキュメント"},
    {"title": "ChatGPT（Chrome ウェブストア）", "publisher": "Chrome ウェブストア", "url": "https://chromewebstore.google.com/detail/chatgpt/hehggadaopoacecdllhhajmbjkdcmajg", "kind": "公式サイト"},
    {"title": "ChatGPT can now look at your Chrome tabs to do tasks for you", "publisher": "Engadget", "url": "https://www.engadget.com/2288580/open-ai-updates-chatgpt-extension-for-chrome/", "kind": "報道"}
  ],
  "thumb_prompt": "A laptop on a messy home desk with a dozen browser windows fanned out in the air above it like playing cards, while a small friendly robot hand reaches out from the screen to fill in a paper appointment form with a pen.",
  "thumb_style": "photo",
  "thumb_text": "ChatGPT×Chrome",
  "share_text": "ChatGPTのChrome拡張が更新。開いているタブを読んで比較、Workならフォーム入力や予定登録まで代行",
  "editor_note": ""
}
---
OpenAIは現地時間10月15日、ChatGPTのGoogle Chrome向け拡張機能を更新し、ブラウザで開いているタブの中身をChatGPTに読ませて、比較や作業の代行まで頼めるようにしました。Chromeウェブストアの表示では、この拡張機能の利用者は約700万人です。単独のブラウザ「ChatGPT Atlas」を8月に終えたOpenAIにとって、Chromeの中で使ってもらうための本命の機能になります。

## 何が変わったか

拡張機能とは、ブラウザに後から足して機能を増やす小さなソフトです。今回の更新で、Chromeの画面の横にChatGPTを開くと、これまでの会話履歴をそのまま呼び出しながら、見ているサイトと並べて使えるようになりました。

{{x:https://x.com/ChatGPT/status/2110823740309401654}}

ChatGPTの公式アカウントは、ブラウザの中でChatGPTの全機能が使え、普通の会話（Chat）と作業の代行（Work）をサイトの横で使い分けられると投稿しています。

米Engadgetによると、できることは大きく2つです。

- **Chatでタブを比べる**: 開いている複数のタブを読ませ、たとえばソファの候補を寸法・価格・配送日数・返品条件で比べさせる
- **Workに作業を任せる**: 複数のタブから必要な情報を拾い、メッセージの送信、フォームの入力、タブの整理、カレンダーへの予定の追加、メールの下書きまで進める。新しい歯医者の問診フォームを埋めて、予約をカレンダーに入れる例が紹介されています

ChatGPT Workとは、何段階もある仕事をまとめて引き受けるOpenAIのエージェント（指示を受けて自分で手順を進めるAI）です。Engadgetは、拡張機能はどのChatGPTのプランでも使え、Chromeのほか、同じ仕組みで作られたMicrosoft Edge・Brave・Operaでも動くと報じています。

## 安全のための仕組み

ブラウザを操作させる以上、気になるのは勝手な操作です。OpenAIの公式ドキュメントは、拡張機能が「ログイン済みのサイトを読んだり操作したりできる」と説明したうえで、初期設定の動きを次のように書いています。

:::quote https://learn.chatgpt.com/docs/chrome-extension.md | OpenAI公式ドキュメント「Chrome extension」
> By default, ChatGPT asks before it interacts with each new website.
初期設定では、ChatGPTは新しいWebサイトを操作する前に、毎回確認を求めます。
:::

同じドキュメントは、拡張機能でのブラウザ操作の完全な記録をOpenAIが別に保存することはないとしています。一方で、ページに書かれた内容は「信用できない情報」として扱い、続けさせる前にそのサイトを自分で確かめるよう利用者に求めています。悪意のあるページに紛れ込んだ指示でAIが誤った操作をする危険を、OpenAI自身が認めている形です。

使える範囲には細かい差があります。ドキュメントでは、横に開く会話画面はChrome・Edge・Brave・Vivaldiで使え、Operaは非対応です。提供の進み具合や、会社のアカウントの設定によっては使えない場合があるとも書かれています。

{{card:https://learn.chatgpt.com/docs/chrome-extension.md|Chrome extension（設定方法と許可の仕組み）|OpenAI}}

## 背景と評判

OpenAIは自社のブラウザ「ChatGPT Atlas」を8月9日に終了し、機能をChromeの拡張機能とパソコン用アプリに移してきました。ブラウザの中のAIでは、GoogleがChromeにGeminiを組み込んでおり、Engadgetは今回の更新でChatGPTがその対抗馬として強くなったと評しています。

ただ、評判は割れています。Chromeウェブストアでのこの拡張機能の評価は、10月17日時点で922件の評価の平均が5点満点の2.2でした。ストア側も「最近のレビューを反映していない可能性がある」と注記しており、今回の更新で評価が変わるかはまだ分かりません。

ChatGPTに複数のステップの仕事を任せる使い方は、企業でも広がっています。米Oracleが10万人超でChatGPT Workを使う事例は[こちらの記事](/news/20261009-oracle-chatgpt-work-codex-recruiting/)で紹介しました。

## 日本のビジネスへの影響

- **使えるか**: 拡張機能はChromeウェブストアから日本でも入れられます。ただしストアの対応言語の表示は英語だけで、Workをタブ操作に使える範囲は、プランや会社の設定、提供の進み具合で変わるとOpenAIは説明しています。自分のアカウントで実際に試して確かめるのが確実です
- **誰に効くか**: 調べものの多い企画・マーケティング担当と、事務作業の多いバックオフィスです。競合の商品ページを5つ開いて「価格と特徴を表にして」と頼む、複数のメールや予約サイトを見ながら日程調整とフォーム入力を任せる、といった使い方に向きます
- **今すぐやれること**: まずはChatで、比較したいページを数枚開いて表にまとめさせてみてください。Workにフォーム入力を任せるのは、社外に送信されない練習用のフォームや、間違えても困らない作業から始めるのが安全です
- **注意点**: ログインした状態の社内システムや取引先のサイトも操作の対象になります。サイトごとの許可を「すべて許可」にしない、顧客情報を扱う画面では使わない、など社内でルールを決めてから広げてください。ChatGPTとほかの対話AIの選び方は「[チャットAIの選び方](/best/chat/)」にまとめています
