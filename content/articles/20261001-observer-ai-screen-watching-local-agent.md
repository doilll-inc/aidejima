---
{
  "title": "Observer AIは画面を見張って知らせるローカルAIアプリ、作者の母親も設定できる手軽さに",
  "description": "個人開発者が1年かけて作ったオープンソースアプリObserver AIが話題だ。画面やカメラをローカルのAIに見張らせ、変化があれば電話やメールで知らせる。9月公開のv3.0.0で、作者の母親が初めて自分で設定できた。",
  "date": "2026-10-01T17:49:00+09:00",
  "updated": "2026-10-01T18:55:00+09:00",
  "category": "usecases",
  "tags": ["Observer AI", "ローカルLLM", "オープンソース", "エージェント", "個人開発", "活用事例"],
  "summary": [
    "Observer AIは、画面やカメラを手元のAIモデルに見張らせ、変化があれば通知や記録をするオープンソースのアプリ",
    "作者のRoy Medina氏は1年かけて設定を簡単にし、9月18日公開のv3.0.0で母親が初めて自分で見張り役を設定できた",
    "AIの処理は手元のllama.cppやブラウザ内で動くが、メールやメッセージの通知は外部のサービスを経由する"
  ],
  "sources": [
    {"title": "Roy3838/Observer", "publisher": "GitHub Roy3838", "url": "https://github.com/Roy3838/Observer", "kind": "公式ドキュメント"},
    {"title": "Thanks to you r/LocalLLaMA, my mom was able to use my app! The open-source app that can watch your screen and trigger actions.", "publisher": "Reddit r/LocalLLaMA（作者の投稿）", "url": "https://www.reddit.com/r/LocalLLaMA/comments/1wtelk8/thanks_to_you_rlocalllama_my_mom_was_able_to_use/", "kind": "公式発表"},
    {"title": "Observer AI - Local Open-Source Micro-Agents", "publisher": "Observer AI", "url": "https://observer-ai.com/", "kind": "公式発表"},
    {"title": "Using local LLMs to monitor your screen", "publisher": "Observer AI（YouTube）", "url": "https://www.youtube.com/watch?v=NCaWVOprZwE", "kind": "公式発表"},
    {"title": "Observer AI v3.0.0（リリース）", "publisher": "GitHub Roy3838", "url": "https://github.com/Roy3838/Observer/releases/tag/v3.0.0", "kind": "公式ドキュメント"}
  ],
  "thumb_text": "Observer AI",
  "share_text": "画面を見張って知らせるオープンソースのローカルAIアプリObserver AI。作者の母親も自分で設定できるほど簡単になった",
  "thumb_style": "3d",
  "thumb_prompt": "A friendly round robot eye perched on top of a computer monitor like an owl, watching the screen, with a smartphone next to it ringing with a notification glow.",
  "editor_note": ""
}
---
個人開発者のRoy Medina氏が作るオープンソースのアプリ「Observer AI」が、ローカルLLM（手元のパソコンで動かすAIモデル）の利用者が集まる掲示板r/LocalLLaMAで話題になっています。画面やカメラを手元のAIに見張らせ、「〇〇が起きたら知らせる」を自動化するアプリです。作者は9月29日の投稿で、9月18日に公開したv3.0.0で、母親が初めて自分で見張り役のエージェントを設定できたと報告しました。

## 何を作ったか

Observer AIの基本の考え方は「XになったらYをする」です。きっかけの例として、公式サイトやGitHubには、ダウンロードや動画の書き出し（レンダリング）の完了、ダッシュボードの表示の変化、カメラに人が映ったとき、作業中に気が散ったときなどが挙がっています。知らせ方は電話、SMS、WhatsApp、Telegram、Discord、メールで、知らせずに記録だけ残すこともできます。作者はr/LocalLLaMAへの投稿で、コンサートのチケットが出たら購入ボタンを押すという使い方も紹介しました。

:::quote https://observer-ai.com/ | Observer AI公式サイト
> The agent that monitors your screen, so you don't have to.
あなたの代わりに画面を見張るエージェント。
:::

