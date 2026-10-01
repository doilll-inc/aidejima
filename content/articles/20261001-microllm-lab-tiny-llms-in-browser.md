---
{
  "title": "MicroLLM Labはブラウザで小型LLM7種を試せる実験場、WebGPUで端末内だけで動く",
  "description": "小型の言語モデル7種をブラウザだけで動かして比べるMicroLLM Labが公開された。モデルは2600万〜3億6000万パラメーターで、4ビットに圧縮して端末で動かす。作者によると3万6000のIPから30万回超のアクセスがあった。",
  "date": "2026-10-01T18:33:00+09:00",
  "category": "usecases",
  "tags": ["MicroLLM Lab", "WebGPU", "活用事例", "個人開発", "ローカルLLM", "オープンソース"],
  "summary": [
    "MicroLLM Labは、2600万〜3億6000万パラメーターの小型言語モデル7種をブラウザだけで動かせる実験場",
    "MicroLLM Labは重みを4ビットに圧縮して端末に保存し、Mac mini M4では毎秒100トークン超で答える",
    "作者によるとHN掲載後に3万6000のIPから30万回超のアクセスがあり、600GB分のモデルが配信された"
  ],
  "sources": [
    {"title": "MicroLLM lab（README）", "publisher": "GitHub robss2020", "url": "https://github.com/robss2020/microllm-lab", "kind": "公式ドキュメント"},
    {"title": "PetitGPT Safari / Metal speedup（WRITEUP.md）", "publisher": "GitHub robss2020", "url": "https://github.com/robss2020/microllm-lab/blob/main/WRITEUP.md", "kind": "公式ドキュメント"},
    {"title": "MicroLLM lab — conversion and harness report（REPORT.md）", "publisher": "GitHub robss2020", "url": "https://github.com/robss2020/microllm-lab/blob/main/REPORT.md", "kind": "公式ドキュメント"},
    {"title": "MicroLLM lab — tiny LLMs, Q4, in your browser", "publisher": "stateofutopia.com", "url": "https://stateofutopia.com/experiments/microllmlab/", "kind": "公式発表"},
    {"title": "MicroLLM Lab – Try 7 tiny LLM's in the browser（作者の投稿とコメント）", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=49882781", "kind": "公式発表"},
    {"title": "PetitGPT", "publisher": "GitHub yangqi0", "url": "https://github.com/yangqi0/petitgpt", "kind": "公式ドキュメント"}
  ],
  "thumb_text": "MicroLLM Lab",
  "share_text": "小型LLM7種をブラウザだけで動かして比べるMicroLLM Lab。重みは4ビットで端末に保存し、入力は外に出ない",
  "editor_note": ""
}
---
GitHubでrobss2020名義の開発者は現地時間9月28日、小さな言語モデル7種をブラウザだけで動かして比べられる「MicroLLM Lab」をHacker Newsに投稿しました。モデルは2600万〜3億6000万パラメーターで、4ビットに圧縮した重みを手元のGPUで動かします。投稿は282ポイントを集め、作者によると3万6000のIPアドレスから30万回を超えるアクセスがありました。

## 何を作ったか

MicroLLM Labとは、大型のAIではなく小型言語モデル（SLM）をブラウザの中で動かし、速度と正確さを測れる実験ページです。ブラウザからGPUで計算させる規格WebGPUで動き、使えない環境ではWebAssembly、さらにJavaScriptに切り替えます。重みはブラウザ内に保存され、入力した文章は端末の外に出ません。アカウントも要りません。

画面には、チャット、決まった問題で正誤を確かめるベンチマーク、モデル同士の比較、JavaScriptで独自の評価を書ける欄があります。

| モデル | パラメーター | 4ビット版の容量 |
|---|---|---|
| PetitGPT research-v1 | 1億2460万 | 74MB |
| SmolLM2 135M Instruct | 1億3450万 | 80MB |
| L20-Edu 135M | 1億3450万 | 80MB |
| SmolLM2 360M Instruct | 3億6200万 | 216MB |
| MiniMind2 104M | 1億400万 | 62MB |
| MiniMind2 Small 26M | 2600万 | 15MB |
| GPT-2 124M | 1億2440万 | 77MB |

:::quote https://github.com/robss2020/microllm-lab | MicroLLM lab GitHub README
> A 135M network will fail arithmetic and invent facts. This lab measures that, instead of hiding it behind a chat skin.
1億3500万パラメーターのネットワークは計算を間違え、事実をでっち上げます。この実験場はそれをチャット画面の裏に隠さず、測ります。
:::

## どう作ったか

出発点は、yangqi0が1枚のRTX 4090で学習した研究用モデルPetitGPTです。作者はこれをWebGPU向けに移植し、重みを4ビットに詰める変換ツールと、複数のモデルを同じ条件で動かす仕組みを作りました。Hugging Faceにある同じ形のモデルなら、付属のスクリプトで変換して追加できます。

Mac向けには計算の割り振りを見直しました。1つの計算グループで全体を処理していたためGPUの大半が遊んでいたのを、多数のグループに分けるなどして、Mac mini M4での4ビット版の生成速度を毎秒52トークンから168トークンに上げたと記録しています。

{{card:https://stateofutopia.com/experiments/microllmlab/|MicroLLM lab（ブラウザで試す）|robss2020}}

## 成果（作者の公表値）

Mac mini M4のSafariでは、PetitGPTが「Say hello」に87ミリ秒、毎秒115トークンで答えました。SmolLM2 135M Instructは毎秒66トークンと遅いものの、20問の客観テストで14問に正解し、「2+2=4」などの問題にも答えました。

作者はHNのコメントで、投稿が約12時間トップページに載り、確認した時点で3万6000のIPアドレスから30万回を超えるリクエストがあったと書いています。配信したモデルは600GB分で、普段の2日間の訪問は1600IPほどだそうです。

## 反応と論点

HNでは、普通の質問をして「使い物にならない」と書く人や、「2+2は2」といった珍回答の報告が相次ぎました。これに対し、SLMは知識や推論が乏しく、感情の判定や分類、情報の抜き出しに使う道具で、大型モデルと比べるものではないという指摘も出ています。画面の情報が多すぎるとの声を受け、作者は冒頭に要約を置き、解説を「読まなくてよい」欄にまとめ直しました。

## 日本のビジネスへの影響

無料でブラウザから試せます。READMEに日本語の性能は示されておらず、MiniMind2は英語より中国語が得意と説明されています。日本語の業務にそのまま使う前提ではありません。

関係が深いのは、Webサービスやアプリに端末内で動くAI機能を載せたい開発者です。問い合わせの分類や振り分けを、クラウドのAPIを呼ぶ前に端末で済ませる設計を考えるとき、速度と精度の兼ね合いを利用者と同じブラウザで確かめられます。

今すぐやれることは、自社で扱う短い英文の分類問題を独自評価の欄に書き、7モデルの正答率と速度を比べることです。注意点として、作者は重要な回答には使わないよう求めています。扱える文脈は2048トークンまでで、モデルごとに15〜216MBのダウンロードが要ります。ラボのコードはApache-2.0で、重みは元のライセンス（GPT-2はMIT、ほかはApache-2.0）を引き継ぎます。小型モデルの選び方は[ローカルLLMのおすすめ](/best/local-llm/)にまとめています。
