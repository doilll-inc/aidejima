---
{
  "title": "AIが書いた文章に見えない「透かし」、OpenAIがEUのChatGPTで数週間内に導入",
  "description": "OpenAIがEUのAI法に対応し、ChatGPTとCodexがEU内で出力する文章に見えない電子透かしを数週間以内に入れると発表した。単語の25%を言い換えると検出率は17%に落ちるなど、限界も自ら公表している。",
  "date": "2026-10-06T02:20:00+09:00",
  "category": "policy",
  "tags": ["OpenAI", "ChatGPT", "textGrain", "電子透かし", "EU AI Act", "規制"],
  "summary": [
    "OpenAIはEUのAI法に合わせ、EU内のChatGPTとCodexの文章に目に見えない電子透かしを数週間以内に入れる",
    "透かしは単語の選び方に統計的な癖を混ぜる方式で、判定ツールはまず承認された研究者などにだけ提供する",
    "OpenAI自身が、短い文や言い換えた文では見つけにくく、透かしがなくても人が書いた証拠にはならないと説明している"
  ],
  "sources": [
    {"title": "Our approach to EU text provenance rules", "publisher": "OpenAI", "url": "https://openai.com/index/eu-text-provenance/", "kind": "公式発表"},
    {"title": "How Claude marks AI-generated content", "publisher": "Anthropic（Claudeヘルプセンター）", "url": "https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content", "kind": "公式ドキュメント"},
    {"title": "Code of Practice on Transparency of AI-generated Content", "publisher": "European Commission", "url": "https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content", "kind": "公式ドキュメント"},
    {"title": "OpenAI Begins Phased Text Watermarking Under EU AI Act Rules", "publisher": "Unite.AI", "url": "https://www.unite.ai/openai-begins-phased-text-watermarking-under-eu-ai-act-rules/", "kind": "報道"},
    {"title": "ChatGPT Is Getting Invisible Watermarks for Text", "publisher": "Trending Topics", "url": "https://www.trendingtopics.eu/chatgpt-text-watermark-eu/", "kind": "報道"}
  ],
  "thumb_prompt": "A typed business letter on a desk under an ultraviolet lamp, revealing a faint hidden pattern of glowing dots woven between the words, with a magnifying glass resting beside it.",
  "thumb_style": "photo",
  "thumb_text": "文章の電子透かし",
  "share_text": "ChatGPTの文章に見えない透かし。OpenAIがEUで導入へ、言い換えると見つけにくい限界も公表",
  "editor_note": ""
}
---
OpenAIは現地時間10月5日、EU（欧州連合）のAI法に対応するため、EU内のChatGPTとCodexが出力する文章に、目に見えない電子透かしを今後数週間で入れると発表しました。API（自社のサービスにOpenAIのAIを組み込むための接続口）の利用者は、世界中で同日から希望すれば透かしを付けられます。一方でOpenAIは、単語の25%を言い換えると検出率が17%まで落ちるといった限界も、自ら数字で示しました。

## 何が発表されたか

電子透かしとは、AIが作った文章だと後から機械で判定できるよう、文章に埋め込む目に見えない目印のことです。OpenAIの技術は「textGrain」と呼ばれ、文字や記号を足すのではなく、AIが単語を選ぶときの選び方に統計的な癖を混ぜます。読んでも違いはわからず、専用の判定ツールで調べたときだけ癖が見えます。

導入は段階的です。

| 対象 | 内容 | 時期 |
|---|---|---|
| ChatGPT・Codex | EU内の対象利用者の文章に透かしを入れる（全プラン） | 今後数週間 |
| API | 世界中の利用者が一部のモデルで選んでオンにできる。初期設定はオフ | 10月5日から |
| 判定ツール | 承認された研究者・専門機関だけに個別に提供。一般公開はしない | 10月5日から申請受付 |

EU以外のChatGPTには、現時点で透かしは入りません。OpenAIは、地域を絞ることで実際の使われ方から学ぶ余地を残すと説明しています。品質への影響については、最新モデルGPT-6 Astraで8種類の性能試験を比べ、透かしの有無で意味のある差は見られなかったとしています。

## OpenAI自身が示した「見つけにくい」場面

今回の発表で目を引くのは、OpenAIが透かしの弱点を具体的な数字で開示したことです。誤って「透かしあり」と判定する率を1%に抑えた条件で、次の結果でした。

