---
{
  "title": "サイバー攻撃の調査が38分から89秒に、英SophosがOpenAIのAIで対応の半分を自動化",
  "description": "セキュリティ大手の英Sophosが、OpenAIのサイバー防御プログラム「Daybreak」でAIの調査役を作り、1件あたり平均38分かかっていた攻撃の調査と対応を約89秒に短縮した。全案件の52%はAIが最後まで処理している。",
  "date": "2026-10-10T01:30:00+09:00",
  "category": "usecases",
  "tags": ["Sophos", "OpenAI Daybreak", "OpenAI", "活用事例", "導入事例", "セキュリティ"],
  "summary": [
    "英国のセキュリティ大手Sophosは、OpenAIのAIで作った調査役のAIにより、攻撃の疑いがある案件の対応時間を平均約38分から約89秒に縮めた",
    "Sophosが監視を請け負う案件のうち52%は、人が決めた範囲の中でAIが調査から対応まで最後までこなしている",
    "システムを止めるような影響の大きい操作は人が判断する仕組みを残しており、AIに任せる範囲を顧客ごとに3段階で選べる"
  ],
  "sources": [
    {"title": "Sophos cuts threat investigation time by 96% with OpenAI Daybreak", "publisher": "OpenAI", "url": "https://openai.com/index/sophos/", "kind": "公式発表"},
    {"title": "Daybreak | OpenAI for cybersecurity", "publisher": "OpenAI", "url": "https://openai.com/daybreak/", "kind": "公式発表"},
    {"title": "Sophos Joins the OpenAI Daybreak Cyber Partner Program to Strengthen Customer Defense with Frontier AI", "publisher": "Sophos", "url": "https://www.sophos.com/en-us/press/press-releases/2026/06/sophos-joins-the-openai", "kind": "公式サイト"}
  ],
  "thumb_text": "38分→89秒",
  "thumb_style": "3d",
  "thumb_prompt": "A security operations room shown as a 3D scene where a huge hourglass has been replaced by a tiny stopwatch on the desk, while a small friendly robot hands a neat one-page report to a human analyst seen from behind.",
  "share_text": "サイバー攻撃の調査が平均38分から89秒に。英SophosがOpenAIのAIで調査役を作り、案件の52%を自動処理",
  "editor_note": ""
}
---
英国のセキュリティ大手Sophosは、OpenAIのAIで作った「調査役のAI」を使い、攻撃の疑いがある案件1件の調査と対応にかかる時間を平均約38分から約89秒に縮めました。OpenAIが現地時間10月9日に導入事例として公開したもので、Sophosが扱う案件の52%は、すでにAIが調査から対応まで最後まで処理しています。

## 数字で見る効果

成果の中心は、AIを使った案件の平均対応時間です。

| 項目 | 数字 |
|---|---|
| AIを使った案件の平均対応時間 | 約38分 → 約89秒 |
| AIが調査から対応まで終えた案件 | 監視サービスの案件の52% |
| 1日に調べる案件 | 約1,000〜2,000件 |
| 案件を処理する監視拠点 | 世界9カ所 |

もとの約38分も遅かったわけではありません。ピーターソン最高技術責任者（CTO）は、プロの監視拠点の96%を上回る速さだったと説明しています。その水準から、AIを使う案件ではさらに短くなりました。

:::quote https://openai.com/index/sophos/ | OpenAI「Sophos cuts threat investigation time by 96% with OpenAI Daybreak」
> Now, because of the agents we’ve been able to build through the Daybreak programme, the average response time for cases using those agents has fallen to about 89 seconds.
Daybreakのプログラムを通じて作ったAIエージェントのおかげで、それを使う案件の平均対応時間は約89秒まで下がった。
:::

時間のほかにOpenAIが挙げるのは、顧客ごとに調査の速さと質がばらつきにくくなる点と、採用の難しいセキュリティ人材の数ではなく計算資源で処理量を伸ばせる点です。人の分析担当者は、例外的な案件や重い判断に集中できるとしています。

