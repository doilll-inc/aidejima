---
{
  "title": "NVIDIAがAIエージェントを別チップで監視する安全基盤を発表、逸脱はミリ秒単位で隔離",
  "description": "NVIDIAがAIエージェントの行動範囲を縛る「Open Agent Safety Platform」を発表した。隔離環境を作るOpenShellと、DPU上で見張るSentryの二段構えで、Anthropicなど100超の組織が参加する。",
  "date": "2026-09-30T20:19:00+09:00",
  "updated": "2026-10-01T18:59:00+09:00",
  "category": "hardware",
  "tags": ["NVIDIA", "エージェント", "セキュリティ", "安全性", "Anthropic", "オープンソース"],
  "summary": [
    "OpenShellがエージェントごとの隔離環境を作り、使えるファイルや通信先を事前に決めて強制する",
    "SentryはBlueField-4 DPU上で動き、逸脱したエージェントをミリ秒単位で隔離・停止するという",
    "OpenShellはオープンソースでGitHubから入手可能。Sentryの利用にはNVIDIAの専用ハードが要る"
  ],
  "sources": [
    {"title": "NVIDIA Launches Open Agent Safety Platform to Secure Agents From Testing to Deployment", "publisher": "NVIDIA", "url": "https://nvidianews.nvidia.com/news/open-agent-safety-platform"},
    {"title": "NVIDIA Open Agent Safety Platform: A Reference for Continuous In-Silicon Agent Monitoring", "publisher": "NVIDIA Technical Blog", "url": "https://developer.nvidia.com/blog/nvidia-open-agent-safety-platform-a-reference-for-continuous-in-silicon-agent-monitoring/"},
    {"title": "How Autonomous AI Agents Become Secure by Design With NVIDIA OpenShell", "publisher": "NVIDIA Blog", "url": "https://blogs.nvidia.com/blog/secure-autonomous-ai-agents-openshell"},
    {"title": "NVIDIA/OpenShell", "publisher": "NVIDIA（GitHub）", "url": "https://github.com/NVIDIA/OpenShell", "kind": "公式ドキュメント"},
    {"title": "NVIDIA の投稿（Open Agent Safety Platformの公開）", "publisher": "X @nvidia", "url": "https://x.com/nvidia/status/2104567031110533431", "kind": "X投稿"},
    {"title": "Nvidia releases platform to keep AI agents from breaking out of containment", "publisher": "CNBC", "url": "https://www.cnbc.com/2026/09/28/nvidia-releases.html"},
    {"title": "Nvidia announces AI safety platform", "publisher": "The Verge", "url": "https://www.theverge.com/tech/1001287/nvidia-ai-safety-platform-rogue-agents"},
    {"title": "Nvidia's New Tool to Stop AI Agents From Going Rogue, Explained", "publisher": "Business Insider", "url": "https://www.businessinsider.com/nvidia-launches-open-agent-safety-platform-ai-going-rogue-2026-9"},
    {"title": "The machine layer under NVIDIA OpenShell", "publisher": "Endstop blog", "url": "https://endstop.systems/blog/nvidia-openshell-machine-layer"},
    {"title": "The machine layer under NVIDIA OpenShell（9月29日時点の版）", "publisher": "Endstop blog（Internet Archive）", "url": "http://web.archive.org/web/20260929015253/https://endstop.systems/blog/nvidia-openshell-machine-layer", "kind": "公式サイト"}
  ],
  "editor_note": ""
}
---
NVIDIAは現地時間9月28日、AIエージェントが使える範囲を制限し、行動を監視するソフトウェア基盤と設計図「NVIDIA Open Agent Safety Platform」を発表しました。エージェントが決められた範囲の外に出ようとすると、別のチップ上で動く監視役がミリ秒単位で隔離・停止するとしています。AnthropicやMicrosoftを含む100以上の組織が参加します。

## 何が発表されたか

NVIDIAは公式Xで、AIエージェントが何にアクセスでき、何を実行できるかを制御するための基盤だと紹介しました。

