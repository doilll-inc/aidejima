---
{
  "title": "Slipstreamは64GBのMacで95.5GiBのQwenを動かすOSS、llama.cppの1.76倍の速さ",
  "description": "個人開発者がApple Silicon向けの推論エンジンSlipstreamを公開した。メモリに入らない95.5GiBのQwen3.8-Flash-Nextを、専門家の重みをSSDから読み出して64GBのMacで毎秒41〜52トークンで動かす。",
  "date": "2026-10-02T20:10:00+09:00",
  "category": "usecases",
  "tags": ["Slipstream", "Qwen3.8-Flash-Next", "活用事例", "個人開発", "ローカルLLM", "オープンソース"],
  "summary": [
    "Slipstreamは、メモリより大きいMoEモデルの重みをSSDから必要な分だけ読み込み、64GBのMacで動かすC++とMetal製の推論エンジン",
    "作者の計測では、95.5GiBのQwen3.8-Flash-Nextを毎秒41〜52トークンで生成し、llama.cppの改造版より平均1.76倍速い",
    "OpenAI互換のAPIで社内のコーディングエージェントにもつなげられるが、検証はM5 Pro搭載のMacBook Pro 1台だけ"
  ],
  "sources": [
    {"title": "npanj/slipstream（README）", "publisher": "GitHub npanj", "url": "https://github.com/npanj/slipstream", "kind": "公式ドキュメント"},
    {"title": "nitinpanj/Swift-Qwen3.8-Flash-Next-Q4_0-Q8out-v3-GGUF", "publisher": "Hugging Face", "url": "https://huggingface.co/nitinpanj/Swift-Qwen3.8-Flash-Next-Q4_0-Q8out-v3-GGUF", "kind": "公式サイト"},
    {"title": "nitinpanj/qwen38-flash-next-v3", "publisher": "Hugging Face", "url": "https://huggingface.co/nitinpanj/qwen38-flash-next-v3", "kind": "公式サイト"},
    {"title": "Running 95.5 GiB Qwen3.8-Flash-Next at 41–52 tok/s on a 64GB Mac (1.76x faster than llama.cpp)", "publisher": "Reddit r/LocalLLaMA", "url": "https://www.reddit.com/r/LocalLLaMA/comments/1wva7l2/running_955_gib_qwen38flashnext_at_4152_toks_on_a/", "kind": "コミュニティ"}
  ],
  "thumb_text": "Slipstream",
  "share_text": "64GBのMacで95.5GiBのQwen3.8-Flash-Nextを毎秒41〜52トークンで。SSDから重みを流す推論エンジンSlipstream",
  "editor_note": ""
}
---
GitHubのユーザーnpanjが、メモリに収まらない大きな言語モデルをMacで動かす推論エンジン「Slipstream」をオープンソースで公開しました。95.5GiB（約103GB）あるAlibabaのQwen3.8-Flash-Nextを、メモリ64GBのMacで毎秒41〜52トークンの速さで動かせるとしています。作者は米国時間10月1日、Redditのローカル LLM 系コミュニティr/LocalLLaMAで公開を告知しました。

## 何を作ったか

Slipstreamとは、Apple Silicon（Mチップ）のMac専用に、C++とAppleのGPU向け言語Metalで書かれた推論エンジンです。ふつう、モデルを動かすには重みをすべてメモリに載せる必要があり、64GBのMacに約100GBのモデルは入りません。Slipstreamは、入りきらない分をSSDに置いたまま、必要になった部分だけを読み出します。

これができるのは、Qwen3.8-Flash-NextがMoE（Mixture of Experts、専門家の混合）という作りだからです。READMEによると、このモデルは全体で1257億パラメーターあり、512の「専門家」に分かれていますが、1トークンを作るときに使うのは73億パラメーター分だけです。毎回使う専門家だけを読めば、全体をメモリに載せなくても計算できます。

