---
{
  "title": "StrataはVRAM 12GBのゲーミングPCで125BのQwenを動かすOSS、毎秒94トークン",
  "description": "個人開発者のNiko1221が、1250億パラメーターのQwen3.8-Flash-NextをVRAM 12GBのゲーミングPCで動かす推論エンジンStrataを公開した。RTX 5070で毎秒94トークン。GitHubのスターは公開10日で8500を超えた。",
  "date": "2026-10-04T10:20:00+09:00",
  "category": "usecases",
  "tags": ["Strata", "Qwen3.8-Flash-Next", "活用事例", "個人開発", "ローカルLLM", "オープンソース"],
  "summary": [
    "Strataは、1250億パラメーターのQwen3.8-Flash-NextをVRAM 12GB以上のNVIDIAかAMDのGPUを積んだWindows・Linux機で動かすオープンソースの推論エンジン",
    "作者の計測では、RTX 5070とメモリ64GBのPCで毎秒53〜94トークンを生成し、OpenAI互換とAnthropic互換のAPIでClaude Codeなどにもつなげられる",
    "Strataは公開から10日でGitHubのスターが8500を超えたが、r/LocalLLaMAでは宣伝投稿が多すぎるとの不満も出ており、数字は作者と利用者の自己計測が中心"
  ],
  "sources": [
    {"title": "Niko1221/Strata（README）", "publisher": "GitHub Niko1221", "url": "https://github.com/Niko1221/Strata", "kind": "公式ドキュメント"},
    {"title": "How Strata works", "publisher": "GitHub Niko1221", "url": "https://github.com/Niko1221/Strata/blob/main/docs/HOW_IT_WORKS.md", "kind": "公式ドキュメント"},
    {"title": "Qwen/Qwen3.8-Flash-Next", "publisher": "Hugging Face Qwen", "url": "https://huggingface.co/Qwen/Qwen3.8-Flash-Next", "kind": "公式ドキュメント"},
    {"title": "Strata Qwen 3.8 flash next is the biggest thing since the release of Qwen 3.8 27b", "publisher": "Reddit r/LocalLLaMA", "url": "https://www.reddit.com/r/LocalLLaMA/comments/1wx1bi1/strata_qwen_38_flash_next_is_the_biggest_thing/", "kind": "コミュニティ"},
    {"title": "Anyone sitting on a lot of slow system memory and a modest GPU.. try Strata + Qwen3.8 Next.", "publisher": "Reddit r/LocalLLaMA", "url": "https://www.reddit.com/r/LocalLLaMA/comments/1wwcqas/anyone_sitting_on_a_lot_of_slow_system_memory_and/", "kind": "コミュニティ"},
    {"title": "Yes bots we get it, Strata is good now please stop", "publisher": "Reddit r/LocalLLaMA", "url": "https://www.reddit.com/r/LocalLLaMA/comments/1wwobfg/yes_bots_we_get_it_strata_is_good_now_please_stop/", "kind": "コミュニティ"},
    {"title": "The Rise of Overfit Inference Engines", "publisher": "Reddit r/LocalLLaMA", "url": "https://www.reddit.com/r/LocalLLaMA/comments/1wwu6zj/the_rise_of_overfit_inference_engines/", "kind": "コミュニティ"}
  ],
  "thumb_text": "Strata",
  "share_text": "125BのQwen3.8-Flash-NextがVRAM 12GBのゲーミングPCで毎秒94トークン。OSSの推論エンジンStrata",
  "thumb_style": "photo",
  "thumb_prompt": "A glowing gaming PC tower with a glass side panel on a teenager's desk, and inside it, instead of parts, a giant glowing brain-like cloud of light squeezed impossibly into the small case.",
  "editor_note": ""
}
---
GitHubのユーザーNiko1221が公開した推論エンジン「Strata」が、ローカルLLMの利用者の間で広がっています。1250億パラメーターのAlibabaのモデルQwen3.8-Flash-Nextを、VRAM 12GBのグラフィックカードを積んだ普通のゲーミングPCで動かし、作者の計測ではRTX 5070で毎秒94トークンを生成します。リポジトリは米国時間9月24日に作られ、10月4日時点でGitHubのスターは8500を超えました。

## 何を作ったか

Strataとは、Qwen3.8-Flash-Nextを家庭用のPCで動かすことに絞った、MITライセンスのオープンソースの推論エンジンです。対応するのはWindowsとLinuxで、NVIDIAのGeForce RTX 20〜50シリーズか、AMDのRadeon RX 7000・9000シリーズなど、VRAM 12GB以上のGPUが条件です。メインメモリは32GB以上、ディスクは約80GBを求めます。

:::quote https://github.com/Niko1221/Strata | Niko1221「Strata」README
> It chats, writes code, reads pictures and works with your apps and coding agents, and nothing leaves your PC.
チャットし、コードを書き、画像を読み、手元のアプリやコーディングエージェントとも連携します。データはPCの外に一切出ません。
:::

