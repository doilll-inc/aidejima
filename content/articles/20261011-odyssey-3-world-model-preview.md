---
{
  "title": "文章で書いた世界をその場で歩き回れるAI、米Odysseyが「Odyssey-3」を試用公開 ロボットも動かす",
  "description": "米新興Odysseyが、文章から動く3D風の世界を作り、操作に合わせてその場で変化させるAI「Odyssey-3」を試用公開した。20時間分の運転データでインドの公道を走る車を動かすなど、ロボットや車の制御にも使えるとしています。",
  "date": "2026-10-11T23:58:00+09:00",
  "category": "products",
  "tags": ["Odyssey", "Odyssey-3", "ワールドモデル", "ロボット", "ゲーム"],
  "summary": [
    "米新興Odysseyが、文章の指示から動く世界を作り、利用者の操作に合わせてその場で変化させるAIを試用公開した",
    "自分視点・後ろからの視点で中を歩き回れ、途中で出来事を起こすとAIが続きの映像を予測して描く",
    "同じAIでロボットの腕や人型ロボット、車も動かしたとしており、20時間分の運転データでインドの公道を走らせた"
  ],
  "sources": [
    {"title": "Meet Odyssey-3: Our Most Powerful Foundation World Model", "publisher": "Odyssey", "url": "https://odyssey.systems/meet-odyssey-3", "kind": "公式発表"},
    {"title": "Introducing Odyssey-3", "publisher": "Odyssey", "url": "https://odyssey.systems/introducing-odyssey-3", "kind": "公式発表"},
    {"title": "Odyssey-3 is a new generative world model that you can try for free", "publisher": "The Decoder", "url": "https://the-decoder.com/odyssey-3-is-a-new-generative-world-model-that-you-can-try-for-free/", "kind": "報道"},
    {"title": "Odyssey-3 drives a car in India and runs humanoids from one world model", "publisher": "The Next Web", "url": "https://thenextweb.com/news/odyssey-3-world-model-robots-humanoids-cars-drones", "kind": "報道"}
  ],
  "thumb_prompt": "A person seen from behind sitting at a desk, typing on a keyboard, while a misty forest path with a small wooden bridge grows out of the computer monitor and spills across the desk onto the floor.",
  "thumb_style": "illustration",
  "thumb_text": "Odyssey-3",
  "share_text": "文章で書いた世界にその場で入って歩き回れるAI「Odyssey-3」が試用公開。同じAIでロボットや車も動かす",
  "editor_note": ""
}
---
米カリフォルニア州の新興企業Odysseyは現地時間10月8日、文章で指示した場面から動く世界を作り、利用者の操作に合わせてその場で変化させるAI「Odyssey-3」を、研究用の試用版として公開しました。同じAIを土台に、ロボットの腕や人型ロボット、車まで動かしたとしています。車は20時間分の運転データだけで、インドの公道を走らせたといいます。

## 何が発表されたか

Odyssey-3は、いわゆる「ワールドモデル」です。ワールドモデルとは、映像から世の中の動き方を学び、「この状態でこう動いたら次にどうなるか」を予測して描くAIのことです。動画を作るAIと似ていますが、利用者の操作を受けて続きをその場で作り続ける点が違います。

公開された試用版では、自分の目線（一人称）か、後ろから見る視点（三人称）を選んで、生成された世界の中を歩き回れます。カメラの向きを別に動かしたり、途中で出来事を起こしたりすると、AIがそれに応じた続きの映像を描きます。

:::quote https://odyssey.systems/meet-odyssey-3 | Odyssey「Meet Odyssey-3: Our Most Powerful Foundation World Model」
> You can move through the environment or introduce an event during generation and observe how the model responds.
生成の途中で世界の中を移動したり、出来事を起こしたりして、モデルがどう反応するかを観察できる。
:::

試せるのは軽量版の「Odyssey-3 Flash」です。The Decoderは、このデモを無料で試せると報じています。画面の解像度は標準版が832×480、上位版の「Odyssey-3 Pro」がハイビジョン相当の1280×720です。料金や一般向けの提供条件は、公式ページには書かれていません。開発者には個別の問い合わせを呼びかけています。

{{card:https://odyssey.systems/meet-odyssey-3|Meet Odyssey-3: Our Most Powerful Foundation World Model|Odyssey}}

## ゲームの世界から、現実のロボットや車へ

Odysseyが強調するのは、映像を作るだけでなく「機械を動かす頭脳の土台」になる点です。公式ページでは、次のような例を挙げています。

| 対象 | Odysseyが公表した内容 |
|---|---|
| ロボットの腕 | 数十時間分の実演データで物をつかむ作業をこなし、つかみ損ねた後に持ち直すなど、教えていない動きも見せた |
| 人型ロボット | スイスのFlexionがOdyssey-3を使って制御を作り、照明が変わっても作業を続けられた |
| 車 | 20時間分の運転データで学ばせ、インドの公道で走行した |
| ゲーム | 人気ゲーム「GTA V」の映像で学んだAIが車を運転し、学習していない別のゲームでも動けた |

## 背景

ワールドモデルは、文章や画像を扱う今の対話AIの「次」として、大手も力を入れる分野です。Google DeepMindが「Genie」を開発しているほか、9月末には米AMDが同じ分野の新興企業World Labsの買収を発表しました（[AMDのWorld Labs買収の記事](/news/20260930-amd-acquires-world-labs/)）。

Odysseyは自動運転の開発経験者らが立ち上げた会社で、6月にAmazonやAMDの投資部門などから3億1,000万ドルを調達しています。The Next Webは、このときの企業価値を14億5,000万ドルと報じています。

## 反応と論点

性能の数字は、ほとんどが会社自身の発表です。Odysseyは、物理法則に沿った映像を作れるかを測る公開の試験「Physics-IQ Verified」で上位版が66.1点の最高記録を出したとしています。ただThe Decoderは、この点数が8回作った映像から1つを選ぶやり方で出したもので、試験のルールが求める4回の平均（63.37点）とは違うと指摘しています。

The Next Webも、ロボットや車の成果は会社が公開したデモで、成功率などの第三者による検証はまだないと伝えています。運転についても、公式の2つのページで「実際の運転データ」と「シミュレーションの運転データ」と書き方が分かれており、条件の詳細ははっきりしません。

## 日本のビジネスへの影響

- **使えるか**: 試用版は公式サイトから開けます。日本からの利用制限は書かれていませんが、操作画面は英語です。研究用の試用版なので、仕事で使う前提の料金や利用規約はまだ示されていません
- **誰にどう効くか**: ゲームや映像、広告の企画担当者にとっては、「文章で書いた舞台の中を歩いて見る」試作が数分でできる道具になりえます。製造業や物流でロボット導入を検討する担当者には、大量の実演データを集めなくてもロボットを教えられる方向に技術が進んでいることを示す例です
- **今すぐやれること**: 自社の売り場や展示会のブースを文章で描写し、試用版の中を歩いてみると、ワールドモデルで何ができて何がまだ粗いかを体感できます。動画生成AIとの違いを知るには[動画生成AIのガイド](/best/video-generation/)と見比べるとわかりやすいです
- **注意点**: 性能の数字は会社の自己申告が中心で、ロボットや車の制御は研究段階のデモです。試用版に入力した文章や生成物の扱いも確認できていないため、社外秘の情報は入れないでください
