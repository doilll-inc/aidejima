---
{
  "title": "DeepSeekの格安AIが料金そのままで性能アップ、自社の試験ではClaudeの前世代を上回る項目も",
  "description": "中国のDeepSeekが10月17日、軽量版AI「V4.1-Flash」の更新版を公開した。APIの料金は据え置きで、出力100万トークンあたり最大1.20ドルとClaude Opus 5.5の約17分の1。独立評価機関の指数も39から45に上がった。",
  "date": "2026-10-19T18:20:00+09:00",
  "category": "models",
  "tags": ["DeepSeek", "DeepSeek-V4.1-Flash-1017", "中国AI", "オープンウェイト", "料金"],
  "summary": [
    "中国のDeepSeekが10月17日、格安AI「V4.1-Flash」の更新版を公開し、Webとアプリ、開発者向けのAPIで使えるようにした",
    "DeepSeekの試験では、プログラム修正などの項目で米AnthropicのClaude Opus 5やOpenAIのGPT-5.6 Solを上回ったとしている",
    "APIの料金は据え置きで、文章を出力する単価はClaude Opus 5.5の約17分の1。ただしデータは中国で保存される"
  ],
  "sources": [
    {"title": "DeepSeek-V4.1-Flash-1017: Wish-Driven Programming Made Real", "publisher": "DeepSeek API Docs", "url": "https://api-docs.deepseek.com/news/news261017", "kind": "公式発表"},
    {"title": "DeepSeek の投稿", "publisher": "X @deepseek_ai", "url": "https://x.com/deepseek_ai/status/2111375640717033777", "kind": "X投稿"},
    {"title": "Models & Pricing", "publisher": "DeepSeek API Docs", "url": "https://api-docs.deepseek.com/quick_start/pricing", "kind": "公式ドキュメント"},
    {"title": "DeepSeek-V4.1-Flash-1017（モデルカード）", "publisher": "Hugging Face deepseek-ai", "url": "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017", "kind": "公式ドキュメント"},
    {"title": "Claude の料金", "publisher": "Anthropic", "url": "https://platform.claude.com/docs/en/about-claude/pricing", "kind": "公式ドキュメント"},
    {"title": "DeepSeek V4.1 Flash 1017 (Max)", "publisher": "Artificial Analysis", "url": "https://artificialanalysis.ai/models/deepseek-v4-1-flash-1017", "kind": "公式ドキュメント"},
    {"title": "DeepSeek-V4.1-Flash-1017 on AA & Vals index", "publisher": "Reddit r/LocalLLaMA", "url": "https://www.reddit.com/r/LocalLLaMA/comments/1x9owju/deepseekv41flash1017_on_aa_vals_index/", "kind": "コミュニティ"},
    {"title": "DeepSeek pushes out updated AI model it says is faster, leaner", "publisher": "The Star", "url": "https://www.thestar.com.my/tech/tech-news/2026/10/19/deepseek-pushes-out-updated-ai-model-it-says-is-faster-leaner", "kind": "報道"},
    {"title": "DeepSeek's Post-Training Lead Declares \"Entering the Era of Democratized Wish-Driven Coding\"", "publisher": "Wccftech", "url": "https://wccftech.com/deepseeks-post-training-lead-declares-entering-the-era-of-democratized-wish-driven-coding-as-v4-1-flash-1017-model-smokes-openais-gpt-5-5-sol/", "kind": "報道"},
    {"title": "DeepSeek's Upgraded V4.1-Flash Model Shakes Up AI Industry", "publisher": "The Information", "url": "https://www.theinformation.com/briefings/deepseeks-upgraded-v4-1-flash-model-shakes-ai-industry", "kind": "報道"}
  ],
  "thumb_prompt": "A small cheap paper price tag hanging from a gleaming racing car engine on a workbench, next to a much larger and heavier engine with an enormous price tag.",
  "thumb_style": "photo",
  "thumb_text": "V4.1-Flash-1017",
  "share_text": "DeepSeekが格安AIを更新。料金据え置きで性能アップ、出力単価はClaude Opus 5.5の約17分の1",
  "editor_note": ""
}
---
中国のAI企業DeepSeekは現地時間10月17日、軽量で安い対話AI「DeepSeek-V4.1-Flash」の更新版「DeepSeek-V4.1-Flash-1017」を公開しました。料金は据え置きのまま性能を引き上げ、自社の試験ではプログラムの修正や業務の自動化といった項目で、米AnthropicのClaude Opus 5やOpenAIのGPT-5.6 Solを上回ったとしています。

## 何が発表されたか

DeepSeek-V4.1-Flash-1017とは、9月10日に出たV4.1-Flashを改良した版です。DeepSeekはWeb版・スマホアプリ・開発者向けのAPI（自社のシステムからAIを呼び出す窓口）で同日から切り替え、中身のデータもHugging Faceで公開しました。ライセンスはMITで、商用でも条件なく使えます。

DeepSeekは公式Xで、前の版より試験の成績が良く、作業が速く終わり、出力も短くなったと説明しています。出力が短いほど、使った分だけ払う料金も下がります。

