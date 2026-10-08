---
{
  "title": "AnthropicがClaude Haiku 5.5を公開、前の版より平均75%安く問い合わせ対応や要約向け",
  "description": "AnthropicはClaudeの軽量モデルHaiku 5.5を公開した。前の版より動かす費用が平均75%安く、仕事の模擬試験ではOpenAIの軽量版を上回った。同時にMaxとTeamの会員へ月100〜500ドル分の開発用クレジットを配る。",
  "date": "2026-10-08T10:54:00+09:00",
  "category": "models",
  "tags": ["Anthropic", "Claude Haiku 5.5", "Claude", "API", "料金"],
  "summary": [
    "Anthropicは10月7日、Claudeで最も小さく速いモデル「Claude Haiku 5.5」を公開し、動かす費用は前の版より平均75%安いとした",
    "実際の職業の作業を模した試験では、前のHaiku 4.5を大きく上回り、OpenAIの軽量版GPT-6 Lunaよりも高い点を出した",
    "あわせて有料のMaxとTeamの会員に、Claudeを自社の道具に組み込むための月100〜500ドル分のクレジットを配り始める"
  ],
  "sources": [
    {"title": "Introducing Claude Haiku 5.5", "publisher": "Anthropic", "url": "https://www.anthropic.com/claude-haiku-5-5", "kind": "公式発表"},
    {"title": "Models overview", "publisher": "Claude Platform Docs", "url": "https://platform.claude.com/docs/en/about-claude/models/overview", "kind": "公式ドキュメント"},
    {"title": "Claude の投稿", "publisher": "X @claudeai", "url": "https://x.com/claudeai/status/2107894039626277339", "kind": "X投稿"},
    {"title": "Claude の投稿（料金）", "publisher": "X @claudeai", "url": "https://x.com/claudeai/status/2107894052041490537", "kind": "X投稿"},
    {"title": "Claude Haiku 5.5", "publisher": "Simon Willison's Weblog", "url": "https://simonwillison.net/2026/Oct/7/claude-haiku-5-5/", "kind": "公式サイト"},
    {"title": "Anthropic upgrades Claude with new Haiku 5.5 model, details here", "publisher": "9to5Mac", "url": "https://9to5mac.com/2026/10/07/anthropic-upgrades-claude-with-new-haiku-5-5-model-details-here/", "kind": "報道"},
    {"title": "Claude Haiku 5.5 arrives with massive price cuts proving the AI pricing arms race is far from over", "publisher": "The Decoder", "url": "https://the-decoder.com/claude-haiku-5-5-arrives-with-massive-price-cuts-proving-the-ai-pricing-arms-race-is-far-from-over/", "kind": "報道"}
  ],
  "thumb_text": "Claude Haiku 5.5",
  "thumb_style": "diorama",
  "thumb_prompt": "A miniature post office diorama where one tiny courier on a toy scooter races between towering stacks of thousands of envelopes, sorting them into neat bins, while a small price tag on the counter is cut down by a giant pair of scissors.",
  "share_text": "Claude Haiku 5.5が登場。前の版より平均75%安く、問い合わせ対応や大量の要約向けの軽量AI",
  "editor_note": ""
}
---
Anthropicは現地時間10月7日、AI「Claude」の軽量モデル「Claude Haiku 5.5」を公開しました。同社のモデルの中で最も安く速いモデルで、動かす費用は前の版のHaiku 4.5より平均75%下がったとしています。

## 何が発表されたか

Claude Haiku 5.5とは、要約、分類、データの検索、顧客からの問い合わせへの即答など、量が多く1件あたりの費用を抑えたい作業向けのAIモデルです。Claudeには上位の「Opus」、中位の「Sonnet」、軽量の「Haiku」があり、今回は9月のOpus 5.5、Sonnet 5.5に続く「5.5」世代の3つ目です。

料金は、企業が自社のサービスに組み込むときの従量課金（API）で決まります。100万トークン（トークンはAIが文章を数える単位）あたりの価格を前の版と比べると、次のとおりです。

| 100万トークンあたり | Haiku 5.5（10万トークン以下の依頼） | Haiku 5.5（10万トークン超） | Haiku 4.5 | Sonnet 5.5 |
|---|---|---|---|---|
| 読み込む文章 | $0.10 | $0.50 | $1.00 | $2.00 |
| 書き出す文章 | $0.50 | $2.50 | $5.00 | $10.00 |

:::quote https://www.anthropic.com/claude-haiku-5-5 | Anthropic公式発表「Introducing Claude Haiku 5.5」
> Claude Haiku 5.5 is priced 90% lower than Claude Haiku 4.5 for requests up to 100,000 tokens, and 50% lower for requests over 100,000 tokens.
Claude Haiku 5.5の価格は、10万トークン以下の依頼ではHaiku 4.5より90%、10万トークンを超える依頼では50%低く設定されています。
:::

