---
{
  "title": "AIで論文が書けすぎて1人月2本までに、世界最大の論文公開サイトarXivが投稿を制限",
  "description": "世界中の研究者が論文を先行公開するarXivが、投稿を1人あたり月2本までに制限した。9月の投稿は過去最多の4万363本で、2年前の約2倍。AIで量産された中身の薄い論文が、ボランティアの審査担当を圧迫しているとしています。",
  "date": "2026-10-11T18:58:00+09:00",
  "category": "research",
  "tags": ["arXiv", "論文", "生成AI", "ハルシネーション", "安全性"],
  "summary": [
    "論文の公開サイトarXivが10月1日から、投稿を1人あたり月2本・審査待ちは同時に3本までに制限した",
    "9月の投稿は過去最多の4万363本で2年前の約2倍、AI分野に限ると2年で6倍超に増えた",
    "AIで量産された中身の薄い論文の確認に人手を取られ、まともな論文の公開が数日〜数週間遅れていた"
  ],
  "sources": [
    {"title": "Fair Moderation, Equitable Access, and AI: arXiv’s Updated Rate Limit Policy", "publisher": "arXiv blog", "url": "https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/", "kind": "公式発表"},
    {"title": "Thomas G. Dietterich の投稿", "publisher": "X @tdietterich", "url": "https://x.com/tdietterich/status/2105751408855450078", "kind": "X投稿"},
    {"title": "Alex Kontorovich の投稿", "publisher": "X @AlexKontorovich", "url": "https://x.com/AlexKontorovich/status/2105851875224334563", "kind": "X投稿"},
    {"title": "Scott Kominers の投稿", "publisher": "X @skominers", "url": "https://x.com/skominers/status/2105792318385050095", "kind": "X投稿"},
    {"title": "arXiv is rate limiting submissions because it can't keep up with AI slop", "publisher": "404 Media", "url": "https://404media.co/arxiv-is-rate-limiting-submissions-because-it-cant-keep-up-with-ai-slop", "kind": "報道"},
    {"title": "arXiv’s new preprint submission cap divides opinion", "publisher": "Times Higher Education", "url": "https://www.timeshighereducation.com/node/745300", "kind": "報道"},
    {"title": "ArXiv caps submissions at two per month as AI paper flood overwhelms the preprint server", "publisher": "The Decoder", "url": "https://the-decoder.com/arxiv-caps-submissions-at-two-per-month-as-ai-paper-flood-overwhelms-the-preprint-server/", "kind": "報道"}
  ],
  "thumb_prompt": "A small library return slot with a turnstile-style counter showing two slots, while an enormous avalanche of identical paper manuscripts piles up outside the door, a single tidy manuscript passing through.",
  "thumb_style": "3d",
  "thumb_text": "arXiv 月2本まで",
  "share_text": "AIで論文が量産されすぎて、論文公開サイトarXivが1人月2本までに。9月は過去最多の4万本",
  "editor_note": ""
}
---
世界中の研究者が論文を無料で先行公開するサイト「arXiv（アーカイブ）」は、現地時間10月1日から、投稿を1人あたり月2本までに制限しました。9月の投稿は過去最多の4万363本で、2年前の約2倍。AIで手軽に書かれた中身の薄い論文が増え、内容を確かめるボランティアの手が追いつかなくなったためです。

## 何が決まったか

arXivとは、学会誌の審査（査読）を通る前の論文を誰でも公開・閲覧できる、物理学・数学・計算機科学などの論文公開サイトです。OpenAIやGoogleなどが新しいAIの技術を発表するときにも、論文はまずここに載ることが多く、AI業界の「掲示板」の役割を担っています。

新しいルールの中身は次のとおりです。

- 投稿できるのは1人あたり**暦の月ごとに2本まで**。分野を問わず全カテゴリーに適用
- 審査待ちなどで処理中の投稿は、これまでどおり**同時に3本まで**（2024年からの上限）
- **却下された投稿も2本に数える**。審査担当の時間を使うのは「投稿」だからという理由
- 数えるのは投稿手続きをした人だけで、**共著者の枠は減らない**
- 公開前に自分で取り下げた投稿は数えない

:::quote https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/ | arXiv公式ブログ「Fair Moderation, Equitable Access, and AI」
> arXiv now limits submitters to up to two submissions per calendar month, with a limit of three total active submissions at any given time.
arXivは、投稿者1人あたりの投稿を暦の月ごとに最大2本、処理中の投稿は常に合計3本までに制限します。
:::

arXivはこの制限を、AIを使う研究者の新しい作法を決め、審査の道具と手順を改善するまでの「つなぎ（stopgap）」と位置づけています。影響を見ながら必要に応じて見直すとしています。

## 何が問題になっているのか

