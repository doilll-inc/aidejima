---
{
  "title": "AIの文章が読みにくい理由、ClaudeやGPTは数学やプログラムの訓練で「詰め込む」癖 米大学が14のAIを調査",
  "description": "米ニューヨーク大学とテキサス大学の研究者が、ClaudeやGPTなど14のAIの文章を人の文章と比べ、読みにくさにつながる6つの書き方を多用していると論文で示した。正解だけを評価する訓練で、短く詰め込む癖がつくと見ている。",
  "date": "2026-10-27T05:00:00+09:00",
  "category": "research",
  "tags": ["Claude", "Claude Opus 5.5", "GPT-5.6", "論文", "文章作成"],
  "summary": [
    "米ニューヨーク大学とテキサス大学の研究者が、ClaudeやGPTなど14のAIが書いた会話・作業記録・作文を人の文章と比べた",
    "最先端のAI9つはどれも、聞き慣れない言葉の組み合わせや、物を主語にして生き物のような動詞を使う書き方を人より多く使っていた",
    "研究者は、数学やプログラムで正解だけを評価する訓練が原因と推測し、短い答えを褒める訓練でAIの文が人から離れることを確かめた"
  ],
  "sources": [
    {"title": "Why is AI-generated language so hard to understand?", "publisher": "arXiv（Clark, Martin, Mahowald）", "url": "https://arxiv.org/abs/2610.29162v1", "kind": "論文"},
    {"title": "Why is AI-generated language so hard to understand?（HTML版本文）", "publisher": "arXiv", "url": "https://arxiv.org/html/2610.29162v1", "kind": "論文"},
    {"title": "Researchers find six patterns that make AI text so exhausting to read", "publisher": "The Decoder", "url": "https://the-decoder.com/researchers-find-six-patterns-that-make-ai-text-so-exhausting-to-read/", "kind": "報道"}
  ],
  "thumb_prompt": "A tired reader at a desk holding a magnifying glass over a single sentence that has grown into a tangled knot of rope spilling off the page, while a small robot proudly hands over another knotted page.",
  "thumb_style": "illustration",
  "thumb_text": "AIの文章はなぜ読みにくい",
  "share_text": "ClaudeやGPTの文章が読みにくいのはなぜか。米大学が14のAIを調べ、6つの「読みにくい書き方」を多用していると論文に",
  "editor_note": ""
}
---
米ニューヨーク大学とテキサス大学オースティン校の研究者3人は、ClaudeやGPTなど14のAIが書いた文章を人の文章と比べ、最先端のAIほど読む人に負担をかける書き方を多用しているとする論文を、現地時間10月21日に論文公開サイトarXivで発表しました。原因は、数学やプログラミングで「正解したか」だけを評価する訓練にあると推測し、その仮説を小さな実験で裏づけています。

## 何がわかったか

論文は、心理言語学（人が文を読んで理解する仕組みを調べる学問）で「読むのに手間がかかる」とわかっている書き方が、AIの文章にどれだけ出てくるかを数えたものです。英語の文章を対象に、AIと人の雑談、プログラムの修正作業、作文の3つの場面で比べました。

人の側の比較対象には、映画の字幕、プログラマー向けの質問サイトStackExchange、米国の学生の作文を使っています。論文の冒頭は、AIが書きそうな文の見本から始まります。

:::quote https://arxiv.org/html/2610.29162v1 | 論文「Why is AI-generated language so hard to understand?」本文
> Your instinct is right; the convoluted sentence you are currently reading is quietly eating its own reader-patience budget — footnote it.
あなたの直感は正しい。今読んでいるこの入り組んだ文は、読み手の忍耐予算を静かに食いつぶしている——脚注にしておこう。
:::

この1文に、AIが多用する書き方が詰まっていると研究者は説明しています。調べた6つの書き方を、日本語に置き換えて整理すると次のとおりです。

| 書き方 | 英語の例 | 日本語でいえば |
|---|---|---|
| 見慣れない言葉の組み合わせ | reader-patience budget | 「読者忍耐予算」のような造語 |
| 主語と述語が遠く離れる | 長い説明をはさむ文 | 主語のあとに長い修飾が続き、述語がなかなか来ない |
| 省ける言葉を省く | the book the professor wrote | 関係を示す言葉を抜いて詰める |
| 名詞を何個も重ねる | horror movie soundtrack generator | 「ホラー映画音楽生成器」 |
| 名詞をそのまま動詞にする | footnote it | 「脚注する」 |
| 物を主語に生き物の動詞 | the sentence is eating | 「文が食いつぶす」 |

