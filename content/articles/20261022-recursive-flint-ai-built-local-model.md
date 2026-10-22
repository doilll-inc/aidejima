---
{
  "title": "AIが開発のほぼ全工程を手伝ったAI「Flint」を無料公開、ノートPCでネットなしに動く 4か月で完成",
  "description": "米新興企業Recursiveは、自社の自動研究システムが設計から高速化までほぼ全工程に関わったプログラミング用AI「Flint」を無料で公開した。少人数のチームが4か月足らずで一から作り、MacBook Proで毎秒125語以上を出せるという。",
  "date": "2026-10-22T18:40:00+09:00",
  "category": "dev",
  "tags": ["Recursive", "Recursive Flint", "ローカルLLM", "オープンウェイト", "コーディング", "エージェント"],
  "summary": [
    "米新興企業Recursiveは10月21日、プログラミング用のAI「Flint」を無料で公開した。手元のノートPCで、ネットにつながずに動く",
    "開発では同社の自動研究システム「Eureka Machine」が、AIの設計から軽量化、高速化までほぼすべての工程に関わった",
    "少人数のチームが4か月足らずで一から作った。AIがAIを作る「自己改善」の実地試験として注目と警戒の両方を集めている"
  ],
  "sources": [
    {"title": "Introducing Flint", "publisher": "Recursive", "url": "https://www.recursive.com/updates/introducing-recursive-flint", "kind": "公式サイト"},
    {"title": "RecursiveSI/flint", "publisher": "Hugging Face", "url": "https://huggingface.co/RecursiveSI/flint", "kind": "公式ドキュメント"},
    {"title": "Richard Socher の投稿", "publisher": "X @RichardSocher", "url": "https://x.com/RichardSocher/status/2112944385415426249", "kind": "X投稿"},
    {"title": "Recursive launches Flint, a laptop coding model it says was largely built by AI", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/10/21/recursive-launches-flint-a-laptop-coding-model-it-says-was-largely-built-by-ai/", "kind": "報道"},
    {"title": "This Startup Is All In on Recursive Self-Improvement. Its Latest Model Is Scary Good", "publisher": "WIRED", "url": "https://www.wired.com/story/recursive-self-improvement-flint-latest-model-scary-good/", "kind": "報道"}
  ],
  "thumb_prompt": "A miniature workshop on a desk where tiny robot figures in lab coats are assembling a glowing laptop-sized machine on a workbench, while one lone human figure stands aside holding a clipboard and watching; the laptop next to the workshop shows no internet signal.",
  "thumb_style": "diorama",
  "thumb_text": "Recursive Flint",
  "share_text": "AIが開発のほぼ全工程を手伝ったAI「Flint」が無料公開。ノートPCでネットなしに動き、少人数で4か月で完成",
  "editor_note": ""
}
---
米国の新興企業Recursiveは現地時間10月21日、プログラミング用のAI「Flint」を無料で公開しました。開発では同社の自動研究システム「Eureka Machine」が、AIの設計から軽量化、高速化までほぼすべての工程に関わり、少人数のチームが4か月足らずで一から作り上げたといいます。完成したFlintは手元のノートPCで、ネットにつながずに動きます。

## 何が発表されたか

Flintとは、プログラムの不具合の修正や機能の追加、テストの作成といった開発作業を任せるためのAIです。中身のデータ（重み）が公開されている「オープンウェイト」型で、AI共有サイトのHugging Faceから誰でもダウンロードできます。ライセンスは商用利用も認めるApache 2.0です。

手元のPCで動くため、社外のサーバーにコードを送らずに済み、使った量に応じたAPI料金もかかりません。同社によると、AppleのM4 Proを積んだMacBook Proで毎秒125語（トークン）以上、NVIDIAの小型AIマシン「RTX Spark」では毎秒150語以上を生成し、同程度の大きさのAIと比べて最大2倍速いとしています。

速さの理由は作りにあります。Flintは全体で約400億個の部品（パラメーター）を持ちますが、1語を出すたびに使うのはそのうち約25億個だけです。必要な専門家だけを呼び出す「混合エキスパート」と呼ばれる方式で、同社はソフトの不具合修正などを測る試験で、同じ規模（500億未満）の同方式のAIの中で最も高い成績だったとしています。

開発体制について、同社は公式ブログで次のように書いています。

:::quote https://www.recursive.com/updates/introducing-recursive-flint | Recursive公式ブログ「Introducing Flint」
> Our small team of people and agents built it from scratch in under four months.
私たちの少人数の人間とエージェント（自律的に動くAI）のチームが、4か月足らずでこれを一から作りました。
:::

{{card:https://huggingface.co/RecursiveSI/flint|RecursiveSI/flint|Hugging Face}}

## AIはどこを手伝ったのか

Eureka Machineとは、アイデアを出し、実装し、試し、その結果から次に何を試すかを決めるという研究の一連の流れを自動で回すシステムです。複数の方向を並行して探り、うまくいった工夫を組み合わせていきます。公式ブログは、Flintで実際にAIが担った例を3つ挙げています。

- **設計**: 1語ごとに使う部品を減らして速くするため、専門家の数や幅の組み合わせを探索し、「全体400億・使うのは25億」という形を選んだ
- **軽量化**: 一般的なやり方に反して、出力を担う部分まで4ビットに縮め、性能の落ち込みを補う追加の訓練方法も自分で見つけた。訓練の手数は従来の方法のほぼ半分になり、縮めた版の成績は元の版と1点未満の差に収まった
- **高速化**: AppleのチップやNVIDIAの機器で動かすための専用プログラムを、機種に合わせて書き起こした

TechCrunchによると、こうした工夫によってモデルの大きさは71%小さくなったといいます。ただし、AIのおかげで研究者の作業時間がどれだけ減ったかは公表していません。

## 背景

Recursiveは、米Salesforceで研究部門のトップを務めたリチャード・ソーチャー氏が率いる会社です。TechCrunchは、同社が5月に6億5,000万ドルを調達し、評価額は46億5,000万ドルだったと報じています。社名のとおり「AIが自分より優れたAIを作り、それがさらに優れたAIを作る」という再帰的な自己改善を目標に掲げ、Flintはその最初の実地試験という位置づけです。

AIに研究そのものを任せる動きはほかの大手にも広がっています。TechCrunchは、OpenAIが9月に、社内のAIエージェントの作業量が8月半ばの時点で人間の研究者1人の勤務1日あたり3.1日分に達したと説明したことも紹介しています。

## 反応と論点

ソーチャー氏はXでFlintを紹介し、自社の自動研究システムで作った、手元で速く動くプログラミング用AIだと説明しています。

{{x:https://x.com/RichardSocher/status/2112944385415426249}}

TechCrunchによると、米WIREDの記者がメモリ48GBのMacでFlintを試し、やることリストのアプリやWeb上の情報を集める道具を作らせたところ、頼んだ作業を毎回こなしたといいます。小型のプログラミング用AIはエラーを出したり遅かったりしがちだった、という比較も紹介されています。

一方で、Recursive自身も限界を認めています。ClaudeやCodexのような大型の有料サービスより細かい指示が必要で、大きな作業は小さく分けて頼むよう勧めています。また、AIがAIを改良し続ける「自己改善」は、人の手を離れて制御できなくなることを心配する研究者も多い考え方です。TechCrunchは、今回の仕組みは人が監督する研究の助手にとどまると書き、ソーチャー氏も、人が監督していつでも止められる形を目指すとWIREDに語ったと伝えられています。

## 日本のビジネスへの影響

**使えるか**: Flintは無料で、日本からもダウンロードできます。商用利用もできるライセンスです。ただし主な想定はプログラミングで、日本語の文章作成やビジネス文書の品質については公式の説明がありません。公式の速度はM4 Pro搭載のMacBook Proで測ったもので、WIREDの記者もメモリ48GBのMacで試しています。一般的な事務用ノートPCで同じ速さが出るとは限りません。

**誰にどう効くか**: 社内のシステム担当者や、ソースコードを社外のAIサービスに送れない受託開発の会社に向きます。経営者にとっては、AIの開発そのものをAIが担い、少人数・短期間で新しいモデルが出てくる流れが速まっていることを示す例です。

**今すぐやれること**: 社外にコードを出せない案件を抱える開発チームは、余っているMacで小さな修正作業を試し、クラウドのAIとの差を見てみる価値があります。手元で動くAIの選び方は[ローカルLLM・オープンウェイトモデルのおすすめ](/best/local-llm/)で比較しています。同じく手元で動くAIとしては、Metaが[Mac 2台で動く大型モデル](/news/20261016-meta-muse-spark-open-mac-studio/)を公開しています。

**注意点**: 性能の数字はRecursive自身の測定によるもので、第三者の評価はこれからです。AIが書いたコードは必ず人が確認してから使い、社内の機器に入れる際は情報システム部門の許可を取る必要があります。
