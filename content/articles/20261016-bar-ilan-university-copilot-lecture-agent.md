---
{
  "title": "Copilotで作った講義のAI助手、イスラエルの大学が71科目で導入 自習5時間が3時間になった学生も",
  "description": "イスラエルのバル・イラン大学は、教員が載せた講義録画や資料だけを元に要約や小テストを作るAI助手を71科目・約2,400人で試し、新学期に約100科目へ広げる。MicrosoftのCopilot Studioで作られ、自習が1日5〜6時間から3時間に減った学生もいる。",
  "date": "2026-10-16T03:30:00+09:00",
  "category": "usecases",
  "tags": ["Bar-Ilan University", "Copilot Studio", "Microsoft", "活用事例", "導入事例", "教育"],
  "summary": [
    "イスラエルのバル・イラン大学が、教員の講義録画やスライドだけを元に答えるAI助手を、2月から71科目・学生約2,400人で試した",
    "AI助手は要約や小テスト、模擬試験を作り、ヘブライ語・アラビア語・英語に対応。MicrosoftのCopilot Studioで作られている",
    "自習が1日5〜6時間から約3時間に減った学生や、期末試験の平均点が3ポイント上がった授業があり、新学期は約100科目を追加する"
  ],
  "sources": [
    {"title": "Missed a lecture? This AI agent at Bar-Ilan University helps students catch up", "publisher": "Microsoft Source EMEA", "url": "https://news.microsoft.com/source/emea/features/missed-a-lecture-this-ai-agent-at-bar-ilan-university-helps-students-catch-up/", "kind": "公式発表"},
    {"title": "Copilot Studio pricing", "publisher": "Microsoft", "url": "https://www.microsoft.com/en-us/microsoft-365-copilot/pricing/copilot-studio", "kind": "公式ドキュメント"}
  ],
  "thumb_prompt": "A miniature university lecture hall with rows of tiny empty seats, where one small student figure sits at the back with a laptop while a friendly little robot tutor stands at the lectern holding up a stack of index-card quizzes.",
  "thumb_style": "diorama",
  "thumb_text": "講義のAI助手",
  "share_text": "講義の録画や資料だけを元に要約と小テストを作るAI助手。イスラエルの大学が71科目で試し、自習5〜6時間が3時間になった学生も",
  "editor_note": ""
}
---
イスラエルのバル・イラン大学は、教員がアップロードした講義の録画やスライドだけを元に、学生の質問に答えたり要約や小テストを作ったりするAI助手を、2026年2月から71科目・学生約2,400人で試しました。Microsoftが現地時間10月15日に公式サイトで紹介したもので、10月に始まった新学期には約100科目を追加します。自習の時間が1日5〜6時間から約3時間に減ったという学生の声も紹介されています。

## 何を作ったか

バル・イラン大学は、テルアビブ近郊にある学生2万人超の公立の研究大学です。AI助手は、大学が授業で使っている学習管理システム「Moodle」（課題の提出や教材の配布に使う仕組み）の中に組み込まれています。

学生が普段の言葉で質問すると、AI助手は次のようなことをしてくれます。

- その科目の教材から関係する箇所を探し、要約して返す
- 講義で扱ったテーマについて、選択式や記述式の小テストを作り、正誤と解説を返す
- 教員の教材を元に、模擬試験を作る

答えの元にするのは、講義の録画とその文字起こし、スライド、論文など、教員がアップロードした資料だけです。ネット上の一般的な情報ではなく「その先生の授業の中身」に沿って答える設計にしているのがポイントです。言語はヘブライ語・アラビア語・英語に対応しています。

## どう作ったか

開発したのは、KPMGとOpenAppの2社です。Microsoftの「Copilot Studio」（プログラムを書かずにAI助手を組み立てられる企業向けの道具）を使い、AIの機能にはMicrosoftのクラウドのAIサービスを使っています。大学のデータは、大学が管理する安全なクラウド環境の中で動かしています。使ったAIモデルの名前や費用は公表されていません。

AIに任せる前の準備は教員がしています。講師のエリヤフ・ビトン氏は、教材を書き直し、動画講義の文字起こしを用意し、スライドの要点に論文や参考文献を書き足しました。そのうえで、AI助手の答えが正確だと納得できるまで試したといいます。

