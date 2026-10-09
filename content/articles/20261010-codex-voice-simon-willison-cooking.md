---
{
  "title": "Codexに料理しながら話しかけてブログの新機能を完成、米国の著名開発者が30分の音声作業を公開",
  "description": "米国の開発者サイモン・ウィリソン氏が、ChatGPTのデスクトップアプリにあるCodexに夕食を作りながら声で指示し、約30分でブログの新ページをほぼ完成させた。仕上げには文字入力でさらに30分かかったという。",
  "date": "2026-10-10T03:50:00+09:00",
  "category": "usecases",
  "tags": ["Codex", "ChatGPT", "OpenAI", "活用事例", "音声会話", "個人開発"],
  "summary": [
    "米国の開発者サイモン・ウィリソン氏が、OpenAIのCodexに料理中に声だけで指示し、ブログの新しいページを作った",
    "声での作業は夕食づくりの約30分で、ほぼ公開できる状態に。点検と手直しは文字入力に切り替えてさらに約30分",
    "本人は「同時に別のことができるのが最大の利点」としつつ、細かい修正は今もキーボードの方が速いと書いている"
  ],
  "sources": [
    {"title": "A new feature for my blog, built using my voice", "publisher": "Simon Willison's Weblog", "url": "https://simonwillison.net/2026/Oct/9/built-using-my-voice/", "kind": "公式サイト"},
    {"title": "ChatGPT Voice is now in the desktop app", "publisher": "OpenAI Developer Community", "url": "https://community.openai.com/t/chatgpt-voice-is-now-in-the-desktop-app/1388031", "kind": "公式発表"},
    {"title": "OpenAI Developers の投稿", "publisher": "X @OpenAIDevs", "url": "https://x.com/OpenAIDevs/status/2080378875394289839", "kind": "X投稿"},
    {"title": "simonw/simonwillisonblog Pull Request #719", "publisher": "GitHub", "url": "https://github.com/simonw/simonwillisonblog/pull/719", "kind": "公式サイト"},
    {"title": "ChatGPT Voice experience gets a massive upgrade on desktop", "publisher": "Neowin", "url": "https://www.neowin.net/news/chatgpt-voice-experience-gets-a-massive-upgrade-on-desktop/", "kind": "報道"}
  ],
  "thumb_text": "Codex 音声",
  "thumb_style": "diorama",
  "thumb_prompt": "A miniature home kitchen where a tiny figure stirs a steaming pot on the stove while an open laptop on the counter builds a glowing web page by itself, with small speech bubbles floating from the cook toward the laptop.",
  "share_text": "夕食を作りながらCodexに話しかけ、30分でブログの新ページがほぼ完成。米国の著名開発者が手順を公開",
  "editor_note": ""
}
---
米国の開発者サイモン・ウィリソン氏は現地時間10月9日、OpenAIのAI開発ツール「Codex」に夕食を作りながら声で話しかけ、自分のブログに新しいページを作ったと公表しました。声だけの作業は料理にかかった約30分で、ほぼ公開できるところまで進んだといいます。

ウィリソン氏は生成AIの使い方を自分のブログで細かく検証し続けている開発者です。ブログはWebサービスを作る仕組み「Django」で自作しており、今回もそこに機能を足しました。

## 何を作ったか

作ったのは、これまで配信してきたメールマガジンを一覧で読めるページです。無料で毎週配信しているものと、支援者だけに毎月送っているものを、新しい順に並べて表示します。

本人のブログによると、声の指示で次のところまで仕上がりました。

- 配信記事を保存しておく入れ物（データベースの設計）と、管理画面
- 4つの取り込み口。メール配信サービスSubstackの新着と過去分、GitHubに公開している月刊号、非公開の最新号
- 一覧ページと年ごとのページ、サイト内検索への組み込み
- 日付別のページには出すが、タグ別のページやトップページには出さない、という細かい表示ルール

ページのデザインもAIが作り、ウィリソン氏が台所から画面をちらっと見て声で直させたと書いています。

:::quote https://simonwillison.net/2026/Oct/9/built-using-my-voice/ | Simon Willison's Weblog「A new feature for my blog, built using my voice」
> I built the feature almost entirely using my voice, chatting away to my laptop while I cooked dinner.
この機能は、夕食を作りながらノートPCに話しかけて、ほぼ声だけで作り上げた。
:::

## どう作ったか

使ったのは、ChatGPTのデスクトップアプリに入っているCodexの画面と、その音声会話の機能です。AIの頭脳にはOpenAIの上位モデル「GPT-6 Astra」を選んでいました。

