---
{
  "title": "Aleph Alphaが中国製LLMの政治的偏りを測定、中立な回答は17〜41%どまり",
  "description": "独Aleph Alphaは、政治的に微妙な967問で中国製のオープンウェイトモデル6種を評価し、中立な回答は17〜41%にとどまったと公表した。中国製モデルで作った学習データを使ったNVIDIAのNemotron Cascade 2にも影響が出ていたという。",
  "date": "2026-10-05T03:10:00+09:00",
  "category": "policy",
  "tags": ["Aleph Alpha", "Qwen", "DeepSeek", "中国AI", "ソブリンAI", "オープンウェイト"],
  "summary": [
    "Aleph Alphaは天安門や台湾など56テーマから作った967問で、Qwen・DeepSeek・Kimiの計6モデルを評価した",
    "中国製6モデルの中立な回答は17〜41%で、Claude Sonnet 5は70%、Mistral Small 2603は92%だった",
    "中国製モデルで生成した学習データを使ったNVIDIAのNemotron Cascade 2も、17%の質問で中国共産党の立場に沿う回答をした"
  ],
  "sources": [
    {"title": "Training on the Party Line: Chinese Political Influence on LLMs in China and the World", "publisher": "Aleph Alpha", "url": "https://aleph-alpha.com/en/blog/training-on-the-party-line/", "kind": "公式発表"},
    {"title": "Chinese AI models parrot state doctrine or refuse to answer on sensitive topics", "publisher": "The Decoder", "url": "https://the-decoder.com/chinese-ai-models-parrot-state-doctrine-or-refuse-to-answer-on-sensitive-topics/", "kind": "報道"}
  ],
  "thumb_text": "中国製LLMの偏り",
  "share_text": "中国製LLM6種に政治的に微妙な967問。中立な回答は17〜41%。中国製モデルで作った学習データ経由でNVIDIAのモデルにも影響",
  "editor_note": ""
}
---
ドイツのAI企業Aleph Alphaは、中国製のオープンウェイトモデル（重みが公開され、自社の環境で動かせるモデル）6種に政治的に微妙な質問967問を投げ、中立な回答は17〜41%にとどまったとする調査結果を公式ブログで公開しました。公開は現地時間9月28日で、10月4日にThe Decoderが報じて注目を集めています。中国製モデルが作った学習データを通じて、米NVIDIAのモデルにも同じ傾向が入り込んでいたと指摘しています。

## 何が分かったか

調査は、天安門事件、台湾、新疆、チベット、香港、検閲など56のテーマを人の手で選び、そこからGPT-OSS 120Bに質問を作らせて967問にまとめたものです。回答の判定もGPT-OSS 120Bが行い、「中国共産党の主張をなぞる」「中立」「回答を拒む」の3つに分けました。

Aleph Alphaはブログの冒頭で、結論を次のようにまとめています。

:::quote https://aleph-alpha.com/en/blog/training-on-the-party-line/ | Aleph Alpha「Training on the Party Line」
> Chinese open-weight LLMs are strongly aligned with Chinese government positions on political issues. On our benchmark of 967 politically sensitive prompts, six Chinese models answered only 17 to 41 percent of prompts in a balanced way.
中国製のオープンウェイトLLMは、政治的な問題で中国政府の立場に強く沿っている。政治的に微妙な967問のベンチマークで、中国製6モデルが中立に答えたのは17〜41%にすぎなかった。
:::

モデルごとの結果は次のとおりです（ブログの図から編集部が作表）。

| モデル | 党の主張をなぞる | 中立 | 拒否 |
|---|---|---|---|
| Qwen 3.6 35B-A3B | 80% | 17% | 2.5% |
| Qwen 3.8 2.4T-A95B | 62% | 19% | 19% |
| DeepSeek R1 0528 | 77% | 22% | 0.8% |
| DeepSeek V4 Pro 0813 | 16% | 18% | 66% |
| Kimi K2.5 | 47% | 37% | 16% |
| Kimi K3 | 40% | 41% | 19% |
| Claude Sonnet 5（比較用） | 2.8% | 70% | 27% |
| Mistral Small 2603（比較用） | 8% | 92% | 0.2% |

世代による変化もありました。Aleph Alphaによると、中立な回答の割合は各社とも新旧でほぼ変わらない一方、Qwenは3.6で党の主張を述べていた質問の一部を3.8では拒否するようになり、DeepSeekではその傾向がさらに強く出ています。DeepSeek V4 Proは3分の2の質問に答えていません。

中国に触れない240問でも試したところ、領土問題や人権といったテーマでは、中国製モデルが中国共産党の論点を持ち出す場合があったとしています。ただし、評価したすべての中国製モデルで見られたわけではないとも書いています。

## 学習データ経由の「汚染」

意外な結果として挙げているのが、NVIDIAのNemotron Cascade 2 30B-A3Bです。中国製ではないこのモデルも、17%の質問で党の主張に沿う回答をしました。

原因として、NVIDIAが公開している追加学習（SFT）用のデータを調べたところ、会話データの応答の多くがDeepSeekやQwenで生成されており、930万行のうち約3,500行に中国共産党の論点が含まれていたといいます。ごく一部の混入でも、学習したモデルの振る舞いに表れたことになります。

一方で、影響の強さは中国製モデルほどではありません。Nemotron Cascade 2は75%の質問に中立に答え、中国に触れない質問では党の立場に寄る傾向は見られなかったとしています。

## 背景と論点

性能の高い中国製モデルは寛容なライセンスで公開されることが多く、他社が学習データを作る道具としても広く使われています。Aleph Alphaは、オープンウェイトの最先端を中国の研究所が占めている以上、初めて大規模なモデルを作る企業はその政治的な偏りと付き合わざるを得ないと指摘し、この問題は広く認識されていないと書いています。

この調査には割り引いて読むべき点もあります。The Decoderは、Aleph Alphaが政府などに「ソブリンAI（自国で管理できるAI）」を売る企業で、中国製モデルとの違いを示すことに商業的な利害があると指摘しています。Aleph Alpha自身も、判定に使ったLLMの偏りが調査の限界になりうると認めています。同社は先日、自社のオープンウェイトモデル「Kolibri-1」を公開したばかりです（[Kolibri-1の記事](/news/20261003-aleph-alpha-kolibri-1-open-weight/)）。

同社は対策として、追加学習データから中国の政治的な内容を検出して除き、望ましい振る舞いを示すデータを足し、今回のようなベンチマークで評価する、という3つを自社で取り入れたとしています。

## 日本のビジネスへの影響

QwenやDeepSeekのモデルは日本でも自由に入手でき、社内での運用や、日本語向けに追加学習したモデルの土台として使われています。調査の対象は中国関連の政治的な話題で、議事録の要約や翻訳、コード生成といった日常業務への影響は示されていません。

影響が大きいのは、中国製モデルを使って顧客向けのチャットボットや記事生成、教育サービスを提供している企業です。台湾や人権などに触れる質問が来たときに、党の主張をそのまま返すおそれがあります。中国製モデルで学習データを作り、自社モデルを追加学習している開発チームも、Nemotronの例のように偏りを引き継ぐ可能性があります。

今すぐできるのは、自社で使っているモデルに台湾・天安門・新疆などの質問を数十問投げ、回答を確かめることです。学習データを中国製モデルで生成している場合は、政治的な話題を含む行を抽出して点検する工程を足すと安心です。

注意点として、判定はLLMによる自動分類で、ブログで例として示された質問は英語です。日本語で同じ傾向が出るかは示されていません。手元で動かすモデルの選び方は[ローカルLLMのガイド](/best/local-llm/)にまとめています。
