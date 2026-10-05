---
{
  "title": "uniopenがAmazon Nova 2 Liteを自社規定で微調整、投稿審査の精度を本番水準に",
  "description": "台湾の統一企業グループの会員サービスuniopenは、投稿審査にAmazon Nova 2 Liteを微調整して使っている。3,391件の会話で学習させ、行動分類の精度を示すF1を0.5852から0.8550に上げた。AWSが10月1日に公開した事例をまとめる。",
  "date": "2026-10-02T04:10:00+09:00",
  "category": "usecases",
  "tags": ["uniopen", "Amazon Nova 2 Lite", "AWS", "導入事例", "活用事例", "EC"],
  "summary": [
    "台湾の統一企業グループのuniopenは、会員とのやり取りの審査にAmazon Nova 2 Liteを自社規定で微調整して使っている",
    "3,391件の会話で学習させると、9種の行動分類のF1は0.5852から0.8364、対象の分類は0.4162から0.8302に上がった",
    "出力をJSONから1行ずつの形式に変えるだけで両方が本番の目標値を超え、人の確認は判断が難しい案件に絞った"
  ],
  "sources": [
    {"title": "How uniopen customized Amazon Nova to their retail moderation policies for production deployment", "publisher": "AWS Machine Learning Blog", "url": "https://aws.amazon.com/blogs/machine-learning/how-uniopen-customized-amazon-nova-to-their-retail-moderation-policies-for-production-deployment/", "kind": "公式発表"},
    {"title": "Supervised fine-tuning (SFT) on Nova 2.0 on SageMaker Training Jobs", "publisher": "AWS Documentation", "url": "https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-sft-2-smtj.html", "kind": "公式ドキュメント"}
  ],
  "thumb_text": "Amazon Nova 2 Lite",
  "share_text": "台湾uniopenがAmazon Nova 2 Liteを自社の審査規定で微調整。3,391件の学習で分類精度F1が0.58→0.86に",
  "thumb_style": "3d",
  "thumb_prompt": "A conveyor belt of colorful chat speech bubbles passing through a scanner gate, where a few bubbles are gently lifted out by a robot hand into a red tray.",
  "editor_note": ""
}
---
台湾の統一企業グループが運営する会員・EC向けサービス「uniopen」は、顧客とのやり取りの審査（モデレーション）に、AWSの軽量モデル「Amazon Nova 2 Lite」を自社の規定に合わせて微調整して使っています。AWSが現地時間10月1日に公開した事例によると、3,391件の会話で学習させた結果、行動の分類精度を示すF1スコアは0.5852から0.8550に上がり、本番投入の目標を超えました。大きなモデルに頼らず、小さなモデルを自社の基準で鍛えて使う例です。

## 何を作ったか

uniopenは、Web・タブレット・スマートフォンでECや会員特典を提供する統一企業グループのサービスです。そこに寄せられる顧客とのやり取りを、2つの軸で分類する審査の仕組みを作りました。

- **何が起きたか**：9種類の行動のどれに当たるか
- **何についてか**：対象が「ブランド」「その他」「禁止対象」のどれか

難しいのは、両方が当たって初めて審査の判断として役に立つ点です。

:::quote https://aws.amazon.com/blogs/machine-learning/how-uniopen-customized-amazon-nova-to-their-retail-moderation-policies-for-production-deployment/ | AWS Machine Learning Blog「How uniopen customized Amazon Nova」
> Both must be correct for a moderation decision to be useful, and both are specific to uniopen’s business rather than something a general-purpose model can be expected to learn out of the box.
審査の判断として役立つには両方が正しくなければなりません。しかもどちらもuniopenの事業に固有のもので、汎用モデルが最初から身につけているとは期待できません。
:::

## どう作ったか

使ったのはAmazonのNovaシリーズの2モデルです。日々の審査はNova 2 Liteが担い、上位のNova 2 Proは、利用者から「判定が間違っている」と報告があったときに修正案を作る役に回しました。ただし修正案はそのまま学習に使わず、必ず人が確認してから学習用のデータに入れます。AIが作ったラベルを正解扱いしないための決まりです。

