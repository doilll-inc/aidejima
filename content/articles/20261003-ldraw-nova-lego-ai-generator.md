---
{
  "title": "ldraw-novaは言葉からLEGOの設計図を作るOSS、GPT-6 AstraとOpus 5.5で組み立て",
  "description": "開発者のanteloc氏が、AIエージェントに指示するだけでLEGOの3D CADモデルを作れるOSS「ldraw-nova」を公開した。部品を直接置かせず生成用のPythonを書かせるのが要点で、作者の概算では複雑なモデル1体で約5ドルかかる。",
  "date": "2026-10-03T10:50:00+09:00",
  "category": "usecases",
  "tags": ["ldraw-nova", "LDraw", "活用事例", "個人開発", "オープンソース", "エージェント"],
  "summary": [
    "ldraw-novaは、AIエージェントに作りたいものを伝えるとLEGOの3D CADモデルをLDraw形式で出力するオープンソースのツール",
    "エージェントに部品の座標を直接計算させず、設計図と生成用Pythonを書かせる「コンパイラ」型の設計が特徴",
    "作者によると大きく正確なモデルはGPT-6 AstraやClaude Opus 5.5級が必要で、Technicの機構は1体約5ドルの概算"
  ],
  "sources": [
    {"title": "anteloc/ldraw-nova", "publisher": "GitHub", "url": "https://github.com/anteloc/ldraw-nova", "kind": "公式サイト"},
    {"title": "Show HN: Made an open-source Lego AI generator", "publisher": "Hacker News", "url": "https://news.ycombinator.com/item?id=49937916"},
    {"title": "ldraw-nova samples", "publisher": "anteloc", "url": "https://anteloc.github.io/index-samples.html", "kind": "公式サイト"},
    {"title": "ldraw-nova デモ動画", "publisher": "YouTube（作者）", "url": "https://youtu.be/YDjjxGqWpgU", "kind": "公式サイト"}
  ],
  "thumb_text": "ldraw-nova",
  "share_text": "言葉で頼むとAIがLEGOの設計図を作るOSS「ldraw-nova」。部品を置かせず生成コードを書かせるのがコツ",
  "thumb_style": "photo",
  "thumb_prompt": "Colorful plastic toy bricks assembling themselves into a detailed castle on a desk, mid-air pieces floating into place, next to a glowing blueprint sheet of abstract lines.",
  "editor_note": ""
}
---
開発者のanteloc氏が、AIエージェントに作りたいものを伝えるとLEGOの3D CADモデルを組み上げるオープンソースのツール「ldraw-nova」を公開し、現地時間10月2日にHacker NewsのShow HNで紹介しました。GPT-6 AstraとClaude Opus 5.5を使って、エージェント向けの道具一式と手順書を作り込んだといいます。投稿は65ポイントを集め、AIで「現実に組める物」を設計させる試みとして議論になりました。

## 何を作ったか

ldraw-novaとは、LEGOのモデルを記述する言語「LDraw」のソースコードを、AIエージェントに書かせるための道具・手順書・見本をまとめたものです。LDrawは、どの部品をどの位置にどの向きで置くかを1行ずつ並べる、いわばLEGO版のアセンブリ言語で、LDViewやLeoCADなどの無料ツールで開くと3Dモデルとして回したり編集したりできます。

組み立てが終わると、次のものが手に入ります。

- LDraw形式のソースファイル（.mpd）
- ブラウザで見られる3Dビューアーや画像、Meta Quest 3向けのVR表示
- Blenderで編集できるglTF（.glb）ファイル
- エージェントとのやりとりと、エージェントの思考の記録

作例の一覧には、クレーン、車両、家が並ぶ街並みなどが公開されています。作者が作ったデモ動画もあります。

