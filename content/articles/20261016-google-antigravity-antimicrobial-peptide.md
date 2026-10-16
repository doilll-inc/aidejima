---
{
  "title": "Antigravityで研究者とAIが新しい抗菌物質の候補を発見、数日の下調べを1回で",
  "description": "Google DeepMindは10月15日、AI開発ツールGoogle Antigravityで、働きが未知のタンパク質数百万件から新しい抗菌物質の候補を見つけた手順を公開した。候補は実験で確認中。科学者1万人への無料枠の募集もある。",
  "date": "2026-10-16T22:50:00+09:00",
  "category": "research",
  "tags": ["Google DeepMind", "Antigravity", "ProtNLM", "AlphaFold", "医療", "エージェント"],
  "summary": [
    "Google DeepMindは、AI開発ツールのGoogle Antigravityで研究者とAIが組み、新しい抗菌物質の候補を見つけた手順を公開した",
    "機能がわからないまま眠っていたタンパク質数百万件から候補を絞り、立体構造や周りの遺伝子まで調べて実験計画も作らせた",
    "候補はまだ実験で効き目を確かめている段階。Googleは科学者1万人にAntigravityの最上位の利用枠を無料で配る募集をしている"
  ],
  "sources": [
    {"title": "Accelerating the search for antimicrobial peptides with Google Antigravity", "publisher": "Google DeepMind", "url": "https://deepmind.google/blog/accelerating-antimicrobial-discovery/", "kind": "公式発表"},
    {"title": "Why choose Google Antigravity for science", "publisher": "Google Antigravity", "url": "https://antigravity.google/use-cases/science", "kind": "公式サイト"}
  ],
  "thumb_text": "Google Antigravity",
  "share_text": "Antigravityで研究者とAIが新しい抗菌物質の候補を発見。数日かかる下調べが1回の作業に",
  "thumb_style": "illustration",
  "thumb_prompt": "A scientist's lab bench at night with a single glowing petri dish, while a tiny helpful robot stands on a towering mountain of unlabeled specimen jars, holding up one jar that shines.",
  "editor_note": ""
}
---
Google DeepMindは現地時間10月15日、同社のAI開発ツール「Google Antigravity」を使い、研究者とAIが組んで新しい抗菌物質の候補を見つけた手順を公式ブログで公開しました。機能がわからないまま公開データベースに眠っていたタンパク質数百万件から候補を絞り込み、実験の計画まで1回の作業でまとめています。候補はいま、実験室で効き目を確かめている段階です。

## 何が発表されたか

Google Antigravityとは、Googleが提供する、AIに作業を任せて進めるための開発ツールです。もともとはプログラムを書かせる用途で知られていますが、Googleは科学研究向けの使い方にも力を入れています。今回のブログは、その「科学の作業台」としての使い方を、抗菌物質探しを例に具体的に見せたものです。

背景にあるのは、薬が効かない細菌（薬剤耐性菌）の広がりです。ブログでは、2050年には薬剤耐性による死者が世界で年1,000万人に達するという推計を挙げています。新しい抗生物質が要る一方で、候補探しは複数のデータベースや道具を行き来する手間のかかる作業でした。

:::quote https://deepmind.google/blog/accelerating-antimicrobial-discovery/ | Google DeepMind「Accelerating the search for antimicrobial peptides with Google Antigravity」
> This technical walkthrough shows how biologists used Google Antigravity to uncover a novel antimicrobial peptide candidate which has predicted activity against the pathogens involved in respiratory tract infections. The lead identified here is now undergoing wet-lab validation.
この技術解説では、生物学者がGoogle Antigravityを使い、呼吸器の感染症に関わる病原体に効くと予測される新しい抗菌ペプチドの候補を見つけた方法を紹介します。ここで特定した候補は、現在、実験室で検証中です。
:::

## AIと研究者は何をしたか

出発点は、タンパク質の情報を集めた世界的な公開データベース「UniProt」です。ここには、遺伝子の解読で見つかったものの、何をするのかわかっていないタンパク質が数百万件あります。Googleは、アミノ酸の並びからタンパク質の働きを推定するAI「ProtNLM」でこれらに説明を付けており、Antigravityの中からそれを使えます。

