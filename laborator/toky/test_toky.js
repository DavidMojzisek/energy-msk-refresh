// Logická kontrola stránky bez prohlížeče. Spuštění: node test_toky.js
const fs = require("fs");
const path = require("path");
const vm = require("vm");

const HERE = __dirname;
const ROOT = path.resolve(HERE, "..", "..", "..");
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
    tag, style:{setProperty(){}}, dataset:{}, attrs:{}, children:[], value:"", textContent:"", tabIndex:0, disabled:false,
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
    ctx:null, innerHTML:"",
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
  const ids = {}, counter = {}, bg = {};
  const pick = (attr, names) => names.map(n => { const b = makeEl("button"); b.dataset[attr] = n; return b; });
  const moments = pick("moment", ["rocni", "zima", "leto"]), routes = pick("path", ["progresivni", "konzervativni"]);
  const years = pick("year", ["2025", "2050"]), steels = pick("steel", ["1", "0"]);
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
        if(i === "bgfx") ids[i].ctx = makeCtx(bg);
      }
      return ids[i];
    },
    createElementNS:(ns, tag) => makeEl(tag),
    createElement:tag => makeEl(tag),
    querySelectorAll:s => ({"[data-moment]":moments, "[data-path]":routes, "[data-year]":years, "[data-steel]":steels, "[data-scen]":ids.segScen ? ids.segScen.children : []}[s] || []),
  };
  const ctx = {
    document, window:windowObj, Intl, Math, Number, String, Object, Array, Float64Array, Float32Array, console, JSON,
    requestAnimationFrame:f => { rafQueue.push(f); return rafQueue.length; },
    setTimeout:f => { f(); return 1; }, clearTimeout(){}, setInterval:() => 1, clearInterval(){},
  };
  vm.runInNewContext(scriptOf(html) + "\n;globalThis.ui = ui; globalThis.layoutBoxes = layoutBoxes;", ctx);
  const pump = (times, step) => {
    let t = 1000;
    for(let k = 0; k < times; k++){
      t += step;
      const queue = rafQueue.splice(0);
      queue.forEach(f => f(t));
    }
  };
  return {ctx, ids, moments, routes, years, steels, counter, bg, pump, rafQueue};
}

const html = fs.readFileSync(path.join(HERE, "index.html"), "utf8");
const page = runPage(html, {width:1400});
page.pump(60, 16);
check(page.counter.stroke > 0, `smyčka kreslí částice, tahů na plátno ${page.counter.stroke}`);
check((page.bg.stroke || 0) > 0, `pozadí se kreslí v zimě, tahů ${page.bg.stroke || 0}`);

