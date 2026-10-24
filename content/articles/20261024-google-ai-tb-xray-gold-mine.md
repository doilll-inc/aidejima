---
{
  "title": "地下4kmの金鉱で結核の疑いをAIが45秒で判定、Googleの技術を使い6か国40施設に",
  "description": "Googleの胸部X線を読むAIを使い、南アフリカの新興企業が結核の検診を6か国約40施設で実施している。医師90人以上が2万5,000枚超を確認し、結果が出るまで数週間かかっていた待ちを45秒未満に縮めた。",
  "date": "2026-10-24T18:20:00+09:00",
  "category": "usecases",
  "tags": ["Google", "Nexus AI", "MedGemma", "医療", "活用事例", "導入事例"],
  "summary": [
    "GoogleのX線画像を読むAIを元に、南アフリカのNexus AIが結核の検診ツールを作り6か国約40施設で使っている",
    "医師90人以上が2万5,000枚超のX線を確認し、数週間かかった結果待ちが45秒未満になった",
    "深さ4kmの金鉱の中でもネットなしで検診でき、インドネシアは年5,000万人の検診にGoogleの無料AIを使う"
  ],
  "sources": [
    {"title": "Bringing foundational models to the front lines of TB screening", "publisher": "Google Research", "url": "https://research.google/blog/bringing-foundational-models-to-the-front-lines-of-tb-screening/", "kind": "公式発表"},
    {"title": "Meet the Pretoria team using AI to spot lung disease in as little as 45 seconds", "publisher": "Google Africa Blog", "url": "https://blog.google/intl/en-africa/company-news/outreach-and-initiatives/meet-the-pretoria-team-using-ai-to-spot-lung-disease-in-as-little-as-45-seconds/", "kind": "公式発表"},
    {"title": "Pretoria start-up uses AI to detect lung disease in miners", "publisher": "Tech Africa", "url": "https://tech.africa/nexus-ai-lung-disease-screening/", "kind": "報道"}
  ],
  "thumb_prompt": "A compact portable X-ray machine set up on a rough rock floor deep inside a dimly lit mine tunnel, a miner's helmet lamp beam falling on a glowing tablet showing a chest X-ray.",
  "thumb_style": "photo",
  "thumb_text": "結核検診AI",
  "share_text": "地下4kmの金鉱でもネットなしで結核の疑いをAIが45秒で判定。Googleの技術で6か国約40施設、2万5,000枚超を確認",
  "editor_note": ""
}
---
Google Researchは現地時間10月23日、胸部X線の画像から結核の疑いを見つけるAIが、アフリカなど6か国の約40の医療施設で使われていると公表しました。南アフリカの新興企業Nexus AIがGoogleのAIを元に医療機器として仕上げたもので、医師90人以上が2万5,000枚を超える画像を確認し、数週間かかっていた結果待ちを45秒未満に縮めています。

## 何に使ったか

結核は治る病気ですが、Googleによると毎年123万人以上が亡くなっています。早く見つけるにはX線の画像を読む放射線科の医師が要りますが、農村や鉱山ではその医師がいません。画像を撮っても、結果が分かるまで数日から数週間待つことになり、その間に感染が広がります。

そこで、X線を撮ったその場でAIが画像を読み、「結核が疑われる」「追加の検査が必要」といった所見に印を付けて医師に渡します。最終的な判断は医師がします。

最も厳しい現場は、南アフリカのムポネン金鉱です。世界有数の深さの鉱山で、粉じんを吸い続ける鉱員は肺の病気になりやすい環境にあります。Nexus AIは持ち運べるX線撮影機と、ネットなしで動くAIを地下4kmまで持ち込みました。

:::quote https://research.google/blog/bringing-foundational-models-to-the-front-lines-of-tb-screening/ | Google Research公式ブログ「Bringing foundational models to the front lines of TB screening」
> Screening, triage and confirmatory testing can now happen in a single visit, compressing a pathway that often takes weeks.
検診、優先度の振り分け、確定のための検査が、いまでは1回の受診で済むようになりました。これまで数週間かかることが多かった流れが短くなっています。
:::

AIが結核を疑った鉱員は、その場で確定診断のための検査に回されます。

## どう作ったか

始まりはGoogleの研究です。同社は2019年に、X線から結核を見つけるAIが経験のある放射線科医と同じ水準で読めることを論文で示し、2021年には国際組織Stop TB Partnershipの比較評価で上位に入りました。

