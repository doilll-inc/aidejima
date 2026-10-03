---
{
  "title": "AppleがmacOSの「フルディスクアクセス」を厳格化へ、AIエージェントの危険増大を理由に",
  "description": "Appleは10月2日、macOSの「フルディスクアクセス」権限に追加の管理策を入れると開発者向けに告知した。AIエージェントが自律的になるほど危険が「大幅に」増すとし、許可には明確な操作を求める。時期は未定。",
  "date": "2026-10-03T10:30:00+09:00",
  "category": "policy",
  "tags": ["Apple", "macOS", "エージェント", "セキュリティ", "プライバシー"],
  "summary": [
    "Appleは現地時間10月2日、macOSのフルディスクアクセス権限に追加の管理策を導入すると開発者向けに告知した",
    "理由として、AIエージェントが高性能で自律的になるほど、この権限の危険が大幅に増すことを挙げた",
    "導入の時期や対象のmacOSのバージョン、具体的な仕組みはまだ公表されていない"
  ],
  "sources": [
    {"title": "Updates to Full Disk Access in macOS", "publisher": "Apple Developer", "url": "https://developer.apple.com/news/?id=p6zjojqw", "kind": "公式発表"},
    {"title": "Apple says it's tightening macOS 'Full Disk Access' controls due to new risks from AI agents", "publisher": "TechCrunch", "url": "https://techcrunch.com/2026/10/02/apple-says-its-tightening-macos-full-disk-access-controls-due-to-new-risks-from-ai-agents/", "kind": "報道"},
    {"title": "Apple sounds the alarm on AI agents and 'Full Disk Access'", "publisher": "Engadget", "url": "https://www.engadget.com/2276186/apple-sounds-the-alarm-on-ai-agents-and-full-disk-access/", "kind": "報道"},
    {"title": "Apple says it's tightening macOS privacy controls amid the rise of AI agents", "publisher": "9to5Mac", "url": "https://9to5mac.com/2026/10/02/apple-says-its-tightening-macos-privacy-controls-amid-the-rise-of-ai-agents/", "kind": "報道"},
    {"title": "Apple Announces 'Full Disk Access' Changes on macOS Due to AI Agents", "publisher": "MacRumors", "url": "https://www.macrumors.com/2026/10/02/apple-announces-macos-full-disk-access-changes/", "kind": "報道"}
  ],
  "thumb_text": "フルディスクアクセス",
  "share_text": "AppleがmacOSのフルディスクアクセスを厳格化へ。AIエージェントで危険が大幅に増すと開発者に告知",
  "editor_note": ""
}
---
Appleは現地時間10月2日、macOSの「フルディスクアクセス」権限に追加の管理策を導入すると、開発者向けサイトで告知しました。AIエージェントが高性能で自律的になるにつれ、この権限の危険が「大幅に」増すと説明しています。導入の時期や具体的な仕組みは明らかにしていません。

## 何が発表されたか

フルディスクアクセスとは、macOSの「システム設定」にある許可の1つで、認めたアプリはディスク上のほぼすべてのデータを読めるようになります。写真や連絡先のようにデータの種類ごとに許可を求める通常の仕組みとは違い、一度認めると見える範囲が一気に広がります。Appleはこの権限を、Macでバックアップ用のアプリが正しく動くためのものと位置づけています。

今回Appleが打ち出したのは、この許可を出す手順そのものを重くする方針です。

:::quote https://developer.apple.com/news/?id=p6zjojqw | Apple Developer「Updates to Full Disk Access in macOS」
> Going forward, we will introduce additional controls to ensure that users who genuinely wish to grant an app this extraordinary level of access can only do so with very explicit user action. Addressing this is critical.
今後、この並外れた水準のアクセスを本当に許可したい利用者だけが、非常に明確な操作をしたときにのみ許可できるよう、追加の管理策を導入します。これへの対処は極めて重要です。
:::

