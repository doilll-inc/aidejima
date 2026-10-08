---
{
  "title": "韓国の銀行から約2万6000人分の情報流出、攻撃者はAIで侵入しClaudeに売り先も相談",
  "description": "韓国の大手銀行など複数の金融機関で9月末から情報流出が相次いだ。米CrowdStrikeは、攻撃者が中国製のAI侵入ツールで攻撃を自動化し、Claudeに盗んだデータの売り先まで尋ねていたと分析した。確認された被害は約2万6000人分。",
  "date": "2026-10-08T19:55:00+09:00",
  "category": "policy",
  "tags": ["CrowdStrike", "ARTEX", "セキュリティ", "Claude Code", "DeepSeek", "金融"],
  "summary": [
    "韓国の新韓銀行など複数の金融機関で9月末から不正アクセスが続き、確認された流出は約2万6000人分にのぼると韓国紙が報じた",
    "米セキュリティ企業CrowdStrikeは、攻撃者が中国製のAI侵入ツールとDeepSeekなどのAIで攻撃を自動化したと分析した",
    "攻撃者の作業記録には、AIのClaudeに盗んだデータの売り先を尋ねたやり取りも残っており、少人数でも短期間に多くの侵入ができると警告した"
  ],
  "sources": [
    {"title": "Unknown Threat Actor Uses AI-Driven ARTEX to Target South Korean Finance", "publisher": "CrowdStrike", "url": "https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/", "kind": "公式発表"},
    {"title": "Exclusive: Chinese AI tool ARTEX used in wave of bank hacks, probe finds", "publisher": "The Herald Business", "url": "https://biz.heraldcorp.com/article/10892497", "kind": "報道"},
    {"title": "Shinhan, Kookmin, Hana data breaches fuel concerns over AI-powered cyberattacks in financial sector", "publisher": "The Korea Times", "url": "https://www.koreatimes.co.kr/path/A2026100210440004938", "kind": "報道"},
    {"title": "Police open formal AI bank hack probe", "publisher": "Korea JoongAng Daily", "url": "https://www.koreajoongangdaily.com/business/police-open-formal-ai-bank-hack-probe/12907472", "kind": "報道"},
    {"title": "AI-powered hacking tools enabled a likely single attacker to breach multiple South Korean banks", "publisher": "The Decoder", "url": "https://the-decoder.com/ai-powered-hacking-tools-enabled-a-likely-single-attacker-to-breach-multiple-south-korean-banks/", "kind": "報道"}
  ],
  "thumb_text": "AIで銀行に侵入",
  "thumb_style": "diorama",
  "thumb_prompt": "A miniature bank vault diorama at night where a single tiny hooded figure sits at a laptop while dozens of small toy robots swarm out across the floor, prying open rows of filing drawers and carrying away paper folders.",
  "share_text": "韓国の銀行で約2万6000人分の情報流出。攻撃者はAIで侵入を自動化し、Claudeに売り先まで相談していた",
  "editor_note": ""
}
---
韓国の大手銀行など複数の金融機関で9月末から相次いだ顧客情報の流出について、米セキュリティ企業CrowdStrikeは現地時間10月7日、攻撃者がAIを使って侵入を自動化していたとする分析を公開しました。韓国の報道によると、確認された流出は4行で合わせて約2万6000人分にのぼります。

## 何が起きたか

韓国紙の報道を合わせると、最初に被害が出たのは新韓銀行です。9月28日、融資の仲介業者が審査の進み具合を確かめるための仕組みが認証を突破され、2万5729人分の氏名、電話番号、年収、借入限度額などが抜き取られました。続いてKB国民銀行で119人分、ハナ銀行で89人分、BNK釜山銀行で外部委託の従業員11人分の流出が判明し、ウリィ銀行とNH農協銀行も攻撃を受けたものの流出はなかったと報じられています。

狙われたのは、いずれも行員や取引先が使う社内向けの仕組みでした。ネットバンキングやスマホのアプリとは別のもので、銀行側は取引の記録やお金の移動に関わるデータは漏れていないと説明しています。

CrowdStrikeは、攻撃者が管理するサーバーの中身が外から見える状態になっていたことから、攻撃の手順を細かく読み取れたとしています。

:::quote https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/ | CrowdStrike公式ブログ「Unknown Threat Actor Uses AI-Driven ARTEX to Target South Korean Finance」
> Analysis of threat actor-controlled open directories uncovered Claude Code session histories, ARTEX configuration files, and Claude memory files, providing direct insight into the threat actor's operational methodology and tooling.
攻撃者が管理する公開状態のフォルダを分析したところ、Claude Codeの作業履歴、ARTEXの設定ファイル、Claudeの記憶ファイルが見つかり、攻撃者の手口と道具を直接知る手がかりになった。
:::

## AIはどう使われたか

中心にあったのは「ARTEX」です。ARTEXとは、中国で開発されたオープンソース（誰でも無料で入手できる形で公開されたソフト）の侵入テスト用ツールで、本来は自社の守りの弱点を探すために使う道具を、AIが自分で考えて進める仕組みにしたものです。

