---
{
  "title": "Codexに任天堂Switch 2の守りを破らせた、ゲーム機2台をAIにつなぎ約2週間 個人が初の改造方法を公開",
  "description": "米国のセキュリティ研究者pepsipu氏が、OpenAIのCodexを使って任天堂Switch 2の制限を外す初の方法「ns2jb」を公開した。AIにゲーム機2台の操作と画面を任せ、約2週間で欠陥を発見。マリオカートの改造版は1日で作った。",
  "date": "2026-10-23T10:35:00+09:00",
  "category": "policy",
  "tags": ["Codex", "OpenAI", "Nintendo Switch 2", "セキュリティ", "ゲーム", "エージェント"],
  "summary": [
    "米国の研究者pepsipu氏が、任天堂Switch 2の制限を外して自作のプログラムを動かす初の方法「ns2jb」を10月22日に公開した",
    "OpenAIのCodexに2台のゲーム機のコントローラー操作と画面を任せ、複数のCodexを並行して欠陥を探させ、約2週間で突破した",
    "人は狙いを決めて仕上げの組み立てを担い、改造版マリオカートはCodexがほぼ1日で作った。AIで「破る側」の手間が大きく下がっている"
  ],
  "sources": [
    {"title": "jailbreaking the switch 2", "publisher": "Sammy Hajhamid（pepsipu）のブログ", "url": "https://pepsipu.com/blog/2026-10-switch2-jailbreak-ns2jb/", "kind": "公式サイト"},
    {"title": "pepsipu の投稿", "publisher": "X @pepsipu", "url": "https://x.com/pepsipu/status/2113117920373137622", "kind": "X投稿"},
    {"title": "Nintendo Switch 2 jailbreak breakthrough shows what AI can do, but it's not a one-click hack", "publisher": "Digital Trends", "url": "https://www.digitaltrends.com/gaming/nintendo-switch-2-jailbreak-ai-codex/", "kind": "報道"}
  ],
  "thumb_prompt": "Two handheld game consoles on a cluttered desk wired to small black boxes and a laptop, with a tiny robot arm pressing a console power button using a smart light-switch gadget, as glowing cracks spread across a padlock icon floating above the consoles.",
  "thumb_style": "illustration",
  "thumb_text": "Codex × Switch 2",
  "share_text": "Codexに任天堂Switch 2の守りを破らせた。ゲーム機2台をAIにつないで約2週間、個人が初の改造方法を公開",
  "editor_note": ""
}
---
米国のセキュリティ研究者pepsipu（ペプシプ）氏は現地時間10月22日、任天堂のゲーム機Switch 2の制限を外し、任天堂が認めていないプログラムを動かす方法「ns2jb」を公開しました。本人によれば、この種の方法はSwitch 2で初めてです。欠陥探しの大部分を担ったのは、OpenAIのAIエージェント「Codex」です。作業期間は約2週間で、本体を物理的に改造せず、ソフトだけで突破した点が注目されています。

## 何が起きたか

ゲーム機は、メーカーが許可したソフトしか動かないよう何重にも守られています。この守りを破って自由にプログラムを動かすことは「ジェイルブレイク（脱獄）」と呼ばれ、pepsipu氏は、Switch 2でこの種の突破をした例は自分の知る限り初めてだとしています。

pepsipu氏はXで公開を告げ、Switch 2専用ソフト『マリオカートワールド』に、サンリオのシナモロールや米国のアニメのキャラクター、初音ミクなどを走らせた改造版を見せました。

