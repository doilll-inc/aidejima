"""用途別AIガイド（/best/、data/guides/*.json）の読み込みと検証。build.py から使い、単体でも検証できる。

  python3 guides.py check image-generation   # 1本を検証（エラー・注意を表示。エラーがあれば終了コード1）
  python3 guides.py check                    # 全部

検証ルールの正本は docs/guides-design.md §5.3 と data/guides/SCHEMA.md。
"""
from __future__ import annotations

import json
import re
import sys
import urllib.parse
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GUIDES = ROOT / "data" / "guides"
JST = timezone(timedelta(hours=9))
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
FACT_KEYS = ("japanese", "commercial_use", "data_policy", "availability_japan")
STALE_FACT_DAYS = 45
STALE_REVIEW_DAYS = 35
VERDICT_ORDER = ["best-quality", "best-value", "free", "japanese", "commercial", "business", "developer", "beginner", "voice"]


def today() -> date:
    return datetime.now(JST).date()


def parse_day(s: str) -> date | None:
    if not isinstance(s, str) or not DATE_RE.fullmatch(s):
        return None
    try:
        return date.fromisoformat(s)
    except ValueError:
        return None


def host_of(url: str) -> str:
    try:
        return urllib.parse.urlsplit(url).netloc.lower().removeprefix("www.")
    except ValueError:
        return ""


def reg_domain(host: str) -> str:
    """ざっくりした登録ドメイン（example.co.jp / example.com）"""
    parts = host.split(".")
    if len(parts) >= 3 and parts[-2] in ("co", "or", "ne", "go", "ac", "com", "net", "org") and len(parts[-1]) == 2:
        return ".".join(parts[-3:])
    return ".".join(parts[-2:])


def load_index() -> dict:
    p = GUIDES / "_index.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {"groups": [], "nav": []}


def load_all() -> list[dict]:
    out = []
    for p in sorted(GUIDES.glob("*.json")):
        if p.name.startswith("_"):
            continue
        g = json.loads(p.read_text(encoding="utf-8"))
        g["_file"] = p.stem
        out.append(g)
    return out


def iter_facts(prod: dict):
    """製品行の fact（出典と確認日が必要なもの）を (名前, dict) で返す"""
    pr = prod.get("pricing") or {}
    if pr.get("free"):
        yield "pricing.free", pr["free"]
    for i, plan in enumerate(pr.get("plans") or []):
        yield f"pricing.plans[{i}]", plan
    if pr.get("usage"):
        yield "pricing.usage", pr["usage"]
    for k in FACT_KEYS:
        if prod.get(k):
            yield k, prod[k]
    if prod.get("latest"):
        yield "latest", prod["latest"]