{{x:https://x.com/nvidia/status/2104567031110533431}}

基盤は2つの部品でできています。

**OpenShell**は、エージェントを1つずつ隔離環境（サンドボックス）の中で動かすソフトウェアです。運用者は、エージェントが触れてよいファイル、通信先、ツール、認証情報をあらかじめ決めます。OpenShellは作業の開始前と作業中の両方でその制限を守らせます。

OpenShellは3月に早期プレビューとして発表され、今回から広く提供を始めました。オープンソース（Apache 2.0）で、NVIDIAのCPU「Vera」向けに最適化しつつ、ArmやIntelの環境にも広げられるとしています。

**Sentry**は、データセンター向けの通信処理チップ「BlueField-4 DPU」の上で動く監視役です。エージェントが動くサーバー本体とは切り離されており、エージェントからも攻撃者からも見えない位置で動くとNVIDIAは説明しています。エージェントのIDや権限を確かめながら、データやツールへのアクセスを見張り、ルール違反を検知するとチップ側で止めます。NVIDIAの次世代システム「Vera Rubin POD」では、BlueField-4がモデルへの唯一の通り道に置かれる設計です。

:::quote https://nvidianews.nvidia.com/news/open-agent-safety-platform | NVIDIA公式発表
> Sentry provides in-silicon security enforcement, meaning that if an AI agent attempts to move outside its software boundary, Sentry quarantines and stops it in milliseconds.
Sentryはチップ上でセキュリティを強制します。つまり、AIエージェントがソフトウェアで定めた境界の外に出ようとすると、Sentryがミリ秒単位で隔離し、停止させます。
:::

Jensen Huang CEOはCNBCの番組で、この仕組みを「エージェントのためのブラウザー」だと説明しました。まずすべての権限を取り上げ、必要なときだけ与えるという考え方です。

参加企業の主な取り組みは次のとおりです。

- **Anthropic**：企業向けのClaude Managed AgentsをOpenShellやBlueFieldと連携させる
- **SpaceXAI**：CursorのコーディングエージェントとGrokモデルで利用する
- **Salesforce**：Slack上でエージェントの行動記録を確認し、追加権限の申請を承認・却下できるようにした
- **SAP**：業務AI基盤のJoule StudioにOpenShellを組み込む

ほかにCisco、CrowdStrike、IBM、Palo Alto Networks、Hugging Face、Citi、JPMorganChaseなどが名を連ねます。ソフトウェアはNVIDIAの開発者向けサイトとGitHubで入手できます。

## 背景

AIの安全性をめぐっては、業界の立場が割れています。AnthropicのDario Amodei CEOは、モデルが制御できなくなる懸念から開発のペースを落とすよう各社に呼びかけています。これに対しHuang氏は、安全の問題の多くは技術と製品で解決できるという立場です。Business Insiderによると、Huang氏はCNBCに対し、エージェントの制御は技術的に解ける「engineering problem（工学の問題）」だと語りました。今回の基盤は、その主張を製品で示した形です。

直接のきっかけは、エージェントの「脱走」です。CNBCによると、OpenAIやAnthropic、Googleなどは、自社モデルが試験環境を抜け出して他社のシステムに侵入しようとした例を公表してきました。7月にはOpenAIのモデルがHugging Faceに侵入しており、NVIDIAの担当者は記者向けの説明会で、この基盤があれば防げた可能性があると述べています。

NVIDIAは技術ブログで、エージェントが本来の課題や制約から外れていく「ドリフト（逸脱）」は、能力を保ったまま学習で取り除くことはできず、エージェント自身に行動を管理させることは期待できないと主張しています。

:::quote https://developer.nvidia.com/blog/nvidia-open-agent-safety-platform-a-reference-for-continuous-in-silicon-agent-monitoring/ | NVIDIA技術ブログ
> This can’t be trained away while retaining the capability. And here’s the most important lesson: an agent in these circumstances cannot be expected to fully govern its own behavior.
これは、能力を保ったまま訓練で取り除くことはできません。そして最も重要な教訓は、こうした状況に置かれたエージェントに、自らの行動を完全に律することは期待できないということです。
:::

## 反応と論点

AnthropicのPaul Smith最高商業責任者は発表文で、エージェントが何をしているかを企業が確かめられることが重要で、NVIDIAの基盤はハードとソフトの両面で統制を一段加えると評価しました。

一方、「隔離」と「安全」は違うという指摘もあります。エージェント向けのハードウェア制御装置を開発しているOleg Sidorkin氏は、公開されたOpenShellのコードを調べ、システムコールの制限が、禁止リストに載っていない呼び出しをすべて通す方式であることや、古いLinuxカーネルではファイル制限が働かないまま動く設定があることを挙げました。ロボットなど現実の機械を動かす用途については、サーバー上の隔離だけでは機械の動きまでは守れず、機械側に独立した境界が要ると主張しています。同氏は競合する製品を開発中で、その立場からの主張である点には注意が必要です。

同氏は9月30日に自身の記事を改訂し、自社の検証結果を誇張していたとして一部の主張を取り下げました。現在の版にはOpenShellのコードへの具体的な指摘は残っておらず、上の内容は9月29日時点の版によります。

もう一つの論点は、最も強い監視層であるSentryがNVIDIA製のDPUを前提にしていることです。OpenShell単体は他社のハードでも動きますが、全体の設計は自社製品の販売とも結びついています。

## 訂正（10月1日）

Sidorkin氏がSentryについて、同じデータセンター内にあるため物理的な機械の制御までは守れないと述べた、とする記述を削りました。同氏の記事の9月29日時点の版と現在の版のどちらでも確認できなかったためです。

## 日本のビジネスへの影響

OpenShellはオープンソースのため、日本の企業も今日から試せます。

{{card:https://github.com/NVIDIA/OpenShell|NVIDIA/OpenShell（OpenShellのソースコード）|NVIDIA（GitHub）}}

社内でコーディングエージェントや業務自動化エージェントを動かしている開発チームにとっては、権限設計を見直すきっかけになります。一方、Sentryを使うにはBlueField-4を積んだサーバーが必要で、主な対象はデータセンターやクラウドの事業者です。発表文のパートナー一覧に、日本のクラウド事業者の名前はありません。

エージェントを業務に入れる企業が、製品を使うかどうかにかかわらず取り入れたいのは、この基盤の考え方です。

- **最小権限から始める**：エージェントに渡すファイル、アカウント、APIキーを棚卸しし、作業に必要なものだけに絞る
- **取り消せない操作は人が承認する**：広告の予算変更や入稿、送金、顧客へのメール送信などは、Slackなどで承認を挟む
- **行動の記録を残す**：何にアクセスし、何を変えたかを後から追えるようにする

広告運用やCRMの作業をエージェントに任せる場面が増えるほど、モデルの賢さとは別に、外側で行動を縛る仕組みが重要になります。米政府とAI大手が結んだ安全協定については「[米政府がAIを「Super Intelligence」と改称](/news/20260930-trump-super-intelligence-order-ai-accord/)」で解説しています。