制限の対象はAIそのものではありません。arXivは、AIを使ったと明記し、研究として新しい価値があれば、AIを道具にした論文も受け付けています。困っているのは、1つの研究を細かく切り分けて本数を稼ぐ「サラミ論文」や、範囲がごく狭い「薄い論文」、AIが書いた文字ばかり多い論文が一気に増えたことです。

こうした論文をはじくのは、無償で協力するボランティアの審査担当です。編集諮問委員会のトーマス・ディータリック委員長は、負担を生んでいるのは一部の著者だと説明しています。

:::quote https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/ | arXiv公式ブログ（編集諮問委員会のトーマス・ディータリック委員長の言葉）
> However, a relatively small proportion of authors are submitting a large number of low-quality papers and consuming a disproportionate fraction of the moderators’ time. This is unfair to authors who continue to submit quality papers — their papers can be delayed for days or weeks as a result.
しかし、比較的少数の著者が質の低い論文を大量に投稿し、審査担当の時間を不釣り合いに多く使っています。これは質の高い論文を投稿し続けている著者にとって不公平で、その論文の公開が数日から数週間遅れることもあります。
:::

## 数字で見る「論文の洪水」

9月ひと月の投稿数を公式ブログの数字で並べると、10年で4倍に増えています。

| 時期 | 9月の投稿数 |
|---|---|
| 2016年 | 9,869本 |
| 2024年 | 2万569本 |
| 2026年 | 4万363本（過去最多） |

伸びがいちばん大きいのはAI分野（cs.AI）で、2年で6倍を超えました。ほかの分野も同じ2年で2倍です。今年9月の投稿だけで、スタッフと審査担当への問い合わせが約9,000件寄せられました。

## これまでの締め付け

arXivがAI由来の投稿に手を打つのは初めてではありません。404 Mediaなどの報道によると、昨年11月には計算機科学分野の総説や意見論文の受け付けを、査読を通ったものに限定しました。今年5月には、AIが作った架空の参考文献のような、確かめていないAIの出力をそのまま含む論文を出した著者を1年間投稿禁止にする方針を打ち出したと報じられています。

The Decoderは、arXivが今年7月にコーネル大学から独立した非営利団体になり、9月に複数の財団などから3〜5年で計1,720万ドルの資金を得て、AIが生成した投稿への対策にも充てると報じています。

## 反応と論点

ディータリック氏は発表当日、Xで研究者に向けて新しい上限を告知し、投稿数が指数関数的に増えていることを理由に挙げました。

賛成の声として、米ラトガース大学の数学者アレックス・コントロビッチ氏は「今月あなたが出す42本は読まない。いちばん良い2本を選んで」とXに投稿しています。

{{x:https://x.com/AlexKontorovich/status/2105851875224334563}}

一方、ハーバード・ビジネス・スクールで市場設計を研究するスコット・コミナーズ氏は、Xで「節約すべきは審査の手間であって、学問ではない」と反対しました。審査を通りやすい論文を選ぶことと、科学的に価値のある論文を選ぶことは別だという指摘です。

{{x:https://x.com/skominers/status/2105792318385050095}}

ルールの作りにも論点があります。数えるのは投稿手続きをした人だけなので、人数の多い研究室は手続きをする人を分ければ多くの論文を出せます。一人で研究する人ほど、月2本の枠がそのまま上限になる仕組みです。

## 日本のビジネスへの影響

- **使えるか**: 制限は日本の研究者・企業の研究部門にも一律に適用されています。論文を読む側には変化はなく、これまでどおり無料で読めます
- **誰にどう効くか**: 企業の研究開発部門は、学会の締め切り前に論文をまとめて出す計画を見直す必要があります。共著者の枠は減らないので、投稿の手続きをする人を分ける運用が現実的です。AI製品を選ぶ担当者や広報にとっては、「arXivに論文あり」は査読済みの証明ではないという前提が、これまで以上に大事になります
- **今すぐやれること**: 社内の資料や提案書でarXivの論文を根拠に引いているなら、学会で採択されたものか、著者がどこの所属かを1本ずつ確かめておきましょう。AIで論文や資料を調べるときの注意点は、[調べもの・リサーチAIのガイド](/best/research/)にもまとめています
- **注意点**: arXiv自身が「つなぎ」と言うとおり、上限はこの先変わる可能性があります。却下された投稿も枠を使うので、AIで下書きした論文を急いで出すと、その月の公開機会を失うおそれがあります

AIによる「質の低い成果物の洪水」は、論文に限りません。オープンソースのバグ報奨金でも、AIが作った無効な報告の急増で受け付けが止まった例があります（[Googleがオープンソースのバグ報奨金を一時停止](/news/20261005-google-oss-vrp-pause-ai-reports/)）。
