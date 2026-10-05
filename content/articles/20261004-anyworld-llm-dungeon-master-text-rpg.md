---
{
  "title": "AnyWorldはローカルLLMが進行役を務める多人数テキストRPG、自宅のサーバーで遊べるOSS",
  "description": "個人開発者が、AIを進行役にした多人数のテキストRPG「AnyWorld」をMITライセンスで公開した。ローカルのGemma 4で動き、生成設定を詰めると指示を守る試験の合格率が62%から100%に上がったという。",
  "date": "2026-10-04T19:10:00+09:00",
  "category": "usecases",
  "tags": ["AnyWorld", "Gemma 4", "活用事例", "個人開発", "ゲーム", "ローカルLLM"],
  "summary": [
    "AnyWorldは、ホストが書いた舞台設定をもとにAIが物語を進め、最大6人がブラウザで自分の行動を文章で書き込む多人数のテキストRPG",
    "AnyWorldはllama.cpp互換のローカルLLMかOpenAIのAPIにつなぐ。作者は開発中、Gemma 4の26B A4Bを12.8万トークンの文脈で進行役に使った",
    "作者は付属の試験で、温度などの生成設定を詰めるとモデルの合格率が62%から安定して100%になったと公表している"
  ],
  "sources": [
    {"title": "iamarxs/AnyWorld", "publisher": "GitHub（iamarxs）", "url": "https://github.com/iamarxs/AnyWorld", "kind": "公式サイト"},
    {"title": "AnyWorld INSTALL.md", "publisher": "GitHub（iamarxs）", "url": "https://github.com/iamarxs/AnyWorld/blob/main/INSTALL.md", "kind": "公式サイト"},
    {"title": "Anyworld, a self-hosted multiplayer text RPG where a local LLM is the Dungeon Master", "publisher": "Reddit r/LocalLLaMA", "url": "https://www.reddit.com/r/LocalLLaMA/comments/1wwkudj/anyworld_a_selfhosted_multiplayer_text_rpg_where/", "kind": "コミュニティ"}
  ],
  "thumb_text": "AnyWorld",
  "share_text": "AIが進行役のテキストRPGを自宅サーバーで。Gemma 4で動く多人数ゲーム「AnyWorld」",
  "thumb_style": "diorama",
  "thumb_prompt": "A tiny fantasy tabletop adventure where a small glowing laptop sits at the head of the table as the game master behind a little screen, with three miniature adventurers and a dragon figure in front of it.",
  "editor_note": ""
}
---
個人開発者のiamarxs氏が、AIを進行役（ダンジョンマスター、DM）にした多人数参加のテキストRPG「AnyWorld」をGitHubで公開しています。サイコロも点数表もなく、参加者は自分のキャラクターの行動を文章で書くだけで、AIがそれをまとめて物語を進めます。作者は現地時間10月3日、ローカルLLMの利用者が集まるRedditのr/LocalLLaMAで紹介しました。

## 何を作ったか

AnyWorldとは、1人がゲームサーバーを立ててAIのモデルにつなぎ、仲間がブラウザから参加して遊ぶテキストアドベンチャーです。参加できる人数は設定で決め、設定例の既定値は6人です。ライセンスはMITです。作者は、初期の無料版のAI Dungeon（AI Dungeon 2）から着想を得たと書いています。

:::quote https://github.com/iamarxs/AnyWorld | AnyWorldのREADME（GitHub）
> A multiplayer text adventure where you never have to roll dice or keep score — just write what your character does.
サイコロを振ることも点数をつけることもない多人数のテキストアドベンチャー。自分のキャラクターが何をするかを書くだけでいい。
:::

遊び方は次の流れです。

1. ホストが舞台とパーティーの目的を書く。AIがシナリオの題名を付ける
2. 参加者がパスワードで入り、ホストが開始するとAIが冒頭の場面を書く
3. 参加者が順番に行動を書き込み、全員がそろうとAIがまとめて1ラウンド分の結果を書く

