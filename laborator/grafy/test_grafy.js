// Logická kontrola stránky grafů bez prohlížeče. Spuštění: node test_grafy.js
const fs = require("fs");
const path = require("path");
const vm = require("vm");
const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");
let failures = 0;
const check = (ok, text) => { console.log((ok ? "OK    " : "CHYBA ") + text); if(!ok) failures++; };

function runPage(width){
  const ids = {};
  const el = tag => {
    const e = {tag, style:{}, dataset:{}, attrs:{}, children:[], textContent:"", clientWidth:0, innerHTML:"",
      setAttribute(k, v){ e.attrs[k] = String(v); }, getAttribute(k){ return e.attrs[k]; },
      addEventListener(t, f){ (e.l = e.l || {})[t] = f; },
      appendChild(c){ e.children.push(c); return c; },
      getBoundingClientRect(){ return {left:0, top:0, width:width, height:400}; }};
    let inner = "";
    Object.defineProperty(e, "innerHTML", {get(){ return inner; }, set(v){ inner = v; if(v === "") e.children = []; }});
    return e;
  };
  const document = {getElementById(i){ if(!ids[i]){ ids[i] = el("div"); ids[i].clientWidth = width; } return ids[i]; }, createElement:tag => el(tag)};
  const ctx = {document, window:{innerWidth:width, addEventListener(){}}, Intl, Math, Number, String, Object, Array, console, setTimeout:f => 1, clearTimeout(){}};
  vm.runInNewContext(html.slice(html.indexOf('"use strict";'), html.lastIndexOf("</script>")) + "\n;globalThis.ui = ui; globalThis.D = D; globalThis.SERIES = SERIES;", ctx);
  return {ctx, ids};
}
const texts = ["heatTitle", "hHeat", "weekTitle", "hWeek", "stepTitle", "hSteps", "tempoTitle", "hTempo", "hSplit"];
const bad = (p, label) => {
  for(const id of texts.concat(["tHeat", "tWeek", "tSteps", "tTempo", "tSplit", "cHeat", "cWeek", "cSteps", "cTempo", "cSplit"])){
    const v = (p.ids[id].innerHTML || "") + (p.ids[id].textContent || "");
    if(!v) check(false, `${label}: ${id} je prázdné`);
    if(/undefined|NaN|null/.test(v)) check(false, `${label}: ${id} obsahuje ${v.match(/undefined|NaN|null/)[0]}`);
  }
};
const page = runPage(900);
const {D} = page.ctx;
bad(page, "výchozí");
for(const w of [320, 390, 900]){
  const p = runPage(w);
  bad(p, "šířka " + w);
  for(const [k] of [["progresivni"], ["konzervativni"]]){
    p.ids.segPath.children.find(b => b.dataset.k === k).l.click();
    bad(p, `${w} ${k}`);
    for(const b of p.ids.segHeat.children.slice()){ const f = p.ids.segHeat.children.find(x => x.dataset.k === b.dataset.k); f.l.click(); bad(p, `${w} ${k} rok ${b.dataset.k}`); }
    for(const b of p.ids.segWeek.children.slice()){ const f = p.ids.segWeek.children.find(x => x.dataset.k === b.dataset.k); f.l.click(); bad(p, `${w} ${k} týden ${b.dataset.k}`); }
  }
  check(true, `šířka ${w}: všechny volby se vykreslí bez chyby`);
}
/* Data a vlastnosti grafů */
const week = D.weeks.progresivni.roky[String(D.weeks.progresivni.nejhorsi)];
const sup = page.ctx.SERIES.reduce((a, [k]) => a + week[k][10], 0);
check(Math.abs(sup - week.zatizeni[10] - (week.vodik[10])) < 1000, "nabídka týdne je nad zatížením");
for(const p of ["progresivni", "konzervativni"]) for(const y of Object.keys(D.weeks[p].roky)){
  const w = D.weeks[p].roky[y];
  if(w.teplota >= 0) check(false, `${p} ${y}: týden není studený, ${w.teplota} °C`);
  const n = page.ctx.SERIES.reduce((a, [k]) => a + (w[k].length === 168 ? 1 : 0), 0);
  if(n !== 7) check(false, `${p} ${y}: řady nemají 168 hodin`);
}
check(true, "všechny týdny mají průměr pod nulou a 168 hodin");
check(D.heat.progresivni.median.length === 8760 && D.heat.konzervativni.roky["2017"].length === 8760, "rok po hodinách má 8 760 hodnot");
const sm = D.steps.progresivni.smr, zd = D.steps.progresivni.zdroje;
check(sm.every(r => r.bezZdroje) && zd.every(r => !r.bezZdroje), "druhý a další SMR jsou označené jako bez podkladu");
check(page.ids.cSteps.innerHTML.includes("url(#hatch)"), "bloky bez podkladu jsou šrafované");
check(zd[0].dovoz > zd[1].dovoz && zd[1].dovoz > zd[2].dovoz, `každý krok snižuje dovoz: ${zd.map(r => r.dovoz).join(", ")}`);
check(D.split.progresivni.every(r => r.proVodik > 0) && D.split.konzervativni.every(r => r.proVodik === 0), "dovoz pro vodík jen v progresivní cestě");
check(D.tempo.length === 4 && D.rekord.vitr_MW_rok.hodnota > 0, `tempo: ${D.tempo.map(t => t.vitrKrat).join(", ")}`);
console.log("INFO  " + page.ids.hHeat.innerHTML.replace(/<[^>]+>/g, "").slice(-300));
console.log("INFO  " + page.ids.hWeek.innerHTML.replace(/<[^>]+>/g, "").slice(-340));
console.log("INFO  " + page.ids.hSteps.innerHTML.replace(/<[^>]+>/g, "").slice(-300));
console.log("INFO  " + page.ids.hTempo.innerHTML.replace(/<[^>]+>/g, "").slice(-220));
console.log("INFO  " + page.ids.hSplit.innerHTML.replace(/<[^>]+>/g, "").slice(-200));
/* Zakázané věci */
for(const w of [...JSON.parse(fs.readFileSync(path.join(__dirname, "../../../nastroje/zakazana_slova.json"), "utf8")), "http"]) check(!html.toLowerCase().includes(w), `na stránce není „${w}“`);
for(const c of ["–", "—", "→", "←"]) check(!html.includes(c), `na stránce není znak U+${c.codePointAt(0).toString(16)}`);
check(!/<script[^>]+src=/.test(html), "žádné vnější skripty");
console.log(failures ? `CHYB ${failures}` : "test OK");
process.exit(failures ? 1 : 0);
