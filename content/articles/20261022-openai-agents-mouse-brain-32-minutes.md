---
{
  "title": "数か月分の脳データの読み解きをAIが32分で、OpenAIが数千体のAIに手分けさせ新しい手がかりを発見",
  "description": "OpenAIが研究機関と組み、数千体のAIエージェントにマウスの脳細胞のデータを手分けして読み解かせた。人なら数か月から1年かかる作業を32分で終え、アルツハイマー病などにつながる新しい手がかりを見つけた。結果は研究者向けに無料公開された。",
  "date": "2026-10-22T23:40:00+09:00",
  "category": "research",
  "tags": ["OpenAI", "GPT-Rosalind", "エージェント", "医療", "PerturbAI", "論文"],
  "summary": [
    "OpenAIが研究機関2社と組み、数千体のAIエージェントにマウスの脳細胞のデータを手分けして解析させた",
    "人なら数か月から1年かかる読み解きを32分で終え、脳の病気につながりうる新しい手がかりを見つけた",
    "1体のAIに全部やらせるより、手分けさせたほうが引用した論文は700本超と多く、専門家も7割以上がその結果を選んだ"
  ],
  "sources": [
    {"title": "Using thousands of AI agents to uncover new leads in biological data", "publisher": "OpenAI", "url": "https://openai.com/index/scaling-ai-research-for-complex-biological-data/", "kind": "公式発表"},
    {"title": "distributed_agent（reasoning atlas）", "publisher": "GitHub jinlabneurogenomics", "url": "https://github.com/jinlabneurogenomics/distributed_agent", "kind": "公式ドキュメント"},
    {"title": "OpenAI agents analyze mouse brain data in 32 minutes, a job that would take humans months", "publisher": "The Decoder", "url": "https://the-decoder.com/openai-agents-analyze-mouse-brain-data-in-32-minutes-a-job-that-would-take-humans-months/", "kind": "報道"}
  ],
  "thumb_prompt": "A huge wall of glowing data tiles about brain cells, with hundreds of tiny identical robot figures each reading one tile at the same time, and a single clock on the wall showing just past the half-hour.",
  "thumb_style": "photo",
  "thumb_text": "AIが32分で解析",
  "share_text": "人なら数か月の脳データの読み解きを、数千体のAIが手分けして32分で。OpenAIが新しい手がかりを発見",
  "editor_note": ""
}
---
OpenAIは現地時間10月22日、研究機関のPerturbAIおよびScripps Researchと組み、数千体のAIエージェント（自分で調べて考えるAI）に手分けさせて、マウスの脳細胞の大量のデータをわずか32分で読み解いた研究を公表しました。人が同じ作業をすると数か月から1年かかる見込みで、AIはアルツハイマー病やパーキンソン病につながりうる新しい手がかりを見つけました。結果は研究者が今日から使える形で無料公開されています。

## 何をしたのか

素材になったのは「全脳CRISPRアトラス」と呼ばれる既存のデータです。マウスの脳で遺伝子を1つずつ働かなくし、脳のさまざまな種類の細胞がそれぞれどう変わったかを、何百万個もの細胞について記録した地図のようなものです。遺伝子の操作は何千通りもあり、研究者が1つずつ論文と照らし合わせて意味を探るには多すぎました。

そこでOpenAIは、仕事を遺伝子の操作ごとに切り分けました。受け持つのは、生命科学向けのモデル「GPT-Rosalind」で動くAIエージェントで、1体につき1つの操作です。各AIは担当分のデータを見て、関係しそうな論文を探し、なぜその変化が起きたのかの仮説を書きます。数千体分の報告は1つにまとめられ、遺伝子から細胞の変化、根拠の論文、考えられる仕組みまでをたどれる「推論アトラス」として公開されました。

成果は速さだけではありません。研究チームの見積もりでは、人が操作を1つずつ調べて論文を読むと数か月から1年かかります。AIは人が以前に出していた分析結果を再現し、それ以外の手がかりも挙げました。どの発見が新しく価値があるかというAIの見立ても、報告の出どころを伏せて読んだ専門家の判断とおおむね合っていたといいます。

