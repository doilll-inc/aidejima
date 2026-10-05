---
{
  "title": "Pac-Benchで32のAIがパックマンを一発作成、Claude Opus 5.5が99点で首位",
  "description": "AIに1回の指示だけでパックマンを作らせて比べるPac-Benchが公開された。32作品を100点満点で採点し、Claude Opus 5.5が99点で首位、GPT-6.1 Solは91点。最下位は文法エラーの2点だった。",
  "date": "2026-10-01T18:30:00+09:00",
  "category": "usecases",
  "tags": ["Pac-Bench", "Claude Opus 5.5", "活用事例", "ベンチマーク", "コーディング", "ゲーム"],
  "summary": [
    "Pac-Benchは「1枚のHTMLでパックマンを作って」という1回の指示だけで、AIが作ったゲームを比べる試み",
    "Pac-Benchの32作品ではClaude Opus 5.5が99点で首位、GPT-6.1 Solは91点だった",
    "Pac-Benchの採点はOpus 5.5による自動プレイとコード監査で、首位のモデル自身が審査役を兼ねている"
  ],
  "sources": [
    {"title": "Pac-Man bake-off（README）", "publisher": "GitHub jonclegg", "url": "https://github.com/jonclegg/pacman-bakeoff", "kind": "公式ドキュメント"},
    {"title": "Pac-Man Bake-off: Re-test (v2)（採点の方法と結果）", "publisher": "GitHub jonclegg", "url": "https://github.com/jonclegg/pacman-bakeoff/blob/main/bench/scoring/v2.md", "kind": "公式ドキュメント"},
    {"title": "entries/meta.json（各作品の点数・時間・費用）", "publisher": "GitHub jonclegg", "url": "https://github.com/jonclegg/pacman-bakeoff/blob/main/entries/meta.json", "kind": "公式ドキュメント"},
    {"title": "PacBench（作品ギャラリー）", "publisher": "jonclegg.github.io", "url": "https://jonclegg.github.io/pacman-bakeoff/", "kind": "公式発表"},
    {"title": "Show HN: Pac-Bench – How well can models one-shot a Pac-Man game?（作者の投稿）", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=49885493", "kind": "公式発表"}
  ],
  "thumb_text": "Pac-Bench",
  "share_text": "AIに1回の指示だけでパックマンを作らせる比較。32作品中、Claude Opus 5.5が99点で首位",
  "thumb_style": "3d",
  "thumb_prompt": "A shiny yellow round arcade character chomping through a maze of glowing dots, while a row of small robots holding scorecards judges it from the side.",
  "editor_note": ""
}
---
GitHubでjonclegg名義の開発者は現地時間9月28日、AIが1回の指示だけでパックマンをどこまで作れるかを比べるサイト「Pac-Bench」を、Hacker NewsのShow HNで公開しました。32作品を100点満点で採点した結果、AnthropicのClaude Opus 5.5が99点で首位でした。

## 何を作ったか

Pac-Benchとは、AIモデルとコーディング用ツールの組み合わせに「Create a Pac-Man game in a single HTML page（1枚のHTMLページでパックマンを作って）」と指示し、できたゲームを並べたギャラリーです。やり直しや追加の指示はなく、各作品はその場で遊べます。点数・費用・時間・トークン数で並べ替えられます。

使ったツールはClaude Code、Codex、Grok Build、Cursor Cloud、Antigravityなどで、ほかのモデルはOpenRouter経由でClaude Codeから動かしています。作者はパックマンを選んだ理由を、1年前に試したときはどのモデルもうまく作れず、新モデルが出るたびに試してきたからだと説明しています。画面写真で見栄えが比べやすく、5秒遊べば出来がわかる点も挙げています。

{{card:https://jonclegg.github.io/pacman-bakeoff/|PacBench（全作品を遊べるギャラリー）|jonclegg}}

## どう採点したか

:::quote https://github.com/jonclegg/pacman-bakeoff | Pac-Man bake-off GitHub README
> Scores (out of 100) come from Opus 5.5's 2026-09-28 re-test of the live games on this site: a 90 s automated play test plus a source and maze audit.
100点満点の点数は、Opus 5.5が2026年9月28日にサイト上のゲームを再テストした結果です。90秒の自動プレイテストと、ソースコードと迷路の監査を組み合わせています。
:::

配点は操作20点、ゴースト25点、パックマンが動けなくならないか20点、迷路20点、音15点です。自動プレイでは画面の色からパックマンとゴースト4体の位置を追い、迷路は行き止まりや取れないエサがないかを経路探索で調べました。異常はブラウザで1件ずつ確認し直し、上位3作品の順位は音への意見を受けて見直したと記録されています。

## 成果（作者の公表結果）

上位7作品は次の通りです（費用は作者が各ツールの記録などから見積もった値）。

| モデル（ツール） | 点数 | 時間 | 費用 |
|---|---|---|---|
| Claude Opus 5.5（Claude Code） | 99 | 9.3分 | 1.99ドル |
| Claude Fable 5.1（Claude Code） | 96 | 14.8分 | 5.87ドル |
| Claude Sonnet 5.5（Claude Code＋OpenRouter） | 95 | 14.4分 | 1.61ドル |
| Claude Fable 5（Claude Code＋OpenRouter） | 95 | 37.0分 | 17.28ドル |
| Grok 4.7（Grok Build） | 94 | 36.5分 | 1.69ドル |
| GPT-6.1 Sol（Codex） | 91 | 8.6分 | 0.51ドル |
| GPT-5.6 Sol（Codex） | 90 | 4.9分 | 0.72ドル |

最下位はMiniMax M3の2点で、文法エラーで画面が真っ白でした。同じ会社でも世代差は大きく、Claude Opus 4.8は28点、Opus 5は58点、Claude Sonnet 5は18点です。最も多い失敗は、ゴーストが止まるか巣から出てこない不具合で、11作品に見られました。作者はHNで、Opus 5.5について「指摘することが何もない初めてのモデル」と書いています。

## 反応と論点

HNでは、Opus 5.5の作品はゴーストごとに追いかけ方が違うなど原作にほぼ忠実だと評価する声が続きました。一方、パックマンの模倣作は学習データに大量にあるはずで、記憶の再現を測っているだけではないか、指示が短すぎるという批判も出ています。

採点役のOpus 5.5が首位になっている点にも注意が要ります。また9月30日に公開された自動計測の手順では、1文ではなく、迷路やゴースト4体などの最低条件を並べた指示書を渡す形になっています。

## 日本のビジネスへの影響

ギャラリーは無料でブラウザから遊べますが、画面は英語です。リポジトリにはライセンスの記載がなく、作品やコードの再利用条件は示されていません。

関係が深いのは、社内で使うコーディングAIを選ぶ開発チームの責任者です。同じ会社のモデルでも18点から99点まで開きがあり、費用と時間の差も大きいことがわかります。GPT-6.1 Solは91点を約0.5ドル・9分弱で出しており、価格重視の選択肢になります。

今すぐやれることは、自社の小さな定型タスクを1つ決め、複数のAIに同じ指示で一発で作らせ、目視でなく自動テストで比べることです。注意点は、各モデル1回の試行で、何度も走らせたときのばらつきは示されていないことです。有名なゲームの再現が実務の力を表すとも限りません。モデルの使い方は[Claude Opus 5.5のプロンプトの書き方](/news/20260930-claude-opus-5-5-prompting-guide/)、選び方は[コーディングAIの比較](/best/coding/)にまとめています。
