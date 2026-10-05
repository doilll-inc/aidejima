---
{
  "title": "MicrosoftがMAI-Transcribe-2-Streamingを公開、音声エージェント向けに聞く・話すを高速化",
  "description": "Microsoft AIが逐次文字起こしのMAI-Transcribe-2-Streamingと音声合成のMAI-Voice-2.1・2.1-Flashを公開した。文字起こしは60言語で年末まで1時間$0.54。音声合成は23言語だが、現時点で日本語の音声はない。",
  "date": "2026-10-02T19:10:00+09:00",
  "category": "models",
  "tags": ["Microsoft", "MAI-Transcribe-2-Streaming", "MAI-Voice-2.1", "文字起こし", "音声合成", "エージェント"],
  "summary": [
    "Microsoft AIは現地時間10月1日、話している最中に文字を返すMAI-Transcribe-2-Streamingと、音声合成のMAI-Voice-2.1・2.1-Flashを公開した",
    "MAI-Transcribe-2-Streamingは日本語を含む60言語に対応し、料金は年末までの導入価格で音声1時間あたり$0.54",
    "MAI-Voice-2.1は100万文字$22、Flashは$15だが、対応23言語の音声一覧に日本語は含まれていない"
  ],
  "sources": [
    {"title": "Our first streaming transcription model debuts at no. 1 on Artificial Analysis", "publisher": "Microsoft AI", "url": "https://microsoft.ai/news/our-first-streaming-transcription-model/", "kind": "公式発表"},
    {"title": "MAI-Transcribe-2-Streaming overview", "publisher": "Microsoft Learn", "url": "https://learn.microsoft.com/en-us/azure/ai-services/speech-service/mai-transcribe-2-streaming", "kind": "公式ドキュメント"},
    {"title": "Use MAI-Transcribe-2-Streaming with the Realtime API", "publisher": "Microsoft Learn", "url": "https://learn.microsoft.com/en-us/azure/ai-services/speech-service/mai-transcribe-2-streaming-realtime", "kind": "公式ドキュメント"},
    {"title": "MAI-Voice-2.1 and MAI-Voice-2.1-Flash", "publisher": "Microsoft Learn", "url": "https://learn.microsoft.com/en-us/azure/ai-services/speech-service/mai-voices", "kind": "公式ドキュメント"},
    {"title": "Microsoft AI の投稿", "publisher": "X @MicrosoftAI", "url": "https://x.com/MicrosoftAI/status/2105693024013467905", "kind": "X投稿"},
    {"title": "Microsoft targets ultra-realistic voice agents with its first streaming transcription model", "publisher": "SiliconANGLE", "url": "https://siliconangle.com/2026/10/01/microsoft-targets-ultra-realistic-voice-agents-with-its-first-streaming-transcription-model/", "kind": "報道"},
    {"title": "Microsoft AI releases new transcription and text-to-speech models for voice agents", "publisher": "The Decoder", "url": "https://the-decoder.com/microsoft-ai-releases-new-transcription-and-text-to-speech-models-for-voice-agents/", "kind": "報道"}
  ],
  "thumb_text": "MAI-Transcribe-2",
  "share_text": "MicrosoftがMAI-Transcribe-2-Streamingと音声合成MAI-Voice-2.1を公開。文字起こしは1時間$0.54",
  "thumb_style": "3d",
  "thumb_prompt": "A pair of headphones and a microphone facing each other, with a ribbon of sound waves flowing from the mic and instantly turning into a ribbon of abstract text-like dashes.",
  "editor_note": ""
}
---
Microsoft AIは現地時間10月1日、話している最中に文字を返す初の逐次（ストリーミング）文字起こしモデル「MAI-Transcribe-2-Streaming」と、音声合成モデル「MAI-Voice-2.1」「MAI-Voice-2.1-Flash」を公開しました。文字起こしは日本語を含む60言語に対応し、年末までの導入価格は音声1時間あたり$0.54です。狙いは、聞いて考えて話す「音声エージェント」の待ち時間を両端で縮めることです。

## 何が発表されたか

3つのモデルは、音声の入り口と出口を受け持ちます。いずれもMicrosoft Foundryで公開プレビューとして提供され、Microsoftの試用サイトMAI PlaygroundやOpenRouterからも使えるとしています。

| モデル | 役割 | 公式の料金 | 言語 |
|---|---|---|---|
| MAI-Transcribe-2-Streaming | 逐次文字起こし | 音声1時間$0.54（年末までの導入価格） | 60言語（日本語あり） |
| MAI-Voice-2.1 | 高品質の音声合成 | 100万文字$22 | 23言語（日本語なし） |
| MAI-Voice-2.1-Flash | 低遅延の音声合成 | 100万文字$15 | 23言語（日本語なし） |

MAI-Transcribe-2-Streamingとは、音声を流し続けながら、途中経過の文字を随時受け取れる音声認識モデルです。従来のMAI-Transcribe-2が録音済みの音声をまとめて処理するのに対し、こちらは通話や会議の最中に字幕を出す用途を想定しています。

