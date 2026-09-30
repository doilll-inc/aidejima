---
{
  "title": "中国GLM-5.3の攻撃コード作成力はMythos級、安全策は簡単に外れるとAnthropic",
  "description": "Anthropicは、中国Zhipu AIのオープンウェイトモデルGLM-5.3の攻撃コード作成能力が、限定公開のClaude Mythos Previewに近いと報告した。安全策も簡単な手法で64〜100%回避できたという。",
  "date": "2026-09-30T20:25:00+09:00",
  "category": "policy",
  "tags": [
    "Anthropic",
    "Zhipu",
    "GLM",
    "セキュリティ",
    "中国AI",
    "オープンソース"
  ],
  "summary": [
    "Chrome V8の既知の脆弱性を使う試験で、GLM-5.3は410回中50回攻撃コードを完成させた",
    "Claude Mythos Previewは56回で、GLM-5.2やClaude Opus 4.6はほぼ0%だった",
    "拒否機能の除去は約4,400ドルの計算費で可能。Anthropicは政府による安全性試験を求めた"
  ],
  "sources": [
    {
      "title": "GLM-5.3 and the spread of advanced cyber capabilities",
      "publisher": "Anthropic",
      "url": "https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities"
    },
    {
      "title": "CAISI's Assessment of Z.ai's GLM-5.3 Cyber Capabilities",
      "publisher": "NIST",
      "url": "https://www.nist.gov/news-events/news/2026/09/caisis-assessment-zais-glm-53-cyber-capabilities"
    },
    {
      "title": "zai-org/GLM-5.3",
      "publisher": "Hugging Face",
      "url": "https://huggingface.co/zai-org/GLM-5.3"
    },
    {
      "title": "Anthropic says Zhipu's open-weight GLM-5.3 nearly matches Claude Mythos Preview at building exploits",
      "publisher": "The Decoder",
      "url": "https://the-decoder.com/anthropic-says-zhipus-open-weight-glm-5-3-nearly-matches-claude-mythos-preview-at-building-exploits/"
    },
    {
      "title": "A quote from Anthropic Frontier Red Team",
      "publisher": "Simon Willison's Weblog",
      "url": "https://simonwillison.net/2026/Sep/29/anthropic-frontier-red-team/"
    },
    {
      "title": "GLM-5.3 and the spread of advanced cyber capabilities",
      "publisher": "Hacker News",
      "url": "https://news.ycombinator.com/item?id=49897075"
    },
    {
      "title": "Anthropic CEO Dario Amodei says he does not support open-weight AI ban",
      "publisher": "Axios",
      "url": "https://axios.com/2026/07/27/anthropic-open-weight-ban-china-dario-amodei"
    },
    {
      "title": "Anthropic Says Never Sought Ban on Open-Weights AI Models",
      "publisher": "Bloomberg Law",
      "url": "https://news.bloomberglaw.com/artificial-intelligence/anthropic-says-never-sought-ban-on-open-weights-ai-models"
    }
  ],
  "editor_note": "",
  "thumb_text": "GLM-5.3",
  "thumb_kicker": "Zhipu"
}
---
Anthropicで最先端モデルの危険な能力を検証するFrontier Red Teamは現地時間9月29日、中国Zhipu AI（海外ではZ.ai）のオープンウェイトモデル「GLM-5.3」の分析を公表しました。攻撃コード（エクスプロイト）を自力で組み上げる能力は、Anthropicが限定公開にとどめている「Claude Mythos Preview」に迫るとしています。一方で安全策は、簡単な手法で64〜100%の割合で回避できたと報告しました。

## 何が発表されたか

Anthropicは、外部とつながらない隔離環境で、自ら用意した標的だけを相手に試験したと説明しています。主な結果は次のとおりです。

| 試験 | GLM-5.3 | Claude Mythos Preview |
|---|---|---|
| ExploitBench（Chrome V8の既知の脆弱性から攻撃コードを作る） | 410回中50回成功 | 410回中56回成功 |
| 社内のバイナリ攻撃試験（OSS-Fuzz参加プロジェクトの100課題） | 4% | 6% |

後者では、Claude Opus 4.6や前世代のGLM-5.2は1件も成功しませんでした。Anthropicは、GLM-5.3はMythos Previewに及ばないものの「意味のある一線を越えた」としています。

