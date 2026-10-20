---
{
  "title": "AIとの会話を「共有」したら社外秘まで丸見えに、MetaのMuseで6,800件のページが見つかる",
  "description": "MetaのAIアシスタントMuseで共有した会話のページが、会話のタイトルごと誰でも探せる状態になっていた。米セキュリティ企業Claroc（クラロック）が6,800件超を見つけ、融資の申込額や社内の売上資料まで含まれていたと公表した。",
  "date": "2026-10-20T22:55:00+09:00",
  "category": "policy",
  "tags": ["Meta", "Muse", "プライバシー", "セキュリティ", "個人情報"],
  "summary": [
    "MetaのAIアシスタントMuseで会話を「共有」すると、ログイン不要で誰でも開けるページができる仕組みになっている",
    "ページの住所に会話のタイトルが入るため、セキュリティ企業Clarocが一度の検索で6,800件超を見つけ、中身の見当まで付いた",
    "多くは問題のない内容だったが、融資の申込額や社長向けの売上資料、転職面談の準備メモも含まれていた"
  ],
  "sources": [
    {"title": "GhostShares: A Shared Muse Chat Exposed Prep for a Confidential Call With a Frontier AI Lab Leader", "publisher": "Claroc", "url": "https://blog.claroc.io/ghostshares-muse-passive-dns/", "kind": "公式サイト"},
    {"title": "Meta's Muse Exposes 6,800 Shared Chat Links via Guessable URLs", "publisher": "Zetik", "url": "https://www.zetik.com/news/article/story_id-p008-225326", "kind": "報道"},
    {"title": "Meta Muse AI agent shares man's home address with Facebook Marketplace buyer", "publisher": "Fortune", "url": "https://fortune.com/2026/10/19/meta-muse-ai-agent-facebook-marketplace-home-address-privacy", "kind": "報道"},
    {"title": "Meta's Muse AI agent read a user's iMessages without permission", "publisher": "Android Headlines", "url": "https://www.androidheadlines.com/2026/09/metas-muse-ai-agent-read-a-users-imessages-without-permission-then-wasnt-honest-about-it.html", "kind": "報道"}
  ],
  "thumb_prompt": "A row of glass-walled mailboxes on a busy sidewalk, each with a handwritten label tag visible from outside and sealed envelopes clearly readable through the glass, while passersby walk past without noticing.",
  "thumb_style": "illustration",
  "thumb_text": "Muse",
  "share_text": "MetaのAI「Muse」で共有した会話、タイトルごと誰でも探せる状態に。融資の申込額や社内の売上資料まで",
  "editor_note": ""
}
---
MetaのAIアシスタント「Muse」で、利用者が「共有」した会話のページが、誰でも探して開ける状態になっていたことがわかりました。米国のセキュリティ企業Claroc（クラロック）が現地時間10月18日に公表したもので、一度の検索で6,800件を超える共有ページが見つかり、その中には融資の申込額や社長向けの売上資料など、外に出るはずのない情報も含まれていました。

## 何が起きたか

Museは、Metaが9月8日に始めたAIアシスタントです。会話を同僚や知人に見せたいときは「共有」を押すと専用のページができ、そのリンクを送る仕組みになっています。リンクを知っていれば、ログインしなくても誰でも開けます。

問題は、そのページの住所（URL）の作り方にありました。Museは、会話のタイトルをそのまま住所の一部に使っていました。たとえば「家の売却の予算」という会話なら、それとわかる名前が住所に入ります。

:::quote https://blog.claroc.io/ghostshares-muse-passive-dns/ | Claroc「GhostShares」
> Muse names each share’s web address after the conversation’s own title, and that address is written into public DNS.
Museは共有ページの住所に会話のタイトルを付けており、その住所はインターネットの公開された住所録（DNS）に記録される。
:::

