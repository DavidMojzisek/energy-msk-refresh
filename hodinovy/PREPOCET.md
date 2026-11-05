# Přepočet bilance MSK 2050: hodiny, flotila, křivky a soběstačnost

Stav k 2026-11-05. Výpočet stojí na tabulce položek a hodinovém modelu pro 5 povětrnostních let 2015 až 2019. Soběstačnost znamená jen elektřinu vyrobenou v kraji. Palivo pro SMR i zemní plyn je dovezené i tehdy, když je bilance elektřiny kladná. Výchozí nastavení je jediné: baterie 2,7 GWh a 675 MW s vyrovnáváním dne, elektrolyzér 197 MW, malá nádrž 20 t, flotila 70 % na bateriích a 30 % na vodíku v MHD a nákladní dopravě, auta na vodík nejezdí. Dovoz 4 667 GWh, vývoz 3,0 GWh, zimní špička dovozu 851 MW, bilance prosince až února −1 362 GWh. Jiný běh má vždy svůj název, hlavně rovnoměrná elektrolýza bez nádrže. Rozvrh plynu, elektrolýzy ze sítě a nádrže zná celý rok dopředu, baterie zná den dopředu přesně.

## 1. Odpověď

**S elektrárnami, které obě cesty předpokládají, kraj v roce 2050 zůstane závislý na dovozu.** Progresivní cesta vyrobí 7 862 GWh a spotřebuje 12 526 GWh, tedy 62,8 %. Chybí 4 664 GWh. Konzervativní cesta vyrobí 3 956 GWh ze 8 262 GWh, tedy 47,9 %, a chybí 4 306 GWh.

**Závislost plyne z toho, kolik elektráren cesty předpokládají a kolik elektřiny spotřebují, není to fyzikální mez.** Konzervativní cesta by rok uzavřela 1 774 MW větru navíc, tedy 1 870 MW uvnitř meze studie 2 014 MW. Překážkou je tempo: 73 MW za rok, 8,0krát víc než největší roční přírůstek kraje, a v hodinách i tak zůstane dovoz 532 GWh a 457 GWh přebytku. Progresivní cesta rok uzavře větrem na mezi a 1,7 GWp fotovoltaiky navíc, nebo více než jedním dalším SMR (1,28 čistého bloku), pro který podklad není.

| Úroveň | Progresivní, 1 SMR, flotila 70:30, malá nádrž | Konzervativní, bez SMR |
|---|---|---|
| 1, rok | Nesplněno, −4 664 GWh. Podíl běhů pod 25 % | Nesplněno, −4 306 GWh. Podíl běhů pod 5 %. Rok uzavře vítr uvnitř meze, překáží tempo |
| 2, říjen až březen | Nesplněno, −2 474 GWh. Podíl běhů pod 10 % | Nesplněno, −2 147 GWh. Podíl běhů pod 1 %. Vítr samotný +1 668 MW |
| 2, prosinec až únor | Nesplněno, −1 362 GWh. Podíl běhů pod 10 % | Nesplněno, −1 062 GWh. Podíl běhů pod 1 %. Vítr samotný +1 625 MW |
| 3, hodiny | Nesplněno. Bez dovozu 7,2 % hodin, zimní špička dovozu 907 MW v nejhorším roce při nádrži 20 t, roční špička 907 MW | Nesplněno. Bez dovozu 0,0 % hodin, špička 497 MW |

Podíl běhů je pásmo, ne přesné číslo. Závisí na neověřené korelaci a mezích, viz oddíl 7. Úroveň 2 v simulaci počítá s rovnoměrnou elektrolýzou.

## 2. Bilance

| Cesta | Veličina, GWh | 2026 | 2030 | 2040 | 2050 |
|---|---|---|---|---|---|
| Progresivní | Výroba | 2 498 | 2 973 | 4 276 | 7 862 |
| Progresivní | Spotřeba | 7 006 | 7 285 | 9 748 | 12 526 |
| Konzervativní | Výroba | 2 506 | 3 243 | 3 064 | 3 956 |
| Konzervativní | Spotřeba | 7 003 | 7 050 | 8 070 | 8 262 |

Hodnoty 2050 po skupinách, GWh:

| Skupina | Progresivní | Konzervativní |
|---|---|---|
| SMR | 3 942,0 | 0,0 |
| Fotovoltaika | 1 580,8 | 426,8 |
| Vítr | 1 539,9 | 236,7 |
| Plyn nový a syntetický | 115,2 | 2 279,5 |
| Kogenerace a hutní plyny | 60,0 | 389,1 |
| Biomasa, bioplyn, voda, odpad, ostatní | 624,3 | 624,3 |
| Ocel | 2 285,5 | 1 895,5 |
| Ostatní průmysl a doly | 2 006,7 | 1 586,4 |
| Domácnosti a služby | 1 197,6 | 1 347,1 |
| Vytápění a chlazení | 1 389,8 | 1 334,4 |
| Doprava na bateriích a trolejích | 1 774,5 | 510,4 |
| Vodík | 1 241,8 | 13,7 |
| Datacentra | 700,8 | 70,1 |
| Vlastní spotřeba zdrojů | 460,1 | 218,2 |
| Ostatní energetika | 1 000,8 | 1 000,8 |
| Ztráty v sítích a baterií | 468,2 | 285,5 |

Bilance 2050: progresivní −4 663,7 GWh, konzervativní −4 305,8 GWh.

## 3. Co se změnilo

Všechny řádky, kde se změnila hodnota 2050, mez nebo stupeň. Účinek je změna ročního schodku v GWh: kladné číslo schodek zvětšuje. Odvozené řádky a řádky z hodinového výpočtu jsou po ustálení.

