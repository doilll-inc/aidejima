---
{
  "title": "GitHubのオープンソースAIエージェント、Androidアプリの脆弱性を24件発見",
  "description": "GitHub Security Labは、オープンソースのAIエージェントとAndroid向けの監査手順で、アプリの脆弱性を24件見つけて報告した。位置情報の漏えいやアカウント乗っ取りにつながるものもあり、手順は公開リポジトリから誰でも実行できる。",
  "date": "2026-10-01T18:32:00+09:00",
  "category": "dev",
  "tags": ["GitHub", "GitHub Security Lab", "セキュリティ", "オープンソース", "エージェント", "スマートフォン"],
  "summary": [
    "GitHub Security LabはAIエージェントとAndroid向け監査手順で、Androidアプリの脆弱性を24件見つけて報告した",
    "地図アプリOsmAndでは権限のないアプリが位置情報を抜き取れる穴、Wikipediaアプリではアカウント乗っ取りの穴が見つかった",
    "手順はMITライセンスで公開され、Codespace上で自社のリポジトリに実行できるが、Copilotの契約と人による確認が要る"
  ],
  "sources": [
    {"title": "How we found 24 Android vulnerabilities using our open source AI security agent", "publisher": "GitHub Blog", "url": "https://github.blog/security/how-we-found-24-android-vulnerabilities-using-our-open-source-ai-security-agent/", "kind": "公式発表"},
    {"title": "seclab-taskflows（README）", "publisher": "GitHub Security Lab", "url": "https://github.com/GitHubSecurityLab/seclab-taskflows", "kind": "公式ドキュメント"},
    {"title": "seclab-taskflow-agent（README）", "publisher": "GitHub Security Lab", "url": "https://github.com/GitHubSecurityLab/seclab-taskflow-agent", "kind": "公式ドキュメント"},
    {"title": "All advisories discovered with AI agents", "publisher": "GitHub Security Lab", "url": "https://securitylab.github.com/ai-agents/", "kind": "公式ドキュメント"},
    {"title": "Community-powered security with AI: an open source framework for security research", "publisher": "GitHub Blog", "url": "https://github.blog/security/community-powered-security-with-ai-an-open-source-framework-for-security-research/", "kind": "公式発表"},
    {"title": "How to scan for vulnerabilities with GitHub Security Lab’s open source AI-powered framework", "publisher": "GitHub Blog", "url": "https://github.blog/security/how-to-scan-for-vulnerabilities-with-github-security-labs-open-source-ai-powered-framework/", "kind": "公式発表"}
  ],
  "thumb_text": "Taskflow Agent",
  "share_text": "GitHub Security LabがオープンソースのAIエージェントでAndroidアプリの脆弱性を24件発見。手順は公開済み",
  "thumb_style": "3d",
  "thumb_prompt": "A smartphone laid flat with a small robot detective holding a flashlight walking across its screen, finding glowing cracks in the glass.",
  "editor_note": ""
}
---
GitHubのセキュリティ研究チームGitHub Security Labは現地時間9月28日、オープンソースのAIエージェントとAndroidアプリ向けに作った監査手順を使い、Androidアプリの脆弱性を24件見つけて報告したと公式ブログで明らかにしました。位置情報の抜き取りやアカウント乗っ取りにつながる重大なものも含まれます。手順は公開されており、自社のアプリのリポジトリにそのまま実行できます。

## 何が発表されたか

使われたのは、GitHub Security Labが2026年1月に公開した「GitHub Security Lab Taskflow Agent」です。これは、AIへの指示と作業の手順（タスクフロー）をYAMLで書き、共有して自動で実行するための枠組みです。MCP（AIが外部のツールを使うための共通規格）に対応し、MITライセンスで公開されています。

今回、研究者のKevin Stubbings氏はAndroid向けに手順を2つ足しました。1つは、攻撃者が送り込んだデータが入ってくる場所（入口）を、モバイルアプリの入口とそれ以外に分ける手順です。もう1つは、入口ごとに確認すべき脆弱性の種類を一覧で渡す手順です。たとえばIntent（Androidでアプリの部品どうしが動作を頼むためのメッセージ）を受け取る入口なら、権限を持つアプリが他者に悪用される「confused deputy」や、安全でないブロードキャストを必ず調べさせます。

:::quote https://github.blog/security/how-we-found-24-android-vulnerabilities-using-our-open-source-ai-security-agent/ | GitHub公式ブログ「How we found 24 Android vulnerabilities using our open source AI security agent」
> As these examples show, LLMs can find logic vulnerabilities with critical impact, not just generic bug classes.
これらの例が示すように、LLMはありがちな種類のバグだけでなく、重大な影響を持つ論理的な脆弱性も見つけられます。
:::

