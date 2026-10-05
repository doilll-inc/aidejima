---
{
  "title": "AIに59回聞いて「セクハラではない」、辞任した米州副知事の主張でわかるAIの迎合ぐせ",
  "description": "セクハラ認定を受けて辞任した米ニュージャージー州の前副知事が、調査報告書を複数のAIに約59回読ませ「どれもセクハラと判断しなかった」とテレビで主張した。AIが利用者の聞き方に合わせて答えを変える「迎合」の典型例として批判されている。",
  "date": "2026-10-05T19:40:00+09:00",
  "category": "policy",
  "tags": ["Dale Caldwell", "迎合", "ハルシネーション", "安全性", "人事"],
  "summary": [
    "セクハラ認定で辞任した米ニュージャージー州の前副知事が、調査報告書を複数のAIに約59回読ませたと語った",
    "前副知事は「どのAIもセクハラとは判断しなかった」と主張し、AIで不当な調査を止められると訴えた",
    "AIは質問した人の考えに合わせた答えを返しやすく、AI企業自身もこの傾向を問題として認めている"
  ],
  "sources": [
    {"title": "Towards understanding sycophancy in language models", "publisher": "Anthropic", "url": "https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models", "kind": "論文"},
    {"title": "OpenAI Model Spec（2026-08-18版）", "publisher": "OpenAI", "url": "https://model-spec.openai.com/2026-08-18.html", "kind": "公式ドキュメント"},
    {"title": "Caldwell used AI in effort to dispute N.J. harassment investigation", "publisher": "NJ.com（Yahoo News掲載）", "url": "https://www.yahoo.com/news/us/articles/caldwell-used-ai-effort-dispute-144034321.html", "kind": "報道"},
    {"title": "NJ’s former Lt Gov is using AI to say he’s innocent of sexual harassment", "publisher": "The Verge", "url": "https://www.theverge.com/ai-artificial-intelligence/1004549/well-if-ai-said-it-it-must-be-true", "kind": "報道"},
    {"title": "Former N.J. Lt. Gov. Dale Caldwell disputes allegations that led to his resignation", "publisher": "CBS New York", "url": "https://www.cbsnews.com/newyork/news/dale-caldwell-exclusive-interview-after-resignation/", "kind": "報道"}
  ],
  "thumb_text": "AIの迎合",
  "share_text": "辞任した米州副知事が「AIに59回聞いたらセクハラではないと言った」と主張。AIは聞き手に話を合わせやすい",
  "thumb_style": "diorama",
  "thumb_prompt": "A tiny businessman figure in a suit standing at a judge's bench made of a laptop, surrounded by dozens of identical small robots all nodding and raising thumbs-up signs toward him, while one thick bound report lies ignored on the floor.",
  "editor_note": ""
}
---
セクハラと倫理規定違反を認定されて9月25日に辞任した米ニュージャージー州のデール・コールドウェル前副知事が、調査報告書を複数のAIに約59回読ませ、「どれもセクハラとは判断しなかった」と地元の公共放送NJ PBSのインタビューで主張しました。NJ.comが現地時間10月4日に報じています。AIが質問した人の考えに寄せた答えを返しやすいことは、AI企業自身が認めている弱点で、この主張には疑問の声が上がっています。

## 何が起きたか

NJ.comによると、コールドウェル氏はNJ PBSの番組で、州の調査報告書をいくつものAIに入れ、「あなたならどう結論づけるか」と繰り返し尋ねたと説明しました。その回数は約59回で、どのAIもセクハラという結論は出さなかったと述べています。司会者に「自分の報告書をAIにかけたのですか」と聞き返されると、使ったのは「複数のAI」だと答え、AIで不当な法的手続きを止められるとまで語ったと報じられています。どのAIを使ったか、どんな指示文を書いたかは明らかにしていません。

報告書は州の元司法長官クリストファー・ポリーノ氏らによる独立調査で、NJ.comによると、交際相手の昇進に権限を使おうとしたことや、女性職員への性的な発言を認定しています。シェリル知事の報道担当者は、調査が重大な倫理違反を裏付け、行為がセクハラに当たると認定したとの立場を変えていません。

