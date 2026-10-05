---
{
  "title": "Googleがオープンソースのバグ報奨金を一時停止、AIが作った無効な報告が急増",
  "description": "Googleは10月1日、オープンソースの脆弱性に報奨金を払う「OSS VRP」で、製品の脆弱性の受け付けを止めた。AIを使った自動の報告が急増し、大半が無効だったためで、今後の方針は2027年1〜3月期に示す。",
  "date": "2026-10-05T10:30:00+09:00",
  "category": "policy",
  "tags": ["Google", "OSS VRP", "セキュリティ", "オープンソース", "ハルシネーション"],
  "summary": [
    "GoogleはOSS VRPで、製品の脆弱性の新規報告の受け付けを10月1日から一時停止した",
    "理由は自動化された報告の急増で、その大半が無効だったとGoogleは説明している",
    "サプライチェーンの報告と受付済みの報告は対象外で、今後の方針は2027年1〜3月期に示す"
  ],
  "sources": [
    {"title": "Google VRP の投稿（OSS VRPの受け付け停止）", "publisher": "X @GoogleVRP", "url": "https://x.com/GoogleVRP/status/2105689195180179605", "kind": "X投稿"},
    {"title": "Google froze its open source bug bounty program due to a ‘significant rise’ in AI submissions", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/10/04/google-froze-its-open-source-bug-bounty-program-due-to-a-significant-rise-in-ai-submissions/", "kind": "報道"},
    {"title": "Google pauses open source bug bounty program as AI-generated reports pile up", "publisher": "Crypto Briefing", "url": "https://cryptobriefing.com/google-pauses-open-source-bug-bounty-ai/", "kind": "報道"},
    {"title": "Curl shutters bug bounty program to stop AI slop", "publisher": "The Register", "url": "https://www.theregister.com/security/2026/01/21/curl-shutters-bug-bounty-program-to-stop-ai-slop/5063039", "kind": "報道"}
  ],
  "thumb_text": "OSS VRP",
  "share_text": "Googleがオープンソースのバグ報奨金で製品の脆弱性の受け付けを停止。AIによる無効な報告の急増が理由",
  "editor_note": ""
}
---
Googleは現地時間10月1日、オープンソースの脆弱性に報奨金を払う「OSS VRP」で、製品の脆弱性の新規報告の受け付けを一時停止しました。AIなどで自動化された報告が急増し、その大半が無効だったことが理由です。今後の方針は2027年1〜3月期に示すとしています。

## 何が起きたか

OSS VRP（Open Source Software Vulnerability Reward Program）とは、Googleが公開しているオープンソースのソフトウェアについて、脆弱性を見つけて報告した外部の研究者に報奨金を払う制度です。いわゆるバグ報奨金（バグバウンティ）の一つです。

Googleの脆弱性報奨金チームは10月1日、公式Xで停止を告知しました。投稿では、OSS VRPで製品の脆弱性の報告を当面受け付けないこと、サプライチェーン関連の報告と処理中の報告には影響しないことを伝え、ほかの報奨金制度に報告先を移すよう勧めています。

{{x:https://x.com/GoogleVRP/status/2105689195180179605}}

停止の範囲を整理すると次のとおりです。

- **止まるもの**：OSS VRPでの、製品そのものの脆弱性の新規報告
- **続くもの**：OSS VRPのサプライチェーン関連の報告（ソフトの配布や依存関係を狙う攻撃への対策）、10月1日より前に出された報告の審査
- **代わりの窓口**：Googleのほかの報奨金制度。TechCrunchとCrypto Briefingによると、Google Cloudの一部のリポジトリの脆弱性はCloud VRPで受け付け、修正を出した人に報いるPatch Rewards Programも案内しています

TechCrunchによると、Googleは制度のルールページで、停止の理由を「自動化された報告の大幅な増加」とし、その大半が有効ではなかったと説明しています。制度の今後については、2027年1〜3月期に知らせるとしています。

## 背景

AIを使えば、コードを読ませて「脆弱性らしきもの」の報告書を大量に作れます。報告書は体裁が整っていても、実際には悪用できない、存在しない欠陥を書いたものが少なくありません。それでも受け取った側は、一件ずつ再現を試さないと無効だと判断できません。報告者の手間はほぼゼロなのに、確認の手間は人間に残るという不均衡があります。

オープンソースの世界では、Googleより先に同じ問題にぶつかった例があります。The Registerによると、通信ツール「curl」の開発者Daniel Stenberg氏は1月、AIが作った質の低い報告を減らすため、同プロジェクトの報奨金制度を終えると決めました。最後の1週間に届いた7件はいずれも本物の脆弱性ではなかったと報じられています。

Googleの停止が重いのは、規模の違いです。curlは一つのプロジェクトですが、OSS VRPはGoogleが関わる多数のオープンソースを対象にした制度です。資金も人手もある大企業でさえ、報奨金を払う仕組みを維持できなくなったことを示しています。

## 反応と論点

報道では、確認作業が本来の仕事を圧迫したという見方が目立ちます。TechCrunchは、Googleの技術者とオープンソースの保守担当者が、無効な情報やAIの誤り（ハルシネーション）を含む報告に追われていたと伝えています。Crypto Briefingは、ボランティアや小さなチームで保守されているプロジェクトほど、存在しない脆弱性を否定する余力がないと指摘しています。

一方で、論点はAIを使うこと自体ではなく、「確かめずに出す」報告の量です。報奨金を止めれば悪質な大量報告は減りますが、正当な研究者にとっても報告の動機が一つ減ります。Googleが2027年にどんな形で再開するのか、たとえば報告者の実績や再現手順の提出を条件にするのかは、まだ示されていません。

## 日本のビジネスへの影響

OSS VRPは世界の研究者が対象の制度で、停止は日本からの報告にも同じく及びます。日本のセキュリティ研究者で、Google関連のオープンソースの脆弱性を報告していた人は、Cloud VRPやPatch Rewards Programなど、ほかの窓口の条件を確かめる必要があります。

より広く関係するのは、自社でバグ報奨金や脆弱性の受付窓口を持つ企業のセキュリティ担当者と、オープンソースを公開している開発者です。AIが作った報告は今後も増える前提で、受付の設計を見直す時期に来ています。今すぐできるのは、報告フォームで再現手順と影響の説明を必須にし、それがない報告は優先度を下げる運用を決めておくことです。

注意したいのは、窓口を閉じすぎることです。報告の受付をやめると、本物の脆弱性が公開の場で暴露される危険が高まります。AIで報告を一次仕分けする仕組みを入れる手もありますが、AIの判断で本物の報告を捨ててしまわないよう、最終判断は人が持つ体制にしておくべきです。社内でAIのコーディングツールを使ってコードを点検する場合も、出てきた指摘は必ず人が再現して確かめる運用が前提になります。ツール選びは[コーディング支援AIのガイド](/best/coding/)を参考にしてください。