24件の多くはパストラバーサル（ファイルの場所を操作して想定外のファイルを読み書きする攻撃）のような単純なもので、重大なものは数件でした。見つかった場所は、WebView（アプリ内でWebページを表示する部品）でのスクリプト実行など、専門家が予想する場所に集まったとしています。

## 見つかった脆弱性の例

1つ目は、1,000万ダウンロードを超える地図アプリOsmAndです。外部から呼び出せる画面が、設定の取り込みに使う追加データを誰からでも受け取っていました。このため、権限を持たない別のアプリが、利用者に気づかれずに設定を書き換えられました。地図画像の取得先を攻撃者のサーバーに変えれば、利用者が見た地点の座標や、経路の出発地と目的地が送られてしまいます。

2つ目はWikipediaのAndroidアプリです。`wikipedia://`で始まるリンクの行き先を「末尾がwikipedia.orgか」だけで判定していたため、`evil-wikipedia.org`のような偽サイトを開けました。Cookieを渡す判定にも同じ誤りがあり、2つを組み合わせると、Wikimediaの全プロジェクトで使えるログイン情報を抜き取れたといいます。

## 自社のアプリで試すには

手順は公開リポジトリ「seclab-taskflows」にあります。ブログが案内する使い方は、リポジトリからCodespace（GitHubのクラウド開発環境）を起動し、対象のリポジトリ名を渡して監査スクリプトを実行するだけです。中規模のリポジトリで1〜2時間かかり、結果はSQLiteのデータベースにまとまります。脆弱性の可能性が高い行には印が付きます。

{{card:https://github.com/GitHubSecurityLab/seclab-taskflows|seclab-taskflows（監査用のタスクフロー集）|GitHub Security Lab}}

ブログはスクリプト名を`run_mobile.sh`としていますが、10月1日時点のリポジトリにあるのは`run_audit.sh`です。READMEでは、こちらがAndroidやiOSのアプリも見分けて調べると説明しています。モバイル向けの手順にはDockerが必要です。既定ではGitHub CopilotのAPIを使いますが、環境変数で別のAI APIにも切り替えられます。

## 論点

ブログは限界も率直に書いています。AIは現実にはまず起きない条件の問題や、深刻度の低い問題まで報告し、深刻度の見積もりもよく外します。保存場所の優先順位のような込み入った動きを読み違え、誤検知も出ます。

:::quote https://github.blog/security/how-we-found-24-android-vulnerabilities-using-our-open-source-ai-security-agent/ | GitHub公式ブログ「How we found 24 Android vulnerabilities using our open source AI security agent」
> Because of this, each finding should be reviewed by a security researcher with knowledge of mobile applications.
このため、見つかった問題は1件ずつ、モバイルアプリに詳しいセキュリティ研究者が確認すべきです。
:::

一方で、AIは各言語のAPIの安全な使い方と危ない使い方をよく知っており、作らせた攻撃の検証コードはほとんど手直し不要だったとしています。Web向けの監査手順では、3月の時点で80件以上の脆弱性を報告しています。AIで防御側の作業を広げる動きは各社に共通で、Googleも新モデルを[まずサイバー防御の組織に提供](/news/20261001-google-gemini-4-argon/)しています。

## 日本のビジネスへの影響

手順はMITライセンスで公開され、日本からも使えます。ただしGitHub Copilotの契約が必要で、上位モデルの利用枠を消費します。道具の呼び出しが多く、トークンを大量に使う点もブログが注意しています。

関係が深いのは、スマホアプリを自社で開発する、または外注している事業会社の開発責任者とセキュリティ担当です。まずは自社のAndroidアプリのリポジトリを1つ選び、検証用に監査を1回実行して、印が付いた行をエンジニアが確かめるのが現実的な一手です。外部から呼び出せる画面が受け取る追加データと、リンク先のドメインを「末尾一致」で判定している箇所は、AIを使わなくても今日から点検できます。

注意点は3つです。ソースコードをAIのAPIに送るため、社内規程と委託契約で許されているかを先に確かめてください。他社のオープンソースで見つけた問題は、公開する前に開発元へ非公開で報告するのが作法です。誤検知もあるため、結果をそのまま修正指示にせず、人が再現を確認してください。Copilotのプランと料金は「[コーディングAIのおすすめと料金比較](/best/coding/)」で比べられます。
