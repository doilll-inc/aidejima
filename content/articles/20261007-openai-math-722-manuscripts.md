---
{
  "title": "OpenAIが未公開AIの数学論文722本を一挙公開、約4,000問に挑み1件あたり平均3時間",
  "description": "OpenAIは10月6日、未公開の社内AIが数学の未解決問題に取り組んだ論文722本をGitHubで公開した。約4,000問を出し、成果1件あたり平均3時間の計算を使った。数学者からは成果の量産が学問を損なうとの懸念も出ている。",
  "date": "2026-10-07T19:40:00+09:00",
  "updated": "2026-10-10T23:27:00+09:00",
  "category": "research",
  "tags": ["OpenAI", "openai/math", "数学", "論文", "安全性"],
  "summary": [
    "OpenAIは10月6日、未公開の社内AIが数学の未解決問題に取り組んだ論文722本を、372のテーマに分けてGitHubで公開した",
    "AIには約4,000問を出し、成果1件あたり平均3時間分を考えさせた。一部は計算機で正しさを自動確認できる形の証明も付いている",
    "9月にはフィールズ賞受賞者25人が「AIによる証明の量産は数学を損なう」と声明を出しており、査読前の大量公開に賛否が分かれている"
  ],
  "sources": [
    {"title": "openai/math README", "publisher": "OpenAI（GitHub）", "url": "https://github.com/openai/math", "kind": "公式ドキュメント"},
    {"title": "openai/math history.md", "publisher": "OpenAI（GitHub）", "url": "https://github.com/openai/math/blob/main/history.md", "kind": "公式ドキュメント"},
    {"title": "Dan Roberts の投稿", "publisher": "X @danintheory", "url": "https://x.com/danintheory/status/2108065033070789090", "kind": "X投稿"},
    {"title": "Terence Tao の投稿", "publisher": "Mathstodon @tao", "url": "https://mathstodon.xyz/@tao/117395268130901862", "kind": "コミュニティ"},
    {"title": "100+ reactions to 100+ solutions", "publisher": "Proofs and Prompts", "url": "https://proofsandprompts.com/2026/10/08/100-reactions-to-100-solutions/", "kind": "コミュニティ"},
    {"title": "Sharing AI progress in mathematics（議論）", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=49984923", "kind": "コミュニティ"},
    {"title": "OpenAI dumps 372 AI-generated math proofs on GitHub, telling the academic world to keep up", "publisher": "The Decoder", "url": "https://the-decoder.com/openai-dumps-372-ai-generated-math-proofs-on-github-telling-the-academic-world-to-keep-up/", "kind": "報道"},
    {"title": "25 Winners of Math's 'Nobel Prize' Decry the AI Invasion of Their Discipline", "publisher": "Scientific American", "url": "https://www.scientificamerican.com/article/25-winners-of-maths-nobel-prize-decry-the-ai-invasion-of-their-discipline/", "kind": "報道"},
    {"title": "AI May Have Solved a Longstanding Math Problem With a Million-Dollar Prize", "publisher": "Smithsonian Magazine", "url": "https://www.smithsonianmag.com/smart-news/ai-may-have-solved-a-longstanding-math-problem-with-a-million-dollar-prize-it-ignited-a-controversy-over-who-gets-credit-180989472/", "kind": "報道"},
    {"title": "\"How much beauty have we lost?\" Mathematicians react with shock and disgust as OpenAI bulldozes their field", "publisher": "The Decoder", "url": "https://the-decoder.com/how-much-beauty-have-we-lost-mathematicians-react-with-shock-and-disgust-as-openai-bulldozes-their-field/", "kind": "報道"},
    {"title": "OpenAI's math solutions aren't meeting the field's standards yet", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/10/08/openais-math-solutions-arent-meeting-the-fields-standards-yet/", "kind": "報道"}
  ],
  "thumb_text": "数学論文722本",
  "thumb_style": "photo",
  "thumb_prompt": "A university lecture hall at night where towering stacks of freshly printed math papers fill every seat, while a single chalkboard at the front still holds one half-finished equation written by hand.",
  "share_text": "OpenAIが未公開AIの数学論文722本を一挙公開。約4,000問に挑み、1件あたり平均3時間の計算",
  "editor_note": ""
}
---
OpenAIは現地時間10月6日、まだ一般公開していない社内のAIモデルが数学の未解決問題に取り組んだ論文722本を、GitHub上のリポジトリ「openai/math」で公開しました。AIに出した問題は約4,000問で、成果1件あたり平均3時間分の計算を使ったとしています。

## 何が公開されたか

openai/mathとは、OpenAIの社内モデルが書いた数学の原稿と、その証明を裏付ける資料をまとめた公開の保管庫です。722本の原稿は、主な結果と関連する補足や別証明をひとまとめにした372の「ファミリー」に分けられ、数学の分野ごとに分類されています。

公開の経緯について、OpenAIは説明文で次のように書いています。

:::quote https://github.com/openai/math | OpenAI「openai/math」README
> As part of model development, we evaluate our models on open research problems. We expanded these evaluations after performance on our existing mathematical evaluations saturated.
モデル開発の一環として、未解決の研究課題でモデルを評価している。既存の数学の評価ではモデルの成績が頭打ちになったため、この評価を広げた。
:::

つまり、これまでの数学の試験ではAIがほぼ満点を取るようになり、力を測れなくなったため、答えのわかっていない本物の研究課題を試験代わりに使い始めた、ということです。

手順はほぼ共通で、未公開のモデルに有料プラン「ChatGPT Pro」の考える機能で平均3時間ずつ取り組ませました。約4,000問の出力を、関連する結果ごとにまとめ、一定の重要度に届いたものだけを残した結果が今回の一覧です。例外として、素数の分布に関わるリーマンゼータ関数の研究など一部は別の手順で作られ、うち1本は読みやすさのために人が文章を手直ししたと明記しています。

10件については、AIがどう考えて答えにたどり着いたかの要約も添えました。円周率πの性質、物理学の磁石のモデル、計算の難しさを扱う理論など、分野は幅広くなっています。

## まだ「確定した成果」ではない

公開された結果は、検証の段階がばらばらです。一部には「Lean（リーン）」と呼ばれる証明支援ソフトで、計算機が論理の正しさを1行ずつ確かめられる形の証明が付いていますが、全部ではありません。OpenAI自身も説明文でこう断っています。

:::quote https://github.com/openai/math | OpenAI「openai/math」README
> Some of the unformalized results could have issues. We will endeavor to fix any such issues quickly.
計算機による検証用の形にしていない結果の一部には、問題があるかもしれない。そうした問題は速やかに直すよう努める。
:::

訂正や改訂は新しい版として記録し、以前の版も見られるように残す方針です。論文誌の査読（専門家による審査）を経た結果ではない点は、数字の大きさとは分けて受け止める必要があります。

## 背景

OpenAIは9月、流体の動きを表す「ナビエ–ストークス方程式」の難問を社内システムで解いたと発表しました。100万ドルの懸賞金がかかる7つの「ミレニアム懸賞問題」の1つで、約1万のAIエージェントを動かしたとSmithsonian Magazineなどが報じています。この件では、同じ問題に取り組んでいた人間の研究者の成果がAIの学習に使われていないかをめぐり、手柄の帰属が争点になったとも伝えられています。

その直後、数学のノーベル賞と呼ばれるフィールズ賞の受賞者25人が声明「A Severe Misalignment of AI in Mathematics」を出しました。Scientific Americanによると、声明は、数学者が大事にしているのは答えそのものより理解や洞察を深める過程だと強調し、AI企業と数学界では目指すものが大きく食い違っていると訴えています。テレンス・タオ氏も署名者の1人です。今回の722本は、その声明から1カ月足らずでの公開でした。

## 反応と論点

The Decoderは、OpenAIが著名な数学者らの助言グループと協議したものの、その役割は「結果をどう伝えるか」に限られ、公開するかどうかや速さは対象外だったと報じています。数学界からは、AIが一度に大量の結果を出すと、人間の研究者が確認しきれないという懸念が出ています。

開発者が集まる掲示板Hacker Newsでも投稿は900ポイントを超え、800件以上のコメントが付きました。人間なら数十年分の前進だと評価する声がある一方、博士課程の途中で同じテーマの論文を書いている学生はどうすればいいのかという戸惑いや、20年以上取り組んできた問題が一覧に「解決済み」として載っていたという投稿もありました。少なくとも人が目を通したことを示すため、確認者の名前を原稿に載せるべきだという提案も出ています。

成果の数そのものより、「誰が確かめるのか」「誰の手柄か」という研究の仕組みの問いが前に出てきた、というのが今回の一番の論点です。

## 追記（10月9日）

OpenAIは現地時間10月7日、公開した原稿のうち3本を取り下げました。リポジトリの更新履歴によると、「分裂アーベル8次元多様体上のWeil類の代数性」を扱う原稿で符号の誤りが見つかり、証明の要の議論が成り立たなくなりました。同じ構成を使っていた2本の原稿も、あわせて取り下げています。

ほかに14本で証明の修復や記述の訂正を行い、関連する13本の引用を更新しました。計算機で正しさを確かめられる形（Lean）の証明も6件増え、主な結果のうち形式化済みは719件中300件（約42%）になったとしています。取り下げた原稿は、理由の説明と保管版へのリンクを付けて残す方針です。

{{x:https://x.com/danintheory/status/2108065033070789090}}

OpenAIの研究者ダン・ロバーツ氏はXで、新しい形式化6件、修正19件、取り下げ3件を反映したと投稿し、今後も誤りが見つかれば更新を続けると書いています。

数学者側からは批判が続いています。フィールズ賞受賞者のテレンス・タオ氏はMastodonへの投稿で、AIに問題を解かせた人が結果を十分に理解しておらず、質問に答えたり講演したりできないまま「解決済み」になる例が多いと指摘しました。TechCrunchは、OpenAIが助言を受けた数学者グループの「未公開モデルで難問を試さない」という要請に今回の公開が沿っていないと報じています。公開から2日で3本が取り下げられたことは、「誰が確かめるのか」という論点を具体的な形で示した格好です。

## 追記（10月10日）

数学者が運営するブログ「Proofs and Prompts」は現地時間10月8日から、今回の公開への数学者の反応を募って1つのページに載せています。タイトルは「100件超の解決に100件超の反応」で、10日までに寄稿が追加され続けています。所属や肩書きは書かず、名前だけを添える形にしたと運営者は説明しています。

寄せられた声は、驚きや期待から、喪失感や怒りまでさまざまです。2022年のフィールズ賞受賞者ユーゴー・デュミニル＝コパン氏は、自分がこれまで講演や論文で挙げてきた主な未解決問題が1つ残らず一覧に載っていたと書き、「身動きが取れない」と心境を明かしました。同じページで、2018年に同賞を受けたペーター・ショルツェ氏は「数学はマラソンであって短距離走ではない」と書き、目標は人間が数学を理解することで、それには時間がかかると呼びかけています。

テレンス・タオ氏は、AIの証明には消化すれば実りのある新しい発想が含まれていると認めました。そのうえで、通常の大発見と違い、質問に答えたり講演したり学生を育てたりする人間がいないことに強い不満を示しています。大学院生や若手が時間をかけて進めてきた研究が一度の公開で乱されたことも問題視しました。ほかに、一覧の原稿の質にばらつきがあり、確かめるには何カ月もかかるとして、OpenAIのやり方が数学の共同体を壊しかねないと批判する声もあります。The Decoderはこのブログを紹介し、反応の多くが自分の仕事や若手研究者の将来への不安だったと報じています。

## 日本のビジネスへの影響

- **使えるか**: 公開された原稿と証明は誰でもGitHubで読めます。ただし成果を出したモデルは未公開で、いつ一般向けに出るかは示されていません。現時点では「この性能のAIを明日から仕事で使える」という話ではありません
- **誰にどう効くか**: 研究開発部門を持つメーカーや製薬、金融の数理担当者、大学と組む事業の企画担当者に関係があります。AIが「答えのない問い」に数時間かけて取り組み、検証可能な形で結果を出す使い方が、数学以外の研究にも広がる可能性があります
- **今すぐやれること**: 自社の研究や分析で「人が数日かけて検討している問い」を1つ選び、いま使える上位のAIに時間をかけて考えさせ、結果を担当者が検証する小さな試行をしてみてください
- **注意点**: OpenAI自身が一部の結果に誤りがありうると認めています。AIの出した結論は、検証の手段（計算機による確認や専門家の審査）とセットで扱い、そのまま社外の資料や意思決定に使わないことが大切です

AIに調べものや検討をさせるときのサービスの選び方は、[調べもの・リサーチに強いAIのおすすめ](/best/research/)にまとめています。
