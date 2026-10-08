---
{
  "title": "Copilotがパソコン内のファイルを読んで整理や不具合対応まで代行、MicrosoftがWindowsの新機能",
  "description": "MicrosoftはWindowsのCopilotが、利用者の許可を得てパソコン内のファイルや最近の作業を読み、ファイル整理や不具合の診断まで代わりに行えるようにすると発表した。対象はCopilot+ PCで、数か月かけて配信する。",
  "date": "2026-10-08T20:05:00+09:00",
  "category": "products",
  "tags": ["Microsoft", "Copilot", "Windows", "エージェント", "Surface Laptop Ultra", "新機能"],
  "summary": [
    "MicrosoftはWindowsのCopilotが、利用者の許可を得てパソコン内のファイルや最近の作業内容を読めるようにすると発表した",
    "Copilotはファイルの整理や不具合の診断などをWindows上で代わりに行い、軽い仕事はパソコン内のAIで処理して費用を抑える",
    "対象はAI処理用の部品を積んだCopilot+ PCで、今後数か月かけて配信する。タスクバーの検索にも数千の操作が加わる"
  ],
  "sources": [
    {"title": "Building Windows for hybrid intelligence", "publisher": "Windows Experience Blog", "url": "https://blogs.windows.com/windowsexperience/2026/10/07/building-windows-for-hybrid-intelligence/", "kind": "公式発表"},
    {"title": "From searching to doing: Building a faster, more streamlined Windows Search", "publisher": "Windows Insider Blog", "url": "https://blogs.windows.com/windows-insider/2026/10/07/from-searching-to-doing-building-a-faster-more-streamlined-windows-search/", "kind": "公式発表"},
    {"title": "Everything announced at Microsoft's Windows and Surface event", "publisher": "Engadget", "url": "https://www.engadget.com/2280298/everything-announced-at-microsofts-windows-and-surface-event/", "kind": "報道"}
  ],
  "thumb_text": "Copilot",
  "thumb_style": "photo",
  "thumb_prompt": "A cluttered office desk at dusk where an open laptop is surrounded by paper documents that are lifting off the desk and sorting themselves into neat labeled folders in mid-air, while the office chair in front of it sits empty.",
  "share_text": "WindowsのCopilotが、許可すればパソコン内のファイルを読んで整理や不具合対応まで代行するように",
  "editor_note": ""
}
---
Microsoftは現地時間10月7日、WindowsのAIアシスタント「Copilot」が、利用者の許可を得てパソコンの中のファイルや最近の作業内容を読み、ファイルの整理や不具合の診断まで代わりに行えるようにすると発表しました。対象はAI処理用の部品を積んだ「Copilot+ PC」で、今後数か月かけて順次配信します。

## 何が発表されたか

発表はWindowsとSurfaceの新製品イベントに合わせたもので、Windows担当のパヴァン・ダヴルリ上級副社長が公式ブログで全体像を説明しました。Microsoftはこの方向性を「ハイブリッド・インテリジェンス」と呼んでいます。パソコンの中で動くAIと、ネットの向こうのデータセンターで動くAIを、仕事に応じて使い分けるという考え方です。

Copilotに加わる力は3つあります。

- **パソコンの中身を理解する**: 許可すれば、パソコン内のファイルや最近の作業を読み、質問や依頼に生かします
- **代わりに操作する**: ファイルの整理、パソコンの不調の診断、トラブルの解決、プログラムの作成、決まった手順の作業などを、Windows上で直接こなします
- **パソコンの中のAIを使う**: 向いている仕事はパソコン内のAIで処理し、必要なときだけデータセンターのAIと組み合わせます

:::quote https://blogs.windows.com/windowsexperience/2026/10/07/building-windows-for-hybrid-intelligence/ | Windows Experience Blog「Building Windows for hybrid intelligence」
> Copilot can take action on your behalf across Windows, helping complete tasks like organizing files, assessing device diagnostics, troubleshooting issues, coding, and carrying out workflows directly on your device.
CopilotはWindows全体であなたの代わりに操作し、ファイルの整理、端末の診断、問題の解決、コーディング、一連の作業をパソコン上で直接こなす手助けをする。
:::

Copilotは最近、「Home」「Code」「Autopilot」の3つの使い方を軸に作り直されています。今回の変更で、Homeでは作業中のファイルを取り込んで共有用の資料にまとめ、Codeでは一言の指示からWindows用のアプリを作れるようになります。Autopilotは、利用者が別のことをしている間も作業を続ける常駐型の助手として、パソコンの中身と操作の権限を持つようになります。

