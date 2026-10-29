---
{
  "title": "Claudeなど16のAIに税理士の実務50件を任せたら、合格は最高でも1割 客が聞かなかった落とし穴を見逃す",
  "description": "米Surge AIが、税の専門家が作った実務課題50件で16のAIを試験した結果を公開した。最高のClaude Sonnet 5.5でも合格率は10.8%、GPT-6 Astraは4.8%。計算はできても、依頼者が気づいていない期限や前提の確認を見落とした。",
  "date": "2026-10-29T20:40:00+09:00",
  "category": "research",
  "tags": ["Claude", "Claude Sonnet 5.5", "Surge AI", "DAYJOB", "税務", "エージェント"],
  "summary": [
    "米Surge AIが、税の専門家が作った実務の課題50件をAIに任せる試験「DAYJOB: Tax」の結果を10月27日に公開した",
    "首位はClaude Sonnet 5.5で合格率10.8%、OpenAIのGPT-6 Astraは4.8%、GoogleのGemini 4 Argonは3.2%だった",
    "AIは計算や個々の手順はこなせても、依頼者が聞かなかった期限や、書類から疑うべき前提を見落とすことが多かった"
  ],
  "sources": [
    {"title": "DAYJOB: Tax — Benchmarking AI Agents on Professional Tax Work", "publisher": "Surge AI", "url": "https://surgehq.ai/blog/dayjob-tax", "kind": "公式発表"},
    {"title": "DAYJOB: Tax Benchmark（リーダーボード）", "publisher": "Surge AI", "url": "https://surgehq.ai/benchmarks/dayjob-tax", "kind": "公式発表"},
    {"title": "DAYJOB: Can Agents Survive a 9 to 5?", "publisher": "Surge AI", "url": "https://surgehq.ai/blog/dayjob", "kind": "公式発表"}
  ],
  "thumb_text": "DAYJOB: Tax",
  "thumb_prompt": "A 3D render of a tidy accountant's desk where a small friendly robot proudly holds up a perfectly calculated tax form, while behind it a calendar page with one date circled in red is quietly slipping off the desk unnoticed.",
  "thumb_style": "3d",
  "share_text": "Claudeなど16のAIに税理士の実務50件を任せたら、合格は最高でも1割。計算はできても客が聞かなかった期限を見逃す",
  "editor_note": ""
}
---
AIの評価データを作る米Surge AIは現地時間10月27日、税の専門家が作った実務の課題50件をAIに任せる試験「DAYJOB: Tax」の結果を公開しました。試した16のAIのうち最高のAnthropic「Claude Sonnet 5.5」でも合格率は10.8%で、OpenAIやGoogleの最上位モデルは5%を下回りました。

## 何が起きたか

DAYJOB: Taxとは、税理士や税務の担当者が実際にこなしている仕事を、依頼の受け付けから納品物の完成まで丸ごとAIに任せて採点する試験です。AIは依頼者からの相談と関係書類を受け取り、申告書や作業記録、ほかの人の申告内容の点検結果、依頼者への助言書を作ります。

課題は個人・家族、小規模事業、組合（パートナーシップ）、不動産・投資、相続・贈与・信託、国際税務、企業の取引、税務調査や争いの8分野にわたります。用意された書類は全部で1,789点あり、1件あたりの中央値は30点、多いものは123点です。PDFが1,487点、Excelが117点で、手書きの領収書の写真や作業員の派遣記録まで含まれます。

課題は、大手会計事務所での経験を持つ税の専門家が実務の流れをもとに作り、3段階の専門家の点検を経ています。採点は厳しめで、計算・根拠・重要な論点・納品物について決められた基準の95%以上を満たした場合だけ「合格」になります。

:::quote https://surgehq.ai/blog/dayjob-tax | Surge AI公式ブログ「DAYJOB: Tax — Benchmarking AI Agents on Professional Tax Work」
> These assignments test professional judgment alongside tax knowledge, calculations, retrieval, and instruction following.
これらの課題は、税の知識や計算、資料探し、指示どおりに進める力とあわせて、専門家としての判断力を試します。
:::

## 結果

Surge AIが公開した順位表の主な結果は次のとおりです（いずれも各社のモデルを最も深く考えさせる設定で試したもの）。

| 順位 | AIモデル | 開発元 | 合格率 |
|---|---|---|---|
| 1 | Claude Sonnet 5.5 | Anthropic | 10.8% |
| 2 | Claude Fable 5.1 | Anthropic | 9.6% |
| 3 | Claude Opus 5.5 | Anthropic | 9.2% |
| 5 | Grok 4.7 | xAI | 5.0% |
| 6 | GPT-6 Astra | OpenAI | 4.8% |
| 7 | GPT-6.1 Sol | OpenAI | 4.0% |
| 9 | Gemini 4 Argon | Google | 3.2% |
| 14〜16 | Kimi K3・Mistral Large 4・Qwen 3.8 Max | 各社 | 0% |

