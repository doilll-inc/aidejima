---
{
  "title": "AIに「昔のゲーム風の曲を」と頼んだら楽譜の書き方から発明、6曲入りのジュークボックスに",
  "description": "開発者でAIの検証ブログで知られるSimon Willison氏が、AnthropicのClaude Opus 5.5にゲーム音楽の作曲を頼んだ。AIは文字で書く独自の楽譜形式を考え、6曲とブラウザで鳴らす再生機まで1回の指示で作った。",
  "date": "2026-10-07T04:10:00+09:00",
  "category": "usecases",
  "tags": ["Scrimshaw Jukebox", "Claude Opus 5.5", "活用事例", "個人開発", "音楽", "ゲーム"],
  "summary": [
    "開発者のSimon Willison氏は10月6日、AIのClaude Opus 5.5に作らせたゲーム音楽の再生機「Scrimshaw Jukebox」を公開した",
    "Claude Opus 5.5は文字だけで書ける独自の楽譜の形式を考え、海辺や幽霊船を思わせる6曲を作り、ブラウザで鳴らす仕組みまで用意した",
    "Willison氏は結果を「驚くほど良い」と評価しつつ、作曲がAIの新しい能力かどうかは比較実験が要るとしている"
  ],
  "sources": [
    {"title": "Tool: Scrimshaw Jukebox", "publisher": "Simon Willison's Weblog", "url": "https://simonwillison.net/2026/Oct/6/scrimshaw-jukebox/", "kind": "公式サイト"},
    {"title": "Scrimshaw Jukebox", "publisher": "tools.simonwillison.net", "url": "https://tools.simonwillison.net/scrimshaw-jukebox", "kind": "公式サイト"},
    {"title": "Tool: Kākāpō Party", "publisher": "Simon Willison's Weblog", "url": "https://simonwillison.net/2026/Sep/26/kakapo-party/", "kind": "公式サイト"},
    {"title": "Simon Willison の投稿", "publisher": "X @simonw", "url": "https://x.com/simonw/status/2104002636513206422", "kind": "X投稿"},
    {"title": "Scrimshaw Jukebox: Opus 5.5 compone 6 pistas retro jugables", "publisher": "Ecosistema Startup", "url": "https://ecosistemastartup.com/scrimshaw-jukebox-opus-5-5-compone-6-pistas-retro-jugables/", "kind": "報道"}
  ],
  "thumb_text": "Scrimshaw Jukebox",
  "thumb_style": "3d",
  "thumb_prompt": "A vintage wooden jukebox standing on a moonlit pirate harbor pier, its glowing front panel showing scrolling lines of plain text instead of records, with a small pirate ship's lantern swaying beside it.",
  "share_text": "AIに「昔のゲーム風の曲を」と頼んだら、楽譜の書き方から考えて6曲と再生機まで作った",
  "editor_note": ""
}
---
AIの検証ブログで知られる開発者のSimon Willison氏は現地時間10月6日、AnthropicのAI「Claude Opus 5.5」に作曲させたゲーム音楽を、ブラウザで聴ける「Scrimshaw Jukebox」として公開しました。AIは曲を作るだけでなく、文字で書く楽譜の形式を自分で考え、それを鳴らす再生機まで1回の依頼で仕上げています。

## 何を作ったか

Scrimshaw Jukeboxとは、文字だけで書かれた楽譜を、ブラウザの中のシンセサイザー（電子的に音を作る楽器）で演奏するウェブページです。「Moonlit Harbor（月夜の港）」「Ghost Galleon（幽霊船）」「Duel on the Docks（波止場の決闘）」など、昔の冒険ゲームを思わせる6曲が入っています。録音した音は使っておらず、音はすべてその場で合成されます。

再生中に楽譜を開いて書き換えると、その場で曲が変わります。パートごとに音を消すこともでき、メロディー、和音、ベース、打楽器がどう重なっているかを耳で確かめられます。

