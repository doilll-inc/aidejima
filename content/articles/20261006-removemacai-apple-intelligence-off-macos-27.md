---
{
  "title": "Macの「Apple Intelligence」を消して12GB空ける無料ツール、オフのスイッチ廃止で個人が公開",
  "description": "最新のmacOS 27でApple Intelligenceを一括でオフにするスイッチがなくなったことを受け、個人開発者がAI機能を止めてモデルを消す無料ツール「RemoveMacAI」を公開した。報道各社の試算では約12GBの空き容量が戻るが、使えなくなる機能も多い。",
  "date": "2026-10-06T19:50:00+09:00",
  "category": "products",
  "tags": ["Apple", "Apple Intelligence", "RemoveMacAI", "macOS", "オープンソース", "個人開発"],
  "summary": [
    "最新のmacOS 27では、AppleのAI機能「Apple Intelligence」をまとめてオフにするスイッチがなくなった",
    "個人開発者が、AI機能を止めて本体に保存されたAIモデルを消す無料ツールを公開し、約12GBが空くと報じられている",
    "Siriや文章作成支援などが使えなくなり、Appleの非公式な方法に頼るため、将来のアップデートで動かなくなるおそれもある"
  ],
  "sources": [
    {"title": "RemoveMacAI（README）", "publisher": "GitHub omlahore/RemoveMacAI", "url": "https://github.com/omlahore/RemoveMacAI", "kind": "公式サイト"},
    {"title": "How to get the next generation of Apple Intelligence", "publisher": "Apple Support", "url": "https://support.apple.com/en-us/121115", "kind": "公式ドキュメント"},
    {"title": "An open-source tool lets you delete 12GB of Apple Intelligence data on macOS", "publisher": "The Verge", "url": "https://www.theverge.com/ai-artificial-intelligence/1004672/mac-delete-apple-intelligence-ai-tool", "kind": "報道"},
    {"title": "Mac Users Reclaim 12GB+ of Storage With Apple Intelligence Removal Tool", "publisher": "MacRumors", "url": "https://www.macrumors.com/2026/10/05/apple-intelligence-removal-tool-frees-mac-storage/", "kind": "報道"},
    {"title": "This tool frees up Apple Intelligence storage on macOS, but think twice before using it", "publisher": "9to5Mac", "url": "https://9to5mac.com/2026/10/05/this-tool-frees-up-apple-intelligence-storage-on-macos-but-think-twice-before-using-it/", "kind": "報道"},
    {"title": "New tool removes Apple Intelligence from macOS 27 to reclaim storage", "publisher": "Cult of Mac", "url": "https://www.cultofmac.com/news/remove-apple-intelligence-macos-27-removemacai", "kind": "報道"}
  ],
  "thumb_style": "illustration",
  "thumb_prompt": "A laptop computer drawn like a moving truck being unloaded, with workers carrying out heavy crates labeled only with small sparkle symbols, and a big empty bright space left inside the laptop's screen.",
  "thumb_text": "RemoveMacAI",
  "share_text": "MacのAI機能をまとめてオフにして約12GB空ける無料ツール。macOS 27でオフのスイッチがなくなり個人が公開",
  "editor_note": ""
}
---
最新のmacOS 27でAppleのAI機能「Apple Intelligence」を一括でオフにするスイッチがなくなったことを受け、個人開発者のオム・ラホール氏が、AI機能を止めて本体のAIモデルを削除する無料ツール「RemoveMacAI」をGitHubで公開しました。報道各社によると、1回の操作で約12GBの保存容量を取り戻せます。

## 何が起きたか

RemoveMacAIとは、macOS 27を入れたMacで、Apple Intelligenceの各機能をまとめてオフにし、ダウンロード済みのAIモデル（AIの本体にあたるデータ）を消して、再ダウンロードも止めるツールです。誰でも無料で使え、中身のプログラムも公開されています。

作者は、ツールを作った理由をREADME（説明書きのページ）の冒頭でこう書いています。