| Řádek | Cesta | Staré P50 | Nové P50 | Staré P10 až P90 | Nové P10 až P90 | Stupeň | Účinek GWh | Důvod |
|---|---|---|---|---|---|---|---|---|
| vítr | progresivni | 1 539,9 | 1 539,9 | 866,1 až 3 372,0 | 866,1 až 3 372,0 | C na D | 0,0 | Stejná metoda krajského podílu jako FVE, stupeň D. Rok 2026 společný, 41,8 MW × 2 471 h. |
| vítr | konzervativni | 236,7 | 236,7 | 129,9 až 506,7 | 129,9 až 506,7 | C na D | 0,0 | Stejná metoda krajského podílu jako FVE, stupeň D. Rok 2026 společný, 41,8 MW × 2 471 h. |
| biomasa | progresivni | 432,0 | 432,0 | 370,0 až 568,5 | 370,0 až 475,0 | C | 0,0 | P90 475 GWh, studie uvádí potenciál jako prakticky vyčerpaný. |
| biomasa | konzervativni | 432,0 | 432,0 | 370,0 až 568,5 | 370,0 až 475,0 | C | 0,0 | P90 475 GWh, studie uvádí potenciál jako prakticky vyčerpaný. |
| SMR | progresivni | 3 942,0 | 3 942,0 | 3 504,0 až 4 029,5 | 3 461,0 až 3 942,0 | C | 0,0 | P50 beze změny. P10 změřené využití ČR 2024, P90 = P50. Rok P90 2050: bez SMR je samostatný případ. |
| SMR | konzervativni | 0,0 | 0,0 | 0,0 až 0,0 | 0,0 až 0,0 | B na D | 0,0 | Volba cesty, žádná studie ji neuvádí. |
| syntetický plyn z odpadu | progresivni | 231,0 | 115,2 | 148,5 až 288,0 | 74,1 až 231,0 | D | 115,8 | Výroba 0,48 MWh/t podle Dopadové studie s.137 místo 0,96 MWh/t. Dřívější výpočet je P90. |
| syntetický plyn z odpadu | konzervativni | 231,0 | 115,2 | 148,5 až 288,0 | 74,1 až 231,0 | D | 115,8 | Výroba 0,48 MWh/t podle Dopadové studie s.137 místo 0,96 MWh/t. Dřívější výpočet je P90. |
| energetické využití odpadu | progresivni | 44,2 | 44,2 | 40,1 až 45,5 | 35,0 až 50,0 | B na C | 0,0 | Meze jsou prostý úsudek, konzervativní P10 je případ, že se zařízení nepostaví. |
| energetické využití odpadu | konzervativni | 44,2 | 44,2 | 40,1 až 45,5 | 0,0 až 50,0 | B na C | 0,0 | Meze jsou prostý úsudek, konzervativní P10 je případ, že se zařízení nepostaví. |
| Třinecké železárny | progresivni | 1 230,8 | 1 549,2 | 1 000,0 až 1 939,2 | 769,2 až 1 939,2 | D | 318,4 | Čistý nárůst 300 kWh/t místo tiskového 180 kWh/t, Nová huť stejnou technologií počítá 450 kWh/t. P10 je případ bez pece. Úsudek. |
| Třinecké železárny | konzervativni | 1 000,0 | 1 159,2 | 800,0 až 1 500,0 | 769,2 až 1 500,0 | C na D | 159,2 | Čistý nárůst 300 kWh/t místo tiskového 180 kWh/t, Nová huť stejnou technologií počítá 450 kWh/t. P10 je případ bez pece. Úsudek. |
| Nová huť | progresivni | 736,3 | 736,3 | 239,3 až 886,3 | 61,3 až 886,3 | D | 0,0 | P50 beze změny, P10 je případ bez pece, 61,32 GWh. |
| Nová huť | konzervativni | 736,3 | 736,3 | 461,3 až 886,3 | 61,3 až 886,3 | D | 0,0 | P50 beze změny, P10 je případ bez pece, 61,32 GWh. |
| domácnosti bez vytápění | progresivni | 423,6 | 423,6 | 309,9 až 548,0 | 309,9 až 925,0 | D | 0,0 | P50 beze změny, P90 925 GWh: 370 000 domácností × 2,5 MWh. Rozdělení mezi tarifní řádky je nejisté. |
| domácnosti bez vytápění | konzervativni | 423,6 | 423,6 | 309,9 až 548,0 | 309,9 až 925,0 | D | 0,0 | P50 beze změny, P90 925 GWh: 370 000 domácností × 2,5 MWh. Rozdělení mezi tarifní řádky je nejisté. |
| elektrokotle v teplárnách | progresivni | 150,0 | 10,1 | 50,0 až 400,0 | 0,0 až 70,0 | D | −139,9 | Mez 70 MW je náš součet: 18 MW (s.121), 12 MW a nejvýš dva další po 20 MW (s.166, extrémní scénář). Předpokládá, že 18 a 12 MW jsou dva různé kotle. Kotel bere jen přebytek, řádek je výsledek hodinového běhu. |
| elektrokotle v teplárnách | konzervativni | 9,0 | 0,0 | 2,0 až 40,0 | 0,0 až 9,0 | D | −9,0 | Mez 70 MW je náš součet: 18 MW (s.121), 12 MW a nejvýš dva další po 20 MW (s.166, extrémní scénář). Předpokládá, že 18 a 12 MW jsou dva různé kotle. Kotel bere jen přebytek, řádek je výsledek hodinového běhu. |
| nákladní doprava | progresivni | 558,6 | 782,1 | 234,4 až 657,2 | 328,1 až 920,1 | D | 223,5 | Flotila 70:30. |
| vlaky | progresivni | 37,6 | 37,6 | 37,6 až 111,1 | 30,0 až 111,1 | B na C | 0,0 | P10 pod P50, dřívější mez neměla žádný pokles. |
| vlaky | konzervativni | 35,7 | 35,7 | 30,0 až 100,0 | 30,0 až 100,0 | B na D | 0,0 | 95 % je z definice cesty, ne z publikace. |
| MHD | progresivni | 11,9 | 16,6 | 11,9 až 33,9 | 13,3 až 47,4 | D | 4,7 | Flotila 70:30. Křivka bez P10 pod P50, P10 o 20 % níž. |
| MHD | konzervativni | 19,0 | 19,0 | 15,0 až 65,0 | 15,0 až 65,0 | B na D | 0,0 | 80 % je z definice cesty, hodnota pod základem. |
| výroba vodíku | progresivni | 45,8 | 45,8 | 20,0 až 260,4 | 20,0 až 260,4 | B na C | 0,0 | P50 2050 je ze studie, 2030 a 2040 jsou volba modelu. |
| výroba vodíku: osobní auta | progresivni | 0,0 | 0,0 | 0,0 až 0,0 | 0,0 až 0,0 | C na D | 0,0 | Stupeň podle jednotného pravidla: nejslabší vstup hodnoty P50. |
| výroba vodíku: osobní auta | konzervativni | 0,0 | 0,0 | 0,0 až 0,0 | 0,0 až 0,0 | C na D | 0,0 | Stupeň podle jednotného pravidla: nejslabší vstup hodnoty P50. |
| výroba vodíku: nákladní doprava | progresivni | 1 925,0 | 1 174,9 | 884,5 až 2 958,5 | 540,3 až 1 802,1 | D | −750,1 | Flotila 70:30. Komprese 3,1 kWh/kg změřená místo modelových 2,23 kWh/kg, celkem 51,36 kWh/kg. |
| výroba vodíku: MHD | progresivni | 34,6 | 21,1 | 16,1 až 103,1 | 9,8 až 62,8 | D | −13,5 | Flotila 70:30. Komprese 3,1 kWh/kg změřená místo modelových 2,23 kWh/kg, celkem 51,36 kWh/kg. |
| výroba syntetického plynu | progresivni | 0,0 | 0,0 | 0,0 až 0,0 | 0,0 až 0,0 | C na D | 0,0 | Volba modelu proti s.169 studie, nula je znak neznámé hodnoty. |
| výroba syntetického plynu | konzervativni | 0,0 | 0,0 | 0,0 až 0,0 | 0,0 až 0,0 | C na D | 0,0 | Volba modelu proti s.169 studie, nula je znak neznámé hodnoty. |
| vlastní spotřeba zdrojů | progresivni | 491,6 | 460,1 | 368,7 až 614,5 | 345,1 až 575,2 | C | −31,5 | Vzorec z výroby, počítá i SMR, 310 GWh na blok. Dřívější řádek byl jen křivka přes milníky. |
| vlastní spotřeba zdrojů | konzervativni | 227,6 | 218,2 | 170,7 až 284,5 | 163,7 až 272,8 | C | −9,4 | Vzorec z výroby, počítá i SMR, 310 GWh na blok. Dřívější řádek byl jen křivka přes milníky. |
| ostatní energetika (přidaná položka) | progresivni | 1 000,8 | 1 000,8 | 600,0 až 1 050,0 | 600,0 až 1 200,0 | D | 0,0 | P90 1 200 GWh, měřené pololetí 2026 je už nad dřívějším P90. |
| ostatní energetika (přidaná položka) | konzervativni | 1 000,8 | 1 000,8 | 600,0 až 1 050,0 | 600,0 až 1 200,0 | D | 0,0 | P90 1 200 GWh, měřené pololetí 2026 je už nad dřívějším P90. |
| ztráty v sítích | progresivni | 426,4 | 410,4 | 383,2 až 546,4 | 369,4 až 525,3 | C | −16,0 | Stejný vzorec v obou cestách, r = 3,547 %. V konzervativní cestě odpadá násobek 1,7. |
| ztráty v sítích | konzervativni | 446,2 | 267,8 | 336,2 až 530,9 | 241,0 až 342,7 | D na C | −178,4 | Stejný vzorec v obou cestách, r = 3,547 %. V konzervativní cestě odpadá násobek 1,7. |
| ztráty baterií | progresivni | 40,7 | 57,8 | 22,0 až 88,2 | 31,2 až 125,4 | D | 17,1 | Baterie cykluje i ze sítě, nabito minus vybito z hodinového běhu. |
| ztráty baterií | konzervativni | 0,0 | 17,8 | 0,0 až 0,0 | 9,6 až 38,6 | D | 17,8 | Baterie cykluje i ze sítě, nabito minus vybito z hodinového běhu. |
| úspory a účinnost | progresivni | −290,0 | −299,1 | −500,0 až −100,0 | −500,0 až −100,0 | D | −9,1 | Oprava součtu, ostatní průmysl má základ 1 571,4 GWh. |
| úspory a účinnost | konzervativni | −145,0 | −149,6 | −300,0 až −50,0 | −300,0 až −50,0 | D | −4,6 | Oprava součtu, ostatní průmysl má základ 1 571,4 GWh. |

**Pravidlo stupně důkazu je jedno:** řídí se nejslabším vstupem hodnoty P50 pro rok 2050. Meze P10 a P90 jsou téměř všude úsudek a stupeň se k nim nevztahuje.

**Křivky.** Ploché řádky už nemají falešnou S-křivku ze zaokrouhlení, to samo zúžilo pásmo spotřeby v roce 2026. Nové plynové bloky, datacentra a vodík ze studie jsou nula, dokud neběží žádné zařízení. FVE, vítr a tepelná čerpadla mají v roce 2026 obě cesty stejný uzel. Uhlí v teplárnách odchází postupně. Milníky u skokových řádků ukazují hodnotu v tom roce, ne podmíněný stav. Ztráty a vlastní spotřeba jsou vzorce, proto se cesty v roce 2026 liší jen o pár GWh.

**Uzel plynu 2035 zůstává neuvedený.** Tab.30 s.132 dává pro 2035 výkon 683 MW, ne energii. Uzel v GWh při 3 521 h a 90 % by byl 2 164 GWh a milník 2040 je 1 372 GWh, takže by energie mezi 2035 a 2040 klesala bez důvodu. Výkon už na energii nezávisí, zimní pohled proto rok 2035 počítá správně.

**Elektrolyzér.** Platí jedna definice: výkon = řádky vodíku flotily × (1 + míra ztrát sítě) × 1 000 / plné hodiny. Plné hodiny jsou z hodinového výpočtu (6 294 h, nejmenší výkon, při kterém výchozí nastavení vyveze pod 1 % přebytku). Výsledek je 197 MW. Řádek 45,8 GWh ze studie je vodík mimo flotilu a běží jako rovnoměrná zátěž mimo tento výkon.

## 4. Baterie a vodík, dnešní mix, 1 SMR

### Pravidlo

Přebytek má přednost. Každou půlnoc se z křivky zbytkového zatížení na další den a z náboje najde nejnižší rovná hladina, kterou baterie udrží v pořadí hodin. Nad hladinou vybíjí, pod hladinou minus 100 MW nabíjí ze sítě a nechá místo na přebytek, který ten den ještě přijde. Nabíjení končí pod hladinou, takže při přesné předpovědi denní špička nestoupne, kontrola to hlídá v každém běhu. Rozdíl 100 MW je úsudek: menší rozdíl přidává cykly a ztráty a špičku téměř nemění. Pravidlo jen z přebytku zůstává jako varianta.