:::quote https://news.microsoft.com/source/emea/features/missed-a-lecture-this-ai-agent-at-bar-ilan-university-helps-students-catch-up/ | Microsoft公式「Missed a lecture? This AI agent at Bar-Ilan University helps students catch up」
> If I want it to be my assistant, I need to teach it.
自分の助手にしたいなら、まず自分が教えなければいけない。（ビトン氏）
:::

## 成果

Microsoftの紹介記事に出てくる数字は、次のとおりです。

| 項目 | 内容 |
|---|---|
| 試行の規模 | 2月から71科目、学生約2,400人 |
| 新学期の拡大 | 2026/27年度の前期（10月開始）に約100科目を追加 |
| 学生の自習時間 | 犯罪学と心理学を学ぶ1年生は、講義後の自習が1日5〜6時間から約3時間に |
| 期末試験 | ビトン氏の授業（約50人）の平均点が例年より3ポイント高かった |

:::quote https://news.microsoft.com/source/emea/features/missed-a-lecture-this-ai-agent-at-bar-ilan-university-helps-students-catch-up/ | Microsoft公式（同記事）
> She now spends about three hours a day studying after lectures, compared with five to six hours previously.
彼女はいま講義後の自習に1日約3時間を使っている。以前は5〜6時間だった。
:::

ただし、どちらも個人の体験や1つの授業の結果です。ビトン氏自身、平均点の上昇はその年の学生がもともと優秀だった影響もありうると話しています。試験の点数がAI助手の効果だと言い切れる調査ではありません。

数字以外の変化もあります。ビトン氏は、事務的な質問や繰り返しの質問が減り、学生が試験の前に落ち着いていると話しています。年に4〜6回の90分の討論の授業は続けていて、自分の役割は知識を教えることから、学生の相談に乗る「指導役」に変わりつつあるといいます。学生の側も、AI助手は先生の代わりではなく、先生と一緒に使うものだと受け止めています。

## 日本で真似するなら

- **必要なもの**: 社内やスクールの教材（録画・文字起こし・スライド・マニュアル）と、AI助手を組み立てる道具。Copilot Studioの場合、Microsoft 365 Copilot（1人月30ドル、年払い）の契約者は組織内向けのAI助手を追加費用なしで作れます。社外の人も使うWebサイトなどに公開するには、別途Copilot Studioの契約（月200ドルで2万5,000クレジットのパックか従量課金）が必要です（10月16日時点、米国の公式料金ページ）
- **手順の目安**: ①対象を1つの講座や研修に絞る ②教材をそろえ、録画は文字起こしする ③AI助手が答えてよい範囲を「その教材の中だけ」に限る ④担当者が質問を何十個も投げて答えを確かめる ⑤少人数で試してから広げる
- **注意点**: 答えの質は教材の質で決まります。バル・イラン大学でも、教員が教材を作り直す手間をかけています。古い資料をそのまま入れると、古い答えが返ってきます

{{card:https://www.microsoft.com/en-us/microsoft-365-copilot/pricing/copilot-studio|Copilot Studio pricing|Microsoft}}

## 日本のビジネスへの影響

- **使えるか**: Copilot StudioはMicrosoft 365を使っている日本企業でも利用でき、同じような仕組みは日本でも作れます。Microsoftの対話AIの料金の全体像は[Copilotの使い方と料金](/news/20261015-copilot-how-to-use-pricing/)にまとめています
- **誰に効くか**: 大学や専門学校だけでなく、企業の人事・研修担当者に向いた事例です。新人研修や社内講座の録画とスライドを読ませれば、欠席した人や復習したい人が自分のペースで要点と小テストを受けられます。営業マニュアルや商品知識の勉強にも応用できます
- **今すぐやれること**: 社内にある研修動画のうち、毎年同じ内容を繰り返している講座を1つ選び、文字起こしがあるかを確かめてください。文字起こしと資料がそろえば、試作の材料になります
- **注意点**: 社員の個人情報や社外秘の資料を入れる場合は、データがどこに保存されるかを情報システム部門と確認してください。AIの答えをうのみにしないよう、最終的な判断は講師や担当者に確認する流れも残しておくべきです。資料の要約に使えるAIの比較は「[リサーチAIの選び方](/best/research/)」にまとめています