ただ、論文の成果をそのまま病院で使うことはできません。撮影機が施設ごとに違う、ネットがない、医療機器としての認証が要る、といった壁があります。ここを埋めたのが、南アフリカの行政首都プレトリアの新興企業Nexus Intelligence（製品名Nexus AI）です。

Googleのアフリカ向けブログによると、同社は医師と臨床工学技士が2022年に立ち上げました。Googleからライセンスを受けたAIを元に、2つのAIを同時に動かす仕組みにしています。1つは肺が正常かどうかを見て異常な場所を示し、もう1つは結核らしい所見に絞って調べます。結果は色の濃淡や輪郭線で画像に重ねて医師に見せます。

この製品は、欧州の医療機器規則で中〜高リスクの機器に当たる「クラスIIb」の認証を取りました。世界保健機関（WHO）の事前認定や、米国の食品医薬品局（FDA）の承認に向けた手続きも進めています。

## 成果

Google Researchが公表した数字は次のとおりです。

| 項目 | 数字 |
|---|---|
| 使っている国 | 南アフリカ、シエラレオネ、コートジボワール（コンゴ民主共和国、ザンビア、カメルーンに拡大中） |
| 施設数 | 約40 |
| 確認した画像 | 2万5,000枚超（医師90人以上） |
| 結果が出るまで | 数週間から45秒未満に |
| 無料の検診 | 公立の診療所で3,000件超（年1万件が目標） |

{{card:https://blog.google/intl/en-africa/company-news/outreach-and-initiatives/meet-the-pretoria-team-using-ai-to-spot-lung-disease-in-as-little-as-45-seconds/|Meet the Pretoria team using AI to spot lung disease in as little as 45 seconds|Google Africa Blog}}

## 1社の道具から、国ごとに作れる無料のAIへ

結核の患者が世界で2番目に多いインドネシアでは、保健省が年5,000万人のX線検診を目標にしています。医師が1枚ずつ読んでいては追いつかない規模で、同省はGoogleが無料で公開している医療向けのAIを、国内で撮った画像で鍛え直して使っています。

その土台のひとつが「MedGemma」です。X線の所見と患者の経過を合わせて読み、医師の質問に言葉で答えるAIで、ネットにつながない端末でも動きます。Googleによると、公開以来のダウンロードは1,000万回を超えました。Nexus AIのように1社と製品を作るだけでは届く範囲が限られるため、各国が自分で作れる材料を配る、というのが同社の方針です。

:::quote https://research.google/blog/bringing-foundational-models-to-the-front-lines-of-tb-screening/ | Google Research公式ブログ「Bringing foundational models to the front lines of TB screening」
> Open models help enable public health systems to build sovereign solutions that protect patient privacy.
公開されたモデルは、各国の公衆衛生の仕組みが、患者のプライバシーを守る自前の解決策を作る助けになります。
:::

インドネシアでもAIは国内の設備で動かすため、患者のデータは国外に出ません。

X線の機械そのものが無い地域には、別の手もあります。スマホで録ったせきの音から結核を見分ける研究で、ザンビアやガーナで進んでいます。

## 日本のビジネスへの影響

- **使えるか**: Nexus AIの製品は日本では提供されていません。一方、MedGemmaなどGoogleの医療向けAIは開発者向けに公開されており、日本からも入手できます。ただし日本で診断に使う製品にするには、国内の医療機器としての承認が別に必要です。
- **誰にどう効くか**: 医療機器メーカーや病院・健診事業者の企画担当者には、「専門医がいない場所で、AIが一次の振り分けをして医師が最終判断する」という役割分担の実例になります。製造業や建設業で安全衛生を担う人にとっても、ネットのない現場にAIを持ち込める点は参考になります。
- **今すぐやれること**: 自社の現場で「専門家が見るまで何日も待っている確認作業」を洗い出してください。画像の一次チェックをAIに任せ、人は最終判断だけをする形にできないかを検討する材料になります。手元のPCやネットにつながない端末で動くAIは、[ローカルで動かせるAIのガイド](/best/local-llm/)でまとめています。
- **注意点**: 今回の数字はGoogleと提携先の公表で、外部の第三者が検証した効果ではありません。また、AIはあくまで「疑い」を示す道具で、Nexus AIも最終判断は医師が行う設計にしています。人の確認を省く使い方はしないことです。