**Co je známo dopředu.** Baterie zná křivku dalšího dne přesně. Rozvrh plynu, elektrolýzy ze sítě a nádrže zná celý rok. Se včerejší křivkou místo předpovědi baterie ve výchozím nastavení zvedne denní špičku 7 až 13 dnů v roce, nejvýš o 278 MW. Když plyn dostane práh z předchozího povětrnostního roku místo znalosti celého roku, stoupne ve výchozím nastavení zimní špička dovozu v nejhorším roce z 837 na 1 004 MW a po vyčerpání paliva roční špička v nejhorším roce na 1 205 MW; v roce po chladnějším roce zůstane až 73 GWh plynu nevyužito.

### Velikost bez cíle

E_den = součet kladných odchylek od denního průměru / √0,88, výkon = největší hodinová odchylka. Spotřeba bez elektrolýzy minus neřízené zdroje včetně SMR, 1 825 dnů.

| Statistika | E_den GWh | Výkon MW |
|---|---|---|
| Medián | 2,71 | 588 |
| P90 | 4,49 | 805 |
| P95 | 4,89 | 855 |
| Maximum | 6,27 | 1 140 |

Pravidlo pro velikost je medián a 4 hodiny: **2,7 GWh a 675 MW**. Medián denního přebytku je 0,32 GWh a 34 % dnů přebytek nemá, přebytek sám by takovou baterii nenaplnil.


Podle velikosti, průměr 5 let, rovnoměrná elektrolýza bez nádrže. Noc je 18:00 až 06:00 v pevném čase SEČ, úspora je čistá po nabíjení ve stejné noci. Večer je 17:00 až 22:00. Kryté noci jsou počet za rok plně / aspoň z poloviny. Pokles špičky prosince až února je medián / nejhorší povětrnostní rok.

| Pravidlo | GWh | Cykly | Nabito z přebytku GWh | Nabito ze sítě GWh | Noc úspora GWh | Večer úspora GWh | Kryté noci | Pokles špičky před plynem MW | Pokles špičky po plynu MW | Po plynu po letech | Dovoz GWh | Vývoz GWh | Ztráty GWh | Kotle GWh |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vyrovnání dne | 0,0 | 0 | 0 | 0 | 0 | 0 | 0,0 / 0,0 | 0 / 0 | 0 / 0 | 2015: 0, 2016: 0, 2017: 0, 2018: 0, 2019: 0 | 4 771 | 126,3 | 0,0 | 49 |
| Vyrovnání dne | 0,5 | 261 | 46 | 102 | 24 | 97 | 0,0 / 0,0 | 118 / 87 | 30 / 24 | 2015: 30, 2016: 31, 2017: 24, 2018: 35, 2019: 28 | 4 743 | 91,2 | 17,8 | 38 |
| Vyrovnání dne | 1,0 | 275 | 98 | 215 | 107 | 200 | 0,0 / 0,0 | 148 / 88 | 62 / 52 | 2015: 67, 2016: 62, 2017: 52, 2018: 72, 2019: 59 | 4 711 | 53,1 | 37,5 | 25 |
| Vyrovnání dne | 1,5 | 254 | 126 | 307 | 192 | 265 | 0,0 / 0,2 | 148 / 87 | 80 / 67 | 2015: 95, 2016: 80, 2017: 67, 2018: 90, 2019: 77 | 4 697 | 34,8 | 52,0 | 15 |
| Vyrovnání dne | 2,0 | 228 | 143 | 376 | 259 | 305 | 0,0 / 0,2 | 148 / 87 | 91 / 75 | 2015: 109, 2016: 91, 2017: 75, 2018: 104, 2019: 90 | 4 690 | 23,7 | 62,3 | 9 |
| Vyrovnání dne | 2,7 | 193 | 160 | 430 | 308 | 332 | 0,0 / 0,4 | 148 / 87 | 100 / 78 | 2015: 119, 2016: 97, 2017: 78, 2018: 111, 2019: 100 | 4 682 | 11,8 | 70,9 | 4 |
| Vyrovnání dne | 3,0 | 178 | 165 | 443 | 318 | 337 | 0,0 / 1,2 | 148 / 87 | 102 / 78 | 2015: 121, 2016: 99, 2017: 78, 2018: 113, 2019: 102 | 4 679 | 8,3 | 73,0 | 3 |
| Vyrovnání dne | 4,0 | 140 | 174 | 465 | 333 | 345 | 0,0 / 2,2 | 148 / 87 | 101 / 75 | 2015: 121, 2016: 97, 2017: 75, 2018: 111, 2019: 101 | 4 674 | 1,7 | 76,6 | 1 |
| Vyrovnání dne | 5,0 | 114 | 175 | 473 | 337 | 346 | 0,0 / 2,4 | 148 / 87 | 100 / 74 | 2015: 119, 2016: 95, 2017: 74, 2018: 110, 2019: 100 | 4 674 | 0,7 | 77,7 | 0 |
| Vyrovnání dne | 8,0 | 72 | 176 | 477 | 338 | 347 | 0,0 / 2,2 | 148 / 87 | 98 / 72 | 2015: 117, 2016: 93, 2017: 72, 2018: 108, 2019: 98 | 4 674 | 0,0 | 78,3 | 0 |
| Vyrovnání dne | 12,0 | 48 | 176 | 477 | 338 | 347 | 0,0 / 2,4 | 148 / 87 | 98 / 72 | 2015: 117, 2016: 94, 2017: 72, 2018: 108, 2019: 98 | 4 674 | 0,0 | 78,3 | 0 |
| Jen přebytek | 0,0 | 0 | 0 | 0 | 0 | 0 | 0,0 / 0,0 | 0 / 0 | 0 / 0 | 2015: 0, 2016: 0, 2017: 0, 2018: 0, 2019: 0 | 4 771 | 126,3 | 0,0 | 49 |
| Jen přebytek | 0,5 | 116 | 66 | 0 | 9 | 19 | 0,0 / 0,0 | 0 / 0 | 0 / 0 | 2015: 0, 2016: 1, 2017: 0, 2018: 1, 2019: 0 | 4 713 | 75,5 | 7,9 | 34 |
| Jen přebytek | 1,0 | 99 | 112 | 0 | 19 | 37 | 0,0 / 0,0 | 0 / 0 | 0 / 0 | 2015: 0, 2016: 1, 2017: 0, 2018: 0, 2019: 0 | 4 672 | 41,5 | 13,5 | 22 |
| Jen přebytek | 1,5 | 83 | 142 | 0 | 28 | 51 | 0,0 / 0,0 | 0 / 0 | 0 / 0 | 2015: 0, 2016: 1, 2017: 0, 2018: 0, 2019: 0 | 4 646 | 21,7 | 17,1 | 12 |
| Jen přebytek | 2,0 | 70 | 159 | 0 | 33 | 62 | 0,0 / 0,0 | 0 / 0 | 0 / 0 | 2015: 0, 2016: 0, 2017: 0, 2018: 0, 2019: 0 | 4 631 | 10,9 | 19,1 | 6 |
| Jen přebytek | 2,7 | 55 | 170 | 0 | 38 | 69 | 0,0 / 0,6 | 0 / 0 | 0 / 0 | 2015: 0, 2016: 0, 2017: 0, 2018: 0, 2019: 0 | 4 621 | 3,9 | 20,4 | 2 |
| Jen přebytek | 3,0 | 51 | 172 | 0 | 39 | 71 | 0,0 / 0,8 | 0 / 0 | 0 / 0 | 2015: 0, 2016: 0, 2017: 0, 2018: 0, 2019: 0 | 4 620 | 2,4 | 20,7 | 1 |
| Jen přebytek | 4,0 | 39 | 175 | 0 | 41 | 72 | 0,0 / 2,8 | 0 / 0 | 0 / 0 | 2015: 0, 2016: 0, 2017: 0, 2018: 0, 2019: 0 | 4 617 | 0,4 | 21,0 | 0 |
| Jen přebytek | 5,0 | 31 | 176 | 0 | 42 | 72 | 0,0 / 2,8 | 0 / 0 | 0 / 0 | 2015: 0, 2016: 0, 2017: 0, 2018: 0, 2019: 0 | 4 617 | 0,1 | 21,1 | 0 |
| Jen přebytek | 8,0 | 19 | 176 | 0 | 42 | 72 | 0,0 / 2,8 | 0 / 0 | 0 / 0 | 2015: 0, 2016: 0, 2017: 0, 2018: 0, 2019: 0 | 4 617 | 0,0 | 21,1 | 0 |
| Jen přebytek | 12,0 | 13 | 176 | 0 | 42 | 72 | 0,0 / 2,8 | 0 / 0 | 0 / 0 | 2015: 0, 2016: 0, 2017: 0, 2018: 0, 2019: 0 | 4 617 | 0,0 | 21,1 | 0 |

**Co je ta velikost poctivě, při rovnoměrné elektrolýze bez nádrže.** 2,7 GWh je jeden den výkyvu, ne záloha a ne zdroj energie. Proti pravidlu jen z přebytku vyrovnávání dne zvedá ztráty z 20,4 na 70,9 GWh a roční dovoz z 4 621 na 4 682 GWh. Za to dává pokles zimní špičky 148 / 87 MW před plynem a 100 / 78 MW po plynu, pravidlo jen z přebytku 0 / 0 MW. Večer ušetří 332 GWh proti 69 GWh. Bez baterie je dovoz 4 771 GWh a kotle berou 49 GWh proti 4 GWh.

