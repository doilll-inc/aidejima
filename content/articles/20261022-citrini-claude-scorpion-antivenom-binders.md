---
{
  "title": "科学の素人がClaudeにサソリの解毒薬の設計を任せた、64時間で211候補 毒に結合したのは17個",
  "description": "米投資調査会社Citrini Researchの5人が、Anthropicの社内モデルのClaudeにサソリ毒を抑えるタンパク質を設計させた。人が送った指示は最初の180候補でわずか5通。実験で毒にくっついたのは211個中17個で、毒を無力化できるかはまだ試していない。",
  "date": "2026-10-22T23:15:00+09:00",
  "category": "usecases",
  "tags": ["Claude", "Claude Science", "Citrini Research", "Anthropic", "活用事例", "医療"],
  "summary": [
    "生物学の専門家でない米投資調査会社の5人が、Claudeにサソリの毒を抑えるタンパク質の設計を任せた",
    "Claudeは64時間で約32万個を設計して候補を絞り、外部の実験会社で試した211個のうち17個が毒にくっついた",
    "毒を無力化できるかは未検証で、Anthropic自身も「解毒薬を作ったとは主張しない」としている"
  ],
  "sources": [
    {"title": "How Claude designed protein binders against scorpion neurotoxins", "publisher": "Anthropic", "url": "https://www.anthropic.com/research/claude-scorpion-toxin-binder-design", "kind": "公式発表"},
    {"title": "Citrini Therapeutics（We Wanted to Use Claude to Create a New Drug）", "publisher": "Citrini Research", "url": "https://www.citriniresearch.com/p/citrini-therapeutics", "kind": "公式サイト"},
    {"title": "Claude did not invent scorpion antivenom", "publisher": "The Verge", "url": "https://www.theverge.com/ai-artificial-intelligence/1016443/anthropic-claude-citrini-vibecoding-scorpion-antivenom", "kind": "報道"}
  ],
  "thumb_prompt": "A tiny glossy scorpion on a laboratory bench facing a row of colorful miniature protein models that look like puzzle pieces, while a laptop beside them shows hundreds of tiny glowing tiles being sorted overnight.",
  "thumb_style": "3d",
  "thumb_text": "Claude×サソリ毒",
  "share_text": "科学の素人5人がClaudeにサソリの解毒薬の候補づくりを任せた。指示は5通、211候補のうち17個が毒に結合",
  "editor_note": ""
}
---
米国の投資調査会社Citrini Researchは現地時間10月20日、生物学の専門家ではない社員5人が、AnthropicのClaudeにサソリの毒を抑えるタンパク質の設計を任せた実験の結果を公表しました。Claudeは64時間で候補を絞り込み、外部の実験会社で試した211個のうち17個が狙った毒にくっつきました。同じ日にAnthropicも技術的な報告を公開しましたが、毒を無力化できるかはまだ試しておらず、「解毒薬を作ったとは主張しない」としています。

## 何をしたのか

挑戦したのは、株式の調査を本業とする会社です。Citriniのブログによると、参加した5人のうち3人は科学の素養がまったくなく、残る2人も新薬開発の経験はほとんどありませんでした。「AIで創薬が本当に変わったのか」を投資判断のために確かめようと、20万ドルの予算を組んで自分たちで試すことにしたといいます。

題材に選んだのは、サソリの毒の成分にくっついて働きを邪魔する小さなタンパク質（ミニバインダー）です。Anthropicによると、サソリには毎年120万人以上が刺され、3,250人以上が亡くなっています。多くは医療が届きにくい地域の子どもです。いまの解毒薬は、サソリから採った毒を馬に注射してできた抗体を精製して作るため、手間と費用がかかります。

## どう作ったか

最初はつまずきました。Citriniが自社で用意した環境で頼むと、Claudeは生物兵器への悪用を防ぐ安全装置に止められました。そこでAnthropicの研究チームと組み、Anthropicの社内で、一般には公開されていない研究用モデルを使って作業しました。使ったのは、Claudeに科学研究をさせる環境「Claude Science」です。

指示文は約35ページにのぼり、そのほとんどもClaudeと一緒に書いたといいます。指示を出してからの動きは次のとおりです。

- 最初の一晩で、Claudeは300を超える下請けのAIを立ち上げ、300台超のGPU（AIの計算に使う半導体）を同時に動かした
- 12種類の設計ツールを使い分けて318,484個のタンパク質を設計し、毒との組み合わせ553,052通りの形を予測して絞り込んだ
- 64時間後に180個の候補を選び、実験会社への発注に必要な仕様書と報告書までまとめた。作れる形式を確かめるため、実験会社の担当者にメールで質問もした

