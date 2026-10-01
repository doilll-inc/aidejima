---
{
  "title": "Observer AIは画面を見張って知らせるローカルAIアプリ、作者の母親も設定できる手軽さに",
  "description": "個人開発者が1年かけて作ったオープンソースアプリObserver AIが話題だ。画面やカメラをローカルのAIに見張らせ、変化があれば電話やメールで知らせる。9月公開のv3.0.0で、作者の母親が初めて自分で設定できた。",
  "date": "2026-10-01T17:49:00+09:00",
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
  "editor_note": ""
}
---
個人開発者のRoy Medina氏が作るオープンソースのアプリ「Observer AI」が、ローカルLLM（手元のパソコンで動かすAIモデル）の利用者が集まる掲示板r/LocalLLaMAで話題になっています。画面やカメラを手元のAIに見張らせ、「〇〇が起きたら知らせる」を自動化するアプリです。作者は9月29日の投稿で、9月18日に公開したv3.0.0で、母親が初めて自分で見張り役のエージェントを設定できたと報告しました。

## 何を作ったか

Observer AIの考え方は「XになったらYをする」です。公式サイトとGitHubの説明には、次のような使い方が並びます。

- ダウンロードが終わったらSMSで知らせる
- レンダリング（動画や3DCGの書き出し）が終わったらWhatsAppで知らせる
- ダッシュボードの表示が変わったらメールを送る
- カメラに人が映ったらTelegramで知らせる
- 気が散っていたら電話をかける

:::quote https://observer-ai.com/ | Observer AI公式サイト
> The agent that monitors your screen, so you don't have to.
あなたの代わりに画面を見張るエージェント。
:::

見張る対象（センサー）は、画面のスクリーンショット、画面の文字読み取り（OCR）、カメラ、クリップボード、マイクや画面の音声の文字起こしなどです。知らせ方（ツール）は、Discord、Telegram、メール、電話、WhatsApp、SMS、画面への通知、録画の開始と停止、マウスのクリックまで用意されています。r/LocalLLaMAの投稿では「コンサートのチケットが出たら購入ボタンを押す」という例も挙げています。

{{youtube:https://www.youtube.com/watch?v=NCaWVOprZwE}}

## どう作ったか

見張り役は「マイクロエージェント」と呼ぶ小さな部品で、センサー、AIモデル、ツールの3つでできています。たとえば「画面にObserverのロゴがあればOBSERVERと答え、なければCONTINUEと答えて」という指示を、決めた間隔で画面の画像と一緒にAIへ渡します。返事にOBSERVERが含まれていれば、JavaScriptのコードがメールを送る、という仕組みです。

今の版では、このエージェントを手で組む必要が減りました。司令役のエージェント「Observer」に見張りたい内容を文章で伝えると、Observerが道具の連携規格MCPを通じて設定を組み立てます。作者は、仕組みは面白いが設定が手作業すぎるという掲示板の声を受け、1年かけて誰でも使えるようにしてきたと書いています。数か月ごとに母親に試してもらい、今回初めて母親がローカルのモデルで見張り役を設定できたことを、作者は「mom benchmark（母親ベンチマーク）」に合格したと表現しました。

AIの処理は手元で行います。デスクトップアプリはllama.cppを内蔵し、ブラウザ版はtransformers.jsでGoogleの小型モデルGemma 4 E2Bをブラウザの中で動かすため、インストールなしで試せます。OllamaなどOpenAI互換のサーバーにもつなげます。ライセンスはAGPLv3です。作者は投稿で、中核部分は今後も無料のオープンソースのままにすると約束し、「if it's free for me, it should be free for the user（自分にとって無料なら、利用者にも無料であるべき）」と書いています。

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
