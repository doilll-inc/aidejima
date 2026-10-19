---
{
  "title": "100字足らずの指示でAIが通販サイトに次々侵入、日本も主な標的に 1件あたり約5ドルとの試算",
  "description": "調査会社のNorForgeは10月19日、AIエージェントを使った攻撃者が米国・日本・オーストラリアのネット通販サイトなどを狙っていたと公表した。ロイターなどによると1,200超のサイトを試し、100社以上に侵入。1件の作業は平均約5ドルとNorForgeは試算する。",
  "date": "2026-10-20T04:35:00+09:00",
  "category": "policy",
  "tags": ["NorForge", "Cairn", "セキュリティ", "エージェント", "EC", "DeepSeek"],
  "summary": [
    "人の代わりに作業を進めるAIを使った攻撃者が、米国・日本・オーストラリアの通販サイトなどに侵入を試みていた",
    "調査会社NorForgeによると、1件の作業費は平均約5ドル、成功率は約1割。攻撃者の指示は中国語で100字足らずだったと報じられている",
    "攻撃者は操作画面をネットにさらしたままにしていて、そこから手口が丸見えになった。日本の小売店への侵入例も載っている"
  ],
  "sources": [
    {"title": "Inside Cairn", "publisher": "NorForge", "url": "https://norforge.com/blog/inside_cairn", "kind": "公式発表"},
    {"title": "AI agents broke into 100+ sites for one hacker at $50 each, researcher says", "publisher": "The Next Web", "url": "https://thenextweb.com/news/ai-agents-hacker-cairn-100-sites-deere-norforge", "kind": "報道"},
    {"title": "AI autonomous hacking targeted 1,200+ sites, breaching 100+ company websites", "publisher": "The Cryptonomist", "url": "https://en.cryptonomist.ch/2026/10/19/ai-autonomous-hacking-breaches/", "kind": "報道"},
    {"title": "A hacker broke into John Deere and SharkNinja with an army of AI agents", "publisher": "The Verge", "url": "https://www.theverge.com/ai-artificial-intelligence/1013643/ai-agents-hack-john-deere-shark-ninja-cummins", "kind": "報道"}
  ],
  "thumb_prompt": "A glowing online shop storefront rendered as a small glass building at night, with dozens of tiny identical robot figures quietly lining up at its back door holding keys, while the front door shows a calm open sign.",
  "thumb_style": "3d",
  "share_text": "100字足らずの指示でAIが通販サイトに次々侵入。日本も主な標的で、1件あたり約5ドルとの試算",
  "editor_note": ""
}
---
セキュリティ調査会社のNorForgeは現地時間10月19日、人の代わりに作業を進めるAI（AIエージェント）を使った攻撃者が、米国・日本・オーストラリアのネット通販サイトなどに侵入を試みていた、とする調査を公表しました。ロイター通信などによると、攻撃者は1,200を超えるサイトを狙い、100社以上のサイトに入り込んでいました。

## 何が起きたか

攻撃に使われたのは「Cairn」という無料公開のソフトです。本来はセキュリティの点検（わざと攻撃してみて弱点を探す作業）のために作られたもので、複数のAIエージェントが手分けして、狙ったサイトを調べ、弱点を探し、入り込もうとします。NorForgeは、このソフトの操作画面がパスワードもなくネットにさらされているものを20以上見つけ、中を見て攻撃の様子を突き止めました。

:::quote https://norforge.com/blog/inside_cairn | NorForge「Inside Cairn」
> It is clear that AI-driven frameworks are used to perform malicious actions.
AIで動く仕組みが悪意ある行為に使われていることは明らかだ。
:::

NorForgeは攻撃者をいくつかの集団に分けています。最も大きいのは中国語を使う集団で、操作画面14個、1,100件を超える攻撃作業が見つかりました。狙いは主に米国・日本・オーストラリアの通販サイトや決済の仕組みで、報告書には「日本の小売店への侵入」の流れを示した図も載っています。英語を使う別の集団は、クレジットカードや暗号資産の情報を盗むことを狙っていたとしています。