:::quote https://github.com/omlahore/RemoveMacAI | RemoveMacAI（GitHub）README
> macOS 27 no longer has a single switch for Apple Intelligence, and its models stay on disk after the features are turned off.
macOS 27にはApple Intelligenceをまとめてオフにするスイッチがもうなく、機能をオフにしてもモデルはディスクに残ったままになります。
:::

ツールがオフにするのは、Siri（「Hey Siri」とメニューバーのアイコンを含む）、文章の書き直しや要約をする「作文ツール」、絵文字を作る「Genmoji」、画像を作る「Image Playground」、ChatGPTとの連携、メール・メッセージ・Safari・メモ・通知の要約、写真から不要な物を消す機能などです。音声入力は別の設定なので残ります。`--keep` という指定で、写真の機能だけ残すといった使い分けもできます。

## どのくらい容量が空くか

Appleの公式サポートページは、最新のApple Intelligenceに必要な保存容量を、M3以降のチップと12GB以上のメモリを積んだMacで最大14GB、それ以外の対応Macで最大8GBとしています。

{{card:https://support.apple.com/en-us/121115|How to get the next generation of Apple Intelligence|Apple Support}}

The Verge、MacRumors、Cult of Macはいずれも、RemoveMacAIで約12GBが空くと報じています。Cult of Macは、機種によっては設定画面のApple Intelligenceの表示が30GBを超える例もあると伝えています。なお作者によると、モデルを消したあともmacOSが実際にファイルを片付けるまでは、設定画面の「ストレージ」に容量が残って見えることがあります。

## どういう仕組みか

READMEによると、ツールはMacのシステムの中身を直接書き換えません。会社が社員のMacを管理するときに使う「構成プロファイル」という公式の仕組みで機能を止め、モデルの削除もAppleのダウンロード管理の機能を通して行います。そのうえで、消したモデルの取得先をMacの中の閉じた窓口に振り向けて、再ダウンロードを防ぎます。プロファイルを入れる際は、利用者が「システム設定」で承認する必要があります。

元に戻すには `removemacai revert` を実行してプロファイルを外すだけで、その後はmacOSが必要に応じてモデルを再びダウンロードします。作者は、先行して同じ仕組みを調べ上げた別の開発者のツールを土台にしたと明記しています。対応はAppleの自社チップを積んだMacとmacOS 27だけです。

## 反応と論点

「AIはいらないので容量を返してほしい」という人には歓迎される一方で、慎重な声も出ています。9to5Macは、システムの深い部分を変える非公式のツールであり、Appleが今後このやり方を塞ぐ可能性もあるとして「使う前によく考えて」と呼びかけました。MacRumorsは、ツールが使う設定の一部はmacOS 26.4で非推奨（将来なくなる予定）になったという作者の説明を紹介し、利用は自己責任だと添えています。

また、作者のREADMEによると、Siriやカレンダーの言葉による予定編集だけでなく、AppleのAIモデルを使うほかのアプリやショートカットの一部も動かなくなります。Appleはこのツールについてコメントを出していません。

## 日本のビジネスへの影響

- **使えるか**: 無料で、日本のMacでもmacOS 27とAppleの自社チップという条件を満たせば動きます。ただし操作は「ターミナル」に1行を貼り付けて実行する形で、画面のボタンだけでは完結しません。
- **誰にどう効くか**: 容量の小さいMacを社員に配っている企業の情報システム担当者に関係があります。会社のMacでは、AI機能を使わせない方針の有無も含めて、管理の方法を決めておく必要が出てきました。個人では、容量不足に悩むMacユーザーが対象です。
- **今すぐやれること**: まず「システム設定」→「一般」→「ストレージ」でApple Intelligenceが何GB使っているかを確かめましょう。試すなら、変更内容を表示するだけの `--dry-run` 付きで実行し、何がオフになるかを見てから判断するのが安全です。
- **注意点**: 会社のMacに個人の判断で入れるのは避け、情報システム部門に相談してください。Appleの仕様変更で将来動かなくなるおそれがあり、作文ツールなどの便利な機能も一緒に使えなくなります。文章の下書きや要約に別のAIを使うなら、[文章作成AIのおすすめと料金比較](/best/writing/)が参考になります。