AIに渡せる入力（センサー）は、画面のスクリーンショットと文字読み取り（OCR）、カメラ、クリップボード、マイクや画面の音声の文字起こしなどです。AIの判断を受けて動く道具（ツール）には、先の通知のほか、画面へのお知らせ表示、録画の開始と停止、マウスのクリックまであります。

{{youtube:https://www.youtube.com/watch?v=NCaWVOprZwE}}

## どう作ったか

見張り役は「マイクロエージェント」と呼ぶ小さな部品で、センサー、AIモデル、ツールの3つを組み合わせて作ります。READMEにある基本の例では、画面にObserverのロゴが映っているかどうかを決まった言葉で答えさせる指示文を、決めた間隔で画面の画像と一緒にAIへ渡します。返事の中身をJavaScriptのコードが判定し、ロゴがあればメールを送ります。

今の版では、このエージェントを手で組む必要が減りました。司令役のエージェント「Observer」に見張りたい内容を文章で伝えると、Observerが道具の連携規格MCPを通じて設定を組み立てます。

投稿によると、以前の版は仕組みこそ面白がられたものの、設定に手間がかかりすぎると掲示板で指摘されていました。作者はそこから1年かけて、技術に詳しくない人でも使える形に直してきました。数か月ごとに母親に使ってもらっており、今回初めて母親がローカルのモデルで見張り役を組めたことを、作者は「mom benchmark（母親ベンチマーク）」に合格したと表しています。

AIの処理は手元で行います。デスクトップアプリはllama.cppを内蔵し、ブラウザ版はtransformers.jsでGoogleの小型モデルGemma 4 E2Bをブラウザの中で動かすため、インストールなしで試せます。OllamaなどOpenAI互換のサーバーにもつなげます。

ライセンスはAGPLv3です。作者はr/LocalLLaMAの投稿で、中核部分はこれからも無料のオープンソースのままにすると約束し、「自分にとって無料なら、利用者にも無料であるべき」という線引きは変えないと書いています。

## 反応

コメント欄では、ウェブカメラで自分を見張らせて、ぼんやりSNSを眺めていたら注意してもらえるかという質問に、作者が「できる」と答えました。画面全体を見られること、24時間動かせること、30秒ごとなど決めた間隔で画面を確認することも作者が説明しています。高性能な自宅サーバーなら確認の間隔を約3秒まで縮められるとのことです。一方で、投稿文がAIで書かれたものだとして、掲示板の規則違反を指摘するコメントも付きました。GitHubのスターは10月1日時点で約1,600です。

## 日本で真似するなら

仕事で使うなら、待ち時間の多い作業の見張りが向いています。動画の書き出しやデータ処理の完了、社内ダッシュボードの数値の変化などです。広告の管理画面や在庫・予約の空き状況を見張らせる使い方も考えられます。

始め方は、まずブラウザ版で見張り役を1つ作り、通知先をDiscordかTelegramにすることです。日本語の画面をどこまで正しく読めるかは選ぶモデル次第なので、自分の画面で試してから使ってください。同じ日に紹介した推論エンジン「[Magnitude](/news/20261001-magnitude-self-optimizing-inference-engine/)」もOpenAI互換のAPIを持っており、つなぎ先の候補になります。

## 日本のビジネスへの影響

Observer AIは無料で、日本からも使えます。ただし電話・WhatsApp・SMSの通知は作者側での登録が必要で、SMSは米国とカナダには送れません。

関係が深いのは、管理画面の前で数字の変化を待つことが多い広告運用者や、書き出し待ちの多い動画制作者です。見張りをAIに任せれば、画面に張り付く時間を減らせます。

今すぐやれるのは、毎日確認している画面を1つ選び、「この数字が変わったら知らせる」見張り役をブラウザ版で作ってみることです。

注意点は2つあります。1つは情報の流れです。AIの判断は手元で行いますが、メールやTelegramの通知はObserverのアカウントやボットを通じて送られ、画面の画像を添付すると、その画像も外部のサービスを通ります。顧客情報が映る画面には使わないでください。もう1つは自動クリックです。チケットや限定商品の購入ボタンを自動で押す使い方は、販売サイトの規約で禁止されている場合があります。ローカルのAIモデルの選び方は「[ローカルLLM・オープンウェイトモデルのおすすめ](/best/local-llm/)」にまとめています。
