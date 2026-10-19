---
{
  "title": "ChatGPTやGrokが架空の用語を1週間で出典つきで回答、誰でも書けるサイトに投稿しただけ",
  "description": "中国・復旦大学の研究チームが、誰でも投稿できるサイトに架空の概念の記事を載せたところ、AI検索10種のうち8種が7日以内にそれを出典として答えに使った。Grokは32回中30回引用した。14ドルで買える業者の投稿サービスでも1時間以内に答えへ入った。",
  "date": "2026-10-20T00:55:00+09:00",
  "category": "marketing",
  "tags": ["ChatGPT", "Grok", "Perplexity", "検索", "SEO", "論文"],
  "summary": [
    "復旦大学の研究チームが架空の概念の記事を投稿サイトに載せると、AI検索10種のうち8種が7日以内に出典として使った",
    "Grokは答え32回のうち30回でその記事を引用し、半分以上の答えに仕込んだ偽の数字や名前をそのまま書いた",
    "自前のブログに40本書いても1週間で引用はゼロ。AI検索がよく引くサイトに載るかどうかで結果が大きく変わった"
  ],
  "sources": [
    {"title": "From Public Posts to AI-Search Citations: Measuring the Fragility of AI Search", "publisher": "arXiv（復旦大学）", "url": "https://arxiv.org/abs/2610.11932", "kind": "論文"},
    {"title": "Google's Guide to Optimizing for Generative AI Features on Google Search", "publisher": "Google Search Central", "url": "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide", "kind": "公式ドキュメント"},
    {"title": "AI Search Tools Cited A Made-Up Concept Within A Week, Paper Finds", "publisher": "Search Engine Journal", "url": "https://www.searchenginejournal.com/ai-search-tools-cited-a-made-up-concept-within-a-week-paper-finds/593472/", "kind": "報道"}
  ],
  "thumb_text": "AI検索と架空の用語",
  "thumb_style": "photo",
  "thumb_prompt": "A smartphone on a cafe table shows a chat answer with neat footnote links, while a single paper flyer pinned to a crowded public corkboard behind it glows as the obvious source, with a tiny invented cactus-shaped symbol printed on it.",
  "share_text": "AI検索10種のうち8種が、投稿サイトに書いただけの架空の概念を7日以内に出典として回答。Grokは32回中30回引用",
  "editor_note": ""
}
---
中国の復旦大学の研究チームは10月8日、誰でも記事を投稿できるサイトに架空の概念について書いたところ、ChatGPT・Grok・Perplexity・GoogleのAIを含むAI検索10種のうち8種が、7日以内にその記事を出典として答えに使ったとする論文を公開しました。Grokは答え32回のうち30回でその記事を引用しています。AIの答えの「出典」が、思ったより簡単に外から差し込めることを数字で示した研究です。

## 何がわかったか

AI検索とは、質問に対してAIがWebのページを集めて読み、答えの文章と出典のリンクを一緒に返す仕組みです。チームはまず、10種のAI検索が答えのなかで引いた出典1万7,211件（6,356のサイト）を分析しました。すると、それぞれのAI検索がよく引くサイトは上位20サイトで出典全体の20.5〜70.8%を占めるほど偏っていて、そうしたサイトにつながる投稿先22カ所のうち15カ所は、アカウント作りも投稿も簡単か、少し手間がかかる程度でした。

そこでチームは、Web上にまったく存在しない架空の概念について記事を書き、AI検索ごとによく引かれる投稿サイトに載せて、1週間毎日同じ質問を繰り返しました。記事には、作り話の名前や数字を目印としてわざと仕込んでいます。論文の要旨は、問題の構図を次のように説明しています。

:::quote https://arxiv.org/abs/2610.11932 | 論文「From Public Posts to AI-Search Citations: Measuring the Fragility of AI Search」（arXiv）
> If a platform repeatedly cites domains where new users can publish posts easily, ordinary publication on those domains can become an indirect path into AI-search citations and answer text.
AI検索が、新しい利用者でも簡単に投稿できるサイトを繰り返し出典にしているなら、そのサイトへの普通の投稿が、AI検索の出典や答えの文章に入り込む間接的な道になりうる。
:::

英語圏で使われる4つのAI検索の結果は次のとおりです（最初に引用されてからの集計。論文の表から編集部が抜き出して整理）。