**Ve výchozím nastavení s malou nádrží 20 t**, kdy elektrolyzér v zimě běží a nádrž ho přesouvá jen o hodiny, je zimní špička po plynu 851 MW s baterií a 903 MW bez ní, pokles medián 51 MW, nejhorší rok 39 MW. Před plynem je pokles 7 MW v mediánu a 0 MW v nejhorším roce. Baterie 5 GWh dá po plynu 47 / 34 MW, baterie 12 GWh 45 / 33 MW, baterie 2,7 GWh s plánem na dva dny 77 / 59 MW, vše s přesnou předpovědí.

**Baterie na tři dny.** Definice cesty uvádí 3 dny akumulace. Tři dny průměrného zatížení roku 2050, 1 430 MW, je 103 GWh. Pravidlo 4 h by dalo 25 738 MW, proto výkon 1 362 MW, největší hodinové zbytkové zatížení bez baterie. Pravidlo je stejné a plánuje jen den dopředu. Roční dovoz 4 658 GWh, vývoz 0,0 GWh, ztráty 62,6 GWh, zimní špička dovozu 857 MW, bez dovozu 7,3 % hodin. Výchozí nastavení: 4 667 GWh, 3,0 GWh, 57,8 GWh, 851 MW a 7,2 % hodin.

Přebytek před baterií, kotli a elektrolyzérem je 311 GWh. Z něj jde 172 GWh do vodíku, 10 GWh do kotlů, 126 GWh do baterie a 3,0 GWh je vývoz. Baterie bere ze sítě 356 GWh, ztráty jsou 57,8 GWh. Přebytek do vodíku tu zahrnuje i výrobu v přebytkových hodinách, kterou rozvrh nádrže vede jako výrobu ze sítě. Večer klesne dovoz o 184 GWh, roční dovoz o 101 GWh, zbytek se přesune do jiných hodin. Pravidlo jen z přebytku při stejné nádrži: dovoz 4 644 GWh, ztráty 34,3 GWh, pokles špičky po plynu 1 / 0 MW.

**Citlivost na předpověď.** Když hladinu místo předpovědi určí včerejší křivka, tedy jen známá informace, pokles špičky po plynu je ve výchozím nastavení 33 / 27 MW a při rovnoměrné elektrolýze bez nádrže 60 / 14 MW, ztráty 61,6 GWh. V roce se studeným náhlým dnem nepředvídaná špička zůstane. Chyba skutečné předpovědi leží mezi oběma případy.

**Konzervativní cesta** má baterii podle své definice, zálohu 10 % ze 3 dnů průměrného zatížení roku 2050 943 MW: 6,8 GWh a 1 226 MW. Čtyřhodinové pravidlo dává 1 700 MW, největší hodinové zbytkové zatížení bez baterie je 1 226 MW. Se stejným pravidlem vyrovnání dne: dovoz z 4 288 na 4 306 GWh, ztráty 17,8 GWh, 19 plných cyklů za rok, pokles zimní špičky 0 MW v mediánu. Pravidlo denního výkyvu by tam dalo 0,9 GWh, pokles zimní špičky 0 MW v mediánu a ztráty asi 17 GWh, v nejhorším roce pokles žádný.

### Elektrolyzér

Velikost určuje pravidlo přímo ve výchozím nastavení: nejmenší elektrolyzér v celých MW, který s malou nádrží vyveze pod 1 % přebytku v průměru 5 let. Tabulka je z téhož výpočtu, větší výkony jsou pro srovnání.

| Elektrolyzér MW | Plné hodiny | Vývoz GWh | Vývoz z přebytku | Dovoz GWh | Přebytek do H2 GWh | Podíl přebytku na vodíku | Síť do H2 GWh | Ztráty baterie GWh |
|---|---|---|---|---|---|---|---|---|
| 148 | 8 378 | 9,6 | 3,1 % | 4 684 | 138 | 11,2 % | 1 102 | 68,3 |
| 197 | 6 294 | 3,0 | 1,0 % | 4 667 | 172 | 13,9 % | 1 068 | 57,8 |
| 296 | 4 189 | 2,7 | 0,9 % | 4 664 | 222 | 17,9 % | 1 018 | 55,8 |
| 492 | 2 520 | 3,4 | 1,1 % | 4 676 | 211 | 17,1 % | 1 029 | 67,2 |

Potřeba flotily je 1 240 GWh a přebytek 311 GWh. Výchozí výkon 197 MW znamená 6 294 hodin na plný výkon za rok a vývoz 3,0 GWh, 1,0 % přebytku.

### Nádrž při pevné kapacitě

Baterie 2,7 GWh a 675 MW, elektrolyzér 197 MW, rovnoměrný odběr flotily. Výrobu rozvrhuje hodinový lineární program po jednotlivých letech s předvídáním: nejdřív co nejméně vývozu, potom co nejméně výroby ze sítě v prosinci až únoru, potom nižší zimní špička. Baterie pak vyrovnává to, co zbude.

| Nádrž | Výroba H2 v prosinci až únoru GWh | Bilance prosinec až únor GWh | Bilance říjen až březen GWh | Zimní špička dovozu MW, průměr / nejhorší rok | Vývoz GWh | Dovoz GWh |
|---|---|---|---|---|---|---|
| 0 t | 306 | −1 368 | −2 484 | 862 / 917 | 10,4 | 4 687 |
| 5 t | 305 | −1 365 | −2 479 | 858 / 914 | 7,6 | 4 678 |
| 10 t | 305 | −1 363 | −2 476 | 855 / 910 | 5,3 | 4 670 |
| 20 t | 305 | −1 362 | −2 474 | 851 / 907 | 3,0 | 4 667 |
| 50 t | 303 | −1 362 | −2 476 | 838 / 894 | 3,1 | 4 667 |
| 100 t | 300 | −1 363 | −2 479 | 827 / 884 | 3,6 | 4 668 |

Výchozí je malá nádrž 20 t. Výhrady: 20 t je asi 8 h spotřeby flotily, rozvrh zná celý rok a denní tankovací profil část nádrže spotřebuje.

## 5. Dvě zimní špičky a jejich smíření

**Stránka, zimní špička:** návrhový případ podle metody studie. Řádek × koeficient, kalibrováno na rok 2023. Vítr a slunce 0, SMR 0,95, plyn výkon × 0,9 bez ohledu na palivo, elektrolýza vypnutá.

**Hodinový model, špička prosince až února:** největší hodinové zatížení, případně dovoz, ve skutečném průběhu daného povětrnostního roku se skutečným větrem a sluncem a s plynem jen do ročního rozpočtu.

**Výsledek.** Zatížení v roce 2050: stránka 1 632 MW, hodinově medián 1 975 MW (rozsah 1 814 až 1 997 MW) v progresivní cestě, 1 226 a 1 425 MW v konzervativní. Tepelné čerpadlo má nyní 3,5 až 5,5 kW na odběrné místo v hodině svého maxima místo dřívějších 8,2 kW: běžná spotřeba 2,5 MWh z 8,9 MWh jde tvarem spotřebičů a v tuhých mrazech čerpadlo běží rovnoměrně. Terénní údaj 1,7 kW je z mírnější Británie a na −18 °C se nepřenáší. Koeficient čerpadel a přímotopů je nyní z hodinového modelu, tyto řádky se tedy shodují.

| Řádek, MW ve špičce | Stránka, progresivní | Hodinově, medián | Stránka, konzervativní | Hodinově, medián |
|---|---|---|---|---|
| vytápění tepelnými čerpadly | 639 | 644 | 295 | 291 |
| přímotopy | 0 | 0 | 243 | 245 |
| osobní auta | 132 | 211 | 26 | 42 |
| nákladní doprava | 67 | 131 | 23 | 37 |
| domácnosti bez vytápění | 60 | 82 | 60 | 86 |
| služby a veřejný sektor | 105 | 126 | 105 | 139 |
| Třinecké železárny | 139 | 177 | 104 | 132 |
| Nová huť | 66 | 84 | 66 | 84 |
| ostatní průmysl a chemie | 187 | 227 | 147 | 179 |
| ostatní energetika (přidaná položka) | 86 | 114 | 86 | 114 |
| vlastní spotřeba zdrojů | 47 | 53 | 22 | 25 |
| datacentra | 55 | 80 | 5 | 8 |

**Proč se smějí lišit.** Stránka kalibruje všechny řádky na metodu studie: zatížení 2025 je tam 1 169 MW. Stejné hodinové tvary dají na řádcích roku 2025 1 309 MW, rozsah 1 236 až 1 419 MW. Rozdíl je tedy z větší části ve stejném poměru už dnes a jde hlavně na ploché průmyslové řádky a na večerní nabíjení aut. Hodinové tvary jsou celostátní a poměr k měřené špičce kraje nelze ověřit, protože roční maximum zatížení MSK se nesleduje. Výsledek hodinového dovozu tedy není dolní mez, stránka není horní mez a obě čísla se uvádějí vedle sebe.

**Plyn.** Progresivní bloky mají 433 MW v hodinovém modelu i na stránce, palivo jen 115,2 GWh, tedy 266 h plného výkonu. Dříve z energie vycházelo 115 MW.

