---
{
  "title": "天文学者がClaudeで夜空全体の紫外線地図を初めて完成、「後回しの仕事」をAIの作業チームに",
  "description": "米ジョンズ・ホプキンス大の天文学者が、Anthropicの研究者向けアプリ「Claude Science」で空全体の紫外線の地図を初めて完成させた。観測されていない3分の1は他の波長から推定し、試験では実測との差が約10%だった。",
  "date": "2026-10-09T20:00:00+09:00",
  "category": "usecases",
  "tags": ["Claude Science", "Claude", "Anthropic", "活用事例", "天文学", "エージェント"],
  "summary": [
    "米ジョンズ・ホプキンス大の天文学者ブライス・メナール氏が、AnthropicのClaude Scienceを使い、空全体の紫外線の地図を初めて完成させた",
    "人工衛星が撮った3万8,000枚の観測をAIの作業チームが集めて整え、まだ誰も観測していない空の約3分の1は他の光の観測から推定した",
    "推定の精度は、答えを隠した試験で実測との差が約10%。数週間かかる地道な作業のため、天文学者が後回しにしてきた仕事だった"
  ],
  "sources": [
    {"title": "Using Claude Science to produce the first complete map of the sky in UV light", "publisher": "Anthropic", "url": "https://www.anthropic.com/research/the-missing-map-of-the-sky", "kind": "公式発表"},
    {"title": "Claude Science", "publisher": "Anthropic", "url": "https://claude.com/product/claude-science", "kind": "公式ドキュメント"},
    {"title": "Anthropic's Claude Science creates the first complete ultraviolet map of the sky", "publisher": "The Decoder", "url": "https://the-decoder.com/anthropics-claude-science-creates-the-first-complete-ultraviolet-map-of-the-sky/", "kind": "報道"}
  ],
  "thumb_text": "Claude Science",
  "share_text": "天文学者がClaude Scienceで空全体の紫外線地図を初めて完成。誰も観測していない3分の1はAIが推定",
  "thumb_style": "3d",
  "thumb_prompt": "A glowing violet map of the whole night sky unrolled like a giant scroll across a classroom floor, with one third of it still being painted in by tiny robotic arms, a small telescope standing beside it.",
  "editor_note": ""
}
---
米ジョンズ・ホプキンス大学の天文学者ブライス・メナール氏が、Anthropicの研究者向けアプリ「Claude Science」を使って、空全体を紫外線で見た地図を初めて完成させました。現地時間10月8日にAnthropicのサイトで本人が作り方を公開しています。これまで誰も紫外線で観測していなかった空の約3分の1は、AIが他の光の観測データから推定して埋めました。

## 何ができたか

完成したのは、天の川の中心を真ん中に置いた、空全体の紫外線の画像です。紫外線で見ると、若い星のまわりの雲や、星の爆発が残したリング状のちりなど、星の光に照らされたちりの姿が浮かび上がります。全体の約3分の1は観測ではなくAIの推定で、地図の点ごとに「実測」か「推定」かの印と、推定の確からしさが付いています。

使い道としてまず想定しているのは大学の授業です。空の姿を波長ごとに見比べさせる授業で、メナール氏はこれまで紫外線だけは穴の空いた地図しか見せられなかったといいます。

## なぜこれまで無かったのか

紫外線は地球のオゾン層に吸収されるため、宇宙の望遠鏡でしか観測できません。中心となるのはNASAの衛星GALEX（2003〜2013年に運用）のデータですが、写せたのは空の約3分の2にとどまります。明るい星が密集する天の川の中心部は、機器が壊れるおそれがあるため、わざと避けていたからです。

欠けた部分を統計的に埋める方法自体はありました。足りなかったのは人手です。きちんとやれば画素単位の補正と分析の繰り返しで数週間かかり、研究の本筋ではないため、天文学者は後回しにしがちだったとメナール氏は説明しています。

今回使ったClaude Scienceは、Anthropicが研究者向けに出しているアプリです。Claudeのモデルに、データ分析や60以上の科学データベースとの接続、計算機の管理といった機能を足したもので、いまはベータ版としてClaudeのPro・Max・Team・Enterpriseの各プランで使えます。