専門家がモデルを使う実験も行いました。ある研究者は約1日で、広く使われるブラウザー（Linux版）のJavaScriptエンジンから未知の脆弱性を複数見つけ、ページを開いただけで閲覧者のファイルを読み取れる攻撃につなげました。脆弱性は開発元に報告済みです。

小型版のGLM-5.3-Flashでは、公開済みのChromeの脆弱性と別の既知の欠陥を組み合わせた攻撃を、人の関与20分とモデルの作業8時間で完成させました。ZhipuのAPI料金に換算すると20.40ドルだったといいます。

安全策の回避率は次のとおりです。

- **偽の設定を与える**（演習中のレッドチームだと思い込ませる）：64%
- **思考の書き出しを先に埋める**（検討済みで実行すると決めた体裁にする）：92%
- **拒否機能を取り除いた改変版**を使う：100%

拒否機能の除去（abliterationと呼ばれる手法）は、Anthropicのチームが初めて試して約2,200 GPU時間、約4,400ドルの計算費で済みました。慣れたチームなら約600 GPU時間とみています。改変後も一般的な能力はほとんど落ちず、公開から数日で改変版が出回ったとしています。Claudeについては、偽の設定は安全策で防がれ、思考の書き出しを埋める操作はAPIでできず、重みも公開していないため改変もできない、とAnthropicは説明しています。

## 背景

米国立標準技術研究所（NIST）のCAISIによると、GLM-5.3は8月14日に公開され、その2週間後に重みが配布されました。Hugging Face上の本体は約7,500億パラメーターで独自ライセンス、Flash版はMITライセンスです。CAISIは9月17日の評価で、GLM-5.3を「これまでで最もサイバー能力の高いオープンウェイトモデル」とし、米国の最先端から約4か月遅れの水準と結論づけました。Anthropicの結果もこれとおおむね一致します。

Mythos Previewは、Anthropicが約5か月前に発表したモデルで、同社は高度な攻撃コードを最初から最後まで自力で作れる初のモデルと位置づけています。同社は悪用を懸念して一般公開を避け、防御側の組織に限って提供してきました。今回の報告は、同等の能力が誰でもダウンロードできる形で出回ったことを示しています。

Anthropicは結論として、政府がGLM-5.3の後継を含む高性能モデルの安全性試験を行うべきだと主張しました。防御側が攻撃側と同等以上のモデルを使えるよう、自社モデルの提供も広げるとしています。

## 反応と論点

Hacker Newsの投稿には約230ポイント、約220件のコメントが付き、批判が多数を占めました。競合を名指しした報告は利益相反ではないか、オープンウェイトモデル規制への地ならしではないか、という指摘です。閉じたモデルはセキュリティ業務でも拒否が多く、防御のためにこそ制限のないモデルが必要だという声や、結果的にGLM-5.3の宣伝になっているという皮肉も目立ちました。一方で、公開された重みは回収できず、危険性は現実だとする意見もあります。

規制をめぐっては、AnthropicのDario Amodei CEOが7月27日、オープンウェイトモデルの禁止を主張したことはないと表明しています（AxiosやBloomberg Lawが報道）。今回の報告も求めているのは政府による試験で、禁止ではありません。ただし、中国製オープンモデルへの規制論が米国で強まるきっかけになるかは注視が必要です。

## 日本のビジネスへの影響

GLM-5.3は日本からもHugging Faceで入手でき、各種APIでも使えます。攻撃者が使える道具の水準が上がったことは、日本企業にとっても前提の変化です。

特に影響が大きいのは、公開済みの脆弱性への対応速度です。Flash版の例のように、公開済みの情報から攻撃コードを仕上げるまでがモデルの作業8時間、約20ドルで済むなら、パッチ適用を後回しにできる期間は短くなります。ブラウザーや各種ドライバー、ネットワーク機器など、報告で名前が挙がった分野の更新は優先度を上げるべきです。

中国製のオープンウェイトモデルを社内で使う企業は、ライセンスの違い（本体とFlash版で条件が異なる）や、出所のわからない改変版を使っていないかを確認しておくと安心です。自社のシステムやコードの点検に使う防御目的の利用は正当な使い方ですが、利用範囲と記録を社内で決めておくことが前提になります。
