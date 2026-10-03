---
{
  "title": "Google検索がAI生成コンテンツの指針を改訂、公開前に人の手で事実確認を求める",
  "description": "Googleは10月1日、検索向けの「生成AIコンテンツの使い方」の指針に3文を加え、AIが作った文章は公開前に人が事実確認すべきだと明記した。対象はtitleやmeta description、構造化データ、画像のalt属性にも及ぶ。",
  "date": "2026-10-03T23:20:00+09:00",
  "category": "marketing",
  "tags": ["Google", "Google検索", "SEO", "検索", "ハルシネーション"],
  "summary": [
    "Googleは現地時間10月1日、検索セントラルの生成AIコンテンツの指針を改訂し、公開前に人の手で事実確認することが「critical（極めて重要）」と書き加えた",
    "Googleの改訂では、生成AIは事実を取り出すのではなく次の語を予測するため誤り（ハルシネーション）を含みうる、という理由も明記された",
    "人による確認の対象はtitle要素・meta description・構造化データ・画像の代替テキストまで及ぶ。新たな罰則や順位の仕組みは発表されていない"
  ],
  "sources": [
    {"title": "Google Search's guidance on using generative AI content on your website", "publisher": "Google検索セントラル", "url": "https://developers.google.com/search/docs/fundamentals/using-gen-ai-content", "kind": "公式ドキュメント"},
    {"title": "Latest Google Search Documentation Updates", "publisher": "Google検索セントラル", "url": "https://developers.google.com/search/updates", "kind": "公式ドキュメント"},
    {"title": "Google Search's guidance on using generative AI content on your website（9月27日時点のアーカイブ）", "publisher": "Internet Archive", "url": "https://web.archive.org/web/20260927014811/https://developers.google.com/search/docs/fundamentals/using-gen-ai-content", "kind": "公式ドキュメント"},
    {"title": "Google Tells Sites To Fact-Check AI Content Before Publishing", "publisher": "Search Engine Journal", "url": "https://www.searchenginejournal.com/google-fact-check-ai-content-before-publishing/591782/", "kind": "報道"},
    {"title": "Google Updates AI Content Guidelines: Manually Factcheck & Review AI-Generated Content", "publisher": "Search Engine Roundtable", "url": "https://www.seroundtable.com/google-updates-ai-content-guidelines-factcheck-review-42217.html", "kind": "報道"},
    {"title": "Google tells sites to manually factcheck all AI content before publishing", "publisher": "PPC Land", "url": "https://ppc.land/google-tells-sites-to-manually-factcheck-all-ai-content-before-publishing/", "kind": "報道"}
  ],
  "thumb_text": "AI生成コンテンツ指針",
  "share_text": "Google検索がAI生成コンテンツの指針を改訂。titleや構造化データも含め、公開前に人が事実確認を",
  "editor_note": ""
}
---
Googleは現地時間10月1日、サイト運営者向けの検索セントラルにある「生成AIコンテンツの使い方」の指針を改訂し、AIが作った文章は公開前に人の手で事実確認するよう明記しました。確認の対象は本文だけでなく、検索結果に表示されるtitle要素やmeta description、構造化データ、画像の代替テキスト（alt属性）にも及びます。

## 何が変わったか

AIデジマ編集部が9月27日時点のアーカイブと現在のページを突き合わせたところ、変わったのは「正確さ・品質・関連性に注力する」という節の後半だけでした。改訂前は「メタデータもこれに含まれる」という1文でしたが、改訂後は生成AIが誤りを含む理由と、人による確認の必要性を説明する3文が加わっています。

:::quote https://developers.google.com/search/docs/fundamentals/using-gen-ai-content | Google検索セントラル「Google Search's guidance on using generative AI content on your website」
> It is critical to manually factcheck and review all AI-generated content for accuracy and trustworthiness before publishing.
公開前に、AIが生成したすべてのコンテンツを人の手で事実確認し、正確さと信頼性を見直すことが極めて重要です。
:::

