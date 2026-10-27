---
{
  "title": "OpenAIが新AI「GPT-6.1 Terra」、画面を見てパソコン作業を代行 料金は前のモデルの半分",
  "description": "OpenAIが中位の新モデルGPT-6.1 Terraを公開した。画面を読み取ってアプリを操作する作業が得意で、APIの料金は入力100万トークンあたり1ドルと前のGPT-5.6 Terraの半分。ChatGPT WorkとCodexでは有料プランで使える。",
  "date": "2026-10-27T10:55:00+09:00",
  "category": "models",
  "tags": ["OpenAI", "GPT-6.1 Terra", "ChatGPT Work", "Codex", "料金", "エージェント"],
  "summary": [
    "OpenAIは10月26日、画面を読み取ってアプリを操作するのが得意な新モデル「GPT-6.1 Terra」を公開した",
    "OpenAIによると、仕事の操作を試す試験で最上位のGPT-6 Astraに並び、1単位あたりの料金は10分の1",
    "ChatGPTの有料プラン（Plus・Pro・Enterprise・Edu）のChatGPT WorkとCodexで使え、APIの料金は前の版の半分"
  ],
  "sources": [
    {"title": "GPT-6.1 Terra: delivering fast and capable computer use at a lower price", "publisher": "OpenAI Developer Community", "url": "https://community.openai.com/t/gpt-6-1-terra-delivering-fast-and-capable-computer-use-at-a-lower-price/1409900", "kind": "公式発表"},
    {"title": "GPT-6.1 Terra Model | OpenAI API", "publisher": "OpenAI Developers", "url": "https://developers.openai.com/api/docs/models/gpt-6.1-terra", "kind": "公式ドキュメント"},
    {"title": "GPT-6.1 Terra System Card", "publisher": "OpenAI Deployment Safety Hub", "url": "https://deploymentsafety.openai.com/gpt-6-1-terra", "kind": "公式ドキュメント"},
    {"title": "OpenAI の投稿（発表）", "publisher": "X @OpenAI", "url": "https://x.com/OpenAI/status/2114780711664398349", "kind": "X投稿"},
    {"title": "OpenAI の投稿（Agents' Last Exam）", "publisher": "X @OpenAI", "url": "https://x.com/OpenAI/status/2114780717188272382", "kind": "X投稿"},
    {"title": "GPT-6.1 Terra in GitHub Copilot", "publisher": "GitHub Changelog", "url": "https://github.blog/changelog/2026-10-26-gpt-6-1-terra-in-github-copilot", "kind": "公式発表"},
    {"title": "GPT-6.1 Terra（Hacker News）", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=50248124", "kind": "コミュニティ"},
    {"title": "GPT-6.1 Terra", "publisher": "Simon Willison's Weblog", "url": "https://simonwillison.net/2026/Oct/26/gpt-61-terra/", "kind": "報道"},
    {"title": "GPT-6.1 Terra halves OpenAI's API prices and still gains ground on its larger models", "publisher": "The Decoder", "url": "https://the-decoder.com/gpt-6-1-terra-halves-openais-api-prices-and-still-gains-ground-on-its-larger-models/", "kind": "報道"},
    {"title": "OpenAI upgrades ChatGPT and Codex with new GPT-6.1 Terra model", "publisher": "9to5Mac", "url": "https://9to5mac.com/2026/10/26/openai-upgrades-chatgpt-and-codex-with-new-gpt-6-1-terra-model/", "kind": "報道"}
  ],
  "thumb_prompt": "A laptop on an office desk whose mouse cursor is moving by itself, filling in a long paper form, while a half-price tag hangs from the screen's corner.",
  "thumb_style": "photo",
  "thumb_text": "GPT-6.1 Terra",
  "share_text": "OpenAIが新モデルGPT-6.1 Terraを公開。画面を見てアプリを操作する作業が得意で、APIの料金は前の版の半分",
  "editor_note": ""
}
---
OpenAIは現地時間10月26日、中位の新モデル「GPT-6.1 Terra」を公開しました。パソコンの画面を読み取り、アプリをまたいで操作する作業を得意とし、APIの料金は入力100万トークンあたり1ドルと、前の「GPT-5.6 Terra」の半分に下がりました。ChatGPTでは有料プランの仕事用画面「ChatGPT Work」とプログラミング用の「Codex」で使えます。

## 何が発表されたか

GPT-6.1 Terraとは、OpenAIの4段階のモデル（下からLuna・Terra・Sol・Astra）のうち、下から2番目にあたる「速くて安い実務向け」のモデルです。9月に出たGPT-6.1 Sol（[OpenAIが「GPT-6.1 Sol」を公開](/news/20260930-openai-gpt-6-1-sol/)）や最上位のGPT-6 Astraより軽く、大量の定型作業をこなす用途を狙っています。

{{x:https://x.com/OpenAI/status/2114780711664398349}}

OpenAIは公式Xで、画面に何が映っているかを理解してアプリをまたいで操作し、自然な文章も書ける「1日の仕事全体に使えるモデル」だと紹介しました。報道によると、OpenAIは提案書の下書き、図面の読み取り、申込書などの入力を想定した使い道に挙げています。

提供範囲は、開発者向けの公式フォーラムでの発表に書かれています。

:::quote https://community.openai.com/t/gpt-6-1-terra-delivering-fast-and-capable-computer-use-at-a-lower-price/1409900 | OpenAI Developer Community「GPT-6.1 Terra: delivering fast and capable computer use at a lower price」
> GPT-6.1 Terra is rolling out now and is available to all Plus, Pro, Enterprise, and Edu users in ChatGPT Work and Codex. Developers can also access it through the OpenAI API as gpt-6.1-terra.
GPT-6.1 Terraは順次提供を始めており、Plus、Pro、Enterprise、EduのすべてのユーザーがChatGPT WorkとCodexで使えます。開発者はOpenAIのAPIから「gpt-6.1-terra」として使えます。
:::

同じ発表で、ChatGPT WorkとCodexの利用枠（プランごとに使える量）は、GPT-5.6 Terraより長持ちし、Solや Astraを使う場合よりはるかに多くの作業ができると説明しています。一方で、深い調べものや複雑なプログラミングにはSolかAstraを選ぶよう勧めています。

## 料金は前の版の半分、Solと比べても半分

APIの公式ドキュメント（10月27日時点）では、次の料金です。1トークンは英語でおよそ1単語弱の文字量です。

| モデル | 入力（100万トークンあたり） | 出力（同） | 一度読んだ部分の再入力 |
|---|---|---|---|
| GPT-6.1 Terra | 1ドル | 5ドル | 0.05ドル |
| GPT-6.1 Sol | 2ドル | 10ドル | 0.1ドル |
| GPT-6 Astra | 10ドル | 50ドル | ― |
| GPT-6 Luna | 0.1ドル | 0.5ドル | ― |
| （参考）Claude Sonnet 5.5 | 2ドル | 10ドル | ― |

一度に読める量は約105万トークン（入力は最大92.2万トークン）、一度に書ける量は12.8万トークンで、学習データは2026年6月1日までです。読み取れるのは文章と画像で、音声や動画には対応していません。

{{card:https://developers.openai.com/api/docs/models/gpt-6.1-terra|GPT-6.1 Terra Model（料金・仕様）|OpenAI Developers}}

## 性能はどこまで上がったか

OpenAIが強調したのは、職場のソフトをAIに操作させる試験「Agents' Last Exam」の結果です。

{{x:https://x.com/OpenAI/status/2114780717188272382}}

OpenAIは公式Xで、GPT-6.1 Terraがこの試験で最上位のGPT-6 Astraに並び、1トークンあたりの料金は10分の1、作業を終えるまでの時間はAstraやSolの平均3分の1以下だと投稿しました。いずれもOpenAI自身の測定です。

外部の評価では、AIの性能を比べる米Artificial Analysisの総合指数でTerraが48点となり、前のGPT-5.6 Terra（42点）から上がった一方、GPT-6.1 Sol（52点）には届かなかったとThe Decoderが報じています。

安全面では、OpenAIが公開した安全性の報告書で、サイバー攻撃に悪用されうる能力を社内基準の最も高い段階「Critical」と判定し、Solや Astraと同じ防御の仕組みを組み込んだとしています。心の健康に関する相談への対応を測る試験では55.5%と、前の版の46.2%から上がりました。

GitHubも同日、プログラミング支援の「GitHub Copilot」の有料プラン（Pro・Pro+・Max・Business・Enterprise）でGPT-6.1 Terraを選べるようにしました。

## 反応と論点

開発者が集まる掲示板Hacker Newsでは、発表の話題に約500ポイントが集まりました。OpenAIの社員テッド・サンダース氏は投稿で、モデルの序列が「Luna < Terra < Sol < Astra」であると整理し、APIを使う開発者にとっては、Solより安くLunaよりずっと賢い中間の選択肢になると説明しました。ChatGPTの有料会員にとっては大きな変化ではない、とも書いています。

批判で多かったのは名前のわかりにくさです。版の数字と4つの名前が混ざっていて、Terra 6.1がSol 6より上なのか下なのか判断できない、どの作業にどのモデルを選べばよいか公式の目安がない、といった声が出ました。開発者のサイモン・ウィリソン氏も自身のブログで、中位のモデルは選び方が難しいと指摘し、繰り返しの多いパソコン操作を安く回す用途に向くとの見方を示しています。

競争の面では、AnthropicのClaude Sonnet 5.5（入力2ドル・出力10ドル）に対し、同じ中位の層でちょうど半額になります。OpenAIは大口の顧客にも値引きでClaudeからの乗り換えを促していると報じられており（[OpenAIが大幅値引きでClaudeの大口客を奪う](/news/20261025-openai-discounts-poach-anthropic-claude-customers/)）、価格での競争がさらに強まりそうです。

## 日本のビジネスへの影響

- **使えるか**: ChatGPTの有料プラン（Plus以上）なら日本からも、ChatGPT WorkとCodexで選べます。発表で挙げられた対象に無料プランは含まれていません。APIの料金はドル建てです
- **誰にどう効くか**: 社内でAIに定型の事務作業（申込書の入力、資料の下書き、画面を見ながらの転記）を任せたい業務改革・情報システムの担当者には、費用を半分に抑えながら質を上げられる選択肢になります。APIで自社サービスにAIを組み込んでいる開発者は、GPT-5.6 Terraからの置き換えで請求額が下がる可能性が高いです
- **今すぐやれること**: APIでGPT-5.6 TerraやGPT-6.1 Solを使っている処理があれば、いくつかの作業をGPT-6.1 Terraに切り替えて、出来と費用を並べて比べる
- **注意点**: 性能の数字の多くはOpenAI自身の測定です。OpenAIも深い調べものや複雑な開発には上位のSolかAstraを勧めており、難しい仕事まで一律に置き換えると品質が落ちるおそれがあります。用途ごとの選び方は[AIのAPIの選び方ガイド](/best/api/)にまとめています
