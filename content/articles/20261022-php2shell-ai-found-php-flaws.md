---
{
  "title": "WordPressなどWebサイトの多くが動く仕組みに重大な穴、AIが見つけて修正版が公開",
  "description": "Webサイトを動かすプログラム言語PHPに、外から乗っ取れる重大な欠陥が2件見つかり、10月21日に修正版が出た。発見には米Wizなどが最新のAIを使った。Wizは世界のWebサイトの約70%がPHPで動くとしており、米国家安全保障局（NSA）も即時の更新を呼びかけている。",
  "date": "2026-10-22T10:20:00+09:00",
  "category": "policy",
  "tags": ["PHP", "PHP2Shell", "セキュリティ", "WordPress", "Gemini 4 Argon", "GPT-5.6 Sol"],
  "summary": [
    "Webサイトを動かすPHPに、パスワードなしで外からサーバーを乗っ取れる重大な欠陥が2件見つかり、10月21日に修正版が出た",
    "見つけたのは米Wizなどのセキュリティ企業で、GoogleのGemini 4 ArgonやOpenAIのGPT-5.6 Solを使った。欠陥は10年以上前からあった",
    "公表前に情報が漏れて攻撃の準備が進んだおそれがあり、WordPressや米NSAはサーバーのPHPをすぐ更新するよう求めている"
  ],
  "sources": [
    {"title": "Today's PHP Security Release, and How We're Strengthening PHP Security", "publisher": "The PHP Foundation", "url": "https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/", "kind": "公式発表"},
    {"title": "PHP2Shell: AI uncovers critical RCE vulnerabilities affecting 70% of the Internet", "publisher": "Wiz Blog", "url": "https://www.wiz.io/blog/php2shell-php-rce", "kind": "公式発表"},
    {"title": "NSA Cyber の投稿", "publisher": "X @NSACyber", "url": "https://x.com/NSACyber/status/2112903220209098897", "kind": "X投稿"},
    {"title": "WordPress の投稿", "publisher": "X @WordPress", "url": "https://x.com/WordPress/status/2112907323265917274", "kind": "X投稿"},
    {"title": "Today's PHP Security Release, and How We're Strengthening PHP Security", "publisher": "Simon Willison", "url": "https://simonwillison.net/2026/Oct/21/php-security-release/"},
    {"title": "PHP Armageddon: OpenAI, Google's Wiz find ancient holes, panicking the internet", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/10/21/php-armageddon-openai-googles-wiz-find-ancient-holes-panicking-the-internet/", "kind": "報道"},
    {"title": "OpenAI's GPT-5.6 Sol and Google's Gemini 4 Argon found critical PHP flaw affecting millions of websites", "publisher": "The Decoder", "url": "https://the-decoder.com/openais-gpt-5-6-sol-and-gemini-4-argon-discovered-the-critical-php-vulnerability-affecting-millions-of-websites/", "kind": "報道"}
  ],
  "thumb_prompt": "An old brick foundation under a row of colorful small shop buildings, with a tiny glowing magnifying-glass robot pointing at one long hidden crack running beneath all of them while workers rush in with patch kits.",
  "thumb_style": "illustration",
  "thumb_text": "PHP2Shell",
  "share_text": "Webサイトの多くが動くPHPに重大な穴、AIが見つけて修正版が公開。WordPressのサイトも更新が必要",
  "editor_note": ""
}
---
Webサイトを動かすためのプログラム言語「PHP」に、外部から認証なしでサーバーを乗っ取れる重大な欠陥が2件見つかり、開発元のPHPプロジェクトは現地時間10月21日に修正版を公開しました。欠陥を見つけたセキュリティ企業は、GoogleやOpenAIの最新のAIを使っていました。発見した米Wizによると世界のWebサイトの約70%がPHPで動いており、WordPressで作った会社のサイトも、サーバー側で更新しないと危険な状態です。

## 何が起きたか

PHPとは、WordPressやDrupalのようなサイト作成ソフトの土台になっている、Webサーバー上で動くプログラム言語です。会社のホームページやブログ、ネットショップの多くがこの上で動いています。

今回見つかったのは、PHPの中核部分のメモリーの扱いにかかわる欠陥2件です。Wizは「PHP2Shell」と名付けました。深刻度の指標CVSSは10点満点で9.2で、最も重い「緊急」にあたります。悪用されると、パスワードを知らない外部の人がサーバーの中で好きな命令を実行できます。Wizは、最新版のWordPress・Drupal・Joomlaの環境で実際に乗っ取りができることを確かめたとしています。

PHPの運営団体PHP Foundationは、修正したPHP 8.5.12、8.4.27、8.3.36、8.2.35を公開し、強い言葉で更新を求めました。

:::quote https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/ | The PHP Foundation「Today's PHP Security Release, and How We're Strengthening PHP Security」
> If you run PHP, it is imperative that you update now.
PHPを使っているなら、いますぐ更新することが不可欠です。
:::

Wizによると、欠陥はPHP 5.4までさかのぼるほぼすべての版にあり、ここ10年に出た版には必ずどちらかが含まれます。8.2より古い版はもう修正が配られないため、古いPHPのままのサイトは版を上げる必要があります。

## AIは何をしたのか

Wizは、自社のセキュリティ用AIエージェント「Wiz Atlas」に、GoogleのGemini 4 ArgonとOpenAIのGPT-5.6 Solを組み合わせて調べました。8月19日に最初の欠陥を見つけ、翌日にはDrupal、2日後にはWordPressで乗っ取りを確かめています。AIは欠陥の発見だけでなく、攻撃の手順づくり、攻撃の検知方法、修正が効くかの確認にも使われました。

:::quote https://www.wiz.io/blog/php2shell-php-rce | Wiz Blog「PHP2Shell」
> Frontier AI models substantially reduced that barrier, turning a longstanding flaw into an exploit.
最先端のAIモデルがその壁を大きく下げ、長く眠っていた欠陥を実際の攻撃手段に変えた。
:::

ここで言う「壁」とは、欠陥が実際に悪用できることを示すまでの手順の複雑さです。Wizは、人間の研究者にとっては現実的にできる範囲の限界に近い作業だったと説明しています。欠陥は何十年も前からありましたが、悪用が難しすぎて見過ごされてきました。

もう1社、セキュリティ企業のCalifも欠陥の1つを見つけています。OpenAIがオープンソースの欠陥探しを支援する取り組み「Patch the Planet」の一環で、GPT-5.6 Solを使ったと、TechCrunchなどが報じています。

## 公表前に情報が漏れた

今回は、欠陥の公表と修正版の配布の段取りが崩れました。PHP Foundationの説明では、本来は10月22日に修正版を出す予定でした。

- 10月20日 15時ごろ（協定世界時）: 欠陥の番号が掲示板やSNSで出回る。技術的な中身は含まれていなかった
- 同日 20時ごろ: Califが、攻撃の実演動画を誤って公開。動画の写しがSNSで広がり、攻撃手順づくりを早めた
- 10月21日 7時41分: 別の企業が、取り決めより6時間以上早く修正入りのソフトを公開
- 同日 14時: PHPプロジェクトが予定を1日早めて修正版を公開

PHP Foundationは、公開の時点では実際に動く攻撃手段は見つかっていなかったとしています。一方で、Wizの報告からPHP側が対応を始めるまでに約1か月かかったことについて、PHP Foundationは「安全担当チームの意思決定の仕組みと人手不足による構造的な失敗」だったと認めています。

## 反応と論点

米国家安全保障局（NSA）のサイバー部門はXで、PHPを使うすべての組織に更新への備えを呼びかけました。

{{x:https://x.com/NSACyber/status/2112903220209098897}}

TechCrunchは、NSAはすぐに更新できないサイトはいったん止めるよう求めていると報じています。WordPressの公式アカウントも、欠陥はWordPress固有のものではなくサーバー側のPHPの問題だとして、サイトの持ち主にホスティング会社の更新予定を確かめるよう求めました。

{{x:https://x.com/WordPress/status/2112907323265917274}}

論点は、AIが守る側にも攻める側にも同じように効くことです。PHP Foundationは、道具が欠陥を見つける速さはかつてなく上がっており、それは守る側にも攻撃する側にも当てはまると書いています。報告の件数は今後も増え続けるとの見通しです。PHP Foundation自身も、届いた報告の確認や整理にAnthropicのClaude MythosやOpenAIのAIを使い始めています。ただし判断と修正はすべて人が行うとしています。数人の開発者が支えるオープンソースに、AIが見つけた大量の欠陥が押し寄せる構図は、10月に[米バンク・オブ・アメリカが4,000人で修正に当たると明かした件](/news/20261016-bank-of-america-mythos-patching-4000/)とも重なります。

## 日本のビジネスへの影響

- **使えるか（影響を受けるか）**: PHPは国内でも会社のホームページ、WordPressのブログやオウンドメディア、ネットショップで広く使われています。日本のサイトも対象です。ただし更新はサイトの持ち主ではなく、サーバーを管理する側の作業になることが多いです
- **誰にどう効くか**: 自社サイトやオウンドメディアを運営するマーケティング担当者、Webサイトの管理を外部の制作会社やレンタルサーバーに任せている中小企業の経営者に直接関係します。サイトが乗っ取られると、顧客情報の流出や、偽のページへの書き換えにつながります
- **今すぐやれること**: 今日のうちに、サイトの制作会社かレンタルサーバー・ホスティング会社に「PHPを8.5.12・8.4.27・8.3.36・8.2.35のいずれか以降に更新したか、予定はいつか」を問い合わせてください。レンタルサーバーの多くは管理画面でPHPの版を確認できます。社内でAIを使ってシステムの点検を進めるなら、道具の選び方は[コーディングAIのおすすめと料金比較](/best/coding/)が参考になります
- **注意点**: 8.1以前の古い版は修正の対象外で、版を上げるとプラグインやテーマが動かなくなる場合があります。更新前に、バックアップと表示の確認を制作会社と段取りしておく必要があります。AIで欠陥が見つかる速度が上がった以上、こうした緊急の更新は今後も増えると見て、サイトの保守契約に「緊急の安全更新」を含めておくと慌てずに済みます