The Next Webによると、中国語の集団は、月の訪問数が20万〜150万程度の通販サイトを選んで攻撃していました。目的は、サイトに「アップローダー」と呼ばれる裏口を仕込み、あとからいつでも入れるようにすることです。NorForgeは実際に、大手の部品販売サイトでこの裏口が動いているのを確かめました。

## どれくらい安く、どれくらい人手がいらないのか

NorForgeの試算では、失敗したものも含めた1件の作業の費用は平均約5ドルです。うまくいった作業は、始めてから侵入するまで平均23時間弱かかり、成功率は約1割でした。

ロイター通信の取材に応じたNorForgeの研究者スノーレ・ファーゲルランド氏は、侵入に成功した1件あたりは約50ドル、全体で約5,000ドルと見積もったと報じられています。攻撃者がAIに渡した指示は中国語で100字足らずで、「サイトでプログラムを動かせる方法を探し、裏口を仕込め」という中身だったとされています。ファーゲルランド氏は、こうしたAIにはまだ人の見張りが必要だと思っていたと話し、進み方を「驚くべきもの」と表現しています。

作業を担当するAIには「claudecode_deepseek-v4.1-flash」という名前が付いていました。NorForgeは、プログラミングAIの「Claude Code」の仕組みで、中国DeepSeekの安いモデル「DeepSeek V4.1 Flash」を動かしていた可能性があるとしています。ただし推測で、AnthropicやDeepSeekが関わったことを示すものではありません。DeepSeekのこのモデルは、性能を上げて料金を据え置いたばかりです（[DeepSeekの格安AIが料金そのままで性能アップ](/news/20261019-deepseek-v4-1-flash-1017-update/)）。

## 被害を受けた会社とソフトの作者の話

ロイターは、被害を受けた会社として、米農機大手のディア（John Deere）、家電のSharkNinja、エンジン大手のカミンズを挙げていると報じられています。ディアは必要な対策を取り、重要な情報が見られた形跡はないと説明しました。SharkNinjaは、製品サポートの情報だけを載せた別のサイトが被害に遭い、すでに封じ込めたとしています。カミンズは、取引先が運営するサイトが攻撃された可能性を調べていると答えました。どれだけのデータが盗まれたかはわかっていません。

Cairnの作者は、ハッキング攻撃のために作ったものではなく、悪用は本意ではないとXで述べたと報じられています。

## 攻撃者の「うっかり」も明らかに

NorForgeは、攻撃者もこの技術を使いこなせていないと指摘しています。急いで成果を出そうとして操作画面を守らずに放置し、自分たちの手口をさらしただけでなく、盗んだパスワードや鍵まで画面に残していました。NorForgeが調べると数百件見つかり、うち約11%は実際に使えるものでした。正規のセキュリティ点検の会社も同じように画面を放置し、顧客の情報をさらしていた例があったといいます。NorForgeはロイターと協力して被害者に知らせ、サーバーの事業者に画面の停止を求めています。

## 日本のビジネスへの影響

- **関係あるか**: 日本は主な標的の1つと名指しされています。月の訪問数が数十万〜百数十万の中規模の通販サイトが狙われており、大企業だけの話ではありません
- **誰に効くか**: 自社の通販サイトを運営するEC担当者と、サイトの制作・保守を外部に任せている経営者です。カミンズの例のように、取引先が運営するサイトが入口になることもあります
- **今すぐやれること**: 通販サイトの制作会社や保守の担当者に、使っているソフトが最新か、見覚えのないファイルの「アップロード画面」がないかを確かめてもらうことです。古いソフトを使い続けている販促用の特設サイトや、使い終わったキャンペーンサイトは、閉じるのが手早い対策です
- **注意点**: 1件5ドル前後で試せるなら、攻撃の数はこれからも増えると考えるのが自然です。AIを使った攻撃の広がりについては、Anthropicも警告を出しています（[格安テレビ端末やスマート家電にAIが自分をコピーして広がる恐れ](/news/20261014-anthropic-self-replicating-ai-iot-devices/)）。自社でAIの点検ツールを使う場合も、その操作画面をネットにさらさないよう注意が必要です
