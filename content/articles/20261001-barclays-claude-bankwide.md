---
{
  "title": "英BarclaysがClaudeを全行に拡大、行員1.6万人が利用しメールは1日12万通を仕分け",
  "description": "英大手銀行BarclaysがAnthropicのClaudeを全行に広げる。行員向けの検索アシスタントは1万6,000人以上が使い、市場部門では1日約12万通のメールを分類。Claude Codeは2026年末に開発者の50%へ広げる計画だ。",
  "date": "2026-10-01T17:46:00+09:00",
  "updated": "2026-10-01T18:53:00+09:00",
  "category": "usecases",
  "tags": ["Barclays", "Claude", "Anthropic", "金融", "導入事例", "活用事例"],
  "summary": [
    "英大手銀行BarclaysはAnthropicとの提携を広げ、Claudeを開発・業務・顧客対応に全行で使う",
    "行員向けの社内検索アシスタントは2025年から稼働し、1万6,000人以上が使って検索は100万回を超えた",
    "市場部門ではClaudeが1日約12万通のメールを仕分け、Claude Codeは2026年末に開発者の50%へ広げる"
  ],
  "sources": [
    {"title": "Barclays scales Claude to upgrade operations and improve client experience", "publisher": "Anthropic", "url": "https://www.anthropic.com/news/barclays-scales-claude", "kind": "公式発表"},
    {"title": "Claude Code", "publisher": "Anthropic（Claude）", "url": "https://claude.com/product/claude-code", "kind": "公式発表"},
    {"title": "Financial services | Claude by Anthropic", "publisher": "Anthropic（Claude）", "url": "https://claude.com/solutions/financial-services", "kind": "公式発表"}
  ],
  "thumb_text": "Barclays×Claude",
  "share_text": "英BarclaysがClaudeを全行に拡大。行員1.6万人が社内検索に使い、市場部門のメールは1日12万通をAIが仕分け",
  "editor_note": ""
}
---
英国の大手銀行Barclaysが、AnthropicのAI「Claude」を全行の業務に広げると、Anthropicが現地時間10月1日に公式ブログで発表しました。顧客対応を支える行員向けの検索アシスタントはすでに1万6,000人以上が使い、市場部門ではClaudeが1日約12万通のメールを仕分けています。開発者向けのClaude Codeは、2026年末までに開発者の50%に広げる計画です。

## 何に使っているか

Barclaysは、個人向けの預金や融資から投資銀行業務までを1社で手がける英国のユニバーサルバンクです。発表で利用規模の数字が示されたのは、顧客対応の裏方、市場部門の事務、ソフトウェア開発の3つの現場です。

| 現場 | Claudeの役割 | 公表された数字 |
|---|---|---|
| Barclays UKの顧客対応 | 行員向けの社内検索「Colleague Knowledge Assistant」 | 2025年から稼働、利用者1万6,000人以上、検索100万回超 |
| 市場部門（Global Markets） | 顧客からの問い合わせメールの仕分け | 1日約12万通 |
| ソフトウェア開発 | コーディングエージェント「Claude Code」 | 2026年末に開発者の50%、2027年にエンジニアの過半数（計画） |

### 顧客対応：行員が答えを探す時間を縮める

Colleague Knowledge Assistantは、英国の個人顧客2,000万人超を抱えるBarclays UKの行員が、顧客に答えるための情報を探す社内ツールです。仕組みについて、Anthropicは次のように書いています。

:::quote https://www.anthropic.com/news/barclays-scales-claude | Anthropic公式ブログ「Barclays scales Claude to upgrade operations and improve client experience」
> The capability, which has been live since 2025, is powered by Claude through a retrieval-augmented generation architecture. More than 16,000 colleagues have adopted the assistant, and it has handled over one million searches.
この機能は2025年から稼働しており、Claudeが検索拡張生成（RAG）の構成で動いています。1万6,000人以上の行員が使い、検索は100万回を超えました。
:::

