/* AIの料金計算（/tools/ryoukin/）
   データはページに埋め込んだ JSON（build.py → ryoukin.py が data/guides/*.json から作る）。
   計算はこのブラウザの中だけで行い、入力はどこにも送らない。条件は URL（?g=&p=&n=&b=）に残すので、そのまま共有できる。
   数字はデータにあるものだけを使う。年払いの年額がなく「月あたり」だけのものは12か月分を「約」で出し、
   どの出し方をしたかを各行に書く */
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
  // mon=月あたり / yr=1年分 / approx=目安（約）/ tag=払い方の制約 / flags=出し方の説明
  function price(pl, b) {
    if (pl.na) return null;
    var r = { approx: false, flags: [], tag: "" };
    var m = pl.m,
      y = pl.y,
      ym = pl.ym;
    function yearOfM() {
      return pl.then != null && pl.pm
        ? m * pl.pm + pl.then * (12 - pl.pm)
        : m * 12;
    }
    if (pl.p != null) {
      r.mon = pl.p;
      r.yr = pl.p * 12;
      r.unit = "m";
      r.approx = true;
      r.flags.push(
        "公式の表記からは月払いか年払いかが分からないため、表示の月額の12か月分",
      );
    } else if (b === "m") {
      if (m != null) {
        r.mon = m;
        r.yr = yearOfM();
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
        r.yr = yearOfM();
        r.mon = r.yr / 12;
        r.unit = "m";
        if (pl.only === "m") r.tag = "月払いのみ";
        else r.flags.push("年払いの料金がデータにないため、月払いの12か月分");
      }
    }
    if (pl.then != null && r.unit === "m" && pl.p == null) {
      r.flags.push(
        "最初の" +
          pl.pm +
          "か月は月" +
          money(m, pl.cur) +
          "、その後は月" +
          money(pl.then, pl.cur) +
          "（1年分はその合計）",
      );
    }
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

  function cheapest(list) {
    return list.reduce(function (a, r) {
      return !a || r.yr < a.yr - 1e-9 ? r : a;
    }, null);
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
    var isTeam = function (r) {
      return r.pl.kind !== "personal";
    };
    var tBest = cheapest(pool.filter(isTeam));
    return {
      rows: rows,
      cur: cur,
      best: cheapest(pool),
      pBest: cheapest(
        pool.filter(function (r) {
          return !isTeam(r);
        }),
      ),
      tBest: tBest,
      tOther: tBest ? null : cheapest(ok.filter(isTeam)),
      tNa: rows.filter(function (r) {
        return isTeam(r) && (r.pl.na || !r.st.ok);
      }),
    };
  }

  if (typeof module !== "undefined" && module.exports) {
    module.exports = {
      money: money,
      price: price,
      seats: seats,
      calcProduct: calcProduct,
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
  function amt(r, key) {
    return (
      (r.pr.approx ? "約" : "") +
      money(r[key], r.pl.cur) +
      (r.pl.from ? "〜" : "")
    );
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
    var kind = pl.kind === "seat" ? "1人あたり" : pl.kind === "team" ? "1契約でチーム" + (pl.who ? "（" + esc(pl.who) + "）" : "") : "1人用";
    if (!r.pr || !r.st.ok) return kind;
    var per =
      r.pr.unit === "y" ? money(pl.y, pl.cur) + "/年"
      : r.pr.unit === "ym" ? "月" + money(pl.ym, pl.cur) + "（年払い）"
      : pl.p != null ? money(pl.p, pl.cur) + "/月"
      : money(pl.m, pl.cur) + "/月";
    if (pl.from) per += "〜";
    var cnt = "";
    if (pl.kind === "seat" && (s.n > 1 || r.st.u > s.n)) cnt = "・" + esc(r.st.label);
    else if (pl.kind === "personal" && s.n > 1) cnt = "・" + s.n + "人分";
    return kind + " " + per + cnt;
  }

  function planRow(r, s, isBest) {
    var pl = r.pl;
    var head = '<span class="rk-plan">' + esc(pl.name) + '</span><span class="rk-kind">' + unitLine(r, s) + "</span>";
    var notes = [];
    if (r.pr && r.pr.tag) notes.push(r.pr.tag);
    if (r.pr) notes = notes.concat(r.pr.flags);
    if (pl.note) notes.push(pl.note);
    if (notes.length) head += '<span class="rk-flag">' + notes.map(esc).join("。") + "</span>";
    head += '<span class="rk-shown">公式の表記：' + esc(pl.shown) + (pl.checked ? "（" + esc(pl.checked) + " 確認）" : "") + "</span>";
    if (pl.na) return '<tr class="rk-na"><th scope="row">' + head + '</th><td colspan="2">金額の記載なし</td></tr>';
    if (!r.st.ok) return '<tr class="rk-na"><th scope="row">' + head + '</th><td colspan="2">' + s.n + "人では使えない（" + esc(r.st.why) + "）</td></tr>";
    return "<tr" + (isBest ? ' class="is-best"' : "") + '><th scope="row">' + head + "</th><td>" + amt(r, "mon") + "</td><td>" + amt(r, "yr") + "</td></tr>";
  }

  function summary(c, s) {
    if (!c.best) return "この人数で計算できるプランがデータにありません。";
    var B = c.best;
    var who = s.n + "人・" + (s.b === "m" ? "月払い" : "年払い");
    var t =
      s.b === "m"
        ? who +
          "で一番安い有料プランは" +
          B.pl.name +
          "で、月" +
          amt(B, "mon") +
          "（1年で" +
          amt(B, "yr") +
          "）です。"
        : who +
          "で一番安い有料プランは" +
          B.pl.name +
          "で、1年で" +
          amt(B, "yr") +
          "（月あたり" +
          amt(B, "mon") +
          "）です。";
    var key = s.b === "m" ? "mon" : "yr";
    var per = s.b === "m" ? "月" : "年";
    var P = c.pBest,
      T = c.tBest;
    if (P && T) {
      // 一番安い方はもう書いたので、もう一方（個人向け⇔チーム・ビジネス向け）の一番安いプランとの差を書く
      var d = Math.abs(T[key] - P[key]);
      var ap = P.pr.approx || T.pr.approx ? "約" : "";
      var minNote = T.st.u > s.n ? "（最低" + T.pl.min + "人分）" : "";
      if (d < 0.005) {
        t += "個人向けの" + P.pl.name + "とチーム・ビジネス向けの" + T.pl.name + minNote + "は、" + s.n + "人だと同じ額です。";
      } else if (B === P) {
        t += "チーム・ビジネス向けで一番安い" + T.pl.name + "は" + per + amt(T, key) + minNote + "で、" + P.pl.name + "より" + per + ap + money(d, c.cur) + "高くなります。";
      } else {
        t += "個人向けで一番安い" + P.pl.name + "を" + s.n + "人分契約すると" + per + amt(P, key) + "で、" + T.pl.name + "より" + per + ap + money(d, c.cur) + "高くなります。";
      }
    } else if (P && c.tOther) {
      t +=
        "チーム・ビジネス向けの" +
        c.tOther.pl.name +
        "は通貨が違う（" +
        c.tOther.pl.cur +
        "）ため、並べて比べていません。";
    } else if (P && c.tNa.length) {
      var x = c.tNa[0];
      t +=
        "チーム・ビジネス向けの" +
        x.pl.name +
        "は" +
        (x.pl.na
          ? "金額の記載がありません。"
          : s.n + "人では使えません（" + x.st.why + "）。");
    } else if (P) {
      t += "このデータには、チーム・ビジネス向けのプランの料金がありません。";
    }
    return t;
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
        '<p class="rk-cap">各製品で一番安い有料プランです。プランの中身は製品によって違います。</p>';
      h +=
        '<div class="table-wrap"><table class="rk-table rk-overview"><thead><tr><th scope="col">AI</th><th scope="col">プラン</th><th scope="col">' +
        colN +
        '月額</th><th scope="col">' +
        colN +
        "年額</th></tr></thead><tbody>";
      calcs.forEach(function (x) {
        var B = x.c.best;
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