微調整は、Amazon SageMaker AIの教師あり学習（SFT。正解付きの例で学ばせる方法）で行いました。モデル全体ではなく、追加の小さな重みだけを学習するLoRAという方式です。学習データは3,391件の会話の区切り（会話ウィンドウ）で、評価は別に取り分けた737件で比べました。

{{card:https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-sft-2-smtj.html|Supervised fine-tuning (SFT) on Nova 2.0 on SageMaker Training Jobs|AWS Documentation}}

周辺の仕組みもAWSのサービスで組んでいます。

| 役割 | 使ったもの |
|---|---|
| 修正済みデータと学習データの保存 | Amazon S3 |
| 本番と候補のモデル設定の管理 | Amazon DynamoDB |
| 評価・配備の自動化 | Amazon EKS上のArgo Workflows、Argo CD |
| 異常の通知 | Amazon SNS、Amazon CloudWatch |

新しいモデルや指示文（プロンプト）を本番に出すときは、2段階の関門を通します。必ず合格すべき回帰テストに落ちたら、その場で止めて担当者に知らせます。合格しても、特定の分類だけ成績が下がったなどの警告が出れば、管理者が承認するまで本番に出しません。

## 成果

公表された数字は、同じ737件での3段階の比較です。

| 指標 | 微調整なし | 微調整後 | 出力形式の変更後 | 本番の目標 |
|---|---|---|---|---|
| 行動のF1（9種） | 0.5852 | 0.8364 | 0.8550 | 0.8500以上 |
| 対象のF1（3種） | 0.4162 | 0.8302 | 0.8491 | 0.8200以上 |

F1は正しく拾えた度合いと誤りの少なさを合わせた0〜1の指標で、ここでは各分類を同じ重みで平均しています。よく出る分類で高い点を取っても、苦手な分類の低さが隠れない測り方です。

最も効いたのは微調整で、特に対象の分類が約2倍になりました。最後の一押しは学習ではなく指示の変更です。出力をJSONから1行ずつの形式に変え、複数の行動の返し方を明確にしただけで、両方の指標が目標を超えました。その結果、日常の審査は微調整したモデルに任せ、人の確認は判断が難しい案件に集中できるようになったといいます。

なお、事例には学習にかかった費用や時間、応答速度、人手がどれだけ減ったかの数字は書かれていません。他社のモデルとの比較もありません。

## 日本で真似するなら

- **必要なもの**：自社の審査基準を言葉にした分類表と、人が正解を付けた過去のやり取り数千件。uniopenの例では学習用が約3,400件、評価用が約700件でした
- **手順の目安**：まず微調整なしのモデルで評価用データの点数を測り、目標値を決めます。次に正解付きデータで微調整し、最後に出力形式などの指示を整えます。評価用データは途中で入れ替えず、同じもので比べ続けるのがこの事例の要点です
- **注意点**：Novaのモデルは提供されるAWSのリージョンが限られ、事例でも地域によって使えるモデルが違うと注意しています。東京リージョンで使えるかは事前に確認してください。分類の苦手な部分を人が拾う運用を残すことも前提です

## 日本のビジネスへの影響

- **使えるか**：Amazon Nova 2 LiteとSageMaker AIでの微調整は、AWSの契約があれば日本の企業も使えます。ただし対応リージョンは事前の確認が必要です。日本語の審査でどこまで精度が出るかは、この事例からは分かりません
- **誰に効くか**：口コミ・問い合わせ・SNSのコメントを審査しているEC事業者やカスタマーサポートの責任者です。ブランドへの言及か、禁止対象かといった自社固有の基準は、汎用モデルに指示を書くだけでは届かないことを数字で示しています
- **今すぐやれること**：審査の現場で人が付けた判定の記録を集め、正解付きデータとして使える形に整えるところから始めてください。他のAPIの料金や選び方は[AI APIのガイド](/best/api/)で比べられます
- **注意点**：AIに作らせた修正案を確認なしで学習に回すと、誤りが積み重なります。uniopenが人の確認を必須にしているのはこのためです。顧客の発言を学習に使う場合は、利用規約やプライバシーポリシーで扱いを確かめてください
