---
{
  "title": "Geminiが詐欺メッセージの「狙い」を読んで警告、Androidの新機能 画面共有中はカード番号も隠す",
  "description": "GoogleはAndroidの詐欺対策を強化し、Googleメッセージで見知らぬ相手との会話をGeminiが読んで詐欺の狙いを見抜く設定を数週間以内に配ると発表した。同社の詐欺検知はすでに月500万件超の電話とメッセージに警告を出している。",
  "date": "2026-10-15T03:10:00+09:00",
  "category": "products",
  "tags": ["Google", "Gemini", "Android", "詐欺", "セキュリティ", "プライバシー"],
  "summary": [
    "GoogleがAndroidの新しい詐欺対策を発表。Googleメッセージに見知らぬ相手との会話をGeminiが読んで警告する設定が加わる",
    "画面共有中はブラウザーに打ち込むパスワードやカードの番号が自動で隠れるようになり、Android 15以降の端末に今月配られる",
    "Googleの詐欺検知はすでに毎月500万件を超える電話とメッセージに警告を出している。新機能の日本での提供は明記されていない"
  ],
  "sources": [
    {"title": "New Android protections to help keep you safe from mobile scams", "publisher": "Google", "url": "https://blog.google/security/new-android-scam-protections/", "kind": "公式発表"},
    {"title": "Staying One Step Ahead: Strengthening Android's Lead in Scam Protection", "publisher": "Google", "url": "https://blog.google/security/strengthening-android-lead-in-scam-protection/", "kind": "公式発表"},
    {"title": "Android will use Gemini to warn you about scammy messages", "publisher": "Engadget", "url": "https://www.engadget.com/2286355/android-will-use-gemini-to-warn-you-about-scammy-messages/", "kind": "報道"}
  ],
  "thumb_prompt": "A smartphone lying on a kitchen table showing a friendly chat bubble, while a small glowing magnifying glass hovers over it revealing a fishing hook hidden inside the message bubble.",
  "thumb_style": "3d",
  "thumb_text": "Android 詐欺対策",
  "share_text": "見知らぬ相手とのやり取りをGeminiが読んで詐欺の狙いを警告。Androidの新しい詐欺対策、画面共有中はカード番号も自動で隠す",
  "editor_note": ""
}
---
Googleは現地時間10月14日、Androidスマホ向けの新しい詐欺対策を発表し、Googleメッセージで知らない相手とやり取りしているときに、Geminiが会話の流れから相手の狙いを読み取って警告する設定を数週間以内に配ると明らかにしました。あわせて、画面共有中にパスワードやカード情報を自動で隠す機能や、電話の転送を悪用する手口への対策も加わります。Googleによると、同社の詐欺検知はすでに毎月500万件を超える電話とメッセージに警告を出しています。

## 何が発表されたか

中心になるのは、Googleメッセージ（Android標準のSMS・チャットアプリ）に加わる「強化保護モード（Enhanced protection mode）」です。自分でオンにする設定で、オンにすると次の3つが働きます。

- **会話の狙いをGeminiが判定**: 連絡先にない相手との会話を、Googleのクラウド上の高性能なGeminiが読み、だまそうとする意図を早めに見抜く。これまで端末の中だけで行っていた判定を補う形
- **見慣れないリンクの事前チェック**: スマホの中で動く小型のAI「Gemini Nano」が、まだ危険サイトの一覧に載っていない新しいURLも、ネット上の情報をもとに安全かどうか判定する
- **知らない番号からのリンクに確認画面**: 連絡先にない番号から届いたリンクを押す前に、注意を促す画面をはさむ。これまでは一部の国や、最も強い保護設定をオンにした端末だけの機能だった

:::quote https://blog.google/security/new-android-scam-protections/ | Google公式ブログ「New Android protections to help keep you safe from mobile scams」
> Scammers often disguise their true motives behind slow-burn conversations.
詐欺師は、時間をかけてゆっくり進める会話の陰に本当の狙いを隠すことがよくあります。
:::

