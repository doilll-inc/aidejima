---
{
  "title": "知られていなかったWebページ数億件がChatGPTの検索に、CloudflareとOpenAIが試験結果を公表",
  "description": "CloudflareとOpenAIが、Cloudflareの通信の情報を手がかりにChatGPTの検索が新しいWebページを見つける共同試験の途中結果を公表した。Cloudflare全体の約1%のサイトで試し、数億件のページが新たにOpenAIの検索の索引に入った。",
  "date": "2026-10-15T23:40:00+09:00",
  "category": "marketing",
  "tags": ["Cloudflare", "ChatGPT", "OpenAI", "SEO", "検索", "マーケティング"],
  "summary": [
    "CloudflareとOpenAIが10月15日、ChatGPTの検索が新しいWebページを見つけやすくする共同試験の途中結果を公表した",
    "Cloudflareを使うサイト全体の約1%で試したところ、OpenAIがこれまで知らなかったWebページを数億件見つけて検索の索引に入れた",
    "他サイトからリンクされていないページも見つかりやすくなる。ページの中身はAIの学習には渡さず、ページの所在などの情報だけを使う"
  ],
  "sources": [
    {"title": "Cloudflare and OpenAI: making AI discovery better for everyone", "publisher": "Cloudflare", "url": "https://blog.cloudflare.com/cloudflare-openai-discovery-agentic-web/", "kind": "公式発表"},
    {"title": "Cloudflare spent a year blocking AI crawlers. Now it's helping OpenAI index the web", "publisher": "The Next Web", "url": "https://thenextweb.com/news/cloudflare-openai-research-pilot-ai-search", "kind": "報道"}
  ],
  "thumb_prompt": "A lighthouse beam sweeping across a dark sea of thousands of tiny floating paper web pages, lighting up a few small handwritten manuals and restaurant menus that had been drifting unseen, while a small rowboat with a magnifying glass gathers them.",
  "thumb_style": "illustration",
  "thumb_text": "ChatGPT検索",
  "share_text": "ChatGPTが知らなかったWebページ数億件を発見。CloudflareとOpenAIが、通信の情報を手がかりにする共同試験の結果を公表",
  "editor_note": ""
}
---
Webサイトの通信を中継する米Cloudflareと、ChatGPTを開発するOpenAIは現地時間10月15日、ChatGPTの検索が新しいWebページを見つけやすくするための共同試験の途中結果を公表しました。Cloudflareを使うサイト全体の約1%で試したところ、OpenAIはこれまで知らなかったWebページを数億件見つけ、検索の索引（AIが答えを探すときに参照するページの一覧）に加えたといいます。

## 何が起きたか

Cloudflareは、世界の多くのWebサイトの手前に立って通信を中継し、攻撃から守ったり表示を速くしたりしている会社です。そのため、どのページが新しくできたか、いつ更新されたかを、通信の流れから知ることができます。両社は7月にこの共同試験を始め、Cloudflareが持つこうした「手がかり」で、OpenAIの検索用の巡回プログラム（クローラー）が有用なページにたどり着けるかを試してきました。

ブログはCloudflareの担当者2人とOpenAIの担当者2人の連名で、役割分担をこう説明しています。Cloudflareは「このページがある」「更新された」という手がかりを渡すだけで、そのページをChatGPTの答えでどう扱うかは、OpenAIが関連性や役立ち度から独自に判断します。

:::quote https://blog.cloudflare.com/cloudflare-openai-discovery-agentic-web/ | Cloudflare公式ブログ「Cloudflare and OpenAI: making AI discovery better for everyone」
> This joint pilot, which used a participating cohort of ~1% of Cloudflare's total network, has enabled OpenAI to discover and index hundreds of millions of new web pages, helping people discover more useful content and get more questions answered through ChatGPT.
Cloudflareのネットワーク全体の約1%が参加したこの共同試験で、OpenAIは数億件の新しいWebページを発見して索引に加えられました。人々がより役立つ情報を見つけ、ChatGPTでより多くの質問に答えが得られるようになっています。
:::

