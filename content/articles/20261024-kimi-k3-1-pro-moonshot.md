---
{
  "title": "Kimiの新AI「K3.1 Pro」がClaude上位モデルに迫る、料金は半分で11月に中身も公開",
  "description": "中国Moonshot AIがKimiの新モデル「Kimi K3.1 Pro」を公開した。第三者の総合評価では55点で世界4位、首位のClaude Opus 5.5（58点）に迫る。APIの料金は入力100万トークンあたり2ドルで、前のK3より3割安い。",
  "date": "2026-10-24T17:40:00+09:00",
  "category": "models",
  "tags": ["Kimi", "Kimi K3.1 Pro", "Moonshot AI", "中国AI", "オープンウェイト", "料金"],
  "summary": [
    "中国のMoonshot AIが、対話AI「Kimi」の新モデルKimi K3.1 Proを10月23日に公開した",
    "第三者の総合評価で55点の世界4位、首位のClaude Opus 5.5（58点）との差は3点だった",
    "料金はClaude Opus 5.5の半分で、11月4日までに誰でもダウンロードできる形で中身を公開する"
  ],
  "sources": [
    {"title": "Introducing Kimi K3.1 Pro", "publisher": "Kimi（Moonshot AI）", "url": "https://www.kimi.ai/blog/kimi-k3-1-pro", "kind": "公式発表"},
    {"title": "Model Inference Pricing", "publisher": "Kimi API Platform", "url": "https://platform.kimi.ai/docs/pricing/chat", "kind": "公式ドキュメント"},
    {"title": "Kimi.ai の投稿", "publisher": "X @Kimi_Moonshot", "url": "https://x.com/Kimi_Moonshot/status/2113680701770068067", "kind": "X投稿"},
    {"title": "Artificial Analysis の投稿", "publisher": "X @ArtificialAnlys", "url": "https://x.com/ArtificialAnlys/status/2113688083145314416", "kind": "X投稿"},
    {"title": "Introducing Kimi K3.1 Pro", "publisher": "Simon Willison's Weblog", "url": "https://simonwillison.net/2026/Oct/23/kimi-k31-pro/", "kind": "報道"},
    {"title": "Chinese AI model Kimi K3.1 Pro is closing in on Anthropic's Claude Opus 5.5", "publisher": "The Decoder", "url": "https://the-decoder.com/chinese-ai-model-kimi-k3-1-pro-is-closing-in-on-anthropics-claude-opus-5-5/", "kind": "報道"}
  ],
  "thumb_prompt": "A tiny runner in a red tracking suit closing the gap on a much larger runner on a miniature stadium track, with a price tag cut in half lying on the lane.",
  "thumb_style": "diorama",
  "thumb_text": "Kimi K3.1 Pro",
  "share_text": "中国のKimiが新モデルK3.1 Proを公開。総合評価でClaude Opus 5.5に3点差、料金は半分。11月4日までに中身も公開",
  "editor_note": ""
}
---
中国のAI企業Moonshot AIは現地時間10月23日、対話AI「Kimi」の新しいモデル「Kimi K3.1 Pro」を公開しました。AIの性能を比べる米Artificial Analysisの総合評価では55点で世界4位に入り、首位のAnthropic「Claude Opus 5.5」（58点）に3点差まで迫っています。APIの料金はClaude Opus 5.5の半分で、11月4日までにはモデルの中身（重み）も公開すると約束しています。

## 何が発表されたか

Kimi K3.1 Proとは、前のモデル「Kimi K3」を土台に、追加の訓練を大幅に増やして仕上げ直したモデルです。一度に読める量は100万トークン（日本語の本で数冊分）で、文章だけでなく画像も読み取れます。

