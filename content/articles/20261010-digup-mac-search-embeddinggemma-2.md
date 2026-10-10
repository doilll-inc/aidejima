---
{
  "title": "「シマウマが出てくる動画」と打つとその場面へ、Macの中身を言葉で探す無料アプリ",
  "description": "Macの写真・PDF・録音・動画を、覚えている内容を言葉で書くだけで探せる無料アプリ「DigUp」を個人開発者が公開した。Googleが10月6日に出した新しいAIを手元のMacで動かし、ファイルは外に出さない。初回に865MBのモデルを取り込む。",
  "date": "2026-10-10T23:26:00+09:00",
  "category": "usecases",
  "tags": ["DigUp", "EmbeddingGemma 2", "活用事例", "個人開発", "オープンソース", "Gemma"],
  "summary": [
    "個人開発者が、Macの写真・PDF・録音・動画を「覚えている内容」を言葉で書くだけで探せる無料アプリDigUpを公開した",
    "動画や録音はその場面の秒数から、PDFは該当のページから開く。Googleが10月6日に公開した無料のAIをMacの中だけで動かし、ファイルは外に送らない",
    "意味での検索は100以上の言語に対応するが、日本語は請求書番号のような言葉の完全一致の検索が弱いと作者が明記している"
  ],
  "sources": [
    {"title": "DigUp（README）", "publisher": "GitHub ARahim3", "url": "https://github.com/ARahim3/DigUp", "kind": "公式サイト"},
    {"title": "EmbeddingGemma 2: an open, lightweight multimodal embedding model", "publisher": "Google", "url": "https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2", "kind": "公式発表"},
    {"title": "google/embeddinggemma-2", "publisher": "Hugging Face（Google）", "url": "https://huggingface.co/google/embeddinggemma-2", "kind": "公式ドキュメント"},
    {"title": "Open-source Mac app that runs EmbeddingGemma 2 locally to search your files by what's in them", "publisher": "Reddit r/LocalLLaMA", "url": "https://www.reddit.com/r/LocalLLaMA/comments/1x2eeds/opensource_mac_app_that_runs_embeddinggemma_2/", "kind": "コミュニティ"}
  ],
  "thumb_text": "DigUp",
  "thumb_style": "photo",
  "thumb_prompt": "A laptop on a messy home desk whose screen shows a paused video frame of a zebra, while a small shovel rests on the keyboard as if it had just dug the clip out of a mountain of paper folders piled behind it.",
  "share_text": "「シマウマが出てくる動画」「ペットについての契約の条項」と打つとその場面やページへ。Macのファイルを中身で探す無料アプリ",
  "editor_note": ""
}
---
Macに保存した写真・PDF・録音・動画を、ファイル名ではなく「覚えている内容」を言葉で書くだけで探せる無料アプリ「DigUp」を、個人開発者のアブドゥル・ラヒム氏がGitHubで公開しました。「シマウマが出てくる動画」と打てば動画がその場面から再生され、「賃貸契約のペットの条項」と打てばPDFの該当ページが開きます。Googleが現地時間10月6日に公開した新しいAIを、Macの中だけで動かしています。

## 何を作ったのか

DigUpとは、Macのメニューバーに常駐し、選んだフォルダーの中身を読み込んでおいて、言葉で探せるようにするアプリです。どのアプリを開いていても、キーボードの組み合わせ（Shift＋Command＋スペース）で検索窓が出ます。READMEに載っている例は、たとえば次のようなものです。

- 「睡眠について話しているところ」→ ポッドキャストの録音のその分の位置へ
- 「浜辺の犬」→ 写真、「支払いが拒否されたエラー」→ その画面のスクリーンショット
- 英語で検索して、ベンガル語やアラビア語で書いたメモが見つかる

請求書番号やエラーコード、人名のような「その文字そのもの」も、ファイル名・文書の本文・スクリーンショット内の文字から探します。意味で探す検索と、文字で探す検索を組み合わせた作りです。MacにもとからあるSpotlightとの違いについて、作者は、Spotlightは名前や文字で探すのに対し、DigUpは写っているものや話している内容でも探し、該当のページや場面まで連れていく点だと説明しています。

## どう作ったか

中心にあるのは、Google DeepMindが10月6日に無料で公開したAI「EmbeddingGemma 2」です。文章・画像・音声・動画を同じ「意味の地図」の上に並べるための部品で、「浜辺の犬」という言葉と浜辺の犬の写真が、地図の上で近い位置に置かれます。

