---
{
  "title": "Claude Opus 5.5のプロンプトの書き方、Anthropic公式ガイドの要点と変更点",
  "description": "AnthropicはClaude Opus 5.5向けのプロンプト公式ガイドを公開している。思考量はeffortで決め、長時間エージェントの途中停止や貼り付け文の扱いには専用の書き方を勧める。Opus 5から変わった点を実務目線で整理した。",
  "date": "2026-09-30T20:28:00+09:00",
  "updated": "2026-10-01T16:00:00+09:00",
  "category": "dev",
  "tags": ["Anthropic", "Claude Opus 5.5", "プロンプト", "API", "エージェント", "開発者"],
  "summary": [
    "標準のeffortはOpus 5の「high」から「medium」に。思考はオフにできず、effortが主な調整手段",
    "「考えてから答えて」などの指示は削除を推奨。推論を本文に書かせると拒否される場合も",
    "無人エージェントの途中停止、貼り付け文への仕込み指示、画一的なデザインに個別の対策を示した"
  ],
  "sources": [
    {"title": "Prompting Claude Opus 5.5", "publisher": "Anthropic", "url": "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5"},
    {"title": "What's new in Claude Opus 5.5", "publisher": "Anthropic", "url": "https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5"},
    {"title": "Effort", "publisher": "Anthropic", "url": "https://platform.claude.com/docs/en/build-with-claude/effort"},
    {"title": "Claude Opus 5.5", "publisher": "Anthropic", "url": "https://www.anthropic.com/claude-opus-5-5"},
    {"title": "Claude Developers の投稿（Opus 5.5で最初に試すこと）", "publisher": "X @ClaudeDevs", "url": "https://x.com/ClaudeDevs/status/2102491840612380934"},
    {"title": "Simon Willison の投稿", "publisher": "X @simonw", "url": "https://x.com/simonw/status/2102546103984079131"},
    {"title": "Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, and a new price war", "publisher": "Simon Willison's Weblog", "url": "https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/"},
    {"title": "Prompting Claude Opus 5.5", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=49874728"}
  ],
  "editor_note": ""
}
---
Anthropicは、9月22日に公開した「Claude Opus 5.5」向けのプロンプト公式ガイド「Prompting Claude Opus 5.5」を開発者向けドキュメントで公開しています。基本の立場は、Claude Opus 5で使っていたプロンプトは書き換えなくてもおおむね動く、というものです。そのうえで、思考量の決め方とエージェント運用で、前の世代とは違う書き方を勧めています。

## 何が発表されたか

前提として、Claude Opus 5.5のAPI料金は100万トークンあたり入力4ドル・出力20ドルで、Opus 5の5ドル・25ドルから2割下がりました。出力の速さはOpus 5より30%以上速く、同じ作業をより少ないトークンで終えるとAnthropicは説明しています。

ガイドとAPIの変更点のうち、実務に効くものをまとめると次のとおりです。

| 項目 | Opus 5 | Opus 5.5 |
|---|---|---|
| effortの標準値 | high | medium |
| 思考（thinking）のオフ | high以下で可能 | 不可（指定すると400エラー） |
| ツールの強制呼び出し | 可能 | 不可（`tool_choice`のany・toolはエラー） |
| ツール呼び出しの合間の進捗メモ | textブロックで返る | thinkingブロックで返り、標準設定では中身が空 |

### 1. 思考量はeffortで決める

effort（どれだけ考えてトークンを使うかの設定）が、品質・速度・費用を調整する主な手段になりました。

:::quote https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5 | Anthropic公式ドキュメント「Prompting Claude Opus 5.5」
> Effort is the main control for how much Claude Opus 5.5 thinks, and because thinking is always on, it's the first setting to adjust when trading off intelligence, latency, and cost.
effortは、Claude Opus 5.5がどれだけ考えるかを決める主な調整手段だ。思考は常にオンなので、知能・遅延・費用のバランスを取るときに最初に調整すべき設定になる。
:::

Anthropicの社内評価では、コーディングや知的作業の課題で、Opus 5.5のmediumがOpus 5のhighと同等以上だったといいます。一方で、同じ段階でもOpus 5.5の方が多く考える傾向があり、特にxhighとmaxで顕著です。

ガイドは、前モデルの設定を持ち越さず自社の評価で複数段階を試すこと、思考分を見込んで`max_tokens`を大きく取ることを勧めています。思考を減らしたいときは、プロンプトで指示するよりeffortを下げる方が確実だとしています。

### 2. 「よく考えて」系の指示は外す

チャット用のシステムプロンプトに「答える前によく考えて」と書いている場合、外すことを検討するよう勧めています。社内テストでは、外しても品質を落とさずに返答が早くなりました。推論を回答本文に書き出させる指示も削除の対象です。この指示は新しい拒否区分の対象になり得るため、推論は要約された思考ブロックから読むよう案内しています。

Anthropicの開発者向けアカウントも公開日にXで、Opus 5.5で最初に試すことの一つとして「think carefully（よく考えて）」の指示を外すよう呼びかけました。常に先に考えるため不要だという理由です。

{{x:https://x.com/ClaudeDevs/status/2102491840612380934}}

### 3. 無人エージェントの途中停止を防ぐ

Opus 5.5は長い作業の途中で進捗を報告し、そこでターンを終えることがあります。自動で回すエージェントでは、これを「完了」と誤認して止まってしまいます。ガイドの基本の考え方は次の一文です。

:::quote https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5 | Anthropic公式ドキュメント「Prompting Claude Opus 5.5」
> Treat a text-only end of turn as a report rather than as proof the task is done.
テキストだけで終わったターンは、作業完了の証拠ではなく、報告として扱うこと。
:::

ガイドは、残タスクをチェックリストで管理し、未完了なら続行を促す短いメッセージを送ることを勧めます。自動の続行は2〜3回までに抑え、本当に行き詰まった場合は人が確認できるようにします。

### 4. その他の要点

- **複数アプリをまたぐ業務**：メールや表計算、CRMを行き来するエージェントには、手を動かす前に関係しそうな資料を広く確認させる一文が効く
- **時間の目安**：複数のエージェントを使う場合、経過時間と予算（例：`elapsed 340s / 1200s`）を毎回伝えると早く終わりやすい
- **貼り付けた文章の区別**：ユーザーが貼った文章を、ランダムなIDを付けたタグで囲む。中に紛れた指示に従わないよう指示でき、プロンプトインジェクション（外部の文章に仕込まれた命令）への対策になる
- **デザイン指示**：「AIっぽさを避けて」では別の定番に置き換わるだけ。避けたい配色やラベルの形などを具体的に列挙する

## 反応と論点

開発者のSimon Willison氏は公開初日のブログで、最上位のmaxで試したところ、思考だけで出力上限の12万8,000トークンを使い切って回答が返らなかったと報告しました。2回試して2回とも失敗し、1回あたり2.56ドルと20分近くかかったといいます。xhighとmaxは効果を測ってから使う、というガイドの注意とも重なります。Willison氏はこの記事をXでも紹介しています。

{{x:https://x.com/simonw/status/2102546103984079131}}

9月28日にHacker Newsに投稿されたガイドには200ポイント超、約220件のコメントが付きました。Willison氏は貼り付け文のタグについて、以前はこの種の防御に懐疑的だったが、Anthropicが学習させているなら機能するかもしれないとコメントしています。一方で、プロンプトの作法が数か月ごとに変わることへの不満や、Opus 5.5の文章が長すぎるという声、思考の中身を読めないことへの批判も出ました。新バージョンのソフトに移行ガイドが付くのと同じだ、と冷静に受け止める意見もあります。

## 日本のビジネスへの影響

Claude Opus 5.5はClaude APIのほか、Amazon Bedrock、Google Cloud、Microsoft Foundryで使え、日本からも利用できます。ガイドは特定の言語に限った内容ではなく、日本語のプロンプトにも応用できます。

移行時にまず確認したいのは次の4点です。

- **エラーになる設定を外す**：思考オフや思考量の手動指定、`tool_choice`でのツール強制呼び出しは400エラーになる
- **effortを明示して比べる**：未指定だとmediumで動く。lowからhighまで自社の業務で試し、1件あたりの実費で比べる
- **古い「考えさせる」指示を消す**：思考を促す指示や推論を書き出させる指示は、遅延や拒否の原因になる
- **画面表示を確認する**：進捗メモを利用者に見せているアプリは、表示設定を変えないと作業中に何も出なくなる

マーケティングの現場で問い合わせメールや口コミを貼り付けて要約させる場合は、貼り付け部分をタグで区別するだけで、文中の指示に引きずられる事故を減らせます。LPやバナーの試作でAIに下書きを作らせる場合も、「おしゃれに」ではなく、使わない色や装飾を具体的に書く方が狙いに近づきます。