{{x:https://x.com/pepsipu/status/2113117920373137622}}

投稿では、Switch 2の脱獄に成功し、マリオカートワールドにキャラクターを追加したと報告し、詳しい解説と手順へのリンクを載せています。対象は公開時点で最新の本体ソフト（23.0.1）です。

## Codexは何をしたのか

pepsipu氏が自身のブログで明かした作業の分担は、次のようなものです。

- **人が用意した環境**: Switch 1とSwitch 2の2台を、外からコントローラー操作と画面の取り込みができる小型の機器につなぎました。本体が固まったときは、Amazonで買える照明用のスマートスイッチで電源ボタンを押させる仕掛けまで作り、AIが人の手を借りずに試行を繰り返せるようにしました
- **Codexの担当**: 複数のCodexを並行して動かし、それぞれ別の入り口を探させました。ブラウザーを狙う方法は失敗しましたが、Switch 1用の古いプログラミング学習ソフトに数値のあふれによる欠陥を見つけ、さらに本体のファイル管理の部分にも欠陥を見つけました
- **人の担当**: どこを狙うかの判断、メモリーの中身の取り出しと分析、見つかった欠陥を組み合わせて最終的にプログラムを動かすまでの道筋づくりは、pepsipu氏自身が行いました

:::quote https://pepsipu.com/blog/2026-10-switch2-jailbreak-ns2jb/ | pepsipu氏のブログ「jailbreaking the switch 2」
> The JetKVMs allow Codex to send controller inputs to the Switches over USB and receive video output over HDMI.
JetKVM（遠隔操作用の小型機器）によって、CodexはUSB経由でSwitchにコントローラーの操作を送り、HDMI経由で画面の映像を受け取れる。
:::

デモに使ったマリオカートの改造版は、Codexにほぼ任せて1日で作ったといいます。pepsipu氏は「遊びで作った」と書いています。

## できること、できないこと

米Digital Trendsは、今回の方法は「ワンクリックで終わる改造」ではないと伝えています。電源を入れ直すと元に戻るため、使うたびにやり直す必要があります。本体の中の一部の仕組みしか乗っ取れず、好きなソフトを自由に入れられる状態にはなっていません。

入り口に使われたSwitch 1用ソフトは米国のeショップで約25ドルで売られていますが、同紙は、買えば誰でも同じことができるわけではないとしています。任天堂がこのソフトの販売を止めれば、この入り口はふさがる可能性があります。任天堂の公式な反応は、記事の執筆時点で確認できていません。

## 背景と論点

AIを使った欠陥探しは、ここ数週間で急に目立つようになりました。10月21日には、Webサイトの多くが動くプログラム言語PHPの重大な欠陥をAIが見つけ、[修正版が出たばかり](/news/20261022-php2shell-ai-found-php-flaws/)です。今回は、専門の企業ではなく個人が、市販の機器とAIだけで世界的なゲーム機の守りを2週間で破った点が違います。

守る側から見ると、これまで高度な専門家が数か月かけていた作業が、AIで短く安くなっていることを意味します。一方で、pepsipu氏の記録を見ると、AIが自力で最後まで突破したわけではなく、狙いの判断や最後の組み立ては人が担っています。「AIが勝手にハッキングした」という受け止め方は正確ではありません。

## 日本のビジネスへの影響

- **使えるか**: Codexは日本からも使えますが、今回のようにゲーム機など他社の製品の守りを破る行為は、日本では不正競争防止法や著作権法の技術的保護手段の回避に当たるおそれがあり、利用規約にも反します。真似をする話ではありません
- **誰にどう効くか**: ゲーム会社や家電・IoT機器メーカーの製品開発・セキュリティ担当者に直接関係します。個人がAIに機器の操作と画面の確認を任せ、休まず試行を繰り返せるようになったことで、発売後に守りが破られるまでの時間は短くなると見ておく必要があります
- **今すぐやれること**: 自社製品を持つ会社は、同じようにAIを使って自社の機器やアプリの欠陥を先に探す社内の試験を検討するとよいでしょう。外部の研究者からの報告を受け付ける窓口（脆弱性報奨金の制度など）が整っているかも見直しどころです
- **注意点**: 守りの弱点は、今回のように古い互換用のソフトなど、見落としやすい周辺部分から突かれることがあります。最新の部分だけでなく、過去の製品との互換の仕組みも点検の対象に含める必要があります

AIにプログラムを書かせる道具の比較と料金は、[AIコーディングツールのおすすめと料金比較](/best/coding/)にまとめています。
