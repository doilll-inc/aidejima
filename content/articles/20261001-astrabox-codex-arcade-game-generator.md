---
{
  "title": "ASTRABOXはCodexでアーケードゲームを作るOSS、遊びながら声で作り直せる",
  "description": "オープンソースのASTRABOXが公開された。遊びたいゲームを文章か声で伝えるとCodexが作り、遊んでいる最中に声で直せる。手元のPCで動き、付属の4本のゲームはCodexにログインしなくても遊べる。",
  "date": "2026-10-01T17:49:00+09:00",
  "updated": "2026-10-01T18:51:00+09:00",
  "category": "usecases",
  "tags": ["ASTRABOX", "Codex", "活用事例", "個人開発", "ゲーム", "オープンソース"],
  "summary": [
    "GitHubでQualzzを名乗る開発者が、文章や声で頼むとCodexがアーケードゲームを作るASTRABOXをMITライセンスで公開した",
    "ASTRABOXでは遊んでいる最中に変更を頼むと、互換性のある変更なら試合の状態を保ったままゲームが差し替わる",
    "ASTRABOXの生成には自分のCodexアカウントと利用枠を使い、初期設定のモデルはGPT-6 Astra。Raspberry Piの筐体にも載せられる"
  ],
  "sources": [
    {"title": "ASTRABOX（README）", "publisher": "GitHub Qualzz", "url": "https://github.com/Qualzz/astrabox", "kind": "公式ドキュメント"},
    {"title": "Architecture", "publisher": "GitHub Qualzz", "url": "https://github.com/Qualzz/astrabox/blob/main/docs/ARCHITECTURE.md", "kind": "公式ドキュメント"},
    {"title": "Release verification — 2026-09-30", "publisher": "GitHub Qualzz", "url": "https://github.com/Qualzz/astrabox/blob/main/docs/VERIFICATION.md", "kind": "公式ドキュメント"},
    {"title": "Optional Raspberry Pi deployment", "publisher": "GitHub Qualzz", "url": "https://github.com/Qualzz/astrabox/blob/main/deploy/raspberry-pi/README.md", "kind": "公式ドキュメント"},
    {"title": "Astrabox - Open source Arcade Game Generator", "publisher": "Reddit r/LocalLLaMA", "url": "https://www.reddit.com/r/LocalLLaMA/comments/1wumex2/astrabox_open_source_arcade_game_generator/", "kind": "コミュニティ"},
    {"title": "AstraBox（同名の別プロジェクト）", "publisher": "GitHub Colton-z", "url": "https://github.com/Colton-z/AstraBox", "kind": "公式サイト"}
  ],
  "thumb_text": "ASTRABOX",
  "share_text": "文章や声で頼むとCodexがアーケードゲームを作り、遊びながら声で直せるOSS「ASTRABOX」",
  "editor_note": ""
}
---
GitHubでQualzzを名乗る開発者が協定世界時の9月30日、遊びたいアーケードゲームを文章か声で伝えるとAIが作るオープンソースのツール「ASTRABOX」を公開しました。遊んでいる最中でも、「パドルを大きくして」のように頼めばゲームが作り直されます。ローカルLLMの開発者が集まるRedditのr/LocalLLaMAでも紹介されました。

## 何を作ったか

ASTRABOXとは、ゲームを作る・遊ぶ・作り変えるをひとつの画面で行う、手元のPCで動くゲーム工房です。月面を模した3Dのメニュー画面に頭がテレビの形をしたロボットが立ち、ゲームを選んだり、ロボットに話しかけて新しいゲームを頼んだりできます。

作ったゲームは、それぞれ独立した「カートリッジ」として保存されます。タイトル画面・見た目・音楽・得点表示はゲームごとに違い、入力・スコア・リプレイ・終了・2人目の参加といった共通部分は、共有の実行環境が受け持ちます。キーボード、ゲームパッド、USBのアーケード用コントローラーに対応し、Raspberry Piと実物のアーケード筐体で動かすこともできます（必須ではありません）。

{{card:https://github.com/Qualzz/astrabox|Qualzz/astrabox|Qualzz}}

:::quote https://github.com/Qualzz/astrabox | ASTRABOX GitHub README
> Describe a game by text or voice, play it, then ask for changes while playing. Compatible edits preserve the current match; larger changes may need a restart.
ゲームを文章か声で説明して遊び、遊びながら変更を頼めます。互換性のある変更なら進行中の試合はそのまま続き、大きな変更では再起動が必要になることがあります。
:::

## どう作ったか

生成の中核は、OpenAIのコーディングエージェント「Codex」です。ASTRABOXはバージョンを固定したCodex CLIをPC上で動かし、利用者自身のCodexアカウントと利用枠でゲームを作ります。初期設定のモデルはGPT-6 Astraで、環境変数で別のモデルに切り替えられます。メニューの3DはThree.js、各ゲームはPixiJSで描かれます。

仕組みは2層です。中央のアシスタントが「新しいゲームを作る」「既存のゲームを直す」「一覧を見る」「画面を撮る」といった道具を持ち、依頼を各ゲームの担当に振り分けます。担当はゲームごとに別の会話を持つため、後から何度でも同じゲームを直せます。変更は作業用の場所で行い、静的な検査を通ったものだけを公開し、ブラウザが差し替えて動作中の状態を引き継ぎます。

## 成果

リポジトリにはポン、隕石よけ、ブロック積み、ブロック崩しの4本のゲームが入っており、Codexにログインしなくても遊べます。作者が公開した検証記録では、267件のテストが通り、最初の公開版はmacOSとLinuxの自動テストに合格したとしています。

作者は、確かめていないことも明記しています。今回の公開版では、声でゲームを作る・直す一連の流れを最初から最後まであらためて実行しておらず、実物のジョイスティックやマイク、Raspberry Pi向けのインストーラーも実機では試していないとしています。Windowsは未検証です。

## 日本で真似するなら

必要なのは、Node.js 22.13以上（または24以上）、WebGL2が動くブラウザ、Codexのアカウントです。ライセンスはMITで、効果音はCC0の素材を使っています。READMEに日本語についての記載はなく、声の聞き取りの品質はCodex側の機能に左右されると書かれています。

READMEは、サーバーをインターネットに公開しないよう警告しています。生成したゲームのコードを隔離して安全に動かす仕組みではないためです。なお、AIエージェントの実行基盤として同名の「AstraBox」という別プロジェクトもあるので、探すときはリポジトリ名に注意してください。

## 日本のビジネスへの影響

ゲーム会社や、イベント・販促の企画担当者にとっては、企画段階の試作を短時間で何本も作って遊び比べる道具になります。展示会のアーケード筐体で、来場者の注文どおりにゲームが変わる体験を見せる使い方も考えられます。

今すぐやれることは、付属の4本を手元で動かし、1本をテキストの指示で直してみることです。1回の変更でCodexの利用枠をどれだけ使うかを最初に確かめておくと、運用の見積もりが立ちます。Codexの最近の発表は[DevDay 2026のまとめ](/news/20260930-openai-devday-2026-roundup/)に、ほかのコーディングAIとの比較は[コーディングAIのおすすめ](/best/coding/)にまとめています。

注意点は、試験的な公開版であることです。Codexとの声の連携は固定したCLIの版に依存しており、別の版との互換性は保証しないと作者は書いています。生成コードはそのままでは隔離されないため、社外の人が自由に触れる形で公開する用途には向きません。
