---
{
  "title": "難しい病気の診断でAIが医師の2倍以上正解、Microsoftの研究が科学誌Scienceに 実際の病院でも試験へ",
  "description": "Microsoftの診断AI「MAI-DxO」が、難しい症例304件で83%を正しく診断し、参考資料を使った医師の36%を大きく上回ったという論文がScienceに載った。検査費用は半分から3分の1。米ボストンの病院で患者を対象にした試験も始める。",
  "date": "2026-10-23T10:15:00+09:00",
  "category": "research",
  "tags": ["Microsoft", "MAI-DxO", "医療", "論文", "GPT-5.5"],
  "summary": [
    "Microsoftの診断AI「MAI-DxO」が、医学誌に載った難しい症例304件で83%を正しく診断し、資料を使える医師の36%を上回った",
    "MAI-DxOは複数のAIに医師団のように話し合わせて検査を選ぶ仕組みで、検査費用は医師の半分から3分の1で済んだとMicrosoftは発表した",
    "比べた医師は総合診療医などで専門医は含まれず、伸びの多くは土台のAIの性能によるとの指摘もある。今後は実際の病院で患者を相手に試す"
  ],
  "sources": [
    {"title": "Building medical superintelligence", "publisher": "Microsoft AI", "url": "https://microsoft.ai/news/building-medical-superintelligence/", "kind": "公式発表"},
    {"title": "Microsoft's Mustafa Suleyman says its AI outperforms doctors on hard cases as he chases 'medical superintelligence'", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/10/22/microsofts-mustafa-suleyman-says-its-ai-outperforms-doctors-on-hard-cases-as-he-chases-medical-superintelligence/", "kind": "報道"}
  ],
  "thumb_prompt": "Five small friendly robots in white doctor coats seated around a round table, debating over a single patient chart and a tray of test tubes, while one robot crosses out an expensive scan from the list.",
  "thumb_style": "3d",
  "thumb_text": "MAI-DxO",
  "share_text": "難しい病気の診断でMicrosoftのAIが83%正解、資料を使う医師は36%。Scienceに論文、次は実際の病院で試験",
  "editor_note": ""
}
---
Microsoftは現地時間10月22日、診断を手伝うAI「MAI-DxO」が、難しい症例の診断で医師を大きく上回ったとする論文が科学誌Scienceに掲載されたと発表しました。医学誌に載った難しい症例304件で、MAI-DxOは83%を正しく診断し、教科書やネットを使える医師の正解率36%の2倍以上でした。次は米ボストンの病院で、実際の患者を相手に試します。

## 何が発表されたか

MAI-DxOとは、MicrosoftのAI部門Microsoft AIが作った、複数のAIを「仮想の医師団」として動かす診断の仕組みです。AIたちが診断の候補を出し合い、どの検査をするかを決め、検査費用も気にしながら何度も話し合って結論を出します。土台には、OpenAIやGoogle、Anthropic、DeepSeekなど各社の対話AIを使えます。

試験は、医師が患者に質問し、検査を頼み、結果を見て絞り込んでいく実際の診察の流れをまねて行われました。問題として使われたのは、米国の医学誌NEJMに載った難しい症例304件と、救急外来によくある症例を集めた別のデータです。

:::quote https://microsoft.ai/news/building-medical-superintelligence/ | Microsoft AI「Building medical superintelligence」
> On complex NEJM cases, MAI-DxO achieved 83% diagnostic accuracy.
NEJMの難しい症例で、MAI-DxOは83%の診断正解率を達成した。
:::

結果をまとめると次のとおりです。

| 症例 | MAI-DxO | 医師 |
|---|---|---|
| 難しい症例（NEJM、304件） | 83% | 資料なし22%、資料あり36% |
| 救急外来のよくある症例 | 80% | 47% |

費用の面では、MAI-DxOは医師より少ない検査で正しい診断にたどり着き、かかった検査費用は半分から3分の1だったとMicrosoftは説明しています。費用を抑える設定にした場合でも、難しい症例で81%を正解しました。試験の仕組み（SDBench）は一部の症例について無料公開され、ほかの研究者が同じ条件で確かめられるようにしています。

## 何がAIの手柄なのか

注目されているのは、伸びのどこまでがMAI-DxOの「話し合わせる仕組み」によるもので、どこからが土台のAIの賢さによるものかです。TechCrunchが論文のデータをもとに報じたところでは、OpenAIのGPT-5.5を単独で使うと難しい症例の正解率は72%でしたが、MAI-DxOに組み込むと87%近くまで上がりました。性能が低めのGoogleのGemini 2.5 Flashでも、単独の46.4%から69%近くに伸びています。

一方で、救急外来の症例では、単独のAIでもMAI-DxOでも正解率は85%前後とほぼ同じでした。同紙は、仕組みの効果は難しい症例や性能の低いAIほど大きいものの、AIどうしの性能差のほうがその上積みより大きいと指摘しています。Microsoftの研究者も、土台のAIが満点に近づくほど上積みは小さくなると認めているといいます。

比べた相手にも注意が要ります。試験に参加したのは総合診療医や一般内科医で、それぞれ1人で診断しました。本来こうした難しい症例を受け持つ専門医や、医師のチームとは比べていません。

## これからどうなるか

Microsoftは、ボストンのBeth Israel Deaconess Medical Centerと組み、病院の現場で患者が直接このAIとやりとりする試験を行うと発表しました。同意した患者は通常の診療を受けつつAIとも対話し、AIの判断と医師の独自の判断を比べます。発表文では、ここからが本当の試験だと位置づけています。

:::quote https://microsoft.ai/news/building-medical-superintelligence/ | Microsoft AI「Building medical superintelligence」
> Benchmarks matter, but the true test is performance in real clinical environments.
試験の点数は大事だが、本当の試験は実際の診療の場でどれだけ力を発揮できるかだ。
:::

Microsoft AIのムスタファ・スレイマンCEOは今回の結果を「医療の超知能」への一歩と呼んでいると、TechCrunchが報じています。MicrosoftはMayo Clinicと医療向けのAIモデルを共同で開発しており、TechCrunchによると来年の公開を予定しています。診断AIそのものを製品として医療機関に提供する時期は、発表文には書かれていません。

## 日本のビジネスへの影響

- **使えるか**: MAI-DxOは研究段階で、製品としての提供や日本での利用は発表されていません。試験に使った症例も米国の医学誌と米国の救急外来のもので、日本語や日本の診療の流れでの性能は分かっていません
- **誰にどう効くか**: 医療機関の経営者や、医療・ヘルスケア分野の事業担当者には、「AIが診断の第2の意見を出し、余分な検査を減らす」という使い方が現実味を帯びてきたことを示す結果です。保険会社や健康診断サービスの企画担当者にとっても、検査費用を抑える根拠として参考になります
- **今すぐやれること**: 今は様子見でよい段階です。社内で医療やヘルスケアのAI活用を検討しているなら、公開された試験の仕組みや論文を読み、「どの医師と比べたか」「どの土台のAIを使ったか」を確認する習慣をつけておくと、今後出てくる製品の宣伝文句を見極めやすくなります
- **注意点**: 「医師の4倍正確」といった数字は、資料を使わない一般の医師との比較から出たものです。日本では診断は医師が行うもので、AIの判断をそのまま患者に伝える使い方は医療関係の法律上の論点にもなります。数字だけで導入を判断しないことが大切です

MAI-DxOの土台にもなるChatGPTやClaude、Geminiの違いと料金は、[チャットAIのおすすめと料金比較](/best/chat/)にまとめています。
