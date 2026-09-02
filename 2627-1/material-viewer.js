(function () {
  "use strict";

  const ALLOWED_LECTURES = new Set(["01", "02", "03", "04", "05", "06", "07", "08", "10", "11", "12", "13", "14"]);
  const DOCUMENT_PATTERN = /^materials\/lec-(\d{2})\/lecture-note\.md$/;
  const DECK_PATTERN = /^lecture-(\d{2})-[a-z0-9]+(?:-[a-z0-9]+)*\.html$/;
  const DIRECTIVE_PATTERN = /^(example|derivation|proof|exercise|hint|solution)$/;
  const DIRECTIVE_LABELS = {
    example: "Ví dụ",
    derivation: "Suy diễn",
    proof: "Chứng minh",
    exercise: "Bài tập",
    hint: "Gợi ý",
    solution: "Lời giải"
  };

  const statusElement = document.getElementById("material-status");
  const layoutElement = document.getElementById("material-layout");
  const contentElement = document.getElementById("material-content");
  const titleElement = document.getElementById("material-title");
  const kindElement = document.getElementById("material-kind");
  const deckLink = document.getElementById("deck-link");
  const sourceLink = document.getElementById("source-link");
  const tocList = document.getElementById("toc-list");

  function escapeHtml(value) {
    return String(value)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  function fail(message, detail) {
    statusElement.className = "material-status material-status--error";
    statusElement.innerHTML = `<strong>Không thể mở tài liệu.</strong><span>${escapeHtml(message)}</span>`;
    if (detail) console.error(detail);
    layoutElement.hidden = true;
    document.title = "Không thể mở tài liệu · Học sâu";
  }

  function readRequest() {
    const parameters = new URLSearchParams(window.location.search);
    const documentPath = parameters.get("doc") || "";
    const deckPath = parameters.get("deck") || "";
    const documentMatch = DOCUMENT_PATTERN.exec(documentPath);
    const deckMatch = DECK_PATTERN.exec(deckPath);

    if (!documentMatch || !deckMatch) {
      throw new Error("Đường dẫn ghi chú hoặc bộ trang chiếu không đúng quy ước.");
    }
    if (!ALLOWED_LECTURES.has(documentMatch[1]) || !ALLOWED_LECTURES.has(deckMatch[1])) {
      throw new Error("Số bài không thuộc các buổi được phép công bố.");
    }
    if (documentMatch[1] !== deckMatch[1]) {
      throw new Error("Số bài của ghi chú không khớp với bộ trang chiếu.");
    }

    return { documentPath, deckPath, lecture: documentMatch[1] };
  }

  function validateDirectives(markdown) {
    let openDirective = null;
    let fence = null;
    markdown.split(/\r?\n/).forEach((line, index) => {
      const trimmed = line.trim();
      const fenceMatch = /^ {0,3}(```|~~~)/.exec(line);
      if (fenceMatch) {
        if (!fence) fence = fenceMatch[1];
        else if (fence === fenceMatch[1]) fence = null;
        return;
      }
      if (fence || /^(?: {4}|\t)/.test(line)) return;

      const opening = /^:::[ \t]*(\S+)(?:\s+.*)?$/.exec(trimmed);
      if (trimmed === ":::") {
        if (!openDirective) throw new Error(`Dấu đóng khối ::: không có dấu mở ở dòng ${index + 1}.`);
        openDirective = null;
        return;
      }
      if (!opening) return;
      if (!DIRECTIVE_PATTERN.test(opening[1])) {
        throw new Error(`Loại khối “${opening[1]}” không được hỗ trợ ở dòng ${index + 1}.`);
      }
      if (openDirective) {
        throw new Error(`Không được lồng khối :::; khối “${openDirective}” chưa đóng ở dòng ${index + 1}.`);
      }
      openDirective = opening[1];
    });
    if (openDirective) throw new Error(`Khối “${openDirective}” chưa có dấu đóng :::.`);
  }

  function protectMath(markdown) {
    const expressions = [];
    const randomValues = new Uint32Array(2);
    window.crypto.getRandomValues(randomValues);
    const tokenPrefix = `MATH${Array.from(randomValues, (value) => value.toString(36)).join("")}PLACEHOLDER`;
    const pattern = /```[\s\S]*?```|~~~[\s\S]*?~~~|`[^`\n]*`|\$\$[\s\S]*?\$\$|\$(?!\s)(?:\\.|[^$\n])+?\$/g;
    const source = markdown.replace(pattern, (match) => {
      if (match.startsWith("`") || !match.startsWith("$")) return match;
      const token = `${tokenPrefix}${expressions.length}TOKEN`;
      expressions.push(match);
      return token;
    });
    return { source, expressions, tokenPrefix };
  }

  function restoreMath(root, expressions, tokenPrefix) {
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    const nodes = [];
    const tokenPattern = new RegExp(`${tokenPrefix}(\\d+)TOKEN`, "g");
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach((node) => {
      node.data = node.data.replace(tokenPattern, (match, index) => expressions[Number(index)] ?? match);
    });
  }

  function configureMarked() {
    if (!window.marked || typeof window.marked.parse !== "function") {
      throw new Error("Không tải được thư viện Marked cục bộ.");
    }
    const directive = {
      name: "materialDirective",
      level: "block",
      start(source) {
        const index = source.match(/^:::[ \t]*(?:example|derivation|proof|exercise|hint|solution)(?:\s|$)/m)?.index;
        return typeof index === "number" ? index : undefined;
      },
      tokenizer(source) {
        const match = /^:::[ \t]*(example|derivation|proof|exercise|hint|solution)(?:[ \t]+([^\n]+))?[ \t]*\n([\s\S]*?)\n:::[ \t]*(?:\n|$)/.exec(source);
        if (!match) return undefined;
        return {
          type: "materialDirective",
          raw: match[0],
          kind: match[1],
          title: match[2]?.trim() || "",
          tokens: this.lexer.blockTokens(match[3].trim(), [])
        };
      },
      renderer(token) {
        const title = escapeHtml(token.title || DIRECTIVE_LABELS[token.kind]);
        const body = this.parser.parse(token.tokens);
        if (token.kind === "hint" || token.kind === "solution") {
          return `<details class="material-block material-block--${token.kind}"><summary>${title}</summary><div class="material-block__body">${body}</div></details>`;
        }
        return `<section class="material-block material-block--${token.kind}"><h3>${title}</h3><div class="material-block__body">${body}</div></section>`;
      }
    };
    window.marked.use({
      gfm: true,
      breaks: false,
      renderer: { html(token) { return escapeHtml(token.text); } },
      extensions: [directive]
    });
  }

  function sanitize(html) {
    if (!window.DOMPurify || typeof window.DOMPurify.sanitize !== "function") {
      throw new Error("Không tải được thư viện DOMPurify cục bộ.");
    }
    return window.DOMPurify.sanitize(html, {
      USE_PROFILES: { html: true },
      ALLOW_DATA_ATTR: false,
      FORBID_TAGS: ["script", "style", "iframe", "object", "embed", "form", "input", "button", "textarea", "select", "option", "template", "svg", "math"],
      FORBID_ATTR: ["style", "srcset"]
    });
  }

  function validateImages(lecture) {
    const imagePattern = new RegExp(`^img/lec-${lecture}/[A-Za-z0-9][A-Za-z0-9._-]*\\.svg$`);
    contentElement.querySelectorAll("img").forEach((image) => {
      const source = image.getAttribute("src") || "";
      if (!imagePattern.test(source)) {
        throw new Error(`Hình “${source || "không có đường dẫn"}” không thuộc thư mục SVG của Bài ${lecture}.`);
      }
      if (!image.getAttribute("alt")?.trim()) {
        throw new Error(`Hình “${source}” phải có mô tả thay thế.`);
      }
      image.setAttribute("loading", "lazy");
      image.setAttribute("decoding", "async");
    });
  }

  function slugify(value) {
    return value.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/đ/g, "d").replace(/Đ/g, "D")
      .toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "") || "muc";
  }

  function headingLabel(heading) {
    const clone = heading.cloneNode(true);
    clone.querySelectorAll(".katex-mathml").forEach((node) => node.remove());
    return clone.textContent.trim();
  }

  function buildTableOfContents() {
    const headings = Array.from(contentElement.querySelectorAll("h2, h3"))
      .filter((heading) => !heading.closest(".material-block"));
    const usedIds = new Map();
    const list = document.createElement("ol");
    headings.forEach((heading) => {
      const label = headingLabel(heading) || "Mục";
      const baseId = slugify(label);
      const count = usedIds.get(baseId) || 0;
      usedIds.set(baseId, count + 1);
      heading.id = count === 0 ? baseId : `${baseId}-${count + 1}`;
      const item = document.createElement("li");
      if (heading.tagName === "H3") item.className = "toc-level-3";
      const link = document.createElement("a");
      link.href = `#${heading.id}`;
      link.textContent = label;
      item.appendChild(link);
      list.appendChild(item);
    });
    tocList.replaceChildren(list);
    if (headings.length === 0) tocList.innerHTML = '<p class="muted-text">Tài liệu chưa có mục cấp hai.</p>';
  }

  function hardenLinks() {
    let removedLinks = 0;
    const allowedProtocols = new Set(["http:", "https:", "mailto:"]);
    contentElement.querySelectorAll("a[href]").forEach((link) => {
      try {
        const target = new URL(link.getAttribute("href"), window.location.href);
        if (!allowedProtocols.has(target.protocol)) {
          link.removeAttribute("href");
          removedLinks += 1;
        } else if (target.origin !== window.location.origin) {
          link.rel = "noopener noreferrer";
        }
      } catch (error) {
        link.removeAttribute("href");
        removedLinks += 1;
      }
    });
    return removedLinks;
  }

  function renderMath() {
    if (typeof window.renderMathInElement !== "function") {
      throw new Error("Không tải được phần mở rộng auto-render của KaTeX.");
    }
    const mathErrors = [];
    window.renderMathInElement(contentElement, {
      delimiters: [{ left: "$$", right: "$$", display: true }, { left: "$", right: "$", display: false }],
      ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code", "option"],
      throwOnError: false,
      errorCallback(message) { mathErrors.push(message); console.error(message); }
    });
    return mathErrors.length;
  }

  function preparePrinting() {
    let previouslyOpen = [];
    window.addEventListener("beforeprint", () => {
      previouslyOpen = Array.from(contentElement.querySelectorAll("details:not([open])"));
      previouslyOpen.forEach((details) => details.setAttribute("open", ""));
    });
    window.addEventListener("afterprint", () => {
      previouslyOpen.forEach((details) => details.removeAttribute("open"));
      previouslyOpen = [];
    });
  }

  async function loadMaterial() {
    let request;
    try {
      request = readRequest();
      configureMarked();
    } catch (error) {
      fail(error.message, error);
      return;
    }

    deckLink.href = request.deckPath;
    sourceLink.href = request.documentPath;
    kindElement.textContent = `Ghi chú bài giảng · Bài ${request.lecture}`;

    try {
      const response = await fetch(request.documentPath, { credentials: "same-origin", cache: "no-cache" });
      if (!response.ok) throw new Error(`Máy chủ trả mã ${response.status} khi tải Markdown.`);
      const markdown = await response.text();
      validateDirectives(markdown);
      const protectedMath = protectMath(markdown);
      contentElement.innerHTML = sanitize(window.marked.parse(protectedMath.source));
      restoreMath(contentElement, protectedMath.expressions, protectedMath.tokenPrefix);
      validateImages(request.lecture);

      const firstHeading = contentElement.querySelector("h1");
      if (!firstHeading || !firstHeading.textContent.trim()) {
        throw new Error("Tài liệu phải bắt đầu bằng một heading cấp một có tiêu đề.");
      }
      const title = firstHeading.textContent.trim();
      titleElement.textContent = title;
      document.title = `${title} · Học sâu`;
      firstHeading.remove();

      const warnings = [];
      const removedLinks = hardenLinks();
      if (removedLinks > 0) warnings.push(`${removedLinks} liên kết không an toàn hoặc không hợp lệ đã bị vô hiệu hóa.`);
      try {
        const mathErrors = renderMath();
        if (mathErrors > 0) warnings.push(`${mathErrors} công thức cần kiểm tra.`);
      } catch (mathError) {
        warnings.push("Không tải được KaTeX; nội dung văn bản vẫn được giữ nguyên.");
        console.error(mathError);
      }
      buildTableOfContents();
      preparePrinting();

      if (warnings.length === 0) statusElement.hidden = true;
      else {
        statusElement.className = "material-status material-status--warning";
        statusElement.textContent = `Tài liệu đã mở với cảnh báo: ${warnings.join(" ")}`;
        statusElement.hidden = false;
      }
      layoutElement.hidden = false;
    } catch (error) {
      fail(error.message, error);
    }
  }

  loadMaterial();
})();
