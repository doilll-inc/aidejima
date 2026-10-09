---
{
  "title": "電力や水道へのサイバー攻撃にAIで備える、Anthropicが日立など11社と防衛計画",
  "description": "Anthropicは10月8日、電力網や水道などの重要インフラとオープンソースのソフトを守る「Anthropic Cyber Mission」を始めた。日立やCrowdStrikeなど11社と組み、無料のAI点検も提供。AIが見つけた弱点の候補は半年で2万9,000件を超えた。",
  "date": "2026-10-09T11:15:00+09:00",
  "category": "policy",
  "tags": ["Anthropic", "Anthropic Cyber Mission", "OSS Scanner", "セキュリティ", "Hitachi", "Claude"],
  "summary": [
    "Anthropicは10月8日、電力網・水道・交通などの重要インフラをサイバー攻撃から守る長期計画「Anthropic Cyber Mission」を発表した",
    "日立やCrowdStrike、PwCなど11社と組み、最新のAIと技術者をインフラを守る会社に提供する。電力会社などへは各社を通じて届ける",
    "世界中のソフトの土台となる無償公開のプログラムには、AIで弱点を探す点検「OSS Scanner」を無料で提供する"
  ],
  "sources": [
    {"title": "Introducing the Anthropic Cyber Mission", "publisher": "Anthropic", "url": "https://www.anthropic.com/news/anthropic-cyber-mission", "kind": "公式発表"},
    {"title": "Launching an opt-in vulnerability-finding service for open-source software", "publisher": "Anthropic", "url": "https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source", "kind": "公式発表"},
    {"title": "OSS Scanner", "publisher": "Anthropic", "url": "https://red.anthropic.com/oss-scanner", "kind": "公式ドキュメント"},
    {"title": "Anthropic launches free AI security scans for open-source projects", "publisher": "The Verge", "url": "https://www.theverge.com/ai-artificial-intelligence/1008521/anthropic-open-source-oss-scanner", "kind": "報道"}
  ],
  "thumb_text": "Cyber Mission",
  "thumb_style": "diorama",
  "thumb_prompt": "A miniature city power substation and water tower at dusk, guarded by tiny security workers holding flashlights, while a giant magnifying glass hovers over the tangled cables revealing a few glowing red cracks.",
  "share_text": "Anthropicが電力や水道を狙うサイバー攻撃への備えを支援する計画。日立など11社と組み、無償公開のソフトはAIで無料点検",
  "editor_note": ""
}
---
Anthropicは現地時間10月8日、電力網や水道、交通といった社会の重要インフラと、世界中のソフトの土台になっているオープンソース（誰でも無料で使える公開ソフト）をサイバー攻撃から守る長期計画「Anthropic Cyber Mission」を発表しました。日立製作所やCrowdStrikeなど11社と組んで最新のAIと技術者を送り込むほか、公開ソフトの開発者にはAIによる弱点の点検を無料で提供します。

## 何が発表されたか

Anthropic Cyber Missionとは、AIを悪用した攻撃が増えるなかで、守る側に道具・研究・資金を届けるための同社の取り組みの総称です。最初は2つの分野から始めます。

### 1. 電力や水道を守る会社にAIと技術者を

1つ目は「Critical Infrastructure Defense Program（重要インフラ防衛プログラム）」です。発電所や浄水場、工場の機械を動かす制御システムは何十年も使い続ける前提で作られており、止めて直すことが難しいため、知られた弱点が何年も残りがちです。Anthropicはここに、最新のClaudeのモデル、現場に出向く技術者、攻撃の動向の調査結果を提供します。

ただし電力会社や水道局に直接ではなく、それらが頼っている専門の会社を通じて届けます。最初の参加企業は、Accenture、Booz Allen、CrowdStrike、Deloitte、Dragos、日立製作所、Insane Cyber、Nozomi Networks、Palo Alto Networks、PwC、Rockwell Automationの11社です。コンサルティング会社、セキュリティ会社、制御機器のメーカーと、立場の違う会社が並びます。

Anthropicは6月から米国の州や地方政府向けにも同様の支援をしており、すでに全米の州の半分以上に提供していると説明しています。

### 2. 公開ソフトの弱点をAIで無料点検

2つ目は「OSS Scanner」です。参加を申し込んだオープンソースの開発チームに対し、Anthropicの最も強力なモデルで定期的に弱点を探し、報告を無料で送ります。報告には、弱点を実際に突く再現手順、説明、直し方の案が付きます。