タスクバーの検索も変わります。「ダークモードにして」「画面を暗くして」「ウィンドウを全部最小化して」のように打ち込むと、設定画面を開かずにその場で実行できる操作が数千種類加わります。まずは試験版を使う登録者（Windows Insider）向けに10月7日から英語だけで始まり、検索欄からCopilotと会話する機能は、希望者向けに年内に一部の国から提供するとしています。

{{card:https://blogs.windows.com/windows-insider/2026/10/07/from-searching-to-doing-building-a-faster-more-streamlined-windows-search/|From searching to doing: Building a faster, more streamlined Windows Search|Windows Insider Blog}}

## AIに任せる範囲をどう縛るか

AIがファイルを読み、操作まで行うとなると、どこまで触らせるかが問題になります。Microsoftは同じ日に、AIエージェント（指示を受けて自分で作業を進めるAI）が触れてよいファイルやネットワークを企業が決め、動作中もその範囲に閉じ込める仕組み「Microsoft Execution Containers（MXC）」をWindows 11で正式に提供し始めました。

対応するエージェントには、OpenAIのCodexやGitHub Copilotが入り、AnthropicのClaude Code、Manus、Perplexityなども対応を予定しています。MetaのAIエージェント「Muse」もWindows用のアプリとして近く登場するとしています。

## 背景

Microsoftが今回、パソコンの中で動くAIを前面に出したのは、データセンターのAIを使うほど費用がかさむためです。ブログでは、パソコン内のAIを併用することで利用者の「トークン（AIの利用量を数える単位）をより長く持たせる」と書いています。

それを支える新しいパソコンも発表されました。NVIDIAの新しい半導体「RTX Spark」を積んだ「Surface Laptop Ultra」は、最大128GBのメモリーを持ち、Microsoftによると1200億を超える規模のAIをパソコン単体で動かせます。予約は同日に始まり、10月16日に発売されます。Engadgetによると価格は2,599ドルからです。ASUS、Dell、HP、Lenovo、MSIからも同じ半導体を積んだ機種が出ます。

## 反応と論点

便利さの裏で、プライバシーへの懸念は避けられません。MicrosoftはかつてWindowsの画面を定期的に記録して後から探せる機能「Recall」で強い批判を受け、提供を遅らせた経緯があります。今回は「許可を得て」読むと繰り返し強調していますが、許可の画面がどう示されるか、どのファイルまで読めるかといった細かい仕組みは、ブログには書かれていません。

:::quote https://blogs.windows.com/windowsexperience/2026/10/07/building-windows-for-hybrid-intelligence/ | Windows Experience Blog「Building Windows for hybrid intelligence」
> Copilot understands your PC, takes action with your permission, and uses local models when it makes sense, with you in control at every step.
Copilotはあなたのパソコンを理解し、あなたの許可を得て操作し、理にかなう場面ではパソコン内のAIを使う。どの段階でも主導権はあなたにある。
:::

もう1つの論点は対象機種の狭さです。新しいCopilotの力が使えるのはCopilot+ PCに限られ、配信時期も機種や国、半導体によって違うとしています。手元のパソコンが古ければ、買い替えるまで恩恵はありません。

## 日本のビジネスへの影響

- **使えるか**: 対象はCopilot+ PCで、配信は「今後数か月」です。日本での提供時期と日本語対応は発表されていません。新しい検索の操作も、まずは英語の試験版からです。料金の変更は発表されておらず、Copilotの各プランの料金は[チャットAIの選び方ガイド](/best/chat/)にまとめています
- **誰に効くか**: 毎日WordやExcelの資料を探しては作り直している営業・企画の担当者と、社員のパソコンの不具合対応に追われる情報システム担当です。「先週の会議資料をもとに提案書の下書きを」「この遅さの原因を調べて」といった依頼をCopilotに任せられるようになります
- **今すぐやれること**: 情報システム担当は、社内のパソコンのうちCopilot+ PCがどれだけあるかを確かめ、次の入れ替え計画に入れるかを検討しておくとよいでしょう。あわせて、Copilotに読ませてよいフォルダと読ませたくないフォルダ（人事や顧客の情報など）を先に分けておくと、配信が始まったときに迷わずに済みます
- **注意点**: AIが操作まで行う機能は、間違ったファイルを動かしたり消したりする危険もあります。最初は個人の作業用フォルダなど影響の小さい範囲から試し、顧客情報を扱う部署では社内ルールを決めてから使うのが安全です
