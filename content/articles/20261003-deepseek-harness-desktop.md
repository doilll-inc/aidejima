---
{
  "title": "DeepSeek Harnessにデスクトップ版、MITライセンスのエージェントをMacとWindowsで",
  "description": "DeepSeekがオープンソースのAIエージェント基盤DeepSeek HarnessのmacOS・Windows向けデスクトップ版を公開した。文書作成からコーディング、定期実行まで機能をプラグインで足せる。GitHubのスターは24万を超える。",
  "date": "2026-10-03T03:40:00+09:00",
  "category": "dev",
  "tags": ["DeepSeek", "DeepSeek Harness", "エージェント", "オープンソース", "コーディング", "中国AI"],
  "summary": [
    "DeepSeekは10月2日、AIエージェント基盤DeepSeek HarnessのmacOS（Apple silicon）とWindows向けデスクトップ版を公開した",
    "DeepSeek Harnessは文書・表計算・コード・調べものを扱うMITライセンスのOSSで、機能はすべてプラグインとして足し引きできる",
    "公式の安全上の注意では、セキュリティ監査を受けておらず本番利用に耐える前提ではないと明記している"
  ],
  "sources": [
    {"title": "DeepSeek Harness", "publisher": "DeepSeek", "url": "https://www.deepseek.com/en/harness/", "kind": "公式発表"},
    {"title": "DeepSeek の投稿", "publisher": "X @deepseek_ai", "url": "https://x.com/deepseek_ai/status/2105915715241062644", "kind": "X投稿"},
    {"title": "deepseek-ai/deepseek-harness（README・SAFETY.md）", "publisher": "GitHub deepseek-ai", "url": "https://github.com/deepseek-ai/deepseek-harness", "kind": "公式ドキュメント"},
    {"title": "dsh-v0.2.0-rc.2 リリースノート", "publisher": "GitHub deepseek-ai", "url": "https://github.com/deepseek-ai/deepseek-harness/releases", "kind": "公式ドキュメント"},
    {"title": "DeepSeek Harness Desktop for macOS and Windows", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=49929489", "kind": "コミュニティ"},
    {"title": "DeepSeek Harness Desktop Preview Version Officially Launched", "publisher": "36Kr", "url": "https://eu.36kr.com/en/p/3998199345500040", "kind": "報道"}
  ],
  "thumb_text": "DeepSeek Harness",
  "share_text": "DeepSeekのOSSエージェント「DeepSeek Harness」にMac・Windowsのデスクトップ版。機能は全部プラグイン",
  "thumb_style": "3d",
  "thumb_prompt": "A sleek desktop computer monitor with a friendly robotic arm emerging from the screen, plugging colorful puzzle-piece shaped modules into a toolbox on the desk.",
  "editor_note": ""
}
---
中国のDeepSeekは10月2日、オープンソースのAIエージェント基盤「DeepSeek Harness」のデスクトップ版を、macOS（Apple silicon）とWindows（64ビット）向けに公開しました。これまではコマンドからWeb画面を立ち上げる形でしたが、インストーラーを入れるだけで使えるようになります。GitHubのリポジトリは8月の公開から2か月足らずで24万以上のスターを集めています。

## 何が発表されたか

DeepSeek Harnessとは、DeepSeekが開発する、AIエージェントを動かすための土台（ハーネス）となるソフトです。ファイルの整理、表計算データの分析、文書やスライドの作成、リポジトリを読んだうえでのバグ修正やテスト、出典付きの調べもの、スクリプトの定期実行までを1つの画面で扱います。ライセンスはMITで、商用でも自由に改変して使えます。

{{x:https://x.com/deepseek_ai/status/2105915715241062644}}

DeepSeekの公式アカウントはXで、macOSとWindows向けのパッケージ版を出したと告知し、Linuxはnpmの`@deepseek-ai/dsh`パッケージで使えると案内しました。製品ページは、世界向けの公開プレビュー（試用版）としています。

:::quote https://www.deepseek.com/en/harness/ | DeepSeek公式「DeepSeek Harness」製品ページ
> DeepSeek Harness is now in public preview worldwide and open source, with composable plugins that extend what agents can do.
DeepSeek Harnessは世界向けの公開プレビューとなり、オープンソースです。組み合わせ可能なプラグインで、エージェントのできることを広げられます。
:::

## 何が他と違うのか

最大の特徴は「すべてがプラグイン」という設計です。土台にはCordisというオープンソースのプラグイン基盤を使い、ツール、スキル、画面の部品まで、後から足したり外したりできます。製品ページでは、チャットで頼むとエージェントがプラグインを自分で書いてインストールする「Creator mode」の例として、ポモドーロタイマーを約5分で作る様子を見せています。

公式プラグインとしては、複数のエージェントで作業を分担する機能、承認の自動審査、定期実行、音声入力などが「実験的」として並んでいます。定期実行では「毎週金曜17時に今週のメモを週報にまとめる」といった指示を登録できます。開発者向けには、ツール呼び出しの中身や所要時間を1手ずつ追える画面も用意しています。

9月29日に出たv0.2.0-rc.2のリリースノートによると、デスクトップ版にはプラグイン管理用の`dsh`コマンドが同梱され、Node.jsを別に入れる必要がなくなりました。他社モデルのカタログも更新されており、DeepSeek以外のモデルもつなげます。中国の36Krは、デスクトップ版はDeepSeekのアカウントでログインするか、APIキーを入力して使う形だと報じています。

## 反応と論点

Hacker Newsでは371ポイント、191件のコメントが付きました。プラグイン基盤の設計を評価する声や、設定の移行がスムーズだという投稿がある一方で、懸念も目立ちます。

- **送信データ**: ある利用者は、デスクトップ版ではWeb版と違って利用状況の送信（テレメトリー）が初期設定で有効になっていると指摘し、止める設定を共有しました
- **プラグインの危険**: 誰でもプラグインを作れる分、悪意のあるプラグインが紛れ込む恐れを心配する声があります
- **作り**: 画面がシンプルなのにElectron製で重い、という不満も出ています
- **中国製であること**: 中国の企業が配布するバイナリを警戒する意見に対し、Claude Codeと違ってソースが公開されている点を挙げて反論する投稿もありました

DeepSeek自身も、リポジトリの安全上の注意（SAFETY.md）で強い但し書きを付けています。

:::quote https://github.com/deepseek-ai/deepseek-harness | DeepSeek Harness「SAFETY.md」
> It has not undergone a security audit and must not be treated as secure or production-ready.
セキュリティ監査を受けておらず、安全である、あるいは本番利用に耐えるものとして扱ってはいけません。
:::

READMEも「互換性を壊す変更がある」と大きく書いており、使い捨ての仮想マシンやコンテナで、最小限の権限で動かすよう勧めています。DeepSeekは前日にもHuaweiのAI半導体向けの基盤ソフトを公開しており（[DeepSeekがHuawei Ascend向け基盤ソフトを公開](/news/20261001-deepseek-huawei-ascend-opensource/)）、モデルだけでなく周辺のソフトも自前で揃える動きが続いています。

## 日本のビジネスへの影響

公開プレビューは世界向けで、日本からもダウンロードできます。製品ページは英語と中国語で、日本語対応についての記載はありません。ソフト自体は無料のオープンソースですが、36Krによるとデスクトップ版でDeepSeekのモデルを使うにはアカウントの残高かAPIキーが必要で、使った分の料金がかかります。

関係が深いのは、Claude CodeやCodexのような有料のエージェント製品を社内で比べている開発者と、情報システム部門です。MITライセンスなので、社内向けに改造して自社のモデルや社内APIにつなぐ土台として使えます。今すぐやれることは、個人の検証用マシンか仮想マシンに入れ、社内の機密を含まないリポジトリで、普段使っているコーディングエージェントと同じ作業をさせて比べることです。

注意点は3つです。DeepSeek自身が本番利用を想定しないと明言していること、デスクトップ版では利用データの送信が初期で有効だという指摘があること、DeepSeekのAPIを使えば入力が中国企業のサーバーに送られることです。業務データを扱う前に、送信設定と接続先のモデルを必ず確かめてください。主要なコーディングエージェントの比較は[AIコーディングツールのおすすめ](/best/coding/)にまとめています。
