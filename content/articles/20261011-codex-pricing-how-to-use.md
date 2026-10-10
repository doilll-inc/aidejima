---
{
  "title": "Codexの料金と使い方、ChatGPTの無料版でも試せて本格的に使うなら月20ドルのPlusから",
  "description": "OpenAIのCodexは単体では売られておらず、ChatGPTの各プランに含まれる。無料版でも小さな作業なら試せ、月20ドルのPlusで上位モデルが使える。10月11日時点の公式の料金ページと手順書で、プランごとの違いと始め方を整理した。",
  "date": "2026-10-11T03:10:00+09:00",
  "category": "dev",
  "format": "howto",
  "tags": ["Codex", "OpenAI", "ChatGPT", "料金", "使い方", "コーディング"],
  "summary": [
    "Codexは単体では売られておらず、ChatGPTの無料版・Go・Plus・Pro・Businessなどすべてのプランに含まれる",
    "無料版と月8ドルのGoは軽いモデルだけで、上位のGPT-6.1 SolやGPT-6 Astraを使うには月20ドルのPlus以上が必要",
    "Codexの利用枠はChatGPTの作業機能「ChatGPT Work」と共通で、Plusは5時間ごとの上限、Proにはその上限がない"
  ],
  "sources": [
    {"title": "Pricing | ChatGPT Learn", "publisher": "OpenAI（ChatGPT Learn）", "url": "https://learn.chatgpt.com/docs/pricing", "kind": "公式ドキュメント"},
    {"title": "Quickstart | ChatGPT Learn", "publisher": "OpenAI（ChatGPT Learn）", "url": "https://learn.chatgpt.com/docs/quickstart", "kind": "公式ドキュメント"},
    {"title": "Codex CLI | ChatGPT Learn", "publisher": "OpenAI（ChatGPT Learn）", "url": "https://learn.chatgpt.com/docs/codex/cli", "kind": "公式ドキュメント"},
    {"title": "料金 | ChatGPT", "publisher": "OpenAI", "url": "https://chatgpt.com/ja-JP/pricing/", "kind": "公式ドキュメント"}
  ],
  "thumb_text": "Codex 料金",
  "thumb_style": "3d",
  "thumb_prompt": "Four transparent capsule-shaped vending machine pods of increasing size lined up on a desk, each holding a tiny glowing robot holding a wrench, and the smallest free pod's robot is cheerfully fixing a giant laptop twice its size.",
  "share_text": "Codexの料金は？ChatGPTの無料版から使えるが上位モデルは月20ドルのPlusから。10月11日時点の公式情報でプランと始め方を整理",
  "editor_note": ""
}
---
Codexの料金は、ChatGPTのプラン料金にそのまま含まれる形で、無料版でも試せます。ただし、OpenAIの上位モデルで本格的に作業させるには月20ドルのPlus以上が必要です。この記事では、10月11日時点のOpenAIの公式の料金ページと手順書をもとに、プランごとの違いと始め方を整理します。

## Codexとは、何ができるか

Codexとは、OpenAIが提供する、AIにプログラムを書かせたり直させたりする道具です。チャットにコードを貼り付けて質問するのと違い、Codexは指定したフォルダの中身を自分で調べ、ファイルを書き換え、コマンドを実行して結果を確かめるところまで進めます。

使える場所は、パソコン用のChatGPTアプリ（Mac・Windows・Linux）、ブラウザ、黒い画面に命令を打ち込む「ターミナル」、VS Codeなどの開発ソフト、iPhoneです。クラウド上に作業場所を作っておけば、パソコンを閉じても作業を続けさせられます。

プログラマー以外の使い方も広がっています。AIデジマでは、米Oracleが採用の下調べにChatGPTやCodexを使っている例（[既報](/news/20261009-oracle-chatgpt-work-codex-recruiting/)）や、米国の開発者が料理をしながらCodexに声で指示してブログの機能を作った例（[既報](/news/20261010-codex-voice-simon-willison-cooking/)）を紹介しました。

## 料金とプラン

公式の料金ページは、Codexの扱いを次のように説明しています。

:::quote https://learn.chatgpt.com/docs/pricing | OpenAI「Pricing | ChatGPT Learn」
> ChatGPT Work and Codex are included in your ChatGPT Free, Go, Plus, Pro, Business, Edu, or Enterprise plan. ChatGPT Work and Codex share usage.
ChatGPT WorkとCodexは、ChatGPTの無料版・Go・Plus・Pro・Business・Edu・Enterpriseの各プランに含まれる。ChatGPT WorkとCodexは利用枠を共有する。
:::

ChatGPT Workは、ChatGPTに調べものや資料づくりを最後まで任せる機能です。Codexとは同じ枠から使うので、Workをたくさん使った日はCodexに使える量も減ります。料金ページで確認したプランは次のとおりです（ドル建て）。