{{x:https://x.com/deepseek_ai/status/2111375640717033777}}

公式発表の題は「Wish-Driven Programming Made Real（願うだけでプログラムができる）」です。作例として、北京の故宮（紫禁城）の3Dモデルや、ゲーム「Portal 2」をゲーム制作ソフトGodotで再現したものを挙げています。

DeepSeekがモデルカードで示した主な成績は次のとおりです（いずれもDeepSeekが自社で測った数字）。

| 試験（測るもの） | 新版 | 前の版 | Claude Opus 5 | GPT-5.6 Sol |
|---|---|---|---|---|
| DeepSWE v1.1（ソフトの不具合修正） | 77.0 | 74.2 | 74.0 | 73.0 |
| Automation-Bench（業務の自動化） | 60.5 | 54.8 | 50.3 | 45.8 |
| Terminal-Bench 4.0（PCの操作を伴う作業） | 42.3 | 31.2 | 51.8 | 39.9 |
| HLE（専門家レベルの難問、道具なし） | 42.6 | 36.8 | 56.3 | 44.5 |

上の2つではClaude Opus 5を上回った一方、PC操作や難問ではまだ差があります。比べている相手はAnthropicの現行の上位モデルClaude Opus 5.5ではなく、その前の版です。

## 料金は据え置き、時間帯で半額に

APIの料金表によると、`deepseek-flash` という名前で呼ぶと新版につながり、単価は前の版から変わっていません。AIが読み書きする文字の量の単位である100万トークンあたり、混み合う時間帯で入力0.30ドル・出力1.20ドルです。

:::quote https://api-docs.deepseek.com/quick_start/pricing | DeepSeek API Docs「Models & Pricing」
> Off-peak rates are half of the peak rates.
混雑しない時間帯の料金は、混雑時の半額です。
:::

混雑時は平日の協定世界時1〜4時と6〜10時、日本時間では平日の10〜13時と15〜19時です。それ以外の時間と週末は出力0.60ドルになります。AnthropicのClaude Opus 5.5は出力20ドルなので、DeepSeekは混雑時の1.20ドルでも約17分の1です。

あわせて、Web検索とWebページの読み込みをAPIで呼べる機能も始めました。1,000回あたり0.75ドルで、DeepSeek Harness・Claude Code・Codexから呼ぶ分は北京時間11月1日0時まで無料です。

{{card:https://api-docs.deepseek.com/quick_start/pricing|Models & Pricing|DeepSeek API Docs}}

## 背景

V4.1-Flashは9月10日に登場した軽量版で、画像も読み取れ、一度に100万トークンまで扱えます。マレーシアのThe Starは、9月の発表時に値付けが安すぎて、香港市場で競合のMiniMax・Z.ai・Alibabaの株価が下がったと報じています。

米国の大手が高性能・高価格の上位モデルで競うなか、中国勢は中身を公開した安いモデルで追い上げる構図が続いています。米The Informationも今回の更新について、業界に大きな波紋を広げていると報じました。

## 反応と論点

第三者の評価も上がっています。AIの性能と価格を独自に測るArtificial Analysisは、新版の総合指数を45とし、同じ規模の中身公開モデル121種のなかで2位に置きました。前の版は39でした。

一方で、自社の数字との差を指摘する声もあります。開発者が集まるRedditのr/LocalLLaMAでは、Terminal-Bench 4.0がモデルカードでは42.3なのに、Artificial Analysisの測定では34、別の評価サイトVals Indexでは31.82だったという投稿がありました。投稿者は、DeepSeekがClaude Codeを使って測ったと明記している点を挙げ、測り方の違いが原因ではないかと見ています。

DeepSeekの事後学習の責任者とされるWu Yu氏も、発表に先立ってXに「願うだけでプログラムができる時代の民主化」という趣旨の投稿をしたと、Wccftechが報じています。安定性には課題も残ります。The Starは、DeepSeekのサービスが直前に約5時間止まり、計算資源の不足を原因とみる専門家もいると伝えました。

## 日本のビジネスへの影響

- **使えるか**: DeepSeekのWeb版・アプリ・APIは日本からも使えます。料金はドル建てで、チャージした残高から差し引く形です。中身のデータも公開されているので、自社のサーバーで動かす選択肢もあります（ただし大型のGPUサーバーが必要です）。
- **誰にどう効くか**: AIを自社のサービスや業務システムに組み込んでいる開発責任者や、AIの利用料に悩む事業責任者に関係が深い話です。問い合わせの下書きや大量の文書の分類など、件数が多い作業ほど単価の差が効きます。
- **今すぐやれること**: いま上位モデルで回している作業のうち、機密を含まないものを10〜20件選び、DeepSeekの新版にも同じ指示を出して品質と費用を比べてみてください。時間帯をずらせる一括処理なら、日本時間の夜や週末に回すと半額になります。
- **注意点**: DeepSeekのプライバシーポリシーでは、データは中国で収集・処理・保存され、学習にも使われます（拒否は可能）。顧客の個人情報や社外秘を送る前に、社内規程を確認してください。成績表の数字は自社測定で、第三者の測定では低めに出た項目もあります。

APIの料金をほかの会社と並べて比べるなら、[AI API（LLM）の料金比較と選び方](/best/api/)にまとめています。DeepSeekの安いモデルを手元のPCで動かす試みは[ds4はRedis作者が作るローカルLLMエンジン](/news/20261003-antirez-ds4-dwarfstar-local-llm/)でも紹介しました。