RAGとは、AIが答える前に社内文書を検索し、見つけた資料をもとに回答を作る方式です。AIが学習していない社内規程や商品の細かな条件にも答えられます。

### 市場部門：メールを担当に渡すまでの下ごしらえ

市場部門に届く顧客からの問い合わせメールは1日約12万通にのぼります。ここでClaudeが受け持つのは、メールの種類の判定、足りない情報の補完、どの処理の流れに回すかの判断までです。依頼に処理に必要な情報がそろっているかも確かめ、実際に処理する事務担当の行員がすぐ動けるようにします。Anthropicは、これで手作業が減ったとしています。

### 開発：Claude Codeを段階的に全社へ

開発部門では、古いシステムの刷新やソフトウェアの品質向上にClaudeを使います。Claude Codeはコードを書いて動かすAIエージェントで、Barclaysは利用者を2026年末に開発者の半数、2027年にはソフトウェアエンジニアの過半数まで広げる見込みです。

## どう進めているか

3つの用途に共通するのは、AIは探す・分ける・下準備をする役で、最後に判断して動くのは行員だという分担です。規制の厳しい銀行で使う前提として、Barclaysは用途ごとにガバナンスとセキュリティ管理をかけ、人による監督のもとで展開しているといいます。

発表の中で、グループ共同COO（最高執行責任者）の2人が狙いを説明しています。Anne Marie Darling氏は、定型作業の時間を減らし意思決定を簡素にして、行員が専門性を複雑な問題に向けられるようにすると述べました。Craig Bright氏は、ソフトウェア開発とサイバーセキュリティはAIで作り変えられつつあるとし、技術を作る・試す・守る・運用する工程にAIエージェントを組み込んでいく方針を示しています。

銀行でのClaudeの利用はBarclaysに限りません。Anthropicの金融機関向けページでは、Citiが社内の開発者向けプラットフォームにClaudeを採用した事例なども紹介されています。今回の発表の特徴は、利用者数や処理件数といった規模を数字で示した点にあります。一方で、作業時間の短縮幅や費用の削減額は公表されていません。

## 日本で真似するなら

参考になるのは広げた順番です。Barclaysは、まず社内の情報を探す「行員向けの検索」から始め、次に大量に届く問い合わせの「仕分け」、そして開発の現場へと対象を広げました。どれも、AIの出力をそのまま顧客に出すのではなく、行員の手元に届ける使い方です。

- **社内検索**：商品説明書、事務手続きのマニュアル、FAQを集め、RAGで検索できるようにする。最初はコールセンターや支店など、問い合わせが多い部署から
- **メールの仕分け**：分類のラベルと「処理に必要な情報」の一覧を先に決め、AIには分類と不足情報の指摘だけを任せる
- **開発**：Claude Codeの対象者と普及率の目標を、Barclaysのように数字で決めて段階的に広げる

## 日本のビジネスへの影響

ClaudeとClaude Codeは日本からも使えます。データを日本国内で処理したい場合の選択肢は「[Amazon BedrockのClaude、ソウルとシンガポールで推論を国内完結に](/news/20261001-aws-bedrock-claude-in-region-seoul-singapore/)」で整理しています。

関係が深いのは、銀行・保険・証券の情報システム部門と、顧客対応の部門の責任者です。規制の厳しい英国の大手銀行が、1万人規模で行員にAIを使わせ、顧客対応の裏側に組み込んでいる点は、社内の説得材料になります。

今すぐやれるのは、問い合わせメールを1週間分抜き出し、分類のラベルと必要情報の一覧を作ってClaudeに仕分けさせ、担当者の判断とどれだけ一致するかを比べることです。一致率が見えれば、どこまで任せられるかを議論できます。開発での使い方は「[コーディングAIのおすすめと料金比較](/best/coding/)」を参考にしてください。

注意点として、今回の数字はAnthropicの発表によるもので、効果の大きさはまだ示されていません。顧客の個人情報を含むメールや文書をAIに渡す前に、社内規程やFISC（金融情報システムセンター）の安全対策基準など、既存のルールとの整合を確かめてください。
