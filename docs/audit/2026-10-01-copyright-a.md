# 引用・転載の点検記録（2026-10-01・担当A・28本）

基準: EDITORIAL.md §4「著作権・引用のガバナンス」。各記事で、公式発表と最も詳しい報道1〜2本を開いて段落を見比べ（Meta系ドメインは開かない）、引用カードの原文が公式ページに一字一句あるか、本文の「」に発言者・媒体・sources が揃っているか、引用の割合が2割以内かを確かめた。最後に `AIDEJIMA_DIST=… python3 build.py` で、28本とも「引用（原文＋訳）」「sources にない」「英語の原文」「「」引用」の注意が0件であることを確認した。

## 記事ごとの結果

- 20260930-amd-acquires-world-labs: OK（引用カード2つはAMDの発表文とLi氏のSubstackに原文どおりある。スーCEOの「」はAMDの発表文にあり sources にも入っている。構成は5つの情報源から組んだ独自のもの）
- 20260930-anthropic-glm-5-3-cyber-capabilities: 修正（「何が発表されたか」がAnthropicの研究ページの論点の順番どおりだったので組み直した。小見出しで2つに分け、回避の手法とClaudeの場合を比べる表を作り、MythosとCAISIの話は「背景」へ移した）
- 20260930-anthropic-ipo-prospectus: 修正（リスク要因の節がCTechの記事と同じ順番・ほぼ訳文だったので書き直した／ロイターの地の文を「」で引いていたので言い換えた／47.3億ドルを「ブルームバーグが8月に報道」としていたが確認できず、sourcesにあるFortuneを出典に改め、「訂正」節を置いた）
- 20260930-chatgpt-office-apps-codex: 修正（アルトマン氏の「」の出典をCNBCとしていたのにsourcesに無かったので、記事で発言を確かめて追加した／Codexの段落が直後の引用カードと同じ内容だったので書き換えた）
- 20260930-claude-opus-5-5-prompting-guide: OK（引用カード2つは公式ガイドに原文どおりある。論点を並べ替えて取捨した独自のまとめ。「」は例文と機能名だけ）
- 20260930-google-ai-overviews-publisher-payments: 修正（The Decoderの分析を1文ずつ訳していた箇所を言い換えた／Digidayにある関係者の発言「peanuts」に、発言者と媒体を書き添えた）
- 20260930-meta-muse-permission-address-leak: 修正（Meta系ドメインは開いていない。エイトン氏の段落がDecryptの文の順番をなぞっていたので結論が先に来る形に組み直し、出所を書いた／Inc.のコラムの文を「」で引いていた箇所に、Daring Fireball経由であることを書き添えた）
- 20260930-nvidia-open-agent-safety-platform: 修正（「背景」がCNBCの段落の順番どおりだったので組み直した。Huang氏の発言にはBusiness Insider・CNBCの出所を付けた／Sidorkin氏の記事が9月30日に改訂されて主張の一部が取り下げられていたので、9月29日時点の版（Internet Archive）をsourcesに足し、本文にも改訂を明記した／どの版でも確かめられないSentryの記述を削り、「訂正」節を置いた）
- 20260930-openai-30b-round-1-4t-valuation: 要判断（引用カード2つは原文どおりで、構成も独自なので本文は直していない。ただし「ブルームバーグとFTが9月中旬に評価額1.2兆ドル超での調達検討を報じた」の一文は、sourcesのどのページでも確かめられなかった。TechCrunchとCTechは直接開いて確認した。出所を確かめるか、削るかの判断が要る）
- 20260930-openai-australia-agent-breach-apology: 修正（メディケアの段落がTechCrunchの文の順番どおり、3機関の箇条書きがThe Next Webの文の順番どおりだったので、OpenAIの謝罪文を軸に機関ごとの表に組み直した／時系列の表の出所（OpenAIの謝罪文とABC Newsの9月24日の時系列）を書き添えた。8月11日・9月15日はABC Newsの記事で確認した）
- 20260930-openai-devday-2026-roundup: 修正（出所の補完のみ。The VergeのURLが途中で切れていたので直した／Willison氏の記録とHNの970ポイントの出所をsourcesに足した）
- 20260930-openai-dots-always-on-agents: 修正（引用割合がちょうど20%だったので、本文と内容が重なる引用カードを1つ外した（16%）／Casey Newton氏の評価とHNの反応の出所をsourcesに足した）
- 20260930-openai-gpt-6-1-sol: 修正（評価結果の箇条書きが公式発表と同じ順番だったので用途別の表に組み直した／Ars Technicaの段落をほぼ文ごとに訳していたので書き直した／CFOの発言（CNBC）とHNの出所をsourcesに足した）
- 20260930-trump-super-intelligence-order-ai-accord: 修正（95字の協定名など文書の名称を『』にした／「道義的には拘束力がある」に媒体名（ABC News、BBC）を添えた／ABC Newsの文を訳していた箇所を言い換えた／GPT-6.1 Astraの公開見送りの出典をCNNとしていたが実際はBBCだったので直し、既存の「訂正」節に追記した）
- 20261001-ai-chat-privacy-trackers-study: 修正（HNの複数の書き込みをまとめたものを「」で囲んでいたので地の文にした／HNの種別を「コミュニティ」に直した）
- 20261001-ai-tamagotchi-companion-devices: 修正（「AIたまごっち」はThe Vergeの言い方だと本文に明記した／The Vergeの有料部分にしか無いRabbit R1の記述を削った／Apptopiaの60万人の出所として、無料で読めるThe Vergeの別記事をsourcesに足した）
- 20261001-airbnb-ai-search-social-fall-update: 修正（AI機能とソーシャル機能の箇条書きが公式発表の項目を1つずつ順に訳した形だったので、公式発表とTechCrunchの事実で組み直した）
- 20261001-astrabox-codex-arcade-game-generator: 修正（本文で触れているのにsourcesに無かった2件（r/LocalLLaMAの投稿、同名の別プロジェクト）を足した。Redditは403で開けず、collect.pyの収集記録で投稿があることを確かめた）
- 20261001-aws-bedrock-claude-in-region-seoul-singapore: 修正（後半の2段落がAWSブログの「In-region inference」の節を文の順番どおりになぞっていたので組み直した）
- 20261001-bain-ai-6-trillion-revenue-report: 修正（レポートの4分野の箇条書きの訳を表に組み直した／媒体名のない「」（The Nationalの報道内容）とHNの言い換えの「」を地の文にした／HNの種別を直した）
- 20261001-barclays-claude-bankwide: 修正（Anthropicの公式ブログ1本を段落の順番どおりにほぼ訳した構成だったので、3つの用途の表を軸に自分の言葉で書き直した。引用カードは2つから1つに減らした（19%→10%）。sourcesにある金融機関向けページからCitiの事例を1文足した）
- 20261001-california-ai-firing-law-sb947: OK（引用カード2つ（条文・知事室）は原文どおりある。条文・知事室・Engadgetを組み合わせた独自の構成）
- 20261001-cloudflare-agent-tools-roundup: OK（公式ブログ5本を組み直したまとめ。カードの原文も数字も一致）
- 20261001-cloudflare-pay-per-use-beta: OK（カード2つは原文どおりある。比較表など独自の構成。参加手順の4段階が公式と同じ順番なのは、手順そのものの順番のため）
- 20261001-deepmind-synthid-bio: 修正（「なぜ必要か」の節が公式ブログの節の並びどおりだったので、Ars Technicaの説明を起点に組み直した）
- 20261001-deepseek-huawei-ascend-opensource: OK（引用カード2つは公式リポジトリのREADMEに原文どおりある。数字もリポジトリと一致。構成は独自）
- 20261001-doordash-text-ordering-ai-agent: 修正（公式リリースの「Here's how it works」の箇条書きを1つずつ訳した形だったので、3つの役割に分けた文章に組み直した／リードの「iOS利用者」は出典に無い書き方だったので「米国の利用者」に直した）
- 20261001-draftkings-ai-gambling-targeting-eff: 修正（NYTの本文を直接読んでいないのにNYT由来の発言3か所を「」で引いていたので、間接話法にして伝えた媒体（Tech Times、Yogonet、Complete iGaming）を明記した／HNの564ポイントの出所をsourcesに足した／「20を超える指標」をTech Timesの「more than two dozen」に合わせて「24を超える」にした）

