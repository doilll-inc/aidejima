---
{
  "title": "Cursorの使い方と料金、AIに指示してプログラムを作る開発ツール 無料から試せて有料は月8ドルから",
  "description": "Cursorは、AIに文章で頼むとファイルを読んでプログラムを書き換えてくれる開発ツール。10月からGrokやXと共通の料金プランになり、有料は月8ドルから。ClaudeやGPTを使うなら月30ドルのPremium以上が必要になる。10月25日時点の公式情報で整理した。",
  "date": "2026-10-25T02:10:00+09:00",
  "category": "dev",
  "format": "howto",
  "tags": ["Cursor", "Grok", "SpaceXAI", "使い方", "料金", "コーディング"],
  "summary": [
    "Cursorは、AIに作りたいものを文章で頼むと、ファイルを読んでプログラムを書き、直した箇所を見せてくれる開発ツール",
    "10月からGrok・Xと共通の「The X Subscription」で売られ、無料版のほか有料は月8ドル・30ドル・100ドル・200ドルの4段階",
    "月8ドルのPlusで使えるのはGrokなど自社のAIだけ。ClaudeやGPTを使うには月30ドルのPremium以上で、別に使った分の料金がかかる"
  ],
  "sources": [
    {"title": "Models & Pricing", "publisher": "Cursor Docs", "url": "https://cursor.com/docs/models-and-pricing", "kind": "公式ドキュメント"},
    {"title": "Quickstart", "publisher": "Cursor Docs", "url": "https://cursor.com/docs/get-started/quickstart", "kind": "公式ドキュメント"},
    {"title": "Cursor Agent", "publisher": "Cursor Docs", "url": "https://cursor.com/docs/agent/overview", "kind": "公式ドキュメント"},
    {"title": "料金", "publisher": "Cursor", "url": "https://cursor.com/ja/pricing", "kind": "公式ドキュメント"},
    {"title": "What is The X Subscription?", "publisher": "Cursor Help", "url": "https://cursor.com/help/the-x-subscription/overview", "kind": "公式ドキュメント"},
    {"title": "Legacy Cursor plans", "publisher": "Cursor Docs", "url": "https://cursor.com/docs/account/pricing/legacy-cursor-plans", "kind": "公式ドキュメント"},
    {"title": "Data Use & Privacy Overview", "publisher": "Cursor", "url": "https://cursor.com/data-use", "kind": "公式ドキュメント"},
    {"title": "Cursor for iOS", "publisher": "Cursor Docs", "url": "https://cursor.com/docs/cloud-agent/mobile", "kind": "公式ドキュメント"}
  ],
  "thumb_prompt": "A cozy home desk at night where a laptop screen shows lines of code rewriting themselves, while a person's hand rests not on the keyboard but on a cup of tea, with a handwritten sticky note of plain-language instructions stuck to the screen.",
  "thumb_style": "photo",
  "thumb_text": "Cursor 使い方",
  "share_text": "Cursorの使い方と料金。AIに頼むとプログラムを書く開発ツール、有料は月8ドルから。ClaudeやGPTを使うなら月30ドル以上",
  "editor_note": ""
}
---
Cursorとは、パソコンに入れて使う開発ツールで、作りたいものや直したいところを文章で頼むと、AIがファイルを読んでプログラムを書き換え、変えた箇所を見せてくれます。無料版から試せ、有料プランは月8ドルからです。10月からは対話AIのGrokやSNSのXと共通の料金プランで売られており、ClaudeやGPTなど他社のAIを使うなら月30ドルのPremium以上が必要です。この記事では10月25日時点の公式ドキュメントと料金ページで、使い方と料金を整理します。

## 何ができるか

Cursorの中心は「Agent（エージェント）」という機能です。エージェントとは、指示を受けて自分でファイルを調べ、編集し、コマンドを実行しながら作業を進めるAIのことです。公式ドキュメントによると、Agentにできることは次のとおりです。

- **プログラムの読み解き**: フォルダの中身を検索して読み、全体の仕組みを要約します。初めて見るプログラムの把握に向いています
- **書き換えと確認**: ファイルを編集し、テストなどのコマンドを実行して結果を確かめます。ブラウザを操作して画面の見た目を確かめることもできます
- **計画モード**: 大きな変更では、すぐに書き始めずに関係するファイルを調べ、質問をして、計画を出してから承認を待ちます
- **巻き戻し**: 大きな変更の前に自動で保存点（チェックポイント）を作るので、AIの作業が見当違いなら元に戻せます

月30ドルのPremium以上では、Cursorの会社側のサーバーでAIを動かし続ける「クラウドエージェント」も使えます。iPhone・iPad用のアプリから作業を頼み、進み具合を確かめることもできます。

## 料金とプラン

Cursorは10月、Grokを開発するSpaceXAI（旧xAI）の「The X Subscription」の一部になりました。公式ドキュメントはこう説明しています。

