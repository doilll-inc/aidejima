---
{
  "title": "買収前の契約書調べを「数週間から数時間」に、米大手法律事務所がOpenAIと専用AIを開発",
  "description": "弁護士1,500人を抱える米法律事務所Ropes & Grayが、企業買収の前に相手の契約書を洗い出す調査をAIに下ごしらえさせる道具をOpenAIと開発している。数千ページを読んで論点ごとに仕分け、事務所の書式で報告書まで作る。",
  "date": "2026-10-30T13:00:00+09:00",
  "category": "usecases",
  "tags": ["Ropes & Gray", "OpenAI", "GPT-6 Astra", "活用事例", "導入事例", "法務"],
  "summary": [
    "米国の大手法律事務所Ropes & Grayは、企業買収の前に相手の契約書を調べる作業を手伝うAIを、OpenAIと一緒に開発している",
    "AIは数千ページの資料を読んで関係する文書を探し、論点ごとに仕分けて要約と報告書の下書きまで作る。弁護士は全部を確かめてから客に渡す",
    "事務所は、何週間もかかっていた詳しい報告書を数時間で作れるようにすることを目標に掲げている。仕上がりは中堅手前の若手弁護士並みという"
  ],
  "sources": [
    {"title": "How Ropes & Gray is developing AI for transactional diligence", "publisher": "OpenAI", "url": "https://openai.com/index/ropes-gray-ai-diligence/", "kind": "公式発表"},
    {"title": "Ropes & Gray is Developing AI-Powered Diligence Tool with OpenAI to Deliver Comprehensive Deal Intelligence for Clients", "publisher": "Ropes & Gray", "url": "https://www.ropesgray.com/en/news-and-events/news/2026/09/ropes-gray-is-developing-ai-powered-diligence-tool-with-openai-comprehensive-deal-intelligence", "kind": "公式サイト"},
    {"title": "Ropes & Gray encourages juniors to spend 20% of billable hours on AI", "publisher": "Legal Cheek", "url": "https://www.legalcheek.com/2025/11/ropes-gray-encourages-juniors-to-spend-20-of-billable-hours-on-ai/", "kind": "報道"},
    {"title": "Dedicate 20% of billable time to AI studies, international firm tells juniors", "publisher": "Law Gazette", "url": "https://www.lawgazette.co.uk/news/dedicate-20-of-billable-time-to-ai-studies-international-firm-tells-juniors/5125126.article", "kind": "報道"}
  ],
  "thumb_prompt": "A towering stack of thick paper contracts on a polished conference table being neatly sorted by a small friendly robot arm into color-coded folders, while a lone fountain pen rests on top of a single finished report.",
  "thumb_style": "3d",
  "thumb_text": "Ropes & Gray",
  "share_text": "買収前の契約書調べを数週間から数時間に。弁護士1,500人の米大手法律事務所がOpenAIと専用AIを開発",
  "editor_note": ""
}
---
米国の大手法律事務所Ropes & Gray（ロープス・アンド・グレイ）は、企業を買収する前に相手の契約書を洗い出す「デューデリジェンス」（買収前の調査）を手伝うAIを、OpenAIと一緒に開発しています。OpenAIが現地時間10月29日に公開した導入事例によると、AIが数千ページの資料を読んで論点ごとに仕分け、要約と報告書の下書きまで作ります。事務所は、これまで何週間もかかっていた詳しい報告書を数時間で仕上げることを目標にしています。

## 何を作ったか

企業を買う側は、契約の前に、売り手が示した財務や法律上の説明が正しいかを確かめます。取引先との契約に不利な条項がないか、思わぬ責任を負っていないかを、売り手が用意した大量の資料から探す仕事です。ふつうは弁護士のチームが何日も張りついて進めます。

Ropes & Grayが作っているのは、この調査の「1回目の読み込み」をAIに任せる道具です。

:::quote https://openai.com/index/ropes-gray-ai-diligence/ | OpenAI「How Ropes & Gray is developing AI for transactional diligence」
> The new diligence AI tool takes a first pass by combing through thousands of pages, identifying relevant documents and automatically grouping them together based on themes and issues.
新しい調査用のAIツールは、数千ページを読み込んで関係する文書を見つけ、テーマや論点ごとに自動で仕分けるという最初の作業を担います。
:::