## 要判断として残したもの

1. **30b**：「ブルームバーグとFTが9月中旬に評価額1.2兆ドル超を報じた」の出所がsourcesに無い。WebSearchの上限に達していて追加の確認ができなかった
2. **barclays**：sourcesがAnthropicの3ページだけで、第三者の報道による裏付けが無い（BloombergとThe Bankerが報じていることは分かったが、記事のURLは取れなかった）
3. **draftkings**：有料記事のNYT調査報道を、業界メディアの報道を通して伝える構成のまま。NYT本体をsourcesに入れるかは編集方針の判断になる
4. **astrabox**：r/LocalLLaMAの投稿は開けず、収集記録だけで確かめた
5. **deepseek**：「TileLangがV4系モデルの学習で演算子の実装の大半を担う」は、出典のDeepSeek公式WeChatがCAPTCHAで開けず、直接は確かめていない（The Decoder経由のNYTの記述とTileLangのREADMEで裏付けた）
6. **ai-tamagotchi**：タイトルの「AIたまごっち」はThe Vergeの見出しの言い方を借りている。本文では出所を明記した
7. 出所を書き足した影響で、5本（ipo・glm・meta-muse・trump・nvidia）が本文の長さの注意（3,600字超）に新しくかかった。著作権の点検の範囲外なので削っていない
