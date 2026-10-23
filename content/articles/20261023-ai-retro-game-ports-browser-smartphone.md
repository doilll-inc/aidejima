---
{
  "title": "昔のゲームをClaudeなどのAIでスマホやブラウザへ移植、ゼルダやHaloも 発売元は削除要請",
  "description": "20年以上前の家庭用ゲームを、AIの助けでブラウザやiPhoneで動かす個人の移植が9月末から相次いでいる。ブラウザ版Haloは公開5時間で約2万回遊ばれた。一方で発売元の削除要請や、手作業で解析してきた愛好家の反発も起きている。",
  "date": "2026-10-23T22:25:00+09:00",
  "category": "usecases",
  "tags": ["Claude", "Claude Opus 5.5", "ゲーム", "活用事例", "著作権", "個人開発"],
  "summary": [
    "20年以上前の家庭用ゲームを、AIに解析を手伝わせてブラウザやiPhoneで動くようにする個人の移植が9月末から相次いでいる",
    "ブラウザで遊べる初代Haloは公開5時間で約2万回プレイされ、ゼルダの「風のタクト」もiPhoneやiPadで動く版が無料で公開された",
    "米Activisionは「コール オブ デューティ」のブラウザ版に削除を求め、何年も手作業で解析してきた愛好家の交流サイトは閉鎖を決めた"
  ],
  "sources": [
    {"title": "chrissotraidis/bluewake", "publisher": "GitHub chrissotraidis", "url": "https://github.com/chrissotraidis/bluewake", "kind": "公式サイト"},
    {"title": "The Legend of Zelda: The Wind Waker, now running natively on iOS and iPadOS.", "publisher": "X @chrissotraidis", "url": "https://x.com/chrissotraidis/status/2104569951197839384", "kind": "X投稿"},
    {"title": "It's been 5 hours: Nearly 20,000 games across 115 countries and territories.", "publisher": "X @mitchellhynes", "url": "https://x.com/mitchellhynes/status/2105048698849759310", "kind": "X投稿"},
    {"title": "The Halo CE in the Browser project blew up.", "publisher": "X @mitchellhynes", "url": "https://x.com/mitchellhynes/status/2105442402525987121", "kind": "X投稿"},
    {"title": "Retro gaming is being overrun with AI", "publisher": "The Verge", "url": "https://www.theverge.com/ai-artificial-intelligence/1015430/ai-retro-games-decomp-recomp-port", "kind": "報道"},
    {"title": "We might be cooked, as these vibe-coded web browser ports of Halo, The Simpsons Hit and Run, and GTA Vice City seem to work perfectly", "publisher": "Kotaku", "url": "https://kotaku.com/we-might-be-cooked-as-these-vibe-coded-web-browser-ports-of-halo-the-simpsons-hit-and-run-and-gta-vice-city-seem-to-work-perfectly-2000743300", "kind": "報道"},
    {"title": "Activision hits vibe-coded classic Call of Duty browser ports with DMCA takedowns", "publisher": "XDA Developers", "url": "https://www.xda-developers.com/activision-hits-vibe-coded-classic-call-of-duty-browser-ports-with-dmca-takedowns/", "kind": "報道"},
    {"title": "Video game reverse engineering community shuts down because AI has made it too easy", "publisher": "404 Media", "url": "https://404media.co/video-game-reverse-engineering-community-shuts-down-because-ai-has-made-it-too-easy", "kind": "報道"},
    {"title": "\"Halo\", \"Vice City\", \"Black Ops\": AI ports of games run in the browser", "publisher": "heise online", "url": "https://www.heise.de/en/news/Halo-Vice-City-Black-Ops-AI-ports-of-games-run-in-the-browser-11485764.html", "kind": "報道"}
  ],
  "thumb_prompt": "A chunky retro game console cartridge from the early 2000s plugged directly into the side of a modern smartphone lying on a desk, with tiny pixel-style sea waves and a small sailboat spilling out of the phone screen onto the desk surface.",
  "thumb_style": "3d",
  "thumb_text": "AIでゲーム移植",
  "share_text": "20年以上前のゲームをAIでブラウザやiPhoneへ。ブラウザ版Haloは5時間で約2万回遊ばれたが、発売元は削除要請、愛好家の交流サイトは閉鎖へ",
  "editor_note": ""
}
---
20年以上前の家庭用ゲーム機のソフトを、AIの助けを借りてWebブラウザやiPhoneで動くように作り直す個人の「移植」が、9月末から海外で相次いでいます。Webブラウザで遊べるようにした初代「Halo」は、公開から5時間で約2万回遊ばれました。一方で、ゲームの発売元が削除を求めたり、これまで手作業で解析してきた愛好家の場が閉鎖を決めたりと、反発も広がっています。

## 何が起きているか

米The Vergeは現地時間10月23日、この1か月ほどで、昔のゲームが「本来動かないはずの場所」で動く移植が次々と話題になっていると報じました。仕組みは主に2つあります。ゲームの機械語から人が読めるプログラムを復元する「デコンパイル」と、機械語を別の機種向けにまとめて書き換える「リコンパイル」です。どちらも以前は、熟練した愛好家が何年もかけて進める作業でした。

