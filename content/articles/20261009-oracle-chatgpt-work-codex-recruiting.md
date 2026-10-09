---
{
  "title": "ChatGPTで採用の下調べが2〜4日から15分に、米Oracleの10万人超が仕事を作り直す",
  "description": "OpenAIは10月8日、米Oracleの社員10万人超がChatGPT WorkとCodexを使う導入事例を公開した。採用担当は2〜4日かかった市場調査を15〜20分の準備に縮め、事業部門は報告書を探さず欲しい結果を言葉で頼むようになった。",
  "date": "2026-10-09T11:25:00+09:00",
  "category": "usecases",
  "tags": ["Oracle", "ChatGPT", "ChatGPT Work", "Codex", "活用事例", "導入事例"],
  "summary": [
    "OpenAIは10月8日、米Oracleで10万人超の社員がChatGPT WorkとCodexを採用・事業・IT運用に使う事例を公開した",
    "採用チームはChatGPTで市場調査の道具を自作し、2〜4日かかっていた面談前の下調べを15〜20分にした",
    "事業部門は報告書を探す代わりに欲しい結果を言葉で頼み、2時間かかった集計がほぼ即答に。一方で費用の膨張も報じられている"
  ],
  "sources": [
    {"title": "How Oracle turns days of work into minutes with ChatGPT and Codex", "publisher": "OpenAI", "url": "https://openai.com/index/oracle/", "kind": "公式発表"},
    {"title": "Oracle got AI working on itself only this year", "publisher": "The Next Web", "url": "https://thenextweb.com/news/oracle-internal-ai-rollout-town-hall", "kind": "報道"}
  ],
  "thumb_text": "ChatGPT Work",
  "thumb_style": "photo",
  "thumb_prompt": "A recruiter's desk where a towering stack of salary survey binders and printed job listings has been pushed aside, replaced by a single tablet showing a tidy one-page summary next to a small hourglass with only a few grains of sand left.",
  "share_text": "米Oracleの採用担当が2〜4日かけていた下調べをChatGPTで15分に。10万人超がChatGPT WorkとCodexで仕事を作り直す",
  "editor_note": ""
}
---
OpenAIは現地時間10月8日、米IT大手Oracleの社員10万人超が、仕事を任せるChatGPTの機能「ChatGPT Work」と開発支援のAI「Codex」を使っている導入事例を公開しました。採用担当者は、面談前に2〜4日かけていた市場調査を、自作の道具で15〜20分の準備に縮めています。

## 何をしたか：専門家の下調べを誰でもできる道具に

Oracleの事例で目を引くのは、AIを「質問に答えるもの」ではなく、部署ごとの決まった仕事を片付ける道具づくりに使っている点です。OpenAIの公式事例によると、使い方は採用、事業部門、IT運用の3つに広がっています。

| 部署 | AIに任せたこと | 以前 | 今 |
|---|---|---|---|
| 採用 | 求人票から、似た職種・報酬相場・地域ごとの人材の層を調べる | 2〜4日 | 15〜20分の準備 |
| 事業部門 | 「こういう数字が欲しい」と頼むと、社内のシステムから集計して報告や小さなアプリにする | 数時間 | ほぼ即時 |
| IT運用 | 障害が起きたとき、関係する情報と対応手順書を自動で集める | 約1時間 | 数分 |

### 採用：ChatGPT Workで「市場調査の道具」を自作

採用チームはChatGPT Workで、求人票を入れると似た職種を探し、報酬の相場を比べ、地域ごとに候補者がどれだけいるかを調べる道具を作りました。採用担当者が採用したい部署の責任者と最初に話す前に必要な材料で、以前はそろえるのに2〜4日かかっていました。

:::quote https://openai.com/index/oracle/ | OpenAI「How Oracle turns days of work into minutes with ChatGPT and Codex」
> We’ve built our talent market intelligence tool using ChatGPT Work, and it’s really revolutionized how we do the front end of our recruitment process.
ChatGPT Workで人材市場の調査ツールを作り、採用の最初の段階のやり方が根本から変わった。
:::

こう話すのは、Oracleで採用部門の世界責任者を務めるJan Ackerman上級副社長です。効果は時間だけではありません。同じ道具を全員が使うので、誰が担当しても部署の責任者に渡る材料の質がそろうようになったと説明しています。

### 事業部門：報告書を探すのをやめた

