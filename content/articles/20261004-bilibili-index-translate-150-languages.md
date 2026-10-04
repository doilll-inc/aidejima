---
{
  "title": "Index-Translateは150言語を訳すbilibiliのオープンモデル、用語集や書式の指定に従う",
  "description": "中国の動画サイトbilibiliが翻訳専用のモデル群「Index-Translate」をApache 2.0で公開した。2B・9B・35Bの3サイズで150言語に対応し、10月4日には無料のAPIも始めた。日本語への吹き替えや長文の一括翻訳のモデルもある。",
  "date": "2026-10-04T18:55:00+09:00",
  "category": "dev",
  "tags": ["bilibili", "Index-Translate", "翻訳", "オープンウェイト", "中国AI", "ローカルLLM"],
  "summary": [
    "bilibiliはQwen3.5をもとにした翻訳モデル群Index-Translateを9月30日に公開し、2B・9B・35B-A3B（プレビュー）の重みをApache 2.0で配っている",
    "Index-Translateのテキストモデルは150言語に対応し、用語集の固定、JSONなどの書式の保持、文体の指定といった翻訳の指示に従うよう訓練されている",
    "bilibiliは10月4日、35B-A3BをOpenAI互換の無料APIで公開した。声を保ったまま日本語に吹き替えるIndex-Echoなども同じ一家にある"
  ],
  "sources": [
    {"title": "bilibili/Index-Translate: A Multilingual Translation Model Family", "publisher": "GitHub（bilibili）", "url": "https://github.com/bilibili/Index-Translate", "kind": "公式ドキュメント"},
    {"title": "Index-Translate evaluation", "publisher": "GitHub（bilibili）", "url": "https://github.com/bilibili/Index-Translate/blob/main/docs/evaluation.md", "kind": "公式ドキュメント"},
    {"title": "Index-Translate: A Multilingual Translation Model Family -- Text, Speech, Controlled Dubbing, and Long-Document Translation", "publisher": "arXiv", "url": "https://arxiv.org/abs/2609.40181", "kind": "論文"},
    {"title": "IndexTeam/Index-Translate-9B", "publisher": "Hugging Face（IndexTeam）", "url": "https://huggingface.co/IndexTeam/Index-Translate-9B", "kind": "公式ドキュメント"},
    {"title": "Index-Translate: Bringing Meaning Across Languages, from Text to Speech", "publisher": "bilibili", "url": "https://index-translate.bilibili.com/", "kind": "公式サイト"},
    {"title": "bilibili released Index-Translate, a Multilingual Translation Model Family based on Qwen3.5", "publisher": "Reddit r/LocalLLaMA", "url": "https://www.reddit.com/r/LocalLLaMA/comments/1wxa1wr/bilibili_released_indextranslatea_a_multilingual/", "kind": "コミュニティ"},
    {"title": "Bilibili Open-Sources Index-Translate, a Qwen3.5-Based Translation Model Family for 150 Languages", "publisher": "Pandaily", "url": "https://pandaily.com/bilibili-index-translate-open-source-qwen3-5-150-languages", "kind": "報道"}
  ],
  "thumb_text": "Index-Translate",
  "share_text": "bilibiliが翻訳専用のオープンモデルIndex-Translateを公開。150言語、用語集や書式の指定に従う",
  "editor_note": ""
}
---
中国の動画サイト「bilibili（ビリビリ）」のAIチームが、翻訳に特化したモデル群「Index-Translate」をオープンウェイトで公開しています。テキストの翻訳は150言語に対応し、重みはApache 2.0ライセンスで商用にも使えます。現地時間10月4日には、最大の35B-A3B（プレビュー版）をGPUなしで試せる無料APIも始めました。

## 何が公開されたか

Index-Translateとは、AlibabaのQwen3.5を土台に、翻訳の作業に絞って訓練したモデルの一家です。普通の翻訳エンジンとの違いは、「この用語はこう訳す」「JSONの形は崩さない」といった翻訳の指示を守るように作られている点です。

:::quote https://github.com/bilibili/Index-Translate | bilibili「Index-Translate」README（GitHub）
> The text models cover 150 languages and follow translation instructions such as terminology, formatting, and content-preservation requirements.
テキストモデルは150言語に対応し、用語・書式・原文を残す部分の指定といった翻訳の指示に従う。
:::

公開されたのは、用途の違う4種類です。

