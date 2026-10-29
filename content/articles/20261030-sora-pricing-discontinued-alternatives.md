---
{
  "title": "Soraの料金、今は払っても使えない 4月にアプリが終了、代わりの動画AIは月725円から",
  "description": "OpenAIの動画生成AI「Sora」は、アプリとWeb版が2026年4月26日、開発者向けのAPIが9月24日に終わり、今は料金を払っても使えない。作った動画の書き出し方と、代わりに使える動画AIの料金を10月30日時点の公式ページでまとめた。",
  "date": "2026-10-30T01:20:00+09:00",
  "category": "products",
  "format": "howto",
  "tags": ["Sora", "Sora 2", "OpenAI", "料金", "動画生成", "Gemini"],
  "summary": [
    "OpenAIの動画生成AI「Sora」は、アプリとWeb版が2026年4月26日、API（開発者向けの接続口）が9月24日に終了し、いまは有料でも使えない",
    "Soraで作った動画は、専用ページから書き出しを申し込めばメールで受け取れる。OpenAIは書き出しの期間のあとにデータを完全に消すとしている",
    "代わりにはGoogleのGemini（月725円のプランから動画生成）や、Runway（月15ドルから）などがある"
  ],
  "sources": [
    {"title": "What to know about the Sora discontinuation", "publisher": "OpenAI Help Center", "url": "https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation", "kind": "公式ドキュメント"},
    {"title": "Deprecations", "publisher": "OpenAI API Docs", "url": "https://developers.openai.com/api/docs/deprecations", "kind": "公式ドキュメント"},
    {"title": "Sora 2 is here", "publisher": "OpenAI", "url": "https://openai.com/index/sora-2/", "kind": "公式発表"},
    {"title": "Google AI プラン", "publisher": "Google（日本向け料金ページ）", "url": "https://gemini.google/jp/subscriptions/?hl=ja", "kind": "公式ドキュメント"},
    {"title": "Pricing", "publisher": "Runway", "url": "https://runway.com/pricing", "kind": "公式サイト"},
    {"title": "Kling AI Membership Plan", "publisher": "Kling AI", "url": "https://kling.ai/app/membership/membership-plan", "kind": "公式サイト"},
    {"title": "OpenAI sets two-stage Sora shutdown with app closing April 2026 and API following in September", "publisher": "The Decoder", "url": "https://the-decoder.com/openai-sets-two-stage-sora-shutdown-with-app-closing-april-2026-and-api-following-in-september/", "kind": "報道"},
    {"title": "OpenAI is shutting down Sora, its powerful AI video app", "publisher": "VentureBeat", "url": "https://venturebeat.com/technology/openai-is-shutting-down-sora-its-powerful-ai-video-app", "kind": "報道"}
  ],
  "thumb_prompt": "A miniature movie theater with its marquee lights switched off and a tiny closed shutter at the ticket booth, while across the street a brightly lit new cinema has a small line of tiny people waiting.",
  "thumb_style": "diorama",
  "thumb_text": "Sora 料金",
  "share_text": "Soraの料金は？ 答えは「もう払えない」。アプリは4月、APIは9月に終了。動画の書き出し方と代わりの動画AIの料金をまとめました",
  "editor_note": ""
}
---
Soraの料金は、2026年10月30日時点では「払っても使えない」が答えです。OpenAIの動画生成AI「Sora」は、スマートフォンのアプリとWeb版が2026年4月26日に、開発者向けのAPI（ほかのサービスから呼び出す接続口）が9月24日に提供を終えました。この記事では、Soraが何だったのか、手元の動画を取り出す方法、代わりに使える動画AIの料金を公式ページで確かめてまとめます。

## Soraとは何だったか

Soraとは、文章で指示すると動画を作るOpenAIのAIです。最初のモデルは2024年2月に発表され、2025年秋に後継の「Sora 2」と、同じ名前のSNS型アプリ「Sora」が公開されました。Sora 2は映像と同時に効果音やセリフも作れ、アプリでは自分の姿と声を登録して動画に登場させる「characters」という機能が話題になりました。

いまOpenAIの発表ページを開くと、冒頭に終了を知らせる一文が加えられています。

:::quote https://openai.com/index/sora-2/ | OpenAI公式「Sora 2 is here」
> As of April 26, 2026, the Sora product is no longer available.
2026年4月26日をもって、Soraの製品は利用できなくなりました。
:::

## 終了の日程

終了は2段階でした。OpenAIの公式ヘルプと開発者向けの廃止予定一覧に書かれた日付は次のとおりです。

| 対象 | 終了日 | 確認先 |
|---|---|---|
| Soraのアプリ・Web版 | 2026年4月26日 | OpenAI公式ヘルプ |
| SoraのAPI（sora-2・sora-2-pro など） | 2026年9月24日 | OpenAI API の廃止一覧 |