仕組みの土台は、社内の業務システムを担う「Oracle Applications Lab」のチームが作った対応表です。取引先や注文、製品といった会社の中の「もの」と、その関係や決まりごとを整理してあります。社員が普通の言葉で頼むと、Codexはこの表をもとに必要なシステムとデータを選び、結果を分析・報告・小さなアプリの形で返します。

効果の確かめ方は素朴です。ある社員は、以前なら2時間ほどかかっていた集計をほぼ即座に受け取り、昔ながらの手作業の結果と比べたところ、数字はぴたりと合ったといいます。

:::quote https://openai.com/index/oracle/ | OpenAI「How Oracle turns days of work into minutes with ChatGPT and Codex」
> Business users now describe the outcome they want instead of hunting for a report. That is a major shift.
事業部門の社員は、報告書を探し回る代わりに、欲しい結果を言葉で伝えるようになった。これは大きな変化だ。
:::

チームを率いるRichard Lamグループ副社長の言葉です。

## どう進めたか：AIに任せても「持ち主」は人

AIに作業を任せる範囲が広がっても、Oracleの幹部は「全自動ではない」と念を押しています。Lam氏がいちばん強く警告するのは、AIに任せきりにした結果、誰も手入れできないプログラムが山のように残ることです。そのため、システムの設計や安全対策、AIに書かせるプログラムの形は、人が責任を持って決めるべきだとしています。

仕事の進め方そのものも変わりました。CIO（最高情報責任者）の技術顧問を務めるBarry Shilmover副社長は、アイデアを企画書にまとめる前に、まず動く試作品を作るようになったと話しています。非エンジニアの部署でも、「AIが作ったものの持ち主は人」という決まりと、「紙より先に試作」という順番はそのまま使えます。

## 成果の裏側：費用と「次の詰まり」

The Next Webは9月、Business Insiderの報道をもとに、Oracleの社内導入の舞台裏を伝えています。同社が社員向けにChatGPT EnterpriseとCodexを入れたのは今年の4〜5月で、社内規定や安全対策を整えたうえで、3か月で社員の80%が使うようになったと報じています。

一方で、使い始めが簡単なぶん、請求額の大きさに会社が驚いたとも伝えています。現在は社員に、どのAIモデルをいくら使っているかを見せ、高性能なGPT-6 Astraより安いGPT-5.6 Terraに日常の仕事を回しているといいます。開発者は以前なら2〜3四半期かかった量を1週間で書けるようになった半面、テストや公開の手順が追いつかず、顧客に届く速さは変わっていないとも報じられています。

公式事例が示すのは成功した部分で、こうした詰まりは書かれていません。両方を並べて読むと、AIで速くなった工程の次に、どこが詰まるかまで見ておく必要があることがわかります。

## 日本のビジネスへの影響

- **使えるか**: ChatGPTは日本でも提供されており、法人向けのBusinessプランには円建ての料金もあります。Codexは個人向けのPlusプランから使えます。社内のデータにつなぐ使い方は、情報システム部門の管理のもとで法人向けプランから始めるのが現実的です
- **誰にどう効くか**: いちばん真似しやすいのは採用担当者です。求人票を入れて、似た職種の求人、報酬の相場、地域ごとの人材の層を調べ、1枚にまとめる手順をChatGPTに覚えさせれば、Oracleと同じ「面談前の下調べの道具」になります。営業企画や経営企画の担当者は、毎週作る定型の集計を「欲しい結果」として言葉で頼む形に置き換えられます
- **今すぐやれること**: 自分の部署で「毎回同じ手順で、2〜3日かかっている下調べ」を1つ選び、手順を文章に書き出してChatGPTに渡してみてください。まず人の手作業の結果と数字が合うかを照らし合わせるのが、Oracleでも使われた確かめ方です
- **注意点**: 社員全員に一斉に開放すると費用が膨らみやすいことは、Oracleの例が示しています。部署ごとの利用額を見える化し、日常の仕事には安いモデルを使う決まりを最初から作っておくと安心です。報酬の相場など外部の数字は、AIが集めた出典を人が確かめてから使ってください

対話型AIの選び方と料金は、[チャットAIのおすすめと料金比較](/best/chat/)にまとめています。OpenAIの導入事例では、米Chatham Financialが取引の照合を30分から4分未満に縮めた例も紹介しています（[既報](/news/20261003-chatham-financial-codex-trade-validation/)）。
