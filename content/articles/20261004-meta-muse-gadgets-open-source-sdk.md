---
{
  "title": "Muse Gadgetsは自作の端末にMetaのAIエージェントをつなぐOSS、ESP32やRaspberry Piで",
  "description": "MetaがAIエージェントMuseを自作の電子工作につなぐ「Muse Gadgets」のSDKとファームウェアをApache 2.0で公開した。ESP32の15ボードとRaspberry Piに対応し、自社製のMuse Home Linkも5,000台作った。",
  "date": "2026-10-04T02:00:00+09:00",
  "category": "dev",
  "tags": ["Meta", "Muse Gadgets", "Muse", "オープンソース", "エージェント", "ESP32"],
  "summary": [
    "MetaはAIエージェントMuseを自作の端末につなぐ「Muse Gadgets」のSDKとファームウェアを、Apache 2.0でGitHubに公開した",
    "ESP32向けは15種のボードで動作を確かめてあり、Linux向けはRaspberry Piなどを「Museが操作できる機械」に変える",
    "Metaは家電につなぐ自社製の小型端末Muse Home Linkを5,000台作り、Museの購読者に無料で配ると報じられている"
  ],
  "sources": [
    {"title": "facebookincubator/muse-gadget-sdk（README）", "publisher": "GitHub facebookincubator", "url": "https://github.com/facebookincubator/muse-gadget-sdk", "kind": "公式ドキュメント"},
    {"title": "ESP32 Device SDK（README）", "publisher": "GitHub facebookincubator", "url": "https://github.com/facebookincubator/muse-gadget-sdk/tree/main/esp32", "kind": "公式ドキュメント"},
    {"title": "Linux Device SDK（README）", "publisher": "GitHub facebookincubator", "url": "https://github.com/facebookincubator/muse-gadget-sdk/tree/main/linux", "kind": "公式ドキュメント"},
    {"title": "Nat Friedman の投稿（Muse Home Link）", "publisher": "X @natfriedman", "url": "https://x.com/natfriedman/status/2106099384891158562", "kind": "X投稿"},
    {"title": "Meta wants your next gadget to be Muse-infused", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/10/02/meta-wants-you-to-build-your-own-muse-gadget/", "kind": "報道"},
    {"title": "Meta open sources code to let you make Muse AI gadgets", "publisher": "The Verge", "url": "https://www.theverge.com/tech/1004330/meta-muse-ai-gadgets-home-link", "kind": "報道"},
    {"title": "Shopify Now Enrolls Your Store In Every New AI Shopping Channel", "publisher": "Search Engine Journal", "url": "https://www.searchenginejournal.com/shopify-now-enrolls-your-store-in-every-new-ai-shopping-channel/591049/", "kind": "報道"},
    {"title": "\"Muse Gadgets\" turns AI hardware into an open-source DIY project", "publisher": "The Decoder", "url": "https://the-decoder.com/muse-gadgets-turns-ai-hardware-into-an-open-source-diy-project/", "kind": "報道"}
  ],
  "thumb_text": "Muse Gadgets",
  "share_text": "MetaがAIエージェントMuseを自作端末につなぐSDKをOSSで公開。ESP32の15ボードとRaspberry Piに対応",
  "thumb_style": "photo",
  "thumb_prompt": "A maker's workbench with a bare green circuit board, a few jumper wires and a small round speaker that glows softly as if it is talking, close-up with a soldering iron blurred in the background.",
  "editor_note": ""
}
---
Metaは米国時間10月2日、AIエージェント「Muse」を自作の電子工作につなぐためのソフトウェア一式「Muse Gadgets」を、GitHubでオープンソースとして公開しました。マイコンボードESP32向けのファームウェアとSDK、Raspberry PiなどLinux機向けのSDKが入っており、ライセンスはApache 2.0です。あわせて、家の家電にMuseをつなぐ自社製の小型端末「Muse Home Link」を5,000台作ったことも明らかにしました。

## 何が発表されたか

Muse Gadgetsとは、画面やボタン、センサーを付けた手作りの端末を、スマートフォンのMuseアプリとペアリングして使えるようにする開発キットです。GitHubのREADMEは、趣旨を短く説明しています。

:::quote https://github.com/facebookincubator/muse-gadget-sdk | Meta「Muse Gadgets」README（GitHub）
> Muse gadgets are open source devices you build yourself.
Muse gadgetsは、自分で組み立てるオープンソースの端末だ。
:::

中身は2つに分かれます。

| SDK | 対象 | できること |
|---|---|---|
| ESP32 Device SDK | ESP32搭載のマイコンボード | 家のWi-Fiにつなぎ、画面に状態や画像を出す。ボタンを押して話しかける。対応ボードでは、家庭内ネットワークの機器にMuseが届く |
| Linux Device SDK | Raspberry Pi（3B+・4・5・Zero 2 W）やBluetooth LE付きのLinux機 | Museがコマンドを実行し、ファイルを動かす。センサーやWebhookを足して拡張する |

（出典：muse-gadget-sdkのREADME）

ESP32向けは、動作を確かめたボードが15種類あります。Espressifの開発ボードESP32-C5 DevKitC-1がいちばん手軽な入り口で、M5StackやSeeed、Waveshareの画面付きボードでは、アニメーションのキャラクターと押して話す操作まで動きます。Home Assistantの音声端末や、7.5インチの電子ペーパーにも対応しています。

組み立てにもAIを使う前提です。各フォルダーにはコーディングエージェント向けの説明書 `AGENTS.md` があり、READMEはMetaのコーディングエージェント「Muse Code」に「このファームウェアをビルドして書き込んで」と頼む手順を最初に案内しています。どの端末も、ペアリングにはMuseのアカウントで発行するSDKトークンが要ります。

## Muse Home Link

TechCrunchによるとMeta Superintelligence Labsで製品の責任者を務めるナット・フリードマン氏が、Xで自社製の端末Muse Home Linkを紹介しています。USB-Cで給電する小さな機器で、Museが家のネットワークにつながり、テレビやスピーカーなど、HTTPSで操作できる機器とやり取りできるようになるといいます。

{{x:https://x.com/natfriedman/status/2106099384891158562}}

同氏は投稿で、5,000台を製造したと書いています。TechCrunchとThe Decoderは、Museの購読者に在庫がなくなるまで無料で配り、数週間のうちに出荷すると報じています。

## 背景

Museは、Metaが9月8日に始めた個人向けのAIエージェントです。利用者に代わってフォームを埋め、旅行の予約や買い物までこなすと、TechCrunchやSearch Engine Journalが伝えています。Metaは手のひらサイズの専用端末Muse Charmを12月に発売する計画とも報じられています（[関連記事](/news/20261001-ai-tamagotchi-companion-devices/)）。

The Decoderは、作り手のコミュニティが何を作るかを見ることで、利用者が本当に欲しい端末の形をMetaが学べるとみています。AI専用の端末は、どんな形が正解かまだ定まっていません。TechCrunchは、Museをチャットのアプリにとどめず、中小企業や大企業にも広げるMetaの戦略に沿う動きだと伝えています。

## 反応と論点

READMEは、ボードが壊れたり保証が無効になったりする可能性を挙げ、「自己責任で」と念を押しています。とくにLinux向けは、SDKを入れたアカウントと同じ権限をMuseに渡す作りです。Museには、許可の範囲を超えて住所を伝えたといった報告が出ています（[関連記事](/news/20260930-meta-muse-permission-address-leak/)）。家の機器やサーバーを任せる前に、どこまで触らせるかを決めておく必要があります。

一方、ソースコードが公開されたことで、Museが端末に何を送り、何を実行するのかを利用者自身が確かめられるようになりました。GitHubのスターは、公開から1日足らずで700を超えました。

## 日本のビジネスへの影響

日本での提供については、今回の発表や報道では触れられていません。Muse Home Linkの配布も、Museの購読者が対象です。SDKはGitHubから誰でも入手できますが、使うにはMuseのアカウントとアプリが前提になります。

関係が深いのは、家電やIoT機器を手がける企業の開発者と商品企画の担当者です。市販のESP32ボードで「話しかけると動く家電」を試作できるため、自社製品とAIエージェントの組み合わせを社内で見せる材料になります。

今すぐやれることは、READMEのボード一覧と、各ボードのフォルダーにある説明を読み、自社の機器が家庭内ネットワークからHTTPで操作できるかを確かめることです。Museに限らず、エージェントから操作される側の準備になります。

注意点は2つです。端末のペアリングにはMetaのSDK利用規約への同意が要るため、製品に組み込む前に条件を確かめてください。また、Museに渡す権限は最小限にし、Linux機には専用のアカウントを作ってから入れるのが安全です。クラウドに送らず手元でAIを動かす選択肢は、[ローカルLLM・オープンウェイトモデルのおすすめ](/best/local-llm/)にまとめています。
