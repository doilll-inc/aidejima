---
{
  "title": "ChatGPTが答えの出典に選ぶサイトが変化、まとめ記事より公的機関やメーカー公式を優先 米Ahrefs調査",
  "description": "米Ahrefsの調査で、ChatGPTが答えの出典に挙げるサイトが「まとめ・解説サイト」から「情報を最初に出した側」へ移っていた。医学論文データベースのPubMedは64位から4位に上がり、Redditを出典にする答えは半年で88%減った。",
  "date": "2026-10-13T06:50:00+09:00",
  "category": "marketing",
  "tags": ["ChatGPT", "Ahrefs", "SEO", "検索", "マーケティング"],
  "summary": [
    "米Ahrefsの調査で、ChatGPTが答えの出典に挙げるサイトが、まとめ・解説サイトから公的機関や企業の公式サイトへ移っていた（米国、3月と9月の比較）",
    "医学論文のデータベースPubMedは出典の多いサイトで64位から4位に上昇し、Redditを出典にした答えは5回に1回から43回に1回へ減った",
    "ChatGPTが裏で調べる言葉には「公式」「価格」が増えており、自社サイトに価格や仕様をはっきり書くことが答えに載る近道になっている"
  ],
  "sources": [
    {"title": "How ChatGPT Does Query Fan-Out (15 Million Queries Studied)", "publisher": "Ahrefs", "url": "https://ahrefs.com/blog/query-fan-out-chatgpt/", "kind": "公式サイト"},
    {"title": "ChatGPT search", "publisher": "OpenAI Help Center", "url": "https://help.openai.com/en/articles/9237897-chatgpt-search", "kind": "公式ドキュメント"},
    {"title": "ChatGPT’s Most-Cited Sites Tilt Toward Primary Sources, Data Shows", "publisher": "Search Engine Journal", "url": "https://www.searchenginejournal.com/chatgpt-most-cited-sites-primary-sources-ahrefs/592682/", "kind": "報道"}
  ],
  "thumb_text": "ChatGPTの出典",
  "thumb_style": "3d",
  "thumb_prompt": "A tall stack of glossy summary magazines toppling over on a library table while a small, plain government report and a lab notebook glow under a spotlight, with a giant magnifying glass hovering over them.",
  "share_text": "ChatGPTが出典に選ぶサイトが「まとめ」から「一次情報」へ。PubMedは64位→4位、Redditの引用は半年で88%減",
  "editor_note": ""
}
---
ChatGPTが答えの根拠として示すサイトが、要点をまとめた解説サイトから、情報を最初に出した公的機関や企業の公式サイトへ移っています。SEO（検索エンジン対策）の分析ツールを提供する米Ahrefsが現地時間10月12日に公表した調査で、医学論文のデータベース「PubMed」は米国のChatGPTが出典に挙げるサイトの順位で3月の64位から9月には4位に上がりました。

## 調査で何がわかったか

Ahrefsは2種類のデータを使っています。1つは、米国のChatGPTの答えに付いた出典の集計で、3月は約240万件、9月は約380万件の答えが対象です。もう1つは、ログインしていない無料版のChatGPT（モデルはGPT-5.6 Luna）の答え6,660万件と、そのときChatGPTが裏で走らせた検索約1,500万回の分析です（8月と9月、全世界）。

出典の順位で上がったのは、PubMedのほか、米食品医薬品局（FDA。9月に8位で新たに上位入り）、米疾病対策センター（CDC）、米証券取引委員会（SEC）などの公的機関と、製品を実際に試して評価するサイトでした。下がったのは、WebMDやVerywell Healthのような医療の解説サイト、投資用語の解説で知られるInvestopediaなど、他人の調べた内容をわかりやすくまとめるタイプのサイトです。

:::quote https://ahrefs.com/blog/query-fan-out-chatgpt/ | Ahrefs「How ChatGPT Does Query Fan-Out (15 Million Queries Studied)」
> ChatGPT seems to be moving from sites that summarize information to the sources that produce it.
ChatGPTは、情報をまとめたサイトから、その情報を生み出した側へと移りつつあるようだ。
:::