{{card:https://github.com/npanj/slipstream|npanj/slipstream|GitHub}}

起動するとOpenAI互換のAPIサーバーになり、OpenAIのSDKやcurlからそのまま呼べます。READMEには、ターミナルで動くコーディングエージェントにつなぐ例も載っています。ライセンスはApache-2.0です。

## どう作ったか

速さを出す工夫は大きく3つです。

- **SSDからの専門家の読み出しと先読み**: 次に使いそうな専門家を予測して、計算より先にSSDから読み込んでおく
- **投機的デコード**: 小さな仕組みで先に何トークンか下書きし、本体のモデルでまとめて確かめる。プロンプト中の同じ語句の並びを使う方式と、モデルに組み込まれた複数トークン予測（MTP）を組み合わせる
- **長い文脈でも遅くなりにくいモデルを選ぶ**: Qwen3.8-Flash-Nextは64層のうち48層が、文脈が伸びても記憶量が増えない方式の層で、全文脈を見る層は16層だけ

土台にしたのは、別のオープンソースプロジェクトSplashのMetal向けの設計です。作者はREADMEで、Splashの作者らへの謝辞とともに、今回の拡張を元のプロジェクトへ提案する予定だと書いています。

:::quote https://github.com/npanj/slipstream | npanj「Slipstream」README
> It combines SSD expert streaming with predictive read-ahead and Prompt Lookup + MTP speculative drafting to serve frontier-scale models that exceed your Mac's physical RAM.
SSDからの専門家の読み出しに、予測による先読みと、プロンプト参照とMTPによる投機的な下書きを組み合わせ、Macの物理メモリを超える最先端規模のモデルを動かします。
:::

使う手順は、リポジトリを取得してビルドし、Hugging Faceからモデルを落として起動するだけです。ただしmacOSは64GBのMacでGPUが使えるメモリを約48GiBに制限しているため、コマンドで58GiBまで引き上げる手順が必要です。モデルの保存に約100GB、作業用にさらに約95GBのディスクも要ります。初回は変換に5〜7分かかり、2回目以降は10〜15秒で立ち上がるとしています。

## 成果（作者の公表値）

作者はM5 Proを積んだメモリ64GBのMacBook Proで、llama.cppを改造した版と比べました。数学・論理・Python・Rust・技術解説の6種類の課題で、生成速度の平均は改造版の毎秒23.1トークンに対しSlipstreamは毎秒40.8トークンで、1.76倍でした。最初の1文字が出るまでの時間も、平均1.86秒から1.29秒に縮んでいます。

| 文脈の長さ | 平均の生成速度 |
|---|---|
| 1000トークン未満 | 毎秒41.5トークン |
| 1万6000〜3万2000トークン | 毎秒38.2トークン |
| 6万4000〜9万6000トークン | 毎秒32.4トークン |
| 9万6000〜13万トークン | 毎秒32.9トークン |

（出典：SlipstreamのREADME。作者がエージェントの実利用で計測した3086回分の記録から一部を抜粋）

長い文脈でも速度が大きく落ちない点を、作者は強調しています。13万トークン近い文脈は、資料をまとめて読ませるエージェントでは珍しくない長さです。

## 日本のビジネスへの影響

必要なのは、メモリ64GBのApple Silicon搭載Mac（M2〜M5のPro・Max）と、約200GBの空きディスクです。Hugging Faceのモデルページで対応言語に挙がっているのは英語と中国語で、日本語の性能についてはREADMEに記載がありません。推奨モデルのライセンスはQwenのコミュニティライセンスで、Apache-2.0なのはエンジン側だけです。商用で使うなら、モデル側の条件を別に確かめる必要があります。

向いているのは、社外にコードや資料を出せない会社の開発者や情報システム担当です。100B級のモデルを手元のMac 1台で動かし、OpenAI互換のAPIで社内のツールにつなげられます。今すぐやれることは、64GBのMacがあればREADMEの手順でサーバーを立て、社内のよくある質問やコードレビューを数件流して、クラウドのAPIと答えの質や速さを比べることです。

注意点は、検証の範囲がまだ狭いことです。作者自身が、試したのはM5 Proのマシン1台だけで、NVIDIAやAMDのGPUでは動かしていないと書いています。性能の数字もすべて作者の計測で、正答率の比較は145問の小さな問題集によるものです。リポジトリは9月25日に作られたばかりで、GitHubのスターも一桁です。業務に組み込むなら、まず検証用のMacで試すにとどめ、必要ならLM StudioやOllamaのような定番ツールと並べて比べます。手元でモデルを動かす選択肢は[ローカルLLM・オープンウェイトモデルのおすすめ](/best/local-llm/)にまとめています。
