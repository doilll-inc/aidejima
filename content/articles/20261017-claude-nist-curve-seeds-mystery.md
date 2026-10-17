---
{
  "title": "Claudeが30分で解いた暗号の謎、NSAが説明しなかった数字は1990年代の「時刻」から作られていた",
  "description": "Anthropicは10月16日、ネットの電子署名に使う暗号の設定値の出どころを社内のClaudeが30分足らずで突き止めたと発表した。NSAが説明なしに渡し「裏口」が疑われた数字は、1997〜98年の時刻から作った乱数だった。",
  "date": "2026-10-17T09:55:00+09:00",
  "category": "research",
  "tags": ["Anthropic", "Claude", "Frontier Red Team", "暗号", "セキュリティ", "NSA"],
  "summary": [
    "Anthropicは10月16日、ネットの電子署名に使う暗号の設定値がどう作られたかを、社内のClaudeが30分足らずで解明したと発表した",
    "米国家安全保障局（NSA）が出どころを説明せず、「裏口が仕込まれているのでは」と約25年疑われてきた数字で、正体は1997〜98年の時刻から作った単純な乱数だった",
    "暗号が破られたわけではなく、むしろ裏口の疑いが薄まる結果。3年前からの懸賞金3万6,864ドルは非営利団体に寄付される"
  ],
  "sources": [
    {"title": "Claude reveals ECDSA curve origins", "publisher": "Anthropic", "url": "https://www.anthropic.com/research/ecdsa-curve-origins", "kind": "公式発表"},
    {"title": "The NIST Elliptic Curves Seeds Bounty Has Been Claimed", "publisher": "Filippo Valsorda", "url": "https://words.filippo.io/seeds-solved/", "kind": "公式サイト"},
    {"title": "The NIST Elliptic Curves Seeds Bounty", "publisher": "Filippo Valsorda", "url": "https://words.filippo.io/seeds-bounty/", "kind": "公式サイト"},
    {"title": "Claude reveals ECDSA curve origins（議論）", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=50122800"},
    {"title": "Anthropic Says Claude Traced NIST ECDSA Curve Seeds to a 1990S RNG", "publisher": "Unite.AI", "url": "https://www.unite.ai/anthropic-says-claude-traced-nist-ecdsa-curve-seeds-to-a-1990s-rng/", "kind": "報道"}
  ],
  "thumb_prompt": "A dusty 1990s beige desktop computer in a dim archive room, its old CRT screen glowing with a ticking digital clock, while a modern glowing laptop beside it projects a beam of light that unlocks an old iron padlock resting on the keyboard.",
  "thumb_style": "photo",
  "thumb_text": "暗号の謎を解いたClaude",
  "share_text": "NSAが説明しないまま約25年、「裏口では」と疑われた暗号の数字。Claudeが30分で正体を突き止めたら、1990年代の時刻から作った乱数だった",
  "editor_note": ""
}
---
Claudeを開発する米Anthropicは現地時間10月16日、インターネットの電子署名に使われる暗号の「設定値」がどうやって作られたのかを、社内の研究用Claudeが30分足らずで突き止めたと発表しました。この数字は米国家安全保障局（NSA）が出どころを説明しないまま渡したもので、暗号の専門家の間では「NSAが裏口を仕込んだのでは」という疑いが四半世紀ほど語られてきました。正体は、1997〜98年のパソコンの時刻を元に作った、ごく普通の乱数でした。

## 何が起きたか

対象は、ECDSA（楕円曲線を使った電子署名の方式）です。電子署名は、データが本人から届いたもので途中で書き換えられていないことを確かめる仕組みで、Webサイトの安全な接続などに広く使われています。米国の標準化機関NIST（国立標準技術研究所）は2000年にこの方式の標準を定め、「P-256」などの曲線（暗号の土台になる数式）を推奨しました。

曲線の一部の値は、「シード（種）」と呼ばれる数字から作られています。このシードはNSAが用意したもので、どう選んだのかは示されていませんでした。種を自由に選べるなら、作った側だけが知る弱点を仕込める余地があるのでは、という疑いが消えなかった理由です。

Anthropicの発表によると、社員の1人が10月、社内の研究用モデルに「このシードがどう作られたか突き止められるか」と尋ねました。それまで有力だった手がかりは、あえて伝えずに聞いたといいます。

:::quote https://www.anthropic.com/research/ecdsa-curve-origins | Anthropic「Claude reveals ECDSA curve origins」
> In under half an hour, Claude discovered the origins of the NIST P-192, P-224, P-256, P-384 and P-521 seeds.
30分足らずで、ClaudeはNISTのP-192、P-224、P-256、P-384、P-521のシードの出どころを突き止めた。
:::

## Claudeはどうやって見つけたか

Claudeは「1990年代のプログラムなら、当時よく使われていた乱数の作り方を使ったのでは」と見当を付け、候補となる作り方34通りを総当たりで調べる道具を自分で書きました。そこで、いくつかのシードの先頭の桁がそろってゼロになっている、偶然では起きにくい特徴に気づきます。これが、C言語（1990年代に主流だったプログラミング言語）の標準部品にある乱数の作り方「lrand48」の癖と一致しました。

そこから逆算すると、乱数の出発点はUnix時間（コンピューターが使う時刻の数え方）で、1997年5月〜1998年4月の日時になりました。たとえばP-256のシードは、その時刻から乱数を1,842回分取り出したところに現れます。Anthropicは、同じ手順でシードを再現できるプログラムも公開しています。

発表には、解明した瞬間のClaudeの「考えの途中経過」も載っています。Claudeは「25年来の謎が解けた」と驚いたあと、「自分は試験用の作り物の環境にいるのではないか」と疑い、桁の一致を計算し直して「本物の発見だ」と確かめていました。

## 「裏口」の疑いはどうなったか

Anthropicは、今回の結果は暗号を破ったものではないと明言しています。

:::quote https://www.anthropic.com/research/ecdsa-curve-origins | Anthropic「Claude reveals ECDSA curve origins」
> This is not a cryptographic break, new attack, or weakness in the ECDSA curves. In fact, this makes us more confident the curves were chosen without any backdoors or intentional weaknesses.
これは暗号の解読でも、新しい攻撃でも、ECDSAの曲線の弱点でもない。むしろ、曲線が裏口や意図的な弱点なしに選ばれたという確信が強まった。
:::

時計を元にした単純な乱数なら、誰でも同じ数字を再現できます。作る側が細工できる余地は小さくなります。

この謎には懸賞金がかかっていました。暗号技術者のフィリッポ・ヴァルソルダ氏が2023年10月に呼びかけたもので、寄付を選べば3倍になる仕組みです。同氏のブログによると、Anthropicの10人のチームが10月15日に申請して全額を獲得し、3万6,864ドルを、無料でWebサイトの暗号化証明書を発行する「Let's Encrypt」の運営団体ISRGに寄付します。ヴァルソルダ氏は、時刻の選び方を考えても作る側の自由度は小さく、狙った弱点を仕込むのは無理だと分析しています。

## 反応と論点

米国の技術者が集まる掲示板Hacker Newsでは、600ポイントを超える注目を集めました。陰謀論に決着がついたと歓迎する声が多い一方、「どの時刻を試して捨てたかは分からないので、選んだ余地は残る」という慎重な意見も出ています。この点はAnthropic自身も、何回作り直したかは数字からは分からないと認めています。

ほかにも、似た考え方は以前から一部で提案されていた、人間の研究者の積み重ねがAIの手柄に見えてしまう、という指摘もありました。また、別の種類の曲線の1つ（B-163）のシードと、多くの曲線の「基準点」と呼ばれる値の作り方は、まだ分かっていません。

AnthropicのFrontier Red Team（AIの危険な能力を調べるチーム）は、最近もAIがセキュリティに与える影響を発表しています（[家電にAIが自分をコピーして広がる恐れを警告した件](/news/20261014-anthropic-self-replicating-ai-iot-devices/)）。今回は、AIの調査能力が「疑いを晴らす」方向に使われた例です。

## 日本のビジネスへの影響

- **使えるか**: 解明に使われたのは社内の研究用モデルで、どのモデルかは公表されていません。ただ、公開中のClaudeでも、資料やデータの中から規則性を探す作業は試せます。各社のチャットAIの違いは[チャットAIのガイド](/best/chat/)にまとめています。
- **誰に効くか**: 情報システム部門やセキュリティ担当者には、P-256などの曲線を使い続けてよいかという長年の論点に、一つの根拠が加わりました。経営者や企画職にとっては、専門家が何年も解けなかった問いをAIが短時間で解いた具体例として、社内の「長年の謎」をAIに当ててみる発想の材料になります。
- **今すぐやれること**: 社内で原因が分からないまま放置されているデータの癖（売上の周期、システムの記録の異常など）を1つ選び、データと一緒にClaudeなどに「どういう仕組みで生まれたか仮説を出して確かめて」と頼んでみると、AIの調査の使い方がつかめます。
- **注意点**: 今回は答えを計算で厳密に確かめられる問題でした。AIが出した「もっともらしい説明」は、検証できる形で裏付けを取るまで結論にしないでください。暗号の設定を変える必要はなく、急いで対応することはありません。