{{card:https://claude.com/product/claude-science|Claude Science|Anthropic}}

## AIの作業チームの進め方

メナール氏の指示は、「手に入る紫外線の観測データをすべて集め、基準をそろえて1枚にまとめ、観測されていない部分も埋める」というものでした。Claudeはこれを複数のAIの作業役（エージェント）に割り振りました。工程ごとに整理すると次のようになります。

| 工程 | AIがしたこと | 使ったデータ |
|---|---|---|
| 集める | 公開されている紫外線の観測をネットで探してダウンロード | GALEX（3万8,000回分の観測）、NASAのSwift、韓国のFIMS/SPEAR、欧州のTD-1など |
| そろえる | 明るい星のまわりの「まぶしさ」を除き、時期や機器の違うデータを比べられるよう補正。空の区画ごとに多くのエージェントが並行して処理 | 上記の紫外線データ |
| 埋める | 紫外線と他の光の明るさの関係を観測済みの3分の2で学び、観測のない3分の1に当てはめる | 可視光・赤外線・電波の観測 |
| 星を足す | 1億個を超える星の紫外線の明るさを推定して重ねる | 欧州宇宙機関の衛星Gaiaの可視光の観測 |

「埋める」工程で使ったのは、欠けた部分を周囲から推定する「インペインティング」という手法です。古い写真の傷や欠けを直す技術と同じ考え方です。

精度の確認には、答えのある問題を解かせる方法を使いました。実測がある領域の一部を伏せてAIに埋めさせ、本物と比べたところ、数回の改良を経て差は約10%に収まりました。メナール氏は、目ではほとんど区別できない差だとしています。

人の役割は主に方針を決めることでした。メナール氏がClaudeと次の手順を相談すると、あとはClaudeが何時間も計算を続け、その間、本人は別の研究に戻っていたといいます。作業は数日に及び、地図は10回以上作り直されています。

## AIが見落とした失敗もあった

すべてをAIに任せられたわけではありません。暗い領域の画像に、うっすらとした円い模様が並んでいたのを見つけたのはメナール氏本人でした。GALEXが1回の観測で写す円形の範囲ごとに、地球の大気のかすかな光が消し切れずに残っていたのが原因です。

:::quote https://www.anthropic.com/research/the-missing-map-of-the-sky | Anthropic「Using Claude Science to produce the first complete map of the sky in UV light」
> Claude had listed this as a known issue at the start of the project, but the map had still passed two rounds of review by other agents without the problem being caught.
Claudeは作業の最初にこれを既知の問題として挙げていたが、それでも地図は他のエージェントによる2回の確認を、問題が見つからないまま通っていた。
:::

指摘を受けたエージェントが原因をたどり、3万8,000回分の観測すべてを補正し直すと、数時間の処理で模様は消えました。AIに任せた作業でも、最後に人が目で確かめる工程が欠かせなかったことがわかります。

## 「後回しの仕事」をAIで片付ける

メナール氏は、今回は研究の時間を削らずにこの地図作りを終えられたとしたうえで、同じような仕事はほかの分野にもあるはずだと書いています。

:::quote https://www.anthropic.com/research/the-missing-map-of-the-sky | Anthropic「Using Claude Science to produce the first complete map of the sky in UV light」
> I suspect many scientists can think of a map, a figure, or a resource they’ve been putting off for the same reason.
同じ理由で後回しにしてきた地図や図、資料が、多くの科学者に思い当たるのではないかと思う。
:::

なお、メナール氏はジョンズ・ホプキンス大学の教員であると同時にAnthropicの研究者でもあり、記事は同社のサイトに載ったものです。観測のない3分の1は、試験で精度を確かめたとはいえ推定であり、実際の観測で確かめられたわけではありません。地図に「推定」の印が付いているのはそのためです。

AIを研究の道具に使う例は増えています。ハーバード大の教授がClaude Codeを使い、3カ月で論文原稿36本を書き上げた例もあります（[Claude Codeで3カ月に論文原稿36本、ハーバード大教授が科学計算の道具を無料公開](/news/20261004-bootloops-claude-shaped-science/)）。

## 日本のビジネスへの影響

- **使えるか**: Claude Scienceは、ClaudeのPro・Max・Team・Enterpriseのいずれかのプランで使えるベータ版です（MacとWindows、Linuxのアプリ）。公式ページに提供地域の制限は書かれていません。TeamとEnterpriseでは管理者が有効にする必要があります。大学や非営利の研究機関の研究者向けには割引のプランも用意されています。
- **誰にどう効くか**: 大学や企業の研究開発部門の研究者のほか、公開データを集めて1つの資料にまとめる仕事をする調査・分析担当にも参考になります。複数の統計データをそろえて1枚の地図や表にする、といった「誰かがやるべきだが優先度が低い」作業が向いています。
- **今すぐやれること**: 部署で後回しになっている資料作りやデータ整理を1つ選び、指示を「集める・そろえる・まとめる・欠けを埋める」の段階に分けてAIに渡してみてください。今回のように、答えのわかっている部分を隠して当てさせると、AIの推定がどこまで信用できるかを確かめられます。
- **注意点**: AI同士の確認では見落としが起きました。最終成果物は人が目で確かめる工程を必ず入れてください。また、推定で埋めた部分は推定だと明記して使うことが大切です。調べもの向けのAIの選び方は[用途別AIガイドの「調べもの・リサーチ」](/best/research/)にまとめています。
