---
{
  "title": "Lathoaは子どもがAIのわざとの誤りを探す算数アプリ、出題前に別モデルと検算で確認",
  "description": "スイスのZeroEx Tsitsipas Labsが運営するLathoaは、AIがわざと間違えた解き方から誤りを探す10〜14歳向けの算数アプリだ。誤りが本当に誤りかを検算と別のモデルで確かめてから出題する。無料プランは1日3問まで。",
  "date": "2026-10-01T17:51:00+09:00",
  "category": "usecases",
  "tags": ["Lathoa", "Claude", "活用事例", "教育", "ハルシネーション"],
  "summary": [
    "Lathoaは、ロボットのErrolが段階的に解いた算数の答えから、わざと混ぜた誤りの1手を10〜14歳の子どもが探すアプリだ",
    "Lathoaの作者によるとLLMにわざと間違えさせるのは難しく、検算と別モデルの解答で食い違う問題は捨ててから出題している",
    "Lathoaは問題作成と子どもの説明の採点にAnthropicのClaudeを使う。無料は1日3問、有料は年66.99ドルから"
  ],
  "sources": [
    {"title": "Lathoa | Critical thinking for kids 10–14 in the age of AI", "publisher": "Lathoa", "url": "https://lathoa.ai/en", "kind": "公式発表"},
    {"title": "Show HN: Lathoa, a math app for kids where the AI is wrong on purpose", "publisher": "Hacker News（作者 thanouil1411 の投稿）", "url": "https://news.ycombinator.com/item?id=49909648", "kind": "公式発表"},
    {"title": "Privacy Policy", "publisher": "Lathoa", "url": "https://lathoa.ai/en/privacy", "kind": "公式ドキュメント"},
    {"title": "Help Center", "publisher": "Lathoa", "url": "https://lathoa.ai/en/help", "kind": "公式ドキュメント"},
    {"title": "Impressum", "publisher": "Lathoa", "url": "https://lathoa.ai/en/impressum", "kind": "公式ドキュメント"}
  ],
  "thumb_text": "Lathoa",
  "share_text": "AIがわざと間違えた解き方から誤りを探す子ども向け算数アプリLathoa。出題前に検算と別モデルで確認",
  "editor_note": ""
}
---
子ども向け学習アプリ「Lathoa」の作者が現地時間9月30日、Hacker Newsの「Show HN」で同アプリを紹介しました。AIのロボットがわざと間違えた算数の解き方を見せ、10〜14歳の子どもがどの手順が誤りかを探して理由を書きます。投稿は50ポイント・26件のコメントを集めました。運営はスイスのZeroEx Tsitsipas Labsです。

## 何を作ったか

Lathoaとは、AIの答えをうのみにせず、誤りを見抜く力を算数で鍛えるアプリです。ロボットの「Errol」が問題を一歩ずつ解き、そのうち1つの手順に誤りを入れます。子どもは誤った手順をタップし、何がおかしいかを自分の言葉で書きます。

ホームページの例では、「3時45分に始まる90分の映画はいつ終わるか」という問題で、Errolが「90分は0.90時間」と換算して4時35分と答えます。誤りのない問題もときどき混ぜるため、毎回「間違いがある」と答えるだけでは点が取れません。誤りを見つけて説明まで書くと、より多くの経験値がもらえます。

難しさは3段階で、正答率が80%を超えると難しく、50%を下回ると易しくなります。内容は米国の共通学力基準（Common Core）の4〜8年生に合わせた、計算・分数・比・代数の入り口・初歩の図形です。子どもがAIと自由に会話する機能はありません。

:::quote https://lathoa.ai/en | Lathoa公式サイト「Things parents actually ask.」
> There's no open-ended chat. Kids interact with structured cases; they don't talk to a model.
自由なチャットはありません。子どもは決まった形式の問題に取り組むだけで、モデルと会話はしません。
:::

## どう作ったか

プライバシーポリシーによると、問題の作成と、子どもが書いた説明の採点にはAnthropicのClaudeを使っています。通信はすべてCloudflare AI Gatewayを経由し、名前やメールアドレス、アカウントの識別子は送らないとしています。データベースと認証にはSupabase、決済にはStripeを使います。

作者がShow HNで最も強調したのは、誤答の作り方です。

:::quote https://news.ycombinator.com/item?id=49909648 | Show HN: Lathoa（作者の投稿）
> The part that surprised me: it's hard to get an LLM to be wrong on purpose. Half the time it gives you the right answer and calls it wrong, or a "mistake" that's actually correct.
意外だったのは、LLMにわざと間違えさせるのが難しいことです。半分ほどは、正しい答えを出して誤りだと言うか、実は正しい「間違い」を出してきます。
:::

そこで、子どもに出す前にすべての問題を確かめる仕組みを作りました。できる部分は通常の算術チェックで正確に計算し直し、さらに別のモデルがErrolの解き方を見ずに同じ問題を解きます。どれか1つでも食い違えば、その問題は捨てます。

弱点も作者は書いています。2つ目のモデルが1つ目と同じ間違いをする可能性があり、それを補う算術チェックは今のところ英語の問題でしか働きません。ドイツ語とギリシャ語は小数点にコンマを使うため、数字の読み取りがまだうまくいっていないといいます。サイトは英語・ドイツ語・ギリシャ語で提供されています。

## 成果と反応

利用者数などの数字は公表されていません。料金は、無料プランが1日3問・易しい段階のみで、有料は1人用のLearnerが月6.99ドルか年66.99ドル、保護者向け機能付きのParentが月9.99ドルか年95.99ドル、子ども4人まで使えるFamilyが月14.99ドルか年143.99ドルです。

Hacker Newsでは、「批判的に考える練習にはなるが、いつそれを使うべきかの練習にはならない」という意見や、Khan Academyや学校の授業にも同じ種類の問題があるという指摘が出ました。例題の誤りが易しすぎて自分の子には簡単だったという声や、サイトの文章がAIで書かれたように見えるという批判もありました。作者は、人の間違いを見つけることが、自分で解くこととは違う学びになるのかを、教える立場の人に聞きたいと投稿を締めています。

## 日本のビジネスへの影響

現時点で日本語には対応しておらず、問題も米国の学習基準に沿っています。ブラウザとiOS、Androidで使えるため、英語の算数教材として家庭で試すことはできます。

参考になるのは、教育サービスの企画者と、生成AIで問題やクイズを作る開発者です。「AIに正しく答えさせる」のではなく「AIの誤りを教材にする」という逆の発想と、AIが作った問題を出す前に決まった計算と別モデルの二重チェックに通して怪しいものを捨てる作り方は、日本語の教材や社内研修の確認テストにも応用できます。

今すぐやれることは、登録なしで遊べるホームページの例題を1問解き、誤りの見せ方と説明の書かせ方を確かめることです。注意点は、作者自身が認めるとおり、2つのモデルが同じ誤りをすれば検証をすり抜けることです。日本語で同じ仕組みを作るなら、数字や単位の表記揺れの読み取りを先に固める必要があります。Claudeなどのモデルを組み込む費用は[AI API（LLM）の料金比較](/best/api/)で確かめられます。
