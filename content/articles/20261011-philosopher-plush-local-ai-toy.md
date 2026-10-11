---
{
  "title": "顔を見分けて話し相手になるぬいぐるみ、個人開発者が部品代約110ユーロで作り方を無料公開",
  "description": "個人開発者のマノロ・サルサス氏が、家族の顔と表情を見分け、相手ごとに過去の会話を覚えて話すぬいぐるみ「Philosopher」の作り方とプログラムを無料公開した。部品代は約110ユーロで、会話の処理は自宅のパソコンの中だけで済む。",
  "date": "2026-10-11T10:50:00+09:00",
  "category": "usecases",
  "tags": ["Philosopher", "活用事例", "個人開発", "オープンソース", "ローカルLLM", "音声会話"],
  "summary": [
    "個人開発者が、目の前の人の顔と表情を見分けて、人ごとに過去の会話を覚えて話すぬいぐるみ「Philosopher」を作り、作り方を無料公開した",
    "ぬいぐるみの中は小型の基板とカメラ・首を動かすモーターだけで、聞き取り・考える・話す処理は近くのパソコンが受け持つ",
    "部品代は約110ユーロ（パソコン別）。自宅のパソコンで動くAIと組めば、会話も顔の情報もネットの外に出ない"
  ],
  "sources": [
    {"title": "philosopher（README）", "publisher": "GitHub msalsas", "url": "https://github.com/msalsas/philosopher", "kind": "公式サイト"},
    {"title": "The Philosopher Plush — a DIY AI toy that runs 100% local", "publisher": "DEV Community（マノロ・サルサス氏）", "url": "https://dev.to/msalsas/the-philosopher-plush-a-diy-ai-toy-that-runs-100-local-2h1n", "kind": "公式サイト"},
    {"title": "AI Philosopher Plush", "publisher": "YouTube Philosopher Toy", "url": "https://www.youtube.com/watch?v=Wlafq9nP06E", "kind": "公式サイト"},
    {"title": "Fully local conversational AI: Whisper + Hermes 8B + Kokoro, zero cloud, running inside a plush toy", "publisher": "Reddit r/LocalLLaMA", "url": "https://www.reddit.com/r/LocalLLaMA/comments/1x2cztv/fully_local_conversational_ai_whisper_hermes_8b/", "kind": "コミュニティ"}
  ],
  "thumb_text": "Philosopher",
  "thumb_style": "diorama",
  "thumb_prompt": "A miniature living room where a plush teddy bear with a tiny camera eye sits on a sofa, turning its head toward a small family of figurines, while a laptop on a side table glows as if it is the bear's brain.",
  "share_text": "家族の顔と表情を見分けて、人ごとに会話を覚えて話すぬいぐるみ。部品代約110ユーロ、会話はネットに出さない作りで作者が無料公開",
  "editor_note": ""
}
---
個人開発者のマノロ・サルサス氏が、目の前の人の顔と表情を見分け、相手ごとに過去の会話を覚えて話すぬいぐるみ「Philosopher（哲学者）」を作り、作り方とプログラムをGitHubで無料公開しています。ぬいぐるみ本体の部品代は約110ユーロで、自宅のパソコンで動くAIと組み合わせれば、会話も顔の情報もネットの外に出ません。現地時間10月10日に作者が海外の掲示板Redditに投稿し、改めて注目を集めました。

## 何を作ったのか

Philosopherとは、カメラとマイクとスピーカーを仕込んだぬいぐるみが、目の前の人を見分けて会話する仕組みです。作者のブログによると、ぬいぐるみは複数の人を見分け、表情から気分を読み取り、首を動かしながら返事をします。名前のとおり初期設定は哲学者のような話し方ですが、性格は設定ファイルで切り替えられ、哲学者・好奇心旺盛な子ども・詩人など5種類が用意されています。言葉はスペイン語と英語に対応しています。

作者が公開した動画では、「人生の意味とは何か」という同じ質問に5つの性格それぞれが答える様子が見られます。

