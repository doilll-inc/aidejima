---
{
  "title": "FLUX 3 Imageは枠で配置を指定できる画像モデル、Black Forest Labsが公開",
  "description": "独Black Forest LabsがFLUX 3 Imageを公開した。画面上の枠ごとに描く物を指定でき、編集では触れていない部分を変えない。料金は1K画像1枚$0.048で、10月8日までは半額と報じられている。",
  "date": "2026-10-02T23:40:00+09:00",
  "category": "models",
  "tags": ["Black Forest Labs", "FLUX 3 Image", "画像生成", "画像編集", "広告クリエイティブ", "API"],
  "summary": [
    "Black Forest Labsは現地時間10月1日、画像の生成と編集を担う新モデルFLUX 3 Imageを公開した",
    "FLUX 3 Imageは画面を枠で区切って要素ごとに配置でき、参照画像は最大10枚、出力は最大4K",
    "FLUX 3 ImageのAPI料金は1K画像1枚$0.048、4Kは$0.607で、公式料金ページでは期間限定の半額を表示している"
  ],
  "sources": [
    {"title": "FLUX 3 Image: Maximum control over every pixel", "publisher": "Black Forest Labs", "url": "https://bfl.ai/models/flux-3-image", "kind": "公式サイト"},
    {"title": "Pricing", "publisher": "Black Forest Labs", "url": "https://bfl.ai/pricing", "kind": "公式サイト"},
    {"title": "Release Notes", "publisher": "Black Forest Labs Documentation", "url": "https://docs.bfl.ai/release-notes", "kind": "公式ドキュメント"},
    {"title": "Pricing（API）", "publisher": "Black Forest Labs Documentation", "url": "https://docs.bfl.ai/quick_start/pricing", "kind": "公式ドキュメント"},
    {"title": "Black Forest Labs の投稿（FLUX 3 Imageの発表）", "publisher": "X @bfl_ai", "url": "https://x.com/bfl_ai/status/2105734605621825738"},
    {"title": "OpenRouter の投稿", "publisher": "X @OpenRouter", "url": "https://x.com/OpenRouter/status/2105759062835220852"},
    {"title": "FLUX 3 Image", "publisher": "Replicate", "url": "https://replicate.com/black-forest-labs/flux-3-image", "kind": "公式サイト"},
    {"title": "Black Forest Labs launches Flux 3 Image with multi-step editing that leaves the rest of your picture alone", "publisher": "The Decoder", "url": "https://the-decoder.com/black-forest-labs-launches-flux-3-image-with-multi-step-editing-that-leaves-the-rest-of-your-picture-alone/", "kind": "報道"}
  ],
  "thumb_text": "FLUX 3 Image",
  "share_text": "FLUX 3 Imageは枠ごとに描く物を指定できる画像モデル。1K画像1枚$0.048、編集では他の部分を変えない",
  "thumb_style": "3d",
  "thumb_prompt": "A blank canvas on an easel divided by glowing rectangles, with a painted apple appearing exactly inside one rectangle and a painted cat inside another.",
  "editor_note": ""
}
---
ドイツの画像生成AI企業Black Forest Labs（BFL）は現地時間10月1日、画像の生成と編集を担う新モデル「FLUX 3 Image」を公開しました。画面を枠（バウンディングボックス）で区切り、「ここに見出しの文字」「ここに人物」と要素ごとに置き場所を指定して生成できるのが最大の特徴です。APIの料金は1K（約100万画素）の画像1枚で$0.048です。

## 何が発表されたか

FLUX 3 Imageとは、BFLが7月に発表した動画・音声・画像・ロボット動作をまとめて扱うFLUX 3のうち、画像の生成と編集を受け持つモデルです。公式ページが挙げる機能は4つあります。

- **枠による配置**: 縦横とも0〜1000の座標で枠を描き、枠ごとに中身を文章で書く。最後に場面全体を1行で説明すると、各要素がそれぞれの枠の中に描かれる
- **部分だけの編集**: 枠ごとに描き直し・差し替え・移動ができ、触れていない部分はそのまま残る。複数の箇所を一度に直せる
- **参照画像の合成**: 最大10枚の参照画像を渡すと、どこにどの大きさで置くかをモデルが決めて1枚にまとめる
- **高解像度の出力**: 2Kと4Kをそのまま生成でき、4Kは5456×3072ピクセル