**Bilance s baterií na stránce.** Nikdy se nepřičítá celý výkon. Zimní bilance progresivní cesty 2050 je −672 MW; s baterií −665 MW při změřeném poklesu špičky 7 MW v mediánu a −672 MW při 0 MW v nejhorším povětrnostním roce. Čísla jsou před plynem, protože stránka počítá plyn plným výkonem. Konzervativní zimní bilance je −412 MW.

**Chlazení.** Stejná intenzita na stupeň ve všech letech a strop řádek / 500 h, tedy 384 MW v progresivní cestě. Dříve se každý rok přeškáloval na stejné GWh a chladné léto 2016 dalo 939 MW. Průměr 5 let sedí na řádek, jednotlivé roky se liší. Strop 500 h je úsudek.

**Odstávka SMR.** Předpoklad: plánovaná odstávka v jarním období s nejnižší zbytkovou špičkou, od poloviny dubna. Sken začátků přes 5 let dal nejnižší špičku v rozmezí začátků od poloviny dubna do května. Druhý blok od poloviny září. Roční špička dovozu už tak neleží v odstávce.

## 6. Soběstačnost: výchozí mix a podmínky

### Výchozí mix, řádky P50, průměr 5 let

| Cesta | SMR | Vodík | Výroba GWh | Spotřeba GWh | Roční bilance GWh | Výroba / spotřeba | Říjen až březen GWh | Prosinec až únor GWh | Hodiny bez dovozu | Největší dovoz v zimě MW, nejhorší rok | Největší dovoz za rok MW | Dovoz GWh | Přebytek bez využití GWh |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Progresivní | 0 | flotila na bateriích | 3 920 | 11 331 | −7 410 | 34,6 % | −3 996 | −2 090 | 2,8 % | 1 174 | 1 174 | 7 424 | 1 |
| Progresivní | 0 | 70:30, rovnoměrná výroba | 3 920 | 12 216 | −8 296 | 32,1 % | −4 436 | −2 307 | 1,4 % | 1 298 | 1 298 | 8 307 | 0 |
| Progresivní | 1 | flotila na bateriích | 7 862 | 11 641 | −3 779 | 67,5 % | −2 043 | −1 151 | 12,3 % | 822 | 822 | 3 823 | 31 |
| Progresivní | 1 | 70:30, rovnoměrná výroba | 7 862 | 12 526 | −4 664 | 62,8 % | −2 481 | −1 367 | 8,8 % | 917 | 917 | 4 682 | 12 |
| Progresivní | 2 | flotila na bateriích | 11 804 | 11 951 | −147 | 98,8 % | −298 | −194 | 44,9 % | 424 | 424 | 923 | 643 |
| Progresivní | 2 | 70:30, rovnoměrná výroba | 11 804 | 12 836 | −1 032 | 92,0 % | −713 | −402 | 32,5 % | 519 | 519 | 1 433 | 323 |
| Konzervativní | 0 | bez flotily na vodík | 3 956 | 8 262 | −4 306 | 47,9 % | −2 147 | −1 062 | 0,0 % | 497 | 497 | 4 306 | 0 |
| Konzervativní | 1 | bez flotily na vodík | 7 898 | 8 572 | −674 | 92,1 % | −334 | −166 | 0,4 % | 82 | 205 | 674 | 0 |
| Konzervativní | 2 | bez flotily na vodík | 11 840 | 8 882 | 2 958 | 133,3 % | 350 | 131 | 100,0 % | 0 | 0 | 0 | 960 |

Vodík vyrobený mimo kraj, 70 % flotily zůstává na bateriích: výroba 7 862 GWh, spotřeba 11 286 GWh, bilance −3 424 GWh.

Roční bilance v tabulce počítá s celým rozpočtem plynu. Hodinový model pouští plyn jen při schodku. Bilance sezón počítá i přebytek, který v dané hodině nikdo nevzal. U jednoho SMR je v rovnováze odečtena jeho vlastní spotřeba, blok dá čistě 3 632 GWh, ne 3 942 GWh.

### Co by muselo platit

Přidaný výkon nad řádky tabulky, řádky P50, čistý po vlastní spotřebě. U úrovně 2 je výpočet hodinový, průměr 5 let, požadavek je bilance sezóny aspoň 0. Vítr na mezi znamená doplnit vítr do 2 014 MW a zbytek pokrýt jinak.

| Cesta | SMR výchozí | Vodík | Úroveň | Bilance teď GWh | Jen vítr, přidat MW | Jen FVE, přidat MWp | Jen SMR, přidat | Vítr na mezi 2 014 MW | Půl na půl |
|---|---|---|---|---|---|---|---|---|---|
| Progresivní | 1 | flotila na bateriích | rok | −3 779 | 1 557 | 4 059 | 1,04 | 1 391 MW větru, potom 433 MW FVE nebo 0,11 SMR | 778 MW + 2 029 MWp |
| Progresivní | 1 | flotila na bateriích | říjen až březen | −2 043 | 1 399 | 7 181 | 2 celé | 1 391 MW větru, potom 1 SMR |  |
| Progresivní | 1 | flotila na bateriích | prosinec až únor | −1 151 | 1 475 | 10 618 | 2 celé | 1 391 MW větru, potom 1 SMR |  |
| Progresivní | 1 | 70:30, rovnoměrná výroba | rok | −4 664 | 1 921 | 5 010 | 1,28 | 1 391 MW větru, potom 1 383 MW FVE nebo 0,35 SMR | 961 MW + 2 505 MWp |
| Progresivní | 1 | 70:30, rovnoměrná výroba | říjen až březen | −2 481 | 1 689 | 8 691 | 2 celé | 1 391 MW větru, potom 1 SMR |  |
| Progresivní | 1 | 70:30, rovnoměrná výroba | prosinec až únor | −1 367 | 1 745 | 12 586 | 2 celé | 1 391 MW větru, potom 1 SMR |  |
| Progresivní | 0 | 70:30, rovnoměrná výroba | rok | −8 296 | 3 418 | 8 911 | 2,28 | 1 391 MW větru, potom 5 285 MW FVE nebo 1,35 SMR | 1 709 MW + 4 455 MWp |
| Progresivní | 0 | 70:30, rovnoměrná výroba | říjen až březen | −4 436 | 2 997 | 15 433 | 3 celé | 1 391 MW větru, potom 2 SMR |  |
| Progresivní | 0 | 70:30, rovnoměrná výroba | prosinec až únor | −2 307 | 2 956 | 21 236 | 3 celé | 1 391 MW větru, potom 2 SMR |  |
| Progresivní | 2 | 70:30, rovnoměrná výroba | rok | −1 032 | 425 | 1 108 | 0,28 | 1 391 MW větru, potom 0 MW FVE nebo 0,00 SMR | 213 MW + 554 MWp |
| Progresivní | 2 | 70:30, rovnoměrná výroba | říjen až březen | −713 | 507 | 2 555 | 1 celé | 1 391 MW větru, potom 0 SMR |  |
| Progresivní | 2 | 70:30, rovnoměrná výroba | prosinec až únor | −402 | 535 | 3 777 | 1 celé | 1 391 MW větru, potom 0 SMR |  |
| Konzervativní | 0 | bez flotily na vodík | rok | −4 306 | 1 774 | 4 625 | 1,19 | 1 918 MW větru, potom 0 MW FVE nebo 0,00 SMR | 887 MW + 2 313 MWp |
| Konzervativní | 0 | bez flotily na vodík | říjen až březen | −2 147 | 1 668 | 6 373 | 2 celé | 1 918 MW větru, potom 0 SMR |  |
| Konzervativní | 0 | bez flotily na vodík | prosinec až únor | −1 062 | 1 625 | 7 648 | 2 celé | 1 918 MW větru, potom 0 SMR |  |

**Konzervativní cesta a vítr.** Roční schodek 4 306 GWh zavře 1 774 MW větru, celkem 1 870 MW, uvnitř meze 2 014 MW. Tempo 73,1 MW za rok je 8,0krát největší přírůstek kraje. Hodinově: bilance říjen až březen 144 GWh, prosinec až únor 105 GWh, bez dovozu 23,4 % hodin, největší dovoz 301 MW, přebytek bez využití 457 GWh.

Hodinově s přidanými zdroji, progresivní cesta, flotila 70:30, rovnoměrná výroba:

| Mix | Roční bilance GWh | Říjen až březen GWh | Prosinec až únor GWh | Hodiny bez dovozu | Největší dovoz MW, nejhorší rok | Dovoz GWh | Přebytek bez využití GWh |
|---|---|---|---|---|---|---|---|
| 1 SMR, vítr na mez 2 014 MW | −1 418 | −438 | −277 | 34,08 % | 808 | 2 319 | 901 |
| 3 SMR | 2 230 | 1 136 | 513 | 80,87 % | 53 | 35 | 2 265 |
| 5 SMR | 9 181 | 4 211 | 2 422 | 100,00 % | 0 | 0 | 9 181 |
| 3 SMR, vítr na mez 2 014 MW | 5 410 | 3 172 | 1 600 | 100,00 % | 0 | 0 | 5 410 |
| 3 SMR, vítr na mez, 3 GWp FVE | 8 171 | 4 040 | 1 930 | 100,00 % | 0 | 0 | 8 171 |

