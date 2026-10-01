---
{
  "title": "Jeffは自宅で学習した0.8Bの判断モデル、PostHogも考えてから選ぶJeevesを公開",
  "description": "文章を生成せず選択肢ごとの確率を返す「判断モデル」の公開版が相次いだ。個人開発のJeffは0.8Bで1回22〜28ミリ秒、自宅のGPU1枚で約2時間で学習した。PostHogのJeevesは9Bで、考えてから選ぶ方式で精度を上げた。",
  "date": "2026-10-01T17:51:00+09:00",
  "category": "usecases",
  "tags": ["Jeff", "Jeeves", "PostHog", "オープンウェイト", "個人開発", "活用事例"],
  "summary": [
    "Jeffは状況と選択肢を渡すと各選択肢の確率を返す小型の判断モデルで、0.8B版は1回の判断が22〜28ミリ秒",
    "Jeffの作者はクラウドを使わず、GPU1枚のワークステーションで0.8B版を約2時間で学習し、学習データもオープンモデルで作った",
    "PostHogのJeevesは9Bで、答える前に考える学習によりJevBenchの公開問題で0.935とJevの0.866を上回った"
  ],
  "sources": [
    {"title": "firelex/jeff", "publisher": "GitHub firelex", "url": "https://github.com/firelex/jeff", "kind": "公式ドキュメント"},
    {"title": "PostHog/jeeves", "publisher": "GitHub PostHog", "url": "https://github.com/PostHog/jeeves", "kind": "公式ドキュメント"},
    {"title": "Jeff – Jev-compatible 0.8B decision models, trained at home, ~30 ms", "publisher": "Hacker News（作者の投稿）", "url": "https://news.ycombinator.com/item?id=49883844", "kind": "公式発表"},
    {"title": "Introducing System One Models & Jev", "publisher": "TypeSafe AI", "url": "https://typesafe.ai/blog/introducing-system-one-models-and-jev", "kind": "公式発表"},
    {"title": "Jeeves. Reasoning improves Jev-like decision models", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=49891290", "kind": "報道"}
  ],
  "thumb_text": "Jeff・Jeeves",
  "share_text": "自宅のGPU1枚で学習した0.8Bの判断モデルJeffが1回28ミリ秒。PostHogは考えてから選ぶ9BのJeevesを公開",
  "editor_note": ""
}
---
文章を書かずに「どれを選ぶか」だけを答える小型のAIモデル「Jeff」を、GitHubのfirelexが9月28日に公開しました。0.8B（8億パラメータ）版は、1回の判断が22〜28ミリ秒です。学習はクラウドを使わず、GPU1枚のワークステーションで約2時間でした。翌29日には、製品分析ツールのPostHogが、考えてから選ぶ9Bの判断モデル「Jeeves」を公開しています。

## 判断モデルとは

判断モデルとは、状況の説明と選択肢を受け取り、各選択肢の確率を返すAIモデルです。TypeSafe AIが9月に公開した「Jev」で広く知られるようになり、同社は「System One Model」と呼んでいます。答えは「はい・いいえ」の確率、決めた選択肢から1つ、決めた段階評価のどれか、の3種類です。文章を生成しないので、プログラムの分岐にそのまま使えます。Jevの料金は入力100万トークンあたり0.042ドルで、出力は無料です。

JeffとJeevesはどちらもJevと同じ形式で呼び出せる公開版で、重みとコードを誰でも使えます。JeffはTypeSafeとは無関係だと明記しています。

## Jeff：個人が自宅で作った小型版

:::quote https://github.com/firelex/jeff | Jeff公式リポジトリ（README）
> You describe a situation and list the options in plain words; Jeff returns a calibrated probability for each option from a single forward pass.
状況を説明し、選択肢を普通の言葉で並べるだけです。Jeffは1回の計算で、各選択肢の確率を較正した値で返します。
:::

元になったのはAlibabaのQwen3.5（0.8Bと2B）と、GoogleのGemma 4 E2Bです。選択肢は学習データにないものでもよく、問い合わせの振り分け、ユーザーの意図の判定、投稿の審査、音声コマンドなどに使えます。29日のv1.1で、Qwen版が選べる選択肢は最大26個から254個に増えました。

学習環境は手元の機器だけです。

| 工程 | 使った機器 |
|---|---|
| 学習 | RTX PRO 6000 1枚（0.8B版は約2時間、2B版は約3.5時間） |
| 学習データの作成 | DGX Spark 2台で動かしたオープンモデルQwen3.8-Flash-Next |
| 試験 | MacBook |

学習データに非公開モデルの出力は使っていません。非公開モデルは、合成データの一部の品質確認だけに使ったと説明しています。学習の費用は公表されていません。

5種類の公開ベンチマーク（4,599問）の総合では、0.8B版が79.1%、2B版が82.0%で、Jevの公表値83.0%に迫りました。金融ニュースの感情分類（Financial PhraseBank）では0.8B版が95.7%とJevの77.0%を上回る一方、推論が必要な問題（BBH）では64.9%対94.3%と大きく劣ります。Jevの数字は同じベンチマークの別の問題で測ったものです。

追加学習で用途に合わせることもできます。作者は音声で画面を操作するアプリ向けに約1万1,000例で追加学習し、GPU1枚で約30分、正解率は31.7%から95.8%に上がりました。

## Jeeves：PostHogの「考えてから選ぶ」版

:::quote https://github.com/PostHog/jeeves | Jeeves公式リポジトリ（README）
> Jev-like models give calibrated decision probabilities, but at low accuracy. A lot of pipelines therefore rely on a reasoning model as a fallback.
Jev型のモデルは較正された確率を返しますが、精度は低めです。そのため多くの処理の流れでは、推論モデルを予備として用意しています。
:::

JeevesはQwen3.5-9Bをもとに、答える前に考えるよう強化学習（CISPO）で鍛えました。学習はGPU8枚です。JevBenchの公開問題（231問）では0.935でJevの0.866を、難問（111問）では0.865で0.730を上回りました。一般知識（MMLU）は0.793でJevの0.900に届きません。

速度は、考えずに答えると約0.3秒、考えると中央値3.3秒です（H100 1枚）。考える量の上限は設定できます。Macでも48GB以上のメモリがあれば動きます。

## 反応と論点

Hacker NewsでJeffの投稿は572ポイント、Jeevesは242ポイントを集めました。Jeffには、自分の用途ではJevの94%に対して70%だった、求人広告の分類では0.8B版は使えなかった、という報告が付きました。単純な分類なら、文章を数値化する埋め込みモデルと従来の分類器の組み合わせで十分という指摘もあります。Jeevesには、ドイツ語のツイートの皮肉判定でJevに届かなかったが、投稿の審査ではJevにかなり近かったという試用報告がありました。

## 日本のビジネスへの影響

JeffもJeevesも無料で、Hugging Faceから重みを入手できます。ただしJeffのREADMEは「英語とテキストのみ」と明記しています。

関係が深いのは、問い合わせの振り分けや投稿の審査を自動化したい開発者と、顧客対応の責任者です。社外にデータを出さずに手元で動かせ、自社のデータで追加学習できるのが利点です。

今すぐやれるのは、英語の問い合わせ100件に正解のラベルを付け、Jeffの正解率を測ることです。日本語で使うなら、自社のデータで追加学習してから評価してください。

注意点として、ベンチマークの比較は作者側の計測で、Jevとは別の問題を使っています。小型モデルは複数の手順を踏む推論が苦手です。手元で動かす選択肢は「[ローカルLLM・オープンウェイトモデルのおすすめ](/best/local-llm/)」にまとめています。
