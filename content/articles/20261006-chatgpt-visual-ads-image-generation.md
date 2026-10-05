---
{
  "title": "ChatGPTで画像を作る待ち時間に商品の写真広告、OpenAIが米国で10月中に試験開始",
  "description": "OpenAIがChatGPTに写真で商品を見せる新しい広告を加え、まず画像を生成している間に米国で試験すると発表した。週12億人が使うChatGPTの広告事業で、効果測定などの提携先も20社以上に広げた。",
  "date": "2026-10-06T02:10:00+09:00",
  "category": "marketing",
  "tags": ["OpenAI", "ChatGPT", "広告", "マーケティング", "画像生成"],
  "summary": [
    "OpenAIはChatGPTに商品写真を見せる新しい広告を加え、10月中に米国で一部の広告主と試験を始める",
    "最初の表示場所は、ChatGPTで画像を作っている間。広告は表示を明記し、生成中の画像とは分けて出す",
    "広告の効果を測る外部の提携先も広げ、WeightWatchersは検索広告より獲得単価が15.3%低かったという"
  ],
  "sources": [
    {"title": "Building advertising for the way people use AI", "publisher": "OpenAI", "url": "https://openai.com/index/new-chatgpt-ads-format-and-measurement/", "kind": "公式発表"},
    {"title": "More ways to measure ChatGPT Ads", "publisher": "OpenAI Ads", "url": "https://ads.openai.com/blog/more-ways-to-measure", "kind": "公式発表"},
    {"title": "Ads Manager Availability", "publisher": "OpenAI Help Center", "url": "https://help.openai.com/en/articles/20001245-ads-manager-availability", "kind": "公式ドキュメント"},
    {"title": "OpenAI launches visual ads that appear alongside image generation results", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/10/05/openai-launches-visual-ads-that-appear-alongside-image-generation-results/", "kind": "報道"},
    {"title": "ChatGPT's new ad format fills the image generation loading screen with product carousels", "publisher": "The Decoder", "url": "https://the-decoder.com/chatgpts-new-ad-format-fills-the-image-generation-loading-screen-with-product-carousels/", "kind": "報道"},
    {"title": "OpenAI to flood your eyeballs with visual ads", "publisher": "The Register", "url": "https://www.theregister.com/ai-and-ml/2026/10/05/openai-to-flood-your-eyeballs-with-visual-ads/5301152", "kind": "報道"}
  ],
  "thumb_prompt": "A laptop screen showing a half-painted picture slowly appearing, while a row of glossy product photos (sneakers, a coffee mug, a sofa) slides in beneath it like a shop window carousel.",
  "thumb_style": "3d",
  "thumb_text": "ChatGPT広告",
  "share_text": "ChatGPTで画像を作る待ち時間に商品写真の広告。OpenAIが米国で10月中に試験開始",
  "editor_note": ""
}
---
OpenAIは現地時間10月5日、ChatGPTに商品やサービスを写真で見せる新しい広告の形式を加えると発表しました。最初は利用者がChatGPTで画像を生成している間に表示し、10月中に米国で一部の広告主と試験を始めます。あわせて、広告の効果を測るための外部企業との連携を大きく広げました。

## 何が発表されたか

ChatGPTの広告は2月に始まり、これまでは文字中心の形式でした。今回の新形式は、商品の使用場面や、その商品で得られる体験を画像で見せるものです。OpenAIは公式ブログで、表示場所と扱いを次のように説明しています。

:::quote https://openai.com/index/new-chatgpt-ads-format-and-measurement/ | OpenAI公式ブログ「Building advertising for the way people use AI」
> Initially, we’ll test this new ad format during image generation in ChatGPT. Ads will be clearly labeled, and remain separate from the image being created.
まずはChatGPTでの画像生成中にこの新しい広告形式を試験します。広告は広告だとはっきり表示し、作成中の画像とは切り離します。
:::

The Decoderは、広告は生成中の画像の下に、横に流れるカルーセル（複数の商品画像を順に見せる枠）か商品画像の列として出ると報じています。OpenAIは、広告がChatGPTの回答内容に影響しないという従来の方針も、この形式に当てはまるとしています。

## 広告主向けには「効いたか」を測る道具を拡充

発表のもう半分は、効果測定です。広告主がまず知りたい「出して効いたのか」について、OpenAIは外部の計測会社が出した初期の数字を並べました。

| 広告主 | 測定した会社 | 公表された結果 |
|---|---|---|
| WeightWatchers | DV Rockerbox | 獲得単価が検索広告全体の基準より15.3%低い |
| Dose（健康関連ブランド） | WorkMagic | 上積みとなった購入の67%が新規客 |
| Portland Leather | Triple Whale | ChatGPT広告から来た訪問者の93%が新規 |

OpenAIの広告ブログには、広告を見てクリックせずに1日以内に成果につながったケースのうち52.7%が、表示から1時間以内だったという初期分析も載っています。

こうした数字を各社が自分で確かめられるよう、道具も増えました。

- **データを送る**: 自社のサイトやアプリでの購入・申し込みなどのデータを、Hightouch、Tealium、LiveRampを通じてChatGPT広告へ送れる
- **成果を集計する**: どの広告が成果につながったかを数える計測会社として、AppsFlyer、Adjust、Branch、Northbeamなど10社に対応
- **本当の上積みを測る**: 地域ごとに広告を出し分けて比べ、広告がなくても買った人を除いた効果を測る実験を、Haus、Measured、WorkMagicと始める
- **出す場所を選ぶ**: DoubleVerifyとIntegral Ad Scienceが、実際の会話を見ない試験環境で表示先の安全基準を評価する。条件を満たす広告主は、自社の方針に合わない話題を避ける除外語句（Negative Phrases）も設定できる

{{card:https://ads.openai.com/blog/more-ways-to-measure|More ways to measure ChatGPT Ads|OpenAI Ads}}

## 背景：週12億人の無料利用者をどう収益化するか

OpenAIはChatGPTの週間利用者を12億人としています。広告について同社は、サブスクリプションだけよりはるかに大きな市場に届けられる手段だと位置づけています。

:::quote https://openai.com/index/new-chatgpt-ads-format-and-measurement/ | OpenAI公式ブログ「Building advertising for the way people use AI」
> It allows us to serve a much larger market than subscriptions alone, while giving businesses a new way to reach people as they explore ideas, make decisions and discover products and services relevant to what they’re trying to accomplish.
広告によって、サブスクリプションだけよりはるかに大きな市場に届けられます。同時に企業には、アイデアを探し、判断し、目的に合う商品やサービスを見つけようとしている人に届く新しい手段を提供します。
:::

The Decoderは、ChatGPTの広告はすでに40カ国以上で配信され、広告だけで年換算10億ドルの売上規模に達したと報じています。TechCrunchは、無料で使えるMetaのAIアプリ「Muse」が競合として伸びているなかでの発表だと指摘しています。

## 反応と論点

肯定的に見れば、画像生成は「部屋のインテリア案」「服のコーディネート」など、買い物の直前の行動と結びつきやすい場面です。10月2日にはChatGPTに服の試着機能も加わっており（[関連記事](/news/20261002-chatgpt-virtual-try-on-favorites/)）、画像と買い物を近づける流れが続いています。

一方で懸念もあります。TechCrunchは、広告が使い勝手を損なうおそれがあり、むしろ広告を避けたい利用者を有料プランへ誘う狙いもありうると書いています。英The Registerも、利用者の目に広告があふれるという皮肉を込めた見出しで、米国での試験開始を冷ややかに伝えました。生成中の画像の真下に商品が並ぶため、利用者が「AIが勧めた商品」と受け取らないかどうかも、表示の仕方しだいです。

## 日本のビジネスへの影響

- **使えるか**: 今回の画像広告は、米国での限られた広告主との試験です。日本の利用者に表示する時期は発表されていません。ただしOpenAIのヘルプページでは、広告主が自分で出稿できるAds Managerの対象国に日本が入っており、日本企業も既存のChatGPT広告は試せます。
- **誰にどう効くか**: EC・D2Cのマーケターと広告運用者に関係が深い話です。家具、アパレル、旅行など「使っている場面の写真」で売る商材は、画像を作っている利用者に見せる枠と相性がよいはずです。
- **今すぐやれること**: すでにChatGPT広告を出している企業は、購入データを送る計測タグ（ピクセルやConversions API）を整え、検索広告と獲得単価を比べられる状態にしておくのが先です。画像広告が日本に来たときに、使用場面の写真素材をすぐ出せるよう棚卸ししておくとよいでしょう。
- **注意点**: 公表された成果は提携先による一部広告主の数字で、どの業種でも同じとは限りません。画像の真横に出る広告は、自社の商品と無関係な生成画像（不適切な内容を含むもの）の近くに並ぶ可能性もあるため、除外語句やブランド安全の評価が日本で使えるかも確認が必要です。

広告やクリエイティブ制作に使えるAIツールの比較は、[広告・マーケティング向けAIのガイド](/best/marketing/)にまとめています。
