---
{
  "title": "乳がんの超音波検査が45分から2分に、米国の新興企業4社がAIで検診から治療方針まで支援",
  "description": "NVIDIAが乳がん月間に合わせ、AIで乳がんの検診・診断・治療方針づくりを支える米スタートアップ4社の事例を公開した。着けるだけの自動超音波は片胸約2分で、手持ちの検査の最大45分から大きく縮むという。",
  "date": "2026-10-06T02:30:00+09:00",
  "category": "usecases",
  "tags": ["NVIDIA", "iSono Health", "活用事例", "導入事例", "医療"],
  "summary": [
    "NVIDIAは、AIで乳がんの検診から治療方針の判断までを支える米国のスタートアップ4社の取り組みを紹介した",
    "iSono Healthの着ける自動超音波は片胸約2分で撮影でき、手持ちの検査の最大45分から大幅に短くなるという",
    "病理の画像から抗がん剤の効きや再発リスクを予測するAIは、10以上の医療機関で検証され、診療で使われている"
  ],
  "sources": [
    {"title": "From Scan to Treatment Plan, AI Helps Close Breast Cancer’s Deadliest Gaps", "publisher": "NVIDIA Blog", "url": "https://blogs.nvidia.com/blog/ai-breast-cancer-startups/", "kind": "公式発表"},
    {"title": "iSono Health – Say Hello to ATUSA", "publisher": "iSono Health", "url": "https://www.isonohealth.com/", "kind": "公式サイト"},
    {"title": "Whiterabbit.ai", "publisher": "Whiterabbit.ai", "url": "https://www.whiterabbit.ai/", "kind": "公式サイト"},
    {"title": "Ataraxis AI | Homepage", "publisher": "Ataraxis AI", "url": "https://www.ataraxis.ai/", "kind": "公式サイト"}
  ],
  "thumb_prompt": "A soft wearable cup-shaped ultrasound device resting on a clinic tray next to a small hourglass, with a tablet beside it displaying a glowing 3D scan of tissue.",
  "thumb_style": "illustration",
  "thumb_text": "乳がん×AI",
  "share_text": "乳がんの超音波が45分から2分に。米国の新興企業4社がAIで検診から治療方針まで支援",
  "editor_note": ""
}
---
NVIDIAは現地時間10月5日、同社の新興企業支援プログラム「NVIDIA Inception」に参加する米国のスタートアップ4社が、AIで乳がんの検診・診断・治療方針づくりを支えている事例を公式ブログで紹介しました。着けるだけで撮れる自動の超音波装置は片側の胸を約2分で撮影でき、技師が手で当てる従来の検査（最大45分）から大幅に短くなるといいます。10月は乳がんの啓発月間（ピンクリボン月間）です。

## 何を作ったか：検診から治療まで4つの穴を埋める

NVIDIAは、乳がん診療には「検診を受けない人が多い」「画像を読む放射線科医が足りない」「治療方針を決める検査に何週間もかかる」という穴があると整理しています。4社はそれぞれ別の段階を受け持ちます。

| 会社 | 担う段階 | 何をするか |
|---|---|---|
| iSono Health | 撮影 | 胸に着ける自動の3D超音波装置「ATUSA」。AIが撮影を自動化し、技師がいなくても毎回同じ条件で撮れる |
| Whiterabbit.ai | 検診 | マンモグラフィ（乳房のX線撮影）から乳腺の密度を自動判定するソフトと、将来の発症リスクを見積もるソフト |
| Ataraxis AI | 治療方針 | 診断で必ず作る病理標本の画像から、抗がん剤が効くか、5年以内の再発リスクがどの程度かを予測 |
| SimBioSys | 手術計画 | MRI画像などから腫瘍や血管の立体モデルを作り、手術や治療の計画を助ける |

Whiterabbit.aiの共同創業者は、放射線科医の仕事を「干し草の山から針を探す」作業にたとえています。

