---
{
  "title": "AIに回路設計を任せて対話AI用の計算装置を自作、ブラジルの開発者が中古の業務用基板で公開",
  "description": "ブラジルの開発者Felipe Sens Bonetto氏が、AIエージェントに改良を重ねさせたAI専用の計算装置の設計図「openTPU」を無料公開した。データセンターの払い下げ基板の上で、小型の対話AIが1秒に約85語分の速さで動く。",
  "date": "2026-10-07T20:10:00+09:00",
  "category": "usecases",
  "tags": ["openTPU", "Claude Opus 5.5", "活用事例", "個人開発", "半導体", "オープンソース"],
  "summary": [
    "ブラジルの開発者Felipe Sens Bonetto氏は、AIエージェントに改良を重ねさせたAI専用の計算装置の設計図「openTPU」を無料で公開した",
    "AIが改良案を出して回路を書き換え、自動の試験に合格した案だけを採用する「勝ち抜き戦」を繰り返し、文章を作る速さを大幅に引き上げた",
    "Claude Opus 5.5が改良案と実装を担当し、ある1回の改良は約5分・1.12ドルで回路の大きさを28%減らした"
  ],
  "sources": [
    {"title": "openTPU README", "publisher": "GitHub FeSens/openTPU", "url": "https://github.com/FeSens/openTPU", "kind": "公式サイト"},
    {"title": "Architecture tournament (per component)", "publisher": "GitHub FeSens/openTPU", "url": "https://github.com/FeSens/openTPU/blob/main/docs/tourney.md", "kind": "公式サイト"},
    {"title": "Tourney report: otpu_coll", "publisher": "GitHub FeSens/openTPU", "url": "https://github.com/FeSens/openTPU/blob/main/tools/tourney/runs/otpu_coll/REPORT.md", "kind": "公式サイト"},
    {"title": "auto-arch-tournament README", "publisher": "GitHub FeSens/auto-arch-tournament", "url": "https://github.com/FeSens/auto-arch-tournament", "kind": "公式サイト"},
    {"title": "OpenTPU – An open-source AI accelerator, developed by AI", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=49980715", "kind": "コミュニティ"}
  ],
  "thumb_text": "openTPU",
  "thumb_style": "diorama",
  "thumb_prompt": "A miniature diorama of tiny construction robots laying out glowing copper circuit roads on a large green circuit board as if building a city, while a small chat speech bubble lamp lights up at the center of the board.",
  "share_text": "AIに回路の改良を何度も任せて、対話AIを動かす計算装置を自作。ブラジルの開発者が設計図を無料公開",
  "editor_note": ""
}
---
ブラジル南部フロリアノポリスの開発者Felipe Sens Bonetto氏が、AIエージェントに改良を繰り返させて作ったAI専用の計算装置の設計図「openTPU」をGitHubで無料公開しました。データセンターから払い下げられた業務用の基板の上で、小型の対話AIが実際に動きます。現地時間10月6日に掲示板Hacker Newsで紹介されると、289ポイントと340件のコメントを集めました。

## 何を作ったか

openTPUとは、対話AIの計算だけをこなす専用の計算装置を、回路の設計から動かすソフトまでまるごと公開したプロジェクトです。名前は、GoogleがAIの計算用に自社開発している半導体「TPU」にちなんでいます。

本物の半導体を工場で作るには巨額の費用がかかるため、Bonetto氏は「FPGA」という、後から回路を書き換えられる半導体を載せた基板を使いました。同氏によれば、使った基板はデータセンターで使われなくなったもので、趣味で回路を作る人たちの間で人気があるといいます。

プロジェクトの狙いは、説明文の冒頭に書かれています。

:::quote https://github.com/FeSens/openTPU | openTPU README（GitHub）
> It asks two questions: how far can AI agents go at hardware design, and can they build the chip that runs their own inference?
問いは2つある。AIエージェントはハードウェアの設計でどこまでやれるのか。そして、自分自身を動かすチップを作れるのか。
:::

{{card:https://github.com/FeSens/openTPU|openTPU: An open-source AI accelerator, developed by AI|GitHub}}

## どう作ったか

中心にあるのは、AIどうしを競わせる「勝ち抜き戦」の仕組みです。1回戦ごとに、複数のAIエージェントが並行して「ここをこう変えれば速くなる・小さくなる」という改良案を考え、実際に回路の記述を書き換えます。

書き換えた回路は、自動の関門を順に通ります。まず計算結果が1ビットも狂わずに元と一致するか、次に対話AIを動かしたときに遅くなっていないか、最後に回路の大きさと動く速さがどれだけ改善したか。すべての関門を通り、決められた基準を上回った案のうち最も良いものだけが、新しい「王者」として採用されます。ただし、それを本番の設計に取り込むかどうかは人が決めるルールです。

AIの担当は役割ごとに分かれています。改良案を考える係と実装する係は、AnthropicのClaude Opus 5.5が初期設定で、OpenAIのCodexに切り替えることもできます。AIはネットへの接続を禁じられ、決められたファイル以外は書き換えられないように制限されています。

公開されている記録の1例では、Claude Opus 5.5が出した改良案が約5分・1.12ドル分の利用料で、ある部品の回路の大きさを28%減らしつつ、動く速さの目標も満たしました。

## 成果

Bonetto氏はHacker Newsで、最初は1秒に数語分しか出せなかった装置が、この改良の繰り返しで小型モデルなら毎秒80語分を超えるまで速くなったと説明しています（AIが文章を作るときの単位「トークン」で数えた値）。公開資料の計測では、小型の対話AI「LFM2.5-230M」が毎秒約85トークン、Googleの「Gemma 4」の小型版が毎秒約12トークンで動きました。どの設定でも、計算結果はパソコン上の模擬計算と完全に一致したとしています。

同氏は以前にも、同じやり方でパソコンの頭脳にあたる小さな演算装置（CPU）の設計をAIに改良させています。そのときは約10時間で73の改良案を試し、人が作った定番の公開設計より26%速く、回路は40%小さいものができたと記録しています。

一方、Hacker Newsでは「AIが自分のための半導体を作れるようになった、というのは言い過ぎだ」という指摘も出ました。人が試験の仕組みを用意し、その中でAIが条件付きの最適化をしているにすぎない、という見方です。Bonetto氏自身も、FPGAは本物の専用半導体を工場で作る前に設計を確かめる道具だと位置づけています。

## 日本で真似するなら

- **必要なもの**: 改良の仕組みそのものは、AIエージェントのClaude CodeかCodexと、設計を自動で試験する環境があれば動きます。基板がなくても、模擬計算はノートPCで試せるとしています
- **手順の目安**: まず「正しく動くか」「良くなったか」を自動で判定する試験を作り、その上でAIに改良案と実装を任せ、合格した案だけを残します。人がやるのは、試験の基準づくりと最終的な採用判断です
- **応用先**: 回路に限らず、Webページの表示速度、広告の配信ルール、業務の自動処理など、「良し悪しを数字で自動判定できる」改善作業なら同じ考え方が使えます
- **注意点**: AIは試験に受かることを目指して動くため、試験そのものに抜けがあると、見た目だけ数字が良い改良が採用されかねません。判定の基準は人が厳しく作り込む必要があります

## 日本のビジネスへの影響

- **使えるか**: openTPUは商用利用もできるApache 2.0という条件で公開されており、日本からも自由に読めて試せます。説明は英語のみです
- **誰にどう効くか**: 製造業やエレクトロニクスの設計・開発部門、社内の業務改善を担う企画担当者に関係があります。AIに「1回で正解を出させる」のではなく、「自動の試験で選別しながら何十回も改良させる」使い方は、専門家の作業時間を大きく減らせる可能性を示しています
- **今すぐやれること**: 自社の業務で「良くなったかどうかを数字で判定できる作業」を1つ挙げ、その判定を自動化できるか検討してみてください。それがAIに改良を任せる第一歩になります
- **注意点**: 今回の成果は個人の公開記録で、第三者による検証はまだこれからです。半導体の本格的な設計に使うには、品質保証や安全性の確認を人が担う体制が欠かせません

AIエージェントにプログラムを書かせる道具の選び方は、[コーディングAIのおすすめと料金比較](/best/coding/)にまとめています。
