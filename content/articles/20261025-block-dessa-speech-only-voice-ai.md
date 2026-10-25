---
{
  "title": "笑って息をのみ、相づちも打つ会話AI 決済のSquareを持つBlockが「声だけ」で学ばせた「Dessa」",
  "description": "SquareやCash Appを運営する米Blockが、文字を一切使わず人の会話の音声だけで学習させた会話AI「Dessa」を発表した。話しながら聞き、笑いや皮肉も声から読み取る。MacBook Pro 1台で動くが、一般公開はまだで、まず安全性の研究者に試してもらう。",
  "date": "2026-10-25T10:15:00+09:00",
  "category": "products",
  "tags": ["Block", "Dessa", "音声会話", "Jack Dorsey", "安全性"],
  "summary": [
    "決済サービスSquareやCash Appを運営する米Blockが、人の会話の音声だけで学ばせた会話AI「Dessa」を発表した",
    "多くの音声AIは声をいったん文字に直して答えるが、Dessaは声のまま聞いて声で返し、笑いや皮肉、ため息まで読み取るという",
    "MacBook Pro 1台で動くが一般公開はまだで、Blockはまず少数の安全性の研究者に試してもらい危険を洗い出すとしている"
  ],
  "sources": [
    {"title": "Dessa - the Conversation Model trained only on speech", "publisher": "Block", "url": "https://block.xyz/dessa", "kind": "公式発表"},
    {"title": "Jack Dorsey の投稿", "publisher": "X @jack", "url": "https://x.com/jack/status/2113697902916751661", "kind": "X投稿"},
    {"title": "Ragavan Thurairatnam の投稿", "publisher": "X @RagavanThurair", "url": "https://x.com/RagavanThurair/status/2113671324400861645", "kind": "X投稿"},
    {"title": "Block の投稿（当てっこ遊びのデモ）", "publisher": "X @blocks", "url": "https://x.com/blocks/status/2113704552101032190", "kind": "X投稿"},
    {"title": "Block's new voice model sounds eerily human", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/10/24/blocks-new-voice-model-sounds-eerily-human/", "kind": "報道"},
    {"title": "Block's new AI model Dessa was trained entirely on human speech to catch emotions text-based models miss", "publisher": "The Decoder", "url": "https://the-decoder.com/blocks-new-ai-model-dessa-was-trained-entirely-on-human-speech-to-catch-emotions-text-based-models-miss/", "kind": "報道"}
  ],
  "thumb_prompt": "A sleek laptop on a quiet cafe table with no text on screen, only colorful sound waves rising out of it like ribbons that curl into the shape of a laughing face, while an anonymous person leans in, mid-conversation.",
  "thumb_style": "3d",
  "thumb_text": "Dessa",
  "share_text": "Square運営のBlockが、文字を使わず「声だけ」で学ばせた会話AI「Dessa」を発表。笑い、息をのみ、相づちも打つ",
  "editor_note": ""
}
---
決済サービスSquareやCash Appを運営する米Blockは現地時間10月23日、文字のデータを一切使わず、人どうしの会話の音声だけで学習させた会話AI「Dessa」を発表しました。相手の話を聞きながら同時に話し、笑いや皮肉、ため息といった声の調子まで聞き取って返します。ノートPCのMacBook Pro 1台で動くとしていますが、一般向けの公開はまだで、まず少数のAI安全性の研究者に試してもらうとしています。

## 何が発表されたか

Dessaとは、音声を聞いて音声で答える「音声から音声へ」の会話AIです。Blockの公式ページによると、ゼロから人の会話の音声だけで学習させており、文字のデータも、ほかの会社が作った学習済みのAIも使っていません。Blockは、知る限り「音声だけで学んだのに、人と自然に会話できる世界初のAI」だとしています。

いまの多くの音声AIは、話した声をいったん文字に起こし、文章を作るAIに答えさせ、それを読み上げる仕組みです。Blockはこの「文字を経由する」ことが問題だと指摘します。

:::quote https://block.xyz/dessa | Block「Dessa - the Conversation Model trained only on speech」
> It turns your voice into text and throws away an incredible amount of information text alone can’t carry. The most powerful AIs in the world can’t hear how you feel.
声を文字に変えるとき、文字だけでは運べない膨大な情報を捨てている。世界で最も強力なAIでさえ、あなたがどう感じているかを聞き取れない。
:::

公式ページが挙げるDessaの特徴は次のとおりです。

- **聞きながら話す**: 相手が話し終わるのを待たず、人のように途中で口を挟んだり「うん」「なるほど」と相づちを打ったりする。会話のこうした仕組みは「全二重（フルデュプレックス）」と呼ばれる
- **感情を声で扱う**: 面白いことがあれば話の途中でも笑い、「もっと大きな声で」と頼まれれば声を大きくする。どちらも教えていないのに身についたという
- **手元のPCで動く**: MacBook Pro（M4 Max以上）で、話すより速く答えを作れる
- **少ない言葉で学んだ**: 文章で学ぶAIより「数百分の1」の量の言葉で言語を覚えたとしている

学習に使った計算機は、NVIDIAのAI向けサーバー1ラック（GB200 NVL72）だけです。公式ページには、映画の題名が思い出せない人の代わりに言い当てる、サプライズを聞かされて小声で「oh my god」と息をのむ、といった会話の録音が多数並んでいます。Blockは、どの録音も誰も台本を与えていない実際の会話で、字幕は後から付けたと説明しています。

{{card:https://block.xyz/dessa|Dessa - the Conversation Model trained only on speech|Block}}

## 誰が作ったのか

開発したのは、Block社内の「（とても）小さな」AI研究チームです。カナダ・トロントのAIスタートアップDessaの元メンバーが立ち上げたチームで、2012年からAIを、8年以上前から音声を作るAIを手がけてきたとしています。モデルの名前もこの会社から取っています。チームは共同創業者で会長のジャック・ドーシー氏の直属です。

ドーシー氏はXで、声が知能とやりとりする一番自然な方法だと考えてDessaを作ったと投稿し、話していると人と話しているように感じるとしています。

{{x:https://x.com/jack/status/2113697902916751661}}

開発チームを率いるラガヴァン・トゥライラトナム氏は、Dessaを「音声にとってのGPT-3の瞬間」と表現しました。GPT-3は、文章を作るAIが一気に実用に近づいた2020年のOpenAIのモデルです。

{{x:https://x.com/RagavanThurair/status/2113671324400861645}}

Blockは開発の理由に、好奇心、人とAIのより良い理解、安全性の3つを挙げています。安全性については、AIが力を増しているのに声に表れる感情にはほぼ「耳が聞こえない」状態で、ひどい痛みを抱えた人の声にも気づかず話し続けてしまう、と例を挙げています。

## 反応と論点

TechCrunchは、デモを聞いた印象として「不気味なほど人間らしい」と伝えています。会話の中で疲れたと言うときは本当に疲れた声になり、開発メンバーが投稿したデモでは、感極まって泣き出しそうな声で話す場面もあったと紹介しています。Blockの公式アカウントは、社員とDessaが当てっこ遊びをする動画も投稿しました。

一方で、まだ外部の人が自分で確かめられる状態ではありません。公開されているのは会社が選んだ録音だけで、性能を他社のAIと比べた数字も、モデルの大きさも示されていません。TechCrunchは、声の感情を指示で操れるのかどうかもはっきりしないと指摘しています。

Block自身も危険を意識しています。公開を急がず、大学・企業・研究機関のメールアドレスを持つ安全性の研究者に限って先行利用を受け付けています。TechCrunchは、Blockが特に、音声AIが人をだますような場面を調べてほしいとしていると伝えています。人間そっくりの声で感情まで込めて話せるAIは、電話詐欺やなりすましにも使われうるためです。

## 日本のビジネスへの影響

**使えるか**: 現時点で一般向けの提供はなく、日本語に対応するかどうかも発表されていません。公式ページの会話の録音は英語が中心です。企業が自社のサービスに組み込める形での提供予定も示されていないため、今は様子見でよい段階です。

**誰にどう効くか**: コールセンターや予約受付、店舗の注文受付に音声AIを入れようとしている事業責任者です。TechCrunchによると、Squareはすでに注文受付に音声AIを使っています。文字を経由しない音声AIが実用になれば、「客が怒っている」「迷っている」を声から察して対応を変える、といった使い方が現実味を帯びます。手元のPCで動く点は、通話の音声を外部に送りたくない企業にとっても意味があります。

**今すぐやれること**: 自社で検討中の音声AIが、声を文字に変えてから答える方式か、音声のまま扱う方式かを確認しておくことです。相づちや割り込みへの反応、声の調子の読み取りは、方式によって差が出やすい部分です。いま選べる読み上げ・音声AIは[音声合成・AI読み上げのガイド](/best/text-to-speech/)で比べられます。

**注意点**: 人と区別がつかない声のAIを顧客対応に使う場合、相手がAIだと分かるように伝える配慮が欠かせません。米国では、AIで作った広告に表示を義務づける州法も成立しています（[ペンシルベニア州の新しい法律](/news/20261025-pennsylvania-ai-ad-disclosure-law/)）。