上位3つをAnthropicのClaudeが占めましたが、それでも10回に1回程度しか合格していません。Surge AIは、かかった費用と成績の釣り合いでもClaude Sonnet 5.5とClaude Opus 5.5が優れていたとしています。

## AIは何を見落としたか

Surge AIが紹介した失敗例は、どれも「計算は合っているのに、プロなら気づくべきことに気づかない」というものです。

1つ目は、マンションの売却時期の相談です。依頼者は2024年8月に退去しており、2026年10月と2027年1月のどちらで売るのが得かを尋ねました。米国では、売却前の5年のうち2年以上住んでいれば売却益の一部（最大25万ドル）に税がかかりません。AIはどちらの時期でも条件を満たすと正しく答えましたが、売却が2027年8月末より遅れるとこの優遇を失うという期限には触れませんでした。GPT-6 Astraは5回試して一度もこの期限を指摘せず、Claude Opus 5.5は5回とも指摘しました。

2つ目は、別れようとしている2人が老後のための口座をどう分けるかという相談です。今度は逆に、Claude Opus 5.5が5回とも「2人は法律上の夫婦ではない」と決めつけて助言しました。書類には、事実婚を条件つきで認めるテキサス州で暮らしていたことや、コロラド州で式を挙げたことが残っており、夫婦と認められる可能性がありました。GPT-6 Astraは5回中4回、まず婚姻の状態を確かめる必要があると答えています。

ほかにも、帳簿にある「領収書添付」の領収書が実際には無いのに確認済みとして扱うか、依頼者が「アラバマ州だけで営業している」と言う会社の派遣記録に5つの州が並んでいることに気づくか、といった課題があります。

:::quote https://surgehq.ai/blog/dayjob-tax | Surge AI公式ブログ「DAYJOB: Tax — Benchmarking AI Agents on Professional Tax Work」
> A tax adviser should recognize consequential issues even when the client doesn't know to ask about them.
税の助言者は、依頼者が尋ねることすら知らない重要な問題にも気づくべきです。
:::

## 背景と論点

Surge AIは、AIの訓練や評価に使うデータを作る会社です。9月には同じ形式で医療と金融の実務を試す「DAYJOB」を公開しており、税務はその3分野目になります。

Surge AIによると、これまでの税のAI試験は「難しい質問に答えられるか」「申告書の数字を正しく計算できるか」のように、解くべき問題が最初から決まっているものが中心でした。DAYJOBは、何が問題なのかを自分で見つけられるかまで問う点が違うと説明しています。

一方で、この試験は米国の税制が前提で、課題も50件と多くはありません。合格の基準を95%と高く置いているため、「1割しか使えない」というより「人の確認なしに丸ごと任せられる仕事はまだ1割程度」と読むのが妥当です。また、評価データを作る会社自身が作った試験である点にも留意が必要です。

AIと専門職の関係については、米国の特許弁護士を追った実験で、AIを使うと若手の仕事は上達してもAIなしの実力は伸びなかったという研究もあります（[AIで若手の仕事は上達、でもAIなしの実力は伸びず](/news/20261025-ai-patent-lawyers-junior-expertise-study/)）。

## 日本のビジネスへの影響

- **使えるか**: 試験は米国の税制が前提で、日本の申告や税務相談で同じ結果になるとは限りません。ただし、見落としの型（期限、前提の確認、書類の欠け）は日本の実務にもそのまま当てはまります
- **誰にどう効くか**: 税理士事務所、経理・財務の担当者、そして確定申告や相続の相談にAIを使い始めた経営者に関係があります。AIは計算や書類の読み込みは速くても、「聞かれていないが重要なこと」を拾う力はまだ弱いということです
- **今すぐやれること**: AIに税務の相談や下書きを頼むときは、答えをもらったあとに「この判断が変わる期限や条件はあるか」「私が確認すべき前提は何か」と追加で聞く手順を決めておくと、今回の失敗例のような見落としを減らせます
- **注意点**: 合格率が最も高いClaudeでも、別の課題では前提を決めつけて誤った助言をしました。どのAIでも、申告や資産の分け方のように金額の大きい判断は、資格を持つ専門家の確認を外さないでください

用途に合わせたAIの選び方は、[AIチャット・アシスタントの選び方](/best/chat/)にまとめています。
