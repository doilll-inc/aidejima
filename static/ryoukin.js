/* AIの料金計算（/tools/ryoukin/）
   データはページに埋め込んだ JSON（build.py → ryoukin.py が data/guides/*.json から作る）。
   計算はこのブラウザの中だけで行い、入力はどこにも送らない。条件は URL（?g=&p=&n=&b=）に残すので、そのまま共有できる。
   数字はデータにあるものだけを使う。選んだ払い方の料金が無いプランは別の出し方（月払い×12・年払いの月あたり など）で
   表に出すが、その出し方を各行に書き、要約の「一番安い」「同じ額」は、選んだ払い方の料金がそのまま書かれたプランどうしでだけ言う */
(function () {
  "use strict";
  var SYM = { JPY: "¥", USD: "$", EUR: "€", GBP: "£" };

  function money(v, cur) {
    if (v == null || isNaN(v)) return "—";
    var sym = SYM[cur] || (cur ? cur + " " : "");
    if (cur === "JPY") return sym + Math.round(v).toLocaleString("ja-JP");
    var r = Math.round((v + 1e-9) * 100) / 100;
    var s =
      r % 1 === 0
        ? r.toLocaleString("en-US")
        : r.toLocaleString("en-US", {
            minimumFractionDigits: 2,
            maximumFractionDigits: 2,
          });
    return sym + s;
  }

  // プラン1つを、払い方 b（"m"=月払い / "y"=年払い）で払うときの1人（1契約）あたりの料金
  // mon=月あたり / yr=1年分 / unit=どの数字から出したか（m・y・ym）/ approx=目安（約）/ tag=払い方の制約 / flags=出し方の説明
  function price(pl, b) {
    if (pl.na) return null;
    var r = { approx: false, flags: [], tag: "" };
    var m = pl.m,
      y = pl.y,
      ym = pl.ym;
    if (pl.p != null) {
      r.mon = pl.p;
      r.yr = pl.p * 12;
      r.unit = "p";
      r.approx = true;
      r.flags.push(
        "公式の表記からは月払いか年払いかが分からないため、表示の月額の12か月分",
      );
    } else if (b === "m") {
      if (m != null) {
        r.mon = m;
        r.yr = m * 12;
        r.unit = "m";
        if (pl.only === "m") r.tag = "月払いのみ";
      } else if (y != null || ym != null) {
        r.unit = y != null ? "y" : "ym";
        r.yr = y != null ? y : ym * 12;
        r.mon = y != null ? y / 12 : ym;
        r.approx = y == null;
        if (pl.only === "y") r.tag = "年払いのみ";
        else r.flags.push("月払いの料金がデータにないため、年払いで計算");
        if (y == null)
          r.flags.push("年額の記載がないため、年払いの月あたりの額の12か月分");
      }
    } else {
      if (y != null) {
        r.mon = y / 12;
        r.yr = y;
        r.unit = "y";
        if (pl.yrule) r.flags.push("年額は公式の「" + pl.yrule + "」から計算");
      } else if (ym != null) {
        r.mon = ym;
        r.yr = ym * 12;
        r.unit = "ym";
        r.approx = true;
        r.flags.push("年額の記載がないため、年払いの月あたりの額の12か月分");
      } else if (m != null) {
        r.mon = m;
        r.yr = m * 12;
        r.unit = "m";
        if (pl.only === "m") r.tag = "月払いのみ";
        else r.flags.push("年払いの料金がデータにないため、月払いの12か月分");
      }
    }
    if (pl.usage) r.flags.push("シート料金だけの額（従量課金は別）");
    return r.mon == null ? null : r;
  }

  // 人数 n で何契約・何人分払うか
  function seats(pl, n) {
    if (pl.kind === "team") {
      if (pl.max && n > pl.max)
        return { ok: false, why: "1契約で" + pl.max + "人まで" };
      return { ok: true, u: 1, label: "1契約" };
    }
    if (pl.kind === "seat") {
      if (pl.max && n > pl.max) return { ok: false, why: pl.max + "人まで" };
      var u = Math.max(n, pl.min || 1);
      return {
        ok: true,
        u: u,
        label: u > n ? "最低" + pl.min + "人分" : u + "人分",
      };
    }
    return { ok: true, u: n, label: n === 1 ? "1人" : n + "人分の契約" };
  }

  // 選んだ払い方の料金がデータにそのまま書かれていて、「〜から」でも従量課金つきでもない行。要約で比べるのはこれだけ
  function isDirect(r, b) {
    var pl = r.pl;
    if (!r.pr || !r.st.ok || pl.p != null || pl.from || pl.usage) return false;
    return b === "m"
      ? r.pr.unit === "m" && pl.m != null
      : r.pr.unit === "y" && pl.y != null;
  }

  // 要約に書く「その額をどう出したか」（そのままの額なら空）
  function basis(r, b) {
    var pl = r.pl,
      out = [];
    if (pl.p != null) out.push("月払いか年払いか分からない表示の額");
    else if (b === "m" && r.pr.unit === "y")
      out.push(
        (pl.only === "y" ? "年払いのみで" : "月払いの額が書かれておらず") +
          "、年額の12分の1",
      );
    else if (b === "m" && r.pr.unit === "ym")
      out.push(
        (pl.only === "y" ? "年払いのみで" : "月払いの額が書かれておらず") +
          "、年払いの月あたりの額",
      );
    else if (b === "y" && r.pr.unit === "ym")
      out.push("年払いの月あたり" + money(pl.ym, pl.cur) + "の12か月分");
    else if (b === "y" && r.pr.unit === "m")
      out.push(
        (pl.only === "m" ? "年払いがなく" : "年払いの額が書かれておらず") +
          "、月払いの12か月分",
      );
    if (pl.from) out.push("「〜から」の一番低い額");
    if (pl.usage) out.push("従量課金は別");
    return out.join("・");
  }

  function cheapest(list) {
    return list.reduce(function (a, r) {
      return !a || r.yr < a.yr - 1e-9 ? r : a;
    }, null);
  }

  function isTeam(r) {
    return r.pl.kind !== "personal";
  }

  function calcProduct(prod, n, b) {
    var rows = prod.plans.map(function (pl) {
      var pr = price(pl, b);
      var st = seats(pl, n);
      var row = { pl: pl, pr: pr, st: st };
      if (pr && st.ok) {
        row.mon = pr.mon * st.u;
        row.yr = pr.yr * st.u;
      }
      row.direct = isDirect(row, b);
      return row;
    });
    var ok = rows.filter(function (r) {
      return r.mon != null;
    });
    var curs = ok.map(function (r) {
      return r.pl.cur;
    });
    var cur =
      curs.indexOf("JPY") >= 0
        ? "JPY"
        : curs.indexOf("USD") >= 0
          ? "USD"
          : curs[0];
    var pool = ok.filter(function (r) {
      return r.pl.cur === cur;
    });
    var direct = pool.filter(function (r) {
      return r.direct;
    });
    return {
      rows: rows,
      cur: cur,
      pool: pool,
      direct: direct,
      best: cheapest(direct), // 選んだ払い方の料金がそのまま書かれたプランで一番安いもの（無ければ null）
      bestAny: cheapest(pool), // 目安の額も含めて一番安いもの（表と一覧の「目安」に使う）
      otherCur: cheapest(
        ok.filter(function (r) {
          return r.pl.cur !== cur && isTeam(r);
        }),
      ),
      tNa: rows.filter(function (r) {
        return isTeam(r) && (r.pl.na || !r.st.ok);
      }),
    };
  }

  function amt(r, key) {
    return (
      (r.pr.approx ? "約" : "") +
      money(r[key], r.pl.cur) +
      (r.pl.from ? "〜" : "")
    );
  }

  function names(list) {
    var ns = list.slice(0, 3).map(function (r) {
      return r.pl.name;
    });
    return ns.join("・") + (list.length > 3 ? "など" : "");
  }

  // 製品ごとの要約。「一番安い」「同じ額」は、選んだ払い方の料金がそのまま書かれたプランどうしでだけ言う。
  // 目安の額（月払い×12・年払いの月あたり・「〜から」・従量課金つき・払い方の区別なし）は、出し方を文に書いて別に扱う
  function summary(c, s) {
    var per = s.b === "m" ? "月" : "年";
    var key = s.b === "m" ? "mon" : "yr";
    var bl = s.b === "m" ? "月払い" : "年払い";
    var who = s.n + "人・" + bl;
    if (!c.pool.length)
      return "この人数で計算できるプランがデータにありません。";
    function amounts(r) {
      return s.b === "m"
        ? "月" + amt(r, "mon") + "（1年で" + amt(r, "yr") + "）"
        : "1年で" + amt(r, "yr") + "（月あたり" + amt(r, "mon") + "）";
    }
    var others = c.pool.filter(function (r) {
      return !r.direct;
    });
    if (!c.best) {
      var X = cheapest(others);
      return (
        who +
        "の料金がそのまま書かれたプランは、このデータにありません。表の額は目安で、そのうち一番安いのは" +
        X.pl.name +
        "（" +
        basis(X, s.b) +
        "）の" +
        per +
        amt(X, key) +
        "です。"
      );
    }
    var B = c.best;
    var mentioned = [B];
    var t =
      who +
      "で一番安い有料プランは" +
      B.pl.name +
      "で、" +
      amounts(B) +
      "です。";
    if (B.pl.yrule && s.b === "y")
      t += "年額は公式の「" + B.pl.yrule + "」から出しています。";
    var P = cheapest(
      c.direct.filter(function (r) {
        return !isTeam(r);
      }),
    );
    var T = cheapest(c.direct.filter(isTeam));
    if (P && T) {
      // 一番安い方はもう書いたので、もう一方（個人向け⇔チーム・ビジネス向け）の一番安いプランとの差を書く
      var d = Math.abs(T[key] - P[key]);
      var minNote = T.st.u > s.n ? "（最低" + T.pl.min + "人分）" : "";
      if (d < 0.005)
        t +=
          "個人向けの" +
          P.pl.name +
          "とチーム・ビジネス向けの" +
          T.pl.name +
          minNote +
          "は、" +
          s.n +
          "人だと同じ額です。";
      else if (B === P)
        t +=
          "チーム・ビジネス向けで一番安い" +
          T.pl.name +
          "は" +
          per +
          amt(T, key) +
          minNote +
          "で、" +
          P.pl.name +
          "より" +
          per +
          money(d, c.cur) +
          "高くなります。";
      else
        t +=
          "個人向けで一番安い" +
          P.pl.name +
          "を" +
          s.n +
          "人分契約すると" +
          per +
          amt(P, key) +
          "で、" +
          T.pl.name +
          "より" +
          per +
          money(d, c.cur) +
          "高くなります。";
      mentioned.push(P, T);
    } else {
      // 片方（個人向けかチーム・ビジネス向け）が、そのままの額のプランに無い
      var wantTeam = !!P;
      var label = wantTeam ? "チーム・ビジネス向け" : "個人向け";
      var Y = cheapest(
        others.filter(function (r) {
          return isTeam(r) === wantTeam;
        }),
      );
      if (Y) {
        t +=
          label +
          "の" +
          Y.pl.name +
          "は" +
          basis(Y, s.b) +
          "で" +
          per +
          amt(Y, key) +
          "のため、並べて比べていません。";
        mentioned.push(Y);
      } else if (wantTeam && c.otherCur) {
        t +=
          "チーム・ビジネス向けの" +
          c.otherCur.pl.name +
          "は通貨が違う（" +
          c.otherCur.pl.cur +
          "）ため、並べて比べていません。";
      } else if (wantTeam && c.tNa.length) {
        var x = c.tNa[0];
        t +=
          "チーム・ビジネス向けの" +
          x.pl.name +
          "は" +
          (x.pl.na
            ? "金額の記載がありません。"
            : s.n + "人では使えません（" + x.st.why + "）。");
      } else if (wantTeam) {
        t += "このデータには、チーム・ビジネス向けのプランの料金がありません。";
      }
    }
    var skipped = others.filter(function (r) {
      return mentioned.indexOf(r) < 0;
    });
    if (skipped.length) {
      var why = [];
      skipped.forEach(function (r) {
        var w = r.pl.from
          ? "「〜から」の額"
          : r.pl.usage
            ? "従量課金が別"
            : bl + "の額が書かれていない";
        if (why.indexOf(w) < 0) why.push(w);
      });
      t += names(skipped) + "は比べていません（" + why.join("・") + "）。";
    }
    return t;
  }

  if (typeof module !== "undefined" && module.exports) {
    module.exports = {
      money: money,
      price: price,
      seats: seats,
      calcProduct: calcProduct,
      summary: summary,
    };
    return;
  }

  // ---------- ここから画面 ----------
  var root = document.querySelector("[data-ryoukin]");
  var dataEl = document.getElementById("ryoukin-data");
  if (!root || !dataEl) return;
  var DATA = JSON.parse(dataEl.textContent);
  var byGuide = {};
  DATA.guides.forEach(function (g) {
    byGuide[g.slug] = g;
  });
  var form = root.querySelector("[data-form]");
  var gSel = root.querySelector("[data-guide]");
  var listEl = root.querySelector("[data-products]");
  var nEl = root.querySelector("[data-n]");
  var out = root.querySelector("[data-out]");

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return {
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;",
      }[c];
    });
  }
  function day(s) {
    var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(s || "");
    return m ? +m[2] + "月" + +m[3] + "日" : s || "";
  }
  function shortUrl(u) {
    var s = u.replace(/^https?:\/\/(www\.)?/, "");
    return s.length > 56 ? s.slice(0, 55) + "…" : s;
  }

  function state() {
    var n = parseInt(nEl.value, 10);
    if (!(n >= 1)) n = 1;
    if (n > 1000) n = 1000;
    var b = (form.querySelector('input[name="b"]:checked') || {}).value || "m";
    var ids = Array.prototype.map.call(
      listEl.querySelectorAll("input:checked"),
      function (i) {
        return i.value;
      },
    );
    return { g: gSel.value, p: ids, n: n, b: b };
  }

  function fillProducts(g, want) {
    var ids = g.products.map(function (p) {
      return p.id;
    });
    var sel = (want || []).filter(function (i) {
      return ids.indexOf(i) >= 0;
    });
    if (!sel.length) sel = g.defaults;
    listEl.innerHTML = g.products
      .map(function (p) {
        return (
          '<li><label><input type="checkbox" name="p" value="' +
          esc(p.id) +
          '"' +
          (sel.indexOf(p.id) >= 0 ? " checked" : "") +
          ">" +
          '<span class="rk-pname">' +
          esc(p.name) +
          '</span><span class="rk-pvendor">' +
          esc(p.vendor) +
          "</span></label></li>"
        );
      })
      .join("");
  }

  // プラン名の下に出す「何の料金か」と単価（例: 1人あたり ¥3,850/月・5人分）
  function unitLine(r, s) {
    var pl = r.pl;
    var kind =
      pl.kind === "seat"
        ? "1人あたり"
        : pl.kind === "team"
          ? "1契約でチーム" + (pl.who ? "（" + esc(pl.who) + "）" : "")
          : "1人用";
    if (!r.pr || !r.st.ok) return kind;
    var per =
      r.pr.unit === "y"
        ? money(pl.y, pl.cur) + "/年"
        : r.pr.unit === "ym"
          ? "月" + money(pl.ym, pl.cur) + "（年払い）"
          : r.pr.unit === "p"
            ? money(pl.p, pl.cur) + "/月"
            : money(pl.m, pl.cur) + "/月";
    if (pl.from) per += "〜";
    var cnt = "";
    if (pl.kind === "seat" && (s.n > 1 || r.st.u > s.n))
      cnt = "・" + esc(r.st.label);
    else if (pl.kind === "personal" && s.n > 1) cnt = "・" + s.n + "人分";
    return kind + " " + per + cnt;
  }

  function planRow(r, s, isBest) {
    var pl = r.pl;
    var head =
      '<span class="rk-plan">' +
      esc(pl.name) +
      '</span><span class="rk-kind">' +
      unitLine(r, s) +
      "</span>";
    var notes = [];
    if (r.pr && r.pr.tag) notes.push(r.pr.tag);
    if (r.pr) notes = notes.concat(r.pr.flags);
    if (pl.note) notes.push(pl.note);
    if (notes.length)
      head += '<span class="rk-flag">' + notes.map(esc).join("。") + "</span>";
    head +=
      '<span class="rk-shown">公式の表記：' +
      esc(pl.shown) +
      (pl.checked ? "（" + esc(pl.checked) + " 確認）" : "") +
      "</span>";
    if (pl.na)
      return (
        '<tr class="rk-na"><th scope="row">' +
        head +
        '</th><td colspan="2">金額の記載なし</td></tr>'
      );
    if (!r.st.ok)
      return (
        '<tr class="rk-na"><th scope="row">' +
        head +
        '</th><td colspan="2">' +
        s.n +
        "人では使えない（" +
        esc(r.st.why) +
        "）</td></tr>"
      );
    return (
      "<tr" +
      (isBest ? ' class="is-best"' : "") +
      '><th scope="row">' +
      head +
      "</th><td>" +
      amt(r, "mon") +
      "</td><td>" +
      amt(r, "yr") +
      "</td></tr>"
    );
  }

  function render() {
    var s = state();
    var g = byGuide[s.g];
    var q =
      "?g=" +
      encodeURIComponent(s.g) +
      (s.p.length ? "&p=" + s.p.map(encodeURIComponent).join(",") : "") +
      "&n=" +
      s.n +
      "&b=" +
      s.b;
    try {
      history.replaceState(null, "", location.pathname + q);
    } catch (e) {}
    var prods = g.products.filter(function (p) {
      return s.p.indexOf(p.id) >= 0;
    });
    if (!prods.length) {
      out.innerHTML =
        '<p class="rk-empty">使うAIを1つ以上選ぶと、ここに料金が出ます。</p>';
      return;
    }
    var bl = s.b === "m" ? "月払い" : "年払い";
    var calcs = prods.map(function (p) {
      return { p: p, c: calcProduct(p, s.n, s.b) };
    });
    var h =
      '<h2 class="rk-h">' +
      s.n +
      "人・" +
      bl +
      "の料金（" +
      esc(g.name) +
      "・" +
      prods.length +
      "製品）</h2>";
    var colN = s.n === 1 ? "" : s.n + "人の";
    if (calcs.length > 1) {
      h +=
        '<p class="rk-cap">各製品で、' +
        bl +
        "の料金が書かれたプランのうち一番安いものです（無い製品は目安の額で一番安いもの）。プランの中身は製品によって違います。</p>";
      h +=
        '<div class="table-wrap"><table class="rk-table rk-overview"><thead><tr><th scope="col">AI</th><th scope="col">プラン</th><th scope="col">' +
        colN +
        '月額</th><th scope="col">' +
        colN +
        "年額</th></tr></thead><tbody>";
      calcs.forEach(function (x) {
        var B = x.c.best || x.c.bestAny;
        var free =
          x.p.free && x.p.free.available === true
            ? "無料プランあり"
            : x.p.free && x.p.free.available === false
              ? "無料プランなし"
              : "";
        h +=
          '<tr><th scope="row"><a href="#rk-p-' +
          esc(x.p.id) +
          '">' +
          esc(x.p.name) +
          "</a>" +
          (free ? '<span class="rk-kind">' + free + "</span>" : "") +
          "</th>";
        h += B
          ? "<td>" +
            esc(B.pl.name) +
            (x.c.best
              ? ""
              : '<span class="rk-flag">目安</span>') +
            "</td><td>" +
            amt(B, "mon") +
            "</td><td>" +
            amt(B, "yr") +
            "</td></tr>"
          : '<td colspan="3">この人数で使えるプランがデータにない</td></tr>';
      });
      h += "</tbody></table></div>";
    }
    var foreign = false;
    calcs.forEach(function (x) {
      var p = x.p,
        c = x.c;
      h +=
        '<section class="rk-prod" id="rk-p-' +
        esc(p.id) +
        '"><h3 class="rk-prod-h">' +
        esc(p.name) +
        "<span>" +
        esc(p.vendor) +
        "</span></h3>";
      h += '<p class="rk-sum">' + esc(summary(c, s)) + "</p>";
      h +=
        '<div class="table-wrap"><table class="rk-table"><thead><tr><th scope="col">プラン</th><th scope="col">' +
        colN +
        '月額</th><th scope="col">' +
        colN +
        "年額</th></tr></thead><tbody>";
      c.rows.forEach(function (r) {
        if (r.pl.cur && r.pl.cur !== "JPY") foreign = true;
        h += planRow(r, s, r === c.best);
      });
      h += "</tbody></table></div>";
      if (p.free) {
        var f = p.free;
        h +=
          '<p class="rk-free"><b>無料プラン</b>' +
          (f.available === true
            ? "あり"
            : f.available === false
              ? "なし"
              : "記載なし") +
          (f.detail ? "。" + esc(f.detail) : "") +
          (f.checked ? "（" + esc(f.checked) + " 確認）" : "") +
          "</p>";
      }
      if (p.note)
        h +=
          '<details class="rk-more"><summary>料金についての注記</summary><p>' +
          esc(p.note) +
          "</p></details>";
      h +=
        '<p class="rk-guide">プランごとの中身と、日本語・商用利用・学習利用の条件は<a href="' +
        esc(g.path) +
        (p.featured ? "#d-" + esc(p.id) : "") +
        '">' +
        esc(g.name) +
        "のガイド</a>にあります。</p>";
      h += "</section>";
    });
    h +=
      '<section class="rk-src"><h2 class="rk-h">公式の料金ページと確認日</h2><ul>';
    prods.forEach(function (p) {
      p.sources.forEach(function (x) {
        h +=
          "<li><b>" +
          esc(p.name) +
          '</b><a href="' +
          esc(x.url) +
          '" target="_blank" rel="noopener">' +
          esc(shortUrl(x.url)) +
          "</a><span>" +
          esc(x.checked) +
          " 確認</span></li>";
      });
    });
    h +=
      '</ul><p class="rk-cap">料金は' +
      esc(g.name) +
      "のガイドのデータです（" +
      day(g.reviewed) +
      "に点検）。";
    if (foreign)
      h +=
        "ドル・ユーロ建ての料金は円に換算していません。円で払う額は為替レートとカード会社の手数料で変わります。";
    h += "税込か税抜かは各社の表示のままです。</p></section>";
    out.innerHTML = h;
  }

  // 初期値は URL から（トップの入口・ガイド・モデル図鑑のリンクが製品を選んだ状態で開く）
  var qs = new URLSearchParams(location.search);
  var g0 = byGuide[qs.get("g")]
    ? qs.get("g")
    : byGuide.chat
      ? "chat"
      : DATA.guides[0].slug;
  var want = [];
  qs.getAll("p").forEach(function (v) {
    want = want.concat(v.split(","));
  });
  gSel.value = g0;
  fillProducts(byGuide[g0], want);
  var n0 = parseInt(qs.get("n"), 10);
  if (n0 >= 1 && n0 <= 1000) nEl.value = n0;
  if (qs.get("b") === "y")
    form.querySelector('input[name="b"][value="y"]').checked = true;

  gSel.addEventListener("change", function () {
    fillProducts(byGuide[gSel.value], []);
    render();
  });
  form.addEventListener("change", function (e) {
    if (e.target !== gSel) render();
  });
  nEl.addEventListener("input", render);
  nEl.addEventListener("blur", function () {
    nEl.value = state().n;
  });
  root.querySelectorAll("[data-step]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var n = state().n + parseInt(btn.getAttribute("data-step"), 10);
      nEl.value = Math.max(1, Math.min(1000, n));
      render();
    });
  });
  render();
})();
