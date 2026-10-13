---
{
  "title": "Codexで眠っていたKindleを写真立てに改造、Claudeは安全対策で2回目の指示で停止",
  "description": "使わなくなった電子書籍端末Kindleを、OpenAIのCodexに頼んで写真立てに作り変えた開発者の記録がHacker Newsで129ポイントを集めた。ClaudeやGPT-5.6 Solでは途中で止まり、最後にGPT-6 Astraで完成した。",
  "date": "2026-10-13T12:20:00+09:00",
  "category": "usecases",
  "tags": ["Codex", "GPT-6 Astra", "活用事例", "個人開発", "Claude Opus 5.5", "安全性"],
  "summary": [
    "開発者のNiraj Rajgor氏は、使わなくなったKindleをOpenAIのCodexに頼んで改造し、10枚の写真を4分ごとに映す写真立てにした",
    "AnthropicのClaudeは安全対策で2回目の指示の後に止まり、GPT-5.6 Solも途中でつまずき、GPT-6 Astraで最後まで進んだ",
    "AIが端末の記録と画面を直接読める仕組みを作ってから作業が速く進んだと本人は振り返り、Hacker Newsでは賛否が分かれた"
  ],
  "sources": [
    {"title": "I turned my unused Kindle into a photo frame with GPT-6 Astra", "publisher": "Niraj Rajgor", "url": "https://nirajrajgor.com/blog/kindle-photo-frame-with-ai", "kind": "公式サイト"},
    {"title": "I turned my unused Kindle into a photo frame with GPT-6 Astra（コメント欄）", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=50064318", "kind": "コミュニティ"}
  ],
  "thumb_text": "Kindle×Codex",
  "thumb_style": "photo",
  "thumb_prompt": "An old black-and-white e-reader propped up on a wooden bookshelf like a picture frame, showing a grainy grayscale family beach photo, with a laptop glowing in the dark background covered in scrolling log text.",
  "share_text": "引き出しで眠っていたKindleを、Codexに頼んで写真立てに改造した開発者。Claudeは安全対策で途中停止",
  "editor_note": ""
}
---
引き出しで眠っていた電子書籍端末Kindleを、OpenAIのコーディングAI「Codex」に頼んで写真立てに作り変えた開発者の記録が、現地時間10月12日に開発者向け掲示板Hacker Newsで話題になりました。投稿は129ポイント、82件のコメントを集めています。作ったのは開発者のNiraj Rajgor氏で、AnthropicのClaudeでは安全対策に止められ、最後にOpenAIのGPT-6 Astraで完成させたと書いています。

## 何を作ったのか

Rajgor氏が改造したのは、第10世代の「Kindle」（いちばん安い基本モデル）です。今は木の棚に置かれ、10枚の写真を4分ずつ順番に映す写真立てとして毎日使われています。写真は端末の中に保存するため、Wi-Fiがなくても動きます。表示の時間や明るさを変えられ、Kindleがスリープから戻っても写真の表示が続きます。本を読みたいときは、元の読書画面に戻れます。

Kindleは本来、Amazonが用意した機能しか使えません。自作のアプリを動かすには、利用者が端末の制限を外す「脱獄（ジェイルブレイク）」が必要です。今回はKindleの改造に取り組む有志が公開している方法をもとにし、AIがその周りの道具をそろえました。本人は、この記事は手順書ではないと断っています。

:::quote https://nirajrajgor.com/blog/kindle-photo-frame-with-ai | Niraj Rajgor「I turned my unused Kindle into a photo frame with GPT-6 Astra」
> This was a personal experiment on my own Kindle, not a step-by-step jailbreak guide.
これは自分のKindleで試した個人的な実験で、脱獄の手順を1つずつ説明するガイドではない。
:::

## どう作ったか

作業はMacからWi-Fi経由だけで進め、ケーブルは使っていません。道具はOpenAIのCodexと、複数のAIを切り替えて使える開発ツール「T3 Code」です。プログラムはおもにPythonで書かれ、写真を映す部分と起動画面はC言語、インストールや端末の操作はシェルスクリプト（コマンドをまとめた簡単なプログラム）で作られました。

AIの選び方には試行錯誤がありました。最初に使ったGPT-5.6 Solは、端末の保存領域のエラーを解決できませんでした。次に試したAnthropicのClaude Fable 5.1とClaude Opus 5.5は、どちらもサイバーセキュリティ上の安全対策に引っかかり、2回目の指示の後で止まったといいます。最後にGPT-6 Astraに、個人で使うためのソフトであることと、公開されている有志のプロジェクトを参考にすることをはっきり伝えたところ、脱獄から完成まで進みました。

途中では、前の写真の跡が画面に薄く残る問題も起きました。Kindleの画面は電子ペーパー（電気を使わずに表示を保つ紙のような画面）のため、普通の液晶とは書き換え方が違います。AIが用意した自動テストではこれを見つけられず、最終的にKindleに備わる画面全体の書き換え機能を、写真を切り替えるたびに呼ぶことで解決しました。

## 作業を速くした「見える化」

Rajgor氏が最も効いたと振り返るのは、AIが自分で状況を確かめられる仕組みです。初めは本人が画面をスマートフォンで撮ってAIに見せていましたが、AIが端末とつながりっぱなしの診断用の接続を作り、記録（ログ）と画面の画像を直接読めるようにしてから、作業が一気に進んだといいます。本人はこの仕組みを転機と位置づけ、次は最初から用意すると書いています。

AIに仕事を任せるとき、結果を人が見て伝え直す手間がボトルネックになるという話は、[AI十数体にゲームの中身を復元させた開発者の記録](/news/20261012-ai-agents-decompile-shooter-game/)にも共通します。

## 反応と論点

Hacker Newsの反応は割れました。脱獄の方法自体はすでに有志が公開しているもので、「脱獄できた」という書き方は大げさだという指摘や、AIを次々に替える進め方は原因を絞り込む地道な調べ方とは違う、という批判がありました。

一方で、正当な改造でもClaudeやGPTに断られた経験を語る人が多く、ClaudeからCodexに乗り換えたという声もありました。AIが企業側の守りを固める道具にもなるという懸念に対し、企業の守りは1回勝負だが持ち主はいくらでも時間をかけられる、という反論も出ています。AIに改造が簡単にできるようになると、端末を安く売ってコンテンツで稼ぐ企業の商売に響くのではないか、という見方もありました。

AIの安全対策が「攻撃に使われそうな作業」をどこまで止めるかは、各社で判断が分かれています。同じ作業がClaudeでは止まりGPT-6 Astraでは通ったことは、その違いが利用者の手元で表れた一例です。

## 日本のビジネスへの影響

- **必要なもの**: Codex（ChatGPTのアカウントで使えます。料金は[Codexの料金と使い方](/news/20261011-codex-pricing-how-to-use/)にまとめています）と、改造してもよい自分の端末です。本人は作業時間や費用を書いていません。ほかのコーディングAIとの比較は[コーディングAIのおすすめと料金比較](/best/coding/)をご覧ください。
- **誰に効くか**: 店舗や受付で古いタブレットや端末を案内表示・掲示板として使い回したい、総務や店舗運営の担当者です。今回の手法そのものより、「AIに端末の記録と画面を直接読ませると作業が進む」という進め方が、社内の機器を相手にAIで小さな仕組みを作るときの参考になります。
- **今すぐやれること**: AIに何かを作らせるときは、まず「結果を自分で確かめられる仕組み（記録の読み取りや画面の撮影）を先に作って」と頼んでみてください。人が結果を見て伝え直す往復が減ります。
- **注意点**: 脱獄はメーカーの保証や利用規約に反する場合があり、端末が使えなくなるおそれもあります。本人も「自分の端末か、改造の許可を得た端末だけで試すこと」と書いています。会社の備品で試すのは避けてください。また、AIの安全対策で作業が止まったときに別のAIへ乗り換えるのは、止められた理由を確かめてからにすべきです。
