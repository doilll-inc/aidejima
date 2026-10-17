---
{
  "title": "Difyの使い方と料金、社内向けのAIチャットや自動化をコードなしで作れる 無料から始めて有料は月59ドル",
  "description": "Difyは、社内資料に答えるチャットボットや作業の自動化を、画面上で部品をつないで作れるAIツール。無料のSandboxから使え、有料のProfessionalは月59ドル。10月18日時点の公式情報で始め方と料金を整理した。",
  "date": "2026-10-18T01:30:00+09:00",
  "category": "products",
  "format": "howto",
  "tags": ["Dify", "LangGenius", "使い方", "料金", "エージェント", "オープンソース"],
  "summary": [
    "Difyは、社内資料に答えるチャットボットや仕事の手順を自動化するAIを、プログラムを書かずに画面上で組み立てられるツール",
    "クラウド版は無料のSandboxで試せ、有料はProfessionalが月59ドル、50人まで使えるTeamが月159ドル（年払いは約17%引き）",
    "中身は無料で公開されており、自社のサーバーに入れて使うこともできる。ただし複数の会社に貸し出す使い方などは別契約が必要"
  ],
  "sources": [
    {"title": "Dify Pricing - There's Always a Plan for You", "publisher": "Dify", "url": "https://dify.ai/pricing", "kind": "公式サイト"},
    {"title": "Dify ドキュメント", "publisher": "Dify Docs", "url": "https://docs.dify.ai/ja-jp/introduction", "kind": "公式ドキュメント"},
    {"title": "Quick Start", "publisher": "Dify Docs", "url": "https://docs.dify.ai/en/use-dify/getting-started/quick-start", "kind": "公式ドキュメント"},
    {"title": "Introduction", "publisher": "Dify Docs", "url": "https://docs.dify.ai/en/introduction", "kind": "公式ドキュメント"},
    {"title": "dify LICENSE（Open Source License）", "publisher": "GitHub langgenius/dify", "url": "https://github.com/langgenius/dify/blob/main/LICENSE", "kind": "公式ドキュメント"},
    {"title": "IF Con Tokyo 2026", "publisher": "Dify Blog", "url": "https://www.dify.ai/ja/blog/if-con-tokyo-2026-turn-what-If-into-production", "kind": "公式サイト"}
  ],
  "thumb_text": "Dify 使い方",
  "thumb_style": "3d",
  "thumb_prompt": "Colorful building blocks shaped like a speech bubble, a document folder and a gear snap together on a desk to form a small friendly robot, while a coffee mug sits beside the half-built assembly.",
  "share_text": "Difyは社内チャットボットや作業の自動化をコードなしで組み立てられるAIツール。無料から始められ有料は月59ドル。始め方を整理",
  "editor_note": ""
}
---
Difyとは、社内の資料をもとに答えるチャットボットや、「資料を読む→要約する→SNS向けに書き分ける」といった一連の作業をこなすAIの仕組みを、プログラムを書かずに画面上で部品をつないで作れるツールです。LangGeniusが開発しており、クラウド版は無料のSandboxプランから使え、有料のProfessionalプランは月59ドル（年払いなら年590ドル）です。この記事では10月18日時点の公式サイトと公式ドキュメントで、できること・料金・始め方を整理します。

## 何ができるか

Difyの公式ドキュメント（日本語版あり）は、Difyを次のように定義しています。

:::quote https://docs.dify.ai/en/introduction | Dify Docs「Introduction」
> Dify is an open-source platform for building AI applications.
Difyは、AIアプリケーションを作るためのオープンソースのプラットフォームである。
:::

オープンソースとは、中身（ソースコード）が無料で公開されていて、誰でも自分のサーバーに入れて使える形のことです。作れるものは大きく3つです。

- **チャットボット**: 社内規程や商品マニュアルなどの資料を読み込ませ、その中身にもとづいて答えさせる
- **ワークフロー**: 「入力を受け取る→AIで整理する→条件で分ける→決まった形で出力する」といった手順を、箱を線でつなぐように組み立てて自動化する
- **エージェント**: AIが自分で道具（検索や外部サービス）を選びながら作業を進める仕組み

作ったものはWebページとして公開して社内の人に使ってもらうか、API（ほかのシステムから呼び出す窓口）経由で自社のサービスに組み込めます。中で使うAIは1社に縛られず、公式の料金ページによると、OpenAI・Anthropic・Google（Gemini）・xAI・アリババ（Tongyi）のモデルを切り替えて試せます。

:::quote https://dify.ai/pricing | Dify公式サイト「Pricing」
> Message credits are provided to help you easily try out different models from OpenAI, Anthropic, Gemini, xAI, Tongyi in Dify. Credits are consumed based on the model type.
メッセージクレジットは、OpenAI・Anthropic・Gemini・xAI・TongyiのさまざまなモデルをDifyで手軽に試せるように提供される。クレジットはモデルの種類に応じて消費される。
:::

