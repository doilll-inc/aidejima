"""AIの料金計算（/tools/ryoukin/）のデータを作る。build.py から使い、単体でも点検できる。

  python3 ryoukin.py check    # 補助データ（data/ryoukin.json）が今のガイドの料金と合っているかを点検（合わない行があれば終了コード1）

料金そのものは data/guides/*.json（/best/ のガイド。guides.yml が毎日点検して直す）から読む。
data/ryoukin.json には「その料金が月払いか年払いか」「何人から使えるか」など、計算に要る読み方だけを置く。
補助データに書いた数字・語句は、そのプランの公式の表記（as_shown）・説明（detail）・製品の注記（pricing.note）に
書いてあるものだけを使う。点検で表記が変わって合わなくなった行は使わず、注意を出す（推測で埋めない）。
"""
from __future__ import annotations

import json
import re
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OVERLAY_FILE = ROOT / "data" / "ryoukin.json"
PATH = "/tools/ryoukin/"
# 公式の表記に年払いをにおわせる語があるのに補助データが無いプランは、月払いか年払いかを決めつけない
ANNUAL_CUE = re.compile(r"年|annual|yearly|billed|/yr|\byear\b", re.I)
NUM_FIELDS = ("m", "ym", "y", "min", "max")
TEXT_FIELDS = ("note", "who")
CUR_SYMBOL = {"USD": "$", "JPY": "¥", "EUR": "€", "GBP": "£"}