## 手分けのほうが深く調べられた

今回の肝は「1体に全部やらせる」のではなく「数千体に手分けさせた」ことです。OpenAIは、モデルと計算資源をそろえたまま、1体のAIに全データを渡す方式と比べました。

:::quote https://openai.com/index/scaling-ai-research-for-complex-biological-data/ | OpenAI「Using thousands of AI agents to uncover new leads in biological data」
> As the workload grew, the single agent searched less of the literature, citing only 11 references at the largest workload, while the distributed agents cited more than 700 references.
作業量が増えると、1体のAIは論文をあまり調べなくなり、最大の作業量では11本しか引用しませんでした。一方、手分けしたAIは700本を超える論文を引用しました。
:::

どちらの方式の報告かを伏せて専門家に読み比べてもらうと、75%の割合で手分けした側が選ばれました。OpenAIはこの差を、調べる範囲の広さで説明しています。人の研究者は時間が足りず、いちばん強い反応から手をつけがちです。数千体で並行して当たれば、弱い反応や予想外の反応も取りこぼさずに論文と照らし合わせられる、という理屈です。

## 見つかった手がかり

AIは具体的な手がかりも示しました。1つは、細胞の成長を調節する仕組みに関わる2つの遺伝子（Tsc1とTsc2）が、運動をつかさどる小脳では異なる働きをするという違いです。OpenAIは、これが結節性硬化症という病気の理解につながりうるとしています。

もう1つは、パーキンソン病に似た症状が出る病気に関わる遺伝子（DCTN1）の操作が、コレステロールの生成に関わる遺伝子の働きを強めたという観察です。AIはこれを過去の研究と結びつけ、神経細胞の変性との関係という新しい問いを立てました。

{{card:https://github.com/jinlabneurogenomics/distributed_agent|distributed_agent（推論アトラス）|GitHub jinlabneurogenomics}}

## 反応と論点

OpenAIが引用したケンブリッジ大学のサラ・タイヒマン氏は、細胞の地図を作るのは他の研究者が思いもしない発見のためだとし、AIがその探索を広げられると述べています。UCSFのトマシュ・ノワコフスキ氏も、別々の分野に散らばった手がかりをつなぐことで、病気の生物学を新しく考えられるようになると評価しています。

一方で、AIが出したのはあくまで「次に試すべき手がかり」であり、確かめられた結論ではありません。OpenAI自身も、これらは研究者が優先順位を決めるための材料で、提案された仕組みは追加の実験で検証する必要があるとしています。報道したThe Decoderも、作業量の見積もりは研究チーム自身によるものだと注意を添えています。AIに生物学の研究を任せる試みは各社で進んでおり、Claudeがタンパク質の設計を手がけた例もあります（[Claudeがサソリ毒の解毒薬候補を設計した記事](/news/20261022-citrini-claude-scorpion-antivenom-binders/)）。

## 日本のビジネスへの影響

- **使えるか**: 今回使われたGPT-Rosalindは、審査を通った研究機関向けの限定公開のモデルで、一般の利用者はそのまま使えません。公開されたのは解析結果（推論アトラス）とデータで、研究者はこれを今日から参照できます
- **誰にどう効くか**: 直接関係するのは、製薬・バイオ・素材などで研究開発を持つ企業と、その分野を評価する投資・調査の担当者です。大量の実験データや文献の読み解きを、AIに手分けさせて速める発想は、創薬以外の研究にも当てはまります
- **今すぐやれること**: 自社に時間のかかる文献調査や候補の絞り込みがあるなら、「1つの大きなAIに任せる」より「小さく分けて並行で調べさせる」という今回の手分けの考え方を、社内の調査業務で小さく試す価値があります。チャットAIの選び方は[チャットAIのおすすめと料金比較](/best/chat/)にまとめています
- **注意点**: AIが出すのは仮説であって答えではありません。実験や専門家による検証を前提にし、「AIが発見した」と成果を大きく見せないことが、社内外の信頼につながります
