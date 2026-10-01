---
{
  "title": "Geminiに「スキル」が登場、よく使う指示を保存して「/」で呼び出す",
  "description": "Googleがよく使う指示を保存して再利用する「スキル」をGeminiのチャットに全世界展開した。「/」で呼び出せ、複数を重ねられる。既存のGemsは11月から順次スキルへ移行する。",
  "date": "2026-10-01T15:50:00+09:00",
  "updated": "2026-10-01T18:54:00+09:00",
  "category": "products",
  "tags": ["Google", "Gemini", "新機能", "オフィス", "文章作成"],
  "summary": [
    "Geminiのチャットに「スキル」が全世界で展開され、保存した指示を「/」とスキル名で呼び出せる",
    "複数のスキルを重ねて使え、テキストやPDF、画像の参照ファイルも持たせられる",
    "既存のGemsは個人アカウントで11月、Workspaceは2027年3月と6月に終了し、スキルへ自動移行される"
  ],
  "sources": [
    {"title": "Let skills in Gemini tackle your most repetitive tasks", "publisher": "Google", "url": "https://blog.google/products-and-platforms/products/gemini/automate-tasks-with-skills/"},
    {"title": "Create & manage skills for Gemini Apps", "publisher": "Google ヘルプ", "url": "https://support.google.com/gemini/answer/17094296"},
    {"title": "About the transition from Gems to skills", "publisher": "Google ヘルプ", "url": "https://support.google.com/gemini?p=gems_to_skills"},
    {"title": "Write effective skills for Gemini Apps", "publisher": "Google ヘルプ", "url": "https://support.google.com/gemini/answer/17102773"},
    {"title": "Gemini app replacing Gems with skills in November", "publisher": "9to5Google", "url": "https://9to5google.com/2026/09/27/gemini-gems-skills/"}
  ],
  "thumb_text": "Gemini スキル",
  "share_text": "Geminiに「スキル」が登場。よく使う指示を保存して「/」で呼び出せ、Gemsは11月から順次移行",
  "editor_note": ""
}
---
Googleは現地時間9月30日、よく使う指示を保存して繰り返し使える「スキル」をGeminiのチャットに全世界で展開しました。従来のGemsは置き換えられ、個人アカウントでは11月から順次スキルへ移ります。

## 何が発表されたか

スキルとは、毎回打ち直していた指示を一度保存し、名前で呼び出せるようにしたものです。プロンプト入力欄で「/」に続けてスキル名を入れると適用されます。

:::quote https://blog.google/products-and-platforms/products/gemini/automate-tasks-with-skills/ | Google公式ブログ「Let skills in Gemini tackle your most repetitive tasks」
> Today, we’re rolling out skills directly into Gemini chat globally, and bringing this functionality to Google Workspace business, enterprise, nonprofit, and education customers in the coming weeks.
本日、スキルをGeminiのチャットへ全世界で直接展開します。Google Workspaceのビジネス、エンタープライズ、非営利、教育の各顧客には、今後数週間のうちに提供します。
:::

Gemsとの大きな違いは呼び出し方です。9to5Googleが指摘するように、Gemsはサイドパネルから選んで開く必要がありましたが、スキルは今いるチャットの中で呼べ、複数を同時に重ねられます。依頼の内容が合えば、Geminiが自動で適用することもあります。重ね方の例としてGoogleは、文体のスキルとブランドガイドラインのスキルを組み合わせる使い方を挙げています。

参照ファイルは、この日からプレーンテキスト、PDF、画像を持たせられるようになりました。Gemsにあった他人との共有や、Googleドライブのファイルの追加は、今後数週間でスキルにも加わる予定です。

対象はGoogle AIの全契約層で、現在は18歳以上に限られます。同じ日に発表された[Gemini 4 Argon](/news/20261001-google-gemini-4-argon/)が当面一般に使えないのとは対照的に、こちらは今日から手元で試せます。スキルの作り方は、Geminiとの会話で作る、用意されたひな形を編集する、空のひな形に書く、`SKILL.md`を含むファイルやフォルダをアップロードする、の4通りです。公式ヘルプによれば、他のプラットフォームで作った`SKILL.md`形式のスキルも読み込めます。

## 業務での使いどころ

実務では、出力の形が毎回決まっている作業ほど効きます。

- **定例資料**：週次報告の構成、見出しの粒度、禁止表現をスキルにしておき、数字を貼るだけで原稿にする
- **広告・SNSの文面**：レギュレーション（薬機法上の言い換え、使えない表現）を参照ファイルにしたスキルと、ブランドの文体スキルを重ねる
- **営業メール**：自社の提供価格表をPDFで持たせ、相手の業種に合わせた提案文の下書きを作る
- **議事録**：決定事項・担当・期限の3項目に必ず分ける指示を保存しておく

書き方のコツは、公式ヘルプの「Write effective skills for Gemini Apps」にまとまっています。要点は、いつ使うスキルなのかが名前と説明から分かるようにすること、長い解説より短く要点を絞ること、出力のひな形や実例を入れることです。

制限も確認しておく価値があります。

:::quote https://support.google.com/gemini?p=gems_to_skills | Googleヘルプ「About the transition from Gems to skills」
> You can create as many skills as you want, but only 100 can be active at a time.
スキルはいくつでも作れますが、同時に有効にできるのは100個までです。
:::

アップロードできるのはテキストとして読めるファイルとPDF・画像で、合計100MBまでです。`.docx`や`.xlsx`は対象外で、外部サイトへアクセスするスクリプトも動きません。CanvasやDeep Research、動画・音楽の生成といった機能とはまだ併用できません。

## Gemsからの移行

Gemsのサポートは、個人のGoogleアカウントが2026年11月、Workspaceのビジネス・エンタープライズ・非営利が2027年3月、教育が2027年6月に終わります。同じ11月に、ミニアプリを作る実験的機能Opalと、Google Labs提供のGemsも終了します。保存済みのGemsは対応ファイルごと自動でスキルへ移され、手動で作り直すこともできます。9to5Googleは、Gems管理画面に「2026年11月17日からGemsがスキルになる」という告知が出たと報じています。

## 日本のビジネスへの影響

日本からも使えます。展開は全世界で、Google AIのどの契約層でも対象です。Workspaceのアカウントは数週間後とされており、会社のアカウントで試すのはもう少し先になります。

効くのは、マーケティングや広報で同じ型の文章を量産している担当者と、社内でGemsを配って運用していた情報システム部門です。前者は文体とレギュレーションを分けてスキル化すると、組み合わせの数だけ使い回せます。後者は移行作業が発生します。

今日できることは、既存のGemsの指示文とナレッジファイルを控えておくことです。自動移行はされますが、GitHubのファイルはスキルで未対応のため、そこに依存したGemsは作り直しになります。モバイルアプリでは手動作成が保存されない不具合が公式に告知されているので、作成はウェブ版で行うのが確実です。チャットAI全体の選び方は[チャットAIのおすすめと料金比較](/best/chat/)を参照してください。
