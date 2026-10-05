---
{
  "title": "Oídoは5ドルのマイコンで動く音声認識、Whisper tinyより低い誤り率をうたうOSS",
  "description": "スペインのLokutorが、マイコンESP32-S3だけで英語を文字起こしするオープンソースの音声認識「Oído」を公開した。LibriSpeechの単語誤り率は3.7%で、ノートPCで動かしたWhisper tiny.enの6.3%を下回ると公表している。",
  "date": "2026-10-01T17:48:00+09:00",
  "updated": "2026-10-01T18:55:00+09:00",
  "category": "usecases",
  "tags": ["Lokutor", "Oído", "活用事例", "文字起こし", "オープンソース"],
  "summary": [
    "スペインのLokutorが、5ドルのマイコンESP32-S3だけで英語を文字にする音声認識Oídoをオープンソースで公開した",
    "LibriSpeechの単語誤り率は3.7%と8.2%で、ノートPCのWhisper tiny.en（6.3%と15.9%）を下回ると作者は公表している",
    "速度は実機ではなくエミュレーターの命令数からの推定で、対応は英語のみ。コードはGPLv3で、商用ライセンスも用意する"
  ],
  "sources": [
    {"title": "Oído: speech recognition that fits in a $5 chip（README）", "publisher": "GitHub lokutor-ai", "url": "https://github.com/lokutor-ai/oido", "kind": "公式ドキュメント"},
    {"title": "Oído: Conformer-CTC Small, int8, for the ESP32-S3", "publisher": "Hugging Face lokutor-ai", "url": "https://huggingface.co/lokutor-ai/oido-ctc-small-int8", "kind": "公式ドキュメント"},
    {"title": "Commercial licensing（COMMERCIAL.md）", "publisher": "GitHub lokutor-ai", "url": "https://github.com/lokutor-ai/oido/blob/main/COMMERCIAL.md", "kind": "公式ドキュメント"},
    {"title": "Oído: Open-vocabulary speech recognition on a $5 ESP32-S3（Lokutorの投稿）", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=49907387", "kind": "公式発表"},
    {"title": "Oído: speech recognition that beats Whisper-tiny, running on a $5 microcontroller (open source)（Lokutorチームの投稿）", "publisher": "Reddit r/LocalLLaMA", "url": "https://www.reddit.com/r/LocalLLaMA/comments/1wu2jjy/oído_speech_recognition_that_beats_whispertiny/", "kind": "公式発表"}
  ],
  "thumb_text": "Oído",
  "share_text": "5ドルのマイコンESP32-S3で動く音声認識Oído。誤り率3.7%でWhisper tinyを下回るとうたうOSS",
  "thumb_style": "photo",
  "thumb_prompt": "A tiny microcontroller board smaller than a coin sitting in the palm of a hand, with a glowing ear-shaped sound wave hovering above it.",
  "editor_note": ""
}
---
スペイン・マドリードの音声AI企業Lokutorは現地時間9月30日、マイコン「ESP32-S3」1個だけで英語の音声を文字にするオープンソースの音声認識「Oído（オイド）」をGitHubで公開しました。標準的な評価データLibriSpeechでの単語誤り率は3.7%で、ノートPCで動かしたOpenAIのWhisper tiny.en（6.3%）を下回ると公表しています。開発者コミュニティのRedditのr/LocalLLaMAやHacker Newsにも投稿されました。

## 何を作ったか

Oídoとは、クラウドにもAI専用チップにも頼らず、ESP32-S3という小型マイコンの上で任意の英文を書き起こす音声認識エンジンです。名前は、スペインの厨房で注文を受けたときに返す「聞こえた、了解」という掛け声から取っています。

ESP32-S3は240MHzのデュアルコアCPUを持つマイコンで、作者はREADMEで「5ドルのチップ」と表現しています。同じチップ向けのEspressif純正の音声認識MultiNet7は、あらかじめ決めた命令の一覧を聞き分ける方式です。Oídoは命令の一覧なしで、自由な英文を文字にします。

{{card:https://github.com/lokutor-ai/oido|lokutor-ai/oido|Lokutor}}

:::quote https://github.com/lokutor-ai/oido | Lokutor「Oído」GitHub README
> To our knowledge this is the most accurate LibriSpeech result published for any microcontroller. It is not the first open-vocabulary recognizer on one (Arm has shown Conformer models on Cortex-M55 + Ethos-U NPUs).
私たちの知る限り、マイコンで公表されたLibriSpeechの結果としては最も高精度です。ただし、マイコン上で自由な語彙を認識する初の例ではありません（ArmがCortex-M55とEthos-U NPUの組み合わせでConformerモデルを示しています）。
:::

## どう作ったか

モデルは、NVIDIAが公開している音声認識モデル「Conformer-CTC Small」（1300万パラメーター）です。これを8ビット整数（int8）に量子化し、14.0MBに収めました。4ビット版（8.3MB）も公開されており、こちらは16MBのフラッシュメモリのうち6MBを自分のアプリ用に空けられます。

実行エンジンはC言語で新たに書いたもので、ESP32-S3のベクトル演算命令を使い、1命令で16回の積和演算をこなします。重みをフラッシュから読み出す回数を減らす工夫で、重みの転送量を毎秒18MBから7.5MBに減らしたとしています。発話の区切りを検出する機能や、認識結果を小型の有機ELディスプレイに表示する機能も付いています。

READMEによると、必要な機材はESP32-S3-DevKitC-1のN16R8モデル（16MBフラッシュ、8MB PSRAM）、I2S接続のマイクINMP441、任意で0.96インチのOLEDです。実機がなくても、チップと同じ計算をするPC版で手元の録音を試せます。デモ動画はHugging Faceのモデルページで公開されています。

{{card:https://huggingface.co/lokutor-ai/oido-ctc-small-int8|oido-ctc-small-int8（デモ動画つきモデルページ）|Lokutor（Hugging Face）}}

## 成果（作者の公表値）

| 方式 | 動作環境 | 単語誤り率（clean / other） |
|---|---|---|
| Oído int8 | ESP32-S3 | 3.7% / 8.2% |
| Oído int4 | ESP32-S3 | 4.6% / 10.0% |
| MultiNet7（命令一覧方式） | ESP32-S3 | 8.5% / 21.3% |
| Moonshine tiny | ノートPC | 5.0% / 12.1% |
| Whisper tiny.en | ノートPC | 6.3% / 15.9% |

雑音や残響を加えた14条件の平均でも、Oídoは8.4%で、Whisper tiny.enの12.1%を下回ったとしています。int8にしたことによる精度の低下はわずかで、元のモデルの3.68%に対して3.70%だったと説明しています。

## 論点：公表値をどう読むか

数字を使う前に、押さえておきたい前提が3つあります。

1つ目は、実機ではまだ測っていないことです。作者によると、結果はすべて、ファームウェアと計算がビット単位で一致するPC版と、Espressifのエミュレーター（QEMU）で出したものです。速度もエミュレーターの命令数から実時間係数0.7〜0.95と見積もった値で、実機の計測は数日中に追加するとしています。デモ動画も実機の映像ではなく、チップと同じ計算の出力を早送りしたものです。

2つ目は、比較の条件がそろっていないことです。チップ上の結果はテストセット全体で測っていますが、ノートPCで動かした比較対象は各500発話の抜き出しです。

3つ目は、使い勝手の制約です。文字は単語ごとではなく1発話ごとにまとめて出ます。話し終えて0.8秒の間を置いてから計算するため、2〜4秒の命令なら文字が出るまで約3秒かかります。大勢の話し声や響く部屋は苦手だと、READMEも認めています。

## 日本のビジネスへの影響

対応は英語のみで、READMEに日本語の記載はありません。Lokutorはスペイン語などの多言語モデルや同じチップで動く音声合成を個別に提供するとしていますが、日本語は挙げていません。日本語の会議録や文字起こしが目的なら、[AI文字起こしツールの比較](/best/transcription/)にあるクラウド型の選択肢が現実的です。

関係が深いのは、家電・玩具・産業機器など、ネットにつながない機器に音声入力を載せたいハードウェア開発者です。音声を外部に送らずに済むため、通信や個人情報の扱いが厳しい工場や医療の現場で検討しやすくなります。

最初の一手は、PC版に自社の英語音声を数十件流し、誤り率と待ち時間が要件を満たすかを確かめることです。実機の計測値が公開されるまで、速度の見積もりは保留にしておくのが無難です。

注意点はライセンスです。コードはGPLv3で、消費者向けの機器に組み込む場合はソースの提供や、利用者が改変版を書き込むための情報の提供が求められます。それが難しい製品向けに、Lokutorは台数単位か年単位の商用ライセンスを用意しています。モデルの重みはint8版がCC-BY-4.0、int4版がCC-BY-SA-4.0です。