Vítr na mezi 2 014 MW, 1 SMR, kolik FVE navíc vyrovná bilanci:

| Vodík | Cíl | FVE navíc MWp | Roční bilance GWh | Říjen až březen GWh | Prosinec až únor GWh | Hodiny bez dovozu | Největší dovoz MW, nejhorší rok | Dovoz GWh | Přebytek bez využití GWh |
|---|---|---|---|---|---|---|---|---|---|
| 70:30, malá nádrž | říjen až březen | 1 586 | −58 | 0 | −108 | 39,3 % | 760 | 1 735 | 1 677 |
| 70:30, malá nádrž | prosinec až únor | 2 561 | 829 | 282 | 0 | 41,7 % | 761 | 1 599 | 2 428 |
| 70:30, malá nádrž | rok | 1 650 | 0 | 18 | −101 | 39,5 % | 760 | 1 724 | 1 724 |
| 70:30, rovnoměrná výroba | říjen až březen | 1 537 | −63 | 0 | −108 | 41,5 % | 774 | 1 846 | 1 782 |
| 70:30, rovnoměrná výroba | prosinec až únor | 2 527 | 835 | 284 | 0 | 43,8 % | 746 | 1 722 | 2 556 |
| 70:30, rovnoměrná výroba | rok | 1 608 | 0 | 20 | −100 | 41,7 % | 772 | 1 835 | 1 835 |
| flotila na bateriích | říjen až březen | 44 | −524 | 0 | −61 | 40,9 % | 711 | 1 714 | 1 190 |
| flotila na bateriích | prosinec až únor | 595 | −44 | 157 | 0 | 43,9 % | 700 | 1 537 | 1 493 |
| flotila na bateriích | rok | 645 | 0 | 172 | 6 | 44,1 % | 699 | 1 526 | 1 526 |

### Potenciál a tempo výstavby

| Co | Hodnota | Zdroj | Stupeň |
|---|---|---|---|
| Potenciál větru v kraji | až 2 014 MW | Dopadová studie s.135, ze samostatné simulační studie | B |
| Potenciál FVE v kraji | až 165 GWp, skutečnou mezí je podle studie síť | Dopadová studie s.135-136 | B, jako mez nezávazné |
| Vítr v kraji 2040, modelováno | 330 MW a 863 GWh konzervativně, 961 MW a 2 638 GWh optimisticky | Hanslian, ÚFA AV ČR 2020, Tab. 12 | B |
| Počet SMR v kraji | jeden blok v roce 2045, 350 MW; řádek počítá 500 MW z našeho rozhodnutí. Pro druhý a další blok v kraji zdroj není | Dopadová studie s.126 | C, druhý a další bez zdroje |
| Historické maximum FVE v kraji | +83,3 MW v roce 2023, potom +59,9 a +61,7 MW | ERÚ Roční zpráva 2025, 4.6.8, výkon ke konci roku | A |
| Historické maximum větru v kraji | +9,1 MW v roce 2024, potom +4,3 MW | ERÚ Roční zpráva 2025, 4.6.8 | A |
| Referenční třída, vítr | vrchol 0,8 % dodávky za rok, mezikvartil 0,6 až 1,1 % | Cherp et al. 2021, Nature Energy 6, 742-754, jen výtah, národní hodnoty | B, pro kraj orientačně |
| Referenční třída, FVE | vrchol 0,6 % dodávky za rok, mezikvartil 0,4 až 0,9 % | tamtéž | B, pro kraj orientačně |

Potřebné průměrné roční tempo 2026 až 2050. Procento je přírůstek výroby za rok jako podíl spotřeby progresivní cesty 2050. Je to průměr, skutečný vrchol křivky by byl vyšší.

| Případ | Vítr 2050 | Vítr za rok | proti maximu kraje | % spotřeby za rok | FVE 2050 | FVE za rok | proti maximu kraje | % spotřeby za rok |
|---|---|---|---|---|---|---|---|---|
| Tabulka, progresivní | 623 MW | 23,3 MW | 2,6 × | 0,46 % | 1 678 MWp | 54,8 MWp | 0,7 × | 0,42 % |
| Půl na půl pro úroveň 1 | 1 584 MW | 61,7 MW | 6,8 × | 1,22 % | 4 183 MWp | 155,0 MWp | 1,9 × | 1,18 % |
| Vítr na mezi a zbytek FVE | 2 014 MW | 78,9 MW | 8,7 × | 1,56 % | 3 329 MWp | 120,8 MWp | 1,5 × | 0,92 % |
| Jen FVE | 623 MW | 23,3 MW | 2,6 × | 0,46 % | 6 688 MWp | 255,2 MWp | 3,1 × | 1,93 % |

## 7. Monte Carlo

Běhy losují řádky od P10 do P90 se společnými faktory, obrácenými znaménky a jedním rokem pro položky stejné události. Rok událostí závislých na povolování jde s faktorem povolování. Vlastní spotřeba a ztráty se v každém běhu počítají z losovaných řádků. Roční úroveň má 60 000 běhů, hodinové úrovně 2 000 běhů.

**SMR.** Dřív se bez SMR ocitlo 26 % běhů, protože P90 roku spuštění byl úsudkem 2055. Takový podíl říká něco o jednom odhadnutém roce, ne o projektu. Teď je SMR samostatný případ: progresivní cesta SMR podle své definice má, los mění jen výkon a rok do 2050, a případ bez SMR se uvádí zvlášť. Pravděpodobnost, že SMR nebude, tento výpočet nepřisuzuje.

| Případ | Úroveň 1: rok | Úroveň 2: říjen až březen | Úroveň 2: prosinec až únor | Úroveň 3: žádná hodina s dovozem | Roční bilance P10 / P50 / P90 GWh | Hodiny bez dovozu, medián (P10 až P90) | Největší dovoz MW, medián (P10 až P90) |
|---|---|---|---|---|---|---|---|
| Progresivní, 1 SMR, flotila 70:30, rovnoměrná výroba | pod 10 % | pod 10 % | pod 10 % | pod 1 % | −7 263 / −4 082 / −525 | 12,3 % (2 % až 36 %) | 845 (471 až 1 267) |
| Progresivní, 1 SMR, flotila na bateriích | pod 25 % | pod 25 % | pod 10 % | pod 1 % | −5 965 / −3 176 / 63 | 16,0 % (5 % až 41 %) | 757 (403 až 1 099) |
| Progresivní, bez SMR, flotila 70:30, rovnoměrná výroba | pod 1 % | pod 1 % | pod 1 % | pod 1 % | −10 758 / −7 586 / −4 019 | 3,3 % (0 % až 16 %) | 1 224 (771 až 1 688) |
| Progresivní, bez SMR, flotila na bateriích | pod 1 % | pod 1 % | pod 1 % | pod 1 % | −9 431 / −6 666 / −3 436 | 5,4 % (0 % až 18 %) | 1 117 (717 až 1 531) |
| Progresivní, 2 SMR, flotila 70:30, rovnoměrná výroba | 25 až 50 % | 25 až 50 % | 25 až 50 % | pod 10 % | −3 810 / −605 / 3 006 | 36,7 % (12 % až 98 %) | 489 (83 až 853) |
| Progresivní, 2 SMR, flotila na bateriích | 50 až 75 % | 25 až 50 % | 25 až 50 % | pod 10 % | −2 489 / 320 / 3 595 | 46,7 % (20 % až 100 %) | 382 (38 až 724) |
| Konzervativní, bez SMR | pod 1 % | pod 1 % | pod 1 % | pod 1 % | −6 576 / −4 331 / −2 084 | 0,0 % (0 % až 0 %) | 550 (291 až 823) |
| Konzervativní, 1 SMR navíc proti cestě | 25 až 50 % | 25 až 50 % | 25 až 50 % | pod 25 % | −3 085 / −822 / 1 424 | 1,0 % (0 % až 100 %) | 220 (0 až 485) |
| Konzervativní, 2 SMR navíc proti cestě | nad 90 % | 75 až 90 % | nad 90 % | 75 až 90 % | 365 / 2 664 / 4 967 | 100,0 % (56 % až 100 %) | 0 (0 až 102) |

**Citlivost podílu na neověřených volbách**, úroveň 1, podíl běhů:

| Varianta | Progresivní, 1 SMR, 70:30 | Progresivní, 1 SMR, na bateriích | Progresivní, bez SMR | Progresivní, 2 SMR | Konzervativní | Konzervativní, 1 SMR |
|---|---|---|---|---|---|---|
| korelace 0,6, základ | 7,3 % | 10,6 % | 0,3 % | 41,3 % | 0,6 % | 32,0 % |
| korelace 0 | 1,4 % | 4,0 % | 0,0 % | 37,5 % | 0,0 % | 26,2 % |
| korelace 0,3 | 4,1 % | 7,2 % | 0,1 % | 39,9 % | 0,2 % | 29,2 % |
| korelace 0,9 | 10,1 % | 13,2 % | 0,8 % | 41,7 % | 1,1 % | 33,9 % |
| bez losů mimo P10 až P90 | 3,5 % | 6,3 % | 0,0 % | 40,0 % | 0,0 % | 29,3 % |

Rozsah je 1,4 % až 10,1 % u progresivní cesty s 1 SMR a flotilou 70:30 a 0,0 % až 1,1 % u konzervativní. Proto se uvádí pásmo: progresivní pod 25 %, konzervativní pod 5 %. Medián součtu se od součtu P50 liší, protože řádky jsou nesymetrické.