## AIに任せる範囲の線引き

この事例で参考になるのは、速さよりも線引きのほうです。Sophosの監視サービスでは、顧客が次の3つから任せ方を選びます。

| モード | Sophosがやること | 最終的に手を動かすのは |
|---|---|---|
| 通知 | 調査して対応を提案する | 顧客 |
| 協働 | 対応の前に顧客と相談する | 両者で合意してから |
| 一任 | 顧客の代わりに直接対応する | Sophos |

作業するのが人かAIかで、この線は変わりません。システムを止める、データを消すといった取り返しのつきにくい操作には、人の確認を必ず挟みます。ピーターソン氏は「AIに任せるのが不安なものは、すべて人の判断に回している」と話しています。

先の52%も、Sophosの分析担当者があらかじめ決めた範囲の内側でAIが処理しきった割合です。それ以外の案件では、AIがそろえた材料を見て人が判断します。

## 仕組みと背景

Sophosは、62万5,000を超える組織を守る英国のセキュリティ会社です。顧客のパソコンやネットワークを24時間見張り、怪しい動きを調べて対処する「MDR（Managed Detection and Response、監視と対応の代行）」を提供しています。自社製品と500を超える他社製品から集まる記録は1日に何兆件にもなり、それを調べるべき案件に絞り込んでいます。

今回のAIは、OpenAIのサイバー防御プログラム「Daybreak」で作られました。Daybreakは、OpenAIの高性能なモデル、プログラムを書いたり点検したりする道具「Codex」、セキュリティ向けの機能を、守る側の企業にまとめて提供する枠組みです。Sophosは6月にこのプログラムの協業先に加わったと発表していました。

案件の処理は、AIの分業で進みます。まず1つのAIが、顧客の環境、検知の内容、攻撃の痕跡、関連する脅威情報を案件ごとに集めます。別のAIがその材料で調査の計画を立てて実行・点検し、対応案を添えた要約を分析担当者に渡します。対応の一部は、さらに別のAIが実際に実行します。

{{card:https://openai.com/daybreak/|Daybreak（OpenAIのサイバー防御プログラム）|OpenAI}}

## 日本のビジネスへの影響

- **使えるか**: DaybreakはOpenAIが企業や協業先に向けて提供する枠組みで、日本企業が個別に使えるかは公式ページに地域の記載がありません。現実的には、Sophosのような監視代行サービスを通じて、こうしたAIの恩恵を受ける形になります。OpenAIは、自治体、重要インフラの事業者、地域の金融機関、非営利団体などに、6カ月で10億ドル分の利用補助を用意し、申し込みを受け付けています
- **誰に効くか**: 情報システム部門の責任者と、セキュリティの監視を外部に任せている会社の経営者です。委託先がAIをどう使い、どこで人が判断しているかは、契約の更新時に確かめるべき項目になります
- **今すぐやれること**: 自社の監視の委託先に、AIが自動で対応してよい範囲を「通知だけ」「相談してから」「任せる」のどれにしているかを聞いてください。Sophosの3段階は、そのまま社内の線引きの叩き台に使えます。ただし、ピーターソン氏が他社の責任者にまず勧めるのはAIではなく基本の徹底です。修正プログラムで防げるのは作り手が把握している弱点に限られ、弱点が見つかって悪用される速さも増しているため、修正プログラムの適用、多要素認証（パスワードに加えてスマートフォンなどで本人確認する仕組み）、ネットワークの分割を重ねる守り方を先に確かめてください
- **注意点**: 38分から89秒という数字は、AIを使った案件の平均です。全案件が89秒で終わるわけではありません。攻撃側も同じようにAIを使い始めていることは[韓国の銀行への攻撃の記事](/news/20261008-crowdstrike-artex-korea-bank-ai-hack/)でも伝えています。社内でAIエージェントを動かすときの安全面の考え方は、Anthropicが電力や水道の事業者と進める[防衛計画の記事](/news/20261009-anthropic-cyber-mission-infrastructure/)も参考になります