これまで出典の定番だったSNSや百科事典も大きく減りました。

| 出典にしたサイト | 3月 | 9月下旬 |
|---|---|---|
| Reddit（米国の大型掲示板） | 約5回に1回 | 約43回に1回（88%減） |
| Wikipedia | 約7回に1回 | 約35回に1回（80%減） |
| YouTube | 約370回に1回 | 約500回に1回（27%減） |

Ahrefsは、新しい質問が集計に加わったことによる見かけの変化ではないかを確かめるため、両方の月に共通する約2万5,000件の質問だけでも比べ、表の各サイトが同じ方向に動いていたとしています。

## ChatGPTは裏で何を調べているか

意外なことに、ChatGPTはほとんどの質問でウェブを調べていません。無料版の答え6,660万件のうち、ウェブ検索をしたのは14.4%（およそ7回に1回）でした。検索した場合も、1回の答えにつき平均約1.6回です。

検索の中身を見ると、公式情報を探す傾向がはっきり出ています。特定のサイトの中だけを調べる検索のうち、よく使われる約160サイトに向けたものの75.9%は、apple.comやikea.comのようなメーカー・ブランドの公式サイトでした。検索語に「official（公式）」が入る割合は8月の10.1%から9月は13.1%に、「price（価格）」は6.0%から8.9%に増えています。

別に行った米国の2万件の質問のテストでは、価格・機能・会社の情報を尋ねる質問の84.4%で、少なくとも1つの公式サイトが出典に入りました。一方、「AとBのどちらが安いか」のような比較の質問では68.3%に下がり、出典の半分以上は公式以外のサイトでした。

一方で、OpenAIとコンテンツの利用契約を結んだ報道機関などの記事は、出典に占める割合が3月の7.5%から7月に15.8%へ倍増し、9月下旬も12.5%を保っていました。ChatGPTの検索の仕組みは、OpenAIのヘルプページで説明されています。

{{card:https://help.openai.com/en/articles/9237897-chatgpt-search|ChatGPT search|OpenAI Help Center}}

## 数字の読み方と限界

この調査はAhrefs自身の質問セットに基づくもので、時期によって質問の中身が入れ替わるため、順位の変化の一部は質問の違いによる可能性があるとSearch Engine Journalは指摘しています。また、出典の順位はそのサイトにどれだけ人が流れたかを示すものではありません。無料・未ログインでの利用は、有料版や考える時間の長いモデルより検索の回数が少ないともAhrefsは書いています。

Ahrefs自身も、次のモデル更新でこの傾向はまた変わりうると注意を促しています。Redditの出典が8月に急減したことは別の調査会社も報告しており、ChatGPTの出典の選び方はこの数カ月で何度も変わっています。

## 日本のビジネスへの影響

- **使えるか**: 出典の順位は米国のChatGPTの集計で、日本語の質問で同じ順位の変化が起きているかは示されていません。ただ、裏で走る検索の分析（公式サイトを直接調べる割合など）は全世界の無料版の答えが対象で、日本の利用者の質問も含まれます。
- **誰にどう効くか**: 影響が大きいのは、自社サイトを管理するマーケターと、比較・まとめ記事で集客してきたメディアの運営者です。ChatGPTに製品の価格を聞かれたとき、まとめサイトではなくメーカーの公式ページが出典になる場面が増えています。
- **今すぐやれること**: 自社の製品ページに、価格・仕様・対応地域を画像ではなく文字ではっきり書いているか確かめてください。そのうえで「（自社製品名） 価格」をChatGPTに聞き、どのサイトが出典に出るかを月に1回記録しておくと変化に気づけます。
- **注意点**: 他社の情報をまとめただけのページは、出典から外れやすくなっています。比較の質問では今も第三者の評価サイトが多く使われるため、公式ページだけでなく、外部の評価や報道に取り上げてもらう努力も欠かせません。AIの検索で選ばれる施策の全体像は[マーケティング向けAIのガイド](/best/marketing/)にもまとめています。Google検索側の変化は[Google検索で会社名を調べるとAIの要約が先頭に、米国の調査で9月に急増](/news/20261010-google-ai-overviews-brand-searches-surge/)で取り上げました。