## 8. Co v modelu chybělo

Doplněno jako případy na běhu s rovnoměrnou elektrolýzou bez nádrže, ne na výchozím nastavení. Hodnoty jsou průměr 5 let, v závorce rozsah let.

| Případ | Cesta | Dovoz GWh | Přebytek GWh | Zimní špička dovozu MW | Hodin nad 800 / 1 000 / 1 200 MW |
|---|---|---|---|---|---|
| rovnoměrná elektrolýza, bez nádrže | Progresivní | 4 682 (4 630 až 4 731) | 176 | 862 (836 až 917) | 1 381 / 0 / 0 |
| výpadek SMR v nejhorší zimní hodině | Progresivní | 4 682 (4 630 až 4 731) | 176 | 1 362 (1 336 až 1 417) | 1 381 / 0 / 0 |
| elektromobily a kamiony nabíjené přes den | Progresivní | 4 657 (4 603 až 4 709) | 35 | 845 (820 až 901) | 1 355 / 0 / 0 |
| polovina tepla čerpadel posunutá do 4 h | Progresivní | 4 682 (4 630 až 4 731) | 175 | 861 (836 až 917) | 1 382 / 0 / 0 |
| teplo čerpadel o 10 % méně, mírnější zimy | Progresivní | 4 600 (4 548 až 4 649) | 180 | 845 (818 až 899) | 1 244 / 0 / 0 |
| teplo čerpadel o 21 % méně, mírnější zimy | Progresivní | 4 510 (4 459 až 4 559) | 184 | 827 (800 až 880) | 1 101 / 0 / 0 |
| skutečný rok FVE a tepla, ne průměr | Progresivní | 4 681 (4 501 až 4 808) | 174 | 863 (837 až 941) | 1 392 / 0 / 0 |
| tvar větru ze stanice Brno místo celostátního | Progresivní | 4 742 (4 684 až 4 786) | 305 | 894 (877 až 918) | 1 642 / 0 / 0 |
| výchozí nastavení | Konzervativní | 4 306 (4 256 až 4 350) | 0 | 492 (486 až 497) | 0 / 0 / 0 |

**Co model neumí**, každý řádek s velikostí:

- **Přiměřenost, LOLE.** Bez sazby výpadků ze zdroje se nepočítá. Místo toho hodiny dovozu nad 800, 1 000 a 1 200 MW v nejhorším roce: 1 478, 0 a 0, roční špička 907 MW. Se skutečným rokem fotovoltaiky a tepla a rovnoměrnou elektrolýzou je v nejhorším roce 0 hodin nad 1 000 MW.
- **Mez sítě a dovozu.** Transformační kapacita kraje nebyla zjištěna. Není mez, není počet nedodaných hodin. Velikost určují hodiny výše.
- **Dostupnost dovozu ze sousedů.** Regionální dovoz předpokládá přiměřenost státu. Standard je 15 h nedodávky za rok, Vnitrostátní plán s.75. Velikost pro kraj neznámá.
- **Řízené nabíjení aut.** Nabíjení přes den při rovnoměrné elektrolýze: přebytek 35 proti 176 GWh, zimní špička 845 proti 862 MW. Skutečné pravidlo podle ceny není modelované.
- **Auta jako zásobník.** Výkon = auta × připojený podíl × kW, velikost zcela závisí na předpokladech, nepočítá se.
- **Teplárny a teplo.** Nové plynové bloky běží na špičku, studie je vede teplem. Účinek: hodiny plynu; v energii omezený rozpočtem 115,2 GWh.
- **Ocel na vodíku.** 3,48 MWh/t (Vogl a kol. 2018) proti 0,45 MWh/t: 1,5 mil. t by přidalo asi 4,5 TWh, řádově celý schodek.
- **Biometan.** Bez řádku. Měřítko 340 až 930 GWh, pokud by ho kraj neměl použít jinde. Studie počítá s vtláčením do sítě, ne s výrobou elektřiny.
- **Výroba v průmyslu.** Biocel, Třinec zčásti v řádcích. Velikost bez dat provozovatelů neznámá.
- **Regulace FVE.** Omezení výroby je jen vývoz, 3,0 GWh, zanedbatelné.
- **Ceny.** Hodiny plynu jsou předpoklad, ne výsledek ceny. Bez pružnosti poptávky. Rozhoduje o tom, zda je plynová cesta vůbec věrohodná.
- **Rezervy.** Největší blok 500 MW jde do státní rezervy. Účinek na energii žádný.
- **Klima a voda.** Řádek 55 GWh, účinek klimatu asi ±10 GWh, zanedbatelné.
- **Meziroční vítr.** Skutečné roky FVE a tepla mění dovoz 4 501 až 4 808 GWh. Vítr je v tom normovaný, celostátní index míchá výkon a větrnost. Tvar z Brna dá při rovnoměrné elektrolýze přebytek 305 proti 176 GWh.


## 9. Otevřená rozhodnutí

Nezměněno. Změna ročního schodku 2050 v GWh, kladná schodek zvětšuje. Vlastní spotřeba a ztráty se počítají znovu.

| Rozhodnutí | Progresivní | Konzervativní | Poznámka |
|---|---|---|---|
| Využití SMR 84,4 % (změřeno v ČR 2025) místo 90 % | 226,6 | 0,0 |  |
| Využití SMR 81,7 % (průměr ČR 2024 a 2025) místo 90 % | 334,9 | 0,0 |  |
| Využití SMR 79,0 % (změřeno v ČR 2024) místo 90 % | 443,2 | 0,0 |  |
| Podíl větru kraje 13,07 % místo 11,33 % | −232,2 | −35,7 | vítr při 2 471 h, stejné národní MW |
| Ostatní průmysl bez 420 GWh ze seznamu projektů | −435,7 | 0,0 |  |
| Ostatní průmysl jen polovina ze 420 GWh | −217,9 | 0,0 |  |
| Auta 14,5 kWh/100 km místo 12,0 kWh/100 km | 200,1 | 40,0 | index 0,85 proti 0,705 |
| Vodík 55,1 kWh/kg místo 51,36 kWh/kg | 90,3 | 0,0 | 23287 t ročně |
| Datacentra drží 361,4 GWh od 2040, nerostou na 700,8 | −351,9 | −35,2 |  |
| Datacentra žádná | −726,6 | −72,7 |  |
| Druhý SMR | −3 631,9 | 0,0 | bez podkladu; v konzervativní cestě by to byl první |
| První SMR v konzervativní cestě | 0,0 | −3 631,9 | bez podkladu |
| Míra ztrát roste se zátěží, 30 % stálé a 70 % proměnné | 265,5 | 43,2 | rozdělení bez zdroje, bez zesílení sítě |
| Násobek míry ztrát 1,7 za dvojnásobnou zátěž sítě, v modelu vypuštěný | 0,0 | 199,5 | čtení definice konzervativní cesty |
| Baterie se nabíjí jen z přebytku, ne ze sítě | −24,4 | −18,4 | stejná velikost baterie |
| Nová huť na 80 % výkonu | −139,9 | −139,9 |  |
| Nová huť se nepostaví | −699,8 | −699,8 |  |
| Třinec 450 kWh/t místo 300 | 404,4 | 202,2 |  |
| Třinec 180 kWh/t, tiskový údaj | −323,4 | −161,7 |  |
| Biometan 635 GWh na blocích, dřívější odvození | −635,0 | 0,0 | studie pro kraj číslo nedává |
| Vodík flotily vyrobený mimo kraj | −1 240,0 | 0,0 |  |
| Flotila celá na bateriích | −885,1 | 0,0 |  |

**Otevřené body bez rozhodnutí.** Biometan: dřívější odvození počítalo 866 GWh na 433 MW a 2 000 h, řádek syntetického plynu dával 231 GWh, zbylých 635 GWh nemělo řádek. Studie popisuje přestavbu bioplynových stanic na biometan a vtláčení do sítě, pro výrobu elektřiny v kraji číslo nedává, proto řádek nepřibyl. Syntetický plyn: elektřina na jeho výrobu není vyčíslena, studie ji uvádí jako vysokou. Uzel plynu 2035. Stanice flotily a tankovací profil.

## 10. Kontrola závěrů

**Které změny bez důkazu schodek zvětšují a které zmenšují?** Změny, které schodek zvětšují: Třinec 300 kWh/t (úsudek mezi 180 a 450 kWh/t), syntetický plyn (studie, ale jiná technologie), komprese (měření). Změny, které ho zmenšují: vlastní spotřeba podle vzorce, konzervativní ztráty, úspory, kotle. Nejslabší je Třinec a ztráty. Míra ztrát rostoucí se zátěží by přidala 265 GWh progresivní a 43 GWh konzervativní cestě, ale 30/70 nemá zdroj a vyšší zátěž by šla se zesílením sítě, proto je jen mezi rozhodnutími. Konzervativní cesta z toho profituje o rozdíl mezi 6,03 % a 3,547 %, tedy asi 190 GWh, a je třeba to říct: její dřívější vyšší ztráty byly mechanickým čtením dvojnásobné zátěže. Nové pravidlo baterie výrok neovlivní, roční bilance se mění o ztráty.

**Nezlepšují hodiny závěr?** Rozšíření mezí řádku o hodiny P10 a P90 měří tabulka:

