---
{
  "title": "スマホの中だけでチャットの詐欺を見抜いて警告するAI、Googleとシンガポール政府が共同開発",
  "description": "Google DeepMindとシンガポール政府のGovTechが、スマホの中だけで動き、チャットのやり取りから詐欺を見抜いて警告するAIを開発した。シンガポールでは2019年以降の詐欺被害が40億シンガポールドルを超えている。",
  "date": "2026-10-14T18:05:00+09:00",
  "category": "policy",
  "tags": ["Google DeepMind", "Gemma", "GovTech Singapore", "詐欺", "セキュリティ", "プライバシー"],
  "summary": [
    "Google DeepMindとシンガポール政府のIT機関GovTechが、チャットの会話から詐欺を見抜いて警告するAIを共同開発した",
    "会話の中身はスマホの外に出さずに端末の中だけで判定するため、政府もGoogleも利用者のチャットを読めない仕組み",
    "どのアプリにいつ入るかは未発表。段階的に導入し、他の国への展開も検討しているという"
  ],
  "sources": [
    {"title": "Google DeepMind and Singapore Government collaborate to build fine-tuned AI model for scam detection", "publisher": "Google DeepMind", "url": "https://deepmind.google/blog/on-device-ai-scam-detection-mddi/", "kind": "公式発表"},
    {"title": "How Jian Ming is tackling scams at their roots - Public Sector Transformation Awards 2026", "publisher": "GovTech Singapore", "url": "https://www.tech.gov.sg/technews/how-jian-ming-is-tackling-scams-at-their-roots-public-sector-transformation-awards-2026/", "kind": "公式発表"},
    {"title": "Scam prevention", "publisher": "GovTech Singapore", "url": "https://www.tech.gov.sg/products-and-services/for-citizens/scam-prevention", "kind": "公式ドキュメント"}
  ],
  "thumb_prompt": "Close-up of a hand holding a smartphone on a crowded evening train, the chat screen glowing with a soft amber warning light while a tiny translucent padlock hovers just above the screen.",
  "thumb_style": "photo",
  "thumb_text": "詐欺検知AI",
  "share_text": "チャットの詐欺をスマホの中だけで見抜いて警告。Google DeepMindとシンガポール政府が会話を外に出さないAIを開発",
  "editor_note": ""
}
---
Google DeepMindとシンガポール政府のIT機関GovTech Singaporeは現地時間10月14日、チャットのやり取りから詐欺を見抜き、その場で利用者に警告するAIを共同で開発したと発表しました。会話の中身をスマホの外へ送らず、端末の中だけで判定するのが特徴です。シンガポールでは2019年以降、詐欺の被害額が40億シンガポールドルを超えています。

## 何が発表されたか

今回のAIは、Googleが無料で公開している小型のAIモデル「Gemma」を、シンガポールで実際に使われた詐欺の会話で追加学習させたものです。公的機関や銀行、地元の有名人になりすます手口や、地域で流行している手口を学ばせました。DeepMindは、汎用のAIでは地域ごとのだましの手口を見抜きにくいことを、専用に作り直した理由に挙げています。

チャットの中で相手が人を操ろうとする流れを見つけると、お金や個人情報を渡す前に「いったん手を止めて注意して」と促す警告をその場で出します。判定は2段階です。

1. 軽い判定の仕組みが、届いたメッセージをふるい分ける。問題がなければここで終わる
2. 怪しいものだけ、追加学習したGemmaが前後の会話をまとめて読み、本当に詐欺か、誤報かを判断する

ふだんは軽い判定だけを動かすことで、スマホの電池の消耗を抑える設計です。

:::quote https://deepmind.google/blog/on-device-ai-scam-detection-mddi/ | Google DeepMind「Google DeepMind and Singapore Government collaborate to build fine-tuned AI model for scam detection」
> Fighting scams shouldn't mean sacrificing personal privacy.
詐欺と戦うために、個人のプライバシーを犠牲にするべきではありません。
:::

AIが読めるのは、本人が同意し、各アプリの利用規約で認められた範囲の会話だけです。DeepMindは、この導入によってシンガポール政府もGoogleも利用者の会話にアクセスできないと説明しています。学習はGovTechが管理するクラウド環境の中で行い、個人を特定できる情報は使わず、匿名にした詐欺の通報データなどを使ったとしています。

## まだ決まっていないこと

発表では、どのアプリに組み込まれるのか、いつから使えるのかは明らかにされていません。アプリへの導入は政府と一緒に「慎重に段階を踏んで」進めるとし、他の国での導入も検討中だとしています。見逃しや誤報の割合といった精度の数字も公表されていません。成果は国際会議「シンガポール国際サイバーウィーク（SICW 2026）」で紹介されました。

## 背景

DeepMindによると、シンガポールで届け出のある犯罪の半分以上が、投資詐欺や偽の求人、公務員へのなりすましといった詐欺です。被害額のうち最大80%は、言葉巧みに人をだます手口によるものだといいます。

GovTechはこれまで、詐欺サイトや詐欺に使われる電話番号を見つけて止める仕組みを警察と運用してきました。公式サイトによると、2025年にはWhatsAppの番号8万7,700件超、携帯の回線11万5,800件、ウェブサイト7万6,000件超の遮断に関わっています。ただ、だましのやり取りそのものは暗号化されたチャットの中で進むため、外からは見えません。GovTechは9月の記事で、詐欺が始まることの多いSNS広告や暗号化されたメッセージアプリに向けて「端末の側で守る」方法を探っていると紹介していました。今回のAIはその答えの1つです。

## 論点

端末の中だけで動くAIは、会話を外に送らない点でプライバシーとの両立がしやすい一方、小型モデルを使うため、クラウドの大きなAIより判断の質が落ちる可能性があります。2段階の判定は、電池と精度の折り合いをつける工夫ですが、実際にどの程度見逃し、どの程度誤報を出すかは数字が出ていません。

もう1つは、私的なチャットをAIが読むこと自体への抵抗感です。DeepMindは同意と規約の範囲に限るとしていますが、どのアプリで、どんな画面で同意を求めるかは今後の発表を待つ必要があります。

AIが作った画像や文章を見分ける話題では、Googleは電子透かしの判定ツールも広げています（[関連記事](/news/20261008-google-synthid-detector-global/)）。今回は「誰が作ったか」ではなく「会話の流れが詐欺か」を見る点が違います。

## 日本のビジネスへの影響

- **使えるか**: 現時点で対象はシンガポールで、日本での提供は発表されていません。日本語の詐欺の会話で学習させたモデルもありません。
- **誰にどう効くか**: 銀行・証券・クレジットカード会社の不正対策の担当者と、メッセージアプリやECを運営する企業の担当者に関係します。日本でもSNSやチャットから始まる投資詐欺・なりすまし詐欺は多く、「会話を外に出さずに、端末の中で警告する」という作り方は、利用者の信頼を保ったまま対策を入れる方法として参考になります。
- **今すぐやれること**: 自社アプリや顧客サポートで集めている詐欺の通報内容を、個人情報を除いた形で整理しておくと、同じような地域向けの判定AIを作るときの材料になります。小型モデルを自社の端末やサーバーで動かす選択肢は[ローカルLLMのガイド](/best/local-llm/)にまとめています。
- **注意点**: 精度の数字がまだ公表されていないため、「AIが警告しなければ安全」と受け止められない設計が必要です。私的な会話を読む機能は、同意の取り方を誤ると反発を招きます。
