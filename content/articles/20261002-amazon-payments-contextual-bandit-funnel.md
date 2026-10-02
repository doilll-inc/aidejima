---
{
  "title": "Amazon Paymentsが申込ページの出し分けをAIで最適化、効いた層と効かなかった層を公開",
  "description": "Amazon Paymentsが、申込ページの画像とキャッチコピーの組み合わせを顧客ごとに選ぶ仕組みを7週間A/Bテストした。ある顧客層では最終の承認率が1桁台後半の割合で伸びたが、別の層では悪化した。",
  "date": "2026-10-02T23:43:00+09:00",
  "category": "usecases",
  "tags": ["Amazon Payments", "Amazon SageMaker AI", "AWS", "活用事例", "マーケティング", "LP"],
  "summary": [
    "Amazon Paymentsは、申込ページに出す画像とキャッチコピーの組み合わせを顧客ごとに選ぶ仕組みを本番で7週間試した",
    "Amazon Paymentsのテストでは、ある顧客層で最終段階のコンバージョンが1桁台後半の割合で伸び、別の層では統計的に有意に悪化した",
    "AWSは失敗の原因をモデルではなく素材の候補にあったと分析し、同じ手法を試せるサンプルコードをMIT-0ライセンスで公開した"
  ],
  "sources": [
    {"title": "Uplifting conversion across the acquisition funnel with personalization using contextual bandits on AWS", "publisher": "AWS Machine Learning Blog", "url": "https://aws.amazon.com/blogs/machine-learning/uplifting-conversion-across-the-acquisition-funnel-with-personalization-using-contextual-bandits-on-aws/", "kind": "公式発表"},
    {"title": "sample-multi-objective-contextual-bandit-with-sagemaker", "publisher": "GitHub aws-samples", "url": "https://github.com/aws-samples/sample-multi-objective-contextual-bandit-with-sagemaker", "kind": "公式サイト"}
  ],
  "thumb_text": "Amazon Payments",
  "share_text": "Amazon Paymentsが申込ページの出し分けをAIで7週間テスト。伸びた層と悪化した層の両方を公開",
  "editor_note": ""
}
---
Amazon Paymentsは、申込ページに出す画像とキャッチコピーの組み合わせを顧客ごとにAIで選ぶ仕組みを本番で7週間テストし、その結果をAWSの公式ブログで公開しました（現地時間10月1日）。ある顧客層では申込から承認までの最終段階のコンバージョンが「1桁台後半の割合」で伸びた一方、別の顧客層では既存のページに勝てず、承認率は統計的に有意に下がりました。成功だけでなく失敗まで数字で書いた、珍しい事例です。

## 何を作ったか

Amazon Paymentsが最適化したのは、審査を伴うある商品の申込ページです（商品名は公表されていません）。顧客の流れは「申込の開始」「申込の送信」「審査の承認」の3段階に分かれています。ここで「業界ごとのイメージ画像」と「メリットを伝えるキャッチコピー」を組み合わせた多数のページ案から、顧客ごとに1つを選んで見せます。

選び方に使ったのは、「コンテキスト付き多腕バンディット」と呼ばれる手法です。多腕バンディットとは、たくさんの候補を実際の訪問者に出しながら、成果の良い候補に表示を寄せていき、一部は他の候補の検証に回し続ける強化学習の手法です。A/Bテストのように「テストが終わるまで待つ」必要がありません。コンテキスト付きの場合は、訪問者の支払い行動や取引の内訳といった特徴を見て、人ごとに出す候補を変えます。

:::quote https://aws.amazon.com/blogs/machine-learning/uplifting-conversion-across-the-acquisition-funnel-with-personalization-using-contextual-bandits-on-aws/ | AWS Machine Learning Blog「Uplifting conversion across the acquisition funnel with personalization using contextual bandits on AWS」
> Generative AI has made it possible to produce large amounts of personalized content quickly and at low cost. The new challenge is now one of selection.
生成AIのおかげで、個別向けのコンテンツを素早く安く大量に作れるようになりました。新たな課題は「どれを選ぶか」です。
:::

## どう作ったか

仕組みの要点は4つです。

