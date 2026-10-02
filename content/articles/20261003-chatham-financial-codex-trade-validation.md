---
{
  "title": "Chatham Financialが取引照合をCodex製アプリで30分から4分未満に、社員も自作アプリ",
  "description": "米金融アドバイザリーのChatham FinancialがOpenAIの導入事例として、Codexで作った取引照合アプリで確認作業を約30分から4分未満に縮めたと公表した。社員が業務アプリを自作する社内基盤も持つ。",
  "date": "2026-10-03T03:20:00+09:00",
  "category": "usecases",
  "tags": ["Chatham Financial", "Codex", "OpenAI", "活用事例", "導入事例", "金融"],
  "summary": [
    "Chatham FinancialはCodexで取引照合アプリを作り、1件の確認を約30分から4分未満に縮めたと初期計測で公表した",
    "社員が業務アプリを自作する社内基盤Chatham Vibesでは、アプリ内のAI機能が標準でGPT-5.6 Terraで動く",
    "顧客向けのOnyxでは簡単な分析を安いモデルに、難しい処理をGPT-5.6に振り分けて費用と精度を両立させている"
  ],
  "sources": [
    {"title": "Chatham scales its capital markets expertise with OpenAI", "publisher": "OpenAI", "url": "https://openai.com/index/chatham-financial/", "kind": "公式発表"},
    {"title": "Chatham Financial", "publisher": "Chatham Financial", "url": "https://www.chathamfinancial.com/", "kind": "公式サイト"}
  ],
  "thumb_text": "Codex",
  "share_text": "取引照合を30分から4分未満に。米Chatham FinancialがCodexで作った社内アプリと、モデルの使い分け",
  "editor_note": ""
}
---
金利や為替のヘッジなど資本市場の助言を手がける米Chatham Financialが、OpenAIのCodexで作った取引照合アプリで、1件あたりの確認を約30分から4分未満に縮めたと明らかにしました。OpenAIが米国時間10月1日に公開した導入事例で、同社の幹部が語っています。社員がAIで業務アプリを自作する仕組みや、処理の難しさでモデルを使い分ける設計も紹介されています。

## 何を作ったか

中心にあるのは3つの取り組みです。

- **取引照合アプリ**: 社内システムに入った取引の記録が、顧客が承認し実際に執行された内容と一致しているかを確かめる。裏付けの書類を集め、主要な条件を突き合わせ、食い違いがあれば人の確認に回す
- **Chatham Vibes**: 社員が自分の業務に合わせたアプリを作れる社内基盤。満期を迎える金利キャップ取引の確認と価格表・顧客向け連絡の準備、債券の金利表の作成、ヘッジのダッシュボード作り、取引確認書の点検などに使われている
- **Chatham Onyx**: 資産・借入・デリバティブのデータを1か所にまとめ、顧客と担当者が同じデータを見ながらAIを使える顧客向けの基盤。その中のChatFINは、過去の市場データの傾向をまとめ、顧客のポートフォリオの説明や、借入・デリバティブ・リースの契約書の該当箇所を探してリンクを示す

取引照合は、Chathamが顧客向けに提供する業務改革サービス「Process Zero」の最初の事例でもあります。業務ごとに必要な最小限の入力と証拠を洗い出し、人の判断が欠かせない箇所を決め、残りをAIとAIで作った道具に任せる、という進め方です。

## どう作ったか

アプリの開発にはCodexを使い、アプリの中のAI機能にはGPT-5.6系のモデルを使っています。Onyxでは、Codexを企画・開発・テスト・文書化・レビューまで開発の全工程で使っていると、同社のJohn DeGuenther CTOは述べています。

特徴的なのはモデルの使い分けです。Onyxは、GPT-5.6 Sol、GPT-5.6 Terra、GPT-5.4、GPT-4.1の4つを組み合わせています。

:::quote https://openai.com/index/chatham-financial/ | OpenAI導入事例「Chatham scales its capital markets expertise with OpenAI」
> Tasks like simple analysis and non-production testing are routed to the most cost-effective models, while GPT‑5.6 is used for complex tasks that need to maximize accuracy and value.
簡単な分析や本番以外のテストは最も費用対効果の高いモデルに回し、精度と価値を最大にしたい複雑な処理にはGPT-5.6を使っています。
:::

社員が作るVibesのアプリも同じ考え方で、AI機能は標準でGPT-5.6 Terraが動き、アプリごとの設定でGPT-5.6 Solに上げられます。社員はアプリを作るときにはさまざまなモデルを使えるとしています。全社では、ChatGPTとCodexを調べもの、分析、文書の下書き、ソフトウェア開発などに日常的に使っています。

## 成果（同社の公表値）

公表された数字は、取引照合の時間短縮です。AI助言部門を共同で率いるAlex Nordlinger氏は、OpenAIの事例ページで次のように述べています。

:::quote https://openai.com/index/chatham-financial/ | OpenAI導入事例「Chatham scales its capital markets expertise with OpenAI」
> In early measurement, the application reduced review from approximately 30 minutes to under 4 minutes.
初期の計測では、アプリによって確認作業が約30分から4分未満に縮みました。
:::

ここで目を引くのは、速さより検証の順番です。Nordlinger氏は同じ発言の中で、自動化を広げる前に実際の取引で性能を確かめていることも同じくらい大事だと強調しています。Chathamはアプリの結果を熟練の担当者の判断と並べて比べている段階で、ほかの取引の種類への拡大や、自動化の範囲を広げるのはその後としています。金融の照合業務では、間違いを見逃す損失のほうが時間の節約より大きいためです。

{{card:https://openai.com/index/chatham-financial/|Chatham scales its capital markets expertise with OpenAI|OpenAI}}

なお、事例はOpenAIが自社の顧客を紹介するために公開したもので、30分から4分未満という数字も同社の初期計測です。照合の正確さがどの程度か、何件で測ったかは示されていません。

## 日本のビジネスへの影響

日本でもCodexとOpenAIのAPIは使えます。真似しやすいのは、取引照合のように「記録と証拠書類を突き合わせ、食い違いだけを人に回す」業務です。銀行の約定確認、経理の請求書と発注書の照合、保険の契約内容の点検などが当てはまります。

向いているのは、金融機関や事業会社の経理・バックオフィス部門と、社内の開発担当です。今すぐやれることは、照合業務を1つ選び、過去の100件ほどで「AIの判定」と「担当者の判定」を並べて比べることです。いきなり自動化せず、Chathamと同じく人の判断との一致率を先に測ります。モデルは全件を高いモデルで処理せず、書類の読み取りは安いモデル、食い違いの判断は上位モデルと分けると費用を抑えやすくなります。

注意点は、社員が自由にアプリを作る仕組みの統制です。Chathamは顧客に届く前に専門家が中身を確かめる前提を置いています。日本で同じことをするなら、誰が作ったアプリがどのデータに触れ、どこまで顧客向けに使ってよいかを、先に決めておく必要があります。Codexを含むコーディングAIの料金と選び方は[AIコーディングツールのおすすめ](/best/coding/)にまとめています。
