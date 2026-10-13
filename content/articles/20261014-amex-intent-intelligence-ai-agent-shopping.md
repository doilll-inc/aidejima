---
{
  "title": "AIに買い物を任せても頼んでいない物は買わせない、米アメックスがカード側で止める仕組み",
  "description": "米American Expressが、AIが人の代わりに買い物をするときに、頼まれた範囲（店・予算・商品）を超える支払いを止める仕組みを公開した。米国の消費者の66%がAIに最安値探しを任せたいと答えたとAmexは調べている。",
  "date": "2026-10-14T01:35:00+09:00",
  "category": "marketing",
  "tags": ["American Express", "Intent Intelligence", "エージェント", "決済", "EC", "セキュリティ"],
  "summary": [
    "米American Expressが10月13日、AIが代わりに買い物をするときの不正や間違いを防ぐ仕組みを公開した",
    "買う前に「どの店で・いくらまで・何を」を本人に確認して記録し、その範囲でしか使えない使い捨てのカード情報をAIに渡す",
    "記録はあとで「AIが勝手に買った」と争いになったときの証拠にもなる。Amexは他社にも使ってもらう業界標準を目指す"
  ],
  "sources": [
    {"title": "Intent Intelligence: Building Trust in Agentic Commerce", "publisher": "American Express Technology", "url": "https://americanexpress.io/intent-intelligence-building-trust-in-agentic-commerce/", "kind": "公式発表"},
    {"title": "Amex introduces a framework to prevent AI agents from making unauthorized purchases", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/10/13/amex-introduces-a-framework-to-prevent-ai-agents-from-making-unauthorized-purchases/", "kind": "報道"},
    {"title": "AmEx's Next Step for Agentic Commerce Is a Framework; Forter's Agentic Verification Move", "publisher": "Digital Transactions", "url": "https://www.digitaltransactions.net/amexs-next-step-for-agentic-commerce-is-a-framework-forters-agentic-verification-move/", "kind": "報道"}
  ],
  "thumb_prompt": "A small friendly robot pushing a shopping cart down a supermarket aisle, stopped by a glowing translucent fence made of a handwritten shopping list, while it reaches for an expensive item that is not on the list.",
  "thumb_style": "illustration",
  "thumb_text": "Amex",
  "share_text": "AIに買い物を任せる時代の安全装置。米アメックスが、頼んだ範囲を超える支払いをカード側で止める仕組みを公開",
  "editor_note": ""
}
---
米American Express（アメックス）は現地時間10月13日、AIが人の代わりにネットで買い物をするときに、本人が頼んでいない支払いを止めるための仕組み「Intent Intelligence（インテント・インテリジェンス）」を公開しました。買う前に「どの店で・いくらまで・何を」を本人に確認して記録し、その範囲でしか使えないカード情報だけをAIに渡すのが柱です。Amexは他のカード会社や決済会社にも使ってもらい、業界の標準にしたい考えです。

## 何が発表されたか

Intent Intelligenceとは、利用者がAIに伝えた「買いたいもの」の条件を、支払いの前にカード会社へ届けて守らせる仕組みです。インテントは「意図」の意味で、ここでは本人が許可した買い物の範囲を指します。

Amexの技術ブログは、なぜ新しい仕組みが要るのかをこう説明しています。

:::quote https://americanexpress.io/intent-intelligence-building-trust-in-agentic-commerce/ | American Express Technology「Intent Intelligence: Building Trust in Agentic Commerce」
> A user may define what they want once, while an agent interprets those instructions, evaluates changing conditions, and ultimately executes a purchase on the user’s behalf. This requires a new model of establishing trust in the user, representing intent as clear boundaries, and enforcing those boundaries at execution.
利用者は欲しいものを一度伝えるだけで、あとはAIが指示を解釈し、状況の変化を見ながら、本人に代わって購入まで実行するかもしれません。そのためには、本人を確かめ、意図をはっきりした境界として表し、実行の時点でその境界を守らせる新しい仕組みが必要です。
:::

ブログによると、流れは大きく4段階です。

1. **条件を聞き取る**: AIが利用者の希望を「店・上限金額・期限・買う回数・商品の条件」といった決まった形のデータにまとめる。あいまいな点は聞き返す
2. **本人が承認する**: 利用者が本人確認（パスキーなど）をしたうえで、その条件にOKを出す
3. **「約束の証明」を発行する**: 承認された条件ごとに番号と証明書（電子的な札）を発行し、カード会社が事前にリスクを確かめる
4. **範囲内でしか使えないカード情報をAIに渡す**: AIは本物のカード番号ではなく、条件の範囲と期限の中でだけ使える専用のカード情報で支払う。1回きりか複数回かも選べる

TechCrunchの取材に応じたAmexのハンナ・ボジアン副社長（AIエージェントとの提携・戦略担当）は、たとえば「白のナイキのスニーカー、サイズ9」と頼まれたAIが別メーカーの靴を買おうとしたら、Amexが支払いを止められると説明したと報じられています。利用者は承認した条件を後から見直したり、取り消したりもできます。

この仕組みは、Amexが4月に出した開発者向けのツール一式「ACE（Agentic Commerce Experiences）」に組み込まれました。

## 背景

AIエージェント（目的を伝えると自分で調べて操作まで進めるAI）による買い物は、もう始まっています。Digital Transactionsによると、Amexは自社のネットワークで、AIを通じた買い物が週に数千件あると明らかにしました。TechCrunchによると、Amexの調査では米国の消費者の66%が今後12カ月でAIに最安値を探させたい、61%が商品のおすすめを頼みたいと答えています。

問題は、対話AIがときに思いがけない動きをすることです。頼んでいない色やサイズを選ぶ、別の店で買う、といった間違いが起きたとき、今のカードの仕組みには「本人が何を許可していたか」の記録がありません。Amexのブログは、本人が実際には許可していた買い物を「AIが勝手にやった」と言って取り消しを求める不正が増えるおそれも指摘しています。

条件をカード会社が支払いの前に受け取っておけば、間違いをその場で止められ、もめたときは記録で判断できます。ボジアン氏はDigital Transactionsに対し、この仕組みの狙いは機能を増やすことより、お客さまに主導権を持ち続けてもらうことにあると話しています。

## 反応と論点

TechCrunchによると、Amexは、他社の方式より取引の早い段階で本人の意図を確認する点を強みとしています。Amexはカードの国際的な技術標準を決める団体EMVCoで、AIによる買い物の作業部会の議長も務めていると報じられています。

一方で、現時点で決まっているのは設計図の公開までです。どの決済会社やAIの会社が採用するかは、Amexが協議中としているだけで具体名は出ていません。Digital Transactionsによると、Amex自身もこの仕組みは各社が実装するときの参考という位置づけだとしています。条件を聞き取る精度はAIのモデルによって変わり得るとも報じられており、最初の聞き取りを誤れば、正しく記録された「間違った注文」になる点は残ります。

同じ日には、不正対策の米Forterも、店側がAIの買い物客を確かめられる仕組みを発表しています。カード会社と店の双方で、AIの買い物に備える動きが並行して進んでいます。

## 日本のビジネスへの影響

**使えるか**: 今回はAmexの米国での設計公開で、日本での提供や日本のカード会社の採用は発表されていません。日本のAmex会員がすぐに使える機能ではありません。

**誰にどう効くか**: ネット通販を運営する事業者と、ECのマーケティング担当者に関係します。AIが人の代わりに店を選んで買う時代には、AIが読み取りやすい商品情報（価格・サイズ・色・在庫）を整えている店が選ばれやすくなります。AIが店のサイトを読む動きについては「[ChatGPTが答えの出典に選ぶサイトが変化](/news/20261013-chatgpt-citations-primary-sources-ahrefs/)」も参考になります。マーケティングでAIを使う道具の比較は「[マーケティングAIの選び方](/best/marketing/)」にまとめています。

**今すぐやれること**: 自社サイトの商品ページで、価格・サイズ・色・在庫がページの文章や表としてきちんと読める状態か確認してください。画像の中にだけ書いてある情報は、AIの買い物客には伝わりにくくなります。

**注意点**: AIによる買い物の決済ルールは、カード会社ごとに作られている途中です。どの方式が主流になるかはまだ決まっていないため、特定の方式に合わせた大きな投資は急がなくてよいでしょう。
