---
{
  "title": "Adobeの7製品をClaudeで作り直し無料公開、米開発者「ソフトは終わった」に賛否",
  "description": "米国の開発者Brandon Thomas氏が、Claude Opus 5.5でPhotoshopやPremiereなどAdobeの7製品に似せたアプリを作り、無料公開した。Photoshop版は約1週間で1.7万超の支持を集めたが、開発元もまだ仕事には使えないと認めている。",
  "date": "2026-10-08T10:55:00+09:00",
  "category": "usecases",
  "tags": ["ArtCraft", "Claude Opus 5.5", "活用事例", "個人開発", "オープンソース", "画像編集"],
  "summary": [
    "米国の開発者Brandon Thomas氏は、Claude Opus 5.5を使ってPhotoshopやIllustratorなどAdobeの7製品に似せたアプリを作り、無料で公開した",
    "Photoshop版の「PhotoCraft」はPhotoshopのファイルを開いて編集でき、公開の場のGitHubで1.7万超の支持を集めている",
    "ただし開発元自身が「まだ日々の仕事でPhotoshopの代わりにはならない」と明記しており、見た目が似すぎていることによる法的な危うさも指摘されている"
  ],
  "sources": [
    {"title": "PhotoCraft（GitHub）", "publisher": "ArtCraft / storytold", "url": "https://github.com/storytold/photocraft", "kind": "公式サイト"},
    {"title": "Crafting Apps: open-source creative tools", "publisher": "ArtCraft", "url": "https://getartcraft.com/apps", "kind": "公式サイト"},
    {"title": "Brandon Thomas氏（echelon）のコメント", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=49934228#49934844", "kind": "コミュニティ"},
    {"title": "Brandon Thomas氏（echelon）のコメント「Software is over」", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=49922569#49928088", "kind": "コミュニティ"},
    {"title": "Brandon Thomas氏（echelon）のコメント（開発段階について）", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=49959605", "kind": "コミュニティ"},
    {"title": "“Software is over”: Bold AI developer takes aim at Adobe with open source clones", "publisher": "Ars Technica", "url": "https://arstechnica.com/ai/2026/10/software-is-over-bold-ai-developer-takes-aim-at-adobe-with-open-source-clones/", "kind": "報道"},
    {"title": "Someone Vibe Coded a Free Knockoff of Adobe Creative Suite", "publisher": "Gizmodo", "url": "https://gizmodo.com/someone-vibe-coded-a-free-knockoff-of-adobe-creative-suite-2000823322", "kind": "報道"}
  ],
  "thumb_text": "ArtCraft",
  "thumb_style": "illustration",
  "thumb_prompt": "A lone artisan in a cozy workshop carving seven identical-looking wooden paint palettes and film reels on a workbench, while a friendly robotic arm hands him the tools, and a tall stack of cancelled subscription envelopes sits in the waste bin.",
  "share_text": "PhotoshopなどAdobeの7製品をClaudeで作り直して無料公開。「ソフトは終わった」と語る米開発者に賛否",
  "editor_note": ""
}
---
米国の開発者Brandon Thomas氏が、AnthropicのAI「Claude Opus 5.5」を使い、Photoshop、Illustrator、Premiere ProなどAdobeの代表的な7製品に似せたアプリを作り、9月末から無料のオープンソース（設計図にあたるプログラムを公開し、誰でも使える形）で公開しています。Photoshop版のPhotoCraftは、プログラム共有サイトGitHubで1.7万超のスター（支持の印）を集めました。

## 何を作ったか

アプリ群の名前は「Crafting Apps」で、AIで画像や動画を作るサービスを手がけてきたArtCraftのチームが出しています。7本の対応関係は次のとおりです。

| ArtCraftのアプリ | 似せた元のAdobe製品 | 用途 |
|---|---|---|
| PhotoCraft | Photoshop | 写真・画像の編集 |
| VectorCraft | Illustrator | ロゴや図版などのイラスト |
| FilmCraft | Premiere Pro | 動画編集 |
| LightCraft | Lightroom | 写真の整理と現像 |
| PdfCraft | Acrobat | PDFの閲覧・整理 |
| EffectCraft | After Effects | 動きのある映像効果 |
| DesignCraft | InDesign | 冊子やチラシの組版 |

いずれもMac、Windows、Linuxで動き、一部はブラウザでも使えます。最も進んでいるPhotoCraftは、レイヤー、マスク、文字、図形といったPhotoshopの基本の道具をそろえ、メニューやショートカットキーの位置もPhotoshopに合わせています。Photoshopの保存形式（PSD）のファイルを開いて編集し、保存し直すこともできます。

{{card:https://getartcraft.com/apps|Crafting Apps: open-source creative tools|ArtCraft}}

GitHubを見ると、チームは10月7日にWord、Excel、PowerPoint、AutoCADに似せたアプリの置き場所も新たに作っており、対象はAdobe以外にも広がりつつあります。

## どう作ったか

Thomas氏は開発者の掲示板Hacker Newsへの書き込みで、Opus 5.5を使って、Adobe製品と同じ働きをするアプリを一から作っていると説明しています。元のプログラムを写すのではなく、外から見える動きをまねて作り直す「クリーンルーム」と呼ばれる手法をとったとしています。使ったプログラミング言語はRust（動作が速く、さまざまなOSで動かしやすい言語）です。

作ろうと思ったきっかけについて、同氏は同じ書き込みで、解約の時に違約金を取られる仕組みに何度も悩まされたことを挙げました。Ars Technicaは、同氏が2月からAIだけでプログラムを書いていると語ったことも報じています。

費用の面では、アプリはどれも無料で、利用条件の緩いMITかApacheのライセンスで公開されています。Ars Technicaによると、開発費はArtCraftがもともと売っているAI画像・動画サービスの利用料でまかなう計画です。

## 成果と、本人の見立て

Thomas氏はHacker Newsで「Software is over（ソフトウェアは終わった）」と書き、Photoshopを丸ごと一発で作ったと主張しました。別の書き込みでは、Adobeとの機能の差を99%埋めるには時間がかかるが、年単位ではなく月単位で済むとの見通しを示しています。

一方、公開の場に置かれた説明書きは慎重です。

:::quote https://github.com/storytold/photocraft | ArtCraft「PhotoCraft」GitHubのREADME
> PhotoCraft is in early alpha, and we want to be straight about where it stands: much of Photoshop's feature surface exists in some form, but it is not yet a Photoshop replacement for daily professional work.
PhotoCraftはまだ初期の試作段階で、現状を率直に伝えたい。Photoshopの機能の多くは何らかの形でそろっているが、日々のプロの仕事でPhotoshopの代わりになるところまでは来ていない。
:::

説明書きは、足りないものとして生成AIの機能、約20の道具、文字組みの細かい調整、外部の追加機能（プラグイン）との互換を挙げています。実際に試したGizmodoの記者は、不具合は多いものの本物のPhotoshopを触っている感覚に近く、必要な機能は思った場所にあったと伝えています。ただし、画像を自由に変形する機能は動きが不安定だったと報じています。

Ars Technicaは、プログラムを写さずに作り直すこと自体は一般に合法とされてきた一方、見た目や画面構成が元の製品に似すぎると、商品の外観を守る「トレードドレス」の考え方で争いになりうると指摘しています。

## 日本で真似するなら

- **必要なもの**: Claude Opus 5.5を使えるClaudeの有料プランか、開発用のClaude Code。ただし今回の規模は、Rustの経験が約10年あると語る熟練の開発者による例です
- **手順の目安**: 非エンジニアがいきなり大きなアプリを作るのではなく、「社内で毎月お金を払っているが、使う機能は少しだけ」という道具を1つ選び、必要な機能だけの小さな代わりをClaudeに作らせるのが現実的です
- **使うだけなら**: PhotoCraftなどは公式サイトから無料で入手できます。年に数回だけ画像を加工する用途なら、試す価値はあります
- **注意点**: 試作段階なので、納品物や大事なデータの編集には使わないでください。他社製品の見た目をそのまままねたものを自社で作って社外に出すのは、法的な危うさがあります

## 日本のビジネスへの影響

- **使えるか**: アプリは無料で日本からも入手できます。画面は英語で、日本語の文字組みへの対応は確認できていません
- **誰にどう効くか**: 制作会社やマーケティング部門で、ソフトの月額料金を多くの人数分払っている経営者・管理者にとって、AIで「必要な分だけの道具」を作れる時代が近づいていることを示す例です。デザイナーにとっては、当面はAdobe製品の代わりではなく、軽い作業用の選択肢が1つ増えた程度です
- **今すぐやれること**: 社内で使っている有料ソフトを一覧にし、使っている機能が少ないものを洗い出してください。それが、AIで作る小さな代わりやもっと安い既製品に切り替える候補になります
- **注意点**: 「AIなら何でもすぐ作れる」という主張と、開発元自身の「まだ仕事には使えない」という評価の間には大きな差があります。宣伝の言葉より、実際に自社の作業が終わるかで判断してください

Claudeで作った他の作品の例は、[Claudeが楽譜の書き方から考えたジュークボックスの記事](/news/20261007-scrimshaw-jukebox-claude-game-music/)でも紹介しています。AIを使ったプログラミングの道具の選び方は、[コーディングAIのおすすめと料金比較](/best/coding/)にまとめています。
