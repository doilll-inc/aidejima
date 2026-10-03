---
{
  "title": "ds4はRedis作者が作るローカルLLMエンジン、128GBのMacでDeepSeek V4 Flashが動く",
  "description": "Redis作者antirezが開発する推論エンジンds4の解説サイトがHacker Newsで230ポイントを集めた。少数の大型オープンモデルに絞り、128GBのMacで2ビット版DeepSeek V4 Flashを毎秒39トークンで動かす。",
  "date": "2026-10-03T19:20:00+09:00",
  "category": "usecases",
  "tags": ["DwarfStar 4", "DeepSeek V4 Flash", "活用事例", "個人開発", "ローカルLLM", "オープンソース"],
  "summary": [
    "DwarfStar 4（ds4）は、Redisの作者antirezがC言語で書く、少数の大型オープンモデル専用のローカル推論エンジン",
    "メモリ128GBのM5 Maxで、2ビット量子化したDeepSeek V4 Flashを毎秒39.4トークンで生成する（作者の計測）",
    "9月の更新でQwen3.8 Flash Nextに対応し、一部をSSDから読み出すことで64GBのMacでも動かせるようになった"
  ],
  "sources": [
    {"title": "antirez/ds4（README）", "publisher": "GitHub antirez", "url": "https://github.com/antirez/ds4", "kind": "公式サイト"},
    {"title": "ds4 Performance", "publisher": "GitHub antirez", "url": "https://github.com/antirez/ds4/blob/main/docs/PERFORMANCE.md", "kind": "公式サイト"},
    {"title": "antirez の投稿（ds4の公開）", "publisher": "X @antirez", "url": "https://x.com/antirez/status/2052405820235678175", "kind": "X投稿"},
    {"title": "DwarfStar 4 (ds4): Local DeepSeek V4.1, Qwen and GLM", "publisher": "dwarfstar.sh（コミュニティ運営）", "url": "https://dwarfstar.sh/", "kind": "コミュニティ"},
    {"title": "ds4 September 2026: DeepSeek V4.1 and Qwen3.8 Flash Next", "publisher": "dwarfstar.sh（コミュニティ運営）", "url": "https://dwarfstar.sh/blog/ds4-september-v41-qwen38-and-a-bigger-runtime/", "kind": "コミュニティ"},
    {"title": "From the creator of Redis; run LLM locally with ds4", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=49936575"}
  ],
  "thumb_text": "ds4",
  "share_text": "Redis作者antirezのds4。128GBのMacで2ビット化したDeepSeek V4 Flashを毎秒39トークンで動かすC製の推論エンジン",
  "editor_note": ""
}
---
データベースRedisの作者として知られるSalvatore Sanfilippo氏（antirez）が開発するローカルLLMの推論エンジン「DwarfStar 4（ds4）」が、改めて注目を集めています。米国時間10月2日、有志が運営する解説サイトdwarfstar.shがHacker Newsに投稿され、230ポイントを集めました。メモリ128GBのMacで、2ビットに圧縮したDeepSeek V4 Flashを毎秒39.4トークンで動かせるとしています。

## 何を作ったか

ds4とは、数種類の大型オープンウェイトモデルを手元のパソコンで動かすことだけに絞った、C言語製の推論エンジンです。対応するのはDeepSeek V4 Flash・V4.1 Flash・V4 PRO、Zhipu AIのGLM 5.2・5.3・5.3 Flash、AlibabaのQwen3.8 Flash Nextです。何でも読み込める汎用のツールではなく、プロジェクトが自分で作ったモデルファイル（GGUF）だけを使います。

始まりは5月です。antirez氏はXで、DeepSeek V4 Flash専用の推論エンジンとして公開を告知し、土台になったllama.cppとGGMLの開発者に謝意を示しました。GitHubのスターはその後の5カ月で2万3000を超えています。

{{x:https://x.com/antirez/status/2052405820235678175}}

1つのエンジンで、対話用のコマンド `./ds4`、OpenAIとAnthropicの形式に対応したAPIサーバー `./ds4-server`、エンジンを内蔵したコーディングエージェント `./ds4-agent` の3つを使えます。APIサーバー経由で、Claude CodeやCodex CLIなどのコーディングツールにもつなげられます。ライセンスはMITです。

## どう作ったか

READMEは、なぜ今これが可能になったのかを最初に挙げています。

:::quote https://github.com/antirez/ds4 | antirez「ds4」README
> Capable open-weight models now fit on high-end personal machines.
高性能なオープンウェイトモデルが、ハイエンドの個人向けマシンに収まるようになった。
:::

工夫の柱は3つです。

- **非対称の2ビット量子化**: 2840億パラメーターのDeepSeek V4 Flashのうち、MoE（専門家の混合）の個々の「専門家」の重みは強く圧縮し、全体で共有する重要な経路は精度を保つ
- **KVキャッシュをSSDに保存**: 長い会話の途中経過をディスクに書き出し、再起動しても最初から読み直さずに済む
- **SSDからの読み出し**: メモリに入りきらないモデルは、必要な部分だけをSSDから読む

開発の進め方も特徴的です。READMEは、コーディングAIの強い助けを借りて書き、構想・テスト・デバッグは人が主導していると明記しています。antirez氏は、利用者自身がコーディングエージェントを使って自分のハードウェア向けにds4を改造することを勧めています。antirez氏はHacker Newsのコメントで、C言語を選んだ理由の1つに、AIが質の高いCのコードを書きやすいことを挙げています。

## 成果（作者の公表値）

リポジトリの性能ページには、2ビット版のDeepSeek V4 Flashでの計測が載っています。

| マシン | 文脈の長さ | 入力の処理 | 生成 |
|---|---|---|---|
| M5 Max（128GB） | 2,048トークン | 毎秒790.18トークン | 毎秒39.35トークン |
| M5 Max（128GB） | 65,536トークン | 毎秒398.50トークン | 毎秒27.64トークン |
| DGX Spark（128GB） | 2,048トークン | 毎秒825.76トークン | 毎秒18.05トークン |

（出典：antirez/ds4のdocs/PERFORMANCE.md）

9月の更新では、Qwen3.8 Flash Nextに対応しました。41.73GiBの重みだけをメモリに置き、95.37GiBある語句の表はSSDから直接読むため、64GBのMacが入り口になります。NVIDIAのL40Sを8枚使った構成では、16人の同時利用で合計毎秒約126トークンに達したとしています。

Hacker Newsでは、対応モデルを絞ったぶん「少数のモデルを本当にうまく動かす」と評価する声がありました。一方で、llama.cppとの違いが小さいのではという疑問や、解説サイトの文章がAIで量産したように見えるという批判も出ています。

## 日本のビジネスへの影響

必要なのは、メモリ96GB以上のApple Silicon搭載Mac（READMEの推奨）か、DGX Spark、AMDのStrix Halo搭載機です。Qwen3.8 Flash Nextなら64GBのMacから試せます。モデルファイルは大きく、Qwen3.8の2ビット版でも137.10GiBを落とすため、速いSSDに十分な空きが要ります。

向いているのは、社外にコードを出せない会社の開発者です。手順は、リポジトリを取得して `make` でビルドし、`./download_model.sh ds4f-q2` でモデルを落として `./ds4-server` を起動するだけです。社内のコーディングツールの接続先をこのサーバーに向ければ、クラウドに送らずにエージェントを動かせます。まずは普段の作業を数件流し、クラウドのモデルと答えの質と速さを比べるところから始めます。

注意点は3つあります。READMEは現状をベータ品質と明記しており、変更も速いです。モデルのライセンスはエンジンのMITとは別で、DeepSeek・GLM・Qwenのそれぞれの条件を確かめる必要があります。また、2ビットまで圧縮したモデルは元のモデルと同じ精度ではないため、日本語の文章や業務の答えの質は自分で確かめてください。手元でモデルを動かす選択肢は[ローカルLLM・オープンウェイトモデルのおすすめ](/best/local-llm/)にまとめています。
