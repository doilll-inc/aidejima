---
{
  "title": "ThinkingBoxはAIエージェントに同じ業務を20回やらせる試験、首位のOpus 5.5でも合格は47%",
  "description": "Microsoftが業務エージェントの評価基盤ThinkingBoxを公開した。507の業務を各20回実行し、データベースの最終状態で採点する。1回あたりの成功率は首位のClaude Opus 5.5で67.16%、20回すべて成功した業務は47.53%だった。",
  "date": "2026-10-04T10:40:00+09:00",
  "category": "research",
  "tags": ["Microsoft", "ThinkingBox", "エージェント", "ベンチマーク", "Claude Opus 5.5", "GPT-6 Astra"],
  "summary": [
    "MicrosoftのCopilot Studioチームが、AIエージェントを返答ではなくデータベースの最終状態で採点する評価基盤ThinkingBoxと、507業務の試験を公開した",
    "ThinkingBoxの試験では18モデルに各業務を20回ずつ解かせ、1回あたりの成功率は首位のClaude Opus 5.5で67.16%、20回すべて成功した業務は47.53%にとどまった",
    "ThinkingBoxで失敗した試行の67.24%は、エラーを出さずに正常終了し、データの変更も実行していた。返答やツール呼び出しの確認だけでは失敗を見逃す"
  ],
  "sources": [
    {"title": "The Agent Said It Was Done. The Database Disagreed.", "publisher": "Hugging Face Blog（Microsoft）", "url": "https://huggingface.co/blog/microsoft/thinkingbox", "kind": "公式発表"},
    {"title": "One Success Isn't Reliability: Thinkingbox, a Sandbox and Benchmark for Agents in Stateful Business Workflows", "publisher": "arXiv", "url": "https://arxiv.org/abs/2608.19741", "kind": "論文"},
    {"title": "microsoft/thinkingbox", "publisher": "GitHub Microsoft", "url": "https://github.com/microsoft/thinkingbox", "kind": "公式ドキュメント"},
    {"title": "microsoft/ThinkingBox-Bench", "publisher": "Hugging Face", "url": "https://huggingface.co/datasets/microsoft/ThinkingBox-Bench", "kind": "公式ドキュメント"}
  ],
  "thumb_text": "ThinkingBox",
  "share_text": "AIエージェントに同じ業務を20回。Microsoftの新試験で、首位のClaude Opus 5.5でも全回成功は47%",
  "thumb_style": "illustration",
  "thumb_prompt": "A small robot office worker stacking the same box onto a shelf twenty times in a row, with a long row of green checkmarks and a few red crosses floating above it as a scorecard of shapes.",
  "editor_note": ""
}
---
MicrosoftのCopilot Studioチームは現地時間10月3日、AIエージェントが業務を「毎回」正しくこなせるかを測る評価基盤ThinkingBoxを、Hugging Faceのブログで公開しました。小売や保険など507の業務をそれぞれ20回ずつ解かせたところ、1回あたりの成功率が最も高かったClaude Opus 5.5でも、20回すべて成功した業務は全体の47.53%でした。

## 何が発表されたか

ThinkingBoxとは、AIエージェントにツールを使わせて業務を実行させ、その結果をデータベースの最終状態で採点する、オープンソースの評価用サンドボックス（隔離された実験環境）です。エージェントの返答や、ツールを正しい形式で呼んだかどうかは合否に使いません。業務ごとに用意した検査プログラムが、必要な変更が入ったか、余計な変更が無いかを確かめます。ツールはMCP（AIとツールをつなぐ標準規格）のサーバーとして用意され、毎回まっさらなデータから始めます。

あわせて公開した試験ThinkingBox-Benchは、5分野507業務です。内訳は小売98、自動車保険100、旅行104、ネット銀行の社内IT 104、コンサル会社のIT・人事サポート101で、各社の社内規定に従うことが条件になっています。フレームワークのコードはMIT、試験データはCDLA-Permissive-2.0で公開されました。強化学習用のリポジトリも「近日公開」としています。

:::quote https://huggingface.co/blog/microsoft/thinkingbox | Microsoft「The Agent Said It Was Done. The Database Disagreed.」（Hugging Face Blog）
> One good run tells you a model can do the work. It does not tell you whether it will do it again.
1回うまくいけば、そのモデルに仕事ができることはわかります。けれども、次もまたできるかどうかはわかりません。
:::

