---
{
  "title": "Claude Codeに「Mods」、TypeScriptで画面も動作も作り替えられる拡張機能",
  "description": "AnthropicはClaude Code 2.1.287で、自作のJavaScriptやTypeScriptで画面や動作を作り替えられる「Mods」を追加した。ツール呼び出しの差し止めなどができる一方、サンドボックスの外で動くため入手元の見極めが要る。",
  "date": "2026-10-03T19:00:00+09:00",
  "category": "dev",
  "tags": ["Anthropic", "Claude Code", "Mods", "エージェント", "コーディング", "開発者"],
  "summary": [
    "AnthropicはClaude Code 2.1.287で、JavaScriptやTypeScriptの関数で動作や画面を変えられる「Mods」を既定で有効にした",
    "Modsはツール呼び出し・プロンプト・画面の描画などのイベントに割り込み、見るだけ・書き換える・代わりに応える、の3通りで介入できる",
    "Modsは利用者と同じ権限で動きサンドボックスの対象外のため、Anthropicは信頼できる作者のものだけを入れるよう求めている"
  ],
  "sources": [
    {"title": "Mods overview", "publisher": "Claude Code Docs", "url": "https://code.claude.com/docs/en/plugins/mods/overview", "kind": "公式ドキュメント"},
    {"title": "Getting started with Claude Code mods", "publisher": "claude.dev Blog（Anthropic）", "url": "https://claude.dev/blog/getting-started-with-claude-code-mods/", "kind": "公式発表"},
    {"title": "ClaudeDevs の投稿（Modsの発表）", "publisher": "X @ClaudeDevs", "url": "https://x.com/ClaudeDevs/status/2105721434807083061", "kind": "X投稿"},
    {"title": "ClaudeDevs の投稿（You Should Know）", "publisher": "X @ClaudeDevs", "url": "https://x.com/ClaudeDevs/status/2106118517447876618", "kind": "X投稿"},
    {"title": "Lydia Hallie の投稿", "publisher": "X @lydiahallie", "url": "https://x.com/lydiahallie/status/2105737466254598362", "kind": "X投稿"},
    {"title": "anthropics/claude-code-playground（サンプルのMods）", "publisher": "GitHub Anthropic", "url": "https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods", "kind": "公式ドキュメント"},
    {"title": "Claude Code's new Mods system lets developers rewrite the AI coding tool from the inside", "publisher": "The Decoder", "url": "https://the-decoder.com/claude-codes-new-mods-system-lets-developers-rewrite-the-ai-coding-tool-from-the-inside/", "kind": "報道"},
    {"title": "Claude Code 2.1.287 adds mods, and Anthropic says they can read your API key", "publisher": "MIXED", "url": "https://mixed-news.com/en/claude-code-2-1-287-mods-not-sandboxed-api-key/", "kind": "報道"}
  ],
  "thumb_text": "Claude Code Mods",
  "share_text": "Claude Codeに「Mods」。TypeScriptの関数でツール呼び出しを止めたり、独自の画面を足したりできる",
  "editor_note": ""
}
---
Anthropicは現地時間10月1日、AIのコーディングエージェント「Claude Code」に、利用者が自分のコードで画面や動作を作り替えられる「Mods」を追加しました。JavaScriptかTypeScriptで書いた関数が、ツールの呼び出しやプロンプトの送信、画面の描画といったイベントに割り込みます。Claude Code 2.1.287以降で、既定で有効になっています。

## 何が発表されたか

Modsとは、Claude Codeのプロセスの中で動くイベント処理の関数を、プラグインとして配布・導入する仕組みです。Anthropicの開発者向けアカウントは、Modsで動作の変更、画面のカスタマイズ、自作の機能への差し替えができると投稿しました。少しのTypeScriptで書くことも、Claudeに作らせることもできるとしています。