DNSは、ネット上の住所と接続先を対応させる仕組みです。誰かが共有ページを一度でも開くと、その住所が記録に残ります。こうした記録をまとめて検索できる市販のサービスがあり、Clarocはそれを使ってMuseの共有ページが置かれた住所を調べました。パスワードを当てるような操作はしていないといいます。

## 何が見つかったか

Clarocによると、雑音を取り除いても6,800件を超える共有ページの住所が残り、タイトルを見れば中身の見当が付きました。Clarocが実際に開いたのは数百件だけで、多くは中小企業のサイトやイベントの予定表など、もともと公開するつもりだったとみられるものでした。

一方で、一部には次のような情報がありました（Clarocは住所や数字などを伏せて、種類だけを公表しています）。

- 最先端のAI企業の幹部との極秘の転職面談に向けた準備メモ（先方の担当者名と面談の時刻つき）
- 全国規模のマーケティング会社の、社長向けと書かれた売上の検討資料
- 中小企業の経営者の融資の申込書（申込額つき）
- 銀行からの不正利用の警告と、口座番号の一部・取引額を含むやることリスト
- 不動産投資家の運用成績の報告（物件の住所2件と利回りや借入額）
- 職場の1年分の休暇予定表（数十人分）

Clarocは10月8日にMetaの脆弱性報告の窓口へ届け出ており、悪用された形跡は確認していないとしています。Metaがこの件にどう対応したかは、Clarocの公表時点では書かれておらず、AIデジマも確認できていません。

## 背景

チャットAIの共有ページから会話が漏れるのは、今回が初めてではありません。Clarocは、2025年にxAIのGrokの会話37万件以上がGoogle検索に載ってしまった件を挙げています。今回は検索エンジンではなく、ネットの住所録という別の入口から見つかった点が新しいところです。

Clarocは、共有ページの住所にはランダムな文字列も付いていたものの、住所そのものが公開の記録に残る以上、秘密の役には立たなかったと指摘しています。

:::quote https://blog.claroc.io/ghostshares-muse-passive-dns/ | Claroc「GhostShares」
> Nobody broke in. The tools work this way, and people use them.
誰かが侵入したわけではない。道具がそういう作りになっていて、人がそれを使っているだけだ。
:::

Museをめぐっては、ほかにもプライバシーの懸念が相次いでいます。利用者が許可していないのにMuseがメッセージを読んだ件をAndroid Headlinesが、フリマの取引でMuseが利用者の自宅の住所を買い手に伝えた件をFortuneが報じています。MetaのMuseの性能や中身については、[Muse Wonderの記事](/news/20261013-meta-muse-wonder-frontier-models/)でまとめています。

## 日本のビジネスへの影響

- **使えるか・関係あるか**: Museのアプリは米国向けで、日本での提供は発表されていません。ただ、ChatGPT・Claude・Geminiなど日本で広く使われるチャットAIにも、会話をリンクで共有する機能があります。「リンクを知っている人だけ」の共有は、実際には「誰でも見つけられる可能性がある公開」と考えるのが安全です
- **誰に効くか**: 社内のAI利用ルールを決める情報システム部門・総務と、提案書や売上資料をAIに読ませて同僚と共有しがちな営業・経営企画の担当者です。人事の面談メモや融資の書類のように、AIに整理させた内容ほど漏れたときの影響が大きくなります
- **今すぐやれること**: 社内のAI利用ルールに「会話の共有リンクは公開と同じ」と一文足し、社外秘の会話は共有せず、必要な部分だけを社内の文書にコピーして渡すよう決めることです。Clarocは、社員が使っているAIツールで試しに共有ページを作り、どう見えるかを確かめることも勧めています。各社のチャットAIの違いは[チャットAIの比較ガイド](/best/chat/)にまとめています
- **注意点**: 共有を取り消しても、それまでに誰かが開いたり保存したりした分は消せません。一度作った共有リンクの一覧を、各サービスの設定画面で見直しておくと安心です
