---
{
  "title": "Hugging Faceが音声合成の公開ランキング「Open TTS Leaderboard」、日本語も比較",
  "description": "Hugging Faceはオープンソースの音声合成モデルを自動の指標で比べるOpen TTS Leaderboardを公式ブログで紹介した。聞き取りやすさ・速さ・声の再現度を9言語で測り、日本語では10月1日時点で16モデルを比べている。",
  "date": "2026-10-01T18:32:00+09:00",
  "updated": "2026-10-01T18:55:00+09:00",
  "category": "research",
  "tags": ["Hugging Face", "Open TTS Leaderboard", "音声合成", "ベンチマーク", "オープンソース"],
  "summary": [
    "Hugging FaceのOpen TTS Leaderboardは、オープンソースの音声合成モデルを人の投票ではなく自動の指標で比べる",
    "読み上げを文字起こしした誤り率、生成の速さ、声のクローンの似ている度合いを、日本語を含む9言語で測る",
    "日本語は10月1日時点で16モデルが比較され、誤り率の上位はOmniVoice、NVIDIAのMagpie TTS、Supertonic 3"
  ],
  "sources": [
    {"title": "Open TTS Leaderboard: Scalable Evaluation for Multilingual Text-to-Speech and Voice Cloning", "publisher": "Hugging Face Blog", "url": "https://huggingface.co/blog/open-tts-leaderboard", "kind": "公式発表"},
    {"title": "Open TTS Leaderboard", "publisher": "Hugging Face（hf-audio）", "url": "https://huggingface.co/spaces/hf-audio/open_tts_leaderboard", "kind": "公式ドキュメント"},
    {"title": "CV3-Eval", "publisher": "QwenAudio（GitHub）", "url": "https://github.com/QwenAudio/CV3-Eval", "kind": "公式ドキュメント"}
  ],
  "thumb_text": "Open TTS",
  "share_text": "Hugging Faceが音声合成の公開ランキングOpen TTS Leaderboardを紹介。日本語を含む9言語で、声のクローンも比べられる",
  "thumb_style": "illustration",
  "thumb_prompt": "A podium with first, second and third places where three different colorful speakers stand like athletes, each with sound waves coming out of them.",
  "editor_note": ""
}
---
Hugging Faceは現地時間9月30日、オープンソースの音声合成（TTS）モデルを多言語で比べる公開ランキング「Open TTS Leaderboard」を公式ブログで紹介しました。人の投票ではなく自動の指標で測るため、1つのモデルの評価にかかる時間が数週間から数時間に縮むとしています。評価する言語には日本語も含まれ、10月1日時点で日本語は16モデルが比較されています。

## 何が発表されたか

Open TTS Leaderboardとは、Hugging FaceのAudioチームが運営する、音声合成モデルの成績表です。9月8日に初版を公開し、その後もモデルを追加しています。Hugging Faceには8,000を超える音声合成モデルがありますが、評価の方法がばらばらだったことが作った理由です。

これまでの代表的なランキングは、2つの読み上げを人が聞き比べて投票する方式でした。票が集まるまで時間がかかり、オープンなモデルは載りにくい面があります。ブログによると、Artificial Analysisのランキングでは92モデルのうちオープンウェイト（重みが公開されたモデル）は16にとどまります。

測るのは次の3点です。

| 指標 | 測り方 |
|---|---|
| 聞き取りやすさ | 読み上げた音声をQwen3-ASRで文字起こしし、元の文との誤り率を出す |
| 速さ | H200 GPUでの生成速度と、最初の音が出るまでの時間 |
| 声の再現度 | 声のクローンで、手本の声と生成した声がどれだけ似ているか |

:::quote https://huggingface.co/blog/open-tts-leaderboard | Hugging Face公式ブログ「Open TTS Leaderboard」
> Importantly, the Open TTS Leaderboard does not replace human preference ranking.
大切な点として、Open TTS Leaderboardは人の好みによるランキングに取って代わるものではありません。
:::

自然さや感情の表現、聞き手の好みは直接測っていないと、ブログ自身が断っています。その代わり、各モデルが実際に作った音声を聞き比べて投票できる「Listen」のタブを用意しました。評価に使うスクリプトも近く公開するとしています。

## 日本語の扱いと結果

評価用の文は2つのデータセットから取ります。Seed TTS Evalは英語と中国語だけで、もう一方のCV3-Evalが英語・中国語・フランス語・スペイン語・ドイツ語・イタリア語・日本語・韓国語・ロシア語の9言語を持ちます。CV3-Evalは、音声合成モデルCosyVoice 3の開発チームが、Common Voiceなど実際の録音を手本に作った評価セットです。日本語はこちらで評価されます。

日本語は中国語・韓国語とともに文字を単位に数える言語として扱われ、単語単位の誤り率（WER）ではなく、文字単位の誤り率（CER）が表に出ます。複数の言語を選んだときに出る「平均WER」は、言語ごとの値を同じ重みで平均したものです。

AIデジマ編集部が10月1日に、言語を日本語だけにして確かめた上位5モデルです（文字誤り率は低いほどよい）。

| 順位 | モデル | 文字誤り率 | 大きさ | ライセンスの表示 |
|---|---|---|---|---|
| 1 | k2-fsa/OmniVoice | 4.61 | 0.81B | cc-by-nc |
| 2 | nvidia/magpie_tts_multilingual_357m | 4.79 | 0.31B | NVIDIA Open Model License |
| 3 | Supertone/supertonic-3 | 4.80 | 0.1B | Open RAIL-M |
| 4 | IndexTeam/IndexTTS-2.5 | 5.08 | 1.67B | 独自（custom） |
| 5 | hexgrad/Kokoro-82M | 5.21 | 0.08B | Apache 2.0 |

声のクローンで比べると、日本語に対応する9モデルのうち、文字誤り率の1位はbosonai/higgs-tts-3-4b（4.85）でした。手本の声との近さはopenbmb/VoxCPM2が最も高く、OmniVoiceが続きます。

## 論点

英語の成績はほかの言語に当てはまらない、とブログは強調しています。実際、ブログが多言語に強いモデルとして挙げたFun-CosyVoice3-0.5B-2512は、日本語では16モデル中最下位で、強化学習で調整した版も15位でした。日本で使うなら、英語の順位ではなく日本語の欄を見る必要があります。

対象はオープンなモデルに絞られ、[評価額が220億ドルに達したElevenLabs](/news/20261001-elevenlabs-22b-valuation-tender/)のような商用のサービスは入っていません。日本語を比べられるモデルも16と、英語の30余りより少なめです。また誤り率は文字起こしの精度を通した測り方で、読みの自然さやアクセントの正しさまでは分かりません。

## 日本のビジネスへの影響

ランキングは誰でも無料で見られ、日本語の結果も確かめられます。投票にはHugging Faceへのログインが必要です。

関係が深いのは、読み上げや音声エージェント、動画のナレーションを自社で作りたい開発者と、動画広告を内製するマーケターです。まずは言語で日本語だけを選び、上位のモデルを「Listen」のタブで聞き比べるのが手早い一手です。声のクローンを使うなら、「Voice cloning」に切り替えて手本との近さも見てください。

注意点は、ライセンスです。1位のOmniVoiceは非営利に限るcc-by-ncの表示で、広告や有料サービスには使えない可能性があります。商用で使う前に、各モデルの公式ページで条件を確かめてください。他人の声のクローンには本人の同意が欠かせません。商用サービスを含む料金と選び方は「[音声合成・AI読み上げのおすすめと料金比較](/best/text-to-speech/)」にまとめています。