:::quote https://learn.microsoft.com/en-us/azure/ai-services/speech-service/mai-transcribe-2-streaming | Microsoft Learn「MAI-Transcribe-2-Streaming overview」
> MAI-Transcribe-2-Streaming is a low-latency speech-to-text model for real-time transcription. Send audio as a continuous stream and receive incremental transcripts while the speaker talks.
MAI-Transcribe-2-Streamingは、リアルタイムの文字起こし向けの低遅延な音声認識モデルです。音声を連続したストリームとして送ると、話者が話している間に少しずつ文字起こし結果を受け取れます。
:::

Microsoftの発表によると、最初の仮の結果はおよそ100ミリ秒で返り、話が進むにつれて文脈に合わせて書き直したうえで確定させます。第三者の評価サイトArtificial Analysisでは、確定後の文字起こしと途中経過の両方の正確さで1位になったと説明しています。言語は自動で判定し、途中で言語が切り替わっても追いかけます。

接続方法は、OpenAIのRealtime APIに近い形式のWebSocketか、Azure Speech SDKの2通りです。1回の接続は最長1時間で、ドキュメントに載っている提供リージョンはスウェーデン中部・米国中部・インド南部（米国東部2は近日）です。ドキュメントは「世界中から利用でき、これらのリージョンに振り分ける」としています。

{{card:https://learn.microsoft.com/en-us/azure/ai-services/speech-service/mai-transcribe-2-streaming-realtime|Use MAI-Transcribe-2-Streaming with the Realtime API|Microsoft Learn}}

音声合成のMAI-Voice-2.1は、1つの声のまま複数の言語を、それぞれの言語らしい発音で話せるのが特徴です。Flash版は応答の速さを優先した版で、Microsoftは45秒分の音声を生成する場合でも、話し始めまでの遅延は150ミリ秒だとしています。どちらも5〜60秒の音声から声を再現する機能を備えますが、本人の同意を得た声しか使えない仕組みで、利用には申請と審査が必要です。

:::quote https://learn.microsoft.com/en-us/azure/ai-services/speech-service/mai-voices | Microsoft Learn「MAI-Voice-2.1 and MAI-Voice-2.1-Flash」
> MAI-Voice-2.1 produces natural, expressive speech from text or a short reference clip, with built-in guardrails ensuring only authorized, consented voices can be used.
MAI-Voice-2.1は、テキストや短い参照音声から自然で表現豊かな音声を生成し、許可と同意を得た声だけが使えるよう安全策を組み込んでいます。
:::

## 背景

Microsoftは自社開発のMAIシリーズを増やしています。録音済みの音声を処理するMAI-Transcribe-2はすでにFoundryで提供しており、今回はそこに「逐次処理」と「声の出力」を足して、音声エージェントに必要な部品をそろえた形です。

SiliconANGLEは、この動きを外部のモデル提供元への依存を減らす戦略の一部と位置づけています。Microsoft AIを率いるムスタファ・スレイマン氏が、Anthropicへの支払いを減らし、最終的になくすことが目標だと6月のBloombergの取材で語っていたことも紹介しています。

## 反応と論点

Microsoft AIの公式アカウントはXで3モデルを紹介し、正確な逐次文字起こしと、会話の切り替わりの待ち時間を減らす自然な音声で、会話が途切れない音声エージェントを作れると呼びかけました。

{{x:https://x.com/MicrosoftAI/status/2105693024013467905}}

発表の数字はMicrosoft自身が示したものが中心です。「競合より2倍速く文字が出る」「Flashは同等のモデルより約60%安い」といった比較は、比べた相手や条件をMicrosoftの発表だけでは細かく確かめられません。3モデルとも公開プレビューで、ドキュメントはSLA（稼働の保証）がなく本番運用には勧めないと明記しています。

The Decoderは、4000人を対象にした聞き取りテストで、約半数がMAI-Voiceの声を本物の人間だと思ったとMicrosoftが説明したと報じています。声の自然さは、なりすましへの悪用とも隣り合わせです。Microsoftは声の再現を申請制にすることで、この懸念に対応しようとしています。

## 日本のビジネスへの影響

使えるかどうかは、モデルで分かれます。MAI-Transcribe-2-Streamingは対応言語の表に日本語（ja）があり、日本からも使えます。一方でMAI-Voice-2.1の音声一覧は英語・中国語・韓国語・ヒンディー語などの23言語で、日本語の声は現時点で入っていません。リージョンの表には東日本（Japan East）がありますが、これは処理する拠点の話で、日本語を話せるという意味ではありません。

関係が深いのは、コールセンターや会議の字幕を作る開発者と、電話応対を自動化したいCS（顧客サポート）部門です。通話をその場で文字にして要約やFAQ検索につなぐ構成なら、文字起こしの部分をすぐ試せます。今すぐやれることは、自社の通話録音を数本MAI Playgroundに通し、専門用語や固有名詞の誤りを今のエンジンと比べることです。

注意点は3つあります。$0.54は年末までの導入価格で、来年以降の料金は発表されていません。公開プレビューなので、本番の電話窓口に入れるのは正式提供を待つほうが安全です。日本語で話し返す部分は、当面は別の音声合成を組み合わせる必要があります。文字起こしと音声合成の各サービスの料金や日本語対応は、[文字起こしAIのおすすめ](/best/transcription/)にまとめています。