クラウドで会話を読むことへの不安に対しては、Googleは「Private AI Compute」という仕組みで処理すると説明しています。データは暗号化され、Google自身も中身を見られない専用の環境で処理されるといいます。対象の端末はPixel 10以降、Galaxy S26シリーズ、Galaxy Z FlipとZ Fold8などです。

ほかに発表された主な対策は次のとおりです。

| 機能 | 中身 | 提供時期・対象 |
|---|---|---|
| 画面共有中の自動マスク | ChromeやアプリのWeb画面で、ログイン欄や支払い画面を画面共有中に自動で隠す | 今月、Android 15以降の端末 |
| 電話転送の防止 | アプリが裏で勝手に電話の転送を設定するのを止める。転送用の番号を打たせる手口には警告 | 12月上旬からPixelなど |
| 通知での詐欺警告の拡大 | チャットアプリを開く前に、通知の段階で怪しいメッセージを知らせる。Pixelで始めた機能を他社端末へ | 年内。Motorola、OPPO、Xiaomiなど12ブランド |
| 銀行を名乗る電話の照合 | 銀行のアプリと連携し、本当に銀行からの電話かをその場で確かめ、偽物なら切る | ブラジルなどで提供中 |

電話の転送は、ワンタイムパスワード（ログイン時にSMSや電話で届く使い捨ての確認番号）を横取りしてアカウントを乗っ取るのに使われる手口です。銀行を名乗る電話の照合では、6月の開始からブラジルの大手2行の分だけで300万件を超える偽の電話を止めたとしています。

{{card:https://blog.google/security/new-android-scam-protections/|New Android protections to help keep you safe from mobile scams|Google}}

## 背景

詐欺の手口は、迷惑電話や見るからに怪しいSMSから、「番号を間違えました」と話しかけて何日もかけて信頼を築くような、ゆっくりした会話型に移っています。Googleが米国・カナダ・オーストラリアで行った調査では、スマホ利用者の40%が携帯での詐欺を「とても」または「非常に」心配していると答えました。

Googleはこれまで、Googleメッセージの詐欺検知を端末の中だけで動くAIで行い、2026年2月には20カ国以上に広げていました。今回はそこに、より賢いクラウドのGeminiを「本人が選んだ場合だけ」重ねる形です。前日には、Google DeepMindがシンガポール政府と、端末の中だけでチャットの詐欺を見抜くAIを共同開発したと発表したばかりです（[記事](/news/20261014-deepmind-singapore-on-device-scam-detection/)）。

## 反応と論点

Engadgetは、新しい設定がオプトイン（自分でオンにする方式）で、対象がPixel 10以降など一部の機種に限られると報じています。会話をクラウドに送ることを嫌う人は、従来どおり端末内の判定だけを使えます。

一方で、発表の後半はiPhoneとの比較に多くを割いています。Googleは、自社が費用を出した外部のセキュリティ会社Leviathan Security Groupの評価で、Androidの標準の詐欺対策がiPhoneを上回ったと紹介しました。ただし、依頼元がGoogle自身である点は割り引いて読む必要があります。

## 日本のビジネスへの影響

- **使えるか**: 今回の新機能について、Googleは日本での提供時期を明記していません。画面共有中の自動マスクは「Android 15以降の端末」向けとされ、国の限定は書かれていません。Pixelの電話の詐欺検知はすでに日本でも提供されています（2026年2月の公式発表）
- **誰に効くか**: 金融機関やECのカスタマーサポート担当者です。電話口で「画面を共有してください」と頼ませる詐欺は、サポートを装うのが典型です。端末側で入力欄が隠れるようになっても、自社の案内の仕方を見直す価値があります
- **今すぐやれること**: 社員や家族のAndroidで、Googleメッセージの設定に「詐欺検知」が入っているか確かめ、強化保護モードが届いたらオンにするかを決めておきます。顧客向けには「当社が画面共有やワンタイムパスワードを求めることはない」と改めて告知するのが手堅い一手です
- **注意点**: 強化保護モードでは、知らない相手との会話がクラウドのGeminiで分析されます。会社支給の端末で使うなら、社内の情報管理ルールと照らしてオンにするか判断してください。AIの警告は見逃しも誤報もあり、最後は人が確かめる前提は変わりません