{{x:https://x.com/Kimi_Moonshot/status/2113680701770068067}}

Moonshot AIは公式Xで、ゲームを丸ごと作るプログラミング、3Dソフトでの立体の作成、事実の正確さを強みに挙げました。あわせて、応答が2〜3倍速い「Kimi K3.1 Pro Highspeed」も出しています。

使える場所は、Webとスマホアプリの「Kimi」、パソコン用アプリ「Kimi Work」（3.1.0以降）、プログラミング用の「Kimi Code」、それに企業や開発者向けのAPIです。法人向けの「Kimi Business」では、管理者が有効にするまで使えない設定で始まります。

:::quote https://www.kimi.ai/blog/kimi-k3-1-pro | Kimi公式ブログ「Introducing Kimi K3.1 Pro」
> Kimi K3.1 Pro and Kimi K3.1 Pro Highspeed are available today on Kimi.ai, Kimi Work, Kimi Code, and the Kimi API. The full model weights will be released by Nov 4.
Kimi K3.1 ProとKimi K3.1 Pro Highspeedは、本日からKimi.ai、Kimi Work、Kimi Code、Kimi APIで使えます。モデルの重みは11月4日までにすべて公開します。
:::

重みが公開されると、誰でもダウンロードして自社のサーバーで動かせるようになります。ただし全体で2.8兆パラメーター（AIの規模を表す数）あり、動かすには大型のGPUサーバーが要ります。

## 料金は前のモデルより3割安い

APIの料金表（10月24日時点）では、前のK3より値下げされています。

| モデル | 入力（100万トークンあたり） | 出力（同） | 繰り返し読む部分の入力 |
|---|---|---|---|
| Kimi K3.1 Pro | 2ドル | 10ドル | 0.2ドル |
| Kimi K3.1 Pro Highspeed | 4ドル | 20ドル | 0.2ドル |
| Kimi K3（前のモデル） | 3ドル | 15ドル | 0.3ドル |
| （参考）Claude Opus 5.5 | 4ドル | 20ドル | 0.2ドル |
| （参考）GPT-6.1 Sol | 2ドル | 10ドル | 0.1ドル |

Claude Opus 5.5のちょうど半分で、OpenAIの中位モデルGPT-6.1 Solと同じ水準です。

{{card:https://platform.kimi.ai/docs/pricing/chat|Model Inference Pricing（料金表）|Kimi API Platform}}

## 性能はどこまで迫ったか

Moonshot AIが公表した成績では、AIにパソコン上で実際の作業をさせる試験「Terminal-Bench 4.0」で65.7%となり、OpenAIの最上位モデルGPT-6 Astra（58.2%）を上回り、Claude Opus 5.5（66.4%）に僅かに届きませんでした。財務資料を読み比べて数字を出す試験「OfficeQA Pro v2」では、比べたモデルの中で最も高い64.4でした。

仕事で気になるのは、もっともらしい間違い（ハルシネーション）です。Moonshot AIの社内試験では、主張ごとの誤りの割合がK3の23.4%から8.3%に下がりました。同社は、間違えやすい問題をわざと集めた試験であり、ふだんの誤り率ではないと断っています。

これらは自社の試験の結果です。外部の評価として、Artificial Analysisは公式Xで、K3.1 Proが総合評価で4位に入り、重みが公開されればオープンなモデル（中身を公開しているモデル）で首位になると投稿しました。

{{x:https://x.com/ArtificialAnlys/status/2113688083145314416}}

The Decoderは、同社の評価で上位にいるのはClaude Opus 5.5（58点）、Claude Sonnet 5.5とMetaのMuse Wonder Full（いずれも56点）だと報じています。中身を公開しているモデルと非公開の最上位モデルの差は、12点から3点に縮まる計算です。

## 背景と論点

中国勢はDeepSeekやアリババのQwenのように、中身を無料公開して安く使えるモデルで存在感を高めてきました。Kimi K3は、AIデジマの[ローカルで動かせるAIのガイド](/best/local-llm/)でも、公開評価でオープンなモデルの最上位として扱っています。

一方で懸念もあります。Moonshot AIは今回、悪用されやすいサイバー攻撃の能力を抑えるため、公開版の訓練からその種のデータを取り除いたと説明しました。社内の脆弱性（ソフトの弱点）探しの試験では、取り除く前の90.5%が81.0%に下がっています。OpenAIは10月、Moonshot AIの関係者が自社モデルの答えを大量に引き出して学習に使おうとしたと公表しており（[OpenAIがKimi開発元の関係者による「蒸留」を阻止](/news/20261001-openai-moonshot-distillation-campaign/)）、米国では中国製AIを政府から締め出す動きも出ています（[DeepSeekを米国の政府機関から締め出し](/news/20261020-dhs-deepseek-federal-agencies-ban/)）。

## 日本のビジネスへの影響

- **使えるか**: Kimiのアプリと英語版サイトkimi.ai、APIは日本からも登録できます。公式発表に日本語対応への言及はありませんが、前のK3は投票型の比較サイトLMArenaの日本語部門で8位（10月6日確認時点）に入っていました。料金はドル建てです。
- **誰にどう効くか**: AIを自社のサービスや社内ツールに組み込んでいる開発・企画の担当者には、Claudeの上位モデルに近い性能を半額で試せる選択肢になります。財務資料の読み込みや分析を任せたい経理・企画の担当者にとっても、得意分野として名指しされている点は試す理由になります。
- **今すぐやれること**: 社外秘を含まない過去の資料を使い、いまClaudeやChatGPTでやっている要約や表の作成をKimiでも試し、答えの正確さと費用を並べて比べてみてください。
- **注意点**: 中国企業のサービスなので、顧客情報や社外秘をKimiのアプリやAPIに送るかどうかは、社内の情報管理の決まりを先に確かめる必要があります。11月4日に重みが公開されれば、自社のサーバーで動かしてデータを外に出さない使い方もできますが、その場合は大型のGPUサーバーの費用がかかります。