起動するとブラウザで `http://127.0.0.1:8080` のチャット画面が開き、同じアドレスでOpenAI互換とAnthropic互換のAPIが立ち上がります。READMEには、環境変数 `ANTHROPIC_BASE_URL` を書き換えてClaude Codeの接続先をStrataにする例が載っています。考える深さを4段階で切り替えられ、セットアップ時に選べば画像も読めます。

導入はWindowsなら `START-HERE.bat` をダブルクリックするだけです。インストーラーがGPUとメモリを調べ、入るサイズのモデル（約70GB）を落として起動します。Claude CodeやCursorなどのAIに「この手順書に従って入れて」とURLを渡す導入方法も用意されています。

{{card:https://github.com/Niko1221/Strata|Niko1221/Strata|GitHub}}

## どう動かしているか

Qwen3.8-Flash-Nextは、Hugging Faceのモデルページによると総パラメーター1250億のうち、1トークンごとに動くのは約60億だけのMoE（Mixture of Experts、専門家の混合）モデルです。Strataはこの「毎回ごく一部しか使わない」性質を使い、計算の置き場所をPC全体に割り振ります。

置き場所は3段構えです。容量の大きいSSDには大きな参照用の表を置き、メインメモリには専門家を全部載せます。そのうち呼ばれる回数が多い数千個だけをGPUに常駐させ、GPUに無い専門家はCPUがGPUと同時並行で計算します。

速度を稼ぐもう1つの工夫が投機的デコードです。小さな補助モデルが次の数語を先に書き、本体のモデルがそれをまとめて検証します。READMEによると、出力の中身は変わらず、1.6〜1.8倍速く答えが出ます。

モデルは2ビット前後まで圧縮した版を使います。圧縮版はISTA-DASLabやUnslothなどが作ったもので、エンジンの一部にはllama.cppのライブラリを使っているとREADMEに明記されています。数日前に紹介した[Slipstream](/news/20261002-slipstream-qwen38-flash-next-64gb-mac/)がMac専用でSSDから重みを読み出すのに対し、StrataはWindowsのゲーミングPCに多い「VRAMは少ないがメモリは積める」構成に合わせています。

## 成果（作者と利用者の公表値）

作者がRTX 5070（12GB）、Ryzen 5 7600、メモリ64GBのPCで測った生成速度は次のとおりです。

| サイズ | 回答の生成 | プロンプトの読み込み |
|---|---|---|
| Q2_0（最速） | 毎秒94トークン | 毎秒2650トークン |
| IQ2_XS（64GB機の推奨） | 毎秒79トークン | 毎秒2090トークン |
| IQ3_S（最も高品質） | 毎秒53トークン | 毎秒1620トークン |
| Coder（コード特化） | 毎秒55トークン | 毎秒2180トークン |

（出典：StrataのREADME。AMDのRX 9070 XTでは毎秒44〜60トークン）

r/LocalLLaMAには利用者の報告も並んでいます。RTX 3090を2枚とメモリ96GBの環境で毎秒80〜110トークン出たという投稿や、Radeon RX 7900 XTXとDDR4メモリの環境で毎秒45〜70トークンになり、同じ機械で調整したllama.cppの毎秒約22.5トークンを上回ったという投稿があります。

## 反応と論点

広がり方には反発もあります。r/LocalLLaMAには「ボットがStrataを褒める投稿ばかりだ」と不満をぶつけるスレッドが立ちました。別の投稿では、Strataのように1つのモデルや1種類のハードに絞って最適化した推論エンジンが次々に出ていると指摘し、汎用のllama.cppやvLLMとの役割分担を論じています。

READMEも制約を隠していません。同時に処理できるのは1件の依頼だけで、会話の最初のメッセージは3万トークンあたり約1分かけて読み込みます。モデルの起動中は1〜3分ほどPCが重くなる、または反応しなくなるとも書いています。

## 日本のビジネスへの影響

必要なのは、VRAM 12GB以上のGPUとメモリ32GB以上（推奨64GB）を積んだWindowsかLinuxのPCです。日本語の性能についてREADMEに記載はなく、Qwen3.8-Flash-Nextのモデルページにも日本語の評価は見当たりません。注意したいのはコード特化のCoder版で、READMEは中国語を含むCJK（中国語・日本語・韓国語）の文章が弱いとして、それらには通常版を勧めています。日本語で使うならQ2_0かIQ2_XS、IQ3_Sを選びます。

向いているのは、ソースコードや顧客資料を社外のAIに送れない会社の開発者と情報システム担当です。社内にある開発用やゲーム用のPC 1台で、100B級のモデルをAPIとして立てられます。今すぐやれることは、メモリ64GBのPCにIQ2_XS版を入れ、Claude Codeの接続先をStrataに替えて、普段のコード修正を数件クラウドのモデルと比べることです。

注意点は3つあります。まず、エンジンはMITですが、モデルにはQwenのコミュニティライセンスなど別の条件が付くので、商用で使う前に確かめます。次に、1件ずつしか処理できないため、部署で共有するサーバーには向きません。最後に、速度の数字は作者と利用者の自己計測で、正確さを第三者が比べた結果はまだありません。手元で動かす選択肢全体は[ローカルLLM・オープンウェイトモデルのおすすめ](/best/local-llm/)で比べています。
