---
{
  "title": "Claude Codeの料金は月20ドルのProから、Maxや従量課金との違いと選び方",
  "description": "Claude Codeは単体では売られておらず、Claudeの有料プランに含まれる。個人なら月20ドルのProから使え、上位のMaxは月100ドルと200ドル。チャットとの上限の共有や従量課金との違いを公式情報で整理した。",
  "date": "2026-10-08T00:30:00+09:00",
  "category": "dev",
  "format": "howto",
  "tags": ["Claude Code", "Anthropic", "料金", "使い方", "コーディング"],
  "summary": [
    "Claude Codeは単体では売られておらず、Claudeの有料プラン（Pro・Max・Team・Enterprise）に含まれる。無料版では使えない",
    "個人ならPro（月20ドル、年払いで月17ドル）から始められ、たくさん使う人向けのMaxは月100ドルと月200ドルの2段階",
    "利用上限はチャットと共通で5時間ごとに戻る。上限を超えても、追加料金（従量課金）を有効にすれば作業を続けられる"
  ],
  "sources": [
    {"title": "Plans & Pricing", "publisher": "Anthropic（claude.com）", "url": "https://claude.com/pricing", "kind": "公式ドキュメント"},
    {"title": "What is the Max plan?", "publisher": "Claude Help Center", "url": "https://support.claude.com/en/articles/11049741-what-is-the-max-plan", "kind": "公式ドキュメント"},
    {"title": "Manage costs effectively", "publisher": "Claude Code Docs", "url": "https://code.claude.com/docs/en/costs", "kind": "公式ドキュメント"},
    {"title": "Quickstart", "publisher": "Claude Code Docs", "url": "https://code.claude.com/docs/en/quickstart", "kind": "公式ドキュメント"}
  ],
  "thumb_text": "Claude Code 料金",
  "thumb_style": "3d",
  "thumb_prompt": "Three glass jars of different sizes on a desk, filled with glowing blue sand like hourglasses, next to an open laptop whose screen shows only abstract code shapes; the smallest jar is almost empty while a tiny wind-up robot pours more sand in.",
  "share_text": "Claude Codeの料金は月20ドルのProから。チャットと上限を共有、Maxは月100ドルと200ドル。10月8日時点の公式情報で整理",
  "editor_note": ""
}
---
Claude Codeの料金は、AnthropicのAI「Claude」の有料プランに含まれる形が基本で、個人なら月20ドル（年払いなら月17ドル）のProプランから使えます。無料版には含まれません。この記事では10月8日時点の公式の料金表とヘルプで、プランごとの違いと選び方を整理します。

## Claude Codeとは、何ができるか

Claude Codeとは、Anthropicが提供する、Claudeにパソコン上のファイルを読ませ、プログラムを書かせたり直させたりできる道具です。チャット画面にコードを貼り付けて質問するのと違い、Claude自身がフォルダの中身を調べ、ファイルを編集し、コマンドを実行して結果を確かめるところまで進めます。