開発者向けの廃止一覧では、Sora 2の各モデルと動画用のAPIについて「代わりのモデル」の欄が空欄になっています。OpenAIとして、Soraの後を継ぐ動画生成サービスは示していません。

{{card:https://developers.openai.com/api/docs/deprecations|Deprecations|OpenAI API Docs}}

終了の発表は3月24日でした。VentureBeatによると、OpenAIの広報担当者は計算資源（AIを動かすコンピューター）の需要が増すなかで事業を絞ると説明し、Soraの研究チームはロボットの研究につながる「世界のシミュレーション」の研究を続けるとしています。The Decoderは、アプリとAPIを時期をずらして閉じる2段階の日程を伝えました。

## 作った動画を取り出すには

Soraで作った動画は、まだ書き出しを申し込めます。公式ヘルプが示す手順は次のとおりです。

1. ブラウザで sora.chatgpt.com/sunset を開き、Soraに使っていたアカウントでログインする
2. 「Export」を押す
3. 準備ができるとメールが届くので、案内に沿ってダウンロードする

公式ヘルプは、できるだけ早く書き出すよう勧めています。データの扱いについては、次のように書かれています。

:::quote https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation | OpenAI Help Center「What to know about the Sora discontinuation」
> After Sora is discontinued, and after the period of time of any final export window passes (if we are able to offer one), we will permanently delete any data associated with your use of Sora.
Soraの提供終了後、最終的な書き出し期間を設けられた場合はその期間が過ぎたあとに、Soraの利用に関するデータをすべて完全に削除します。
:::

最終の書き出し期間を設けるかどうかは決まっておらず、設ける場合は事前にメールで知らせるとしています。いつ消えるかが読めないため、残したい動画がある人は先に書き出しておくのが安全です。

## 代わりに使える動画AIと料金

Soraの代わりになる、文章から動画を作るサービスの料金です。10月30日時点で各社の公式料金ページを確認しました。

| サービス | 無料で使えるか | 有料プラン |
|---|---|---|
| Gemini（Google。アプリとGoogle Flowで「Gemini Omni Flash」を使う） | アプリでの動画生成は有料プランから | Google AI Plus 月725円（Flowクレジット200）、Pro 月2,900円（同1,000）、Ultra 月14,500円から |
| Runway | 1回きりの125クレジットで試せる | Standard 月15ドル（625クレジット＝Gen-4.5で約52秒分）、Pro 月35ドル、Max 月95ドル |
| Kling AI | 今回は公式ページで確認できず | 料金ページの表示は「Plans from $6.99」（月6.99ドルから） |

Googleは日本向けの料金を円で出しています。クレジットは動画を作るたびに減る「回数券」のようなもので、動画の長さや画質で使う量が変わります。Runwayの使い方は[Runwayの使い方と料金](/news/20261027-runway-how-to-use-pricing/)で、Klingの最新版は[Kling 4.0の記事](/news/20261020-kling-4-0-30-second-video/)で詳しく書いています。

## 仕事での使いどころ

- **SNS担当者**: Soraで作っていた短い動画の代わりに、Geminiの有料プランで短い動画を作り、投稿の下書きとして社内で見せる
- **広告運用者**: 商品写真から動画を作れるRunwayやKlingで、広告の動画を数パターン作り、どれが反応するかを試す
- **営業・企画**: 提案書に入れるイメージ動画を作る。完成品ではなく「たたき台」として使うと、制作会社への依頼もしやすくなる

## 日本のビジネスへの影響

- **使えるか**: Soraは日本を含むすべての地域で使えなくなっています。Soraのために続けていた契約があれば、ChatGPTのプランを含めて見直す時期です。代わりのGeminiは日本向けに円建てで提供されています。RunwayとKlingはドル建てです。
- **誰にどう効くか**: Soraで動画素材を作っていたSNS担当者や広告運用者は、作り方を別のサービスに移す必要があります。社内マニュアルや研修資料に「動画はSoraで」と書いていれば書き換えが要ります。
- **今すぐやれること**: まず sora.chatgpt.com/sunset でSoraの動画を書き出しましょう。そのうえで、GeminiのPlus（月725円）かRunwayの無料クレジットで、これまでSoraで作っていた動画を1本作り直し、仕上がりを比べるのが手堅い進め方です。
- **注意点**: 動画AIはサービスごとに、作った動画を商用で使える条件が違います。無料枠の動画に透かしが入ったり、商用利用が有料プランだけだったりするので、広告に使う前に各社の規約を確かめてください。Soraのように、サービスそのものが急に終わることもあります。大事な動画は手元に保存しておきましょう。

各社の画質の評価や商用利用の条件は[動画生成AIのおすすめ](/best/video-generation/)で比べています。
