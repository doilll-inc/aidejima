# 著作権・引用の点検記録（2026-10-01・担当B、27本）

判断基準：EDITORIAL.md「著作権・引用のガバナンス」。記事ごとに、主な情報源（公式発表・README・本人投稿と、いちばん詳しい報道1〜2本）を開いて段落を見比べ、引用カードの原文が一字一句ページにあるか、本文の「」に発言者・媒体・sourcesが揃っているか、引用の割合（原文＋訳）が2割以内かを確かめた。Meta系ドメインは開いていない。言い換えだけの修正には「訂正」節を足していない（事実の誤りを直したものだけ足した）。数字などの事実は変えていない。

確認：`AIDEJIMA_DIST=/Users/tomo/.claude/jobs/43206470/tmp/dist_cb python3 build.py` で担当27本に「引用（原文＋訳）」「sources にない」「英語の原文」「「」引用」の注意なし（10月1日19時台）。

| 記事 | 結果 | 内容 |
|---|---|---|
| 20261001-elevenlabs-22b-valuation-tender | 要判断 | 転載・引用は問題なし（構成は公式ブログと別立て、カードは原文どおり）。ただし「企業向けの比率は1年前の40%から55%」の40%がsourcesのどのページにもない（55%は公式ブログにある）。削るか出典を足すかは編集判断。未修正 |
| 20261001-esp32s3-bitnet-llm-cluster | OK | README・workflow.mdを自分の言葉でまとめており直訳なし。カード原文どおり |
| 20261001-ftc-probe-openai-anthropic-ai-labs | 修正 | ロイターの地の文を訳して「」に入れていた1か所（「指示した開発者が責任を負う」）を自分の文に。複数報道を突き合わせた構成でなぞりはなし |
| 20261001-gemini-skills | 修正 | 「Gemsとの違い」の段落が公式ブログの文順に近かったため組み直し。公式ヘルプのコツを訳して「」にした3か所を地の文に（「」上限超え）。その出所のヘルプページをsourcesに追加し、原文とずれていた1点を原文に沿う形に |
| 20261001-github-copilot-hydrafusion-vs-code | 修正 | 3つの進め方の説明・表・料金の段落がChangelogと公式ドキュメントのほぼ直訳だったため、自分の言葉と構成に書き直し |
| 20261001-github-seclab-ai-agent-24-android-vulnerabilities | OK | ブログの順をなぞらず複数の情報源で構成。カード2枚とも原文どおり |
| 20261001-gmi-cloud-668m-series-b-nvidia | 要判断 | 転載・引用は問題なし。「2021年創業」がsourcesのページで確かめられない。未修正 |
| 20261001-google-diffusion-controller-image-generation | 修正 | 定義・重み付け・2つの学習方法の部分が公式ブログの文に近かったため、論文の要旨も使って自分の構成で書き直し |
| 20261001-google-gemini-4-argon | 修正 | HNの書き込みを訳して「」で引いていた2か所を地の文の要約に。HNの議論をsourcesに追加 |
| 20261001-hn-watch-scrimba-explainer-videos | 修正・要判断 | 「何を作ったか」2段落と仕組み・本数上限の段落が公式ドキュメントのほぼ順番どおりの訳だったため、作者のHN返信と合わせて書き直し。要判断：注意点の「Chrome拡張で作った動画も作る前に限定公開か非公開を選んで」は、ドキュメントでは公開で作られ後から変える手順とされ食い違う。未修正 |
| 20261001-hugging-face-open-tts-leaderboard | 修正 | 引用の必要が弱い2枚目のカード（CJKはCERで示す注記）を外し自分の説明に。5.2%に |
| 20261001-jeff-jeeves-open-decision-models | 修正 | READMEの訳に近かった2段落（ゼロショットの使い道、非公開モデル不使用の説明）を言い換え |
| 20261001-lathoa-math-app-ai-wrong-on-purpose | 修正 | 作者のShow HN投稿を文ごとに訳したような箇所（検証の手順と弱点）を自分で組んだ表に。作者のHNコメントの事実を足し、反応の整理を組み直し |
| 20261001-liveramp-chatgpt-ads-first-party-data | 修正 | 「反応と論点」がSearch Engine Journalの分析の流れをなぞり同誌の文を「」で引いていたため、「」を外し自分の構成で書き直し。LiveRampのカードを1文に |
| 20261001-lokutor-oido-esp32-speech-recognition | 修正 | 「論点」がREADMEの状況説明をなぞっていたため組み直し。本文で触れているr/LocalLLaMA投稿をsourcesに追加 |
| 20261001-magnitude-self-optimizing-inference-engine | 修正 | 創業の経緯の段落がLaunch HN投稿を文ごとに言い換えていたため構成を変えて書き直し。HN利用者の書き込みだと分かるように |
| 20261001-microllm-lab-tiny-llms-in-browser | OK | README・サイト・WRITEUP.md・HNを自分の構成でまとめており直訳なし。カード原文どおり |
| 20261001-micron-q4-fy2026-hbm-ai-memory | 修正 | ビルド指摘（引用22%）。需給見通しのカードを外し自分の文に。11.5%に。残したカードは決算説明資料に一字一句あることを確認 |
| 20261001-nvidia-kumo-tabular-open-model | 修正 | Hugging Face Blogの節の順番をなぞっていたため、モデルカードとGitHub READMEも使って構成を組み直し |
| 20261001-observer-ai-screen-watching-local-agent | 修正 | ビルド指摘（76字の英語「」）。訳だけの23字にし、発言者（作者）と媒体（r/LocalLLaMA投稿）を明記。READMEの用例を訳して並べた箇条書きを地の文に、言い換えに付いていた「」を外した |
| 20261001-openai-moonshot-distillation-campaign | 修正 | 本文が公式ブログの段落順をほぼなぞり文ごとの訳に近い箇所があったため、経過→手口→対策→背景に組み直し、論文と報道の事実で補った |
| 20261001-openai-sbdc-small-business-ai | 修正 | ビルド指摘（引用23%）。公式ブログの段落順と3本柱の訳をなぞっていたため、SBDC発表・報告書PDF・Inc.と突き合わせて役割表・倍率表で組み直し。長いカードを外し4.3%に |
| 20261001-openai-synopsys-gpt-synopsys | 修正・訂正 | 共同発表の順番どおりの直訳と、ロイター記事の文順をなぞった「収益」節を組み直し。ロイターの言い回しの「」を外した。The Decoderが書いていない見方を同誌の見方としていたため直し、「訂正（10月1日）」を置いた |
| 20261001-pac-bench-one-shot-pacman | OK | READMEと採点文書の要約で直訳なし。「」2か所は作者とHNを明記しsourcesあり |
| 20261001-papermono-eink-fridge-shopping-list | 修正 | READMEの「How it works」を文ごとに訳した段落を書き直し。本文と重なるREADMEのカードを外した。言い換えに付いていた「」を外した |
| 20261001-reddit-ends-rss-public-api | 修正 | ビルド指摘（引用20%超）。日程の表と重なる2枚目のカードを外し、TechCrunchの段落順をなぞっていた「反応と論点」を自分の切り口で組み直し。11.9%に。残したカードはr/modnews投稿（.rss経由）に一字一句あることを確認 |
| 20261001-tinyaiarena-ai-agents-battle | 修正 | ビルド指摘（引用21%）。ルールと作りの段落がREADMEの箇条書きを同じ順でなぞっていたため、CLAUDE.mdの事実も使って組み直し。READMEのカードを外し8.8%に。HNの「」2か所に発言者を書き足した |

集計：修正21本（うち訂正節1本）、OK 4本、要判断のみ（未修正）2本。要判断は計3件（elevenlabs・gmi-cloud・hn-watch-scrimba。いずれも転載ではなく事実の出典の問題）。
