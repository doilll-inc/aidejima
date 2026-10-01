---
{
  "title": "PaperMonoは冷蔵庫に貼る電子ペーパーの買い物リスト、コードはClaude Code製",
  "description": "開発者のSeamus Cawley氏が、M5Stackの電子ペーパー端末PaperMonoを冷蔵庫の買い物リストにするコードを公開した。約2,400行のC++も手書きせずClaude Codeに作らせ、売り場分けにもClaudeを使う。",
  "date": "2026-10-01T18:27:00+09:00",
  "category": "usecases",
  "tags": ["PaperMono", "Claude Code", "活用事例", "個人開発", "作ってみた", "オープンソース"],
  "summary": [
    "Seamus Cawley氏が、65ドルの電子ペーパー端末PaperMonoを冷蔵庫の買い物リストにするコードを公開した",
    "PaperMonoの買い物リストは、約2,400行のC++も手書きせずClaude Codeで作ったと本人が説明している",
    "サーバーは初めて見た品目名をClaude Code CLIに渡して売り場ごとに振り分け、手で直した結果は以後も保つ"
  ],
  "sources": [
    {"title": "PaperMono Shopping List（README）", "publisher": "GitHub seamusc", "url": "https://github.com/seamusc/papermono-shopping-list", "kind": "公式ドキュメント"},
    {"title": "Server（Auto-sorting with Claude）", "publisher": "GitHub seamusc", "url": "https://github.com/seamusc/papermono-shopping-list/blob/main/docs/server.md", "kind": "公式ドキュメント"},
    {"title": "Design notes", "publisher": "GitHub seamusc", "url": "https://github.com/seamusc/papermono-shopping-list/blob/main/docs/design-notes.md", "kind": "公式ドキュメント"},
    {"title": "Show HN: PaperMono, e-ink fridge magnet shopping list with mobile web page（作者の投稿）", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=49875801", "kind": "公式発表"},
    {"title": "PaperMono（製品ドキュメント）", "publisher": "M5Stack", "url": "https://docs.m5stack.com/en/core/PaperMono", "kind": "公式ドキュメント"},
    {"title": "M5PaperMono with LoRa & NFC（公式ストア）", "publisher": "M5Stack", "url": "https://shop.m5stack.com/products/m5papermono-with-lora-nfc-800x480-3-97-eink-display", "kind": "公式ドキュメント"}
  ],
  "thumb_text": "PaperMono",
  "share_text": "冷蔵庫に貼る電子ペーパーの買い物リスト。コードは全部Claude Codeに書かせ、売り場分けもClaudeが担当",
  "editor_note": ""
}
---
開発者のSeamus Cawley氏は現地時間9月28日、M5Stackの電子ペーパー端末「PaperMono」を冷蔵庫に貼る買い物リストに変えるソフトを、Hacker NewsのShow HNで公開しました。約2,400行のC++を含むコードは手で書かず、AnthropicのコーディングAI「Claude Code」に作らせたと本人が説明しています。新しい品目をどの売り場に入れるかの判断にもClaudeを使います。

## 何を作ったか

PaperMonoとは、ESP32-S3マイコンと3.97インチ（480×800）のタッチ式電子ペーパーを組み合わせたM5Stackの小型端末です。公式ストアの価格は65ドルで、10月1日時点では在庫切れでした。

Cawley氏の「PaperMono Shopping List」は、この端末を冷蔵庫に貼って家族の買い物リストにします。品目は売り場ごとに、店内を歩く順に並びます。端末では品目をタップして消したり画面のキーボードで足したりでき、ほかの家族はスマホのブラウザから追加します。電波の届かない店内でも確認やチェックができ、編集は次の同期まで端末に保存されます。

:::quote https://news.ycombinator.com/item?id=49875801 | Seamus Cawley氏のShow HN投稿（Hacker News）
> Fully vibe-coded with Claude Code, I didn't hand-write this. I wanted to see how Claude would get on with building something useful for a new hardware device.
すべてClaude Codeでバイブコーディングしたもので、私は手で書いていません。新しいハードウェア向けに役立つものを作らせたら、Claudeがどこまでやれるかを見たかったのです。
:::

## どう作ったか

構成は、端末のファームウェア（C++）、FastAPIとSQLiteで作った小さなサーバー、スマホ向けのWeb画面の3つです。端末は電池を長持ちさせるため、同期のときだけWi-Fiにつなぎます。同期の間隔はサーバーが決め、「朝夕だけ1時間ごと」などの設定をWeb画面で選べます。

AIはコードを書かせただけでなく、動作の中にも入っています。サーバーは初めて見た品目名を、売り場の一覧と一緒にClaude Code CLIへ渡し、入れる売り場を答えさせます。答えは保存されるため、同じ名前でClaudeを呼ぶのは1回だけです。失敗すれば「未分類」に入ります。

:::quote https://github.com/seamusc/papermono-shopping-list | PaperMono Shopping List GitHub README
> The first time the server sees a name, it can send it to Claude to file it under an aisle. If you move an item to a different aisle by hand, that correction sticks.
サーバーは初めて見る品目名をClaudeに送り、売り場に振り分けさせられます。手で別の売り場に移せば、その修正は以後も保たれます。
:::

Cawley氏はHNのコメントで、簡単なMCPサーバー（AIが外部のツールを操作するための仕組み）も用意し、週の献立づくりにAIを使うこともあると書いています。電源やタッチ、画面の制御部分は、同じ端末向けのオープンソースMonoMeshから流用し、どこを借りたかを設計メモに一覧で載せています。

{{card:https://github.com/seamusc/papermono-shopping-list|seamusc/papermono-shopping-list|Seamus Cawley}}

## 成果（作者の公表値）

家族が毎日の買い物に使っており、自作の家庭用プロジェクトでは初めてのことだとCawley氏は書いています。電池の持ちは、まだ使い始めたばかりで数字は出せないとしています。

設計メモには、開発中に見つかった不具合も残っています。同期でデータが入れ替わると画面のキーボードが解放済みのメモリを参照する不具合や、低電圧で電源を切る処理が実装されていたのにどこからも呼ばれていなかった不具合などです。HNでは「AIで自分専用のファームウェアが作れる」と歓迎する声と、「付箋で十分」「AI製と知って興味が失せた」という声の両方がありました。

## 日本のビジネスへの影響

READMEに日本語対応の記載はなく、日本語の品目名を端末で表示できるかは試す必要があります。端末は公式ストアで買えますが、在庫が戻るのを待つ必要があります。

関係が深いのは、店舗や工場向けの専用端末を試作したい開発者と企画担当者です。補充メモや作業手順など「スマホを開かずに見たい小さな情報」を電子ペーパーに出す試作の手本になります。AIで新しいハードを動かした例として、電源制御の手順や不具合の記録まで公開されている点も参考になります。

最初の一手は、サーバーだけを自動分類なしで動かし、Web画面で売り場の並びを自社の店に合わせて試すことです。端末に書き込む前には、端末ごとの校正データが入ったフラッシュを必ずバックアップするよう手順書が求めています。

注意点は3つです。ライセンスはGPLv3で、改変して配布する場合はソースの公開が必要です。サーバーには認証がなく、社内LANか認証付きの経路の内側で使う前提です。自動分類を有効にすると、品目名と売り場名がClaude Code経由でAnthropicに送られます。コーディングAIの選び方は[コーディングAIの比較](/best/coding/)にまとめています。