- **短い文ほど見つけにくい**: 心理学のような話題では、200トークン（トークンはAIが文章を数える単位）の文で検出は約80%、400トークンでは約95%。数学のように言い回しの自由が少ない文章では、検出率が大きく下がる
- **言い換えに弱い**: 400トークンの文で単語の10%を同じ意味の別の語に置き換えると、検出率は約92%から66%に、25%置き換えると17%に下がる

そのうえでOpenAIは、透かしから言えないことも明記しました。

:::quote https://openai.com/index/eu-text-provenance/ | OpenAI公式ブログ「Our approach to EU text provenance rules」
> A watermark does not measure human contribution. It can indicate that an OpenAI system generated or processed part of a passage, but not how much human judgment, editing, or creativity went into it.
透かしは人の貢献度を測るものではありません。文章の一部をOpenAIのシステムが生成・加工したことは示せますが、人の判断や編集、創造性がどれだけ加わったかはわかりません。
:::

ほかにも、透かしは利用者個人を特定せず、文章の正確さも保証しないとしています。逆に透かしが見つからなくても、文が短い、編集・翻訳された、他社のAIで書かれたなどの理由がありうるため、人が書いた証拠にはならないとも説明しています。

## 背景：EUの「AIが作ったとわかるように」義務

EUのAI法は、文章を生成するAIの提供者に、出力をAIが作ったものだと機械で判別できる形にするよう求めています。欧州委員会のページによると、この透明性の義務は2026年8月2日から適用されています。欧州委員会は具体的な守り方をまとめた行動規範（Code of Practice）を公開し、規範に従うことが義務を守っている証明の手段になると認めています。OpenAIは判定ツールの提供もこの規範に沿って進めるとしています。

{{card:https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content|Code of Practice on Transparency of AI-generated Content|European Commission}}

競合ではAnthropicが先行しています。Claudeのヘルプページによると、Claudeは自社のアプリやAPIだけでなく、AWS・Google Cloud・Microsoftのクラウド経由の出力にも透かしを入れており、地域をEUに限っていません。Claudeの判定APIも、規制当局・報道機関・研究者などに限った非公開の試験提供です。

## 反応と論点

透かしに積極的な見方は、AIで作った偽情報や大量の自動投稿を、研究者や報道機関が追跡しやすくなるというものです。OpenAIは画像と音声について、すでに企業や団体が使える判定ツールを公開しており、文章にも同じ仕組みを広げる位置づけです。

反対や懸念も根強くあります。Trending Topicsは、Anthropicが透かしを始めた際、自分の文章の推敲にClaudeを使うだけの人や開発者を中心に有料会員の解約が相次いだと報じています。同誌は、母語でない言語の文章をAIで整える人が不利になりうると、OpenAI自身も以前に警告していたと伝えています。OpenAIは今回、透かしの見逃しと誤判定のリスクを理由に、判定ツールを一般公開しないと説明しています。

## 日本のビジネスへの影響

- **使えるか**: 日本で使うChatGPTの文章に、現時点で透かしは入りません。ただし日本の企業がAPIで自社サービスにOpenAIのモデルを組み込んでいる場合は、設定でオンにできます。EU向けにAIで作った文章を出すサービスは、自社がEU AI法の義務の対象になるかを確認する必要があります。
- **誰にどう効くか**: 欧州に拠点や顧客を持つ企業の法務・広報担当と、AIで記事や商品説明を量産するマーケターに関係します。EUの社員がChatGPTで書いた文書には、今後透かしが入ることになります。
- **今すぐやれること**: 欧州向けにAIで文章を作っている場合は、どのAIのどの出力に透かしが入るか（OpenAIはEU内のChatGPT、ClaudeはEUに限らず全出力）を一覧にし、社内規程や顧客への開示方針と突き合わせておくとよいでしょう。
- **注意点**: 透かしは「AIが関わった可能性」を示すだけで、言い換えや翻訳で簡単に弱まります。採用や評価、取引先とのやり取りで「透かしがあるからAIが書いた」「ないから人が書いた」と判断する使い方は、OpenAI自身が否定しています。

ChatGPT・Claude・Geminiの料金やプランの違いは、[チャットAIのガイド](/best/chat/)で比べられます。