:::quote https://blogs.nvidia.com/blog/ai-breast-cancer-startups/ | NVIDIA公式ブログ「From Scan to Treatment Plan, AI Helps Close Breast Cancer’s Deadliest Gaps」
> “Every day, breast radiologists face a needle-in-a-haystack problem, trying to find roughly one cancer in every 200 mammograms,” said Jason Su, cofounder and chief technology officer of Whiterabbit.ai.
「乳腺専門の放射線科医は毎日、マンモグラフィ約200枚に1件ほどのがんを探す、干し草の山から針を探すような仕事に向き合っています」とWhiterabbit.aiの共同創業者で最高技術責任者のジェイソン・スー氏は話しています。
:::

同社は、がんがない画像の確認をAIで自動化し、医師が疑わしい画像に集中できるようにする次世代のAIを研究しています。

## どう作ったか：既存の検査データをAIに読ませる

4社に共通するのは、新しい検査を増やすのではなく、すでに病院にある画像やデータをAIに読ませている点です。

- **iSono Health**: 数千人分の全乳房スキャン、計150万枚以上の超音波画像でAIを学習。同社によると、立体で撮る検査は手持ちの2D超音波より感度が28%高い
- **Whiterabbit.ai**: ワシントン大学（セントルイス）に置いたGPU（AIの計算に使う半導体）の計算機群とクラウドで学習し、判定はクリニックに置いたGPUで動かす
- **Ataraxis AI**: 病理標本のデジタル画像と、標準的な診療情報を組み合わせて予測。手術前の抗がん剤で腫瘍が縮むかを予測するモデルと、手術後の再発リスクと抗がん剤の上乗せ効果を見積もるモデルがある
- **SimBioSys**: NVIDIAの医用画像向けオープンソース基盤「MONAI」で学習データを整え、クラウドで処理

Ataraxis AIの技術担当者はNVIDIAのブログで、腫瘍内科医がいま頼っている判断材料は「15年前に一度学習したきり更新されていない」とし、臨床試験のデータが増えるほど自社のモデルは強くなると説明しています。

## 成果：公表されている数字

- iSono HealthのATUSAは米食品医薬品局（FDA）の認可を取得し、カリフォルニア、テキサス、ジョージア、テネシー、ワシントンD.C.の提携クリニックで使われている。カリフォルニア大学デービス校などで3,200人規模の臨床研究も進めている
- Whiterabbit.aiの乳腺密度ソフトもFDAの認可を取得し、NVIDIAによると数十万人の診療に使われた。同社サイトでは、製品群全体で200万人以上に提供したとしている
- Ataraxis AIの2つのモデルは10以上の医療機関と複数の臨床試験で検証され、すでに診療で使われている。同社サイトでは、遺伝子検査が数週間かかるのに対し、データを受け取ってから24時間以内に結果を返すとしている

なおNVIDIAは記事の末尾で、紹介した技術の一部は研究段階で、FDAの商用認可を得ていないと注記しています。

{{card:https://www.isonohealth.com/|iSono Health – Say Hello to ATUSA|iSono Health}}

## 日本のビジネスへの影響

- **使えるか**: 4社の製品は米国での提供で、日本で使えるという発表はありません。医療機器としてのAIは、日本では医薬品医療機器等法に基づく承認が別に必要です。
- **誰にどう効くか**: 医療機関の経営者や、医療・ヘルスケア領域の事業企画の担当者に参考になります。人手不足の現場で「AIに全部を任せる」のではなく「異常のない画像の確認」や「撮影の標準化」など、専門家の手間が大きい一部分をAIに渡すという切り分け方は、医療以外の検査・点検業務にも応用できる考え方です。
- **今すぐやれること**: 自社の業務で、熟練者が大量の画像や書類から「まれな異常」を探している工程を洗い出してみるとよいでしょう。製造業の外観検査や保険の審査書類など、構図が似た業務は多くあります。
- **注意点**: 公表された数字（感度28%向上など）の多くは各社が自ら示したもので、第三者の比較ではありません。医療AIは、学習に使った患者層と自分たちの対象が違うと精度が変わりうるため、導入時は自分たちのデータで確かめる必要があります。