人の確認を通さずにAIの出力をそのまま送るのが特徴で、そのぶん早く届く代わりに、深刻度の判定違いなどの誤りも含まれうると同社は明記しています。本当に弱点である割合は90%超を見込んでいます。

{{card:https://red.anthropic.com/oss-scanner|OSS Scanner|Anthropic}}

## 背景：見つかる弱点に、直す人手が追いつかない

この計画の出発点は、AIが弱点を見つける力が急に伸びた一方で、それを確かめて直す側の人手が足りないという問題です。Anthropicの研究チームは、OSS Scannerの発表で次のように書いています。

:::quote https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source | Anthropic「Launching an opt-in vulnerability-finding service for open-source software」
> We have discovered over 29,000 candidate vulnerabilities, but have only been able to manually review and triage approximately 6,000 of these.
2万9,000件を超える弱点の候補を見つけたが、人の手で確認し、優先順位を付けられたのは約6,000件にとどまる。
:::

これは過去半年、重要なソフトを同社の最新モデルで調べた結果です。人の確認を待たずに「全部送ってほしい」と求める開発者が増え、未確認の報告をすでに5,000件近く直接送ったといいます。OSS Scannerは、この求めに正式に応える仕組みです。

今回の計画は、限られた企業に強力なモデルを渡して弱点探しをしてきた「Project Glasswing」の経験をもとにしています。Glasswingは今週、より多くの守る側の専門家にモデルを開放する「Cyber Verification Program」に統合されました。AIの攻撃の能力をめぐっては、同社が他社モデルの危険性を測った結果も公表しています（[既報](/news/20260930-anthropic-glm-5-3-cyber-capabilities/)）。

## 反応と論点

OSS Scannerを先行して試した開発者の評価は好意的です。発表によると、暗号処理のソフトを作るwolfSSLは、受け取った74件の報告のうち有効でなかったのは2件だけで、5件は正式な脆弱性として登録されたと答えています。Anthropicが専門家に97件の重大な報告を確認させたところ、85件（88%）が同社の公開基準を満たしました。

それでもAnthropicは、当面は攻撃側が有利だという見方を隠していません。

:::quote https://www.anthropic.com/news/anthropic-cyber-mission | Anthropic「Introducing the Anthropic Cyber Mission」
> Our forecast is that in two years, AI will favor defense: it will be easier to catch bugs before they ship, write fundamentally secure software from scratch, and actively defend systems with models. But in the near term, that may not be true.
2年後にはAIは守る側に有利に働くと予測している。出荷前に不具合を見つけ、最初から安全なソフトを書き、AIで能動的にシステムを守るのが容易になる。だが近い将来はそうではないかもしれない。
:::

実際、10月上旬には韓国の銀行への侵入でAIが使われていたことがわかり、攻撃者が売り先の相談にまでClaudeを使っていたと報告されています（[既報](/news/20261008-crowdstrike-artex-korea-bank-ai-hack/)）。The Vergeも、開発者が弱点を早く知れる利点には引き換えになるものがあると報じています。Anthropic自身も、人の確認を経ない報告には誤りが混じりうると認めています。小さな開発チームには、届く報告の量そのものが負担になりかねません。Anthropicも、人手のある開発チーム向けのサービスだとし、余力のないチームには引き続き人が確認した報告を送るとしています。

## 日本のビジネスへの影響

- **使えるか**: 重要インフラのプログラムは、セキュリティ製品やサービスを提供する会社が参加を申し込む形で、一般の企業が直接使うものではありません。参加企業に日本の日立製作所が入っており、同社は発表の中で、社会インフラを支える制御システムの守りを強める考えを示しています。OSS Scannerは、重要な公開ソフトの中心的な開発者が申し込めます
- **誰にどう効くか**: 電力・ガス・水道・鉄道・工場を持つ企業の経営者や情報システム責任者にとっては、取引のあるセキュリティ会社や機器メーカーが、こうしたAIを使った点検をすでに提供できる状況だという点が重要です
- **今すぐやれること**: 自社の工場や設備の点検を委託している会社に、AIを使った弱点探しに対応しているか、見つかった弱点をどう確かめて直すかを聞いてみてください。自社のサービスで使っている公開ソフトの開発元が、こうした点検に参加しているかも確かめどころです
- **注意点**: AIで見つかる弱点が増えるほど、確かめて直す作業が追いつかなくなります。点検の結果を受け取る前に、誰が確認し、どの順で直すかを決めておかないと、報告の山だけが残ります
