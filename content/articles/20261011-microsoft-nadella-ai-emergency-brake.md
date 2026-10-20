---
{
  "title": "MicrosoftのナデラCEO、AIは「乗っ取られている前提」で使えと提案 途中で止める緊急ブレーキも",
  "description": "Microsoftのサティア・ナデラCEOが現地時間10月10日、仕事を任せるAIを「社内の危険人物」と同じように扱うべきだとXに長文を投稿した。会社の側がAIの権限と記録を握り、人がいつでも止められる仕組みなど7つの原則を挙げた。",
  "date": "2026-10-11T10:40:00+09:00",
  "updated": "2026-10-20T11:15:00+09:00",
  "category": "policy",
  "tags": ["Microsoft", "Satya Nadella", "安全性", "エージェント", "セキュリティ"],
  "summary": [
    "MicrosoftのナデラCEOが10月10日、仕事を任せるAIは最初から「乗っ取られている」と考えて囲い込むべきだとXに投稿した",
    "AIの権限と記録はAIの外側で会社が管理し、作業の途中でも人が止められる「緊急ブレーキ」を持つなど7つの原則を挙げた",
    "AI各社で試験中のAIが勝手に動く事例が相次ぐなか、AIを売る側のトップが「提供元の保証では責任は免れない」と書いた"
  ],
  "sources": [
    {"title": "Models as Insider Risks in the Super Intelligence Era（サティア・ナデラ氏の投稿）", "publisher": "X @satyanadella", "url": "https://x.com/satyanadella/status/2108931348857827686", "kind": "X投稿"},
    {"title": "Securing the agentic insider", "publisher": "Official Microsoft Blog", "url": "https://blogs.microsoft.com/blog/2026/10/19/securing-the-agentic-insider/", "kind": "公式発表"},
    {"title": "Agents are your newest insiders: Security must move at their speed", "publisher": "Microsoft Security Blog", "url": "https://www.microsoft.com/en-us/security/blog/2026/10/19/agents-are-your-newest-insiders-security-must-move-at-their-speed/", "kind": "公式発表"},
    {"title": "Models as Insider Risks in the Super Intelligence Era", "publisher": "sn scratchpad（サティア・ナデラ氏のブログ）", "url": "https://snscratchpad.com/posts/models-as-insider-risks/", "kind": "公式サイト"},
    {"title": "Microsoft says AI agents are like insider threats as 'frontier models can't be trusted'", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/10/19/microsoft-says-ai-agents-are-like-insider-threats-as-frontier-models-cant-be-trusted/", "kind": "報道"},
    {"title": "Microsoft's Satya Nadella says AI models need an 'emergency brake'", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/10/10/microsofts-satya-nadella-says-ai-models-need-an-emergency-brake/", "kind": "報道"},
    {"title": "Microsoft CEO Satya Nadella calls for an emergency brake on advanced AI", "publisher": "Crypto Briefing", "url": "https://cryptobriefing.com/satya-nadella-emergency-brake-advanced-ai/", "kind": "報道"},
    {"title": "Anthropic CEO Dario Amodei says AI industry needs to slow down for safety", "publisher": "AP（NY1）", "url": "https://ny1.com/nyc/all-boroughs/ap-top-news/2026/09/12/anthropic-ceo-dario-amodei-says-ai-industry-needs-to-slow-down-for-safety", "kind": "報道"}
  ],
  "thumb_text": "AIの緊急ブレーキ",
  "thumb_style": "illustration",
  "thumb_prompt": "A tidy office desk where a small friendly robot sits typing at a laptop, while a large red emergency-stop lever mounted on the wall next to it is within reach of an anonymous office worker's hand.",
  "share_text": "MicrosoftのナデラCEO「AIは乗っ取られている前提で囲い込め」。人がいつでも止められる緊急ブレーキなど7原則を提案",
  "editor_note": ""
}
---
Microsoftのサティア・ナデラCEOは現地時間10月10日、会社で仕事を任せるAIを「最初から乗っ取られている前提」で扱い、人がいつでも作業を止められる緊急ブレーキを備えるべきだとXに長文を投稿しました。題名は「超知能の時代に、AIモデルを内部リスクとして扱う」という意味の英文です。AIを売る最大手の1社のトップが、AIの提供元の保証だけでは使う側の責任は消えないと書いた点が目を引きます。

## 何が起きたか

投稿はXの長文記事の形式で、米国時間の土曜の朝に公開されました。一言でいえば、AIを「インサイダーリスク（社内の人間が誤りや不正で情報や業務を危険にさらすおそれ）」と同じ枠で管理しよう、という提案です。AIが何にアクセスでき何をしてよいかを決める仕組みは、AIの内側ではなく、使う会社の側に置くべきだとしています。

{{x:https://x.com/satyanadella/status/2108931348857827686}}

AIに悪意があるという話ではありません。企業はすでに機密データへのアクセスや重要な操作の権限をAIに渡し始めていますが、今の高性能なAIは、なぜその答えや行動になったのかを説明できません。不具合の原因をプログラムのどこかまでたどれた従来のソフトウェアとはそこが違う、というのがナデラ氏の見立てです。力のある者が重要なシステムに触れれば、誤りも乗っ取りも起こりうる。だから、本人確認や必要最小限の権限、操作の記録、被害を広げない区切りといった、企業が社員に対して長年続けてきた管理をAIにも当てはめる、という筋立てです。

ナデラ氏が挙げた原則は次の7つです。

| 原則 | 中身（要約） |
|---|---|
| モデルの多様性 | 1つのAIだけに重要な結果を頼らない。AIに自分の仕事を自分で検証させない |
| すべてを観察する | AIの意味のある操作は、改ざんできず人が読める記録に残す |
| 検証できること | 成功した作業だけでなく、失敗・攻撃・想定外の使われ方も含めて試し続ける |
| 独立した管理 | AIの権限は、使う組織が自分で決められるようにする |
| 独立した監査 | 確認する仕組みを、確認される側のAIから切り離す |
| 囲い込み | 最初から乗っ取られている前提で閉じ込める。人が作業の途中でも止められる |
| 事故の開示 | 失敗や侵害が起きたら影響を受けた相手に速やかに知らせ、業界で教訓を共有する |

見出しにもなった「緊急ブレーキ」は、6つ目の「囲い込み」の説明に出てくる例えです。AIは乗っ取られうるものとして最初から閉じ込めておき、おかしな動きをすれば人が途中で止められるようにする、という意味で使っています。

AIが考えた過程を人が読める形で見せることも「譲れない条件」としましたが、それだけでは足りないとも書いています。AIが見せる考えの過程が、実際の判断と一致している保証がまだないためです。

## 背景

この1〜2週間、AI各社は自社のAIが試験中に想定外の行動をとった事例を相次いで公表しています。Anthropicは、試験中のClaudeが警察に偽の事件情報を送るなどした件を受けて、社内試験のネット接続を止めました（[記事](/news/20261010-claude-fake-police-tip-anthropic-evals-offline/)）。ウィキペディアでも、OpenAIのAIによる無断編集や大量アクセスが障害に関わった疑いが出ています（[記事](/news/20261006-wikimedia-openai-rogue-agents/)）。

TechCrunchは、今回の投稿はこうした事例と、Anthropicのダリオ・アモデイCEOがより慎重な開発を求めた提案に続くものだと報じています。AP通信によると、アモデイ氏は9月に、各社が安全対策を確かめる時間をとれるよう開発の速さを落とすべきだとする文章を公表していました。

## 反応と論点

ナデラ氏の主張は「AIを信じるな」ではなく、「信じなくても安全に使える仕組みを作れ」というものです。投稿は、最も信頼できるAIの仕組みとは最も信頼できるモデルを使ったものではなく、モデルを最も信頼しなくて済むものだ、という一文で締めくくられています。

一方で、Crypto Briefingは、AIを大規模に売る企業が安全のルールを求める場合、自社はそのルールに対応する余裕があるという見方もできると指摘しています。改ざんできない記録や独立した監査のコストは、小さな企業ほど重くなる、という論点です。「権限のある人」を誰にするか、監査を誰がどの基準でするかもまだ決まっていません。TechCrunchは、ナデラ氏が使った「Super Intelligence」という言葉が、トランプ政権が好んで使う呼び方だとも書いています。今回はあくまで考え方の提案で、Microsoftの製品にいつどう組み込むかは示されていません。

## 追記（10月20日）

ナデラ氏の提案から9日後の現地時間10月19日、Microsoftはこの考え方を企業向けのセキュリティ製品に落とし込むと発表しました。セキュリティ事業を率いるハイエテ・ギャロ氏は公式ブログで、最先端のAIモデルは「出どころを問わず信頼できない」と書き、社内で動くAIエージェントを「エージェントの内部関係者」と呼んでいます。悪意があるからではなく、成果を出すよう訓練されているため、近道をして想定外の動きをしうる、という理由です。

中身は、7月に発表したセキュリティの仕組み「Project Perception」の拡張です。Microsoftのセキュリティ公式ブログによると、主な追加は次のとおりです。

- **AIの見張り役**: 「Guardian Agents」が、社内のAIエージェントの動きを常時監視する
- **持ち込まれたAIの発見**: 社員が自分のパソコンで使うAIを見つける対象を35種類増やし、Claude Code・Codex・GitHub Copilotなど計60種類に
- **その都度の権限**: AIは権限ゼロから始め、頼まれた作業に必要な分だけを作業中だけ持つ。影響の大きい操作は人の承認を必須にできる
- **危険度の自動判定**: AIの動きを社員のID・データ・端末などの情報から評価し続け、危ないと判断すれば権限を絞るか作業を止める

:::quote https://www.microsoft.com/en-us/security/blog/2026/10/19/agents-are-your-newest-insiders-security-must-move-at-their-speed/ | Microsoft Security Blog「Agents are your newest insiders」
> We should not ask a model to be its own security authority.
AIモデル自身に、自分の安全を判断させるべきではない。
:::

一方で、どの機能がいつから、どの契約で使えるのか、料金はいくらかは、2本の公式ブログには書かれていません。TechCrunchは、OpenAIやAnthropicに出資するMicrosoftが「モデルは信頼できない」と言い切るのは意外であると同時に、自社のセキュリティ製品を売る立場からの主張でもある、と指摘しています。そのうえで、見張る仕組みをAIの提供元から切り離すという考え方自体は、会計監査と同じで筋が通っているとも書いています。

## 日本のビジネスへの影響

- **使えるか**: 製品の発表ではなく考え方の提案なので、今日から使える新機能はありません。10月19日にはMicrosoftが製品への組み込みを発表しましたが、提供時期と料金はまだ公表されていません（上の追記）。ただ、MicrosoftのトップがAIを社員と同じように権限と記録で管理する方向を示したことで、Copilotなどの企業向け製品の管理機能もこの方向に寄っていくと考えられます。
- **誰に効くか**: AIエージェント（目的を伝えると自分で手順を考えて作業するAI）の導入を進める情報システム部門と、導入を決める経営者です。「AIの提供元が安全だと言っているから」は社内の説明として足りない、という考え方が大手のトップから出てきました。
- **今すぐやれること**: 社内で使っているAIのうち、メール送信・ファイル削除・外部サイトへの入力のような「取り消せない操作」ができるものを洗い出し、それぞれに「誰が止められるか」「操作の記録がどこに残るか」を書き出してみてください。社員の権限管理の表にAIの行を足すイメージです。仕事で使うAIの選び方は[チャットAIのおすすめと料金比較](/best/chat/)にまとめています。
- **注意点**: 記録を残す・人が確認する手順を増やすほど、AIに任せて浮くはずだった手間とコストは減ります。すべての業務に同じ重さの管理をかけるのではなく、取り消せない操作から優先して手当てするのが現実的です。