仕分けたうえで、文書ごとの要約と、事務所が普段使っている書式の報告書を作ります。売り手が資料を置く「データルーム」（買収の検討用に資料を集めた共有の保管場所）の中身を一覧にして分類するので、契約書を1通ずつ見るのではなく、取引先との関係全体を見渡せるといいます。最初に対象にしたのは、事業に大きく関わる取引契約です。

## どう作ったか

使っているのはOpenAIのモデルで、導入事例はGPT-6 Astraの名前を挙げています。工夫は、AIの手順を事務所の弁護士の手順にそろえたことです。最初の目通し、要約、上の立場の弁護士による確認という流れを、同じ問いと枠組みで毎回くり返すように組んでいます。

精度の確かめ方も具体的です。すでに終わった案件で弁護士が書いた調査報告書と、AIが作った下書きを並べ、合っていた点と足りなかった点を洗い出しました。その結果をもとに、評価の基準と報告書の書式を直しています。

事務所の会長Julie Jones氏は9月17日の自社の発表で、時間のかかる法律の仕事に最先端のAIを持ち込む最初の対象が、買収前の調査だと説明しています。

:::quote https://www.ropesgray.com/en/news-and-events/news/2026/09/ropes-gray-is-developing-ai-powered-diligence-tool-with-openai-comprehensive-deal-intelligence | Ropes & Gray「Ropes & Gray is Developing AI-Powered Diligence Tool with OpenAI」
> Ropes & Gray is developing a proprietary AI-powered review tool that can produce a detailed, issue-level diligence report in hours, not weeks.
Ropes & Grayは、論点ごとの詳しい調査報告書を、数週間ではなく数時間で作れる独自のAIツールを開発しています。
:::

## 成果と、弁護士が残す仕事

道具はまだ開発中で、「数時間」はあくまで目標です。導入事例は時間や費用が何割減ったかといった数字は示しておらず、仕上がりの水準を「有能な若手から中堅手前の弁護士の仕事に相当する」と表現しています。

人の確認は外していません。事務所でAIの活用を率いるHoward Glazer氏は導入事例の中で「客は契約書を読む作業に払っているのではなく、そこから下す判断に払っている」と話しています。AIの途中の要約と元の文書を弁護士が簡単に見比べられる作りにしてあり、客に渡すものは全て弁護士が目を通します。読み込みに使っていた時間を、リスクの分析や取引の組み立ての相談に回すねらいです。

この事務所は人の育て方もAI前提に変えています。英国の法律専門メディアLegal CheekとLaw Gazetteは2025年11月、Ropes & Grayが1年目の弁護士に、勤務時間の約2割をAIの訓練や試行に使うよう勧めていると報じました。Legal Cheekによると、年1,900時間の目標のうち約400時間に当たります。事務所は340人のパートナーと1,500人の弁護士を抱えており、次は所内の知識を誰でも引き出せるようにすることを目指すとしています。

## 日本のビジネスへの影響

- **使えるか**: この道具は事務所の独自開発で、外部には売られていません。ただ、使っているのはOpenAIの市販のモデルで、日本の企業でもChatGPTの会社向けプランやAPIから同じモデルを使えます。
- **誰にどう効くか**: 買収や出資の検討をする経営企画・法務の担当者、取引先との契約書を大量に管理している購買や営業管理の部署に向く考え方です。「契約書を1通ずつ読む」作業を、「論点ごとに仕分けた一覧を確かめる」作業に置き換えられます。
- **今すぐやれること**: 過去に終わった案件の契約書と、そのとき人が作った確認メモを1組用意し、同じ契約書をAIに読ませて論点を書き出させてみてください。人のメモと突き合わせれば、AIが拾えたもの、見落としたものが分かり、自社で任せられる範囲を判断できます。Ropes & Grayが最初にやったのもこの比べ方です。
- **注意点**: 契約書には取引先の秘密が含まれるので、入力した内容が学習に使われない会社向けの契約で使うことが前提です。AIの要約だけで判断せず、元の条文を必ず確かめる仕組みを作ってください。日本で弁護士でない人が他人の法律事務を有料で扱うことは弁護士法の制限があるため、外部向けのサービスにするなら弁護士の関与が必要です。業務で使うチャットAIの選び方は[チャットAIのおすすめと料金比較](/best/chat/)にまとめています。