ブログが例に挙げるのは、洗濯機の型番ごとの取扱説明書、パスポート申請の最新の条件と手数料、近所の飲食店の最新メニューと営業時間といったページです。他のサイトからあまりリンクされていなくても、知りたい人には価値がある「細かい情報」を拾えるようになることを狙っています。

試験では、ムダな巡回を減らす工夫も進めています。存在しないページ、どのアドレスでもトップページに飛ばすだけの転送、中身が同じページを、巡回する前に見分けて省きます。更新されたときだけ見に行くよう知らせる仕組みも試しています。攻撃者がまともなサイトに偽のログイン画面を1ページだけ仕込んだようなケースでは、サイト全体ではなくそのページだけに印を付けて、索引から外す試みもしています。

## 背景：AIの巡回を「止める側」だった会社

今回の協力は、Cloudflareのこれまでの姿勢から見ると方向転換にあたります。The Next Webは7月の試験開始時、Cloudflareは前年からサイト運営者がAIの巡回を止められる仕組みを広げ、AI企業が対価を払わない限り拒否できるようにしてきたと伝えています。10月1日には、AIが記事を使うたびにサイトに対価を払う「Pay Per Use」も始めています（[記事](/news/20261001-cloudflare-pay-per-use-beta/)）。

Cloudflareは、今回の取り組みは「止める」方針と両立すると説明しています。ブログでは、手がかりを渡すことはページを読む許可を与えることではないとし、使うのはページの所在や更新といった周辺の情報で、ページの中身をAIの学習用に渡すものではないと明記しました。OpenAIにとっては、記事の使用料を払う提携とは別に、「まだ知らないページをどう見つけるか」という課題に取り組む位置づけです。

## 反応と論点

サイト運営者にとっての利点は、自分のページがAIの答えに使われ、出典としてリンクされる機会が増えることです。ブログは、ChatGPTの検索が出典へのリンクを示すことで、元のサイトへの訪問につながると強調しています。

一方、注意すべき点もブログ自身が認めています。新しいページが見つかると、評価のためにはじめは巡回がかえって増えることがあるとしています。また、試験に参加したのが「Cloudflareのネットワークの約1%」で、どのサイトがどういう手順で参加したのか、今後ほかの検索AIにも同じ手がかりを渡すのか、一般の利用者がいつから参加できるのかは書かれていません。1社が多くのサイトの更新情報を握り、特定のAI企業と組む形になることには、検索の公平さの面から議論が出そうです。

次の段階では、ページの選び方の改善、より速く正確な更新の知らせ方を試し、見つかったページがその後どれだけ訪問や売上につながったかを測るとしています。

## 日本のビジネスへの影響

- **使えるか**: 今回はあくまで研究段階の試験で、参加方法や料金、一般提供の時期は公表されていません。日本のサイトが対象になるかも書かれていません。
- **誰にどう効くか**: オウンドメディアやECサイトのSEO担当者、商品マニュアルやFAQを公開しているメーカーのWeb担当者に関係します。リンクが少なく検索で上位に出にくかったページでも、ChatGPTの答えに出典として載る道が広がります。ChatGPTが出典に公的機関やメーカー公式を選ぶ傾向が強まっているという調査もあります（[記事](/news/20261013-chatgpt-citations-primary-sources-ahrefs/)）。
- **今すぐやれること**: Cloudflareを使っている会社は、管理画面の「AI Crawl Control」でOpenAIの巡回がどこまで許可されているかを確認しておきましょう。止めたままだと、こうした仕組みが広がっても恩恵を受けられません。
- **注意点**: AIに読ませる範囲は、検索に使わせるか、学習に使わせるかで分けて決めるのが基本です。答えに引用されても、ページへの訪問が必ず増えるとは限りません。

ChatGPTの検索など、調べもの向けのAIの選び方は[調べもの・リサーチ向けAIのガイド](/best/research/)にまとめています。