| プラン | 月額 | Codexで使えるもの |
|---|---|---|
| 無料版 | 0ドル | 軽いモデルのGPT-6 Lunaだけ（パソコン用アプリで順次提供）。ちょっとした作業向け |
| Go | 8ドル | 無料版と同じGPT-6 Luna |
| Plus | 20ドル | 上位のGPT-6.1 SolとGPT-6 Lunaに加え、ブラウザ・ターミナル・開発ソフト・iPhoneから使える |
| Pro | 100ドル・200ドル・500ドルの3段階 | 5時間ごとの上限なし。500ドルの段階では、さらに速いUltrafastモードも使える |
| Business | 1人20ドル（年払い、2人以上）。月払いは25ドル | Plusと同じ水準の利用枠。チームで管理できる |
| Enterprise・Edu | 要問い合わせ | 管理機能やデータの保管場所の指定など |

OpenAIの日本語の料金ページは、日本から開くと円で表示されます。AIデジマの用途別ガイドで10月1日に確認した時点では、Plusが月3,000円、Proが月16,800円からでした。

どれくらい使えるかの目安も料金ページにあります。Plusと標準的なBusinessでは、パソコン上での作業の依頼が5時間あたり、最上位のGPT-6 Astraで5〜45回、GPT-6.1 Solで15〜160回、軽いGPT-6 Lunaで350〜3,000回です。クラウドでの作業はこれより多く枠を使い、週単位の上限がかかることもあります。Proには現時点で5時間ごとの上限がありません。

{{card:https://learn.chatgpt.com/docs/pricing|Pricing | ChatGPT Learn|OpenAI}}

### 足りないときはクレジットか従量課金で

PlusとBusinessでは、枠を使い切ったときにChatGPTのクレジットを買い足せます。消費量はモデルで大きく違い、100万トークン（文章の量の単位）あたりのクレジットは、GPT-6.1 Solが入力50・出力250、GPT-6 Astraが入力250・出力1,250です。速く答えさせる「Fast」モードは、プランに含まれる枠を通常の2.5倍の速さで消費します。

月額プランを使わず、開発者向けのAPIキーで使った分だけ払う方法もあります。どのプランでも選べますが、ターミナルや開発ソフトからだけで、クラウドの機能は使えません。料金ページは、APIの単価はプランの枠とは別物なので、プランで何回使えるかの見積もりに使わないよう注意しています。

## 始め方

公式の手順書によると、プログラムに詳しくない人はパソコン用アプリから始めるのが簡単です。

1. ChatGPTのパソコン用アプリをダウンロードしてインストールする（Mac・Windows・Linuxに対応）
2. アプリを開き、ChatGPTのアカウントでログインする
3. 作業させたいフォルダを開く（ChatGPTはそのフォルダのファイルを読み書きできるようになる）
4. 画面上部の切り替えで「Codex」を選ぶ
5. 「このフォルダの表計算ファイルを月別に集計して」のように、やってほしいことを普段の言葉で書いて送る

ターミナルで使う場合は、MacかLinuxなら `curl -fsSL https://chatgpt.com/codex/install.sh | sh` でインストールし、作業したいフォルダで `codex` と打ちます。初回に「Sign in with ChatGPT」を選べば、契約中のプランの枠で使えます。

## 仕事での使いどころ

- **マーケター**: 広告や販売の実績の表計算ファイルをフォルダに入れ、「媒体別に費用対効果を集計してグラフにして」と頼む。集計の小さなプログラムをCodexが書いて動かすので、関数を組む手間が省けます
- **事業・企画の担当者**: 社内向けの申請フォームや商品一覧のページを、説明文だけで試作させる。エンジニアに頼む前のたたき台を自分で用意できます
- **開発者**: 不具合の調査やテストの作成をクラウドの作業場所で任せ、その間は別の仕事を進める。急ぎでない作業を軽いGPT-6 Lunaに回せば、上位モデルの枠を節約できます

## 日本のビジネスへの影響

- **使えるか**: ChatGPTは日本でも提供されており、Codexも日本のアカウントで同じプランから使えます。料金ページは日本から開くと円で表示されます。Codex単体の対応言語の一覧は公式には見当たりません
- **誰にどう効くか**: すでにChatGPT Plusを契約しているマーケターや企画担当者は、追加料金なしで表計算の集計や簡単なページの試作を任せられます。毎日長時間コードを書く開発者は、Plusの5時間ごとの上限に届きやすいので、Proか、使った分だけ払うAPIキーとの比較が要ります
- **今すぐやれること**: 無料版のままパソコン用アプリでCodexを開き、繰り返している集計作業を1つ頼んでみます。軽いモデルで物足りなければ、Plusで上位モデルに切り替えて差を比べます
- **注意点**: ChatGPT Workと枠を共有するため、両方を使う人は上限に早く届きます。Codexはフォルダ内のファイルを書き換えるので、大事なファイルはコピーを取ってから任せてください。古いGPT-5.5は10月14日にCodexを含むChatGPTの全プランで提供が終わります

AnthropicのClaude Codeとの比較は「[Claude Codeの料金](/news/20261008-claude-code-pricing-plans/)」、ほかの道具も含めた選び方は[コーディングAIのおすすめと料金比較](/best/coding/)にまとめています。