理由として、生成モデルは事実を取り出すのではなく、学習データをもとに「ありそうな単語の並び」を予測しているため、出力に誤り（ハルシネーション）が含まれうると書かれています。続く文で、この確認は検索結果に出るtitle要素、meta description、構造化データ、画像の代替テキストにも当てはまるとしています。

ページのほかの部分は変わっていません。人の役に立たないページをAIで大量に作ると「大量生成コンテンツの不正使用」というスパムポリシーに触れうること、検索品質評価ガイドラインの4.6.5節と4.6.6節を参考にできること、EC事業者向けのMerchant Centerの規定（AI生成画像にIPTCのメタデータを付け、AIで作った商品名や説明はその旨を示す）は改訂前から同じ文面です。

{{card:https://developers.google.com/search/updates|Latest Google Search Documentation Updates|Google検索セントラル}}

## 背景

Googleは変更履歴のページで、今回の改訂を「検索品質評価ガイドラインの情報を加えた」と説明し、理由を「開発者向けイベントで使っている説明資料と内容をそろえるため」としています。ただ、評価ガイドラインの節を参照する文は改訂前からあり、実際に増えたのは事実確認の3文です。PPC Landによると、Search Engine JournalとRelevant Audienceも改訂前後を比べ、同じ点を指摘しています。

改訂の時期について、PPC Landは、Googleがバルセロナで開いた開発者イベント「Search Central Live Deep Dive」の会期中で、9月のスパムアップデートの展開中でもあったと報じています。Search Engine Roundtableは、Googleの検索ドキュメントで「critical」という強い語が使われるのは珍しいと指摘しました。

一方で、新しい罰則や順位付けの仕組みは発表されていません。指針はあくまで「こう作ってほしい」という説明で、人が確認したかどうかをGoogleがどう判定するかも書かれていません。Google自身の検索AIを巡っては、[AI OverviewsをめぐるCheggとPenskeの訴訟が棄却された件](/news/20261002-google-ai-overviews-chegg-penske-dismissed/)も伝えています。

## 反応と論点

AIで書くこと自体は認め、最終的な確認は人に求めるという立場は従来と同じで、今回はそれを強い言葉で書き直した形です。批判的な見方もあり、PPC Landは、利用者には人による確認を求める一方、Google自身のAI Overviewsにも誤りが指摘されている点を、ちぐはぐさとして取り上げました。

実務面で影響が大きいのは、メタデータまで名指しされたことです。商品ページのtitleやdescription、画像のaltは件数が多く、AIで一括生成してそのまま流し込みやすい部分です。本文は人が読んでいても、メタデータの確認は後回しになりがちだと編集部は見ています。

## 日本のビジネスへの影響

- **使えるか**: 指針は英語版が先に更新されたもので、Google検索全体に関わる説明です。日本語のサイトにも同じ考え方が当てはまります。日本語版ページへの反映時期は示されていません。
- **誰にどう効くか**: AIで記事や商品説明を量産しているSEO担当者・コンテンツマーケターと、商品データをAIで整えているEC運営者に直接関係します。とくに、titleやmeta description、構造化データの価格や在庫、画像のaltを自動生成している場合は、確認の工程が抜けていないか見直す必要があります。
- **今すぐやれること**: AIを使っている制作フローを洗い出し、「本文」「title・description」「構造化データ」「alt」のそれぞれで誰が事実確認しているかを表にしてみてください。確認者がいない項目から、抜き取り確認を始めるのが現実的です。AIの文章作成ツールの比べ方は[文章作成AIのガイド](/best/writing/)にまとめています。
- **注意点**: 改訂は罰則の新設ではなく、AIで書くこと自体を禁じたものでもありません。過剰に反応してAIの利用をやめるより、人が確認した記録を残し、誤りが見つかったときに直せる体制を作るほうが効果的です。
