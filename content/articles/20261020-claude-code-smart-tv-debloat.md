---
{
  "title": "テレビの広告がClaude Codeで消えた、型番を伝えるだけで家のスマートテレビを作り直す人が続出",
  "description": "スマートテレビの広告や視聴データの収集を、Claude CodeなどのAIに頼んで止める人が海外で増えている。手順を公開したGitHubの「cleanyourtv」は2日で数千人が試したと作者が話し、54機種・23ブランドで動作が確かめられている。",
  "date": "2026-10-20T04:15:00+09:00",
  "updated": "2026-10-24T21:55:00+09:00",
  "category": "usecases",
  "tags": ["Claude Code", "cleanyourtv", "dumbtv", "活用事例", "プライバシー", "広告"],
  "summary": [
    "スマートテレビの広告や重い動作に不満を持つ人が、Claude CodeなどのAIに頼んでテレビの中身を作り直している",
    "米国の開発者は両親のテレビの型番を伝えただけで、AIがWi-Fi経由でテレビを見つけ、不要なアプリ25個を止めた",
    "手順を公開した無料の「cleanyourtv」は54機種で動作が確かめられ、元に戻す仕組みもある。失敗例も出ている"
  ],
  "sources": [
    {"title": "Gathin の投稿", "publisher": "X @gathint", "url": "https://x.com/gathint/status/2111379569030939102", "kind": "X投稿"},
    {"title": "cleanyourtv", "publisher": "GitHub Gathin23", "url": "https://github.com/Gathin23/cleanyourtv", "kind": "公式サイト"},
    {"title": "dumbtv", "publisher": "GitHub humblemuzzu", "url": "https://github.com/humblemuzzu/dumbtv", "kind": "公式サイト"},
    {"title": "Muzzammil の投稿", "publisher": "X @DevMuzzammil", "url": "https://x.com/DevMuzzammil/status/2111912547318395338", "kind": "X投稿"},
    {"title": "Mihir Gupta の投稿", "publisher": "X @0900mihir", "url": "https://x.com/0900mihir/status/2111746030228455883", "kind": "X投稿"},
    {"title": "Ryan Doyle の投稿", "publisher": "X @doooyle", "url": "https://x.com/doooyle/status/2111196679680540724", "kind": "X投稿"},
    {"title": "@jihadsinwar の投稿", "publisher": "X @jihadsinwar", "url": "https://x.com/jihadsinwar/status/2112135188733989173", "kind": "X投稿"},
    {"title": "Jake Stevens の投稿", "publisher": "X @stake_jevens", "url": "https://x.com/stake_jevens/status/2112851884901794284", "kind": "X投稿"},
    {"title": "Quiet Tizen", "publisher": "GitHub jss8649", "url": "https://github.com/jss8649/quiet-tizen", "kind": "公式サイト"},
    {"title": "People are using AI to make their smart TVs dumb again", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/10/19/people-are-using-ai-to-make-their-smart-tvs-dumb-again/", "kind": "報道"},
    {"title": "Developer guts Samsung TV of features that sold his personal data, made it 3x faster", "publisher": "TweakTown", "url": "https://www.tweaktown.com/news/114227/developer-guts-samsung-tv-of-features-that-sold-his-personal-data-made-it-3x-faster/index.html", "kind": "報道"}
  ],
  "thumb_prompt": "A living room at night where a large flat TV shows a clean, minimal home screen, while a pile of tiny colorful advertisement banners lies swept onto the floor beneath it like confetti, a laptop glowing on the sofa.",
  "thumb_style": "photo",
  "thumb_text": "Claude Code",
  "share_text": "テレビの型番をClaude Codeに伝えたら、Netflixの前に出ていた広告が消えた。スマートテレビを作り直す人が海外で続出",
  "editor_note": ""
}
---
スマートテレビの広告や視聴データの収集を、AnthropicのプログラミングAI「Claude Code」などに頼んで止める人が、10月中旬から海外で相次いでいます。手順を無料で公開した「cleanyourtv」の作者は、2日で数千人が自分のテレビで同じことをしたとTechCrunchに話しています。

## 何をしたのか

きっかけの1つは、開発者のGathin T.氏が10月17日にXに書いた投稿です。両親のテレビでは、Netflixを開く前にスポンサーの広告が出ていました。そこでClaude Codeにテレビの型番を伝えたところ、AIが自宅のWi-Fiにつながったテレビを探し出し、メーカーが入れていたアプリ25個を取り除いて、新しいホーム画面まで書いたといいます。仕上がりは「Apple TVのよう」だと書いています。

{{x:https://x.com/gathint/status/2111379569030939102}}

ほかにも同じような報告が続いています。

- **動作を軽くした**: Mihir Gupta氏は、遅くて耐えられなくなったテレビをClaude Codeと午後のうちに直したと投稿しました。不要なアプリ25個を止め、192MBあった標準のホーム画面を83MBの自作のものに置き換え、壁紙も入れ替わるようにしたそうです
- **画面を自分の仕事用に**: Ryan Doyle氏は、販売ページに載っていたテレビの説明をClaude Codeに送って「これをハックできる？」と聞いたと投稿しています。広告と重さが消えただけでなく、売上や予定、天気を映すスクリーンセーバーも作ったといいます

## どう作ったか

Gathin氏はやり方をGitHubに「cleanyourtv」として公開しました。中身は、AIに読ませる指示文と、それを助ける小さな道具です。説明書きによると、流れは次のとおりです。

1. テレビの設定で「開発者向けオプション」を出し、パソコンからの操作を許可する（同じWi-Fiにつながったパソコンを使う）
2. 指示文をClaude Codeのような、パソコンを操作できるAIに貼り、テレビの型番を伝える
3. 使っているアプリや音声操作の有無など、AIの質問に答える
4. AIが今の設定を控えたうえで、メーカーの利用データの送信や広告のアプリを止め、新しいホーム画面を入れて、1つずつ確認する

かかる時間は15分ほどとしています。対象はAndroid TVとGoogle TVを使うテレビで、利用者が確かめた54機種・23ブランドの一覧があります。サムスンやLGの独自の仕組みのテレビは対象外です。説明書きは、元に戻せることを強調しています。

:::quote https://github.com/Gathin23/cleanyourtv | GitHub「cleanyourtv」
> Nothing is flashed, rooted or deleted; packages are disabled in the user profile.
書き換えも、管理者権限の取得も、削除もしない。アプリは利用者の設定の中で止めるだけだ。
:::

別の開発者Muzzammil Yasin Sabuwala氏の「dumbtv」は、AmazonのFire TVを主な対象にしたものです。「テレビは自分が払った分のこと、つまり自分のアプリと外部入力だけをすればいい」という考えで、画面に映る内容を読み取って視聴履歴を集める機能や、広告用の識別番号の仕組みなど、約65個のアプリを止めます。TechCrunchによると、作るのにはDeepSeekとClaudeのモデルを使ったと本人が話しています。

## うまくいかなかった例もある

すべてが順調なわけではありません。あるXの利用者は、Claudeがテレビを再起動しようとして基本ソフトまで消してしまい、テレビが動かなくなったと投稿しています。TechCrunchは、「テレビをハックして」といった短い頼み方ではClaudeが応じないことがあり、手の込んだ頼み方が必要だったという声や、Fire TVの作業が途中で止まった人がいることも伝えています。

cleanyourtvの説明書きも、テレビが頼っているアプリを止めると不具合が出るとして、少しずつ止めて元に戻す道具を手元に置くよう勧めています。多くの場合、テレビの自動更新も止まるので、更新したいときは自分で元に戻す必要があります。作業に使うパソコンからの操作の許可は、終わったら切るよう書かれています。

## 日本で真似するなら

- **必要なもの**: Android TVかGoogle TVのテレビ（TechCrunchによると、ソニーやTCL、シャオミなどの機種で試した報告がある）、同じWi-Fiにつながるパソコン、Claude Code（Claudeの有料プラン、月20ドルのPro以上）。料金は「[Claude Codeの料金](/news/20261008-claude-code-pricing-plans/)」にまとめています
- **始める前に**: 自分の機種がcleanyourtvの一覧に載っているか確かめます。載っていない機種は、AIが手探りで進めることになり、失敗しやすくなります
- **注意点**: メーカーの保証やサポートの対象外になる可能性があります。日本向けのテレビに入っている地上波の番組表やリモコンの専用ボタンの機能を止めてしまうと、普段の視聴に困ります。止めるアプリはAIの提案をそのまま受け入れず、名前を確認してから進めてください

## 追記（10月24日）

この記事で「対象外」と書いたサムスンのテレビでも、同じことをした人が出てきました。米国のJake Stevens氏は現地時間10月21日、OpenAIのプログラミングAI「Codex」を使って、自宅のサムスン製テレビから利用者を追跡する機能を取り除いたとXに投稿しました。Claudeにはテレビの管理者権限を取る作業を断られたため、Codexに切り替えたと書いています。

{{x:https://x.com/stake_jevens/status/2112851884901794284}}

投稿では、止めた機能で動作が「3倍速くなった」としています。TweakTownによると、止めたのは画面に映る番組を読み取って視聴履歴を集める機能（ACR）、HDMIでつないだ機器の監視、音声アシスタント「Bixby」の呼びかけ待ちなどです。

本人とみられるGitHubの「Quiet Tizen」は、投稿よりずっと慎重です。試したのは2025年モデルの75型（UN75U8000FFXZA）1台だけで、サムスンが公開していない内部の仕組みに頼っていると説明しています。

:::quote https://github.com/jss8649/quiet-tizen | GitHub「Quiet Tizen」
> It is a working case study with a reusable toolkit, not a universal installer or a replacement operating system.
1台で試した記録と道具一式であり、どのテレビにも入る万能のインストーラーや、基本ソフトの代わりではない。
:::

説明書きでは、Netflixの操作の遅れが直ったかはまだ確かめられていないとも書いています。メーカーの更新で設定が元に戻ることがあることも明記されています。サムスンのテレビで試すには一時的に管理者権限を取る必要があり、Android TVの手順より危険が大きい点に注意が必要です。

## 日本のビジネスへの影響

- **使えるか**: 手順は無料で公開されており、Claude Codeも日本から使えます。ただし日本向けのテレビでの動作報告はまだ少なく、試すなら使っていない古いテレビからが安全です
- **誰に効くか**: テレビ向けの広告を扱う広告運用者やメディアの担当者です。スマートテレビの広告や視聴データは、テレビメーカーの大きな収入源になっています。AIに頼めば誰でもそれを止められるようになると、テレビ画面の広告の届く範囲や、視聴データの精度が変わってくる可能性があります
- **今すぐやれること**: 自社がテレビ画面の広告や視聴データを使っているなら、こうした「止める人」がどのくらいいるかを広告の配信先に確かめておくことです。個人として試すなら、cleanyourtvの説明書きを読み、元に戻す手順を先に確認してください。プログラミングを任せるAIの選び方は[コーディングAIの用途別ガイド](/best/coding/)を参考にしてください
- **注意点**: AIにパソコンや家電の操作を任せると、思わぬ設定まで変えてしまうことがあります。会社の会議室のテレビやサイネージで試すのは、情報システムの担当者の了解を得てからにしましょう