{{card:https://tools.simonwillison.net/scrimshaw-jukebox|Scrimshaw Jukebox|Simon Willison}}

## どう作ったか

Willison氏がClaudeに送った依頼は短いものでした。まずゲーム音楽を書いてほしいと頼み、そのために簡単な文字ベースの楽譜形式を考え、それを鳴らせる画面を作り、例として何曲か入れるよう指示しています。目指す水準として、往年の冒険ゲーム「The Secret of Monkey Island」の音楽を挙げました。

:::quote https://simonwillison.net/2026/Oct/6/scrimshaw-jukebox/ | Simon Willison's Weblog「Tool: Scrimshaw Jukebox」
> It leaned a lot harder into the Monkey Island theme than I had intended, but the results are surprisingly good.
思っていた以上にMonkey Islandの世界観に寄せてきたが、出来は驚くほど良い。
:::

Claudeが考えた楽譜は、上から順に「設定」「パート（楽器）」「フレーズのまとまり」「曲の構成」を書く形です。テンポや拍子、スチールドラムやオルガンといった楽器の割り当てを1行ずつ書き、音符は「D5」のように音名と高さで表します。音を伸ばすときはハイフンを足し、休みは点で書きます。ゲーム音楽らしく、最初に1回だけ流す部分と、くり返し流す部分を分けて指定できるのも特徴です。小節の長さが合わないと、エディターがどの行が何拍ずれているかを教えてくれます。

使ったのは、AIとの会話画面の中で小さなアプリを作って動かせるClaudeの機能です。プログラムを書かない人でも、同じ頼み方で試せます。

## 成果と、本人の見立て

Willison氏は、文章を扱うAIが作曲までこなせるようになったのは、ここ数カ月で現れた新しい能力かもしれないと書いています。ただし、新旧のモデルで慎重に比べないと、以前からできたのかどうかは判断できないとも付け加えています。

同氏は9月にも、Claude Opus 5.5にドット絵のアニメーションを作らせ、講演の締めくくりのスライドに使いました。その際もXで、ドット絵のアニメーションが「意外なほどうまい」と書いています。

{{x:https://x.com/simonw/status/2104002636513206422}}

文字のやり取りが本業のAIが、絵や音楽のような「文字以外の作品」を、文字で書ける形式に置き換えて作る例が増えています。楽譜を文字にしたことで、AIは曲を組み立てやすくなり、人も中身を読んで直せるようになりました。

## 日本で真似するなら

- **必要なもの**: Opus 5.5を選べるClaudeのプランとブラウザだけです。追加のソフトや楽器は要りません
- **手順の目安**: 「〇〇風のBGMを作りたい。まず文字で書ける簡単な楽譜の形式を考え、それを鳴らせる画面を作り、例を数曲入れて」と頼みます。曲調を変えたいときは、会話で「もっと明るく」「テンポを上げて」と続けます
- **使いどころ**: 社内イベントの動画、展示会の待機画面、アプリの試作品につける仮のBGMなど、まず雰囲気を確かめたい場面に向きます
- **注意点**: Willison氏の例でも、AIは指定した作品の雰囲気に強く寄せました。実在の曲に似すぎていないかは人が確かめ、広告や商品に使う場合は権利面を慎重に判断してください

## 日本のビジネスへの影響

- **使えるか**: Claudeは日本語で使え、同じ依頼は日本からも試せます。ただし今回の6曲そのものの利用条件は示されていません
- **誰にどう効くか**: 動画や販促物を作るマーケター、アプリやゲームの企画担当者に関係があります。作曲の知識がなくても、「港町の夜」のような言葉から短いBGMの試作を作れます
- **今すぐやれること**: 次の社内動画やプレゼン用に、上の頼み方で1曲作らせ、楽譜を少し書き換えて変化を確かめてみてください
- **注意点**: AIが作った曲が既存の曲と似る可能性は残ります。本番で使う音楽は、権利のはっきりした素材や専用の音楽生成サービスと比べて選ぶのが安全です

Claudeを含む対話AIの料金と選び方は、[対話AIのおすすめと料金比較](/best/chat/)にまとめています。
