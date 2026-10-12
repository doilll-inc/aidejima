---
{
  "title": "有名数学者が残した未解決問題9問をGoogleのAIが証明、科学誌Scienceが論文を掲載",
  "description": "Google DeepMindの数学AI「AlphaProof Nexus」の論文が10月8日、科学誌Scienceに載った。数学者エルデシュが残した未解決問題353問のうち9問を、1問数百ドルの計算費用で証明した。",
  "date": "2026-10-12T19:55:00+09:00",
  "category": "research",
  "tags": ["Google DeepMind", "AlphaProof Nexus", "数学", "論文", "Gemini"],
  "summary": [
    "Google DeepMindの数学AI「AlphaProof Nexus」の論文が、10月8日に米科学誌Scienceに掲載された",
    "数学者エルデシュが残した未解決問題353問のうち9問を証明し、計算費用は1問あたり数百ドルだった",
    "証明は計算機で正しさを自動確認できる形で公開。査読前に722本を一挙公開したOpenAIとは進め方が分かれた"
  ],
  "sources": [
    {"title": "Advancing Mathematics Research with AI-Driven Formal Proof Search (arXiv:2605.22763)", "publisher": "Google DeepMind ほか（arXiv）", "url": "https://arxiv.org/abs/2605.22763", "kind": "論文"},
    {"title": "Advancing mathematics research with AI-driven formal proof search", "publisher": "Science", "url": "https://www.science.org/doi/10.1126/science.aej2213", "kind": "論文"},
    {"title": "alphaproof-nexus-results（証明の公開リポジトリ）", "publisher": "Google DeepMind（GitHub）", "url": "https://github.com/google-deepmind/alphaproof-nexus-results", "kind": "公式ドキュメント"},
    {"title": "Pushmeet Kohli の投稿", "publisher": "X @pushmeet", "url": "https://x.com/pushmeet/status/2108265646890815730", "kind": "X投稿"},
    {"title": "Google Deepmind's AlphaProof Nexus solved dozens of open math problems and actually got peer reviewed", "publisher": "The Decoder", "url": "https://the-decoder.com/google-deepminds-alphaproof-nexus-solved-dozens-of-open-math-problems-and-actually-got-peer-reviewed/", "kind": "報道"},
    {"title": "Google Deepmind's AlphaProof Nexus solves decades-old math problems for a few hundred dollars", "publisher": "The Decoder", "url": "https://the-decoder.com/google-deepminds-alphaproof-nexus-solves-decades-old-math-problems-for-a-few-hundred-dollars/", "kind": "報道"},
    {"title": "Some mathematicians call for OpenAI boycott after AI-generated proofs flood their field", "publisher": "The Decoder", "url": "https://the-decoder.com/some-mathematicians-call-for-openai-boycott-after-ai-generated-proofs-flood-their-field/", "kind": "報道"},
    {"title": "DeepMind preprint: LLM+Lean agent resolves 9 Erdos problems and 44 OEIS conjectures", "publisher": "Runtime Wire", "url": "https://runtimewire.com/article/deepmind-llm-lean-erdos-proofs", "kind": "報道"}
  ],
  "thumb_text": "AlphaProof Nexus",
  "thumb_style": "illustration",
  "thumb_prompt": "An old wooden study desk covered with a yellowed notebook of unsolved math problems, where nine of the pages glow softly as if just completed, while a small robot arm holding a pencil rests beside a cold cup of tea.",
  "share_text": "Googleの数学AIが未解決問題9問を証明し、論文がScienceに掲載。1問あたりの計算費用は数百ドル",
  "editor_note": ""
}
---
Google DeepMindの研究チームは現地時間10月8日、数学の証明を自動で探すAI「AlphaProof Nexus」の論文を米科学誌Scienceで発表しました。20世紀の数学者ポール・エルデシュが残した未解決問題353問に挑み、9問の証明に成功しています。計算にかかった費用は1問あたり数百ドルでした。

## 何が発表されたか

AlphaProof Nexusとは、AIが書いた証明を、証明の正しさを機械的に確かめる専用の言語「Lean」でチェックしながら、答えにたどり着くまで書き直しを繰り返す仕組みです。人間の査読者が何週間もかけて読む代わりに、計算機が1行ずつ「論理に穴がないか」を確認します。論文の要旨は、成果を次のようにまとめています。

