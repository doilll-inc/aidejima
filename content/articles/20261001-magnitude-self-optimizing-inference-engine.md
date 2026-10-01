---
{
  "title": "Magnitudeがエージェント向け推論エンジンを発表、端末上で自動調整しMacで92%高速",
  "description": "YC出身のMagnitudeが、手元のPCでAIエージェント用のモデルを動かすオープンソースの推論エンジンを公開した。カーネルを端末上で調整し、同社の計測ではMacの生成速度がllama.cppより92%速い。Claude CodeやCodexにもつながる。",
  "date": "2026-10-01T17:47:00+09:00",
  "category": "usecases",
  "tags": ["Magnitude", "ローカルLLM", "オープンソース", "エージェント", "スタートアップ", "活用事例"],
  "summary": [
    "YC 2025年夏期出身のMagnitudeが、AIエージェント向けのオープンソース推論エンジンをLaunch HNで発表した",
    "モデルを動かす前にGPUカーネルを端末上で約1分かけて調整し、同社の計測ではMacの生成速度がllama.cppより92%速い",
    "Claude CodeやCodexなど既存のエージェントに1クリックでつながるが、複数GPUには未対応で、速度が逆転したとの報告もある"
  ],
  "sources": [
    {"title": "Launch HN: Magnitude (YC S25) – Self-optimizing inference engine for agents", "publisher": "Hacker News（創業者の投稿）", "url": "https://news.ycombinator.com/item?id=49911995", "kind": "公式発表"},
    {"title": "magnitudedev/magnitude", "publisher": "GitHub magnitudedev", "url": "https://github.com/magnitudedev/magnitude", "kind": "公式ドキュメント"},
    {"title": "Run open models as fast as your hardware allows", "publisher": "Magnitude", "url": "https://magnitude.dev/", "kind": "公式発表"},
    {"title": "Browse open models", "publisher": "Magnitude", "url": "https://magnitude.dev/models", "kind": "公式ドキュメント"},
    {"title": "Magnitude HN Demo", "publisher": "Magnitude（YouTube）", "url": "https://www.youtube.com/watch?v=0qE8BWEZu7o", "kind": "公式発表"},
    {"title": "Magnitude: Run open models as fast as your hardware allows", "publisher": "Y Combinator", "url": "https://www.ycombinator.com/companies/magnitude", "kind": "公式発表"}
  ],
  "thumb_text": "Magnitude",
  "share_text": "YC出身のMagnitudeが、端末に合わせて自分を調整するエージェント向け推論エンジンを公開。Macでllama.cppより92%速いと主張",
  "editor_note": ""
}
---
米Y Combinator（2025年夏期）出身のMagnitudeは現地時間9月30日、AIエージェントが使うモデルを手元のパソコンで動かすためのオープンソースの推論エンジン「Magnitude」を、Hacker Newsの「Launch HN」で発表しました。モデルを動かす前に、計算の部品を自分のパソコンに合わせて調整するのが特徴です。同社の計測では、Mac（M4 Pro）での文章の生成速度がllama.cppより92%速くなりました。

## 何を作ったか

推論エンジンとは、公開されているAIモデル（オープンウェイトモデル）を自分のハードウェアで動かすためのソフトです。llama.cpp、Ollama、LM Studioがよく知られています。Magnitudeはこの分野に、エージェント用途に絞って参入しました。

製品はmacOS・Windows・Linux向けのデスクトップアプリです。おすすめのモデルを選んでダウンロードし、使っているエージェントにつなぐだけで使えます。README（説明書）によると、Pi、OpenCode、Hermes、OpenClaw、Codex、Claude Code、Oh My Pi、Clineには1クリックで接続でき、それ以外もOpenAI互換のAPIでつながります。エージェントがモデルを必要としたときだけ起動し、使われなくなると止まります。

