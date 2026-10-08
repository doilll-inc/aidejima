---
{
  "title": "会議の走り書きメモをAIが清書、ネットにつながず動くGoogleのMac用アプリ「Foresight」",
  "description": "Googleは10月6日、会議の録音・文字起こし・メモの清書をすべてMacの中で処理する試験版アプリ「Google AI Edge Foresight」を公開した。7億4000万パラメーターの小型モデルと手元の資料を組み合わせ、会議中の質問にも答える。",
  "date": "2026-10-09T04:05:00+09:00",
  "category": "products",
  "tags": ["Google", "Google AI Edge Foresight", "文字起こし", "Gemma 4", "プライバシー", "ローカルLLM"],
  "summary": [
    "Googleが会議メモ用のMacアプリ「Foresight」を試験公開した。録音も文字起こしもメモの清書もパソコンの中だけで処理する",
    "会議中に箇条書きで走り書きすると、AIが会話の文字起こしから肉付けしてメモに仕上げる。対面の会議にもZoomにも使える",
    "手元のPDFやOffice文書を読ませておけば、会議中に出た質問への答えを出典付きで画面に出す。インターネットがなくても動く"
  ],
  "sources": [
    {"title": "Google AI Edge Foresight", "publisher": "Google for Developers", "url": "https://developers.google.com/edge/foresight", "kind": "公式サイト"},
    {"title": "Google AI Edge with EmbeddingGemma 2", "publisher": "Google Developers Blog", "url": "https://developers.googleblog.com/google-ai-edge-with-embeddinggemma-2/", "kind": "公式発表"},
    {"title": "Google releases a new local-first Granola competitor", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/10/08/google-releases-a-new-local-first-granola-competitor/", "kind": "報道"},
    {"title": "Google's AI note-taking app transcribes your meetings completely offline", "publisher": "The Verge", "url": "https://www.theverge.com/tech/1007985/google-ai-notetaking-app-transcribe-offline", "kind": "報道"},
    {"title": "Google's macOS app: Local AI to capture notes and work with files", "publisher": "heise online", "url": "https://www.heise.de/en/news/Google-s-macOS-app-Local-AI-to-capture-notes-and-work-with-files-11479591.html", "kind": "報道"}
  ],
  "thumb_text": "Foresight",
  "thumb_style": "photo",
  "thumb_prompt": "A laptop on a seat-back tray table inside a dimly lit airplane cabin at night, its screen glowing with neatly organized meeting notes, next to a paper napkin covered in hurried handwritten scribbles.",
  "share_text": "会議中の走り書きをAIがメモに清書。GoogleのMac用アプリ「Foresight」は録音も文字起こしもパソコンの中だけで処理",
  "editor_note": ""
}
---
Googleは現地時間10月6日、会議の文字起こしとメモ作りをすべてMacの中で処理する試験版アプリ「Google AI Edge Foresight」を公開しました。会議の音声や手元の資料をクラウドに送らず、インターネットにつながっていない状態でも動くのが特徴です。

## 何が発表されたか

Google AI Edge Foresightとは、会議に同席してメモ作りと調べものを手伝うMac用のアプリです。Googleで端末の中で動くAIを担当する「Google AI Edge」のチームが、新しい小型モデルの発表に合わせて公開しました。

:::quote https://developers.googleblog.com/google-ai-edge-with-embeddinggemma-2/ | Google Developers Blog「Google AI Edge with EmbeddingGemma 2」
> We are excited to announce the launch of Google AI Edge Foresight for Mac, an experimental app that brings a context-aware meeting companion directly to your device.
Mac向けの「Google AI Edge Foresight」の提供を始める。状況を理解する会議の相棒を、端末そのものに届ける試験的なアプリだ。
:::

公式ページで説明されている機能は、大きく3つです。

- **走り書きの清書**: 会議中、覚えておきたいことを短い箇条書きで打っておくと、AIが会話の文字起こしをもとに中身を補い、整ったメモに仕上げます。オンライン会議でも対面の会議でも使えます
- **手元の資料を覚える**: 仕事のフォルダーや参考資料、図、カレンダーを指定しておくと、AIが中身を読み込みます。対応する形式はPDF、Googleドキュメント、Microsoft Officeの文書、テキスト、Markdown、ブラウザーのブックマークで、Googleドライブもつなげます
- **会議中に答えを出す**: チャットで質問できるほか、「Live Assistance」をオンにすると、会議で出た質問をAIが聞き取り、読み込んだ資料から答えを出典付きのカードで画面に表示します

公式のよくある質問では、Google Meet、Zoom、対面の会話のどれでも、パソコンの音声を聞き取って文字にすると説明しています。

{{card:https://developers.google.com/edge/foresight|Google AI Edge Foresight（ダウンロードページ）|Google for Developers}}

## なぜネットなしで動くのか

中で動いているのは、Googleが同じ日に公開した「EmbeddingGemma 2」と、対話用の「Gemma 4」です。EmbeddingGemma 2は7億4000万パラメーター（AIの規模を表す数字）の小型モデルで、文章・画像・動画・音声を同じ物差しで比べられる形に変換します。このおかげで「先週の打ち合わせで見せた図」のような探し方を、パソコンの中だけで高速にできます。Googleの開発者ブログによると、スマートフォンのPixel 11 Proでは、文章だけを扱う場合に約191MBのメモリーで動く軽さです。

公式ページのよくある質問は、データの扱いを次のように説明しています。

:::quote https://developers.google.com/edge/foresight | Google AI Edge Foresight（よくある質問）
> All AI inference runs 100% locally on your device using on-device Gemma models. Your personal knowledge sources, meeting audio, and notes never leave your computer.
AIの処理はすべて、端末上のGemmaモデルを使って100%手元で動く。個人の資料、会議の音声、メモがパソコンの外に出ることはない。
:::

飛行機の中や、ネットワークから切り離された施設でも使えるとしています。動作環境はAppleの独自チップ（Apple Silicon）を積んだMacに最適化されており、heise onlineはIntelのMacには対応していないと報じています。

## 背景

AIによる会議メモは、米国ではGranolaなどの専用アプリが広く使われている分野です。TechCrunchはForesightを「Granolaの競合」と位置づけ、オフラインで音声を文字にするGoogleの別のアプリ「AI Edge Eloquent」を手がけたチームの新作だと伝えています。Googleはクラウド側でもGoogle Meetの自動メモ（Gemini）を提供しており、Foresightは「会議の中身を外に出したくない人向け」の別の選択肢になります。

料金について公式ページに記載はなく、The Vergeは無料で使えると報じています。heise onlineによると、配布はMac App Storeではなく、Googleのページからの直接ダウンロードです。

## 反応と論点

TechCrunchは、Googleが将来、Geminiのアプリを通じてクラウドのモデルを使う一般向け版を出す可能性にも触れています。ただし、現時点のForesightはあくまで「試験的なアプリ」と明記されており、Googleが正式な製品として続けるかどうかは示されていません。

もう1つの論点は、会議の録音そのものの扱いです。処理がパソコンの中で完結しても、参加者に録音を伝える必要があることは変わりません。また、公式ページには日本語の会議に対応するかの記載がなく、日本の利用者にとってはここが最初の確認点になります。

Googleの会議・資料まわりのAIでは、資料を読ませて要約や音声解説を作る[NotebookLMの使い方](/news/20261009-notebooklm-gemini-notebook-how-to-use/)も参考になります。

## 日本のビジネスへの影響

- **使えるか**: ダウンロードページに提供地域の制限は書かれておらず、Apple Silicon搭載のMacで試せます。ただし日本語の会議への対応は公式に書かれておらず、試験版のため品質や提供の継続も保証されていません
- **誰にどう効くか**: 社外秘の打ち合わせが多い経営企画・法務・M&Aの担当者や、取引先との機密保持契約でクラウドの録音ツールを使えない営業・コンサルタントに向いています。録音や資料がパソコンから出ないため、情報システム部門の審査の論点が少なくて済みます
- **今すぐやれること**: Macを持っている人は、まず社内の短い定例会議で英語と日本語の両方を試し、文字起こしの精度と清書メモの使い勝手を、いま使っている議事録ツールと比べてみてください
- **注意点**: 「手元で完結する」のはAIの処理の話で、Googleドライブをつなげばその部分はネット経由になります。会社のMacに入れる前に、社内のソフト導入ルールに従って許可を取り、参加者への録音の告知も忘れないようにしてください

ほかの文字起こし・議事録ツールとの料金や機能の比較は、[AI文字起こし・議事録ツールのおすすめと料金比較](/best/transcription/)にまとめています。