ChatGPTやClaudeのような「話しかけて使うAI」との違いは、**同じ作業を誰が何度やっても同じ手順で回る仕組み**を作れる点です。一度作れば、AIに詳しくない同僚もフォームに入力するだけで使えます。

## 料金とプラン

クラウド版（Dify Cloud）の料金は次のとおりです（10月18日に公式の料金ページで確認。円建ての表示はなく米ドル建てで、税は別）。

| プラン | 料金 | 人数 | 作れるアプリ | 読み込める資料 | AIの利用枠 |
|---|---|---|---|---|---|
| Sandbox | 無料 | 1人 | 5個 | 50件（50MB） | 200メッセージクレジット（1回限り） |
| Professional | 月59ドル（年払いは年590ドル） | 3人 | 50個 | 500件（5GB） | 毎月5,000クレジット |
| Team | 月159ドル（年払いは年1,590ドル） | 50人 | 200個 | 1,000件（20GB） | 毎月10,000クレジット |
| Enterprise | 要問い合わせ | 複数ワークスペース | — | — | — |

料金はワークスペース（チーム単位の作業場所）ごとで、1人ごとではありません。年払いにすると約17%安くなります。クレジットは使うAIの種類によって減り方が変わり、使い切った後は、自社で契約したOpenAIなどのAPIキー（AIを使うための鍵）に切り替えて使い続けられます。この場合、AIの利用料はDifyではなく各AI企業に払います。無料のSandboxのクレジットは毎月の補充がない1回限りの枠だと、公式のクイックスタートに書かれています。

{{card:https://dify.ai/pricing|Dify Pricing - There's Always a Plan for You|Dify}}

もう1つの選択肢が、無料のCommunity Editionを自社のサーバーやクラウドに入れて使う方法です。公式ドキュメントによると、Docker Compose（ソフトをまとめて起動する道具）で数分で立ち上げられます。社外にデータを出したくない場合に向きますが、サーバーの用意と保守は自社の担当になります。

## 始め方

公式のクイックスタートの手順を、初めて試す人向けにまとめると次のとおりです。

1. cloud.dify.ai を開き、無料で登録する（最初はSandboxプラン）
2. 「Integrations」で使うAIの提供元（例: OpenAI）を追加する。クレジットの範囲で使えるモデルならAPIキーなしで動く
3. 「Studio」で「Create from Blank」を選び、作るものの種類（ワークフローなど）を選んで名前を付ける
4. 画面上に「入力」「AIへの指示」「条件分岐」「出力」などの部品を並べ、線でつなぐ
5. 「Test Run」で試し、問題なければ「Publish」で公開する。直したら公開し直す

公式のチュートリアルでは、下書きと参考資料を入れると、指定した投稿先のSNSごとに文体を変えた投稿文を作るワークフローを例にしています。最初はこの例をなぞると、部品の役割がつかみやすくなります。

{{card:https://docs.dify.ai/ja-jp/introduction|Dify ドキュメント（日本語）|Dify Docs}}

## 仕事での使いどころ

- **人事・総務**: 就業規則や経費精算のルールを読み込ませた社内問い合わせ窓口を作り、よくある質問への一次回答を任せる。無料のSandboxは資料50件までなので、まず1つの規程で試せます
- **マーケター・広報**: 新商品の資料を入れると、プレスリリースの下書き、SNS投稿、メールマガジンの文面をそれぞれの型で出すワークフローを作る。担当者が変わっても同じ品質の下書きが出ます
- **営業企画**: 商談メモを貼ると、決まった項目（課題・予算・次の打ち手）に整理して出すフォームを作り、チームで使い回す

## 日本のビジネスへの影響

- **使えるか**: クラウド版は日本からそのまま登録して使えます。公式サイトと公式ドキュメントには日本語版があり、開発元は日本法人のLangGenius株式会社を通じて9月に東京で年次イベント「IF Con Tokyo 2026」を開くなど、日本での展開にも力を入れています。料金は米ドル建てです。
- **誰にどう効くか**: 社内でAI活用を任されたDX担当者や、エンジニアに頼まず業務を自動化したい企画・マーケティングの担当者に向きます。ChatGPTの個人利用から一歩進んで、「部署の誰でも同じ手順でAIを使える道具」を作りたい段階で候補になります。
- **今すぐやれること**: 無料のSandboxで、自部署のよくある質問を1つの資料にまとめて読み込ませ、チャットボットを1つ作ってみます。クレジットは200回分しかないので、試す相手は数人に絞るのが現実的です。
- **注意点**: 社内資料を外部のクラウドに置くことになるため、扱える情報の範囲を情報システム部門と先に決めておく必要があります。自社サーバーに入れる無料版も商用利用はできますが、ライセンス上、Difyを複数の会社向けのサービスとして貸し出すことや、画面のロゴ・著作権表示を消すことは、別途商用ライセンスが必要です。自社のAPIキーに切り替えた後のAIの利用料は、[AI APIの料金比較](/best/api/)で各社の単価を確かめられます。