もともとは黒い画面にコマンドを打ち込む「ターミナル」で使う道具でしたが、いまは[公式の手順書](https://code.claude.com/docs/en/quickstart)によると、ブラウザ（claude.ai/code）、デスクトップアプリ、VS CodeやJetBrainsといった開発ソフト、Slackからも使えます。

使い道はプログラミングに限りません。AIデジマでも、ハーバード大の教授がClaude Codeで3カ月に論文原稿36本を仕上げた例（[既報](/news/20261004-bootloops-claude-shaped-science/)）や、画面や動きを作り替えられる拡張機能「Mods」（[既報](/news/20261003-claude-code-mods/)）を紹介してきました。

## 料金とプラン

料金表（[claude.com/pricing](https://claude.com/pricing)）で確認した、Claude Codeが使えるプランは次のとおりです。価格はドル建てで、税は含みません。円建ての公式価格はありません。

| プラン | 月額 | 向いている人 |
|---|---|---|
| Free（無料） | 0ドル | Claude Codeは使えない |
| Pro | 20ドル（年払いなら月17ドル） | まず試したい個人 |
| Max 5x | 100ドル | 毎日長時間使う個人（Proの5倍の利用量） |
| Max 20x | 200ドル | 一日中使う個人（Proの20倍の利用量） |
| Team 標準席 | 1人25ドル（年払いなら20ドル） | 社員みんなで使う会社 |
| Team プレミアム席 | 1人125ドル（年払いなら100ドル） | 会社の中でも開発を多く担う人（標準席の5倍） |
| Enterprise | 1人20ドル（年払い）＋使った分をAPI料金で | 大企業 |

Maxプランは、ヘルプページによると月払いだけで、年払いはありません。表示の価格はウェブから申し込んだ場合のもので、スマートフォンのアプリから申し込むと価格が変わる場合があると書かれています。

料金表のよくある質問には、Claude Codeの扱いが次のように書かれています。

:::quote https://claude.com/pricing | Anthropic「Plans & Pricing」
> Claude Code is included in all paid plans. It shares the same usage limits as the rest of your plan, so your work in the terminal and your chats draw from one pool.
Claude Codeはすべての有料プランに含まれる。プランのほかの機能と同じ利用上限を共有するので、ターミナルでの作業とチャットは同じ枠から消費される。
:::

つまり、Proプランでチャットをたくさん使った日は、Claude Codeで使える量も減ります。利用上限は5時間ごとに戻る仕組みで、有料プランには週単位の上限もあります。上限に達したときは、戻るのを待つか、上のプランに変えるか、「使用クレジット」を有効にしてAPIの標準料金で作業を続けるかを選べます。

### 月額プランを使わない「従量課金」もある

Claude Codeは、開発者向けの管理画面「Claude Console」のアカウントでも使えます。この場合は月額ではなく、AIが読み書きした文章の量（トークン）に応じた従量課金です。料金表によると、100万トークンあたりの価格は、標準的なSonnet 5.5が入力2ドル・出力10ドル、上位のOpus 5.5が入力4ドル・出力20ドルです。

どれくらいかかるかの目安として、公式ドキュメントは企業での利用実績を示しています。

:::quote https://code.claude.com/docs/en/costs | Claude Code Docs「Manage costs effectively」
> Across enterprise deployments, the average cost is around $13 per developer per active day and $150-250 per developer per month, with costs remaining below $30 per active day for 90% of users.
企業での導入全体では、開発者1人あたり平均で稼働日1日に約13ドル、月に150〜250ドルかかり、90%の利用者は稼働日1日30ドル未満に収まっている。
:::

毎日使う開発者なら、従量課金で月150〜250ドルかかる計算です。同じ人がMax（月100ドルか200ドル）を契約すれば、上限の範囲内なら定額で済みます。たまにしか使わない人や、会社で使った分だけ払いたい場合は従量課金が向いています。

{{card:https://claude.com/pricing|Plans & Pricing|Anthropic}}

## 始め方

公式の手順書によると、ターミナルで使う場合の流れは次のとおりです。

1. Claudeの有料プラン（Pro以上）を契約するか、Claude Consoleのアカウントを作る
2. ターミナルを開き、Macなら `curl -fsSL https://claude.ai/install.sh | bash`、WindowsのPowerShellなら `irm https://claude.ai/install.ps1 | iex` を貼り付けて実行する
3. 作業したいフォルダで `claude` と打つ。初回はブラウザが開くので、Claudeのアカウントでログインする
4. 「このフォルダには何が入っている？」のように、普段の言葉で頼む

ターミナルに慣れていない人は、ブラウザから使える claude.ai/code やデスクトップアプリから始めるほうが簡単です。

## 仕事での使いどころ

- **マーケター**: 広告の成果データの表計算ファイルをフォルダに置き、「媒体別に費用対効果を集計してグラフにして」と頼む。集計用の小さなプログラムをClaudeが書いて動かすので、関数を組む手間が省けます
- **事業・企画の担当者**: 社内向けの簡単な申請フォームや、商品リストを見せるだけのページを、説明文から試作させる。エンジニアに頼む前の「たたき台」づくりに向いています
- **開発者**: 既存のプログラムの不具合の調査、テストの作成、説明書の更新など、手間のかかる作業を任せる。公式ドキュメントは、関係ない作業に移るときは会話を切り替える（`/clear`）と消費が抑えられるとしています

## 日本のビジネスへの影響

- **使えるか**: 日本はClaudeの公式の提供国に含まれ、日本からProやMaxを契約できます。料金はドル建てで、円建ての公式価格はありません。指示も返答も日本語で通じます
- **誰にどう効くか**: まずは個人のProプラン（月20ドル）で、マーケターや企画担当者が自分の集計・資料づくりの作業を任せられるか試すのが手頃です。毎日の開発に使う開発者は、従量課金の目安（月150〜250ドル）と比べるとMaxのほうが安く済む場合があります
- **今すぐやれること**: Proを1カ月だけ契約し、繰り返している表計算や資料づくりの作業を1つClaude Codeに頼んでみます。上限にすぐ届くようならMaxを、ほとんど使わないなら従量課金を検討します
- **注意点**: チャットとClaude Codeは同じ利用枠を使うので、チャット中心の人がClaude Codeも使うと上限に早く届きます。会社で使う場合、個人向けのPro・Maxは消費者向けの規約で、Team・Enterpriseは法人向けの規約になります。社内の資料を扱うならTeam以上を選ぶのが無難です

ほかのコーディング用AIとの料金比較は、[コーディングAIのおすすめと料金比較](/best/coding/)にまとめています。