| モデル | 何をするか | サイズ |
|---|---|---|
| Index-Translate | テキスト・構造化データ・ネットのスラングの翻訳（150言語） | 2B／9B／35B-A3B（プレビュー） |
| Index-Echo | 話し声を字幕にする、または元の話者の声で吹き替える | 2B／9B |
| Index-Homura | 音節の数を指定して訳す（吹き替えの尺合わせ向け） | 2B／9B |
| Index-NativeLong | 長い文書を丸ごと訳し、固有名詞の訳をそろえる | 2B／9B |

日本語に関係するのは、Index-Echoの吹き替えが中国語・英語から日本語への方向に対応していることと、Index-NativeLongの長文翻訳に中国語と日本語の組み合わせがあることです。35B-A3Bは「350億パラメータのうち1回に動くのは30億」の混合エキスパート（MoE）型で、まだ正式版ではありません。

ローカルで動かすためのGGUF（llama.cpp用）、FP8、NVFP4の量子化版も10月3日に出ました。READMEでは、最小の2Bは一般向けのGPUで動くとしています。ブラウザで開いたページを手元のモデルで訳す拡張機能（Chrome・Edge・Firefox）も同じリポジトリにあります。

{{card:https://index-translate.bilibili.com/|Index-Translate デモと無料API|bilibili}}

## 指示に従う翻訳とは

READMEの例では、韓国語に訳すときに中国語のハッシュタグだけは残す、商談メールらしい丁寧な文体にする、英語の「plant」を工業の文脈で「工場」と訳す、といった指定をしています。用語集はコマンドで「原語:訳語」の組を渡すだけです。

bilibiliが公表した評価表では、指示にどれだけ従ったかを測る「instTrans IFscore」で35B-A3Bが0.8336、9Bが0.8209でした。比較に並べたOpenAIのGPT-5.6-Solは0.7624、GoogleのGemini 3.5 Flash Liteは0.6374です。一方、一般的な翻訳の質を測るWMT26の判定では、GPT-5.6-Solが89.10で、35B-A3Bの76.76を上回っています。素の翻訳の質ではなく、指定を守る力を売りにしたモデルです。

論文では、性能は「1000億パラメータ級の翻訳モデルや最先端モデルに匹敵する」と主張しています。どれも開発元自身の計測で、第三者の検証はまだありません。

## 背景

bilibiliはアニメやゲームの動画が多い中国の動画サイトで、字幕や吹き替えの多言語化は自社の事業に直結します。README の例も、ゲームの告知文や「FF14をやりたくなる」といったネットのスラングの訳が中心です。評価表では、同じく翻訳に特化したオープンモデルのHy-MT2（7Bと30B-A3B）を主な比較相手に置き、9Bはどちらも上回ったとしています。

ローカルLLMの利用者が集まるRedditのr/LocalLLaMAには、10月4日に公開の告知が投稿されました。中国のメディアPandailyも、150言語対応のオープンソース化として報じています。

## 日本のビジネスへの影響

- **使えるか**: 重みはApache 2.0で、日本からもHugging Faceで入手できます。無料APIは日本語の訳文も返せますが、利用規約や回数の上限はREADMEに書かれていません。中国企業のサーバーに文章を送ることになるため、社外秘の文書には使わず、試すなら手元で動かす方が安全です
- **誰にどう効くか**: ゲームやアプリのローカライズ担当、ECの商品情報を多言語化している担当者に向きます。JSONやプレースホルダーを壊さずに訳す指定ができるため、翻訳後の手直しが減る可能性があります。動画の吹き替えを検討しているマーケターは、Index-Echoのデモで日本語の声を確かめられます
- **今すぐやれること**: 自社の用語集10〜20語と、過去に機械翻訳で崩れた文書を1本用意し、デモか9Bで訳してDeepLや汎用のチャットAIと見比べてください。用語が守られるかを数えるだけでも判断材料になります
- **注意点**: 評価はすべて開発元の計測です。35B-A3Bはプレビュー版で、正式版は未公開です。日本語の品質は、自社の文書で確かめるまで分かりません

翻訳サービスの料金と選び方は[AI翻訳のおすすめと料金比較](/best/translation/)にまとめています。ローカルで多言語字幕を作る例として、[mlsubgen](/news/20261003-mlsubgen-local-subtitles-37-languages/)も参考になります。
