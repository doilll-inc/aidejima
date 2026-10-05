---
{
  "title": "Geminiの無料版は10月9日からFlash-Liteだけに、Proは月額AI Pro以上へ",
  "description": "GoogleがGeminiアプリで使えるモデルをプランごとに絞る。無料版は10月9日から最も小さいFlash-Liteだけになり、AI PlusもProを使えなくなる。利用上限は5時間ごとに戻る計算量ベースの方式に移る。",
  "date": "2026-10-04T18:40:00+09:00",
  "category": "products",
  "tags": ["Google", "Gemini", "料金", "Deep Think"],
  "summary": [
    "Googleは、AIのプランに入っていない人のGeminiアプリを10月9日からFlash-Liteだけに切り替えると公式ヘルプで告知した",
    "月額725円のGoogle AI PlusはFlash-LiteとFlashまでになり、ProモデルはAI Pro（月額2,900円）とAI Ultraの利用者に限られる",
    "AI ProとAI UltraではDeep Thinkも選べるとGoogleは案内している。日本の料金ページは10月4日時点で旧内容のまま"
  ],
  "sources": [
    {"title": "Changes to Gemini model access and limits", "publisher": "Gemini Apps Help（Google）", "url": "https://support.google.com/gemini/answer/17004136?hl=en", "kind": "公式ドキュメント"},
    {"title": "Gemini Apps limits & upgrades for Google AI subscribers", "publisher": "Gemini Apps Help（Google）", "url": "https://support.google.com/gemini/answer/16275805?hl=en", "kind": "公式ドキュメント"},
    {"title": "Google AI プラン", "publisher": "Google（日本向け料金ページ）", "url": "https://gemini.google/jp/subscriptions/?hl=ja", "kind": "公式ドキュメント"},
    {"title": "Google's new Gemini tiers cut free users to its weakest model and lock $5/month subscribers out of Pro", "publisher": "The Decoder", "url": "https://the-decoder.com/googles-new-gemini-tiers-cut-free-users-to-its-weakest-model-and-lock-5-month-subscribers-out-of-pro/", "kind": "報道"},
    {"title": "Gemini's free tier is getting a major downgrade on October 9", "publisher": "Digital Trends", "url": "https://www.digitaltrends.com/computing/geminis-free-tier-is-getting-a-major-downgrade-on-october-9/", "kind": "報道"}
  ],
  "thumb_text": "Gemini",
  "share_text": "Geminiの無料版は10月9日からFlash-Liteだけに。AI PlusもProモデルを使えなくなる",
  "thumb_style": "3d",
  "thumb_prompt": "Three glossy toy rockets of different sizes on a launch pad, the biggest two behind a velvet rope with a golden ticket gate, while only the smallest one stays open for everyone.",
  "editor_note": ""
}
---
Googleは、Geminiアプリで使えるモデルをプランごとに分ける変更を公式ヘルプで告知しました。Google AIのプランに入っていない人は10月9日から最も小さいモデルの「Flash-Lite」だけになり、上位の「Pro」はGoogle AI Pro（日本では月額2,900円）以上の利用者に限られます。

## 何が変わるか

対象は、個人アカウントで使うGeminiアプリ（ウェブとスマートフォンアプリ）です。ヘルプページ「Changes to Gemini model access and limits」は、プランごとに選べるモデルを次のように示しています。

| プラン | 日本の月額 | Flash-Lite | Flash | Pro | Deep Think |
|---|---|---|---|---|---|
| プランなし（無料） | 0円 | ○ | × | × | × |
| Google AI Plus | 725円 | ○ | ○ | × | × |
| Google AI Pro | 2,900円 | ○ | ○ | ○ | ○ |
| Google AI Ultra | 14,500円〜 | ○ | ○ | ○ | ○ |

月額は日本向け料金ページの表示です。Deep Thinkとは、複数の考え方を並行して試してから答えを出す推論のモードで、GoogleはAI ProとAI Ultraで選べると書いています。各モデルでは考える量（effort）を低・中・高から選べます。高くするほど答えは丁寧になりますが、そのぶん利用上限を早く使い切ります。

