---
{
  "title": "AIで作った画像や動画か誰でも確かめられる、Googleが判定サイトを世界に公開",
  "description": "Googleは10月7日、画像・動画・音声がAIで作られたかを調べる無料サイト「SynthID Detector」を世界に公開した。OpenAIやNVIDIAのAIで作ったものも判定できる。印を入れた画像と動画は1,800億点を超える。",
  "date": "2026-10-08T00:40:00+09:00",
  "category": "policy",
  "tags": ["Google", "SynthID Detector", "SynthID", "電子透かし", "画像生成", "ディープフェイク"],
  "summary": [
    "Googleは10月7日、画像・動画・音声がAIで作られたかを調べる無料サイト「SynthID Detector」を世界の誰にでも公開した",
    "Googleに加えOpenAI・NVIDIA・韓国Kakaoの生成AIで作ったものも判定でき、Appleも今後対応する。画面は今のところ英語だけ",
    "AIが作品に埋め込む目に見えない印を読む仕組みのため、印のないAIや印が消された画像は見抜けない"
  ],
  "sources": [
    {"title": "We're making it easier to identify AI-generated content globally", "publisher": "Google（blog.google）", "url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/synth-id-ai-content/", "kind": "公式発表"},
    {"title": "SynthID Detector", "publisher": "Google", "url": "https://synthid.com/", "kind": "公式サイト"},
    {"title": "Google's AI detection website is now available", "publisher": "Engadget", "url": "https://www.engadget.com/2279565/google-synth-id-detector-ai-detection-website-is-now-available/", "kind": "報道"},
    {"title": "Google opens SynthID Detector to everyone to check for AI-made media", "publisher": "The Next Web", "url": "https://thenextweb.com/news/google-synthid-detector-public-ai-content-checker", "kind": "報道"}
  ],
  "thumb_text": "SynthID Detector",
  "thumb_style": "photo",
  "thumb_prompt": "A person's hand holding a large magnifying glass over a printed photo of a sunset beach on a wooden desk; through the lens the photo reveals a faint hidden grid of tiny glowing dots, as if invisible ink had been exposed.",
  "share_text": "AIで作った画像・動画・音声かを誰でも無料で確かめられるサイトをGoogleが世界公開。OpenAIやNVIDIAのAI製も判定",
  "editor_note": ""
}
---
Googleは現地時間10月7日、画像・動画・音声がAIで作られたものかを調べられるサイト「SynthID Detector」（synthid.com）を、世界中の誰でも使えるようにしました。無料で、Googleの生成AIに加え、OpenAIやNVIDIAなど提携企業のAIで作られたものも判定できます。

## 何が公開されたか

SynthID Detectorとは、ファイルをアップロードすると、AIが作品に埋め込んだ目に見えない印（電子透かし）が入っているかを調べてくれるサイトです。印の名前が「SynthID」で、Googleの研究部門Google DeepMindが2023年から自社の生成AIの出力に入れてきました。

これまでは2025年5月に、報道関係者や研究者に限って先行版が提供されていました。今回は英語の画面で世界に公開され、Google・OpenAI・Appleのいずれかのアカウントでログインすれば使えるとEngadgetやThe Next Webが報じています。

Google DeepMindのプッシュミート・コーリ副社長は公式ブログで、対象を次のように説明しています。

:::quote https://blog.google/innovation-and-ai/models-and-research/google-deepmind/synth-id-ai-content/ | Google公式ブログ「We're making it easier to identify AI-generated content globally」
> With the new SynthID Detector, anyone can easily check if an image, video, or audio file was made with AI from Google or our partners, including OpenAI, NVIDIA, Kakao, and soon, Apple.
新しいSynthID Detectorで、画像・動画・音声ファイルが、Googleか、OpenAI・NVIDIA・Kakao、そして近くAppleを含む提携企業のAIで作られたものかを、誰でも簡単に確かめられる。
:::

規模の数字も公表されました。SynthIDの印が入った画像と動画は1,800億点を超え、音声は合計24万年分にのぼります。Google検索・Geminiアプリ・Chromeに組み込まれた確認機能には、すでに1日100万件を超える問い合わせが来ているといいます。

## 何がわかり、何がわからないか

便利な一方で、万能の「AI判定機」ではありません。報道各社が指摘している主な限界は次のとおりです。

- **印のないAIは見抜けない**: 調べるのはSynthIDの印だけです。印を入れていない会社のAIで作った画像は、AI製でも検出されません
- **印は消されることがある**: 加工の仕方によっては印が取り除かれる場合があります
- **「全部AI」か「一部だけAI」かは区別しない**: The Next Webによると、結果は「GoogleのAIで作成または編集された」という形で示され、写真の一部をAIで直しただけなのか、まるごと生成したのかまではわかりません

つまり「印が見つかった＝AIが関わった」とは言えても、「印がない＝人が作った本物」とは言えません。ここを取り違えると、かえって誤った安心につながります。

## 背景

生成AIで作った写真や声は、本物との見分けがますます難しくなっています。各社は「作った側が印を入れる」方式で足並みをそろえつつあり、OpenAIもEUでChatGPTが書いた文章に見えない透かしを入れる計画を明らかにしています（[既報](/news/20261006-openai-chatgpt-text-watermark-eu/)）。

Googleの印をOpenAIやNVIDIA、Kakaoが自社のAIに採用したことで、1つのサイトで複数社のAI製品をまとめて確かめられるようになりました。Engadgetによると、Appleの「Apple Intelligence」で作ったものへの対応も近く加わる予定です。

## 日本のビジネスへの影響

- **使えるか**: 日本からも使えます。画面は今のところ英語だけですが、ファイルを入れて結果を見るだけなので操作は難しくありません。無料です
- **誰にどう効くか**: SNSに寄せられた画像や、取引先・応募者から届いた写真の真偽を確かめたい広報・SNS運用の担当者や、採用・審査の担当者に役立ちます。反対に、AIで作った広告画像を使うマーケターは、自社の素材もこうして簡単に「AI製」と判定されることを前提にしておく必要があります
- **今すぐやれること**: 自社で使っているAI画像を1枚 synthid.com に入れて、どう表示されるかを確かめておきます。広告や広報でAI素材を使うなら、「AIで作成」と自分から明記する社内ルールを決めておくと、後から指摘されて慌てずに済みます
- **注意点**: 「印が見つからない」ことは本物の証明になりません。判定結果だけを根拠に、投稿者や取引先を「偽物を出した」と責めないようにしてください

画像を作るAIの選び方と料金は、[画像生成AIのおすすめと料金比較](/best/image-generation/)にまとめています。
