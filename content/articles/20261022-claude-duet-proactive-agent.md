---
{
  "title": "Claudeが毎朝「今日の要対応」を届け仕事も代行、新アプリ「Claude Duet」を米国で試験公開",
  "description": "Anthropicが、Claudeが自分から仕事を見つけて動く新アプリClaude Duetを発表した。Gmailや会計ソフトなど6,000超のサービスとつながり、送信や支払いの前には必ず承認を求める。米国のPro・Max契約者向けに順番待ちで提供を始めた。",
  "date": "2026-10-22T09:55:00+09:00",
  "category": "products",
  "tags": ["Claude", "Claude Duet", "Anthropic", "エージェント", "中小企業"],
  "summary": [
    "Claude Duetは、つないだメールや予定表を数時間おきに見て、対応が必要なことだけを知らせてくるClaudeの新アプリ",
    "会議の調整や売上の見通し表づくりまで任せられ、メール送信や支払いの前には必ず利用者の承認を待つ",
    "提供は米国のClaude Pro・Max契約者への順番待ちから。追加料金はなく、使える量はいまのプランの上限を分け合う"
  ],
  "sources": [
    {"title": "Introducing Claude Duet", "publisher": "Anthropic（Claude公式）", "url": "https://claude.com/resources/articles/claude-duet", "kind": "公式発表"},
    {"title": "Claude Duet | Your personal AI assistant", "publisher": "Anthropic（Claude公式）", "url": "https://claude.com/product/claude-duet", "kind": "公式ドキュメント"},
    {"title": "Claude Duet", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=50186037"},
    {"title": "Claude Duet is Anthropic's answer to Meta Muse and OpenAI Dots", "publisher": "Engadget", "url": "https://www.engadget.com/2293646/claude-duet-is-anthropics-answer-to-meta-muse-and-openai-dots/", "kind": "報道"},
    {"title": "Anthropic takes on Muse with Claude Duet, its new AI agent", "publisher": "The Verge", "url": "https://www.theverge.com/ai-artificial-intelligence/1015843/anthropic-claude-duet-ai-agent", "kind": "報道"}
  ],
  "thumb_prompt": "A tidy home office at early morning with a single smartphone on the desk showing a short glowing checklist, while a small friendly robot assistant quietly holds a stack of envelopes and waits beside a big red 'approve' button.",
  "thumb_style": "3d",
  "thumb_text": "Claude Duet",
  "share_text": "Claudeが自分から仕事を見つけて動く新アプリClaude Duet。送信や支払いの前には必ず承認を待つ",
  "editor_note": ""
}
---
Anthropicは現地時間10月21日、Claudeが利用者に頼まれる前から「いま対応すべきこと」を見つけて知らせ、任された作業を進める新しいアプリ「Claude Duet」を発表しました。Gmailや会計ソフトなど6,000を超えるサービスとつながり、メールの送信や支払いの前には必ず利用者の承認を待ちます。まずは米国のClaude Pro・Max契約者を対象に、順番待ちの「研究プレビュー」（試験公開）として提供を始めました。

## 何が発表されたか

Claude Duetとは、Claudeが利用者の代わりに受信箱や予定表を見張り、必要なときだけ声をかけてくる「先回りする助手」のアプリです。これまでのClaudeは、利用者が話しかけて初めて動きました。Duetは逆に、Claudeの側から「この件、返事が必要です」と知らせてきます。

公式の発表によると、主な働きは次の4つです。

- **朝のまとめ**: つないだアプリ全体から、その日の優先事項・次の一手の下書き・承認待ちの件を短くまとめて届ける
- **見張り**: つないだアカウントを数時間おきに確認し、対応が必要なときだけメッセージを送る。何を・どのくらいの頻度で知らせるかは利用者が決められる
- **作業の代行**: 会議の日程調整から、ダッシュボード（数字を一覧できる画面）や売上の見通し、試作品、Webアプリづくりまで
- **留守中も作業**: Duet専用のクラウド上のコンピューターとブラウザーで動くため、利用者のPCやスマホの電源が切れていても進む。終わると通知が来る

確認の間隔を「数時間おき」にしている理由について、Anthropicは「常に確認するとプランの利用上限をずっと早く使い切ってしまう」と説明しています。

つながるサービスは、Claudeのマーケットプレイスにある6,000超の連携機能です。発表ではGmail、Slack、会計ソフトのQuickBooks、決済のStripe、給与計算のGusto、LinkedIn、電子契約のDocuSign、顧客管理のHubSpot、Canva、Shopifyが例に挙がっています。Stripeの決済サービスLinkの仮想カードやShop Payで、買い物の支払いまで済ませられます。

{{card:https://claude.com/product/claude-duet|Claude Duet | Your personal AI assistant|Anthropic}}

## どこまで任せてよいのか

「勝手に動くAI」で一番気になるのは、勝手に送ったり払ったりしないかです。Duetは、読む・下書きする・準備するところまでは自分で進めます。メッセージの送信、支払い、書類への署名、削除の前には、何をするのかを見せて承認を待ちます。

承認しても実行できない操作も決めてあります。

:::quote https://claude.com/resources/articles/claude-duet | Anthropic「Introducing Claude Duet」
> A few things are off-limits even with your approval, like trading securities or moving money between accounts.
いくつかの操作は、利用者が承認しても実行できません。証券の売買や口座間の送金などです。
:::

情報の扱いでは、専用の仕組みで機密情報を見分けます。クレジットカード番号や身分証の番号のような最も機密度の高い情報は、共有を頼まれても断るように作られています。健康やお金に関する個人情報は、利用者が明確に指示したときだけ共有します。パスワードやログイン用の情報をDuet自身が直接見ることはありません。

弱点も公式に書かれています。メールのやりとりを読み違えたり、緊急度を見誤ったりすることがあります。確認と確認のあいだに届いた件は見落とすこともあります。チケットの予約のような私用の手続きは仕事の作業ほど得意ではなく、Duetがブラウザーで何をしているかを利用者が画面で見る機能もまだありません。

## 料金と提供範囲

公式の製品ページは、提供範囲をこう説明しています。

:::quote https://claude.com/product/claude-duet | Anthropic「Claude Duet」製品ページ
> Claude Duet is a research preview on a waitlist for Claude Pro and Max subscribers in the US. Team and Enterprise plans are not included yet.
Claude Duetは研究プレビューで、米国のClaude Pro・Max契約者が順番待ちで使えます。TeamとEnterpriseプランはまだ対象外です。
:::

追加料金はありません。ただし使える量は、Claudeのほかの機能と同じプランの上限を分け合います。Duetの定期的な見張りや大きな作業も、その上限から差し引かれます。アプリはClaudeの本体とは別で、iOS・Android向けの単独アプリと、Web版のclaude.aiで使えます。Engadgetは、DuetはAnthropicの最上位モデルClaude Opus 5.5で動くと報じています。

## 背景

「頼まれる前に動く個人向けAI」は、この秋の大手各社の主戦場です。Metaは個人向けのAIエージェント「Muse」を米国で提供しており、OpenAIも9月末に専用のクラウドPCで24時間働く「Dots」をChatGPT Pro向けに出しました（[OpenAIのDotsの記事](/news/20260930-openai-dots-always-on-agents/)）。Duetはこの2つへのAnthropicの答えにあたります。

違いは、対象と入口の値段です。OpenAIのDotsは月100ドルからのProプランが対象でした。Duetは月20ドルのProプランから対象に入ります。Anthropicは想定する利用者を「専門職と小規模事業の経営者」とし、発表ではブランド戦略の担当者、不動産の仲介業者、複数店舗の飲食店オーナーが使う場面を紹介しています。たとえば不動産仲介業者には、内見の予約が間違った日に入っていることを指摘しました。

## 反応と論点

技術者の掲示板Hacker Newsでは、発表の投稿に250件超のコメントが付きました。前向きな声としては、OpenAIのDotsやMetaのMuseを使ってきた人が、Claudeのモデルの質の高さを理由に乗り換えを試すと書き込んでいます。

一方で懸念も目立ちます。順番待ちの登録をClaudeのアプリに頼んだら断られたという不満、作業が遅いという声、パスワード管理ソフトとの連携（今後対応予定）を不安視する声がありました。仕事と私生活とお金の情報を1社のAIにまとめて預けることへの警戒もあります。Anthropic自身も、安全対策の詳細は近く追加で公表するとしています。

## 日本のビジネスへの影響

- **使えるか**: 10月22日時点では米国のPro・Max契約者だけが対象で、日本での提供時期は発表されていません。製品ページには日本語の表示がありますが、日本から順番待ちに登録できるとは書かれていません。会社で契約するTeam・Enterpriseプランも対象外です
- **誰にどう効くか**: 効きそうなのは、メールと予定と請求書を一人でさばいている小さな会社の経営者や個人事業主です。営業やマーケティングの担当者にとっても、朝に「今日返すべき連絡」と下書きがそろうのは、受信箱を一から読む時間の節約になります
- **今すぐやれること**: 日本で使えるようになる前に、いまのClaudeで「どのアプリをつなげば朝のまとめが作れるか」を確かめておくとよいです。たとえばGmailとGoogleカレンダーをClaudeにつなぎ、「今日返信が必要なメールと、予定の重なりを教えて」と頼むと、Duetに近い使い方を手動で試せます。チャットAIの選び方は[チャットAIのおすすめと料金比較](/best/chat/)にまとめています
- **注意点**: 見張りや作業はプランの利用上限を消費します。ふだんのチャットやClaude Codeの利用量が減ることになります。会社のメールや顧客情報をつなぐ前に、社内の規程でAIに読ませてよい範囲を決めておく必要があります。承認の画面が出たら、中身を読まずに押さない運用も欠かせません