def validate(g: dict, official_domains: list[str] | None = None) -> tuple[list[str], list[str]]:
    errs: list[str] = []
    warns: list[str] = []
    name = g.get("_file", g.get("slug", "?"))
    now = today()
    official_domains = official_domains or []

    for k in ("slug", "status", "title", "short_name", "updated", "last_reviewed"):
        if not g.get(k):
            errs.append(f"{k} が空")
    if g.get("slug") and g.get("slug") != g.get("_file", g.get("slug")):
        errs.append(f"slug（{g['slug']}）とファイル名（{g.get('_file')}）が違う")
    published = g.get("status") == "published"
    if published and not (g.get("seo") or {}).get("description"):
        errs.append("seo.description が空")
    title = g.get("title", "")
    if "【" in title or "】" in title or re.search(r"20\d\d", title):
        errs.append("title に【】や年を書かない（build が【YYYY年M月版】を付ける）")
    for k in ("created", "updated", "last_reviewed"):
        if g.get(k):
            d = parse_day(g[k])
            if not d:
                errs.append(f"{k} が YYYY-MM-DD でない")
            elif d > now:
                errs.append(f"{k} が未来日")

    prods = g.get("products") or []
    ids = [p.get("id") for p in prods]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        errs.append(f"products[].id が重複: {sorted(dup)}")
    featured = [p for p in prods if p.get("status") == "featured"]

    for p in prods:
        pid = p.get("id", "?")
        if p.get("status") == "watch":
            continue
        prod_reg = reg_domain(host_of(p.get("url", "")))
        for fname, f in iter_facts(p):
            has_value = any(f.get(k) not in (None, "", []) for k in ("amount", "value", "ui", "output", "available", "training_default", "name", "as_shown", "detail"))
            if not has_value:
                continue
            if not f.get("source_url"):
                errs.append(f"{pid}.{fname}: 出典（source_url）がない")
            if not f.get("checked"):
                errs.append(f"{pid}.{fname}: 確認日（checked）がない")
            else:
                d = parse_day(f["checked"])
                if not d:
                    errs.append(f"{pid}.{fname}: checked が YYYY-MM-DD でない")
                elif d > now:
                    errs.append(f"{pid}.{fname}: checked が未来日")
                elif (now - d).days > STALE_FACT_DAYS:
                    warns.append(f"{pid}.{fname}: 確認日が{(now - d).days}日前（要再確認）")
            src = f.get("source_url", "")
            if src:
                h = host_of(src)
                ok = reg_domain(h) == prod_reg or any(h == dd or h.endswith("." + dd) for dd in official_domains)
                if not ok:
                    warns.append(f"{pid}.{fname}: 出典 {h} が公式ドメインに見えない")
        for k in ("strengths", "weaknesses"):
            for s in p.get(k) or []:
                if len(s) > 40:
                    warns.append(f"{pid}.{k}: 「{s[:20]}…」が長い（30字以内の目安）")

    pick_ids = set(ids)
    for v in g.get("verdicts") or []:
        if v.get("pick") not in pick_ids:
            errs.append(f"verdicts[{v.get('id')}].pick「{v.get('pick')}」が products にない")
        for r in v.get("runner_up") or []:
            if r not in pick_ids:
                errs.append(f"verdicts[{v.get('id')}].runner_up「{r}」が products にない")
        ev = v.get("evidence") or []
        if not ev:
            warns.append(f"verdicts[{v.get('id')}]: 根拠（evidence）がない")
        elif all(e.get("kind") == "editorial" for e in ev):
            if v.get("id") == "best-quality":
                errs.append("verdicts[best-quality]: 根拠が編集部の判断だけ（公式か第三者評価が1つ以上必要）")
            else:
                warns.append(f"verdicts[{v.get('id')}]: 根拠が編集部の判断だけ")
        for e in ev:
            if e.get("kind") != "editorial" and not e.get("url"):
                errs.append(f"verdicts[{v.get('id')}]: 根拠に URL がない")
            if e.get("date") and parse_day(e["date"]) and parse_day(e["date"]) > now:
                errs.append(f"verdicts[{v.get('id')}]: 根拠の日付が未来日")
        if re.search(r"最強|圧倒的|神|ヤバ", v.get("answer", "")):
            warns.append(f"verdicts[{v.get('id')}]: 煽り語を使わない")

    for b in g.get("benchmarks") or []:
        d = parse_day(b.get("checked", ""))
        if not b.get("url"):
            errs.append(f"benchmarks[{b.get('id')}]: URL がない")
        if not d:
            errs.append(f"benchmarks[{b.get('id')}]: checked がない／形式が違う")
        elif (now - d).days > STALE_FACT_DAYS:
            warns.append(f"benchmarks[{b.get('id')}]: 確認日が{(now - d).days}日前")

    if published:
        if not g.get("verdicts"):
            errs.append("published なのに verdicts が空")
        if not featured:
            errs.append("published なのに featured の製品がない")
        elif len(featured) < 3:
            warns.append(f"featured が{len(featured)}行（3行未満は noindex）")
        if (g.get("research_plan") or {}).get("candidates"):
            warns.append("research_plan.candidates が残っている（調査漏れ？公開前に空にする）")
        if len(g.get("faq") or []) < 3:
            warns.append("faq が3問未満")
        if len(g.get("criteria") or []) < 3:
            warns.append("criteria が3つ未満")
        lr = parse_day(g.get("last_reviewed", ""))
        if lr and (now - lr).days > STALE_REVIEW_DAYS:
            warns.append(f"last_reviewed が{(now - lr).days}日前（点検が止まっている）")
    if g.get("editor_note") and g.get("_editor_note_by_ai"):
        errs.append("editor_note は人が書く欄")
    return [f"{name}: {e}" for e in errs], [f"{name}: {w}" for w in warns]


def month_edition(g: dict, now: datetime) -> tuple[str, bool]:
    """【YYYY年M月版】の文字列と、点検が止まっているか"""
    lr = parse_day(g.get("last_reviewed", "")) or now.date()
    stale = (now.date() - lr).days > STALE_REVIEW_DAYS
    d = lr if stale else now.date()
    return f"【{d.year}年{d.month}月版】", stale


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] != "check":
        print(__doc__)
        return 2
    taxo = json.loads((ROOT / "data" / "taxonomy.json").read_text(encoding="utf-8"))
    official = taxo.get("source_kinds", {}).get("official_domains", [])
    want = set(argv[2:])
    bad = 0
    for g in load_all():
        if want and g["_file"] not in want:
            continue
        errs, warns = validate(g, official)
        mark = "NG" if errs else "OK"
        feat = sum(1 for p in g.get("products") or [] if p.get("status") == "featured")
        print(f"[{mark}] {g['_file']}（{g.get('status')}・featured {feat}行・答え {len(g.get('verdicts') or [])}）")
        for e in errs:
            print("  エラー:", e)
        for w in warns:
            print("  注意:", w)
        bad += bool(errs)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