{{x:https://x.com/ClaudeDevs/status/2105721434807083061}}

これまでも、設定ファイルに書くフック、スキル、ステータスライン、MCPサーバーで機能を足すことはできました。ただ、どれもClaude Codeの外から働きかける仕組みです。Anthropicの解説ブログは、Modsとの違いを次のように説明しています。

:::quote https://claude.dev/blog/getting-started-with-claude-code-mods/ | claude.dev Blog「Getting started with Claude Code mods」
> Mods go further: they can rewrite or replace what Claude Code does, and draw custom UI.
Modsはさらに踏み込み、Claude Codeの動作を書き換えたり置き換えたりでき、独自の画面も描ける。
:::

仕組みの核は、イベントが処理される直前に関数が呼ばれることです。関数はそのイベントをそのまま通すか、中身を書き換えて通すか、自分で応えて本来の処理を止めるかを選べます。公式ドキュメントとブログを合わせると、使い道は3つの方向に分かれます。

- **動作を変える**: ツール呼び出しを実行前に止めて利用者に確認する、ツールを動かさずに答えを返す、1回のリクエストだけ別のモデルに送る
- **コマンドを足す**: `/` で始まる自作コマンドを、Claudeを介さず、作業中でもすぐ実行する
- **画面を変える**: 会話の横にペイン、入力欄の上に帯を追加する。ツール呼び出しの行やスピナーなど、Claude Code自身が描く部分も置き換えられる（ただし許可を求める確認画面は変えられない）

Anthropic自身も、既存の `/diff` コマンドや `AGENTS.md` を読み込む機能をModsとして作り直しています。

## 試せるサンプルと新しい公式Mod

AnthropicはGitHubの `claude-code-playground` に、そのまま試せる3つのサンプルを公開しました。コンテキストの埋まり具合を天気予報のように表示する「Token Weather」、`rm -rf` や強制プッシュなど危ないコマンドを止めて影響範囲を見せる「Blast Radius」、直前のターンのファイル編集を1つずつ再生する「Replay Theater」です。

{{card:https://code.claude.com/docs/en/plugins/mods/overview|Mods overview|Claude Code Docs}}

翌2日には、組み込みのMod「You Should Know」も加わりました。Claudeが長い作業をしている間に別のエージェントが出力を見張り、利用者が見落としそうな情報を入力欄の上に知らせます。既定ではオフで、`/plugin enable cc-plugin-you-should-know@builtin` で有効にします。

{{x:https://x.com/ClaudeDevs/status/2106118517447876618}}

Modsが画面を描けるのは、ターミナルの `claude` とデスクトップアプリのCodeタブです。VS Code拡張のチャット画面や `claude -p`、Agent SDKでは、関数は動きますが画面には何も描かれません。

## 反応と論点

Lydia Hallie氏はXで、Modsを「Claude Codeのミドルウェア」と表現しました。ツール呼び出しやモデルへのリクエストに割り込んで、実際に起きることを変えられる点を強調しています。

一方で、MIXEDなどの海外メディアは安全面を大きく取り上げました。Modsはサンドボックスの対象外で、利用者と同じ権限でファイルの読み書き、プログラムの起動、ネットへの接続ができます。公式ドキュメントも、環境変数や設定ファイルにあるAPIキーを読めること、`ask` ルールで確認が出るはずのツール呼び出しを自動で承認できることを明記しています。

対策として、導入前に `claude plugin validate` でModが扱うイベントと呼び出す機能を一覧にできます。組織の管理者は、管理設定で会社が配ったMod以外を読み込ませないようにできます。組織が管理する設定を、利用者が入れたModから守る組み込みMod「sec-default」もあります。

## 日本のビジネスへの影響

Claude Codeを使っていれば、追加料金なしで今日から使えます。ドキュメントは英語ですが、作りたいModを日本語で説明してClaudeに書かせることもできます。

効くのは、チームでClaude Codeを使う開発者と、その導入を管理する情報システム部門です。たとえば「本番の設定ファイルへの書き込みは必ず止める」「社内のコーディング規約をプロンプトに自動で足す」といった社内ルールを、各自の運用任せではなく仕組みとして配れます。今すぐやれることは、`claude --version` で2.1.287以降かを確かめ、Blast Radiusを `--plugin-dir` で1セッションだけ読み込んで、危ないコマンドがどう止まるか見ることです。

注意点は、Modは「便利な見た目の拡張」ではなく、手元で動くプログラムだということです。他人が公開したModを入れる前には、ソースを読んで `claude plugin validate` の結果を確かめます。会社として使うなら、まず管理設定で読み込めるModを社内配布のものに限ってから広げるのが安全です。Blast Radiusの説明にあるとおり、こうした見張り役は権限設定の代わりにはならず、確実に止めたい操作は許可ルールで禁止します。コーディングAIの選び方は[コーディングAIのおすすめ](/best/coding/)にまとめています。