切り替えの時期はプランで違います。

:::quote https://support.google.com/gemini/answer/17004136?hl=en | Gemini Apps Help「Changes to Gemini model access and limits」
> These changes will start to take effect for users without an AI subscription on October 9th. For users with an AI Plus subscription, you should receive an email that explains when these changes will take effect for you.
AIのプランに加入していない利用者には10月9日からこの変更が順次適用される。AI Plusの加入者には、いつ適用されるかをメールで知らせる。
:::

ページは「2026年10月から」の変更と書いていますが、地域を限る記述はありません。

利用上限の数え方も変わります。回数ではなく、指示の複雑さ・使う機能・会話の長さから計算量を見積もり、5時間ごとに回復して、週の上限に達すると止まる方式です。上限は無料版を基準に、AI Plusが2倍、AI Proが4倍、AI UltraはAI Proの5倍か20倍です。画像・動画・音楽の生成、Deep Research、Proモデル、長考モードは上限を多く消費すると明記しています。

{{card:https://support.google.com/gemini/answer/17004136?hl=en|Changes to Gemini model access and limits|Gemini Apps Help}}

## これまでとの違い

日本向けの料金ページは10月4日時点で、無料版でも「3.6 Flash」と「3.1 Pro（制限あり）」が使え、AI Plusでも3.1 Proが使えると案内しています。10月9日以降、無料版からはFlashとProの両方が、AI PlusからはProが外れることになります。逆にAI Proは、料金ページでUltra向けの先行機能として紹介してきたDeep Thinkも選べるようになります。

ヘルプの別のページでは、使える会話の長さ（コンテキスト）も無料版が3.2万トークン、AI Plusが12.8万トークン、AI ProとUltraが100万トークンとプランで分けています。モデルと上限の両方で、無料と有料の差をはっきりさせる方向です。

## 背景と論点

Googleは9月30日に最上位モデル「Gemini 4 Argon」を発表しましたが、一般の利用者にはまだ提供していません（[既報](/news/20261001-google-gemini-4-argon/)）。The Decoderは、無料枠を絞る今回の変更が、計算資源を多く使うArgonを一般向けに出す準備になりうると報じています。Digital Trendsなど複数の媒体も、10月9日からの無料版の切り替えを、使える機能が大きく減る変更として取り上げています。

Googleはヘルプで変更の理由を説明していません。無料版でもProを試せたことはGeminiの強みの1つでしたが、ほかの会社の無料版と比べて有利だった点がなくなります。一方、AI ProにDeep Thinkが付くことは、月額2,900円の利用者には上乗せになります。

## 日本のビジネスへの影響

- **使えるか**: 日本でもGeminiアプリは使え、ヘルプの変更告知に地域の除外はありません。日本の料金ページは10月4日時点で更新されていないため、適用日はアプリの表示とGoogleからのメールで確かめてください
- **誰にどう効くか**: 無料版のGeminiで資料の下書きやリサーチをしている個人事業主やマーケターは、10月9日以降、答えの質が下がったと感じる可能性があります。社員に無料版を使わせている会社は、業務の品質がそろわなくなる点に注意が要ります
- **今すぐやれること**: 無料版で回している定型の作業を2〜3件選び、10月9日の前後で同じ指示を出して出力を比べてください。差が大きければAI Pro（月額2,900円、Proモデルと4倍の上限）への切り替えを検討する材料になります。AI Plusの加入者はProが外れるため、Proを日常的に使っているならAI Proとの差額（月2,175円）で判断します
- **注意点**: 上限が計算量で数えられるため、Proや長考モード、画像生成を多用すると有料版でも週の途中で止まることがあります。会社で使うなら、プランだけでなく使い方の目安も共有してください

各社のチャットAIの料金と無料版の違いは、[チャットAIのおすすめと料金比較](/best/chat/)にまとめています。
