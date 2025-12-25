/* CPS Device Comparator - vanilla JS */
(() => {
  const state = {
    view: "explore",
    devices: [],
    filtered: [],
    pickA: "",
    pickB: ""
  };

  const $ = (sel, root = document) => root.querySelector(sel);

  function normalize(s) {
    return (s ?? "")
      .toString()
      .trim()
      .toLowerCase()
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "");
  }

  function displayLabel(d) {
    // Compact label for selects
    return `${d.model}`;
  }

  function setView(view) {
    state.view = view;
    document.querySelectorAll(".tab").forEach(b => b.classList.toggle("is-active", b.dataset.view === view));
    document.querySelectorAll(".view").forEach(v => v.classList.toggle("is-active", v.id === `view-${view}`));
    if (view === "compare") renderCompare();
  }

  function sortDevices(list, sortKey) {
    const dir = sortKey.endsWith("desc") ? -1 : 1;
    const key = sortKey.split("-")[0];

    const getKey = (d) => {
      if (key === "category") return normalize(d.category);
      if (key === "frequency") return normalize(d.frequency);
      return normalize(d.model);
    };

    list.sort((a, b) => {
      const ak = getKey(a);
      const bk = getKey(b);
      if (ak < bk) return -1 * dir;
      if (ak > bk) return 1 * dir;
      return 0;
    });
  }

  function applyFilters() {
    const q = normalize($("#q").value);
    const cat = $("#category").value;
    const sortKey = $("#sort").value;

    let list = [...state.devices];

    if (cat) list = list.filter(d => d.category === cat);

    if (q) {
      list = list.filter(d => {
        const hay = normalize([
          d.model, d.category, d.frequency, d.ram, d.storage, d.protocols, d.io
        ].join(" | "));
        return hay.includes(q);
      });
    }

    sortDevices(list, sortKey);
    state.filtered = list;

    renderTable();
  }

  function renderTable() {
    const tbody = $("#tableBody");
    const empty = $("#empty");
    const n = state.filtered.length;

    $("#count").textContent = `${n} dispositivo${n === 1 ? "" : "s"} mostrados`;

    tbody.innerHTML = "";

    if (!n) {
      empty.hidden = false;
      return;
    }
    empty.hidden = true;

    const frag = document.createDocumentFragment();

    for (const d of state.filtered) {
      const tr = document.createElement("tr");

      const protocolsShort = shorten(d.protocols, 130) || "—";
      const ioShort = shorten(d.io, 130) || "—";

      tr.innerHTML = `
        <td>
          <div class="model-cell">
            <img src="${escapeHtml(d.image)}" alt="${escapeHtml(d.model)}" loading="lazy">
            <div>
              <div class="model-title">${escapeHtml(d.model)}</div>
              <div class="model-sub">${escapeHtml(d.id)}</div>
            </div>
          </div>
        </td>
        <td><span class="badge">${escapeHtml(d.category || "—")}</span></td>
        <td>${escapeHtml(d.frequency || "—")}</td>
        <td>${escapeHtml(d.ram || "—")}</td>
        <td>${escapeHtml(d.storage || "—")}</td>
        <td title="${escapeHtml(d.protocols || "")}">${escapeHtml(protocolsShort)}</td>
        <td title="${escapeHtml(d.io || "")}">${escapeHtml(ioShort)}</td>
        <td class="col-pdf"><a class="btn secondary small" href="${escapeHtml(d.datasheet)}" target="_blank" rel="noopener">PDF</a></td>
      `;
      frag.appendChild(tr);
    }

    tbody.appendChild(frag);
  }

  // (Optional) Card renderer kept for future use, but without compare buttons.
  function deviceCard(d) {
    const a = document.createElement("article");
    a.className = "card";
    a.innerHTML = `
      <div class="thumb"><img src="${escapeHtml(d.image)}" alt="${escapeHtml(d.model)}" loading="lazy"></div>
      <div class="card-body">
        <div class="card-title">
          <h3>${escapeHtml(d.model)}</h3>
          <span class="badge">${escapeHtml(d.category)}</span>
        </div>

        <div class="kv">
          <div class="k">Frecuencia</div><div class="v">${escapeHtml(d.frequency || "—")}</div>
          <div class="k">RAM</div><div class="v">${escapeHtml(d.ram || "—")}</div>
          <div class="k">Almacen.</div><div class="v">${escapeHtml(d.storage || "—")}</div>
          <div class="k">I/O</div><div class="v">${escapeHtml(shorten(d.io, 110) || "—")}</div>
          <div class="k">Protocolos</div><div class="v">${escapeHtml(shorten(d.protocols, 110) || "—")}</div>
        </div>

        <div class="card-actions">
          <a class="btn secondary" href="${escapeHtml(d.datasheet)}" target="_blank" rel="noopener">Ficha PDF</a>
        </div>
      </div>
    `;
    return a;
  }

  function syncComparePickers() {
    const pickA = $("#pickA");
    const pickB = $("#pickB");
    if (!pickA || !pickB) return;

    if (pickA.value !== (state.pickA ?? "")) pickA.value = state.pickA ?? "";
    if (pickB.value !== (state.pickB ?? "")) pickB.value = state.pickB ?? "";
  }

  function renderCompare() {
    const pickA = $("#pickA");
    const pickB = $("#pickB");
    const wrap = $("#compareWrap");
    const diffToggle = $("#diffOnly");
    const swapBtn = $("#swap");

    if (!state.devices.length) return;

    wrap.innerHTML = "";

    // Empty until the user picks both from THIS section.
    const hasA = !!state.pickA;
    const hasB = !!state.pickB;

    diffToggle.disabled = !(hasA && hasB);
    swapBtn.disabled = !(hasA && hasB);

    if (!(hasA && hasB)) {
      const box = document.createElement("div");
      box.className = "empty";
      box.innerHTML = `Selecciona <strong>Dispositivo A</strong> y <strong>Dispositivo B</strong> para ver la comparación.`;
      wrap.appendChild(box);
      return;
    }

    syncComparePickers();

    const a = state.devices.find(d => d.id === state.pickA);
    const b = state.devices.find(d => d.id === state.pickB);

    if (!a || !b) {
      const box = document.createElement("div");
      box.className = "empty";
      box.textContent = "No se encontró uno de los dispositivos seleccionados.";
      wrap.appendChild(box);
      return;
    }

    const diffOnly = diffToggle.checked;

    const fields = [
      ["Categoría", "category"],
      ["Frecuencia", "frequency"],
      ["RAM", "ram"],
      ["Almacenamiento", "storage"],
      ["Protocolos", "protocols"],
      ["I/O", "io"],
    ];

    const rows = [];
    for (const [label, key] of fields) {
      const av = (a[key] ?? "").toString().trim() || "—";
      const bv = (b[key] ?? "").toString().trim() || "—";
      const isDiff = normalize(av) !== normalize(bv);
      if (diffOnly && !isDiff) continue;
      rows.push({ label, av, bv, isDiff });
    }

    const header = document.createElement("div");
    header.className = "compare-header";
    header.innerHTML = `
      <div class="h0">Campo</div>
      <div><a href="${escapeHtml(a.datasheet)}" target="_blank" rel="noopener">${escapeHtml(displayLabel(a))}</a></div>
      <div><a href="${escapeHtml(b.datasheet)}" target="_blank" rel="noopener">${escapeHtml(displayLabel(b))}</a></div>
    `;
    wrap.appendChild(header);

    for (const r of rows) {
      const row = document.createElement("div");
      row.className = "compare-row";
      row.innerHTML = `
        <div class="rk">${escapeHtml(r.label)}</div>
        <div class="${r.isDiff ? "diff" : ""}">${escapeHtml(r.av)}</div>
        <div class="${r.isDiff ? "diff" : ""}">${escapeHtml(r.bv)}</div>
      `;
      wrap.appendChild(row);
    }

    if (!rows.length) {
      const row = document.createElement("div");
      row.className = "compare-row";
      row.innerHTML = `
        <div class="rk">Resultado</div>
        <div>Sin diferencias en los campos seleccionados.</div>
        <div>Sin diferencias en los campos seleccionados.</div>
      `;
      wrap.appendChild(row);
    }
  }

  function escapeHtml(s) {
    return (s ?? "").toString()
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  function shorten(s, n) {
    if (!s) return s;
    const t = s.toString().trim();
    return t.length > n ? (t.slice(0, n - 1) + "…") : t;
  }

  async function init() {
    // Tabs
    document.querySelectorAll(".tab[data-view]").forEach(btn => {
      btn.addEventListener("click", () => setView(btn.dataset.view));
    });

    // Explore controls
    $("#q").addEventListener("input", debounce(applyFilters, 120));
    $("#category").addEventListener("change", applyFilters);
    $("#sort").addEventListener("change", applyFilters);
    $("#clear").addEventListener("click", () => {
      $("#q").value = "";
      $("#category").value = "";
      $("#sort").value = "model-asc";
      applyFilters();
      $("#q").focus();
    });

    // Compare controls
    $("#pickA").addEventListener("change", (e) => { state.pickA = e.target.value; renderCompare(); });
    $("#pickB").addEventListener("change", (e) => { state.pickB = e.target.value; renderCompare(); });
    $("#swap").addEventListener("click", () => {
      const tmp = state.pickA;
      state.pickA = state.pickB;
      state.pickB = tmp;
      syncComparePickers();
      renderCompare();
    });
    $("#diffOnly").addEventListener("change", renderCompare);

    // Load data
    const resp = await fetch("data/devices.json", { cache: "no-store" });
    const data = await resp.json();

    state.devices = data.devices.map(d => ({
      id: d.id,
      model: d.model,
      category: d.category,
      frequency: d.frequency,
      ram: d.ram,
      storage: d.storage,
      protocols: d.protocols,
      io: d.io,
      image: d.image || "assets/img/placeholder.svg",
      datasheet: d.datasheet || "datasheets/placeholder.pdf",
    }));

    // Categories
    const cats = Array.from(new Set(state.devices.map(d => d.category))).sort((a, b) => normalize(a).localeCompare(normalize(b)));
    const catSel = $("#category");
    cats.forEach(c => {
      const opt = document.createElement("option");
      opt.value = c;
      opt.textContent = c;
      catSel.appendChild(opt);
    });

    // Compare pickers (blank until chosen here)
    const pickA = $("#pickA");
    const pickB = $("#pickB");

    const blankA = document.createElement("option");
    blankA.value = "";
    blankA.textContent = "— Selecciona —";
    blankA.selected = true;

    const blankB = blankA.cloneNode(true);

    pickA.appendChild(blankA);
    pickB.appendChild(blankB);

    const optsFragA = document.createDocumentFragment();
    const optsFragB = document.createDocumentFragment();
    state.devices.forEach(d => {
      const o1 = document.createElement("option");
      o1.value = d.id;
      o1.textContent = displayLabel(d);
      const o2 = o1.cloneNode(true);
      optsFragA.appendChild(o1);
      optsFragB.appendChild(o2);
    });
    pickA.appendChild(optsFragA);
    pickB.appendChild(optsFragB);

    applyFilters();
  }

  function debounce(fn, wait) {
    let t = null;
    return (...args) => {
      clearTimeout(t);
      t = setTimeout(() => fn(...args), wait);
    };
  }

  window.addEventListener("DOMContentLoaded", init);
})();