人の出番がどれだけ少なかったかを、Citriniはこう書いています。

:::quote https://www.citriniresearch.com/p/citrini-therapeutics | Citrini Research「Citrini Therapeutics」
> In total, the entirety of the design process that produced the original 180 designs involved a total of five messages sent by humans to Claude.
最初の180個の設計を生んだ工程全体で、人がClaudeに送ったメッセージは合計5通でした。
:::

その後の追加の指示を含めても、Claudeに送ったメッセージは367通です。費用はAIの計算に49,997ドル、実験会社2社への支払いが15万ドル弱でした。計算量はおよそ1万GPU時間で、Anthropicも計算費用の一部を負担しています。

## 成果と限界

追加分を足した211個を、実験会社のAdaptyv BioとTwist Bioscienceの2社がそれぞれ作って試しました。両社の測定でそろって基準を満たし、狙った毒にくっついたのは17個です。5種類の毒のうち4種類に対して結合するものが見つかりました。1種類の毒だけを狙った60個に限ると11個が成功で、Anthropicはこの割合を一般的なタンパク質設計と同程度としています。

いちばん良かった2つは、メキシコのサソリの毒に強く結合しました。既存の抗体と同じ場所にくっついているとみられ、毒を無力化できる可能性があります。一方、1つで5種類すべての毒に効く「万能型」は、Claude自身が事前に「失敗する可能性が高い」と警告したとおり、1つも成功しませんでした。

最大の限界は、毒を本当に無力化できるかをまだ試していないことです。Anthropicは報告の中でこう明言しています。

:::quote https://www.anthropic.com/research/claude-scorpion-toxin-binder-design | Anthropic「How Claude designed protein binders against scorpion neurotoxins」
> We have not confirmed whether these binders neutralize scorpion venom in a cellular environment, so we do not claim to have produced an antivenom.
これらのタンパク質が細胞の環境でサソリ毒を無力化するかは確かめていません。そのため、解毒薬を作ったとは主張しません。
:::

AnthropicとCitriniは、211個すべての設計と測定データを研究者向けに無料で公開しました。

## 反応と論点

Anthropicが意見を求めた外部の研究者2人は、有望な第一歩だと評価しています。そのうち1人は、狙った物にくっつくタンパク質を作ること自体はもう難しくなく、安全で安い薬に仕上げる工程こそが課題だと述べています。

厳しい見方もあります。The Vergeは「Claude did not invent scorpion antivenom」（Claudeはサソリの解毒薬を発明していない）という見出しで報じました。有望な出発点ではあるものの、実際の薬からはほど遠いと専門家が話していると伝えています。The Vergeはまた、Anthropicが株式上場を控え、創薬や生命科学でのAIの可能性を宣伝したい立場にあることにも触れました。Citrini自身も、ブログの後半は有料会員向けの投資銘柄の解説につながっています。

Claudeに研究を任せる事例としては、天文学のデータから新しい星空の地図を作った例もあります（[Claude Scienceの天文学の記事](/news/20261009-claude-science-ultraviolet-sky-map/)）。今回はそれを、専門知識のない人が実験室の外注まで含めて動かした点が新しいところです。

## 日本のビジネスへの影響

- **使えるか**: 今回使われた社内の研究用モデルは一般には公開されていません。生命科学の研究で高度な機能を使うには、Anthropicの審査を受けた専門機関である必要があります。一般の利用者が同じことをそのまま再現することはできません
- **誰にどう効くか**: 直接関係するのは、製薬・素材・食品などで研究開発を持つ企業や、その分野への投資を判断する金融・調査の担当者です。「AIが下調べや設計の試作をどこまで肩代わりできるか」を、自社の研究テーマで見積もる材料になります
- **今すぐやれること**: 研究部門を持つ企業なら、時間のかかる文献調査や候補の絞り込みのうち、どの工程をAIに任せられそうかを棚卸ししておくとよいです。ただし今回のように外部の実験や専門家の検証が前提で、AIの出した候補をそのまま成果とは扱えません
- **注意点**: 「AIが解毒薬を作った」という受け取り方は誤りです。実験でわかったのは毒にくっつくことまでで、薬として効くか・安全かはこれからの検証次第です。社内外への発信では、AIの成果を実際より大きく見せないことが信頼につながります