「平均75%安い」は、この値下げに、同じ作業で使うトークン数が少し増える分を差し引いた数字です。Anthropicによると、前の版への依頼の約90%は10万トークン以下に収まっていました。

{{card:https://platform.claude.com/docs/en/about-claude/models/overview|Models overview（Claudeのモデル一覧と料金）|Claude Platform Docs}}

性能面では、Haikuとして初めて「どれだけ考えるか」の段階を選べるようになりました。公式の資料によると、一度に読める量は100万トークンです。Anthropicが公表した試験の結果では、前の版との差が大きく出ています。

- **実際の職業の作業を模した試験**（44職種の仕事を採点。数字が大きいほど良い）: Haiku 5.5は1620で、Haiku 4.5の735、OpenAIの軽量版GPT-6 Lunaの1437を上回りました。中位のSonnet 5.5は1840です
- **パソコンを操作して作業を終える試験**: 正答率は72.4%で、Haiku 4.5の15.7%から大きく伸びました

提供先はAnthropicのAPIのほか、Amazon Web Services、Google Cloud、Microsoft Azureです。会話アプリのClaudeでどう使えるかは、発表には書かれていません。

あわせて、2つの変更も発表されました。1つは中位のSonnet 5.5の値下げで、一度読んだ文章を使い回すときの料金を半分にし、多くの作業で費用が約20%下がるとしています。もう1つは、月額の有料プラン「Max」と「Team」の会員に、Claudeを自社の道具に組み込むためのAPIクレジットを毎月配ることです。今週から、Max（5倍）は月100ドル、Max（20倍）は月200ドル、Teamは組織全体で最大500ドル分が付きます。

## 背景

軽量モデルは、1件ずつは単純でも件数が多い作業を担います。たとえば、問い合わせメールの振り分け、議事録の要約、大きなAIが資料を作る間に必要な数字だけを探してくる「下請け役」などです。こうした用途では、性能の差より1件あたりの費用と速さが効きます。

OpenAIは9月に軽量版のGPT-6 Lunaを出しており、Haiku 5.5の10万トークン以下の価格は、Lunaと同じ水準です。Anthropicは、難しいプログラミングの作業には引き続きSonnet 5.5やOpus 5.5が向くと説明しており、Haikuを上位モデルの置き換えではなく、補う役として位置づけています。

## 反応と論点

Anthropicは公式Xで、前の版より平均で約75%安く動かせると強調しました。

{{x:https://x.com/claudeai/status/2107894039626277339}}

早く試した企業の声も公式発表に並んでいます。営業支援のHubSpotは、顧客管理の作業を模した社内試験で、これまで試した小型モデルで最も高い92.8%を記録したと述べました。タスク管理のAsanaは、作業完了までの待ち時間が30%以上縮んだとしています。

一方で、AIの検証ブログで知られる開発者のSimon Willison氏は、注意点を2つ挙げています。1つは、文章を区切る方式が変わり、同じ文章でも前の版の約1.25倍のトークンとして数えられることで、同氏はこれを「hidden price increase（見えにくい値上げ）」と書きました。もう1つは、10万トークンを超える長い依頼では料金が5倍に上がるため、その領域ではGPT-6 Lunaの方が割安だという指摘です。

## 日本のビジネスへの影響

- **使えるか**: APIとAWS、Google Cloud、Azure経由で日本からも使えます。料金はドル建てです。会話アプリのClaudeでの扱いは発表されていないため、まずは自社のシステムに組み込む人向けの話です
- **誰にどう効くか**: 問い合わせ窓口やチャットボットを運営する事業担当者と、それを作る開発会社への影響が大きくなります。1件あたりの費用が大きく下がるので、これまで費用が合わずに人手で回していた大量の分類や要約を、AIに任せる判断がしやすくなります。MaxかTeamを契約している会社は、毎月のクレジットで試作の費用をまかなえます
- **今すぐやれること**: 今Haiku 4.5や他社の軽量モデルで動かしている処理があれば、同じ依頼をHaiku 5.5に流し、品質と月額の費用を並べて比べてください。MaxかTeamを契約しているなら、配られるクレジットの受け取り方をClaudeのヘルプで確かめておきます
- **注意点**: 長い資料を丸ごと読ませる使い方では、10万トークンを超えた分の単価が5倍になります。数え方の変更で実際の請求は表の単価ほど下がらない可能性もあるので、本番の前に少量で請求額を確かめてください

Claudeの料金プランの全体像は[Claude Codeの料金の記事](/news/20261008-claude-code-pricing-plans/)、APIの料金比較は[AI API（LLM）の料金比較と選び方](/best/api/)にまとめています。