## どのAIで調べたか

対象は14のAIです。Anthropicの「Claude Sonnet 5」「Claude Opus 5」「Claude Opus 5.5」「Claude Fable 5」、OpenAIの「GPT-5.6」の3種類（Luna・Terra・Sol）、中国のKimi K2.5とGLM 5の9つを最先端のAIとして扱い、これと比べるために、中身が公開されている小型のAI（OlmoとLlama）も加えました。研究に使ったAIの利用料は、試行を含めて合計251.19ドルでした。

結果は、最先端の9つすべてが、人の文章より「見慣れない言葉の組み合わせ」と「物を主語に生き物の動詞」を多く使っていました。会話の場面では、ほとんどのAIが、主語と述語を遠ざける書き方、名詞の重ね、省ける言葉の省略も人より多くなっていました。作文では差は小さめで、研究者はやりとりが何往復も続くほど詰め込みが強まるのではないかと見ています。

一方、AI同士の違いも大きく出ました。小型のLlamaと、追加の訓練をしていない段階のOlmoは人の文章に近い数字でした。同じOlmoでも、会話向けに訓練した版、さらに考える力を鍛えた版と進むほど、最先端のAIと同じくらい読みにくい書き方が増えています。

## なぜ読みにくくなるのか

研究者が立てた仮説は、訓練の目的のずれです。人の言葉は「相手に伝わること」に合わせて磨かれてきました。ところが最近のAIは、数学やプログラムの問題で正解したかどうかで評価する訓練を大量に受けています。そこでは伝わりやすさより、少ない文字数に多くの情報を詰めることが有利になります。

これを確かめるため、研究者は小型のAIに、答えが短いほど高く評価する訓練をかけました。するとAIは、同じ意味を短く言える書き方を選ぶようになり、訓練で扱っていない種類の文でも短い言い方を好むようになりました。人は場面に応じて長い言い方と短い言い方を使い分けますが、訓練後のAIは場面にかかわらず短いほうに寄ったといいます。

## 反応と論点

改善の兆しも示されています。Claude Opus 5.5は、前の世代のOpus 5と比べ、読みにくさにつながる21の比較のうち19で数字が低くなっていました。

:::quote https://arxiv.org/html/2610.29162v1 | 論文「Why is AI-generated language so hard to understand?」本文
> It is of course also possible to reward models for effective communication; indeed, our results indicate that more recent model variants like Opus 5.5 yield a quantifiable improvement over older models like Opus 5.
もちろん、伝わりやすさに対してAIを評価する訓練も可能である。実際、Opus 5.5のような新しい版は、Opus 5のような古い版より数字で見て改善していることが今回の結果からわかる。
:::

独The Decoderもこの論文を取り上げ、6つの書き方を紹介しています。ただし研究には限界もあります。調べたのは英語の文章だけで、会話の題材やプログラムの課題の数も限られます。訓練が原因だという点も、各社の訓練の中身を直接調べたわけではなく、小さな実験による推測です。

AIの答えを人と比べた研究では、[12のAIに人間への本音を聞いたら多くが同じ答えだった調査](/news/20261023-ai-models-same-controversial-take-humans/)もあります。

## 日本のビジネスへの影響

- **使えるか**: 論文は無料で読めます。調べたのは英語の文章だけで、日本語のAIの文章に同じ傾向があるかは確かめられていません
- **誰に効くか**: AIで社外向けの文章やメール、広告文の下書きを作っているマーケターや広報担当者、AIの出力をそのまま報告書に使っている企画職です。読み手が「なんとなく読みにくい」と感じる原因が、AIの書き方の癖にある可能性があります
- **今すぐやれること**: AIに文章を頼むとき、「造語を使わない」「名詞を3つ以上つなげない」「物を主語にして擬人化しない」「主語と述語を近づける」と指示に書き足すことです。6つの癖は、そのまま推敲の点検項目にもなります。文章づくりのAIを選び直すなら[文章作成AIのガイド](/best/writing/)も参考になります
- **注意点**: 読みやすさの差はAIの種類や版で大きく変わり、新しい版で改善している例もあります。「AIの文章は読みにくい」と一律に決めつけず、使っているAIの出力を自分たちの読み手で確かめる必要があります