参加者どうしのチャットはAIに送られないので、作戦会議もできます。ホストは「建物に入ったら20%の確率で崩れる」のような確率イベントを1つだけ仕込めます。サイコロはAIではなくPythonのプログラムが振り、結果は参加者には見せず、物語の展開としてだけ表に出ます。

{{card:https://github.com/iamarxs/AnyWorld|iamarxs/AnyWorld|GitHub}}

## どう作ったか

サーバーはPython 3.11以上で動き、AIはllama.cppのようなOpenAI互換のローカルサーバーか、OpenAIのAPIにつなぎます。OpenAIでは、GPT-5.6 Lunaで実際に動かして試したと書いています。OpenAIにつないだ場合はホストがシナリオを書いた言語で物語が進むため、英語以外の言語でも遊べる仕組みです。ローカルのモデルにつないだ場合は、現時点では英語で語るよう指示しています。

作者がINSTALL.mdで公開した開発時の構成は、Googleのオープンモデル「Gemma 4 26B A4B」（1語ごとに動くのは約40億パラメータ）を12.8万トークンの文脈で動かすものです。より小さいGemma 4の19B版の派生モデルも、メモリの少ないGPUで遊べる候補として推しています。

長く遊ぶための工夫もあります。古いラウンドはAIが要約して覚え直し、要約で事実が抜けていないかを別に確かめ、抜けていれば元の履歴を残します。接続が切れた参加者には「何もしない」行動をサーバーが自動で割り当て、ゲームを止めません。

開発にもAIを使っています。READMEによると、コードを書く手伝いにはQwen 3.8の27B、OpenAIのGPT-5.6 LunaとGPT-6 Astraを使いました。

## 成果と分かったこと

作者は、モデルが確率イベントの指示を正しく守るかを測る試験スクリプトを同梱しています。READMEでは、生成の設定（温度、top-p、top-kなど）が結果を大きく左右したと書いています。

:::quote https://github.com/iamarxs/AnyWorld | AnyWorldのREADME（GitHub）
> With good model settings, the benchmark pass rate for a model climbed from 62% to a consistent 100% over several runs.
適切な設定にすると、あるモデルの試験の合格率は62%から、何度走らせても100%へと上がった。
:::

INSTALL.mdには、Q4に量子化したGemma 4で十分に遊べたという設定値（温度1.0、top-p 0.95、top-k 20など）も載っています。一方で作者は、物語の質と一貫性はモデル次第で、AIがすべての指示を守る保証はないとも書いています。1台のサーバーで同時に遊べるのは1ゲームだけで、再起動すると進行中のゲームは消えます。

## 日本のビジネスへの影響

- **必要なもの**: Python 3.11以上が動くPCと、llama.cppで動かすローカルのモデル。ローカルのモデルでは今のところ英語で語るため、日本語で遊ぶならOpenAIのAPIキーを使う形になります
- **手順の目安**: リポジトリを取得して `pip install -e .` で入れ、`config.yaml` にホスト用と参加者用の別々のパスワードを書いて起動します。ブラウザで `https://127.0.0.1:4141/` を開けば始められ、社内LANの仲間も参加できます
- **使いどころ**: ゲーム以外にも、研修のロールプレイ（クレーム対応や商談の模擬）や、チームでのアイデア出しの即興劇に転用できます。確率イベントを「顧客が急に値引きを求める」のように設定すれば、想定外への対応を練習できます
- **注意点**: 対話の記録（HTML）には、参加者に見せない進行役への指示や判定の結果も残ります。社内で使うなら記録の置き場所を管理してください。OpenAIにつなぐと、参加者の書いた文章は外部に送られます

ローカルでLLMを動かす環境の選び方は、[ローカルLLM・オープンウェイトモデルのおすすめ](/best/local-llm/)にまとめています。AIにゲームを作らせる例では、[ASTRABOX](/news/20261001-astrabox-codex-arcade-game-generator/)の記事もあります。
