---
{
  "title": "ソフトが「どんな入力でも落ちない」ことをClaudeが証明、公開ソフト123本で数百のバグも発見",
  "description": "Anthropicは10月22日、Claudeが公開ソフト123本の239か所について「どんな入力でも異常終了しない」ことを数学的に証明したと発表した。証明の途中で数百のバグも見つけて直した。人なら何十人年もかかる作業を数週間で済ませた。",
  "date": "2026-10-23T22:20:00+09:00",
  "category": "research",
  "tags": ["Anthropic", "Claude", "Theorem", "セキュリティ", "形式検証", "Claude Opus 5.5"],
  "summary": [
    "Anthropicは10月22日、Claudeが誰でも使える公開ソフト123本の239か所で「64MBまでのどんな入力でも異常終了しない」ことを数学で証明したと発表した",
    "証明の途中でClaudeは数百のバグを見つけて直し、何兆回もの自動テストをすり抜けて何年も残っていた欠陥や、10年以上潜んでいた不具合も含まれていた",
    "Anthropicは「証明済み＝バグゼロではない」とも明記しており、前提とした動作環境は一般的なパソコンやサーバーと異なる"
  ],
  "sources": [
    {"title": "LLMs are making formal software verification feasible at a much larger scale", "publisher": "Anthropic", "url": "https://www.anthropic.com/research/formal-verification", "kind": "公式発表"},
    {"title": "LLMs are making formal software verification feasible at a much larger scale（議論）", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=50202217", "kind": "コミュニティ"},
    {"title": "Claude digs up bugs that survived trillions of tests across open-source software", "publisher": "Interesting Engineering", "url": "https://interestingengineering.com/ai-robotics/claude-formal-verification-software-security", "kind": "報道"},
    {"title": "Anthropic Says Claude Proved Security Properties Across 123 Libraries", "publisher": "Unite.AI", "url": "https://www.unite.ai/anthropic-says-claude-proved-security-properties-across-123-libraries/", "kind": "報道"},
    {"title": "Anthropic's Claude now writes code and proves it safe automatically", "publisher": "The Decoder", "url": "https://the-decoder.com/anthropics-claude-now-writes-code-and-proves-it-safe-automatically/", "kind": "報道"}
  ],
  "thumb_prompt": "A towering stack of printed paper proofs filling a quiet server room aisle, with a single small glowing laptop at its base stamping a green checkmark seal onto a tiny cardboard box of software, a few dead beetle-like bugs lying beside it on the floor.",
  "thumb_style": "diorama",
  "thumb_text": "Claudeが証明",
  "share_text": "公開ソフト123本が「どんな入力でも落ちない」ことをClaudeが数学で証明。何兆回のテストをすり抜けたバグも数百件見つけた",
  "editor_note": ""
}
---
Claudeを開発する米Anthropicは現地時間10月22日、Claudeが誰でも使える公開ソフト（オープンソース）123本の239か所について、「64MBまでのどんなデータを入れても異常終了しない」ことを数学的に証明したと発表しました。人の専門家なら何年もかかるとされてきた作業を、数週間で済ませています。証明を書く途中で、Claudeは数百のバグも見つけて直しました。

## 何が発表されたか

今回の技術は「形式検証」と呼ばれます。形式検証とは、プログラムが決められた条件を必ず満たすことを、テストで試すのではなく数学の証明で示す方法です。テストは試した入力しか確かめられませんが、証明が通れば、条件の範囲内のすべての入力で成り立つと言えます。

これまでは手間が大きすぎて、ごく一部でしか使われてきませんでした。Anthropicの発表は、ある基本ソフト（OS）の中核部分は作るのに2人年、形式検証には20人年かかったという例を挙げ、実用は航空機の制御ソフトのような分野に限られてきたと説明しています。

:::quote https://www.anthropic.com/research/formal-verification | Anthropic「LLMs are making formal software verification feasible at a much larger scale」
> Frontier models can now produce correctness proofs for real-world software fully autonomously.
最先端のAIモデルは今や、実際に使われているソフトの正しさの証明を、完全に自力で作れる。
:::

研究は、ソフトの検証を手がける企業Theoremとの共同です。対象は、Googleが運営する公開ソフト向けの自動テストの仕組み「OSS-Fuzz」に登録されたソフトで、XMLの読み込み、印刷、リモートデスクトップなどに使われる部品が含まれます。各ソフトに開発者が用意していたテストを「どんな入力でも落ちない」という条件に書き直し、Claudeがそれを満たすことを証明しました。

証明は、人が読むソースコードではなく、実際に動く機械語のレベルで書かれています。分量は合計で約1億8,000万行、1本あたり約60万行です。証明が本当に正しいかは、Claudeとは別の専用ソフト（Rocqという証明チェッカー）が機械的に確かめます。

## 途中で見つかったバグ

証明を書こうとすると、条件を満たさない箇所、つまりバグに突き当たります。Anthropicによると、この過程で数百のバグが見つかりました。何兆回もの自動テストをすり抜けて何年も残っていたものもあったといいます。

Claudeはバグを見つけるたびに人に止めてもらうのではなく、自分で修正してから証明を続けました。ただし「入力を全部はじけば絶対に落ちない」といった、ずるい直し方で証明を通すおそれがあります。そこでAnthropicは、修正には減点を与え、修正が影響する入力がどれだけ少ないかを証明すれば加点する形にし、修正内容も記録して点検しました。

別の実験では、広く使われているPDF閲覧ソフトの検証で、通常なら1年間に報告される量と同じだけのセキュリティ上のバグを1週間で見つけたとしています。10年以上潜んでいた、これまで知られていなかった不具合も見つかりました。

## 何が言えて、何が言えないか

Anthropicは発表の中で、限界もはっきり書いています。

:::quote https://www.anthropic.com/research/formal-verification | Anthropic「LLMs are making formal software verification feasible at a much larger scale」
> “Formally verified” does not mean “bug-free.”
「形式検証済み」は「バグがない」という意味ではない。
:::

証明が保証するのは、決めた条件の範囲だけです。今回の証明は、1つの処理だけが動く単純な構成で、RISC-Vという種類のCPUとLinuxを前提にしています。多くのパソコンやサーバーは別の種類のCPU（x86やARM）で、部品のつなぎ方も違うため、そのまま当てはまるわけではありません。前提にしたCPUやOSの「数学のモデル」自体に誤りがあれば、証明も意味を失います。

一方で、コストは下がり続けているとAnthropicはみています。36の小さな検証課題で比べると、Claude Opus 5.5は半数の課題を、前の世代のOpus 5より約4割少ない計算量で証明できました。Anthropicは、まだ修正されていないバグがわかってしまうものを除いて証明の一部を公開し、Theoremは同じ仕組みを他の公開ソフトにも適用すると申し出ています。開発者が自分のコードで試すための、Claude向けの追加機能（スキル）も公開しました。

## 反応と論点

米国の技術者が集まる掲示板Hacker Newsでは380ポイントを超え、200件以上のコメントが付きました。自分でもAIを使ってデータベースの書き直しが元と同じ動きをするかを一部証明できた、という実例の報告がありました。

懐疑的な意見も目立ちます。「数学的に完璧でも、解くべき問題を取り違えていれば意味がない」と、条件の決め方そのものを問う声や、複数の処理が同時に動く場面という一番難しい部分を避けている、という指摘です。AIが書いた条件をAIが証明する仕組みでは、条件がずれていても気づきにくいという懸念も出ました。プログラマーの仕事への影響を心配する書き込みもありました。

AnthropicのFrontier Red Team（AIの危険な能力を調べるチーム）は、最近もClaudeで暗号の数字の出どころを突き止めた研究を出しています（「[Claudeが30分で解いた暗号の謎](/news/20261017-claude-nist-curve-seeds-mystery/)」）。AIがバグを見つけて攻撃に使う力が高まるなか、守る側も「直した」ではなく「証明した」と言える段階を目指す流れです。

## 日本のビジネスへの影響

- **使えるか**: 研究の成果で、そのまま買える製品ではありません。Claude自体は日本から使え、Theoremが公開したスキルを使えば開発者が自社のコードで試せます。各社のコーディング向けAIの違いは[コーディングAIのガイド](/best/coding/)にまとめています。
- **誰に効くか**: 情報システム部門やセキュリティ担当者には、社内システムが使っている公開ソフトの部品で、どれが「証明済み」かを確かめられる時代が近づいています。ソフトを納品する受託開発会社にとっては、品質の示し方が「テストを何件通した」から「どの条件を証明した」へ変わる可能性があります。
- **今すぐやれること**: 自社の製品やシステムが使っている公開ソフトの一覧を洗い出し、OSS-Fuzzに登録されているものと、今回の修正が出ているものを確認しておくと、更新の優先順位を付けやすくなります。
- **注意点**: 「AIで証明済み」と聞いても、証明した条件と前提の環境を必ず確かめてください。今回の証明は特定のCPUと構成が前提で、自社の環境で同じ保証が得られるわけではありません。また証明には大量の計算が必要で、費用は公表されていません。
