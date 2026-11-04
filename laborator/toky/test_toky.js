// Logická kontrola stránky bez prohlížeče. Spuštění: node test_toky.js
const fs = require("fs");
const path = require("path");
const vm = require("vm");

const HERE = __dirname;
const WEB = path.resolve(HERE, "..", "..");
let failures = 0;
function check(ok, text){
  console.log((ok ? "OK    " : "CHYBA ") + text);
  if(!ok) failures++;
}

/* ---------- 1. Malá náhrada DOM a běh stránky ---------- */
function scriptOf(html){
  return html.slice(html.indexOf('"use strict";'), html.lastIndexOf("</script>"));
}
function makeEl(tag){
  const cls = new Set();
  const e = {
    tag, style:{setProperty(){}}, dataset:{}, attrs:{}, children:[], value:"", textContent:"", tabIndex:0,
    offsetWidth:230, offsetHeight:120, clientWidth:0,
    classList:{add(c){cls.add(c);}, remove(c){cls.delete(c);}, toggle(c, on){ if(on) cls.add(c); else cls.delete(c); }, contains:c => cls.has(c)},
    setAttribute(k, v){ e.attrs[k] = String(v); },
    getAttribute(k){ return e.attrs[k]; },
    addEventListener(t, f){ (e.l = e.l || {})[t] = f; },
    appendChild(c){ e.children.push(c); return c; },
    insertBefore(c){ e.children.push(c); return c; },
    closest(){ return null; },
    getBoundingClientRect(){ return {left:0, top:0, width:e.clientWidth, height:720}; },
    getContext(){ return e.ctx; },
    ctx:null,
    innerHTML:"",
  };
  return e;
}
function makeCtx(counter){
  return new Proxy({}, {
    get(target, key){
      if(key in target) return target[key];
      return () => { counter[key] = (counter[key] || 0) + 1; };
    },
    set(target, key, value){ target[key] = value; return true; },
  });
}
function runPage(html, opts){
  const ids = {}, counter = {};
  const pick = (attr, names) => names.map(n => { const b = makeEl("button"); b.dataset[attr] = n; return b; });
  const moments = pick("moment", ["rocni", "zima", "leto"]), routes = pick("path", ["progresivni", "konzervativni"]);
  const rafQueue = [];
  const windowObj = {
    innerHeight:opts.height || 900, devicePixelRatio:opts.dpr || 1,
    addEventListener(t, f){ (windowObj.l = windowObj.l || {})[t] = f; },
    matchMedia:() => ({matches:!!opts.reduced, addEventListener(){}}),
  };
  const document = {
    getElementById(i){
      if(!ids[i]){
        ids[i] = makeEl("div");
        if(i === "stage") ids[i].clientWidth = opts.width;
        if(i === "sparks") ids[i].ctx = makeCtx(counter);
      }
      return ids[i];
    },
    createElementNS:(ns, tag) => makeEl(tag),
    createElement:tag => makeEl(tag),
    querySelectorAll:s => ({"[data-moment]":moments, "[data-path]":routes}[s] || []),
  };
  const ctx = {
    document, window:windowObj, Intl, Math, Number, String, Object, Array, Float64Array, Float32Array, console,
    requestAnimationFrame:f => { rafQueue.push(f); return rafQueue.length; },
    setTimeout:f => { f(); return 1; }, clearTimeout(){}, setInterval:() => 1, clearInterval(){},
  };
  vm.runInNewContext(scriptOf(html), ctx);
  const pump = (times, step) => {
    let t = 1000;
    for(let k = 0; k < times; k++){
      t += step;
      const queue = rafQueue.splice(0);
      queue.forEach(f => f(t));
    }
  };
  return {ctx, ids, moments, routes, counter, pump, rafQueue};
}

const html = fs.readFileSync(path.join(HERE, "index.html"), "utf8");

const page = runPage(html, {width:1400});
page.pump(120, 16);
check(page.counter.stroke > 0, `smyčka kreslí částice, tahů na plátno ${page.counter.stroke}`);
const stateNow = () => page.ids.caption.innerHTML + " | " + page.ids.sub.textContent;

/* ---------- 2. Bilance ve všech případech ---------- */
const cons = page.ctx.checkConservation();
check(cons.cases === 156, `počet případů ${cons.cases} (26 let × 2 cesty × 3 okamžiky)`);
check(cons.worst <= 1, `největší reziduál uzlu ${cons.worst.toFixed(4)} MW, kontrol uzlů ${cons.nodes}, nejhorší ${JSON.stringify(cons.where)}`);