| Cesta | Varianta | Vodík | Úroveň 1, podíl | Medián GWh | P90 GWh |
|---|---|---|---|---|---|
| Progresivní | základ | 70:30 | 7,5 % | −4 073 | −464 |
| Progresivní | základ | na bateriích | 11,1 % | −3 159 | 166 |
| Progresivní | meze řádků jen při 942 h a 2 471 h, vítr P10 2 014,8 h | 70:30 | 6,0 % | −4 249 | −744 |
| Progresivní | meze řádků jen při 942 h a 2 471 h, vítr P10 2 014,8 h | na bateriích | 8,8 % | −3 340 | −177 |
| Konzervativní | základ | na bateriích | 0,6 % | −4 335 | −2 078 |
| Konzervativní | meze řádků jen při 942 h a 2 471 h | na bateriích | 0,5 % | −4 347 | −2 119 |

Zvolené meze hodin zvyšují podíl splněných běhů nejvýš o několik procentních bodů, výrok nemění.

Je flotila započítaná dvakrát? Ne. Bateriová a vodíková část nákladní dopravy dávají dohromady 996,8 mil. km (70 % a 30 %), MHD 21,547 mil. km a auta mají vodík 0. Řádky vodíku se v hodinovém modelu nepočítají do bateriové zátěže. Zbývá možný překryv 45,8 GWh.

### Zpětná kontrola metody

| Test | Výsledek |
|---|---|
| Čistá spotřeba 2015 na 2025, držení hodnoty 2015 | předpoklad 5 910,4 GWh, skutečnost 5 963,8 GWh, chyba −0,9 % |
| Výroba 2015 na 2025, držení hodnoty 2015 | předpoklad 6 794,1 GWh, skutečnost 2 805,2 GWh, chyba 142,2 %. V datech roku 2015 uzavírání parních zdrojů není, metoda by ho musela dostat jako datovanou událost |
| Pozorované změny, čistá spotřeba, 2014 až 2025 | za 5 let −8,3 až 12,3 %, za 10 let 0,9 až 3,5 % |
| Šířka P10 až P90 modelu, čistá spotřeba, po 10 letech (2035) | progresivní 26,6 %, konzervativní 25,5 % mediánu |
| Pozorované změny, výroba, 2014 až 2025 | za 5 let −47,2 až −21,7 %, za 10 let −58,7 až −52,4 % |
| Šířka P10 až P90 modelu, výroba, po 10 letech (2035) | progresivní 73,8 %, konzervativní 53,5 % mediánu |
| Pokryje pásmo výroby změnu, kterou kraj zažil? | Ne pro výrobu: pokles −58,7 % za 10 let je větší než polovina šířky pásma. Spotřebu pásmo pokrývá |
| Mimo vzorek: spotřeba sektorů, 1. pololetí 2026 proti 2025, ERÚ tab. 6.3 | změřeno −10,6 GWh za pololetí; křivka za celý rok −63,8 GWh progresivní, −66,6 GWh konzervativní |
| Mimo vzorek: výroba, 1. pololetí 2026 proti 2025, ERÚ tab. 6.1 | změřeno −334,9 GWh za pololetí; křivka za celý rok −307,1 GWh progresivní, −299,7 GWh konzervativní |

### Kontroly

| Kontrola | Hodnota |
|---|---|
| hodinový běh proti hodinový model, největší rozdíl MW | 0,000 |
| progresivni: výroba minus spotřeba P50 proti tabulce GWh | 0,002 |
| konzervativni: výroba minus spotřeba P50 proti tabulce GWh | 0,002 |
| progresivni vyroba: medián společného losování proti model stránky GWh | 0,048 |
| progresivni vyroba: šířka P10 až P90 proti model stránky GWh | 0,014 |
| progresivni spotreba: medián společného losování proti model stránky GWh | 0,020 |
| progresivni spotreba: šířka P10 až P90 proti model stránky GWh | 0,010 |
| konzervativni vyroba: medián společného losování proti model stránky GWh | 0,044 |
| konzervativni vyroba: šířka P10 až P90 proti model stránky GWh | 0,066 |
| konzervativni spotreba: medián společného losování proti model stránky GWh | 0,015 |
| konzervativni spotreba: šířka P10 až P90 proti model stránky GWh | 0,032 |

Další kontroly: křivky stránky proti modelu, součty po letech proti tabulce a test logiky stránky procházejí. Hodinové kontroly 29 z 29 v pořádku, včetně hodinové bilance pod 0,1 GWh a toho, že baterie nezvedla denní špičku. Roční bilance tabulky a hodinového výpočtu se liší o 0,01 GWh v progresivní a 0,00 GWh v konzervativní cestě.

## 11. Změny proti studii

Řádky, které se od studie odchylují, s vysvětlením z poznámky řádku:

| Řádek | Cesta | P50 2050 | Proč studie nestačí, z poznámky řádku |
|---|---|---|---|
| černé uhlí: Dětmarovice | progresivni | 0,0 | Základ není ve studii, ta končí 2023. |
| černé uhlí: Dětmarovice | konzervativni | 0,0 | Základ není ve studii, ta končí 2023. |
| hnědé uhlí | progresivni | 0,0 | Výhled pro hnědé uhlí studie neuvádí, proto Vnitrostátní plán. |
| hnědé uhlí | konzervativni | 0,0 | Výhled pro hnědé uhlí studie neuvádí, proto Vnitrostátní plán. |
| ostatní paliva a odpadní teplo (přidaná položka) | progresivni | 15,0 | Studie tato paliva zvlášť neuvádí. |
| ostatní paliva a odpadní teplo (přidaná položka) | konzervativni | 15,0 | Studie tato paliva zvlášť neuvádí. |
| fotovoltaika střešní | progresivni | 948,5 | Podíl 1,4 % ze 7,2 TWh (100,8 GWh) je pod dnešní výrobou, a progresivní cesta chce maximum OZE, proto Vnitrostátní plán. |
| fotovoltaika střešní | konzervativni | 256,1 | Podíl 1,4 % ze 7,2 TWh (100,8 GWh) je pod dnešní výrobou, a progresivní cesta chce maximum OZE, proto Vnitrostátní plán. |
| fotovoltaika pozemní | progresivni | 632,3 | Podíl 1,4 % ze 7,2 TWh (100,8 GWh) je pod dnešní výrobou, a progresivní cesta chce maximum OZE, proto Vnitrostátní plán. |
| fotovoltaika pozemní | konzervativni | 170,7 | Podíl 1,4 % ze 7,2 TWh (100,8 GWh) je pod dnešní výrobou, a progresivní cesta chce maximum OZE, proto Vnitrostátní plán. |
| vítr | progresivni | 1 539,9 | Podíl 2,1 % ze 7,2 TWh (151,2 GWh) neodpovídá maximu OZE v progresivní cestě, MW pro 2030 a 2050 studie neuvádí, proto Vnitrostátní plán a projekty. |
| vítr | konzervativni | 236,7 | Podíl 2,1 % ze 7,2 TWh (151,2 GWh) neodpovídá maximu OZE v progresivní cestě, MW pro 2030 a 2050 studie neuvádí, proto Vnitrostátní plán a projekty. |
| Třinecké železárny | progresivni | 1 549,2 | Studie spotřebu ani nárůst nečísluje, proto tisk a podklady firmy. |
| Třinecké železárny | konzervativni | 1 159,2 | Studie spotřebu ani nárůst nečísluje, proto tisk a podklady firmy. |
| Nová huť | progresivni | 736,3 | Studie spotřebu nečísluje a počítá s obnovou provozu Liberty, proto web a úsudek. |
| Nová huť | konzervativni | 736,3 | Studie spotřebu nečísluje a počítá s obnovou provozu Liberty, proto web a úsudek. |
| doly | progresivni | 15,0 | Studie spotřebu dolů neuvádí. |
| doly | konzervativni | 15,0 | Studie spotřebu dolů neuvádí. |
| chlazení | progresivni | 191,1 | Studie chlazení neuvádí. |
| chlazení | konzervativni | 158,4 | Studie chlazení neuvádí. |
| datacentra | progresivni | 700,8 | Studie datacentra neuvádí. |
| datacentra | konzervativni | 70,1 | Studie datacentra neuvádí. |
| úspory a účinnost | progresivni | −299,1 | Studie úspory nečísluje. |
| úspory a účinnost | konzervativni | −149,6 | Studie úspory nečísluje. |

## 12. Nejistoty a meze

- Tvary hodin jsou celostátní nebo z Ostravy a jen z 5 let. Úroveň určuje řádek.
- Jeden uzel bez limitů sítě. Baterie vidí den dopředu přesně. Rozvrh plynu, elektrolýzy ze sítě a nádrže zná celý rok dopředu, skutečný provoz by špičku dovozu zvýšil, velikost je v oddíle 4.
- Přes polovinu řádků má stupeň D. Meze P10 a P90 jsou většinou úsudek. Faktor korelace 0,6 je odhad.
- Tvar SMR: odstávka na jaře, celý blok 500 MW. V hodinovém Monte Carlu je losovaná výroba bloku zespodu omezená na 3 130 GWh. Studie uvádí 350 MW a jeden blok 470 MW.
- Cherp et al. 2021 je přečtený jen ve výtahu a je to národní měřítko.
- Tepelná čerpadla a auta nereagují na cenu ani řízení. Datacentra nemají zdroj.