:::quote https://cursor.com/docs/models-and-pricing | Cursor Docs「Models & Pricing」
> Cursor is sold as part of The X Subscription, one subscription for Grok, Cursor, and X. Paid plans include a weekly pool of usage for Cursor models, shared across Grok and Cursor.
CursorはThe X Subscriptionの一部として販売しています。Grok、Cursor、Xを1つにまとめた契約です。有料プランにはCursorのAIを使える週ごとの利用枠があり、GrokとCursorで共有します。
:::

10月25日時点の個人向けプランは次のとおりです（税抜き。日本語の料金ページでもドル表示です）。

| プラン | 月額 | 年払い | 利用枠 | ClaudeやGPTなど他社のAI |
|---|---|---|---|---|
| Free | 0ドル | ― | 少なめ | 使えない |
| Plus | 8ドル | 80ドル | 基本 | 使えない |
| Premium | 30ドル | 300ドル | Plusの4倍 | 使った分を別払い |
| Super | 100ドル | 1,000ドル | Plusの15倍 | 使った分を別払い |
| Ultra | 200ドル | 2,000ドル | Plusの50倍 | 使った分を別払い |

{{card:https://cursor.com/ja/pricing|料金|Cursor}}

料金を選ぶときに押さえたい点は3つです。

- **月8ドルのPlusはGrok専用**: 使えるのはGrok 4.7など自社系のAIとCursor独自のComposer 2.5だけで、クラウドエージェントもありません。Grokのアプリも同じ利用枠で使えます
- **他社のAIは別料金**: ClaudeやGPTはプランの利用枠に含まれず、Premium以上で、事前に入金した残高から各社の公開価格（API定価）で差し引かれます
- **利用枠は毎週リセット**: 1日に使いすぎても1か月分がなくなることはなく、翌週に戻ります。足りなければ追加購入するか、リセットを待ちます

チーム向けは1人あたり月30ドル・100ドル・200ドルから選ぶTeamsと、個別見積もりのEnterpriseがあります。以前の月20ドルのProなどを契約している人は、そのままの料金で使い続けられます。新しいプランへの切り替えは任意ですが、一度切り替えると元に戻せません。

## 始め方

公式のクイックスタートに沿うと、最初の1回は次の4ステップです。

1. **入れる**: cursor.comからダウンロードします。Mac（macOS 12以降）、Windows（10以降）、Linuxに対応しています
2. **サインインしてフォルダを選ぶ**: 作業したいフォルダを開きます
3. **説明させる**: Agentを開き（Macは「Cmd＋I」）、「このプログラムの仕組みを説明して」と頼みます
4. **小さく直させて確かめる**: 小さな改善を頼み、変更点の画面（差分）を見て、問題がなければ受け入れます

公式は、最初の作業には失敗しても影響が小さいものを選ぶよう勧めています。

:::quote https://cursor.com/docs/get-started/quickstart | Cursor Docs「Quickstart」
> Good first tasks are low risk, like improving some copywriting or fixing small UI issues.
最初の作業には、文言の手直しや画面の小さな不具合の修正のように、危険の少ないものが向いています。
:::

## 仕事での使いどころ

- **マーケター・Web担当者**: 自社のランディングページ（広告から誘導する1枚もののページ）の文言差し替えや、キャンペーン用の簡単なページの作成。変更点が画面で見えるので、エンジニアに渡す前の下書きになります
- **事業企画・営業企画**: 表計算では重くなった集計を、小さなプログラムにして自動化する。計画モードで手順を出させてから作らせると、何をするのかを理解したうえで進められます
- **エンジニア**: 初めて担当するプログラムの全体像をつかむ、テストを書かせて実行まで任せる、といった使い方が公式の想定です

## 日本のビジネスへの影響

- **使えるか**: 日本から申し込めて、料金ページと公式ドキュメントには日本語版があります。料金はドル建てで、税は別にかかります
- **誰に効くか**: 毎日プログラムを書くエンジニアに加え、「ちょっとしたページや集計ツールを自分で作りたい」マーケターや企画担当者にも使い道があります。ほかのAIコーディングツールとの比較は[コーディングAIのガイド](/best/coding/)にまとめています
- **今すぐやれること**: 無料版を入れ、手元にある過去のWebページや集計ファイルのフォルダを開いて「何をしているか説明して」と頼んでみてください。仕組みの説明が役に立つかで、有料に進むかを判断できます
- **注意点**: 会社のコードや資料を扱うなら、設定で「プライバシーモード」をオンにしてください。オフのままだと、コードや指示文がCursorのAIの学習に使われることがあると公式に書かれています。また、Claudeなど他社のAIを使い続けると、月額とは別の従量料金がふくらみます。Grokと利用枠を共有する仕組みは「[GrokとCursor、Xの有料機能が月8ドルからの1プランに](/news/20261013-x-subscription-grok-cursor/)」でも紹介しています