CrowdStrikeによると、攻撃に使われたARTEXは中国のDeepSeekの「DeepSeek v4.1-flash」を主な頭脳にしており、そこに中国Zhipu AIの「GLM-5.3」と、xAIの「Grok 4.6」を補助として組み合わせていました。サーバーには、AIに侵入テストの進め方を指示する中国語の文書も置かれていました。

目を引くのは、AnthropicのAIを使った作業記録の中身です。攻撃者はClaude（Anthropicの対話AI）に、韓国から流出したデータは普通どこで売られているかを尋ね、韓国のデータを売買するTelegram（チャットアプリ）のグループ探しも頼んでいました。別の作業では、今回の侵入の「成果」を箇条書きにした「セキュリティ研究者の履歴書」をClaudeに作らせていたとしています。Claudeがどう答えたかは、報告には書かれていません。

攻撃者についてCrowdStrikeは、中国語を使う人物で、目的はお金だと「中程度の確信」で見ています。ただし既知の攻撃グループとは結び付けておらず、履歴書の依頼に含まれていた個人情報も本人のものとは断定できないとしています。

## 韓国当局の受け止め

韓国の金融委員会は10月2日に緊急会議を開き、警察は10月6日に正式な捜査に切り替えました。Korea JoongAng Dailyによると、捜査には28人が当たり、金融監督院は日本を含む12か国にある19の攻撃元アドレスを突き止めています。

韓国の金融保安院の担当者は、AIが攻撃に使われたのは事実だが、人の関与なしにAIが単独で動いたわけではなく、ハッカーがAIを道具として使ったのだとThe Herald Businessに説明しています。攻撃は社内システムを乗っ取るのではなく、問い合わせを繰り返してデータを引き出す手口で、預金を直接動かされるおそれは低い一方、流出した情報が電話詐欺に悪用されかねないとも伝えています。

## 反応と論点

CrowdStrikeが今回の件で最も強調したのは、攻撃の速さです。

:::quote https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/ | CrowdStrike公式ブログ「Unknown Threat Actor Uses AI-Driven ARTEX to Target South Korean Finance」
> This activity demonstrates how AI tooling can enable a financially motivated threat actor to conduct multiple intrusions within a short time span.
今回の活動は、金銭目的の攻撃者がAIの道具を使えば、短い期間に複数の侵入をやってのけられることを示している。
:::

ドイツのAI専門メディアThe Decoderは、この分析を受けて、複数の銀行への侵入が1人の攻撃者によるものだった可能性が高いと報じました。韓国の専門家からも、亜洲大学のクァク・ジン教授が、ハッカーは見つけた弱点すべてを攻めるもので、AIがその速度を大きく上げているとKorea JoongAng Dailyに語っています。

一方で慎重な見方もあります。ARTEXは誰でも入手できる公開ソフトなので、使われた痕跡だけで攻撃者の国籍は決められないという指摘を、同紙は多くの専門家の見方として伝えています。また、CrowdStrike自身も被害を受けた組織の数は確定していないとしており、全体の被害がさらに広がる可能性もあります。

AIの開発元にとっても重い事例です。攻撃者はAnthropicのClaude Codeを作業の土台にしつつ、頭脳には中国製を含む複数社のAIを差し替えて使っていました。作業用の道具と頭脳になるAIを組み合わせ直せるため、1社が対策を強めるだけでは悪用を止めにくいことが、実際の攻撃記録で示された形です（AIデジマ編集部の分析）。補助に使われたGLM-5.3については、9月末にAnthropicが[攻撃用のコードを作る力が限定公開の自社モデルに近いと警告](/news/20260930-anthropic-glm-5-3-cyber-capabilities/)していました。Claude Codeそのものについては、[Claude Codeの料金と選び方](/news/20261008-claude-code-pricing-plans/)の記事でも紹介しています。

## 日本のビジネスへの影響

- **日本にも関係するか**: 攻撃元のアドレスには日本のものも含まれていました。日本の企業のサーバーが知らないうちに踏み台にされている可能性もあり、海外の事件として片付けにくい内容です。ARTEXのような公開ツールは日本からも誰でも入手できます
- **誰に関係が深いか**: 金融機関や、取引先・代理店向けのポータルを持つ企業の情報システム担当と経営者です。今回狙われたのは顧客向けのアプリではなく、仲介業者の照会画面や行員の業務用スマホの仕組みといった「内向き」の入り口でした
- **今すぐやれること**: 社外の取引先や代理店がログインする画面を洗い出し、IDとパスワードだけで入れるものに、ワンタイムパスワードなどの二段階の確認を足すことです。あわせて、短時間に大量の照会が来たときに止める仕組みがあるかを確かめておくと、今回のような「問い合わせを繰り返して抜き出す」手口への備えになります
- **注意点**: 社内で生成AIの利用を禁じても、攻撃者の側は使い続けます。AIを使った攻撃は特別な手口ではなく、昔からある弱点を速く大量に突くものです。新しい対策製品を買う前に、パスワードの使い回しや古い社内システムの放置といった基本の穴をふさぐことが先です
