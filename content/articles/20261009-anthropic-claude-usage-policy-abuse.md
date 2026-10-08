---
{
  "title": "Claudeへの度を越した暴言を規約で禁止、Anthropicが利用ルールを改定 偽アカウントや監視も明記",
  "description": "Anthropicは10月8日、Claudeの利用ルール（Usage Policy）を改定し、11月12日に施行すると発表した。目的のない執拗な暴言を禁じる項目を新設し、政治・商用を問わない偽アカウント運用や、本人の同意のない追跡の禁止も明文化した。",
  "date": "2026-10-09T03:55:00+09:00",
  "category": "policy",
  "tags": ["Anthropic", "Claude", "利用規約", "安全性", "規制"],
  "summary": [
    "AnthropicはClaudeの利用ルールを改定し、11月12日から「目的のない執拗な暴言や残酷な扱い」を禁止事項に加える",
    "Claudeへのいら立ちや反論、暗い題材の創作、性能の試験は対象外で、取り締まりの中心はClaude自身が会話を打ち切る機能のまま",
    "偽アカウントや架空のニュースサイトを使った世論工作は、政治目的でも商売目的でも禁止と1つの章にまとめ直した"
  ],
  "sources": [
    {"title": "2026 Usage Policy update", "publisher": "Anthropic", "url": "https://www.anthropic.com/news/2026-usage-policy-update", "kind": "公式発表"},
    {"title": "Anthropic changes usage policy to ban model abuse and election interference", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/10/08/anthropic-changes-usage-policy-to-ban-model-abuse-and-election-interference/", "kind": "報道"},
    {"title": "Anthropic bans 'abusive or cruel behavior' toward Claude", "publisher": "The Verge", "url": "https://www.theverge.com/ai-artificial-intelligence/1008100/anthropic-new-usage-policy-abuse-claude", "kind": "報道"}
  ],
  "thumb_text": "Claude 利用ルール",
  "thumb_style": "3d",
  "thumb_prompt": "A glossy 3D chat bubble sitting politely on an office desk, holding up a tiny red stop sign toward a giant, angry keyboard that looms over it, with a thick rulebook lying open beside them.",
  "share_text": "Claudeへの度を越した暴言が規約違反に。Anthropicが利用ルールを改定、11月12日施行",
  "editor_note": ""
}
---
Anthropicは現地時間10月8日、対話AI「Claude」の利用ルール（Usage Policy）の改定版を公開し、11月12日に施行すると発表しました。目を引くのは、Claudeに対して目的もなく暴言や残酷な扱いを繰り返す行為を、新たに禁止事項に加えた点です。

## 何が変わったか

Usage Policyとは、ClaudeのアプリやAPI（他社のサービスからClaudeを呼び出す仕組み）を使う全員に適用される「やってはいけないこと」の一覧です。Anthropicは毎年見直しており、今回は1年ぶりの改定になります。発表によると、変更の多くは既存のルールをはっきりさせるためのもので、この1年でClaudeが長い作業を自分で進めるようになったことや、実際に見つかった悪用の手口を反映しています。

主な変更は次のとおりです。

| 項目 | 改定の中身 |
|---|---|
| AIへの暴言 | 目的のない執拗な暴言・残酷な扱いを新たに禁止 |
| 偽アカウント・世論工作 | 選挙・詐欺・偽情報などに散らばっていた規則を1つの章に統合。政治でも商用でも対象 |
| 選挙 | 有権者をだます・選挙を妨害する行為に絞り込み、個人に合わせた選挙運動の一律禁止は撤廃 |
| 兵器 | 兵器を誘導・制御するソフトや部品、ドローンへの武装も禁止対象と明記 |
| 監視・捜査 | 本人の同意のない追跡を禁止。捜査・逮捕・起訴の対象者をClaudeに決めさせたり推薦させたりすることも禁止 |
| 物理的に動く機械 | 人をけがさせうる機械をClaudeが動かす場合、人が監視して止められること、接続が切れても安全な状態を保てることを要求 |
| 提供地域 | 提供対象外の地域にいる人、そこに本社がある企業、そこの資本が過半を握る企業の利用を禁止と明確化 |

{{card:https://www.anthropic.com/news/2026-usage-policy-update|2026 Usage Policy update|Anthropic}}

## 「Claudeへの暴言禁止」はどこまでか

新しい項目について、Anthropicは対象をかなり狭く定義しています。

:::quote https://www.anthropic.com/news/2026-usage-policy-update | Anthropic公式ブログ「2026 Usage Policy update」
> We’ve added a prohibition on sustained and needless abusive or cruel behavior toward our models. The policy update is meant to apply only in extreme cases, where users repeatedly act cruelly toward our models, with no discernible purpose.
当社のモデルに対する、執拗で不必要な暴言や残酷な振る舞いの禁止を加えた。この改定は、利用者が目に見える目的もなく繰り返しモデルを残酷に扱う、極端な場合にだけ適用することを意図している。
:::

回答が気に入らずに強い言葉で言い返す、何度も反論する、暗いテーマの小説を書かせる、AIの弱点を探す試験をする、といった使い方は対象外だと明記しています。取り締まりの主な手段は、Claude自身が悪質な相手との会話を打ち切る機能です。この機能はすでにClaude.aiとClaude Codeに入っており、今回の規約はそれを後追いで明文化した形です。

## 商用の「偽アカウント」も同じ章で禁止

マーケティングに関わる人が押さえておきたいのは、偽装した発信の扱いです。これまで選挙・詐欺・プライバシー・偽情報の各章に分かれていた規則を、1つの章にまとめました。

:::quote https://www.anthropic.com/news/2026-usage-policy-update | Anthropic公式ブログ「2026 Usage Policy update」
> We've consolidated those rules into a new section titled Do Not Engage in Deceptive Campaigns or Artificial Activity, which applies to deceptive activity of any kind (whether political or commercial).
これらの規則を「欺瞞的なキャンペーンや人為的な活動をしない」という新しい章に統合した。政治・商業を問わず、あらゆる欺瞞的な活動に適用される。
:::

発信者を隠すこと、偽アカウントや偽の投稿で内容を拡散することに加え、そうした工作のための道具を作ることも対象です。Anthropicは9月の脅威報告で、国営メディアや政府の宣伝部門、民間企業がClaudeで偽アカウント網や架空のニュースサイトを運営していた例を公表しており、今回の改定はその延長にあります。

一方で、選挙の章は対象を絞りました。非営利団体が外国語で有権者向けの案内を書く、といった正当な活動まで止めていたためで、個人に合わせた選挙運動の一律禁止はやめています。だます目的の働きかけや個人データの悪用は、ほかの章で引き続き禁止です。

## 反応と論点

TechCrunchは、AIへの暴言の禁止を今回の改定でもっとも注目を集める変更として取り上げ、Claudeが8月から悪質な会話を打ち切るよう訓練されてきた流れを紹介しています。The Vergeも見出しでこの点を扱いました。

論点は2つあります。1つは「AIへの配慮」を規約に書くことの意味です。AIに感情があるかは決着していない問いで、利用者を守る規則ではなく、モデルの扱い方の規則を足したことは異例です。もう1つは運用の線引きで、「目的のない」「繰り返し」をどう判定するかは、会話を打ち切るClaude側の判断に委ねられます。ただし、Anthropicは極端な例に限ると繰り返し説明しており、普段の使い方で影響を受ける人はほとんどいない設計です。

AnthropicはClaudeに関する取り組みを続けて発表しており、10月8日には問い合わせ対応向けの小型モデルも公開しています（[AnthropicがClaude Haiku 5.5を公開](/news/20261008-anthropic-claude-haiku-5-5/)）。

## 日本のビジネスへの影響

- **使えるか**: 改定版は11月12日に施行され、日本の利用者にもそのまま適用されます。提供地域の明確化では、対象外の地域の資本が過半を握る企業は、日本に拠点があっても使えない点が改めて書かれました。海外資本の入ったグループ会社で導入している場合は確認が必要です
- **誰にどう効くか**: 広告・SNS運用の担当者には、商用の偽アカウントや発信者を隠した拡散が「Claudeで作ってはいけないもの」とはっきりしたことが大きいです。口コミの水増しや、企業名を伏せた投稿の量産にClaudeを使うと規約違反になります。医療・金融・人事でClaudeを使う企業の担当者は、人が最終確認する体制と、AIを使ったと本人に伝える義務が変わらず求められる点を押さえてください
- **今すぐやれること**: 社内でClaudeを使っている業務を一覧にし、SNSの投稿代行や口コミ対応、採用や融資の判断補助に当たるものがないか、11月12日までに改定版と照らし合わせておくと安心です
- **注意点**: 今回の発表は変更点の要約です。Claudeを組み込んだ自社サービスを提供している場合は、全文が載った公式のUsage Policyのページで、自社の用途がどの章に当たるかを原文で確かめてください。暴言の禁止は極端な例に限られるので、社員の普段の使い方を過度に縛る必要はありません

チャットAIの選び方と料金の比較は、[チャットAIのおすすめと料金比較](/best/chat/)にまとめています。