/* ---------- 3. Bilance z dat nezávisle na funkci stránky ---------- */
const start = html.indexOf("const DATA = ") + "const DATA = ".length;
const end = html.indexOf(";\nconst NF0");
const DATA = JSON.parse(html.slice(start, end).replace(/<\\\//g, "</"));
const ei = {}; DATA.edges.forEach((e, i) => { ei[e.id] = i; });
let worstIndep = 0, negatives = 0, flowCount = 0;
for(const route of Object.keys(DATA.states)) for(const mom of Object.keys(DATA.states[route])) for(const s of DATA.states[route][mom]){
  const f = id => s.e[ei[id]];
  let inp = f("dovoz"), out = f("vyvoz") + f("kBaterie") + f("kElektrolyzer");
  for(const e of DATA.edges){ if(e.kind === "in") inp += s.e[ei[e.id]]; if(e.kind === "out") out += s.e[ei[e.id]]; }
  worstIndep = Math.max(worstIndep, Math.abs(inp - out));
  for(const v of s.e){ flowCount++; if(v < 0) negatives++; }
  worstIndep = Math.max(worstIndep, Math.abs(f("kElektrolyzer") - f("h2Nadrz")), Math.abs(f("h2Nadrz") - f("h2Flotila") - s.m.tankDelta), Math.abs(f("kBaterie") - s.m.charge - s.m.batteryLoss));
  worstIndep = Math.max(worstIndep, Math.abs(f("dovoz") - Math.max(-s.m.balance, 0)));
}
check(worstIndep <= 1, `nezávislý přepočet uzlů, největší rozdíl ${worstIndep.toFixed(4)} MW`);
check(negatives === 0, `záporné toky ${negatives} z ${flowCount}`);

/* ---------- 4. Shoda s funkcí moment() skutečné hlavní stránky ---------- */
function mainPageMoments(){
  const main = fs.readFileSync(path.join(WEB, "index.html"), "utf8");
  const made = [];
  const el = tag => {
    const e = {tag, style:{}, dataset:{}, attrs:{}, children:[], value:"", textContent:"", className:"", previousElementSibling:null,
      setAttribute(k, v){ e.attrs[k] = v; }, addEventListener(t, f){ (e.l = e.l || {})[t] = f; },
      appendChild(c){ e.children.push(c); return c; },
      querySelector(s){ const c = el(); c.selector = s; made.push(c); return c; },
      querySelectorAll(s){
        const n = (e._h || "").split('class="jumpin"').length - 1;
        if(s !== ".jumpin") return [];
        return Array.from({length:n}, () => { const c = el(); c.selector = s; c.previousElementSibling = el(); made.push(c); return c; });
      },
      closest(){ return el(); },
      set innerHTML(v){ e._h = v; e.children = []; }, get innerHTML(){ return e._h || ""; },
      getBoundingClientRect(){ return {left:0, width:1000}; },
    };
    return e;
  };
  const ids = {};
  const pick = (attr, names) => names.map(n => { const b = el(); b.dataset[attr] = n; return b; });
  const toggles = pick("show", ["progresivni", "konzervativni", "vyroba", "spotreba"]), paths = pick("path", ["progresivni", "konzervativni"]);
  const modes = pick("mode", ["simple", "detail"]), views = pick("view", ["energy", "winter", "summer"]);
  const document = {
    getElementById(i){ return ids[i] = ids[i] || el(); },
    createElementNS:(ns, tag) => el(tag), createElement:() => el(), querySelector:() => el(),
    querySelectorAll:s => ({"[data-show]":toggles, "[data-path]":paths, "[data-mode]":modes, "[data-view]":views}[s] || []),
    documentElement:el(),
  };
  const ctx = {document, Intl, Math, Number, String, Object, Map, matchMedia:() => ({matches:false}), innerWidth:1200, console};
  vm.runInNewContext(scriptOf(main), ctx);
  return {ctx, views};
}
try {
  const main = mainPageMoments();
  const compare = (viewIndex, mom) => {
    main.views[viewIndex].l.click();
    let worst = 0, label = "";
    for(const route of ["progresivni", "konzervativni"]) for(let i = 0; i < DATA.years.length; i++){
      const a = main.ctx.moment(route, i), b = DATA.states[route][mom][i].m;
      const pairs = {avail:b.avail, load:b.load, balance:b.balance, batteryMw:b.batteryMw, electro:b.electro, charge:b.charge, heat:b.heat, forH2:b.forH2, spare:b.spare};
      for(const k of Object.keys(pairs)){
        const gap = Math.abs(a[k] - pairs[k]);
        if(gap > worst){ worst = gap; label = `${route} ${DATA.years[i]} ${k}`; }
      }
    }
    check(worst <= 0.01, `moment() hlavní stránky, ${mom}: největší rozdíl ${worst.toFixed(5)} MW (${label})`);
  };
  compare(1, "zima");
  compare(2, "leto");
  /* Roční energie z hlavní stránky: součty výroby a spotřeby. */
  let worstYear = 0;
  for(const route of ["progresivni", "konzervativni"]){
    const gen = main.ctx.totals(route, "vyroba"), use = main.ctx.totals(route, "spotreba");
    gen.forEach((g, i) => { worstYear = Math.max(worstYear, Math.abs(g * 1000 / 8760 - DATA.states[route].rocni[i].m.avail), Math.abs(use[i] * 1000 / 8760 - DATA.states[route].rocni[i].m.load)); });
  }
  check(worstYear <= 0.01, `roční součty hlavní stránky: největší rozdíl ${worstYear.toFixed(5)} MW`);
} catch(err){
  check(false, "hlavní stránku se nepodařilo spustit: " + err.message);
}

/* ---------- 5. Kontrolní tabulka v milnících; rozdíl se hlásí, nic se neupravuje ---------- */
const lines = fs.readFileSync(path.join(WEB, "sezonni_kontrola.csv"), "utf8").trim().split(/\r?\n/);
const header = lines[0].split(",");
const notes = [];
let worstTable = 0;
for(const line of lines.slice(1)){
  const cells = line.split(","), row = {};
  header.forEach((h, k) => { row[h] = cells[k]; });
  const i = Number(row.rok) - 2025, z = DATA.states[row.cesta].zima[i].m, l = DATA.states[row.cesta].leto[i].m;
  const pairs = [["zima_zatizeni_MW", z.load], ["zima_dostupny_MW", z.avail], ["leto_zatizeni_bez_flexibilnich_MW", l.load], ["leto_dostupny_MW", l.avail], ["leto_baterie_nabijeni_MW", l.charge], ["leto_elektrokotle_MW", l.heat], ["leto_pro_vodik_MW", l.forH2], ["leto_potreba_elektrolyzy_MW", l.electro]];
  for(const [name, value] of pairs){
    const gap = Math.abs(Number(row[name]) - value);
    if(name !== "leto_potreba_elektrolyzy_MW") worstTable = Math.max(worstTable, gap);
    if(gap > 0.5) notes.push(`${row.cesta} ${row.rok} ${name}: tabulka ${row[name]}, stránka ${value.toFixed(1)}`);
  }
}
console.log(`INFO  kontrolní tabulka proti datům stránky, největší rozdíl bez potřeby elektrolýzy ${worstTable.toFixed(2)} MW`);
notes.forEach(n => console.log("INFO  " + n));

/* ---------- 6. Ovládání a texty ---------- */
for(const route of page.routes) for(const mom of page.moments){
  route.l.click(); mom.l.click();
  for(const y of [2025, 2030, 2040, 2049, 2050]){
    page.ids.year.l.input({target:{value:String(y)}});
    page.pump(50, 16);
  }
  console.log(`TEXT  ${route.dataset.path} ${mom.dataset.moment} 2050: ${stateNow()}`);
  page.ids.year.l.input({target:{value:"2040"}});
  console.log(`TEXT  ${route.dataset.path} ${mom.dataset.moment} 2040: ${stateNow()}`);
}
/* Popisky pod ukazatelem pro každý uzel, ve všech okamžicích. */
for(const mom of page.moments){
  mom.l.click();
  for(const n of DATA.nodes.concat([{id:"kraj"}])){
    const tip = page.ctx.tipForNode(n.id);
    check(!/undefined|NaN|null/.test(tip), `popisek ${mom.dataset.moment} ${n.id}`);
  }
  DATA.edges.forEach((e, i) => { if(/undefined|NaN|null/.test(page.ctx.tipForEdge(i))) check(false, "popisek toku " + e.id); });
}

/* ---------- 7. Rozmístění: nic se nepřekrývá a nic nepřesahuje ---------- */
for(const width of [340, 360, 390, 430, 600, 759, 760, 900, 1099, 1100, 1280, 1400, 1560, 1920]){
  for(const viewH of [700, 900, 1200]){
    const L = page.ctx.layout(width, viewH), boxes = Object.entries(L.boxes), bad = [];
    for(let a = 0; a < boxes.length; a++){
      const [ia, A] = boxes[a];
      if(A.x - A.w / 2 < 0 || A.x + A.w / 2 > width || A.y - A.h / 2 < 0 || A.y + A.h / 2 > L.stageH) bad.push("mimo " + ia);
      const hubGap = Math.hypot(Math.max(Math.abs(A.x - L.hub.x) - A.w / 2, 0), Math.max(Math.abs(A.y - L.hub.y) - A.h / 2, 0));
      if(hubGap < L.hub.r + 4) bad.push("na kruhu " + ia);
      for(let b = a + 1; b < boxes.length; b++){
        const [ib, B] = boxes[b];
        if(Math.abs(A.x - B.x) < (A.w + B.w) / 2 + 3 && Math.abs(A.y - B.y) < (A.h + B.h) / 2 + 3) bad.push(ia + "+" + ib);
      }
    }
    if(bad.length) check(false, `rozmístění ${width}×${viewH}: ${bad.join(", ")}`);
    const worstStack = 1900 * L.scale;
    if(worstStack > 1.44 * L.hub.r) check(false, `svazek ${worstStack.toFixed(0)} px se nevejde do kruhu ${L.hub.r.toFixed(0)} px při šířce ${width}`);
  }
}
check(true, "rozmístění prošlo pro šířky 340 až 1920 (případné chyby jsou vypsané výš)");

/* Odhad šířky textu: Saira kolem 0,55 em. */
function fits(text, px, room){ return text.length * px * 0.55 <= room; }
for(const n of DATA.nodes){
  if(!fits(n.label, 12.5, 178 - 20 - 30 - 9 - 2)) check(false, `dlouhý název ${n.label}`);
  if(!fits(n.short, 10.5, 118 - 4 - 2)) check(false, `dlouhý krátký název ${n.short}`);
  if(!fits(n.short, 10.5, 80 - 4 - 2)) check(false, `krátký název na telefon ${n.short}`);
}
const maxLabel = Math.max(...DATA.nodes.map(n => n.label.length));
console.log(`INFO  nejdelší název ${maxLabel} znaků`);

/* ---------- 8. Omezený pohyb a úzký displej ---------- */
const still = runPage(html, {width:390, reduced:true});
check(still.rafQueue.length === 0, "při omezeném pohybu neběží smyčka");
check(still.counter.fill > 0, `při omezeném pohybu jsou šipky směru, výplní ${still.counter.fill}`);
still.moments[2].l.click();
check(still.rafQueue.length === 0, "přepnutí okamžiku smyčku nespustí");
const phone = runPage(html, {width:390, dpr:3});
phone.pump(30, 16);
check(phone.ids.sparks.width === 780, `plátno telefonu ${phone.ids.sparks.width} px, hustota omezená na 2`);

/* ---------- 9. Výkon logiky: délka snímku bez kreslení v prohlížeči ---------- */
const perf = runPage(html, {width:1920, dpr:2});
const t0 = process.hrtime.bigint();
perf.pump(600, 16);
const ms = Number(process.hrtime.bigint() - t0) / 1e6 / 600;
console.log(`INFO  výpočet jednoho snímku v node ${ms.toFixed(3)} ms; samotné kreslení v prohlížeči změřit nejde`);

/* ---------- 10. Obsah souborů složky ---------- */
const stripped = html.replace(/[A-Za-z0-9+/]{200,}={0,2}/g, "");
const BANNED = ["ZE" + "VO", "stud" + "ie", "stud" + "ii", "CE" + "ET", "Flow" + "Sim", "V" + "ŠB", "Cla" + "ude", "age" + "nt", "zada" + "vatel", "kole" + "g", "TO" + "DO", "Anth" + "ropic"];
const files = fs.readdirSync(HERE).filter(f => fs.statSync(path.join(HERE, f)).isFile());
for(const f of files){
  const raw = fs.readFileSync(path.join(HERE, f), "utf8");
  const text = f === "index.html" ? stripped : raw.replace(/[A-Za-z0-9+/]{200,}={0,2}/g, "");
  const hits = BANNED.filter(w => text.toLowerCase().includes(w.toLowerCase()));
  check(hits.length === 0, `zakázaná slova v ${f}: ${hits.join(", ") || "žádná"}`);
}
check(!/data:image|<img|\.png|\.webp|\.jpe?g|\.gif/i.test(stripped), "žádný rastr");
check(!/<script[^>]+src=|<link[^>]+href=|@import|url\(\s*["']?https?:|\bfetch\(|XMLHttpRequest/i.test(stripped), "žádné vnější skripty ani síťová volání");
check(html.includes("Pracovní ukázka, čísla se ještě mění."), "věta o pracovní ukázce je na stránce");

console.log(failures ? `\nCHYB: ${failures}` : "\nVše prošlo.");
process.exit(failures ? 1 : 0);
