/* 記事ページの動き
   1) 記事を読み終えて下にスクロールすると、次の記事（ひとつ前に公開された記事）を続けて読み込む。
      読んでいる記事が変わったら、アドレスバーのURL・タブのタイトル・サイドの目次を切り替える。
      検索エンジンには各記事が1ページずつ見える（JSで足した記事はクローラーには関係しない）。
   2) 共有の「リンクをコピー」と、公式動画の埋め込み（クリックで再生）。あとから足した記事でも効くよう document で受ける */
(function () {
  document.addEventListener("click", function (ev) {
    var t = ev.target;
    var copy = t.closest && t.closest(".share-copy");
    if (copy) {
      navigator.clipboard.writeText(copy.dataset.url).then(function () {
        copy.textContent = "コピーしました";
        setTimeout(function () {
          copy.textContent = "リンクをコピー";
        }, 1600);
      });
      return;
    }
    var yt = t.closest && t.closest(".yt-embed[data-id]");
    if (yt && !yt.querySelector("iframe")) {
      ev.preventDefault();
      var f = document.createElement("iframe");
      f.src =
        "https://www.youtube-nocookie.com/embed/" +
        encodeURIComponent(yt.dataset.id) +
        "?autoplay=1&rel=0";
      f.title = yt.dataset.title || "YouTube";
      f.allow =
        "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
      f.allowFullscreen = true;
      yt.innerHTML = "";
      yt.appendChild(f);
    }
  });

  var col = document.querySelector(".post-col");
  if (
    !col ||
    !("IntersectionObserver" in window) ||
    !window.fetch ||
    !window.DOMParser
  )
    return;
  var first = col.querySelector("article.post");
  var chain = col.querySelector(".chain");
  var status = col.querySelector(".chain-status");
  var sideToc = document.querySelector(".side-toc");
  var MAX = 10; // 続けて読み込む上限（それ以降は一覧へ案内）
  var loaded = 1;
  var loading = false;
  var finished = false;
  var current = first;
  var seen = {};
  seen[first.dataset.url] = true;
  document.documentElement.classList.add("chain-on");

  function setCurrent(el) {
    if (el === current) return;
    current = el;
    if (location.pathname !== el.dataset.url) {
      history.replaceState({ chain: true }, "", el.dataset.url);
      document.title = el.dataset.title;
      if (window.gtag)
        window.gtag("event", "page_view", {
          page_location: location.href,
          page_title: el.dataset.title,
        });
    }
    if (sideToc) {
      var toc = el.querySelector(".toc ol");
      var list = sideToc.querySelector("ol");
      if (toc && list) list.innerHTML = toc.innerHTML;
      sideToc.hidden = !toc;
    }
  }

  // 画面の上から4割あたりを通過した記事を「いま読んでいる記事」にする
  var reading = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) setCurrent(e.target);
      });
    },
    { rootMargin: "-40% 0px -55% 0px" },
  );
  reading.observe(first);

  function loadX(node) {
    if (!node.querySelector(".twitter-tweet")) return;
    if (window.twttr && window.twttr.widgets) {
      window.twttr.widgets.load(node);
      return;
    }
    if (document.getElementById("x-widgets")) return;
    var s = document.createElement("script");
    s.id = "x-widgets";
    s.async = true;
    s.src = "https://platform.twitter.com/widgets.js";
    document.body.appendChild(s);
  }

  function finish(message) {
    finished = true;
    status.textContent = "";
    var a = document.createElement("a");
    a.className = "btn-more";
    a.href = status.dataset.list;
    a.textContent = message;
    status.appendChild(a);
  }

  function loadNext() {
    if (loading || finished) return;
    var arts = col.querySelectorAll("article.post");
    var next = arts[arts.length - 1].dataset.next;
    if (!next || seen[next]) return finish("新着ニュースの一覧を見る");
    if (loaded >= MAX) return finish("ほかの記事を一覧で見る");
    loading = true;
    status.textContent = "次の記事を読み込んでいます…";
    fetch(next, { credentials: "same-origin" })
      .then(function (r) {
        if (!r.ok) throw new Error(r.status);
        return r.text();
      })
      .then(function (text) {
        var doc = new DOMParser().parseFromString(text, "text/html");
        var art = doc.querySelector("article.post");
        if (!art) throw new Error("no article");
        // 続けて読む記事では、前後リンクと関連記事は省く（流れを切らないため）
        art.querySelectorAll(".post-nav, .related").forEach(function (n) {
          n.remove();
        });
        art.classList.add("chained");
        // フッターまで飛んで記事の終わりを通り越しているか（足したあと、足した記事の頭を見せる）
        var passed = status.getBoundingClientRect().top < 0;
        var sep = document.createElement("div");
        sep.className = "chain-sep";
        sep.innerHTML = "<span>次の記事</span>";
        chain.appendChild(sep);
        chain.appendChild(art);
        if (passed)
          window.scrollTo({
            top: sep.getBoundingClientRect().top + window.scrollY - 80,
            behavior: "instant",
          });
        seen[art.dataset.url] = true;
        loaded += 1;
        reading.observe(art);
        loadX(art);
        status.textContent = "";
        loading = false;
        // 読み込んだ記事が短く、まだ画面の下が空いているときは続けて読む
        check();
      })
      .catch(function () {
        loading = false;
        finish("新着ニュースの一覧を見る");
      });
  }

  // 記事の終わりが画面の下から1200pxの手前まで来たら、次を読み込み始める。
  // 一気に下まで飛んで記事の終わりを通り越した（フッターまで来た）ときも読み込む。
  // IntersectionObserver だと通り越したときに反応しないので、スクロールのたびに位置で判定する
  var ticking = false;
  function check() {
    ticking = false;
    if (status.getBoundingClientRect().top < window.innerHeight + 1200) loadNext();
  }
  window.addEventListener(
    "scroll",
    function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(check);
    },
    { passive: true },
  );
  check();
})();