急ぐ理由としてAppleが挙げたのがAIエージェントです。エージェントの自律性が高まるほど、これだけ広いアクセスに伴う危険は「大幅に」増すとしています。現状についても、利用者が十分に理解しないまま権限を得て、メールやメッセージ、閲覧履歴まで読めてしまうアプリがあるとの認識を示しました。メッセージアプリなら、影響は利用者本人にとどまらず、やりとりの相手にも及びます。

告知は短く、どのmacOSのバージョンから変わるのか、いま許可しているアプリがどうなるのかは書かれていません。TechCrunchや9to5Macも、Appleは導入の日程を示していないと報じています。

{{card:https://developer.apple.com/news/?id=p6zjojqw|Updates to Full Disk Access in macOS|Apple Developer}}

## 背景：Mac上で動くAIエージェントの増加

Appleが名指しはしていないものの、報道各社はMetaの個人向けエージェント「Muse」の一件をきっかけとみています。米Inc.誌のコラムニストが、拒否したつもりのMacのメッセージ履歴をMuseに同期されていたと主張し、Metaはフルディスクアクセスとメッセージ連携の両方を有効にしない限り読めないと反論していました（経緯は「[MetaのAIエージェントMuse、許可の範囲を超え住所送信や私信を同期したと報告相次ぐ](/news/20260930-meta-muse-permission-address-leak/)」）。

9月末には、OpenAIも専用のクラウドPCで常時動く「[Dots](/news/20260930-openai-dots-always-on-agents/)」を始めており、エージェントが利用者の端末やデータに深く入り込む製品が相次いでいます。Engadgetは、MuseやDotsのほかOpenClawのようなエージェントを挙げ、権限への不安から専用の機械でエージェントを動かす利用者が増え、今年のMac miniの品薄にもつながったと報じています。

## 反応と論点

MacRumorsの読者欄では、厳格化を歓迎する声が目立つ一方、バックアップや監視ツールなど正当にこの権限を必要とするアプリへの影響を心配する声や、「全部か無しか」ではなくもっと細かく許可を選びたいという要望も出ています。

論点は2つあります。1つは、Appleの言う「非常に明確な操作」がどの程度の手間になるかです。設定画面を深くたどらせる方式なら誤って許可する事故は減りますが、正規の開発ツールやバックアップアプリの導入も面倒になります。もう1つは、許可さえ取れば何でも読める構造そのものは変わらない点です。AIデジマ編集部は、今回の告知は許可の「入り口」を固める話で、許可した後にエージェントが何を読み、どこへ送ったかを利用者が確かめる仕組みは、引き続き各アプリの側に委ねられているとみています。

## 日本のビジネスへの影響

macOSの変更なので、日本のMac利用者にも同じように及ぶとみられます。ただ、時期や対象バージョンは発表されておらず、現時点で日本向けの個別の案内もありません。

影響が大きいのは、Macでエージェント型のAIアプリを配る開発者と、社内のMacを管理する情報システム担当者です。開発者は、メッセージやメールの読み取りをフルディスクアクセスに頼る設計なら、許可の手順が重くなる前提で、必要なデータだけを個別の権限で読む方式に切り替えられないか検討しておくと安全です。

今すぐやれることは、社内のMacで「システム設定」の「プライバシーとセキュリティ」からフルディスクアクセスの一覧を開き、どのアプリに許可を出しているかを棚卸しすることです。AIアシスタントやエージェントのアプリが入っていれば、業務に本当に必要かを見直します。

注意点として、フルディスクアクセスを許したアプリは、社員本人のデータだけでなく、取引先や顧客とのメッセージも読めます。顧客の個人情報を扱う端末では、個人情報保護法上の第三者提供や委託の扱いに当たらないかも含めて確認しておくべきです。エージェント機能を持つチャットAIの比較は「[チャットAIのおすすめと料金比較](/best/chat/)」にまとめています。