手順は3段階でした。

1. **最初の一言だけ文字で打つ**: 「開発用のサーバーを起動してブラウザで開いて」と入力し、作業中のサイトを画面で確かめられるようにした
2. **音声会話に切り替えてキッチンへ**: ノートPCを台所に置き、料理しながら「この種類の記事はタグのページには出さない、日付のページには出す」といった要望を話した。AIはときどき質問を返しながらプログラムを書き換えた
3. **料理のあとは文字で仕上げ**: AIに変更をまとめさせ、GitHub上で中身を点検。非公開データの取り込み方が自分の希望と違ったため、文字の指示で直させた。この仕上げにさらに約30分かかった

ウィリソン氏は、言いよどみや言い直しも含めた会話の記録をそのまま公開しています。「えーと」「いや、やっぱり」が並ぶ話し言葉でも、AIは何を作りたいのかを読み取れたと書いています。変更の記録もGitHubで見られます。

{{card:https://github.com/simonw/simonwillisonblog/pull/719|simonw/simonwillisonblog Pull Request #719|GitHub}}

## 使った機能: ChatGPTデスクトップアプリの音声会話

この音声機能は、OpenAIが7月23日に提供を始めたものです。OpenAIの開発者コミュニティでの告知によると、声だけでパソコンを操作したり、ChatGPT WorkやCodexで動く複数のAIに指示を出したりできます。対象はmacOSとWindowsのアプリで、有料のPlus・Pro・Business・Edu・Enterpriseのプランです。

OpenAIの開発者向け公式アカウントは提供開始時、「声に出しながら作る」使い方を次のように紹介していました。1つの会話の中で新しい作業を始め、進み具合を確かめ、CodexとChatGPT Workの作業を操れるという内容です。

{{x:https://x.com/OpenAIDevs/status/2080378875394289839}}

## 本人の評価: 「毎日の道具ではない」が、ながら作業には強い

ウィリソン氏は、この使い方をいつもの作業の主役にするつもりはないと書いています。細かい修正の段階では、エラーの文面や例を貼りつけたり、直したい箇所を選んで示したりする方が、言葉で説明するより速いからです。

一方で、最大の利点は「同時に別のことができること」だと評価しています。料理中はいつもポッドキャストや動画を流していたが、その時間で実際にものを作れるようになった、というのが本人の実感です。在宅勤務だから成り立つ方法で、共有のオフィスでパソコンに話しかけ続けるのは無理だとも付け加えています。

ウィリソン氏は、OpenAIが開発者向けイベント「DevDay」などで声で指示するデモをよく使うことにも触れ、そうした場ではうまく見えると書いています（[DevDay 2026のまとめ](/news/20260930-openai-devday-2026-roundup/)）。今回の記録は、発表会のデモではなく、自分のサイトで公開までやり切った実例である点に価値があります。

## 日本で真似するなら

- **必要なもの**: ChatGPTのデスクトップアプリ（macOSかWindows）と、Plus以上の有料プラン。ChatGPT Plusは月3,000円で、追加料金なしでCodexも使えます（料金は[コーディングAIの比較ガイド](/best/coding/)に整理しています）
- **始め方の目安**: 最初の指示は文字で打ち、作っているものを画面で確認できる状態にしてから音声に切り替える。完成の判断と公開前の点検は、画面の前に座って行う
- **向いている作業**: 社内の一覧ページ、データの集計表、簡単な業務用ツールなど、作りたいものの形がはっきりしているもの

## 日本のビジネスへの影響

- **使えるか**: ChatGPTの音声会話は日本からも使えます。日本語で話しかけて同じ精度で動くかは、OpenAIの発表でもウィリソン氏の記事でも検証されていないため、まずは短い作業で試すのが無難です
- **誰にどう効くか**: 社内ツールを自分で作りたい企画・マーケティング担当者や、移動・家事の合間に作業を進めたい個人事業主に向きます。要望を声で並べ、仕上げだけ机で確認するという分担ができます
- **今すぐやれること**: 社内で使っている表計算の集計作業を1つ選び、「この表を読み込んで、毎週の数字をまとめる画面を作って」と声で頼んでみる。どこまで声で進み、どこからキーボードが必要になるかを測ると、自分の業務に合うかがわかります
- **注意点**: ウィリソン氏も、公開前のコードの点検は自分で画面を見て行いました。非公開データにつなぐための鍵（APIキー）の作成など、権限に関わる作業は声に任せず人が行うべきです。オープンな職場では、話した内容が周りに聞こえる点にも気をつけてください
