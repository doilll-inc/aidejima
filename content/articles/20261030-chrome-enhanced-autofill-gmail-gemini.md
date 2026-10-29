---
{
  "title": "GeminiがGmailから注文番号や予約番号を探し、Chromeの入力欄を自動で埋める 米国で開始",
  "description": "Googleは10月28日、Chromeの自動入力がGemini経由でGmailを参照し、注文番号・配送の追跡番号・航空券の予約情報を入力欄に提案する機能を米国で始めた。パソコン・Android・iPhoneの3つで順次使えるようになる。",
  "date": "2026-10-30T00:40:00+09:00",
  "category": "products",
  "tags": ["Gemini", "Gemini in Chrome", "Google", "Gmail", "Personal Intelligence", "プライバシー"],
  "summary": [
    "GoogleのブラウザChromeの自動入力が、Gmailのメールから注文番号や配送の追跡番号、航空券の予約情報を探して入力欄に提案するようになった",
    "Googleの対話AI「Gemini」がGmailの中身を参照する仕組みで、10月28日から米国でパソコン・Android・iPhone向けに順次始まった",
    "使えるのはGeminiに自分のGmailなどをつなぐ設定をした人だけ。日本での開始時期は発表されていない"
  ],
  "sources": [
    {"title": "Chrome enhanced autofill now pulls data from Gmail", "publisher": "Google公式ブログ", "url": "https://blog.google/products-and-platforms/products/chrome/enhanced-autofill-gmail/", "kind": "公式発表"},
    {"title": "Use Gemini in Chrome", "publisher": "Google Chrome ヘルプ", "url": "https://support.google.com/chrome/answer/16283624?hl=en", "kind": "公式ドキュメント"},
    {"title": "Connect your Google content apps to get a Search services experience that's tailored to you", "publisher": "Google 検索ヘルプ", "url": "https://support.google.com/websearch/answer/16859283?hl=en", "kind": "公式ドキュメント"},
    {"title": "Chrome's AI-powered Autofill can now dig through your Gmail to fill out forms", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/10/28/chromes-ai-powered-autofill-can-now-dig-through-your-gmail-to-fill-out-forms/", "kind": "報道"},
    {"title": "Google Chrome rolling out 'Suggested by Gemini' autofill", "publisher": "9to5Google", "url": "https://9to5google.com/2026/10/28/chrome-autofill-gemini/", "kind": "報道"},
    {"title": "Chrome's Gemini-powered autofill can now pull data from Gmail", "publisher": "Android Authority", "url": "https://www.androidauthority.com/chrome-gemini-autofill-gmail-privacy-3728808/", "kind": "報道"},
    {"title": "Google Chrome's Enhanced Autofill Feature Can Now Pull Information From Gmail", "publisher": "Thurrott", "url": "https://www.thurrott.com/cloud/343330/google-chromes-enhanced-autofill-feature-can-now-pull-information-from-gmail", "kind": "報道"}
  ],
  "thumb_prompt": "A web browser form on a laptop screen with empty input boxes, while a paper airline boarding pass and a delivery receipt slide out of an open envelope and float neatly into the boxes like puzzle pieces.",
  "thumb_style": "illustration",
  "thumb_text": "Chrome 自動入力",
  "share_text": "Chromeの自動入力がGemini経由でGmailを参照、注文番号や航空券の予約番号を入力欄に提案。米国で開始",
  "editor_note": ""
}
---
Googleは現地時間10月28日、ブラウザ「Chrome」の自動入力が、対話AI「Gemini」を通じてGmailのメールを探し、注文番号や配送の追跡番号、航空券の予約情報を入力欄に提案する機能を始めました。まず米国で、パソコン・Android・iPhoneの3つに順次広がります。名前や住所、クレジットカード番号だけだった自動入力が、受信トレイの中身まで扱うようになります。

## 何が始まったか

Chromeには、入力欄をクリックすると保存済みの名前や住所を候補として出す「自動入力」があります。今回、その強化版（Googleは「enhanced autofill」と呼んでいます）が、Gmailに届いたメールから必要な番号を拾ってくるようになりました。Google公式ブログの発表は短いものですが、要点は次の一文です。

:::quote https://blog.google/products-and-platforms/products/chrome/enhanced-autofill-gmail/ | Google公式ブログ「Chrome enhanced autofill now pulls data from Gmail」
> Starting today, Chrome’s enhanced autofill feature can automatically suggest information pulled directly from Gmail as you fill out online forms.
本日から、Chromeの強化版の自動入力は、オンラインのフォームに入力する際に、Gmailから直接取り出した情報を自動で提案できるようになります。
:::

たとえば、航空会社のサイトでオンラインチェックインをするとき、予約確認メールを探して番号を写す手間がなくなります。通販の問い合わせフォームで注文番号を求められたときも同じです。9to5Googleによると、提案は自動入力の候補の中に「Suggested by Gemini（Geminiによる提案）」という見出しで並びます。Android Authorityは、候補を選ぶとどのメールから取ったかが示されると報じています。

対象は、ChromeのGemini機能（Gemini in Chrome）を使っていて、「パーソナル インテリジェンス」を有効にしている人です。パーソナル インテリジェンスとは、GmailやGoogleフォトなど自分のGoogleサービスの中身をGeminiに読ませ、その人に合わせた答えを返させる設定のことです。

## 背景

Googleは今年、パーソナル インテリジェンスを検索の「AIモード」や車のGeminiへと広げてきました。Chromeの自動入力でGmailを使う機能は、開発版のChromeで試されていたものです。Android Authorityによると、試験版ではGoogleフォトや「ほかの接続アプリ」も参照できましたが、今回の正式版はGmailだけに絞られています。Thurrottは、Googleフォトの画像から情報を拾う機能も近く加わる予定だと報じています。

## 反応と論点

Googleは、扱いに注意が必要なデータは暗号化され、強化版の自動入力を使うかどうか、何を参照させるかは設定で決められると説明しています。提案を1件ずつ消すことも、機能ごと切ることもできます。

一方で、ブラウザがメールの中身を読みにいくことへの不安も出ています。Android Authorityは、Googleが最近、パーソナル インテリジェンスでつないだ情報を広告の出し分けに使えるようポリシーを改めた点を挙げ、自動入力のデータが広告に使われるとは限らないとしつつも懸念を示しました。この記事の読者投票（34票）では、便利さを理由に「使う」が47%、「使わない」が29%でした。広告とのつながりは[GmailやフォトをAIモードにつなぐと広告にも使われる件](/news/20261024-google-ai-mode-gmail-photos-ads-policy/)で詳しく書いています。

## 日本のビジネスへの影響

- **使えるか**: 今回のGmail連携は米国だけで、日本での開始時期は発表されていません。なお、ChromeのGemini機能そのものは、Chromeヘルプの対応地域に日本が入っており、日本語でも使えます。
- **誰にどう効くか**: 出張の多い営業や、通販の注文・配送の問い合わせを日々さばくEC担当者には、メールを探して番号を写す作業が減ります。EC事業者側から見ると、顧客がフォームで入力を間違える場面が減る可能性があります。
- **今すぐやれること**: 自社の問い合わせフォームや予約フォームの入力欄に、「注文番号」「予約番号」とわかる名前やラベルが付いているかを見直しておきましょう。AIが欄の意味を読み取りやすくなります。
- **注意点**: パーソナル インテリジェンスは個人のGoogleアカウント向けの設定です。仕事のメールを個人のGmailに転送している人がこの機能をオンにすると、業務の情報もGeminiに参照されます。社内ルールで扱いを決めておくと安心です。

調べものや下調べに使えるAIの選び方は[リサーチ向けAIのおすすめ](/best/research/)にまとめています。
