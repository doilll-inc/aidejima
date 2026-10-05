/* 読むたびに少しうれしくなる仕組み（tomo 2026-10-05「ドーパミンが出るような仕組みにできないかな」）
   1) 記事を最後まで読むと「読了」の通知。今日何本目か・何日連続か・節目（3/7/14/30日連続、累計10/30/50/100本）を出す
   2) 一覧では読んだ記事に「読んだ」の印。まだ読んでいない記事が目立つ
   3) トップに「今日の新着 n/m本」の進み具合と、次に読む1本。全部読んだら次の更新時刻を出す
   4) 画面下の「新着」タブに、今日の未読の数
   5) 記事ページの上端に、読み進み具合のバー
   記録はこの端末のブラウザにだけ残す（サーバーには送らない。GA4には「読了」のイベントだけ送る）。
   消えても困らない便利機能なので、記録できない環境では何も出さない */
(function () {
  var KEY = "aidejima:read"; // { slug: 読了した時刻(ms) }
  var DAYS = "aidejima:days"; // 読了した日（日本時間 YYYY-MM-DD）
  var SLOTS = [7, 12, 17, 21]; // 自動更新の時刻（publish.yml）
  var DWELL = 12000; // 最後までスクロールしただけでは読了にしない（記事が画面に入ってからこの時間は必要）
  var DAY = 864e5;
  var me = document.currentScript;

  function load(k, d) {
    try {
      var v = localStorage.getItem(k);
      return v ? JSON.parse(v) : d;
    } catch (e) {
      return d;
    }
  }
  function save(k, v) {
    try {
      localStorage.setItem(k, JSON.stringify(v));
      return true;
    } catch (e) {
      return false;
    }
  }
  if (!save("aidejima:probe", 1)) return; // 記録できない（プライベートモード等）なら何もしない

  var read = load(KEY, {}) || {};
  var days = load(DAYS, []) || [];
  var recent = null; // [{s, d, t}] 直近48時間の記事（/recent.json）

  function jstDay(ms) {
    return new Date(ms + 9 * 3600e3).toISOString().slice(0, 10);
  }
  function today() {
    return jstDay(Date.now());
  }
  function streak() {
    var set = {};
    days.forEach(function (d) {
      set[d] = 1;
    });
    var t = Date.now();
    var n = 0;
    if (!set[jstDay(t)]) t -= DAY; // 今日まだ読んでいなくても、昨日まで続いていれば途切れていない
    while (set[jstDay(t)]) {
      n++;
      t -= DAY;
    }
    return n;
  }
  function readTodayCount() {
    var d = today();
    var n = 0;
    for (var s in read) if (jstDay(read[s]) === d) n++;
    return n;
  }
  function todaysItems() {
    if (!recent) return null;
    var d = today();
    var items = recent.filter(function (r) {
      return jstDay(Date.parse(r.d)) === d;
    });
    var label = "今日の新着";
    if (!items.length) {
      items = recent.filter(function (r) {
        return Date.now() - Date.parse(r.d) < DAY;
      });
      label = "この24時間の新着";
    }
    return { items: items, label: label };
  }
  function nextUpdate() {
    var h = new Date(Date.now() + 9 * 3600e3).getUTCHours();
    for (var i = 0; i < SLOTS.length; i++)
      if (SLOTS[i] >= h) return SLOTS[i] + "時台";
    return "明日の" + SLOTS[0] + "時台";
  }
  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }
  var base = (
    me && me.dataset.recent ? me.dataset.recent : "/recent.json"
  ).replace(/recent\.json$/, "");
  var ICON_CHECK =
    '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  var ICON_FLAME =
    '<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M12 2.5c.6 3.2 4.8 5.6 4.8 10.3A4.8 4.8 0 0 1 12 17.6a4.8 4.8 0 0 1-4.8-4.8c0-2 .9-3.4 2-4.6.2 1.6 1 2.6 2 3 0-3.2.2-5.9.8-8.7Z" fill="currentColor"/><path d="M12 21.5a3.4 3.4 0 0 1-3.4-3.4c0-1.6 1.2-2.6 2-3.6.2 1 .7 1.6 1.4 1.9.4-1.2.9-1.9 1.6-2.6.9 1.2 1.8 2.5 1.8 4.3a3.4 3.4 0 0 1-3.4 3.4Z" fill="#ffd166"/></svg>';

  // ---------- 一覧の「読んだ」印と、新着タブの未読数 ----------
  function paint() {
    document.querySelectorAll("[data-slug]").forEach(function (el) {
      el.classList.toggle("is-read", !!read[el.dataset.slug]);
    });
    var t = todaysItems();
    var badge = document.querySelector("[data-unread]");
    if (badge && t) {
      var unread = t.items.filter(function (r) {
        return !read[r.s];
      }).length;
      badge.textContent = unread > 9 ? "9+" : unread;
      badge.hidden = !unread;
    }
    daily(t);
  }

  // ---------- トップの「今日の新着 n/m本」 ----------
  function daily(t) {
    var box = document.querySelector("[data-daily]");
    if (!box || !t || !t.items.length) return;
    var total = t.items.length;
    var done = t.items.filter(function (r) {
      return read[r.s];
    }).length;
    var st = streak();
    var next = t.items.filter(function (r) {
      return !read[r.s];
    })[0];
    var sub;
    if (done >= total)
      sub =
        "<b>" +
        t.label +
        "を全部読みました。</b>次の更新は" +
        nextUpdate() +
        "です";
    else if (!done && !st)
      sub = "記事を最後まで読むと、ここに読んだ本数と連続日数がたまります";
    else sub = "あと" + (total - done) + "本で" + t.label + "を読み終わります";
    box.innerHTML =
      '<div class="wrap daily-inner' +
      (done >= total ? " is-done" : "") +
      '">' +
      '<div class="daily-head"><span class="daily-label">' +
      t.label +
      "</span>" +
      '<span class="daily-count"><b>' +
      done +
      "</b>/" +
      total +
      "本 読了</span>" +
      (st >= 2
        ? '<span class="daily-streak">' + ICON_FLAME + st + "日連続</span>"
        : "") +
      "</div>" +
      '<div class="daily-bar" role="progressbar" aria-valuemin="0" aria-valuemax="' +
      total +
      '" aria-valuenow="' +
      done +
      '"><i style="width:' +
      Math.round((done / total) * 100) +
      '%"></i></div>' +
      '<p class="daily-sub">' +
      sub +
      "</p>" +
      (next && next.t
        ? '<a class="daily-next" href="' +
          esc(base + "news/" + next.s + "/") +
          '"><span>次に読む</span>' +
          esc(next.t) +
          "</a>"
        : "") +
      "</div>";
    box.hidden = false;
  }

  // ---------- 読了の通知 ----------
  var toastEl = null;
  var toastTimer = 0;
  function toast(html, big) {
    if (!toastEl) {
      toastEl = document.createElement("div");
      toastEl.className = "reward";
      toastEl.setAttribute("role", "status");
      document.body.appendChild(toastEl);
    }
    toastEl.className = "reward" + (big ? " is-big" : "");
    toastEl.innerHTML = html;
    void toastEl.offsetWidth; // アニメーションをやり直す
    toastEl.classList.add("is-on");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(
      function () {
        toastEl.classList.remove("is-on");
      },
      big ? 4200 : 3000,
    );
  }
  function milestone(st, prevSt, total) {
    var marks = {
      3: "3日連続。習慣になってきました",
      7: "1週間連続で読んでいます",
      14: "2週間連続。AIの流れをつかんでいます",
      30: "30日連続。立派な情報通です",
    };
    if (st !== prevSt && marks[st]) return marks[st];
    var totals = {
      1: "はじめての読了です",
      10: "累計10本読みました",
      30: "累計30本読みました",
      50: "累計50本読みました",
      100: "累計100本。AIデジマの常連です",
    };
    return totals[total] || "";
  }
  function markRead(slug) {
    if (!slug || read[slug]) return;
    var prevSt = streak();
    read[slug] = Date.now();
    var keys = Object.keys(read);
    if (keys.length > 1500) {
      keys.sort(function (a, b) {
        return read[a] - read[b];
      });
      keys.slice(0, keys.length - 1500).forEach(function (k) {
        delete read[k];
      });
    }
    if (days.indexOf(today()) < 0) {
      days.push(today());
      if (days.length > 400) days = days.slice(-400);
    }
    save(KEY, read);
    save(DAYS, days);
    var st = streak();
    var n = readTodayCount();
    var t = todaysItems();
    var allDone =
      t &&
      t.items.length &&
      t.items.every(function (r) {
        return read[r.s];
      }) &&
      t.items.some(function (r) {
        return r.s === slug;
      });
    var note = allDone
      ? t.label + "を全部読みました。次の更新は" + nextUpdate()
      : milestone(st, prevSt, Object.keys(read).length);
    toast(
      '<span class="reward-check">' +
        ICON_CHECK +
        "</span>" +
        '<span class="reward-body"><b>読了</b><span>今日' +
        n +
        "本目</span>" +
        (st >= 2
          ? '<span class="reward-streak">' + ICON_FLAME + st + "日連続</span>"
          : "") +
        (note ? '<em class="reward-note">' + esc(note) + "</em>" : "") +
        "</span>",
      !!note,
    );
    paint();
    if (window.gtag)
      window.gtag("event", "article_read", {
        article_slug: slug,
        streak_days: st,
        read_today: n,
      });
  }

  // ---------- 記事ページ: 読了の判定と、読み進み具合のバー ----------
  var col = document.querySelector(".post-col");
  if (col && "IntersectionObserver" in window) {
    var seenAt = {};
    var bar = document.createElement("div");
    bar.className = "read-progress";
    bar.innerHTML = "<i></i>";
    document.body.appendChild(bar);
    var fill = bar.firstChild;
    function slugOf(el) {
      var m = /\/news\/([^/]+)\/?$/.exec(el.dataset.url || "");
      return m && m[1];
    }
    var enter = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        var s = slugOf(e.target);
        if (e.isIntersecting && s && !seenAt[s]) seenAt[s] = Date.now();
      });
    });
    var end = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var post = e.target.closest("article.post");
        var s = post && slugOf(post);
        if (!s || read[s]) return;
        var wait = DWELL - (Date.now() - (seenAt[s] || Date.now()));
        if (wait <= 0) markRead(s);
        else
          setTimeout(function () {
            var r = e.target.getBoundingClientRect();
            if (r.top < window.innerHeight) markRead(s); // まだ最後のあたりにいれば読了
          }, wait);
      });
    });
    function watch(post) {
      if (post.dataset.watched) return;
      post.dataset.watched = "1";
      enter.observe(post);
      end.observe(
        post.querySelector(".sources") ||
          post.querySelector(".post-body") ||
          post,
      );
    }
    col.querySelectorAll("article.post").forEach(watch);
    // 続けて読み込まれた記事（chain.js）も同じように見る
    // X の埋め込みなどで細かい変化が続くので、落ち着いてからまとめて見る
    var mutTimer = 0;
    new MutationObserver(function () {
      clearTimeout(mutTimer);
      mutTimer = setTimeout(function () {
        col.querySelectorAll("article.post").forEach(watch);
        paint();
      }, 250);
    }).observe(col, { childList: true, subtree: true });

    var ticking = false;
    function progress() {
      ticking = false;
      var vh = window.innerHeight;
      var posts = col.querySelectorAll("article.post");
      var cur = null;
      for (var i = 0; i < posts.length; i++)
        if (posts[i].getBoundingClientRect().top <= vh * 0.4) cur = posts[i];
      if (!cur) cur = posts[0];
      var r = cur.getBoundingClientRect();
      var p = Math.min(
        1,
        Math.max(0, (vh * 0.6 - r.top) / Math.max(1, r.height)),
      );
      fill.style.transform = "scaleX(" + p.toFixed(3) + ")";
      bar.classList.toggle("is-read", !!read[slugOf(cur)]);
    }
    window.addEventListener(
      "scroll",
      function () {
        if (!ticking) {
          ticking = true;
          requestAnimationFrame(progress);
        }
      },
      { passive: true },
    );
    progress();
  }

  paint();
  if (window.fetch && me && me.dataset.recent)
    fetch(me.dataset.recent, { cache: "no-cache" })
      .then(function (r) {
        return r.ok ? r.json() : null;
      })
      .then(function (j) {
        if (Array.isArray(j)) {
          recent = j;
          paint();
        }
      })
      .catch(function () {});
})();