{{card:https://github.com/microsoft/thinkingbox|microsoft/thinkingbox|GitHub Microsoft}}

## 結果：1回の成功率と「20回連続」の差

ブログの表から、主なモデルの数字を抜き出しました。「20回すべて成功」は、507業務のうち20回の試行がすべて合格した業務の数です。

| モデル | 1回あたりの成功率 | 20回すべて成功した業務 | 確実にこなせる業務1件あたりの費用 |
|---|---|---|---|
| Claude Opus 5.5 | 67.16% | 241件（47.53%） | $7.80 |
| Claude Opus 5 | 66.50% | 241件（47.53%） | $13.30 |
| GPT-5.4 | 65.36% | 128件（25.25%） | $6.80 |
| GPT-6 Astra | 58.31% | 231件（45.56%） | $7.45 |
| Kimi-K3 | 57.37% | 68件（13.41%） | $20.68 |
| Qwen3.8-27B | 51.70% | 38件（7.50%） | $24.36 |

（出典：Microsoft「The Agent Said It Was Done. The Database Disagreed.」。費用は20回分の推定費用を、20回すべて成功した業務数で割った値）

目立つのは順位の入れ替わりです。GPT-5.4は1回あたりの成功率では3位ですが、20回すべて成功した業務は128件で、Claude Opus 5.5の約半分でした。逆にGPT-6 Astraは1回あたりでは58.31%にとどまるものの、20回連続でこなせた業務は231件あり、ブログは1回の成功率の78%を保ったと書いています。オープンウェイトではKimi-K3が1回あたり57.37%で最も高く、小売分野だけなら82.24%と全モデルで首位でしたが、20回連続は68件に落ちました。

旧世代との差も大きく出ました。Claude Opus 4.6の1回あたりの成功率は32.09%、Grok-4.3は14.38%です。分野別では旅行が難しく、Claude Opus 5.5も54.28%でした。この分野の首位はGPT-5.4の68.12%です。

## 失敗の多くは「正常終了」していた

論文によると、失敗した試行の多くは、エラーを出さずにデータを書き換えて終わっていました。ブログの集計では、失敗の67.24%が正常に終了し、データを変更する操作を実行し、最後のツール呼び出しでもエラーを返していません。ブログが冒頭で挙げた例では、配送が止まったままの家電の問い合わせで、エージェントはツールを9回正しく呼び、補償の対象外という判断も合っていました。それでも、本来「保留」にすべき問い合わせを「解決済み」にして終えています。

失敗の原因の内訳は、ツールの使い方の誤りが79.9%、データの更新の誤りが10.3%、利用者への対応が途中で終わったものが7.0%、データを変更しないまま終えたものが2.9%でした。

:::quote https://arxiv.org/abs/2608.19741 | 論文「One Success Isn't Reliability」（arXiv）
> Thinkingbox-bench reveals a large gap between occasionally finding a successful trajectory and reliably completing stateful business tasks.
Thinkingbox-benchは、たまに成功する手順を見つけることと、データの状態を変える業務を確実にこなすことの間に、大きな差があることを示しています。
:::

## 背景

エージェントの評価は、コードの修正やWeb操作など「実行して確かめる」試験に移ってきました。ただ、多くの試験は1回解かせた正答率（pass@1）を中心に報告されます。業務に組み込む企業にとっては、返金処理が1回うまくいっても次の4回で誤るなら使えません。ThinkingBoxはこの「繰り返しても崩れないか」を正面から測る点が新しく、論文はCopilot Studioチームの研究者やインターンら14人の連名で、8月に初版が出て10月1日に第4版に改訂されています。

一方で、今回の試験は5分野のシナリオで、使うツールも試験用に作ったものです。自社のシステムや規定でも同じ順位になるとは限りません。また、モデルの成績は各社のエージェントの作り方（指示文や手順の組み方）でも変わり、ThinkingBoxの結果はあくまで共通の条件で比べた値です。モデル単体の得意分野は[Pac-Benchの記事](/news/20261001-pac-bench-one-shot-pacman/)のように試験によって入れ替わります。

## 日本のビジネスへの影響

ThinkingBoxのコードと試験データはGitHubとHugging Faceで誰でも使えます。試験は英語のシナリオで、日本語の業務での成績は測られていません。料金はかからず、評価に使うモデルのAPI代だけが自社の負担になります。

関係が深いのは、問い合わせ対応や社内ITの手続きをエージェントに任せようとしている企業のDX担当と開発者です。モデル選びの基準を「1回の正答率」から「同じ業務を何回やらせても同じ結果になるか」と「確実にこなせる1件あたりの費用」に替える根拠になります。今回の結果では、1回あたりの成功率が近いモデル同士でも、20回連続でこなせる業務の数に約2倍の差がありました。

今すぐやれることは、自社で自動化したい業務を10件ほど選び、同じ入力で20回ずつ実行して、最後にデータベースや台帳の中身が正しいかを確かめることです。ThinkingBoxの仕組みをそのまま使えば、ツールをMCPサーバーとして模した環境で試せます。

注意点として、エージェントの「完了しました」という返事やツールのログは、成功の証拠になりません。本番では、更新後のデータを別の仕組みで検査する工程を残すべきです。APIで使うモデルの料金の比較は[AI API（LLM）の料金比較と選び方](/best/api/)にまとめています。