- **3段階をまとめて最適化**: 開始・送信・承認の段階ごとに予測モデル（LinUCB）を1つずつ持ち、3つのスコアをほぼ同じ重みで足し合わせて候補を選ぶ。開始だけを増やすページは、審査に通らない人まで集めて承認率を下げることがあるため
- **部品単位で審査**: 画像とコピーを1つずつ事前に人が確認し、その掛け合わせで候補を作る。組み合わせがどれだけ増えても、確認するのは部品の数だけで済む
- **週1回のバッチ処理**: Amazon SageMaker AIの処理ジョブが週1回、Amazon S3から前週の結果を読んでモデルを更新し、顧客ごとのおすすめをDynamoDBなどの高速なデータベースに書き出す。ページ表示時は1回引くだけで、その場でのAI推論はしない
- **安全な戻り先**: おすすめがない顧客には従来のページを出す。承認の結果は数日遅れて届くので、次の週のバッチで反映する

最初は候補をランダムに割り当てる期間を設けて偏りのないデータを集め、そこからモデルを立ち上げています。

## 成果

結果は顧客層によって分かれました。

| 顧客層 | 7週間のA/Bテストの結果（既存ページとの比較） |
|---|---|
| 1つ目の層 | 開始・送信・承認の3指標すべてが上向き。最終段階は1桁台後半の割合で上昇 |
| 2つ目の層 | 候補の大半を試しても既存ページに勝つ組み合わせが見つからず、数値はマイナス。承認率の低下は統計的に有意 |

著者のAmazonの研究者2人は、2つ目の層の失敗を「モデルの失敗ではない」と分析しています。十分に探した結果、候補の中に勝てるページがないことがわかった、という見方です。

:::quote https://aws.amazon.com/blogs/machine-learning/uplifting-conversion-across-the-acquisition-funnel-with-personalization-using-contextual-bandits-on-aws/ | AWS Machine Learning Blog「Uplifting conversion across the acquisition funnel with personalization using contextual bandits on AWS」
> This was not a model failure. Thorough exploration can confirm that a content pool contains no winner.
これはモデルの失敗ではありません。徹底的に探索したことで、候補の中に勝者がいないと確かめられたのです。
:::

ほかにも、導入前の検証で、1段階だけを最適化した方針はどれも別の段階で少なくとも1つマイナスを出したと書いています。3段階すべてでマイナスを出さなかったのは、まとめて最適化する方式だけでした。今回、部品は人が細かく管理して用意しましたが、今後は生成AIで部品を大幅に増やせる余地があるとしています。

## 日本で真似するなら

- **必要なもの**: 顧客ごとの行動データ（数値の特徴量）、段階ごとの成果ログ、事前に審査した画像とコピーの部品。AWSを使う場合はSageMaker AI、S3、DynamoDBで同じ構成を組めます
- **手順の目安**: まずAWSが公開したサンプルコードで、合成データを使って動きを確かめます。AWSのアカウントがなくても手元で動くデモが入っています。次に、既存のページを候補の1つに入れて、少数の部品から本番の一部の流入で試します

{{card:https://github.com/aws-samples/sample-multi-objective-contextual-bandit-with-sagemaker|sample-multi-objective-contextual-bandit-with-sagemaker|GitHub aws-samples}}

- **注意点**: クレジットや保険のように審査がある商品では、「申込数」だけを追うと承認率を下げる危険があります。KPIは最後の成果まで含めて設計します。また、顧客層によっては素材のほうが足りず、どれだけ探しても勝てない場合があることを、今回の事例は示しています

## 日本のビジネスへの影響

- **使えるか**: 手法はAWSの一般的なサービス（SageMaker AI、S3、DynamoDB）の組み合わせで、特別な製品は要りません。サンプルコードはMIT-0ライセンスで、商用でも自由に使えます。ただしAmazon Payments自体の仕組みは社内のもので、製品として提供されているわけではありません
- **誰にどう効くか**: 生成AIでバナーやLPの案を大量に作れるようになった**マーケター・広告運用者**に効きます。作った案のどれを誰に出すかを、A/Bテストを何本も回さずに自動で寄せていけます。データ基盤を持つ**開発者・データサイエンティスト**なら、週1回のバッチという軽い構成から始められます
- **今すぐやれること**: 自社のLPで「申込の開始」と「最終の成約」の両方を顧客ごとに記録できているかを確認します。最後の成果が取れていなければ、この手法は使えません
- **注意点**: 1つの層で効いても別の層では逆効果になることがあり、層ごとに分けて学習・評価する必要があります。今回の上昇幅も「1桁台後半」とだけ書かれており、正確な数字や対象商品は公表されていません

広告・マーケティング向けAIツールの選び方は、[マーケティング向けAIのガイド](/best/marketing/)にまとめています。
