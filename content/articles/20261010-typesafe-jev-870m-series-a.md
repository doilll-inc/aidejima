---
{
  "title": "公開から1カ月足らずで評価額75億ドル、文章を書かず「判断」だけするAI「Jev」の米TypeSafe",
  "description": "判断専用のAI「Jev」を開発する米TypeSafe AIが10月9日、評価額75億ドルで8億7,000万ドルを調達したと発表した。Jevの公開は9月で、同社は米大企業500社の3分の1が使っていると主張する。素早い追随や品質の主張には疑問の声もある。",
  "date": "2026-10-10T19:25:00+09:00",
  "category": "business",
  "tags": ["TypeSafe AI", "Jev", "資金調達", "判断モデル", "Andreessen Horowitz"],
  "summary": [
    "判断専用のAI「Jev」を作る米TypeSafe AIが、評価額75億ドルで8億7,000万ドルを調達したと10月9日に発表した",
    "Jevは文章を書かず「どれを選ぶか」を確率で返すAIで、料金は文章を書くAIより大幅に安い入力100万単位あたり0.042ドル",
    "同社は米大企業500社の3分の1が利用中と主張するが、他社が数日で同じ種類のAIを出し、優位が続くかには疑問の声もある"
  ],
  "sources": [
    {"title": "TypeSafe A raises Series AI", "publisher": "TypeSafe AI", "url": "https://typesafe.ai/blog/series-ai", "kind": "公式発表"},
    {"title": "Introducing System One Models & Jev", "publisher": "TypeSafe AI", "url": "https://typesafe.ai/blog/introducing-system-one-models-and-jev", "kind": "公式発表"},
    {"title": "Typesafe AI raises $870M at $7.5B", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=50023450", "kind": "コミュニティ"},
    {"title": "The maker of non-text AI model Jev valued at $7.5B just weeks after launch", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/10/09/the-maker-of-non-text-ai-model-jev-valued-at-7-5b-just-weeks-after-launch/", "kind": "報道"}
  ],
  "thumb_text": "Jev",
  "thumb_style": "photo",
  "thumb_prompt": "A tall glass office tower at dusk with a giant illuminated railway track switch lever installed on its rooftop, a lone silhouetted figure standing beside it about to pull it.",
  "share_text": "文章を書かず「どれを選ぶか」だけ答えるAI「Jev」の米TypeSafeが評価額75億ドルで8.7億ドル調達。公開から1カ月足らず",
  "editor_note": ""
}
---
文章を書かずに「どれを選ぶか」だけを答える判断専用のAI「Jev」を開発する米TypeSafe AIは現地時間10月9日、評価額75億ドルで8億7,000万ドル（シリーズA）を調達したと発表しました。米ベンチャーキャピタルのAndreessen Horowitz（a16z）が主導し、Sequoia Capitalなども加わりました。Jevの公開は9月で、1カ月足らずでの大型調達です。

## 何が発表されたか

TypeSafe AIの発表によると、今回の資金調達は次のとおりです。

| 項目 | 内容 |
|---|---|
| 調達額 | 8億7,000万ドル（シリーズA） |
| 評価額 | 75億ドル |
| 主導 | Andreessen Horowitz |
| 参加 | Sequoia Capital、既存株主のDCVC、個人投資家 |
| 取締役 | a16zのマーティン・カサド氏が就任 |

同社は、米フォーチュン500社（売上高上位500社）の3分の1がすでにJevを使っていると説明しています。集めた資金は、新しいモデルの開発、開発者向けの基盤の拡充、顧客から要望のある企業向け機能、採用に充てるとしています。

:::quote https://typesafe.ai/blog/series-ai | TypeSafe AI公式ブログ「TypeSafe A raises Series AI」
> We’ve saved customers millions of dollars in production already
すでに本番の業務で、顧客の費用を数百万ドル削減しています。
:::

ただし、利用企業の名前や削減額の内訳は示されていません。TechCrunchも、500社の3分の1という数字は同社の主張だと書き添えています。

## Jevとは何か

Jevとは、状況の説明と選択肢を受け取り、各選択肢を選ぶべき確率を返すAIモデルです。ChatGPTのように文章を書くのではなく、「この問い合わせはどの部署に回すか」「この取引は不審か」のような分類・振り分け・採点を、プログラムがそのまま使える形で答えます。同社はこれを「System One Model」（直感的に素早く判断するAI、という意味）と呼んでいます。

:::quote https://typesafe.ai/blog/introducing-system-one-models-and-jev | TypeSafe AI公式ブログ「Introducing System One Models & Jev」
> Think of Jev as a frontier-intelligence function call: unstructured state in, typed probabilistic decisions out.
Jevは、最先端の知能を部品として呼び出すものだと考えてください。整理されていない状況を入れると、決まった形の確率つきの判断が返ってきます。
:::

同社の公表値では、1回の応答は0.07〜0.5秒で、文章を書く最先端のAIの3〜329秒より大幅に速いとしています。料金は入力100万トークン（文字数の単位）あたり0.042ドルで、出力は無料です。一般的な対話AIの入力料金は100万トークンあたり0.2〜10ドルだと同社は比べています。ただし、速さの数字は自社の評価で、現実の効果としては上限に近い値だろうと同社自身が書いています。

{{card:https://typesafe.ai/blog/introducing-system-one-models-and-jev|Introducing System One Models & Jev|TypeSafe AI}}

## 背景

TechCrunchによると、TypeSafeは2024年に、OpenAIの研究者だったディオゴ・アルメイダ氏らが共同で創業しました。Jevは9月15日に公開され、すぐに話題になったと報じています。

Jevの公開後、同じ形式で使える判断専用のAIが相次いで登場しました。個人開発者やPostHogによる無料の公開版は[JeffとJeevesの記事](/news/20261001-jeff-jeeves-open-decision-models/)で、Cloudflareの「Clef」は[Clefの記事](/news/20261002-cloudflare-clef-amazon-strands-decider/)で紹介しています。米国の技術者が古文書の大量のふるい分けにJevを使い、5万9,000件の判定を約3ドルで済ませた例は[古文書400年分をAIで調べた記事](/news/20261010-antiquity-ai-archives-meteorite-eruptions/)にまとめました。

## 反応と論点

技術者の集まる掲示板Hacker Newsでは、発表の投稿に270件を超えるコメントが付きました。目立ったのは「優位は続くのか」という疑問です。同じ種類のモデルが数日で他社や個人から出てきたことを挙げ、「2年かけた秘密の開発が2週間でまねされた」と書き込んだ利用者もいました。AIへの不正な指示（プロンプトインジェクション）に強いという同社の主張についても、デモで簡単に破れたという報告が出ています。

一方で、安さ・速さ・決まった形の出力がそろっている点にこそ価値があると評価する声もありました。開発と売り込みの速さを評価する意見もあります。

## 日本のビジネスへの影響

- **使えるか**：Jevは早期提供（アーリーアクセス）の段階で、開発者がプログラムから呼び出すAPIとして提供されています。日本語での利用や日本向けの提供について、同社の発表に記載はありません
- **誰にどう効くか**：問い合わせの振り分け、不審な取引の判定、商品データの分類など、「選ぶだけ」の判断を毎日大量にこなしている企業の、業務システムや情報システムの担当者に関係します。文章を書くAIに同じ判断をさせている場合、費用と待ち時間を大きく下げられる可能性があります
- **今すぐやれること**：社内でAIに「はい・いいえ」や「AかBか」を答えさせている処理を洗い出し、件数と費用を把握しておくことです。Jevや無料の公開版を試す際の比較材料になります。AIを組み込むサービスの料金は[API比較ガイド](/best/api/)にまとめています
- **注意点**：利用企業数や速さの数字は同社の主張で、第三者の検証は出ていません。同じ形式の無料版や他社版も出ており、1社に絞り込むより、自社のデータで複数を比べてから選ぶほうが安全です