def load_overlay_checked() -> tuple[dict, list[str]]:
    """data/ryoukin.json を読む。壊れていても止めず、補助データなしで動けるようにして注意を返す"""
    if not OVERLAY_FILE.exists():
        return {"plans": []}, []
    try:
        data = json.loads(OVERLAY_FILE.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        return {"plans": []}, [f"data/ryoukin.json を読めない（{e}）。補助データなしで計算する（年払いの語がある料金は「区別なし」になる）"]
    if not isinstance(data, dict):
        return {"plans": []}, ["data/ryoukin.json の形が違う（全体が {…} でない）。補助データなしで計算する"]
    if not isinstance(data.get("plans", []), list):
        data["plans"] = []
        return data, ["data/ryoukin.json の plans が配列でない。補助データなしで計算する"]
    return data, []


def load_overlay() -> dict:
    return load_overlay_checked()[0]


def numbers_in(text: str) -> set[float]:
    """文中の数字（3桁区切りのカンマは外す）"""
    t = re.sub(r"(?<=\d),(?=\d{3})", "", text or "")
    return {float(x) for x in re.findall(r"\d+(?:\.\d+)?", t)}


def fmt_money(v: float | None, cur: str) -> str:
    if v is None:
        return "—"
    sym = CUR_SYMBOL.get(cur, (cur + " ") if cur else "")
    if cur == "JPY":
        return f"{sym}{round(v):,}"
    r = round(v + 1e-9, 2)
    return f"{sym}{r:,.0f}" if float(r).is_integer() else f"{sym}{r:,.2f}"


def host_of(url: str) -> str:
    try:
        return urllib.parse.urlsplit(url).netloc.lower().removeprefix("www.")
    except ValueError:
        return ""


def row_problems(row: dict, text: str) -> list[str]:
    """補助データの1行が、そのプラン自身の文（公式の表記・説明・製品の注記）と合っているか。合わない点を返す"""
    nums = numbers_in(text)
    bad: list[str] = []
    for k in NUM_FIELDS + ("y_mult",):
        v = row.get(k)
        if v is None:
            continue
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            bad.append(f"{k}={v!r}（数値でない）")
        elif k != "y_mult" and float(v) not in nums:
            bad.append(f"{k}={v}")
    for k in TEXT_FIELDS:
        v = row.get(k)
        if v not in (None, "") and (not isinstance(v, str) or v not in text):
            bad.append(f"{k}「{v}」")
    ev = row.get("evidence") or []
    if not isinstance(ev, list):
        bad.append("evidence が配列でない")
    else:
        bad += [f"evidence「{e}」" for e in ev if not isinstance(e, str) or e not in text]
    if row.get("only") not in (None, "m", "y"):
        bad.append(f"only={row.get('only')!r}")
    if row.get("kind") not in (None, "personal", "seat", "team"):
        bad.append(f"kind={row.get('kind')!r}")
    return bad


def index_rows(overlay: dict) -> tuple[dict[str, list[dict]], list[str]]:
    """公式の表記 → 補助データの行（ファイルの順）。形の壊れた行は使わない"""
    by_shown: dict[str, list[dict]] = {}
    warns: list[str] = []
    for i, row in enumerate(overlay.get("plans") or []):
        if not isinstance(row, dict) or not isinstance(row.get("as_shown"), str) or not row["as_shown"]:
            warns.append(f"補助データの plans[{i}] の形が違う（as_shown が無い）ので使わない")
            continue
        if "guides" in row and not (isinstance(row["guides"], list) and all(isinstance(x, str) for x in row["guides"])):
            warns.append(f"補助データの guides が配列でないので使わない: {row['as_shown'][:50]}")
            continue
        by_shown.setdefault(row["as_shown"], []).append(row)
    return by_shown, warns


def pick_row(cands: list[dict], text: str) -> tuple[dict | None, list[str]]:
    """候補の行のうち、そのプランの文と合う最初の行。どれも合わなければ (None, 合わない点)"""
    fails: list[str] = []
    for r in cands:
        bad = row_problems(r, text)
        if not bad:
            return r, []
        fails += bad
    return None, fails


def normalize_plan(pl: dict, row: dict | None, where: str, warns: list[str], dropped: bool = False, quiet: bool = False) -> dict:
    """ガイドのプラン1つ → 計算用の形。数字はガイドの amount か、照合済みの補助データだけ。
    dropped=補助データの行があったのにこのプランの文と合わなかった（料金や注記が変わった）。月払いか年払いかを決めつけない"""
    amount, per, shown = pl.get("amount"), pl.get("per"), pl.get("as_shown") or ""
    out = {
        "name": pl.get("name", ""),
        "cur": pl.get("currency") or "",
        "shown": shown,
        "url": pl.get("source_url", ""),
        "checked": pl.get("checked", ""),
        "kind": "seat" if per == "seat_month" else "personal",
    }
    row = row or {}
    has_num = any(row.get(k) is not None for k in ("m", "ym", "y"))
    m = ym = y = None
    if dropped:
        if amount is not None:
            out["p"] = amount
    elif row.get("unk"):
        if amount is not None:
            out["p"] = amount
    elif has_num:
        m, ym, y = row.get("m"), row.get("ym"), row.get("y")
    elif amount is not None and per in ("month", "seat_month", "year"):
        if not row and ANNUAL_CUE.search(shown):
            # 年払いの表記があるのに読み方が無い。月払いと決めつけず「区別なし」で出す
            out["p"] = amount
            if not quiet:
                warns.append(f"{where}「{pl.get('name')}」: 公式の表記に年払いの語があるが補助データが無い（data/ryoukin.json に足す）: {shown[:50]}")
        elif per == "year":
            y = amount
        else:
            m = amount
    if row.get("y_mult") and m is not None and y is None:
        y = round(m * row["y_mult"], 2)
        out["yrule"] = f"年払いは月額×{row['y_mult']}"
    for k, v in (("m", m), ("ym", ym), ("y", y)):
        if v is not None:
            out[k] = v
    for k in ("only", "min", "max", "note", "who"):
        if row.get(k) not in (None, ""):
            out[k] = row[k]
    for k in ("from", "usage"):
        if row.get(k):
            out[k] = True
    if row.get("kind"):
        out["kind"] = row["kind"]
    if not any(k in out for k in ("m", "ym", "y", "p")):
        out["na"] = True  # 要問い合わせ・他プランに含まれる等。表記だけ出す
    return out


def build_data(guides: list[dict], base_path: str = "") -> tuple[dict, list[str]]:
    """公開中のガイド → ブラウザ用のデータ。戻り値: (データ, 注意)"""
    overlay, warns = load_overlay_checked()
    quiet = bool(warns)  # ファイルごと読めないときは、プランごとの「補助データが無い」は出さない（原因は1つ）
    rows, w = index_rows(overlay)
    warns += w
    used: set[int] = set()
    tried: set[int] = set()
    def typed(key: str, kind: type):
        v = overlay.get(key)
        if v is not None and not isinstance(v, kind):
            warns.append(f"data/ryoukin.json の {key} の形が違うので使わない")
            return kind()
        return v or kind()

    skip = set(typed("skip_guides", list))
    defaults = typed("defaults", dict)
    out_guides = []
    for g in guides:
        if g.get("status") != "published" or g.get("slug") in skip:
            continue
        slug = g["slug"]
        prods = sorted(
            [p for p in g.get("products") or [] if p.get("status") in ("featured", "listed")],
            key=lambda p: (p.get("status") != "featured", p.get("rank", 99), p.get("name", "")),
        )
        items = []
        for p in prods:
            pr = p.get("pricing") or {}
            plans = []
            for pl in pr.get("plans") or []:
                shown = pl.get("as_shown", "")
                where = f"{slug}/{p['id']}"
                # 同じ表記でもガイドごとに、そのプラン自身の文（表記・説明・その製品の注記）だけで照合する
                cands = [r for r in rows.get(shown, []) if not r.get("guides") or slug in r["guides"]]
                row, fails = pick_row(cands, " ".join([shown, pl.get("detail", ""), pr.get("note", "")]))
                tried.update(id(r) for r in cands)
                if row:
                    used.add(id(row))
                elif cands:
                    warns.append(
                        f"{where}「{pl.get('name')}」: 補助データが合わないので使わず、月払いか年払いか分からない扱いにする（{', '.join(fails)}。"
                        f"このガイドの文に無い数字・語句か、形の誤り。料金が変わったら data/ryoukin.json を直す）: {shown[:50]}"
                    )
                plans.append(normalize_plan(pl, row, where, warns, dropped=bool(cands) and not row, quiet=quiet))
            if not any(not pl.get("na") for pl in plans):
                continue
            free = pr.get("free") or {}
            srcs: dict[str, str] = {}
            for f in [free] + list(pr.get("plans") or []):
                if f.get("source_url"):
                    srcs[f["source_url"]] = max(srcs.get(f["source_url"], ""), f.get("checked", ""))
            items.append({
                "id": p["id"],
                "name": p.get("name", ""),
                "vendor": p.get("vendor", ""),
                "url": p.get("url", ""),
                "featured": p.get("status") == "featured",
                "free": {"available": free.get("available"), "detail": free.get("detail", ""), "url": free.get("source_url", ""), "checked": free.get("checked", "")} if free else None,
                "plans": plans,
                "note": pr.get("note", ""),
                "sources": [{"url": u, "host": host_of(u), "checked": c} for u, c in sorted(srcs.items(), key=lambda kv: kv[1], reverse=True)],
            })
        if not items:
            continue
        ids = [i["id"] for i in items]
        want = [i for i in defaults.get(slug, []) if i in ids] or [i["id"] for i in items if i["featured"]][:4] or ids[:4]
        out_guides.append({
            "slug": slug,
            "name": g.get("short_name", slug),
            "title": g.get("full_title") or g.get("title", ""),
            "path": base_path + f"/best/{slug}/",
            "reviewed": g.get("last_reviewed", ""),
            "defaults": want,
            "products": items,
        })
    for shown, rs in rows.items():
        for r in rs:
            if id(r) not in used and id(r) not in tried:
                scope = f"（{','.join(r['guides'])}）" if r.get("guides") else ""
                warns.append(f"補助データの行がどのプランにも当たらない（ガイドの点検で表記が変わった？）: {shown[:50]}{scope}")
    data = {
        "path": base_path + PATH,
        "guides": out_guides,
        "home": [i for i in typed("home_products", list) if isinstance(i, str)],
    }
    return data, warns


def link_for(guide_slug: str, product_id: str) -> str:
    return f"{PATH}?g={guide_slug}&p={product_id}"


def stats(data: dict) -> dict:
    prods = [p for g in data["guides"] for p in g["products"]]
    plans = [pl for p in prods for pl in p["plans"] if not pl.get("na")]
    return {
        "guides": len(data["guides"]),
        "products": len(prods),
        "plans": len(plans),
        "both": sum(1 for pl in plans if pl.get("m") is not None and (pl.get("y") is not None or pl.get("ym") is not None)),
        "unknown_basis": sum(1 for pl in plans if "p" in pl),
    }


def static_rows(product: dict) -> list[dict]:
    """ページに最初から出す表（1人あたりの月払い・年払い）の行。JS が無くても読める"""
    rows = []
    for pl in product["plans"]:
        cur = pl["cur"]
        frm = "〜" if pl.get("from") else ""
        if pl.get("na"):
            rows.append({"plan": pl["name"], "monthly": pl["shown"], "annual": "", "checked": pl["checked"], "na": True})
            continue
        if "p" in pl:
            mo = f"{fmt_money(pl['p'], cur)}{frm}（月払いか年払いかの区別なし）"
            an = "記載なし"
        else:
            if pl.get("m") is not None:
                mo = fmt_money(pl["m"], cur) + frm
            else:
                mo = "年払いのみ" if pl.get("only") == "y" else "記載なし"
            if pl.get("y") is not None:
                an = f"{fmt_money(pl['y'], cur)}{frm}/年" + (f"（月あたり{fmt_money(pl['ym'], cur)}）" if pl.get("ym") is not None else "")
            elif pl.get("ym") is not None:
                an = f"月あたり{fmt_money(pl['ym'], cur)}{frm}"
            elif pl.get("only") == "m":
                an = "なし（月払いのみ）"
            else:
                an = "記載なし"
        rows.append({"plan": pl["name"], "monthly": mo, "annual": an, "checked": pl["checked"], "seat": pl.get("kind") == "seat"})
    return rows


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] != "check":
        print(__doc__)
        return 2
    import guides as guides_mod

    gs = [g for g in guides_mod.load_all() if g.get("status") == "published"]
    data, warns = build_data(gs)
    s = stats(data)
    print(f"料金計算: ガイド{s['guides']}本・製品{s['products']}・計算できるプラン{s['plans']}（月払いと年払いの両方が分かる {s['both']}・区別なし {s['unknown_basis']}）")
    for g in data["guides"]:
        print(f"  {g['slug']}: " + "、".join(p["name"] for p in g["products"]))
    for w in warns:
        print("  注意:", w)
    return 1 if warns else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