{{youtube:https://www.youtube.com/watch?v=0qE8BWEZu7o}}

ライセンスはApache 2.0で、無料です。モデルをダウンロードした後はネット接続が不要で、プロンプトもファイルも手元から出ません。公式のカタログには10月1日時点でQwenやGemmaなど15モデルが並んでいます。

{{card:https://github.com/magnitudedev/magnitude|magnitudedev/magnitude|Magnitude（GitHub）}}

## どう作ったか

創業者のAnders Lie氏とTom Greenwald氏は、以前にオープンソースのブラウザ操作エージェントを作り、GitHubで4,000以上のスターを集めました。それをローカルのモデルで動かそうとしたところ、合う推論エンジンがなかったのが出発点だと、Launch HNの投稿で説明しています。既存のエンジンは、データセンターでのまとめ処理向けか、幅広い機器で動くことを優先したものか、特定の機器向けで機能が足りないものに分かれる、という見立てです。

:::quote https://github.com/magnitudedev/magnitude | Magnitude公式リポジトリ（README）
> They ship kernels precompiled for broad classes of hardware. Magnitude compiles and tunes its kernels on your actual device before a model runs, so they fit your exact chip.
（ほかのエンジンは）幅広い種類のハードウェア向けに事前にビルドしたカーネルを配っています。Magnitudeはモデルを動かす前に、実際の端末の上でカーネルをコンパイル・調整するので、そのチップにぴったり合います。
:::

カーネルとは、GPUで行列計算などを実行する小さなプログラムです。Magnitudeは調整できる値を残した形でカーネルを書き、端末上で最適な値を探します。この調整は、新しいモデルをダウンロードするたびに1回、約1分かかると創業者はHNで答えています。開発はRust製で、カーネルの最適化には複数のコーディングエージェントを並行して走らせているとも明かしました。

エージェント向けの工夫もあります。最初はモデルの重みの分だけメモリを確保し、会話が長くなれば増やし、エージェントが止まれば解放します。同時に動く複数のセッションで共通部分の計算結果（プレフィックスキャッシュ）を共有し、会話の記憶（KVキャッシュ）は圧縮して保存します。

## 成果（同社が公表した数字）

条件は、Qwen 3.6 35B A3B（4ビット）、文脈長6万4,000トークン、投機的デコード（小さなモデルで先読みして速くする手法）なしです。

| 機器 | 生成速度（tok/s） | 読み込み速度（tok/s） | エージェント1つあたりのメモリ |
|---|---|---|---|
| Mac M4 Pro 48GB | 30→57（+92%） | 466→507（+9%） | 28%減 |
| NVIDIA DGX Spark | 49→58（+19%） | 2,033→2,507（+23%） | 27%減 |

比較相手はllama.cppです。リポジトリのスターは10月1日時点で約5,800でした。

## 反応と論点

HNの投稿は157ポイントを集めました。調整が約1分で済む点を評価する声がある一方、厳しい指摘も並びます。「llama.cppに勝つのは低いハードル」で、Macにはもっと速いエンジンがあるという意見や、RTX 5070 Tiではllama.cppの方が20〜30%速かった、M5 Maxでは読み込みも生成もllama.cppが約2倍速かったという報告です。創業者は、M5以降の新しい行列演算を使い切れていない可能性を認め、改善すると答えました。

現時点では複数のGPUを束ねる構成に対応していません。今後は、大きなモデルの一部をメモリやディスクに置いて必要なときだけ読み込む機能などを予定しています。収益化は、将来ローカルとクラウドを行き来できる推論クラウドを作り、トークン単位で課金する構想だと説明しています。

## 日本のビジネスへの影響

Magnitudeは無料で、日本からもダウンロードできます。公式サイトとドキュメントは英語です。

関係が深いのは、社外に出せないコードや文書をAIエージェントで扱いたい開発者と、情報システム部門です。手元のMacやGPUマシンでモデルを動かし、Claude CodeやCodexのつなぎ先をローカルに切り替えられれば、機密性の高い作業だけを社内で完結させる使い分けができます。

今すぐやれるのは、普段使っている機器で、同じモデルをllama.cppやOllamaとMagnitudeの両方で動かし、速度とメモリを比べることです。公表値はM4 ProとDGX Sparkのもので、ほかの機器では逆の結果も報告されています。

注意点として、バージョンは0.2系で、公開直後から不具合の報告が出ています。業務に組み込むのは、自社の機器で検証してからにしてください。ローカルでモデルを動かす選択肢は「[ローカルLLM・オープンウェイトモデルのおすすめ](/best/local-llm/)」にまとめています。