代表的な例が2つあります。

**ブラウザで遊べる初代Halo**: 開発者のミッチェル・ハインズ氏が9月29日に公開しました。2001年に初代Xbox向けに発売されたシューティングゲームを、ソフトのインストールなしにブラウザで動かせます。ゲームのデータは含まれておらず、遊ぶ人が自分のディスクから作ったデータを読み込ませる形です。別の愛好家グループが進めていたデコンパイルの成果を土台にしています。

ハインズ氏はXで、公開から5時間で115の国と地域から2万回近く遊ばれ、平均で毎秒94コマで動いたと報告しました。

{{x:https://x.com/mitchellhynes/status/2105048698849759310}}

**iPhoneで動くゼルダ「風のタクト」**: 任天堂が2002年にゲームキューブで発売した「ゼルダの伝説 風のタクト」を、iPhoneやiPad、Mac、Windowsで直接動くようにした「BlueWake」です。開発者のクリス・ソトレイディス氏は9月28日にXで公開を告知し、画質を最大4倍に上げられることや、横長の画面への対応をうたいました。

{{x:https://x.com/chrissotraidis/status/2104569951197839384}}

## AIは何をしているのか

BlueWakeは、開発の進め方をGitHubの説明ページで明かしています。

:::quote https://github.com/chrissotraidis/bluewake | BlueWake（GitHub）
> BlueWake is developed with substantial AI assistance for code, testing, documentation and debugging.
BlueWakeは、プログラム、テスト、説明書き、不具合の修正にAIの大幅な助けを借りて開発している。
:::

使ったAIの名前は書かれていません。ゲーム情報サイトの米Kotakuは、こうした移植の広がりについて、AnthropicのClaude Opus 5.5がデコンパイルを非常に得意とし、一晩動かしておくだけで作業が進むと紹介しています。米404 Mediaは、OpenAIのGPT-6 Astraのような最新のAIで、ゲームの解析がごく簡単になったと報じました。特定のAIだけの現象ではないようです。

注意したいのは、AIがゼロから作ったわけではない点です。BlueWakeは、愛好家が手作業で進めてきた風のタクトのデコンパイルや、ゲームキューブのエミュレーター（別の機械をまねて動かすソフト）「Dolphin」などの成果の上に作られています。Halo版も同じく、先行する解析の成果を使っています。

## 反発と論点

ゲームの権利を持つ会社は動き始めています。米XDA Developersによると、米Activisionは10月、AIで作られた「コール オブ デューティ ブラックオプス」シリーズのブラウザ版に対し、米国の著作権法に基づく削除要請を出し、作品は公開停止になりました。こちらは元のゲームから地図や人物のデータを取り出して使っていたと報じられています。BlueWakeやHalo版が「ゲームのデータは含めない」「自分で正規に入手したディスクが必要」と明記しているのは、こうした線引きを意識しているためです。BlueWakeは任天堂とは無関係のファンの制作物だとも書いています。

長年の愛好家の間には複雑な受け止めもあります。404 Mediaによると、ゲームの解析に取り組む人たちの交流サイト「decomp.dev」は10月、閉鎖を発表しました。管理者は、AIで大量の解析が持ち込まれ、人が主導した作品とAI任せの作品の見分けがつかなくなり、共同作業というコミュニティの意味が壊れたと説明しています。独メディアのheiseによると、「バンジョーとカズーイの大冒険」のPC版を手がけた開発者は、人の積み上げた道具をAIで使い回すやり方を「敬意を欠く」と批判しました。

一方で、もう売られていない、今の機械では動かないゲームを残す手段になるという見方もあり、heiseもその可能性に触れています。

## 日本のビジネスへの影響

- **使えるか**: 紹介した移植はどれも非公式です。日本のゲームの多くは日本の会社が権利を持っており、取り出したデータを配ったり公開したりすれば著作権の侵害になりえます。遊ぶ場合も、各国の法律やゲームの利用規約を自分で確かめる必要があります。
- **誰に効くか**: 過去の作品を多く持つゲーム会社や、古い業務システムを抱える企業の情報システム部門です。動かせる機械がなくなった古いソフトを、AIの助けで今のパソコンやスマホ向けに作り直せる可能性が見えてきました。逆に、自社の製品が外部の誰かに短期間で解析される前提で守りを考える必要もあります。
- **今すぐやれること**: 自社で動かし続けている古いソフトのうち、作り直しの費用が見合わず放置しているものを1つ挙げ、AIで読み解けるかを小さく試してみる価値があります。コーディング向けAIの選び方は[コーディングAIのガイド](/best/coding/)にまとめています。ゲーム会社は、過去作の非公式な移植が出たときの方針（黙認するか、削除を求めるか、公式に出し直すか）を決めておくと慌てずに済みます。
- **注意点**: 他社の製品の解析は、契約や法律で禁じられている場合があります。自社が権利を持つソフトから始めてください。また、AIが作り直したプログラムには気づきにくい不具合が残ることがあり、元のソフトと同じ動きをするかの確認は欠かせません。
