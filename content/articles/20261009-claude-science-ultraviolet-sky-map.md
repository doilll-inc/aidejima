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

## 何を作ったか

紫外線で空を見ると、若い星のまわりの雲や、星の爆発が残したリング状のちりなど、星の光に照らされたちりの姿が浮かび上がります。ただ、紫外線は地球のオゾン層に吸収されるため、宇宙の望遠鏡でしか観測できません。最大の観測データを持つNASAの衛星GALEX（2003〜2013年に運用）でも、写せたのは空の約3分の2です。明るい星が多い天の川の中心部は、機器が壊れるおそれがあるため、わざと避けていました。

メナール氏は、大学の授業で空の姿を波長ごとに見せるとき、紫外線だけは「穴だらけの地図」しか見せられなかったと書いています。今回の地図はまず学生向けの教材として使う想定です。

Claude Scienceとは、Anthropicが研究者向けに出しているアプリで、Claudeのモデルにデータ分析や60以上の科学データベースとの接続、計算機の管理といった機能を足したものです。いまはベータ版で、ClaudeのPro・Max・Team・Enterpriseの各プランで使えます。

{{card:https://claude.com/product/claude-science|Claude Science|Anthropic}}

## どう作ったか

メナール氏がClaudeに出した指示は、「手に入る紫外線の観測データをすべて集め、基準をそろえて1枚にまとめ、観測されていない部分も埋める」というものでした。作業はClaudeが複数のAIの作業役（エージェント）に割り振り、次の順に進めています。

1. **集める**: 公開されている紫外線の観測データをネットで探してダウンロードする。GALEXのほか、NASAのSwift、韓国のFIMS/SPEAR、欧州のTD-1などの観測を使った
2. **そろえる**: 明るい星のまわりの「まぶしさ」を取り除き、時期や機器の違うデータを比べられるように補正する。空の区画ごとに多くのエージェントが並行して処理した
3. **埋める**: 紫外線で観測済みの3分の2を使って、紫外線の明るさと、可視光・赤外線・電波の観測との関係をAIに学ばせ、観測のない3分の1に当てはめる。欠けた部分を周囲から推定する「インペインティング」という手法で、写真の傷を直す技術と同じ考え方
4. **星を足す**: 欧州宇宙機関の衛星Gaiaの可視光の観測から、1億個を超える星の紫外線の明るさを推定して重ねる

推定の精度は、答えがわかっている場所の一部をわざと隠し、AIに埋めさせて確かめました。何度か改良した結果、実測との差は約10%で、目ではほとんど見分けられない程度だったとしています。地図には、点ごとに「実測」か「推定」かの区別と、推定の確からしさも付けています。

作業は数日にわたり、地図は10回以上作り直されました。メナール氏がClaudeと次の手順を相談し、その後はClaudeが何時間も計算を続け、その間に本人は別の研究を進めるという進め方だったといいます。

## AIが見落とした失敗もあった

完成までには、人が気づいて直した問題もありました。ある晩、メナール氏が暗い領域の画像を見ていると、うっすらと円い模様が並んでいるのに気づきました。GALEXの1回ごとの観測の跡で、地球の大気がわずかに光る影響を消し切れていなかったのが原因です。

:::quote https://www.anthropic.com/research/the-missing-map-of-the-sky | Anthropic「Using Claude Science to produce the first complete map of the sky in UV light」
> Claude had listed this as a known issue at the start of the project, but the map had still passed two rounds of review by other agents without the problem being caught.
Claudeは作業の最初にこれを既知の問題として挙げていたが、それでも地図は他のエージェントによる2回の確認を、問題が見つからないまま通っていた。
:::

メナール氏が指摘すると、エージェントが原因をたどり、3万8,000回分の観測すべてを補正しました。処理は数時間で終わり、円い模様は消えたといいます。AIに任せた作業でも、最後に人が目で確かめる工程が欠かせなかったことがわかります。

## 「後回しの仕事」をAIで片付ける

メナール氏は、この種の地図作りがこれまで手つかずだった理由を、手間の大きさに求めています。きちんとやれば画素単位の補正と分析の繰り返しで数週間かかり、研究の本筋ではないため誰もやりたがらないというわけです。

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