研究者は「肺炎レンサ球菌の仲間（Streptococcus pseudopneumoniae）が持つ新しい抗菌ペプチドを探す」という目標を決め、どの証拠を集めるかを指示しました。AIはその指示に沿って、次のような作業を順に進めています。

| 段階 | AIがしたこと |
|---|---|
| 絞り込み | 数百万件から少数の候補を選び、97個のアミノ酸からなる抗菌物質（バクテリオシン）の候補を見つけた |
| 新しさの確認 | 人が確認済みのタンパク質の一覧と照らし、よく似たものが無いことを確かめた |
| 形の確認 | AlphaFold（タンパク質の立体構造を予測するGoogleのAI）の予測を取り寄せ、実験で形がわかっている抗菌物質とよく似ていることを示した |
| 周りの遺伝子 | 候補のすぐ隣に、物質を運ぶ仕組みの遺伝子が並び、抗菌物質を作って働かせる一式の一部らしいことを見つけた |
| 実験計画 | 論文を読んで効き方と効きそうな菌の範囲を推定し、作り方・効き目・毒性を調べる実験の手順を作った |

## どこまでわかったのか

ブログは、今回の候補を「構造と遺伝子の証拠に裏付けられた、生物学的にありうる候補」としつつ、実験での確認がまだ必要だと明記しています。同じ方法で見つけたほかの候補もいくつか実験に回っていますが、結果はまだ出ていません。候補の数や、作業が何時間短くなったかといった数字は示されておらず、「何日もかかっていたデータベースでの下調べが1回の共同作業になる」という説明にとどまります。査読を受けた論文も出ていません。

つまり、今回は「新しい薬ができた」という話ではなく、薬の候補探しの最初の段階をAIに任せる手順を、実例つきで公開した段階です。Google DeepMindは10月12日にも、AIが数学の未解決問題を証明した成果を発表しており（[関連記事](/news/20261012-deepmind-alphaproof-nexus-science-erdos/)）、科学の分野でAIを「研究の相棒」として売り込む動きが続いています。

## 誰が使えるか

Antigravityは、Mac・Windows・Linux向けのアプリとして配られています。科学向けのページでは、研究用の追加機能（Science plugin）をアプリ内からワンクリックで入れられると案内しています。この追加機能からは、UniProtなど30以上の生命科学のデータベースや、AlphaFoldのデータベースを使えます。

今回の発表に合わせて、タンパク質の形を立体で表示する「Biomolecular Structure Viewer」もAntigravityに加わりました。別の3Dソフトに切り替える必要がなく、研究者が画面上で印を付けた部位はAIにも伝わるため、「この部分はどう働くか」とその場で聞けます。

{{card:https://antigravity.google/use-cases/science|Why choose Google Antigravity for science|Google Antigravity}}

さらにGoogleは、科学者1万人にAntigravityの最上位の利用枠と、同社で最も高性能なモデルのGemini 4 Argonを無料で提供するとして、申し込みを受け付けています。日本の研究者が対象になるかどうかは、ページには書かれていません。

## 日本のビジネスへの影響

- **使えるか**: Antigravityのアプリは日本からもダウンロードでき、サイトには日本語の表示もあります。科学者1万人への無料枠は申し込み制で、日本から応募できるかは10月16日時点で明記されていません。
- **誰にどう効くか**: 製薬・化学・食品メーカーの研究開発部門や、大学の研究室の研究者に関係します。データベースを1つずつ開いて調べ、結果を手で突き合わせていた下調べを、AIに指示しながら1つの画面で進める使い方の手本になります。
- **今すぐやれること**: 研究開発の担当者なら、科学向けのページから無料枠に申し込み、自社の扱う分野のデータベースが追加機能で使えるかを確かめます。社内の研究テーマを1つ選び、過去に人が数日かけた下調べを同じ条件でAIにやらせて、結果と時間を比べてみるとよいでしょう。開発ツールとしての比較は[コーディングAIのガイド](/best/coding/)にあります。
- **注意点**: 今回の成果は、まだ実験で確かめられていない「候補」です。AIの推定はもっともらしく見えても外れることがあり、最終的な判断は実験に頼るしかありません。未発表の研究データや化合物の情報を外部のAIに入れる前に、社内の情報管理の決まりと利用規約を確認してください。
