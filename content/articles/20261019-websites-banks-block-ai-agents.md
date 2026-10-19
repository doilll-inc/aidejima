---
{
  "title": "AIに予約や買い物を任せても門前払い、米国の航空会社や銀行が「代理のAI」を締め出し始めた",
  "description": "利用者の代わりにWebで予約や買い物をするAIを、米国の大手サイトが相次いで拒んでいる。デルタ航空やYelp、JPモルガン、チャールズ・シュワブが外部のAIを止め、Cloudflareは広告のあるページでAIを止める設定を用意した。",
  "date": "2026-10-19T10:10:00+09:00",
  "category": "marketing",
  "tags": ["エージェント", "Muse", "Cloudflare", "Charles Schwab", "EC", "マーケティング"],
  "summary": [
    "利用者の代わりに予約や買い物をするAIを、米国のデルタ航空やYelp、大手銀行などが自社サイトから締め出し始めた",
    "JPモルガンとチャールズ・シュワブは、外部のAIが顧客の口座でお金を動かすのを止め、自社のAI助手に誘導している",
    "サイトの防御サービス大手Cloudflareは、広告で稼ぐサイト向けに「代理のAI」を止める設定を用意した"
  ],
  "sources": [
    {"title": "Have it both ways: stay discoverable in search while disallowing AI training", "publisher": "Cloudflare公式ブログ", "url": "https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/", "kind": "公式発表"},
    {"title": "Meet Charley, Schwab's New AI-Powered Assistant Designed to Help Clients Get Answers and Take Action", "publisher": "Charles Schwab", "url": "https://pressroom.aboutschwab.com/press-releases/press-release/2026/Meet-Charley-Schwabs-New-AI-Powered-Assistant-Designed-to-Help-Clients-Get-Answers-and-Take-Action/default.aspx", "kind": "公式発表"},
    {"title": "Local Business Data API | Yelp Data Licensing", "publisher": "Yelp", "url": "https://business.yelp.com/data/", "kind": "公式サイト"},
    {"title": "Websites are closing their doors to AI agents", "publisher": "The Verge", "url": "https://www.theverge.com/ai-artificial-intelligence/1013195/ai-agents-blocked-web", "kind": "報道"},
    {"title": "The next hurdle for AI agents: getting websites to let them in", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/10/06/the-next-hurdle-for-ai-agents-getting-websites-to-let-them-in/", "kind": "報道"},
    {"title": "Schwab blocks unauthorized AI agents, points clients to Charley", "publisher": "American Banker", "url": "https://www.americanbanker.com/news/schwab-blocks-unauthorized-ai-agents-points-clients-to-charley", "kind": "報道"},
    {"title": "Schwab and JPMorgan are blocking AI agents from moving customer money", "publisher": "The Next Web", "url": "https://thenextweb.com/news/schwab-blocks-ai-agents-meta-muse", "kind": "報道"}
  ],
  "thumb_prompt": "A tiny friendly robot holding a shopping bag and a plane ticket stands in front of a grand bank-like entrance whose heavy doors are firmly shut, while a human customer walks in through a small side door.",
  "thumb_style": "illustration",
  "thumb_text": "AIお断り",
  "share_text": "AIに予約や買い物を任せたら門前払い。米国のデルタ航空やYelp、大手銀行が「代理のAI」を締め出し始めた",
  "editor_note": ""
}
---
利用者に代わってWebサイトで予約や買い物、手続きをこなすAI（エージェント）を、米国の大手企業が自社サイトから締め出す動きが広がっています。The VergeやTechCrunchによると、デルタ航空やレビューサイトのYelpが外部のAIを受け付けず、大手銀行のJPモルガン・チェースと証券大手チャールズ・シュワブも、外部のAIが顧客の口座でお金を動かすのを止めています。AI各社が「何でも代わりにやってくれる」と売り込む機能が、相手のサイトの側で止まり始めた形です。

## 何が起きているか

ここでいうエージェントとは、利用者の指示を受けて自分でWebページを開き、ボタンを押したり入力したりして作業を進めるAIのことです。Metaの「Muse」、xAI（現SpaceXAI）の「Grok」、OpenAIの「Dots」などが、レストランの予約や商品の購入まで代行できるとうたっています。

報道で名前が挙がった主な企業と、その姿勢をまとめると次のようになります。

| 企業 | 姿勢（各社の説明・報道） |
|---|---|
| デルタ航空 | 無許可の自動操作から顧客を守るとし、外部AIに航空券の購入・予約を任せる提携はないとTechCrunchに説明 |
| Yelp | 人間以外のアクセスは、有料のデータ提供プログラムで契約したAIだけ認めるとTechCrunchに説明 |
| JPモルガン・チェース | ダイモンCEOが決算説明会で、外部のAIを社内のシステムに入れないと発言したと各社が報道 |
| チャールズ・シュワブ | ウースターCEOが、顧客のお金を動かそうとする外部AIを止めているとBloombergのテレビ番組で発言したと報道 |
| Amazon | Muse の利用を規約違反として止めたと報道。2025年からはPerplexityの買い物AIをめぐって裁判で争っている |

The Vergeは、利用者の報告として、以前は使えた自動車販売サイトCars.comや鉄道のAmtrakでもAIが使えなくなったと伝えています。理由をはっきり説明していない企業もあり、表に出ていない締め出しもあるとみられます。

## 銀行は「お金を動かすAI」に慎重

いちばん強く拒んでいるのは金融です。American Bankerによると、シュワブは外部のAIが顧客のIDとパスワードを使ってログインしたり、ブラウザーを自動で操作したりして同社のシステムに入るのを止めています。ウースターCEOは、何か起きたときに誰が責任を負うのかがはっきりしないことを理由に挙げています。

代わりにシュワブが用意するのが自社のAI助手「Charley」です。9月30日の発表によると、Charleyは10月から米国の個人顧客に順次提供され、残高や取引履歴の確認、ウォッチリストの更新、受取人の追加などに対応します。発表で示された「できる操作」の中に、送金や支払いは入っていません。

{{card:https://pressroom.aboutschwab.com/press-releases/press-release/2026/Meet-Charley-Schwabs-New-AI-Powered-Assistant-Designed-to-Help-Clients-Get-Answers-and-Take-Action/default.aspx|Meet Charley, Schwab's New AI-Powered Assistant|Charles Schwab}}

The Next Webによると、シュワブは外部のAIにも、お金は動かせず残高の確認や調べものだけができる「読み取り専用」の接続口を用意する方針です。JPモルガンもすでに、一部の外部ツールに口座情報の閲覧は認めつつ、送金や支払いはさせていないと報じられています。

## サイトの防御サービスにも「AIお断り」の設定

多くのサイトを攻撃や不正アクセスから守っている米Cloudflareは、9月15日に設定の仕組みを改めました。同社は、サイトを訪れるAIを「検索用の収集」「AIの学習用の収集」「利用者の代わりにページを開くエージェント」の3種類に分け、それぞれ許可するか止めるかをサイト側で選べるようにしています。エージェントについては「許可」「広告のあるページでは止める」「止める」の3択です。

広告で稼ぐサイトに厳しめの初期設定を勧める理由を、Cloudflareは次のように説明しています。

:::quote https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/ | Cloudflare公式ブログ「Have it both ways: stay discoverable in search while disallowing AI training」
> Ad revenue depends on a human actually seeing the page. Training replaces that visit with an answer; agents fetch the page with nobody there to see the ads.
広告収入は、人が実際にページを見ることで成り立っています。学習はその訪問を答えに置き換え、エージェントは誰も広告を見ないままページを取りに来ます。
:::

TechCrunchは、この設定変更がMuseなどの通信が止まった一因になった可能性を指摘しつつ、確認はされていないと伝えています。サイトが意図して止めていなくても、ロボットか人間かを確かめる仕組みにAIが引っかかって作業が途中で止まる例も多いとされます。

## 反応と論点

論点は「AIは利用者の代理人なのか、ただのロボットなのか」です。Amazonとの裁判でPerplexityは、AIは利用者の手足の延長であり、締め出すのは利用者が手伝いを頼む権利を否定するものだと主張してきました。Metaも、エージェントを追い返すことはその後ろにいる顧客を追い返すことだとする声明を出し、ウォルマートなどの小売りと提携してMuseを受け入れてもらう道を探っています。

一方で、企業側の事情もあります。航空会社や銀行にとっては、本人確認や不正対策を外部のAIにすり抜けられることへの警戒が大きく、誰が責任を負うかの決まりもありません。American Bankerは、シュワブには顧客の待機資金から得る金利収入を守る動機もあるという専門家の見方を紹介しており、「外部のAIは顧客のために働くが、自社のAIは会社のために働く」という指摘もあります。

The Vergeの取材に応じた安全性評価企業EquiStampのCEOは、人間であることを確かめる手間が、近いうちに食料品の通販サイトでも当たり前になりかねないと話しています。AIを止める仕組みが増えるほど、人間の利用者にとってもWebが使いにくくなるおそれがあります。

## 日本のビジネスへの影響

**使えるか**: 今回の締め出しは米国のサイトの話ですが、日本のサイトもCloudflareのような防御サービスを使っていれば、同じ設定でAIの訪問を許すか止めるかを選べます。逆に、日本の利用者がChatGPTなどのエージェント機能で米国の航空会社や銀行の手続きを任せようとしても、途中で止まることがあります。

**誰にどう効くか**: ECサイトや予約サイトを運営するマーケター・事業責任者に直接関わります。AIが買い物の窓口になり始めたとき、AIを止めれば売り逃しになり、通せば広告を見てもらえず、価格の比較も一瞬でされます。AIに選んでもらうための情報の出し方は「[広告・マーケティング向けAIのおすすめ](/best/marketing/)」でも扱っています。

**今すぐやれること**: 自社サイトのアクセス記録や防御サービスの設定画面で、AIのエージェントが来ているか、来ていたら止めているか通しているかを確かめておきましょう。止めているなら、それが意図した設定なのか、初期設定のままなのかを確認するだけでも判断材料になります。

**注意点**: AIを一律に止めると、AIの検索や買い物の窓口から自社が見えなくなるおそれがあります。反対に、決済や会員ページまで通すと、不正利用や誤操作の責任の所在があいまいになります。ページの種類ごとに分けて決めるのが現実的です。