{{youtube:https://youtu.be/YDjjxGqWpgU}}

## どう作ったか

いちばんの工夫は、エージェントに部品を直接置かせないことです。作者は昨年12月ごろから、ChatGPTやClaudeにLDrawを書かせる実験を重ね、3つの試作を経て次の結論に達したとREADMEに書いています。

:::quote https://github.com/anteloc/ldraw-nova | GitHub「anteloc/ldraw-nova」README
> there is a minimum resistance path to geometry math for agents
エージェントにとって、幾何学の計算を最も楽に乗り越える道筋がある。
:::

その道筋とは、回転や位置の計算をモデル自身にさせるのではなく、計算をこなすPythonのコードを書かせることです。実際の流れは次のようになります。

1. エージェントが指示文と、LDrawや組み立て方の手順書を読む
2. 部品やサブモデルの構成、見た目を考え、モデル全体を記述した設計図（plan.json）を作る
3. 設計図を読んでLDrawを出力する生成スクリプト（generate.py）を書いて実行する
4. 画像に描画して確かめ、位置や見た目を直す作業を繰り返す

作者は、エージェントが生成器を作り、生成器が3Dモデルを出す構造を「一種のコンパイラ」と表現しています。道具には、合う部品や見本モデルの検索、部品のめり込みやすき間の検出、画面なしでの描画などがそろっています。部品検索には、作者自身が作った意味検索ツール「jev-rerank」を使い、TypeSafeのモデルで結果を並べ替えます。TypeSafeのAPIキーがなければ全文検索で代用しますが、出来が落ちる可能性があるとしています。

こうした道具は以前の試作でもうまくいかなかったものの、GPT-6 AstraとClaude Opus 5.5の登場で「バイブコーディング（AIに任せて書かせる開発）で正しく作れた」と作者は振り返っています。ツールはDockerのWebアプリとしてまとめられ、OpenAI、Anthropic、OpenRouterのモデルを選べます。

## 成果と課題（作者の説明）

Hacker Newsのコメント欄で費用を問われた作者は、モデルにどれだけ考えさせるかで大きく変わるとしたうえで、GPT-6 AstraでTechnic（歯車や軸を使うシリーズ）の機構を1つ作ると約5ドルという「大ざっぱな」見積もりを示しました。部品を置く際の誤りは、見本が多い家のような分野では少ないものの、検証と修正の繰り返しにも頼っていると答えています。

READMEでは、初版ゆえの課題を率直に挙げています。

- 大きく正確なモデルを作れるのは高価な上位モデルだけで、生成も遅い
- Haikuのような軽いモデル向けの調整はこれから
- ミニフィグ、Technicの機械、宇宙船の出来はまだ不十分
- 説明書からの組み立ては部分的にしか動かない

コメント欄では、物理シミュレーションを加えればロボット教育の競技会に使えるという声や、カーネギーメロン大学の「BrickGPT」など関連研究の紹介が続きました。一方で、LEGOという想像の遊びにAIが入り込むことへの違和感を示す人もいました。作者は、数千個の部品が要る大型モデルは実物を組んでおらず、小さなものを3Dプリンターで出力してみるつもりだと答えています。

{{card:https://github.com/anteloc/ldraw-nova|anteloc/ldraw-nova|GitHub}}

## 日本のビジネスへの影響

ldraw-novaはAGPL-3.0で公開されており、GitとDockerがあれば手元のPCで動かせます。初回のビルドに約5GBの空き容量が必要です。ログイン機能がないので、信頼できるネットワークの中だけで使うよう作者は注意しています。なおLEGOはLEGO Groupの商標で、同社はこのソフトを公認していません。

このプロジェクトから学べるのは、LEGOに限らない設計の型です。座標や角度の計算が絡む仕事をAIに任せるとき、答えを直接出させるのではなく、答えを計算するコードと設計図を書かせ、描画して確かめさせる。この型は、店舗の棚割りや展示ブースの配置図、パッケージの展開図など、マーケティングや販促の現場で図面を扱う作業にも応用できます。

試すなら、まずREADMEの手順でDocker版を立ち上げ、作例の家や車両に近い小さなモデルから頼むのが近道です。上位モデルを使うため、APIの利用上限を先に決めておくと安心です。自社の業務に転用する場合、AGPLのコードを改変して外部にサービス提供するとソースの公開義務が生じる点に注意が要ります。手法だけを参考に、自社のコーディングエージェントで同じ流れを組むのも手です。コーディングエージェントの比較は「[コーディングAIのおすすめと料金比較](/best/coding/)」にまとめています。
