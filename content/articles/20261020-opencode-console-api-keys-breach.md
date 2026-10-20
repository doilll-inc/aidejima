---
{
  "title": "AIの利用料が勝手に数百ドル請求、AIツール「OpenCode」に預けた鍵が盗まれ 調べるAIは協力を拒否",
  "description": "プログラミング用のAIツールOpenCodeのWeb版が侵入され、利用者1.4%が預けていたAIサービスの鍵が悪用された。OpenAI・Anthropic・Googleの利用料が勝手に使われ、1,000ドルを超えた人もいると報じられ、各社が鍵の停止や返金に動いた。",
  "date": "2026-10-20T18:40:00+09:00",
  "category": "dev",
  "tags": ["OpenCode", "OpenCode Console", "セキュリティ", "API", "Anthropic", "OpenAI"],
  "summary": [
    "プログラミング用のAIツールOpenCodeのWeb版が侵入され、利用者の1.4%が預けていたAIサービスの鍵が盗まれた",
    "盗まれた鍵でOpenAI・Anthropic・GoogleのAIが勝手に使われ、1人数百ドル、1,000ドルを超える請求が来た人もいると報じられている",
    "各社は鍵の停止や返金に動いた。調査に使ったAIは途中から攻撃の中身の分析を断り、対応が遅れたと開発者は明かしている"
  ],
  "sources": [
    {"title": "OpenCode のセキュリティ事故の公表", "publisher": "X @opencode", "url": "https://x.com/opencode/status/2111519637049319818", "kind": "X投稿"},
    {"title": "Dax Raad（OpenCode共同創業者）の投稿：Consoleのみが対象", "publisher": "X @thdxr", "url": "https://x.com/thdxr/status/2111572618340188393", "kind": "X投稿"},
    {"title": "Dax Raad の投稿：返金を開始", "publisher": "X @thdxr", "url": "https://x.com/thdxr/status/2111608620441817449", "kind": "X投稿"},
    {"title": "Dax Raad の投稿：調査中にAIが分析を拒否", "publisher": "X @thdxr", "url": "https://x.com/thdxr/status/2111831348336091179", "kind": "X投稿"},
    {"title": "Lydia Hallie（Anthropic）の投稿：Claudeの鍵を無効化", "publisher": "X @lydiahallie", "url": "https://x.com/lydiahallie/status/2111563956666110287", "kind": "X投稿"},
    {"title": "Evan Otero（Google）の投稿：Geminiの鍵を停止", "publisher": "X @EvanOtero", "url": "https://x.com/EvanOtero/status/2111591525876474100", "kind": "X投稿"},
    {"title": "Tibo（OpenAI）の投稿：返金と Daybreak Blue", "publisher": "X @thsottiaux", "url": "https://x.com/thsottiaux/status/2112034063934742720", "kind": "X投稿"},
    {"title": "Chris Sinco の投稿：利用額の警告", "publisher": "X @csinco", "url": "https://x.com/csinco/status/2111466173762334790", "kind": "X投稿"},
    {"title": "David Sacks の投稿", "publisher": "X @DavidSacks", "url": "https://x.com/DavidSacks/status/2111867605388493282", "kind": "X投稿"},
    {"title": "Hackers hit AI coding tool OpenCode, running up charges on users' AI accounts", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/10/19/hackers-hit-ai-coding-tool-opencode-running-up-charges-on-users-ai-accounts/", "kind": "報道"}
  ],
  "thumb_prompt": "A small glowing key hanging on a hook inside a cracked glass cabinet, with a long paper receipt spilling out of a nearby slot and curling across the floor, while a tiny robot in the corner turns its back with arms crossed.",
  "thumb_style": "3d",
  "thumb_text": "OpenCode",
  "share_text": "AIツールOpenCodeに預けた鍵が盗まれ、AIの利用料が勝手に数百ドル。調べるAIは途中で協力を拒否",
  "editor_note": ""
}
---
プログラミング用のAIツール「OpenCode」は現地時間10月17日、Web版のサービス「OpenCode Console」に侵入され、利用者の1.4%が預けていたAIサービスの鍵（APIキー。AIの利用料が請求される合い言葉のようなもの）が悪用されたと公表しました。盗まれた鍵でOpenAI・Anthropic・GoogleのAIが勝手に使われ、1人あたり数百ドル、中には1,000ドルを超える請求が来た人もいるとTechCrunchが報じています。

## 何が起きたか

OpenCodeは、OpenAI・Anthropic・Googleなど各社のAIを選んでプログラミングの作業をさせられる無料公開のツールです。利用者は自分で契約したAIサービスの鍵をツールに登録して使います。今回侵入されたのは、ツール本体ではなく、Web上で鍵などを保存できる古いほうのサービスでした。

{{x:https://x.com/opencode/status/2111519637049319818}}

OpenCodeは公式Xで、前夜にセキュリティの侵害があり、Consoleの利用者の1.4%が影響を受けたと説明しました。対象者には当日の朝にメールで知らせ、メールが届いていない人は影響を受けていないとしています。共同創業者のダックス・ラード氏は、手元のパソコンで動くツール本体の利用者は鍵をOpenCodeに送っていないため対象外だと補足しました。

OpenCodeは今回の攻撃を「大規模な蒸留攻撃」に関係すると説明しています。蒸留とは、他社のAIに大量の質問をして答えを集め、それを使って自分のAIを鍛えるやり方です。他人の鍵を使えば、その費用を鍵の持ち主に払わせることができます。ただしTechCrunchは、蒸留が目的だったという説明には裏付けがなく、懐疑的な見方もあると伝えています。

## 被害に気づいた人と、AI各社の対応

最初に気づいた利用者の1人、クリス・シンコ氏は、寝る前にOpenAI・Anthropic・Googleの3社から利用額の警告が一斉に届いたとXに投稿し、OpenCodeで鍵を使ったことがある人は鍵を止めるよう呼びかけました。

AI各社は、それぞれの開発者向けの担当者がXで対応を伝えています。

| 会社 | 対応 |
|---|---|
| Anthropic | 影響を受けたとみられるClaudeの鍵を無効にした。念のため新しい鍵を作るよう案内 |
| Google | 流出したGeminiの鍵を停止。AI Studioで新しい鍵を作り、古い鍵を消すよう案内 |
| OpenAI | OpenCodeと協力して利用者が使える状態に戻し、攻撃で使われた分の利用料を返金 |

OpenCodeのラード氏も、対象者への連絡は済み、返金の手続きが進んでいるとXで答えています。TechCrunchによると、攻撃者は48時間にわたって休みなく侵入を試み続けていたとラード氏は話しています。どうやって侵入されたのか、鍵がどう保存されていたのかは、まだ明らかにされていません。

## 守る側のAIが「協力を拒否」

もう1つ注目を集めたのは、調査の途中でAIが手を貸さなくなったことです。OpenCodeは攻撃の分析にAIを使っていましたが、攻撃に使われた不正なプログラムを読ませると、AIの安全のための制限に引っかかり、分析を断るようになったといいます。

{{x:https://x.com/thdxr/status/2111831348336091179}}

ラード氏は、AIは途中まではかなり働いたが、その後は断るようになり、対応の最中にもどかしかったと投稿しました。その後、OpenAIが守る側の調査に限って制限をゆるめたAIを使わせる「Daybreak Blue」という枠を使えるようになり、調査が進めやすくなったとしています。OpenAIの担当者も、この枠の申し込みを呼びかけています。

米大統領の科学技術諮問会議の共同議長を務めるデビッド・サックス氏は、この件を取り上げ、AIの安全対策を一部の会社の判断に集める今のやり方では、守る側まで止められてしまうと投稿しました。一方で、攻撃の分析を誰にでも許せば、それを攻撃にも使えてしまうという悩みは残ります。

## 日本のビジネスへの影響

- **関係あるか**: 日本でもOpenCodeを使う開発者はいますが、影響を受けたのはWeb版に鍵を保存していた一部の利用者だけで、メールが届いていなければ対象外です。ただ、AIの鍵をさまざまなツールに登録して使う働き方は日本の職場でも広がっており、同じことはどのツールでも起こりえます
- **誰に効くか**: 社内でAIサービスの契約と支払いをまとめている情報システム部門と、社員が自分でAIツールを試すのを認めている部署の責任者です。鍵が盗まれると、請求は会社のクレジットカードや契約に来ます
- **今すぐやれること**: OpenAI・Anthropic・Googleの管理画面で、使っていない鍵を消し、利用額の上限と警告の設定を確かめることです。今回、被害に早く気づいた人は利用額の警告が届いていました。外部のツールに鍵を登録するときは、ツールごとに別の鍵を作っておけば、1つが漏れても止めるのは1本で済みます。プログラミング用のAIツール選びは[用途別ガイドのコーディングAI](/best/coding/)にまとめています
- **注意点**: AI各社が今回は返金に応じましたが、いつも返金されるとは限りません。また、AIが攻撃に使われる例は増えており、守る側がAIで調べようとしても断られる場面がありうることは、社内の事故対応の手順にも織り込んでおく必要があります（[100字足らずの指示でAIが通販サイトに次々侵入](/news/20261020-ai-agents-cairn-hacked-100-sites-japan/)）