{{youtube:https://www.youtube.com/watch?v=Wlafq9nP06E}}

作ったきっかけについて、作者はブログで、哲学的な会話は好きだが誰かとビールを飲みに行くのは面倒、という人向けだと冗談まじりに書いています。営利目的ではなく、データも集めないとしています。

## どう作ったか

工夫の中心は、ぬいぐるみ自体には頭脳を持たせないことです。中に入っているのは、手のひらより小さい基板「Raspberry Pi Zero」（メモリーは512MB）とカメラ、首を動かすモーターだけです。音声と映像は家の中のネットワークでパソコンへ送られ、パソコンの側が聞き取り・顔と表情の判別・返事の読み上げ・記憶をまとめて受け持ちます。

:::quote https://github.com/msalsas/philosopher | GitHub「philosopher」README
> All of the AI runs on a nearby laptop; the toy itself is a tiny, ML-free Raspberry Pi that just handles microphone, camera, speaker and a head servo.
AIはすべて近くのノートPCで動く。ぬいぐるみ本体はAIを持たない小さなRaspberry Piで、マイク・カメラ・スピーカーと首のモーターを扱うだけだ。
:::

使っている部品はどれも無料で公開されているものです。

| 役割 | 使っているもの |
|---|---|
| 話を聞き取る | Whisper（音声を文字にするAI） |
| 返事を考える | 対話AI。作者は「Hermes」という約80億パラメーターのモデルを手元のサーバーで使用。ChatGPTなどのクラウドのAIにもつなげられる |
| 返事を読み上げる | Kokoro（音声合成AI） |
| 顔と表情を見分ける | 顔認識と表情認識の公開ソフト |
| 人ごとの記憶 | 短期と長期の2種類の記憶を、顔で見分けた人ごとに保存 |

返事は1文ずつ順に読み上げるので、AIが全文を考え終える前に話し始めます。パソコンの管理画面では、いま誰がいるか、その人の表情の移り変わりもグラフで見られます。

ブログに載っている部品代は、ぬいぐるみ15ユーロ、基板とSDカード40ユーロ、カメラ15ユーロ、スピーカー15ユーロ、マイク10ユーロなどで、合計約110ユーロです。ここにパソコンと対話AIを動かすサーバーが別に要ります。作者は画像処理用のメモリー（VRAM）が16GBのサーバーで動かしたと書いています。組み立ては、ぬいぐるみの中綿を抜いてカメラ・基板・モーターを入れるだけで、作者の場合はマイクとスピーカーは外に出したそうです。

## 成果と反応

成果として示された数字は部品代くらいで、返事までの待ち時間などは公表されていません。GitHubの星は4件と、まだ小さな個人の作品です。一方で、話を聞く・考える・話す・顔を見分ける・相手を覚えるという、市販の会話ロボットに近い一式を、家庭の中だけで動かす形にまとめた点が、手元でAIを動かすことに関心のある人が集まる掲示板で注目されました。

AIを入れたおもちゃでは、子どもの声や顔の映像が作った会社のサーバーに送られることが気になる人も多いはずです。Philosopherは、その情報を家の外に出さない作りを個人でまとめた例です。

## 日本のビジネスへの影響

- **使えるか**: プログラムは無料（MITライセンス。商用利用も可）で、日本からも使えます。ただし対応している言葉はスペイン語と英語だけで、日本語で話すには聞き取り・読み上げの設定を自分で差し替える必要があります。
- **誰に効くか**: 玩具・介護・見守りの分野で新しい商品を企画する人です。「顔と表情を見分けて相手ごとに会話を覚える」機能を、外部のクラウドに頼らず家の中だけで動かせることが、部品代約110ユーロの試作で確かめられます。
- **今すぐやれること**: まず作者の動画で、返事の速さと話し方を見てみてください。社内に手元でAIを動かせるパソコンがあれば、ぬいぐるみに入れる前に、パソコンだけでの会話を試すところまでは手順書どおりに進められます。手元で動くAIの選び方は[ローカルLLM・オープンウェイトモデルのおすすめ](/best/local-llm/)にまとめています。
- **注意点**: 顔と表情を読み取って記録するので、家の中で使う場合でも、家族や来客に何を記録しているかを伝えるべきです。商品にするなら、顔の情報は個人情報保護法上の扱いにも注意が要ります。また、返事を考えるAIをクラウドのものにした場合は、会話がネットの外に出ます。
