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

## 何を作ったか

Sophosは、世界の62万5,000以上の組織を守っているセキュリティ会社です。顧客企業のパソコンやネットワークを24時間見張り、怪しい動きがあれば調べて対処する「MDR（Managed Detection and Response、監視と対応の代行）」というサービスを提供しています。

このサービスに入ってくるデータは膨大です。Sophos自身の製品に加え、500以上の他社製品とつながった監視の仕組みが毎日何兆件もの記録を生み、Sophosはそれを1日あたり1,000〜2,000件の「調べるべき案件」に絞り込んで、世界9カ所の監視拠点で処理しています。

この案件の処理に、OpenAIのサイバー防御プログラム「Daybreak」を使って作ったAIを入れました。Daybreakとは、OpenAIの高性能なモデルと、プログラムを書いたり点検したりする道具「Codex」、セキュリティ向けの機能をひとまとめにし、守る側の企業に提供する枠組みです。Sophosは6月にこのプログラムの協業先に加わったと発表していました。

## どう動くか

OpenAIの事例紹介によると、仕組みは3つの役割に分かれています。

1. **調査役のAI**: 案件ごとに、顧客の環境、検知された内容、攻撃の痕跡、関連する脅威情報を集める
2. **計画役のAI**: 集めた材料から調査の計画を立てて実行し、結果を点検する。最後に、取るべき対応の提案付きで要約を作り、分析担当者に渡す
3. **対応役のAI**: 対応の一部を実際に実行する

Sophosのジョン・ピーターソン最高技術責任者（CTO）は、成果を次のように語っています。

:::quote https://openai.com/index/sophos/ | OpenAI「Sophos cuts threat investigation time by 96% with OpenAI Daybreak」
> Now, because of the agents we’ve been able to build through the Daybreak programme, the average response time for cases using those agents has fallen to about 89 seconds.
Daybreakのプログラムを通じて作ったAIエージェントのおかげで、それを使う案件の平均対応時間は約89秒まで下がった。
:::

導入前の平均約38分という数字も、ピーターソン氏によればプロの監視拠点の96%より速い水準でした。そこからさらに縮めたことになります。

## 人の判断をどこに残したか

この事例でいちばん参考になるのは、AIに任せる範囲の決め方です。Sophosの監視サービスには、顧客が選べる3つのモードがあります。

| モード | Sophosがやること | 最終的に手を動かすのは |
|---|---|---|
| 通知 | 調査して対応を提案する | 顧客 |
| 協働 | 対応の前に顧客と相談する | 両者で合意してから |
| 一任 | 顧客の代わりに直接対応する | Sophos |

OpenAIの紹介文によると、この境界は作業をするのが人でもAIでも同じです。システムを止めたり消したりするような影響の大きい操作には、必ず相応の人の確認が入ります。ピーターソン氏は「AIに任せるのが不安なものは、すべて人の判断に回している」と話しています。

52%という数字も「Sophosの分析担当者が決めた範囲の中で」AIが最後まで処理した割合です。残りの案件は、AIがまとめた材料をもとに人が判断します。

## 何を得たか

OpenAIが挙げる成果は、対応時間の短縮と自動化の割合のほかに、顧客への調査の速さと品質がそろうこと、なり手の少ないセキュリティ人材を同じだけ増やさずに、計算資源を増やすことで規模を広げられることです。分析担当者は、例外的な案件や重要な判断に時間を回せるようになったとしています。

一方、ピーターソン氏は他社のセキュリティ責任者への助言として、AIより先に基本を固めることを挙げています。修正プログラムの適用、多要素認証（パスワードに加えてスマートフォンなどで本人確認する仕組み）、ネットワークの分割などを重ねる守り方です。修正プログラムで防げるのは製品の作り手が知っている弱点だけで、弱点が見つかり悪用される速さはかつてない規模になっている、というのが理由です。

{{card:https://openai.com/daybreak/|Daybreak（OpenAIのサイバー防御プログラム）|OpenAI}}

## 日本のビジネスへの影響

- **使えるか**: DaybreakはOpenAIが企業や協業先に向けて提供する枠組みで、日本企業が個別に使えるかは公式ページに地域の記載がありません。現実的には、Sophosのような監視代行サービスを通じて、こうしたAIの恩恵を受ける形になります。OpenAIは、自治体、重要インフラの事業者、地域の金融機関、非営利団体などに、6カ月で10億ドル分の利用補助を用意し、申し込みを受け付けています
- **誰に効くか**: 情報システム部門の責任者と、セキュリティの監視を外部に任せている会社の経営者です。委託先がAIをどう使い、どこで人が判断しているかは、契約の更新時に確かめるべき項目になります
- **今すぐやれること**: 自社の監視の委託先に、AIが自動で対応してよい範囲を「通知だけ」「相談してから」「任せる」のどれにしているかを聞いてください。Sophosの3段階は、そのまま社内の線引きの叩き台に使えます。AIの導入より前に、修正プログラムの適用と多要素認証の徹底を確認するのが先です
- **注意点**: 38分から89秒という数字は、AIを使った案件の平均です。全案件が89秒で終わるわけではありません。攻撃側も同じようにAIを使い始めていることは[韓国の銀行への攻撃の記事](/news/20261008-crowdstrike-artex-korea-bank-ai-hack/)でも伝えています。社内でAIエージェントを動かすときの安全面の考え方は、Anthropicが電力や水道の事業者と進める[防衛計画の記事](/news/20261009-anthropic-cyber-mission-infrastructure/)も参考になります