/* ---------- 2. Data a bilance ---------- */
const start = html.indexOf("const DATA = ") + "const DATA = ".length;
const end = html.indexOf(";\nconst NF0");
const DATA = JSON.parse(html.slice(start, end).replace(/<\\\//g, "</"));
const cons = page.ctx.checkConservation();
check(cons.cases === 2 * 54 * 3 + 2 * 3, `počet stavů ${cons.cases} (54 kombinací × 2 cesty × 3 pohledy, k tomu rok 2025)`);
check(cons.worst <= 1, `největší reziduál uzlu ${cons.worst.toFixed(4)} MW, kontrol uzlů ${cons.nodes}, nejhorší ${JSON.stringify(cons.where)}`);
const ei = {}; DATA.edges.forEach((e, i) => { ei[e.id] = i; });
let neg = 0, flows = 0, tankToGrid = 0, h2Cars = 0;
for(const it of page.ctx.allStates()){
  for(const v of it.state.e){ flows++; if(v < 0) neg++; }
}
for(const e of DATA.edges){
  if(e.from === "nadrz" && e.to !== "flotila") tankToGrid++;
}
check(neg === 0, `záporné toky ${neg} z ${flows}`);
check(tankToGrid === 0, "nádrž má jediný odtok, do flotily");
check(DATA.nodes.find(n => n.id === "flotila").items.length === 0 && !JSON.stringify(DATA.nodes).includes("Vodík pro osobní auta"), "osobní auta na vodíku nikde nejsou");
const BAT = JSON.parse(fs.readFileSync(path.join(ROOT, "graf_scenare/hodinovy_model/vysledky/pevna_prepocet_baterie.json"), "utf8")).baterie;
const eqProg = DATA.equip;
check(eqProg.bateriePWh === BAT.E_GWh && eqProg.bateriePMW === BAT.P_MW && eqProg.elektrolyzerMW === BAT.elektrolyzer_MW && eqProg.nadrzT === 20 && eqProg.plynMW.progresivni === 433 && eqProg.kotleMW.progresivni === 70, `zařízení ${BAT.E_GWh} GWh, ${BAT.P_MW} MW, ${BAT.elektrolyzer_MW} MW, 20 t, 433 MW, 70 MW čteno z modelu`);

/* ---------- 3. Výchozí stav proti zveřejněnému přepočtu ---------- */
const csvOf = name => {
  const lines = fs.readFileSync(path.join(ROOT, "graf_scenare/hodinovy_model/vysledky", name), "utf8").trim().split(/\r?\n/);
  const head = lines[0].split(",");
  return lines.slice(1).map(l => { const c = l.split(","), r = {}; head.forEach((h, i) => { r[h] = c[i]; }); return r; });
};
const pub = csvOf("sobestacnost_vychozi.csv");
const pr = pub.find(r => r.cesta === "progresivni" && r.smr === "1" && r.vodik === "rovnomerne"), kr = pub.find(r => r.cesta === "konzervativni" && r.smr === "0");
const sp = DATA.sums.progresivni["1011"], sk = DATA.sums.konzervativni["1011"];
for(const [name, got, want] of [["progresivní výroba", sp.vyroba, +pr.vyroba_GWh], ["progresivní spotřeba", sp.spotreba, +pr.spotreba_GWh], ["progresivní bilance", sp.bilance, +pr.rocni_bilance_tabulka_GWh], ["konzervativní výroba", sk.vyroba, +kr.vyroba_GWh], ["konzervativní spotřeba", sk.spotreba, +kr.spotreba_GWh], ["konzervativní bilance", sk.bilance, +kr.rocni_bilance_tabulka_GWh], ["konzervativní dovoz", sk.dovoz, +kr.dovoz_GWh]]){
  check(Math.abs(got - want) <= 0.5, `${name}: ${got} proti ${want} GWh`);
}
const tanks = csvOf("pevna_nadrz_male.csv").filter(r => r.varianta_t === "20");
const meanImp = tanks.reduce((a, r) => a + +r.dovoz_GWh, 0) / tanks.length;
check(Math.abs(sp.dovoz - meanImp) <= 0.5, `nádrž 20 t, dovoz: ${sp.dovoz} proti ${meanImp.toFixed(2)} GWh`);
check(Math.abs(sp.spickaZima - Math.max(...tanks.map(r => +r.zima_spicka_dovozu_MW))) <= 1, `nádrž 20 t, největší dovoz v zimě ${sp.spickaZima} MW`);
const base = DATA.baseSum.progresivni;
check(Math.abs(base.dovoz - (base.spotreba - base.vyroba)) <= 0.5, `2025 dovoz ${base.dovoz} GWh sedí na základ tabulky`);

/* ---------- 4. Ovládání ---------- */
const textNow = () => page.ids.caption.innerHTML + " | " + page.ids.sub.textContent;
for(const r of page.routes) for(const mo of page.moments) for(const y of page.years){
  r.l.click(); mo.l.click(); y.l.click();
  for(const s of page.ids.segScen.children){
    if(y.dataset.year === "2050") s.l.click();
    const t = textNow() + " " + page.ids.stateNote.textContent;
    if(/undefined|NaN|null/.test(t)) check(false, "chybný text: " + t);
  }
}
page.routes[0].l.click(); page.years[1].l.click(); page.moments[1].l.click();
const scenBtns = page.ids.segScen.children;
check(scenBtns.length === 5, `scénářů ${scenBtns.length}: ${scenBtns.map(b => b.textContent).join(", ")}`);
const expected = {projekce:"1011", starne:"0000", navrat:"2011", teple:"1211", digital:"1021"};
for(const b of scenBtns){
  b.l.click();
  check(page.ctx.comboKey(page.ctx.ui.combo) === expected[b.dataset.scen], `${b.textContent}: kombinace ${page.ctx.comboKey(page.ctx.ui.combo)}`);
}
scenBtns[0].l.click();
const dflt = textNow();
check(dflt.includes("zimní hodině") && page.ids.snapNote.textContent === "", "výchozí stav bez poznámky o nejbližším stavu");
console.log("INFO  " + dflt);

const s0 = page.ids.s0;
const p0 = page.ctx.stopPos(0, 1, "progresivni");
s0.l.input({target:{value:String(p0 + 3)}});
const snapped = page.ids.snapNote.textContent;
check(snapped.includes("nejbližší spočítaný stav") && snapped.includes("neběžel"), "mimo spočítaný stav to stránka řekne: " + snapped);
check(page.ctx.ui.scen === "navrat" || page.ctx.ui.scen === "projekce" || page.ctx.ui.scen === null, `scénář po posunu ${page.ctx.ui.scen}`);
for(let pos = 0; pos <= 20; pos++){
  s0.l.input({target:{value:String(pos)}});
  const v = page.ctx.physical(0, pos, "progresivni"), st = DATA.drivers.populace, i = page.ctx.ui.combo[0];
  const best = st.reduce((b, x, k) => Math.abs(x.hodnota - v) < Math.abs(st[b].hodnota - v) ? k : b, 0);
  if(i !== best) check(false, `poloha ${pos}: vybrán stupeň ${i}, nejbližší je ${best}`);
}
scenBtns[0].l.click();
const a = page.ctx.sumFor("progresivni", 2050).dovoz;
page.steels[1].l.click();
const b = page.ctx.sumFor("progresivni", 2050).dovoz;
check(b < a, `první pec sníží dovoz: ${a} na ${b} GWh`);
check(page.ctx.ui.scen === null, "ocel mimo scénář ukáže vlastní kombinaci");
page.ids.s1.l.input({target:{value:"10"}});
page.ids.s2.l.input({target:{value:"10"}});
console.log("INFO  " + page.ids.stateNote.textContent);
scenBtns[0].l.click();
page.routes[1].l.click();
check(page.ctx.valueText(2, DATA.drivers.datacentra.konzervativni[1].hodnota) === "10 MW", "konzervativní datacentra čtena z řádku cesty, 10 MW");
page.routes[0].l.click();
page.years[0].l.click();
check(page.ids.s0.disabled === true && page.ids.stateNote.textContent.includes("Rok 2025"), "v roce 2025 jsou posuvníky vypnuté a stránka to říká");
check(flowsIs0(page.ctx.flowsFor("progresivni", 2025, "rocni"), "smr"), "v roce 2025 SMR nevyrábí");
function flowsIs0(st, id){ return st.e[ei[id]] === 0; }
page.years[1].l.click();

/* Popisky a nápovědy všech uzlů */
for(const n of DATA.nodes.concat([{id:"kraj"}])){
  for(const mo of page.moments){
    mo.l.click();
    const t = page.ctx.tipForNode(n.id);
    if(/undefined|NaN/.test(t)) check(false, `nápověda ${n.id}: ${t}`);
  }
}
for(let i = 0; i < DATA.edges.length; i++) if(/undefined|NaN/.test(page.ctx.tipForEdge(i))) check(false, "nápověda toku " + i);
check(html.includes('type="range"'),"posuvníky jsou nativní, ovladatelné klávesnicí");
check(DATA.nodes.length > 0 && html.includes("el.tabIndex = 0"), "uzly lze vybrat klávesnicí");

/* ---------- 5. Pozadí, omezený pohyb, telefon ---------- */
const still = runPage(html, {width:1400, reduced:true});
still.pump(10, 16);
check(still.rafQueue.length === 0 && (still.counter.stroke || 0) === 0, "omezený pohyb: žádná smyčka ani částice");
const phone = runPage(html, {width:390, height:800, dpr:2});
phone.pump(3, 16);
check(phone.ids.bgToggle.attrs["aria-pressed"] === "false", "na telefonu je pozadí ve výchozím stavu vypnuté");
check(!phone.bg.stroke, "na telefonu se pozadí nekreslí");
phone.ids.bgToggle.l.click();
phone.pump(3, 16);
check((phone.bg.stroke || 0) > 0, "po zapnutí se pozadí na telefonu kreslí");
const overlap = page.ctx.coversNumber;
check(typeof overlap === "function", "vločky se vyhýbají uzlům a středu");
for(const b of Object.values(page.ctx.layoutBoxes || {})) if(!overlap(b.x, b.y, 0)) check(false, "střed uzlu není chráněný");
for(const w of [320, 390, 760, 1100, 1400]){
  const p = runPage(html, {width:w});
  const L = p.ctx.layout(w, 900);
  let wide = 0;
  for(const id of Object.keys(L.boxes)){ const b = L.boxes[id]; wide = Math.max(wide, b.x + b.w / 2 - w, -(b.x - b.w / 2)); }
  check(wide <= 0, `šířka ${w}: žádný uzel nepřesahuje, přesah ${wide.toFixed(1)} px`);
}

/* ---------- 6. Zakázané věci na stránce ---------- */
const clean = html.replace(/@font-face[^}]*}/g, "");
for(const w of [...JSON.parse(fs.readFileSync(path.join(__dirname, "../../../nastroje/zakazana_slova.json"), "utf8")), "cdn"]){
  check(!clean.toLowerCase().includes(w.toLowerCase()), `na stránce není „${w}“`);
}
for(const c of ["\u2013", "\u2014", "\u2192", "\u2190", "\u21d2"]) check(!clean.includes(c), `na stránce není znak U+${c.codePointAt(0).toString(16)}`);
check(!/<script[^>]+src=/.test(clean) && !/<link[^>]+stylesheet/.test(clean), "žádné vnější skripty ani styly");
const gz = require("zlib").gzipSync(html).length;
check(gz < 2 * 1024 * 1024, `velikost stránky ${Math.round(html.length / 1024)} kB, gzip ${Math.round(gz / 1024)} kB`);

console.log(failures ? `CHYB ${failures}` : "test OK");
process.exit(failures ? 1 : 0);