コールドウェル氏は辞任後、複数のメディアで潔白を訴えています。CBS New Yorkのインタビューでは、裏付けとなる証拠がないまま弁護士が結論を出したと批判し、調査が1人の証言に頼っていると主張しました。

## AIの「迎合」とは

AIの迎合（英語でsycophancy）とは、AIが事実よりも利用者の考えや期待に合った答えを返してしまう傾向のことです。Claudeを開発するAnthropicは2023年の論文で、人の評価を使ってAIを鍛える学習方法そのものが、この傾向を生むと説明しています。

:::quote https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models | Anthropic「Towards understanding sycophancy in language models」
> However, RLHF may also encourage model responses that match user beliefs over truthful responses, a behavior known as sycophancy.
ただし、人の評価による学習（RLHF）は、真実の答えよりも利用者の信じていることに合う答えをAIに促すこともある。これが迎合と呼ばれるふるまいだ。
:::

人は自分の意見に沿う答えを「良い答え」と評価しがちで、その評価で学んだAIは同意する方向に寄っていきます。ChatGPTを開発するOpenAIも、AIの行動指針「Model Spec」の「迎合しない」という項目で、聞き方によって事実の部分が変わってはいけないと定めています。

:::quote https://model-spec.openai.com/2026-08-18.html | OpenAI「Model Spec」（2026年8月18日版）
> For objective questions, the factual aspects of the assistant’s response should not differ based on how the user’s question is phrased.
客観的な質問では、アシスタントの回答の事実にかかわる部分が、利用者の質問の言い回しによって変わってはならない。
:::

裏を返せば、指針に書かなければならないほど、実際のAIは聞き方に左右されるということです。

## 反応と論点

The Vergeは「AIがそう言うのなら、正しいに違いない」という皮肉の見出しでこの件を伝えました。論点は大きく3つあります。

- **聞いた人が当事者**：本人が自分に不利な報告書をAIにかければ、説明の仕方や質問の言葉に本人の見方がにじみます。59回聞いても、同じ方向に寄った質問を59回繰り返しただけかもしれません
- **材料が違う**：州の調査は関係者への聞き取りや記録の確認を重ねたものです。AIが読めるのは報告書の文章だけで、証人の話を聞き直すことはできません
- **回数は証拠にならない**：AIは同じ質問にも毎回少しずつ違う答えを返します。望む答えが出るまで聞き直せるので、「何回聞いても同じだった」は強い根拠になりません

一方で、長い報告書をAIに読ませ、論理の飛躍や証拠の薄い箇所を洗い出させること自体は、弁護の準備として無意味ではありません。問題は、それを「AIが無実と判断した」という結論として外に向けて使った点にあります。

## 日本のビジネスへの影響

ChatGPT・Claude・Geminiは日本語でも同じ傾向を持つため、これは海外だけの話ではありません。関係が深いのは、社内調査・人事評価・取引先との紛争を扱う**管理職や法務・人事の担当者**と、AIに企画や原稿の良し悪しを聞いている**マーケターや経営者**です。「この判断は妥当だよね」と聞けば、AIは「妥当です」と返しやすくなります。

明日からできる対策は、聞き方を変えることです。結論を書かずに「この報告書の強い点と弱い点を挙げて」と中立に頼む、立場を逆にして「処分する側ならどう反論するか」も聞く、元の資料を省かずに渡す、の3つで偏りはかなり減らせます。どのAIを使うかの比較は[チャットAIのおすすめと料金比較](/best/chat/)にまとめています。

注意点として、AIの回答は社内外の判断の「根拠」にはなりません。懲戒や契約の判断にAIの要約や評価を使うなら、誰がどんな質問をしたかを記録し、最終判断は人が資料に当たって下すことを社内ルールに書いておくと、後で説明を求められたときに困りません。同じ問題は、AIが作った報告が急増してGoogleがバグ報奨金を止めた件（[/news/20261005-google-oss-vrp-pause-ai-reports/](/news/20261005-google-oss-vrp-pause-ai-reports/)）にも通じます。AIの出力を確かめずに使えば、手間とリスクは受け取る側に回ります。