:::quote https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2 | Google公式ブログ「EmbeddingGemma 2」
> EmbeddingGemma 2 is the most capable model for on-device multimodal embeddings, natively mapping combinations of text, images, audio, and video into a unified embedding space.
EmbeddingGemma 2は、端末の中で動かす多種類のデータ向けの埋め込みモデルとして最も高性能で、文章・画像・音声・動画の組み合わせを、1つの共通の空間にそのまま対応づける。
:::

モデルの大きさは7億4,000万パラメーター（AIの規模を表す数）で、Googleはスマホやノートパソコンでも動く設計だとしています。商用利用もできるApache 2.0という条件で公開されています。

DigUpは、このモデルをMacのGPU（画像処理用の半導体）で動かす無料の仕組みに載せ、写真やPDFのページ、動画のコマ、30秒ごとに区切った音声を1つずつ地図に並べて、1つのファイルに保存します。検索するときは、打った言葉を同じ地図に置き、近くにあるものを探す流れです。初回のダウンロードはモデルの865MBで、アプリ本体は約20MBです。作者はMITライセンス（誰でも無料で使え、改変もできる条件）でコードも公開しました。

## 中身はMacの外に出ない

DigUpは、読み込んだファイルを外部のサーバーに送りません。

:::quote https://github.com/ARahim3/DigUp | DigUp README（GitHub）
> Nothing you index leaves your Mac. DigUp goes online only to download the model once and to check for updates once a day.
読み込んだものは何ひとつMacの外に出ない。DigUpがネットにつなぐのは、最初にモデルを1回ダウンロードするときと、1日1回の更新確認のときだけだ。
:::

アカウント登録は不要で、利用状況の送信もないとしています。パスワードや鍵のファイル、隠しフォルダー、iCloudにしか置かれていないファイルは読みません。読むだけで、ファイルを動かしたり書き換えたりはしないと書かれています。

最初の読み込みは、数百ファイルなら数分、大きなダウンロードフォルダーだと1時間ほどかかるとのことです。そのあとは新しいファイルを1〜2秒で検索できるようになります。動作には、Appleの独自チップを積んだMac（M1以降）とmacOS 14以降が必要です。

## 反応と論点

作者は開発者向け掲示板Redditのr/LocalLLaMAで公開を知らせました。GitHubでは公開から2日足らずで数十のスターを集めた段階で、まだ広く使われているとは言えません。Googleのモデルが出てから数日で、こうした手元で動く検索アプリが個人の手で作られた点が目を引きます。AIデジマでも、[Macの写真と動画を言葉で探すSCM](/news/20261005-scm-mac-local-photo-video-ai-search/)や、[ネットにつながず会議メモを清書するGoogleのForesight](/news/20261009-google-ai-edge-foresight-offline-meeting-notes/)を取り上げてきました。「AIに見せたいが、外には出したくない」という需要に応える道具が増えています。

日本語には注意点があります。作者は、意味での検索は100以上の言語で使えるとする一方、試験したのは英語・ベンガル語・アラビア語だけだと書いています。また、日本語や中国語のように単語の間に空白がない言語は単語に区切れないため、請求書番号や名前などの「文字そのもの」での検索が弱いと明記しています。モデルの性能が言語によって同じではないことは、Google自身も断っていると作者は書いています。

## 日本のビジネスへの影響

- **使えるか**: 日本からも無料でダウンロードできます。必要なのはApple独自チップのMacとmacOS 14以降です。日本語の資料も意味で探せる見込みですが、日本語での精度は作者も確かめていません
- **誰にどう効くか**: 撮りためた写真や動画素材を抱える広報・マーケティング担当者、会議の録音や契約書のPDFが積み上がっている営業や法務の担当者に向きます。「あの話をしていた会議の録音」「あの条項がある契約書」を、ファイル名を覚えていなくても探せます
- **今すぐやれること**: まずは社外秘を含まない写真や動画のフォルダー1つだけを選んで読み込ませ、日本語で「赤い看板が映っている写真」のように探して、どこまで当たるかを試してください
- **注意点**: 個人が公開して数日のアプリで、企業での導入実績はありません。社内のPCに入れる前に、情報システム部門の許可を取ってください。中身は外に出ない設計ですが、更新確認のための通信はあります（設定で止められます）

手元のPCで動かせる無料のAIの選び方は、[ローカルLLM・オープンウェイトモデルのおすすめ](/best/local-llm/)にまとめています。