:::quote https://arxiv.org/abs/2605.22763 | Google DeepMindほかの論文（arXiv:2605.22763）要旨
> Our most capable agent autonomously resolved 9 of 353 open Erdős problems at the per-problem cost of a few hundred dollars, proved 44/492 OEIS conjectures, and is being deployed in combinatorics, optimization, graph theory, algebraic geometry, and quantum optics research.
最も高性能なエージェントは、未解決のエルデシュ問題353問のうち9問を1問あたり数百ドルの費用で自律的に解き、OEISの予想492件のうち44件を証明した。組合せ論、最適化、グラフ理論、代数幾何、量子光学の研究で実際に使われ始めている。
:::

OEISとは、数の並び方を集めた世界的なデータベースで、そこに「たぶんこうなるはず」と書き込まれたまま証明されていない予想が多数あります。The Decoderは、解けたエルデシュ問題のうち2問は56年間誰も解けなかったものだと報じています。ほかに代数幾何で15年来の問いに決着をつけ、最適化の分野で既存の限界値を更新したとも伝えています。

証明の文章を書くのはGoogleの対話AI「Gemini 3.1 Pro」で、より難しい部分では2024年の国際数学オリンピックで銀メダル相当の成績を出した専用AI「AlphaProof」を呼び出す構成だと、The Decoderは報じています。証明はすべてGitHubで公開され、誰でも手元で検証を走らせられます。

{{card:https://github.com/google-deepmind/alphaproof-nexus-results|alphaproof-nexus-results|Google DeepMind（GitHub）}}

## 「凝った仕組み」でなくても解けた

論文で興味深いのは、仕組みの複雑さと成果の関係です。研究チームは構成の違う複数のAIを比べました。要旨によると、対話AIに証明を書かせてLeanで確かめる、を交互に繰り返すだけの基本的な型でも同じ9問を解けました。違いが出たのは費用で、最も難しい問題では基本型のほうが高くついたとしています。

つまり「書く→機械が採点→直す」の往復を回すこと自体が成果の大部分を生んでおり、凝った工夫は主に費用を下げる役割だったことになります。一方でThe Decoderは、論文が「まったく新しい理論を必要とする問題には届いていない」と認めている点も紹介しています。成功は、Leanの数学ライブラリが整っている組合せ論や数論などに偏っていました。353問中9問という成功率も、全体から見れば約2.5%です。

## 背景：OpenAIの「一挙公開」との対比

DeepMindのPushmeet Kohli氏は10月8日のXへの投稿で、Scienceへの掲載を報告し、AlphaProof Nexusは2024年の数学オリンピックで成果を出したAlphaProofの後継にあたると説明しました。外部の数学者がすでに研究レベルの結果の証明に使っていることも紹介しています。

{{x:https://x.com/pushmeet/status/2108265646890815730}}

この発表が注目されるのは、ライバルのOpenAIが10月6日、未公開の社内AIが書いた数学の原稿722本を、学術誌の査読を通さずにGitHubで一度に公開したばかりだからです（[OpenAIが未公開AIの数学論文722本を一挙公開](/news/20261007-openai-math-722-manuscripts/)）。The Decoderによると、数学者の団体Association for Human Mathematicsはこれを「研究の規範に反する」としてOpenAIとの協力をやめるよう呼びかけました。

AlphaProof Nexusの研究は、5月にまず論文の下書きを公開して成果を示し、その後に査読を経てScienceに載る、という学術の手順を踏んでいます。The Decoderは見出しで「実際に査読を通った」と強調しました。AIで証明を量産できるようになった今、数学界にとっての焦点は「AIが解けるか」から「誰がどう確かめ、どう発表するか」に移りつつあります。

## 日本のビジネスへの影響

- **使えるか**: AlphaProof Nexus自体は研究用の仕組みで、一般向けの製品やサービスとしての提供は発表されていません。証明の成果物はGitHubで誰でも見られます
- **誰に関係するか**: 数学そのものより、「AIの答えをどう信用するか」に悩む企業の担当者に示唆があります。AIに書かせ、別の仕組みで機械的に検査し、通らなければ書き直させるという今回の構図は、契約書の条項チェックや社内規程との突き合わせ、経理データの検算など、正解の基準を決められる業務にそのまま当てはまります
- **今すぐやれること**: AIに任せている業務のうち「正しいかどうかを機械的に判定できるもの」を洗い出し、AIの出力をそのまま使わず、ルールやチェックリストで自動検査してから人に回す流れを試してみるとよいでしょう。調べものに使うAIの選び方は[用途別ガイド「調べもの・リサーチ」](/best/research/)にまとめています
- **注意点**: 今回の成果は、正しさを機械で厳密に確かめられる数学という特殊な分野でのものです。353問中9問という成功率が示すとおり、AIが新しい発想を必要とする問題を次々解く段階にはまだありません。「AIが難問を解いた」という見出しだけで、自社の複雑な判断業務まで任せられると考えるのは早計です