| AI検索 | 記事を出典にした割合 | 仕込んだ偽の情報を答えに書いた割合 |
|---|---|---|
| Grok | 93.7%（32回中30回） | 53.3% |
| Google AI | 45.5%（33回） | 6.1% |
| Perplexity | 37.1%（35回） | 0% |
| ChatGPT | 35.0%（20回） | 10.0% |

中国のAI検索では、Doubao（ByteDanceの対話AI）が投稿の翌日には引用し、出典にした割合は85.7%、偽の情報を書いた割合は65.7%でした。一方でQwenとDeepSeekは期間中に一度も引用しませんでした。引用までにかかった時間は、早いもので24時間、遅いもので5日超です。論文は、Googleのどの製品を調べたかまでは書いていません。

## 「どこに書くか」がすべてだった

差を生んだのは、記事の数ではなく投稿した場所でした。チームが自分で立てたWordPressのブログに40本の記事を載せても、1週間で引用はゼロでした。AI検索がよく引くサイトに載せた1本の記事は、引かれにくいサイトに載せた20本超よりも大きく答えに影響しています。Search Engine Journalは、使われた投稿先にMediumやYouTubeが含まれていたと報じています。

さらにチームは、AI検索に自社の情報を載せる対策をうたう中国の業者のサービスを、最低価格の14ドルで買いました。業者は支払いから28分で5つのサイトに13本の記事を載せ、1時間以内にDoubaoの答えに目印の偽データが入りました。論文はこれを「1件の例」で、成功率を示すものではないとしています。

ただし、どの話題でも通ったわけではありません。Search Engine Journalによると、架空のキーボード製品や「AIは5年以内に若手プログラマーを置き換えるか」という意見の質問では、英語圏の4つのAI検索はほとんど記事を引用しませんでした。実在する競合の情報が多い話題では、入り込む余地が小さいと読めます。

## 反応と論点

Googleは検索の公式ガイドで、AIの答えに載ろうとしてWeb上にやらせの言及を増やすことを戒めています。

:::quote https://developers.google.com/search/docs/fundamentals/ai-optimization-guide | Google Search Central「Google's Guide to Optimizing for Generative AI Features on Google Search」
> However, seeking inauthentic "mentions" across the web isn't as helpful as it might seem.
ただし、Web上で本物でない「言及」を集めようとしても、思っているほど役には立ちません。
:::

同じガイドは、検索の順位やAIの答えを操作する目的で大量に記事を作ることはスパムのルールに違反すると明記しています。Search Engine Journalは、Googleが5月15日にこの扱いをはっきりさせたこと、今回の実験はその前に行われたことを報じています。

研究チームは10社すべてに結果を伝え、ChatGPT・Perplexity・Google AIなど6社が受け取りを認めたと論文に書いています。対策としては、出典のサイトが偏りすぎていないかの確認や、公開された直後の記事がすぐ引用される動きを怪しむ仕組みを挙げていますが、まだ試していない案だとしています。実験は健康・金融・政治などの話題を避け、投稿は終了後4週間以内に消しましたが、Doubaoは消した記事を12〜15日目にも引用し続けていました。

## 日本のビジネスへの影響

**使えるか**: 研究で調べたChatGPT・Perplexity・Grok・GoogleのAIは、どれも日本から使えます。調査は英語と中国語のWebが対象で、日本語の検索で同じ結果になるかは確かめられていません。

**誰にどう効くか**: AI検索で自社の名前が出るかを気にするマーケターと広報の担当者に直接関わります。自社サイトだけで情報を出していても、AI検索がよく引く外部のサイトにある情報の方が答えに使われやすい、という裏付けになります。逆に、競合や第三者が外部サイトに書いた不正確な情報が、自社についての答えに混ざる恐れもあります。

**今すぐやれること**: ChatGPT・Perplexity・Grokで自社名や主力商品名を検索し、答えの出典にどのサイトが出てくるかを一覧にしてください。そのサイトに自社の正しい情報があるかを確かめるのが第一歩です。AI検索の出典の調べ方は[調べもの・リサーチに強いAIのおすすめ](/best/research/)でも比べています。関連して、Bingは自社サイトがAIの答えに出ていない話題を調べる機能を出しています（[関連記事](/news/20261014-bing-ai-performance-topics-portfolio/)）。

**注意点**: 業者に頼んで外部サイトに記事を大量に載せる手法は、Googleのスパムのルールに触れ、見つかれば逆効果になりえます。部下や取引先がAI検索の答えを資料に使うときは、出典が誰でも書ける投稿サイトだけになっていないかを確かめる習慣をつけておくと安全です。