枠を自分で描く必要はありません。1行の指示と縦横比だけを渡せば、LLMが要素の一覧と枠の配置を下書きし、気に入らない枠だけ動かせます。BFLはこの仕組みを、エージェントが画像を作る用途にも向くと説明しています。

:::quote https://bfl.ai/models/flux-3-image | Black Forest Labs公式「FLUX 3 Image: Maximum control over every pixel」
> Each box can be re-described, replaced with something else or moved. Everything you didn't touch stays exactly where it was, so an image holds together across one round of edits after another.
枠はそれぞれ説明を書き直したり、別の物に差し替えたり、動かしたりできます。触れていない部分はすべてそのままの位置に残るので、何度編集を重ねても画像が崩れません。
:::

BFLは、枠での指定が向く画像として、写真の周りに文字を組むレイアウト、コラージュやコマ割り、雑誌の見開き、人の顔が多い群衆の場面を挙げています。

### 料金と提供先

公式のAPIドキュメントによると、料金は解像度で決まる1枚単位です。

| 解像度 | 1枚の料金 |
|---|---|
| 768×768 | $0.041 |
| 1K（約100万画素） | $0.048 |
| 2K（約400万画素） | $0.100 |
| 4K（約1600万画素） | $0.607 |

BFLの料金ページでは1Kが$0.024と半額で表示されています。The Decoderは、この割引が10月8日まで続くと報じています。

{{card:https://bfl.ai/pricing|Pricing|Black Forest Labs}}

BFLのAPIとPlaygroundのほか、OpenRouterやReplicateでも公開当日から使えるようになりました。自社サーバーで動かしたい企業向けには、重みを有償でライセンスし、追加学習して運用する契約も用意しています。誰でも使える重みの公開は「数週間以内」の予定だとThe Decoderは報じています。

## 背景

画像生成AIの競争の軸は、「きれいな1枚を出す」から「狙ったとおりに直せる」へ移っています。前日の9月30日には、Ideogramが編集を重ねても劣化しにくいIdeogram 4.5を公開したばかりです（[Ideogram 4.5の記事](/news/20261002-ideogram-4-5-precise-edit/)）。広告やECの現場では、商品の色だけ変える、背景だけ季節に合わせるといった差し替えが作業の大半を占めます。2社とも、この「直し」の工程を取りにきています。

BFLの前世代FLUX.2は、サブスクなしの従量課金で、自社ツールに組み込みやすいAPIとして使われてきました。FLUX 3 Imageの1K画像$0.048は、FLUX.2 [pro]の$0.03からより高い価格帯に入ったことになります。

## 反応と論点

BFLはXで、ほかの画素を変えずに何度も編集できることと、枠での配置、4K出力、10枚の参照を発表の柱に挙げました。

{{x:https://x.com/bfl_ai/status/2105734605621825738}}

モデルを取り次ぐOpenRouterはすぐに提供開始を告知しました。開発者がすぐ試せる環境は初日から揃っています。

{{x:https://x.com/OpenRouter/status/2105759062835220852}}

一方で、公式ページには他社モデルとの比較表や、第三者による評価がまだ載っていません。画像内の日本語の文字をどこまで正しく描けるかも書かれていません。枠で配置を決められても、肝心の画質や文字の描写が他社並みかどうかは、公開ランキングに順位が出てから判断する必要があります。

## 日本のビジネスへの影響

- **使えるか**: BFLのAPIのほか、OpenRouterやReplicateからも使えます。日本からの提供を制限する記載はありませんが、提供国の一覧も公式には見つけられませんでした。料金はドル建てで、1K画像1枚$0.048です
- **誰にどう効くか**: バナーやLPの画像を量産する**広告運用者・デザイナー**に効きます。「左上にロゴの余白、中央に商品、右下にコピー」という決まった型を枠で固定し、中身だけ差し替えて何十パターンも作る使い方がしやすくなります。画像生成を自社サービスに組み込む**開発者**は、LLMに配置を任せてから生成する流れを作れます
- **今すぐやれること**: 割引期間のうちに、いま使っている画像モデルと同じ指示で、自社のバナーの型を再現できるか試します。とくに日本語のコピーを画像内に入れる場合の崩れ方を確認します
- **注意点**: BFLの利用規約では、既定で入力と出力が学習に使われます（メールで拒否を申し出られます）。社外秘の商品画像を参照に使う前に確認が必要です。割引が終わると単価は倍になるので、試算は通常料金で行います

画像生成AIの選び方と料金の比較は、[画像生成AIのガイド](/best/image-generation/)にまとめています。
