# Přepočet bilance MSK 2050: hodiny, flotila, křivky a soběstačnost

Stav k 2026-11-05. Výpočet stojí na tabulce položek a hodinovém modelu pro 5 povětrnostních let 2015 až 2019. Soběstačnost znamená jen elektřinu vyrobenou v kraji. Palivo pro SMR i zemní plyn je dovezené i tehdy, když je bilance elektřiny kladná. Výchozí nastavení je jediné: baterie 2,6 GWh a 650 MW s vyrovnáváním dne, elektrolyzér 550 MW, malá nádrž asi 50 t, flotila MHD 50 %, nákladní doprava 50 %, auta 0 %. Dovoz 5 263 GWh, vývoz 0,4 GWh, zimní špička dovozu 911 MW, bilance prosince až února −1 505 GWh. Dva další běhy mají vždy svůj název: elektrolyzér mimo prosinec až únor a rovnoměrná elektrolýza bez nádrže. Rozvrh plynu, elektrolýzy ze sítě a nádrže zná celý rok dopředu, baterie zná den dopředu přesně.

## 1. Odpověď

**S elektrárnami, které obě cesty předpokládají, kraj v roce 2050 zůstane závislý na dovozu.** Progresivní cesta vyrobí 7 862 GWh a spotřebuje 13 128 GWh, tedy 59,9 %. Chybí 5 266 GWh. Konzervativní cesta vyrobí 3 956 GWh ze 8 244 GWh, tedy 48,0 %, a chybí 4 287 GWh.

**Závislost plyne z toho, kolik elektráren cesty předpokládají a kolik elektřiny spotřebují, není to fyzikální mez.** Konzervativní cesta by rok uzavřela 1 766 MW větru navíc, tedy 1 862 MW uvnitř meze studie 2 014 MW. Překážkou je tempo: 73 MW za rok, 8,0krát víc než největší roční přírůstek kraje, a v hodinách i tak zůstane dovoz 766 GWh a 704 GWh přebytku. Progresivní cesta rok uzavře větrem na mezi a 2,2 GWp fotovoltaiky navíc, nebo více než jedním dalším SMR (1,45 čistého bloku), pro který podklad není.

| Úroveň | Progresivní, 1 SMR, flotila 50/50, malá nádrž | Konzervativní, bez SMR |
|---|---|---|
| 1, rok | Nesplněno, −5 266 GWh. Podíl běhů pod 10 % | Nesplněno, −4 287 GWh. Podíl běhů pod 5 %. Rok uzavře vítr uvnitř meze, překáží tempo |
| 2, říjen až březen | Nesplněno, −2 768 GWh. Podíl běhů pod 10 % | Nesplněno, −2 139 GWh. Podíl běhů pod 1 %. Vítr samotný +1 636 MW |
| 2, prosinec až únor | Nesplněno, −1 505 GWh. Podíl běhů pod 5 % | Nesplněno, −1 058 GWh. Podíl běhů pod 1 %. Vítr samotný +1 601 MW |
| 3, hodiny | Nesplněno. Bez dovozu 1,5 % hodin, zimní špička dovozu 977 MW v nejhorším roce při nádrži 50 t, roční špička 1 060 MW | Nesplněno. Bez dovozu 0,0 % hodin, špička 543 MW |

Podíl běhů je pásmo, ne přesné číslo. Závisí na neověřené korelaci a mezích, viz oddíl 7. Úroveň 2 v simulaci počítá s rovnoměrnou elektrolýzou.

## 2. Bilance

| Cesta | Veličina, GWh | 2026 | 2030 | 2040 | 2050 |
|---|---|---|---|---|---|
| Progresivní | Výroba | 2 498 | 2 973 | 4 276 | 7 862 |
| Progresivní | Spotřeba | 7 006 | 7 287 | 9 861 | 13 128 |
| Konzervativní | Výroba | 2 506 | 3 243 | 3 064 | 3 956 |
| Konzervativní | Spotřeba | 7 003 | 7 050 | 8 060 | 8 244 |

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
| Vytápění a chlazení | 1 391,8 | 1 334,4 |
| Doprava na bateriích a trolejích | 1 546,3 | 510,4 |
| Vodík | 2 039,1 | 13,7 |
| Datacentra | 700,8 | 70,1 |
| Vlastní spotřeba zdrojů | 460,1 | 218,2 |
| Ostatní energetika | 1 000,8 | 1 000,8 |
| Ztráty v sítích a baterií | 499,2 | 267,1 |

Bilance 2050: progresivní −5 265,8 GWh, konzervativní −4 287,4 GWh.

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
| elektrokotle v teplárnách | progresivni | 150,0 | 12,1 | 50,0 až 400,0 | 0,0 až 70,0 | D | −137,9 | Mez 70 MW je náš součet: 18 MW (s.121), 12 MW a nejvýš dva další po 20 MW (s.166, extrémní scénář). Předpokládá, že 18 a 12 MW jsou dva různé kotle. Kotel bere jen přebytek, řádek je výsledek hodinového běhu. |
| elektrokotle v teplárnách | konzervativni | 9,0 | 0,0 | 2,0 až 40,0 | 0,0 až 9,0 | D | −9,0 | Mez 70 MW je náš součet: 18 MW (s.121), 12 MW a nejvýš dva další po 20 MW (s.166, extrémní scénář). Předpokládá, že 18 a 12 MW jsou dva různé kotle. Kotel bere jen přebytek, řádek je výsledek hodinového běhu. |
| vlaky | progresivni | 37,6 | 37,6 | 37,6 až 111,1 | 30,0 až 111,1 | B na C | 0,0 | P10 pod P50, dřívější mez neměla žádný pokles. |
| vlaky | konzervativni | 35,7 | 35,7 | 30,0 až 100,0 | 30,0 až 100,0 | B na D | 0,0 | 95 % je z definice cesty, ne z publikace. |
| MHD | progresivni | 11,9 | 11,9 | 11,9 až 33,9 | 9,5 až 33,9 | D | 0,0 | Křivka bez P10 pod P50, P10 o 20 % níž. |
| MHD | konzervativni | 19,0 | 19,0 | 15,0 až 65,0 | 15,0 až 65,0 | B na D | 0,0 | 80 % je z definice cesty, hodnota pod základem. |
| výroba vodíku | progresivni | 45,8 | 45,8 | 20,0 až 260,4 | 20,0 až 260,4 | B na C | 0,0 | P50 2050 je ze studie, 2030 a 2040 jsou volba modelu. |
| výroba vodíku: osobní auta | progresivni | 0,0 | 0,0 | 0,0 až 0,0 | 0,0 až 0,0 | C na D | 0,0 | Stupeň podle jednotného pravidla: nejslabší vstup hodnoty P50. |
| výroba vodíku: osobní auta | konzervativni | 0,0 | 0,0 | 0,0 až 0,0 | 0,0 až 0,0 | C na D | 0,0 | Stupeň podle jednotného pravidla: nejslabší vstup hodnoty P50. |
| výroba vodíku: nákladní doprava | progresivni | 1 925,0 | 1 958,1 | 884,5 až 2 958,5 | 900,5 až 3 003,5 | D | 33,1 | Komprese 3,1 kWh/kg změřená místo modelových 2,23 kWh/kg, celkem 51,36 kWh/kg. |
| výroba vodíku: MHD | progresivni | 34,6 | 35,2 | 16,1 až 103,1 | 16,4 až 104,7 | D | 0,6 | Komprese 3,1 kWh/kg změřená místo modelových 2,23 kWh/kg, celkem 51,36 kWh/kg. |
| výroba syntetického plynu | progresivni | 0,0 | 0,0 | 0,0 až 0,0 | 0,0 až 0,0 | C na D | 0,0 | Volba modelu proti s.169 studie, nula je znak neznámé hodnoty. |
| výroba syntetického plynu | konzervativni | 0,0 | 0,0 | 0,0 až 0,0 | 0,0 až 0,0 | C na D | 0,0 | Volba modelu proti s.169 studie, nula je znak neznámé hodnoty. |
| vlastní spotřeba zdrojů | progresivni | 491,6 | 460,1 | 368,7 až 614,5 | 345,1 až 575,2 | C | −31,5 | Vzorec z výroby, počítá i SMR, 310 GWh na blok. Dřívější řádek byl jen křivka přes milníky. |
| vlastní spotřeba zdrojů | konzervativni | 227,6 | 218,2 | 170,7 až 284,5 | 163,7 až 272,8 | C | −9,4 | Vzorec z výroby, počítá i SMR, 310 GWh na blok. Dřívější řádek byl jen křivka přes milníky. |
| ostatní energetika (přidaná položka) | progresivni | 1 000,8 | 1 000,8 | 600,0 až 1 050,0 | 600,0 až 1 200,0 | D | 0,0 | P90 1 200 GWh, měřené pololetí 2026 je už nad dřívějším P90. |
| ostatní energetika (přidaná položka) | konzervativni | 1 000,8 | 1 000,8 | 600,0 až 1 050,0 | 600,0 až 1 200,0 | D | 0,0 | P90 1 200 GWh, měřené pololetí 2026 je už nad dřívějším P90. |
| ztráty v sítích | progresivni | 426,4 | 431,8 | 383,2 až 546,4 | 388,6 až 552,7 | C | 5,4 | Stejný vzorec v obou cestách, r = 3,547 %. V konzervativní cestě odpadá násobek 1,7. |
| ztráty v sítích | konzervativni | 446,2 | 267,1 | 336,2 až 530,9 | 240,4 až 341,9 | D na C | −179,1 | Stejný vzorec v obou cestách, r = 3,547 %. V konzervativní cestě odpadá násobek 1,7. |
| ztráty baterií | progresivni | 40,7 | 67,4 | 22,0 až 88,2 | 36,4 až 146,3 | D | 26,7 | Baterie cykluje i ze sítě, nabito minus vybito z hodinového běhu. |
| úspory a účinnost | progresivni | −290,0 | −299,1 | −500,0 až −100,0 | −500,0 až −100,0 | D | −9,1 | Oprava součtu, ostatní průmysl má základ 1 571,4 GWh. |
| úspory a účinnost | konzervativni | −145,0 | −149,6 | −300,0 až −50,0 | −300,0 až −50,0 | D | −4,6 | Oprava součtu, ostatní průmysl má základ 1 571,4 GWh. |

**Pravidlo stupně důkazu je jedno:** řídí se nejslabším vstupem hodnoty P50 pro rok 2050. Meze P10 a P90 jsou téměř všude úsudek a stupeň se k nim nevztahuje.

**Křivky.** Ploché řádky už nemají falešnou S-křivku ze zaokrouhlení, to samo zúžilo pásmo spotřeby v roce 2026. Nové plynové bloky, datacentra a vodík ze studie jsou nula, dokud neběží žádné zařízení. FVE, vítr a tepelná čerpadla mají v roce 2026 obě cesty stejný uzel. Uhlí v teplárnách odchází postupně. Milníky u skokových řádků ukazují hodnotu v tom roce, ne podmíněný stav. Ztráty a vlastní spotřeba jsou vzorce, proto se cesty v roce 2026 liší jen o pár GWh.

**Uzel plynu 2035 zůstává neuvedený.** Tab.30 s.132 dává pro 2035 výkon 683 MW, ne energii. Uzel v GWh při 3 521 h a 90 % by byl 2 164 GWh a milník 2040 je 1 372 GWh, takže by energie mezi 2035 a 2040 klesala bez důvodu. Výkon už na energii nezávisí, zimní pohled proto rok 2035 počítá správně.

**Elektrolyzér.** Platí jedna definice: výkon = řádky vodíku flotily × (1 + míra ztrát sítě) × 1 000 / plné hodiny. Plné hodiny jsou z hodinového výpočtu (3 758 h, přebytek do sítě pod 1 %, baterie první, 2,6 GWh). Výsledek je 550 MW. Řádek 45,8 GWh ze studie je vodík mimo flotilu a běží jako rovnoměrná zátěž mimo tento výkon.

## 4. Baterie a vodík, dnešní mix, 1 SMR

### Pravidlo

Přebytek má přednost. Každou půlnoc se z křivky zbytkového zatížení na další den a z náboje najde nejnižší rovná hladina, kterou baterie udrží v pořadí hodin. Nad hladinou vybíjí, pod hladinou minus 100 MW nabíjí ze sítě a nechá místo na přebytek, který ten den ještě přijde. Nabíjení končí pod hladinou, takže při přesné předpovědi denní špička nestoupne, kontrola to hlídá v každém běhu. Rozdíl 100 MW je úsudek: menší rozdíl přidává cykly a ztráty a špičku téměř nemění. Pravidlo jen z přebytku zůstává jako varianta.

**Co je známo dopředu.** Baterie zná křivku dalšího dne přesně. Rozvrh plynu, elektrolýzy ze sítě a nádrže zná celý rok. Se včerejší křivkou místo předpovědi baterie ve výchozím nastavení zvedne denní špičku 2 až 7 dnů v roce, nejvýš o 180 MW; při elektrolyzéru mimo prosinec až únor 3 až 8 dnů, nejvýš o 255 MW. Když plyn dostane práh z předchozího povětrnostního roku místo znalosti celého roku, stoupne ve výchozím nastavení zimní špička dovozu v nejhorším roce z 977 na 1 175 MW a po vyčerpání paliva roční špička na 1 493 MW; v roce po chladnějším roce zůstane až 79 GWh plynu nevyužito. Při elektrolyzéru mimo prosinec až únor je to 747 na 834 MW a roční špička 1 088 MW.

### Velikost bez cíle

E_den = součet kladných odchylek od denního průměru / √0,88, výkon = největší hodinová odchylka. Spotřeba bez elektrolýzy minus neřízené zdroje včetně SMR, 1 825 dnů.

| Statistika | E_den GWh | Výkon MW |
|---|---|---|
| Medián | 2,64 | 582 |
| P90 | 4,42 | 799 |
| P95 | 4,82 | 850 |
| Maximum | 6,17 | 1 129 |

Pravidlo pro velikost je medián a 4 hodiny: **2,6 GWh a 650 MW**. Medián denního přebytku je 0,39 GWh a 32 % dnů přebytek nemá, přebytek sám by takovou baterii nenaplnil.


Podle velikosti, průměr 5 let, elektrolyzér mimo prosinec až únor. Noc je 18:00 až 06:00 v pevném čase SEČ, úspora je čistá po nabíjení ve stejné noci. Večer je 17:00 až 22:00. Kryté noci jsou počet za rok plně / aspoň z poloviny. Pokles špičky prosince až února je medián / nejhorší povětrnostní rok.

| Pravidlo | GWh | Cykly | Nabito z přebytku GWh | Nabito ze sítě GWh | Noc úspora GWh | Večer úspora GWh | Kryté noci | Pokles špičky před plynem MW | Pokles špičky po plynu MW | Po plynu po letech | Dovoz GWh | Vývoz GWh | Ztráty GWh | Kotle GWh |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vyrovnání dne | 0,0 | 0 | 0 | 0 | 0 | 0 | 0,0 / 0,0 | 0 / 0 | 0 / 0 | 2015: 0, 2016: 0, 2017: 0, 2018: 0, 2019: 0 | 5 276 | 9,0 | 0,0 | 81 |
| Vyrovnání dne | 0,5 | 259 | 64 | 83 | 26 | 43 | 0,0 / 0,4 | 122 / 54 | 32 / 25 | 2015: 32, 2016: 32, 2017: 25, 2018: 35, 2019: 29 | 5 279 | 7,6 | 17,7 | 67 |
| Vyrovnání dne | 1,0 | 271 | 147 | 161 | 77 | 83 | 0,0 / 1,0 | 142 / 55 | 61 / 50 | 2015: 67, 2016: 61, 2017: 50, 2018: 70, 2019: 58 | 5 277 | 5,7 | 37,0 | 48 |
| Vyrovnání dne | 1,5 | 248 | 202 | 220 | 113 | 106 | 0,0 / 3,2 | 142 / 55 | 76 / 65 | 2015: 93, 2016: 76, 2017: 65, 2018: 87, 2019: 74 | 5 276 | 5,0 | 50,6 | 34 |
| Vyrovnání dne | 2,0 | 220 | 241 | 259 | 139 | 119 | 0,0 / 4,4 | 142 / 55 | 87 / 71 | 2015: 97, 2016: 82, 2017: 71, 2018: 96, 2019: 87 | 5 273 | 4,1 | 60,1 | 23 |
| Vyrovnání dne | 2,6 | 190 | 277 | 285 | 159 | 129 | 0,0 / 9,2 | 142 / 55 | 94 / 73 | 2015: 101, 2016: 87, 2017: 73, 2018: 102, 2019: 94 | 5 269 | 3,3 | 67,4 | 13 |
| Vyrovnání dne | 3,0 | 172 | 294 | 294 | 169 | 134 | 0,0 / 12,6 | 142 / 55 | 95 / 73 | 2015: 102, 2016: 89, 2017: 73, 2018: 103, 2019: 95 | 5 267 | 2,8 | 70,5 | 8 |
| Vyrovnání dne | 4,0 | 137 | 317 | 305 | 181 | 140 | 0,0 / 20,0 | 142 / 55 | 94 / 70 | 2015: 103, 2016: 90, 2017: 70, 2018: 104, 2019: 94 | 5 265 | 1,8 | 74,6 | 3 |
| Vyrovnání dne | 5,0 | 111 | 324 | 307 | 185 | 141 | 0,0 / 21,4 | 142 / 55 | 93 / 69 | 2015: 104, 2016: 90, 2017: 69, 2018: 103, 2019: 93 | 5 265 | 1,2 | 75,8 | 2 |
| Vyrovnání dne | 8,0 | 70 | 333 | 308 | 190 | 143 | 0,0 / 22,6 | 142 / 55 | 93 / 69 | 2015: 104, 2016: 89, 2017: 69, 2018: 103, 2019: 93 | 5 263 | 0,3 | 76,8 | 0 |
| Vyrovnání dne | 12,0 | 47 | 334 | 308 | 190 | 144 | 0,0 / 22,8 | 142 / 55 | 93 / 69 | 2015: 104, 2016: 89, 2017: 69, 2018: 103, 2019: 93 | 5 263 | 0,0 | 77,0 | 0 |
| Jen přebytek | 0,0 | 0 | 0 | 0 | 0 | 0 | 0,0 / 0,0 | 0 / 0 | 0 / 0 | 2015: 0, 2016: 0, 2017: 0, 2018: 0, 2019: 0 | 5 276 | 9,0 | 0,0 | 81 |
| Jen přebytek | 0,5 | 175 | 100 | 0 | 33 | 18 | 0,2 / 0,2 | 0 / 0 | 3 / 0 | 2015: 3, 2016: 4, 2017: 0, 2018: 3, 2019: 3 | 5 263 | 5,5 | 11,9 | 60 |
| Jen přebytek | 1,0 | 154 | 175 | 0 | 61 | 33 | 0,2 / 1,8 | 0 / 0 | 3 / 0 | 2015: 3, 2016: 4, 2017: 0, 2018: 4, 2019: 2 | 5 254 | 4,0 | 20,9 | 43 |
| Jen přebytek | 1,5 | 135 | 230 | 0 | 83 | 46 | 1,0 / 3,8 | 0 / 0 | 2 / 0 | 2015: 2, 2016: 3, 2017: 0, 2018: 3, 2019: 1 | 5 246 | 3,0 | 27,6 | 30 |
| Jen přebytek | 2,0 | 119 | 270 | 0 | 102 | 58 | 2,2 / 8,4 | 0 / 0 | 2 / 0 | 2015: 2, 2016: 2, 2017: 0, 2018: 2, 2019: 1 | 5 238 | 2,1 | 32,4 | 18 |
| Jen přebytek | 2,6 | 102 | 300 | 0 | 118 | 71 | 3,8 / 14,0 | 0 / 0 | 1 / 0 | 2015: 1, 2016: 2, 2017: 0, 2018: 1, 2019: 1 | 5 232 | 1,5 | 36,0 | 9 |
| Jen přebytek | 3,0 | 92 | 313 | 0 | 126 | 75 | 4,8 / 19,0 | 0 / 0 | 1 / 0 | 2015: 1, 2016: 2, 2017: 0, 2018: 1, 2019: 1 | 5 230 | 1,2 | 37,5 | 5 |
| Jen přebytek | 4,0 | 72 | 327 | 0 | 135 | 77 | 7,2 / 24,4 | 0 / 0 | 1 / 0 | 2015: 1, 2016: 2, 2017: 0, 2018: 1, 2019: 1 | 5 227 | 0,5 | 39,2 | 1 |
| Jen přebytek | 5,0 | 58 | 331 | 0 | 137 | 77 | 8,4 / 24,4 | 0 / 0 | 1 / 0 | 2015: 1, 2016: 2, 2017: 0, 2018: 1, 2019: 1 | 5 227 | 0,3 | 39,8 | 1 |
| Jen přebytek | 8,0 | 37 | 334 | 0 | 138 | 78 | 9,2 / 24,8 | 0 / 0 | 1 / 0 | 2015: 1, 2016: 2, 2017: 0, 2018: 1, 2019: 1 | 5 226 | 0,0 | 40,1 | 0 |
| Jen přebytek | 12,0 | 25 | 334 | 0 | 138 | 78 | 9,2 / 24,8 | 0 / 0 | 1 / 0 | 2015: 1, 2016: 2, 2017: 0, 2018: 1, 2019: 1 | 5 226 | 0,0 | 40,1 | 0 |

**Co je ta velikost poctivě, při elektrolyzéru mimo prosinec až únor.** 2,6 GWh je jeden den výkyvu, ne záloha a ne zdroj energie. Proti pravidlu jen z přebytku nové pravidlo zvedá ztráty z 36,0 na 67,4 GWh a roční dovoz z 5 232 na 5 269 GWh, tedy o 37 GWh. Za to dává pokles zimní špičky 142 / 55 MW před plynem a 94 / 73 MW po plynu, zatímco staré pravidlo prakticky nic (1 / 0 MW). Večer ušetří 129 GWh proti 71 GWh. Celou noc nepokryje skoro nikdy. Pokles špičky přestává růst před plynem už kolem 1 GWh a po plynu kolem 2 až 3 GWh. Při tomto pravidlu, které plánuje jen jeden den dopředu a začíná každou půlnoc s tím, co v baterii zbylo, větší baterie zimní špičku dál nesnižuje. Je to vlastnost pravidla. Stejná baterie s plánem na dva dny, při přesné předpovědi, dá před plynem 244 / 208 MW místo 142 / 55 MW. Je to zkouška výroku, ne návrh. Bez baterie je dovoz 5 276 GWh, jenže přebytek tehdy bere víc kotlů (81 GWh proti 13 GWh), takže čistý přínos baterie pro dovoz je malý.

**Ve výchozím nastavení s malou nádrží 50 t**, kdy elektrolyzér v zimě běží a nádrž ho přesouvá jen o hodiny, je zimní špička po plynu 911 MW s baterií a 969 MW bez ní, pokles medián 60 MW, nejhorší rok 49 MW. Rozvrh elektrolyzéru vyrovnává nejchladnější den sám, proto baterie špičku před plynem nesnižuje: 0 MW. Pokles po plynu vzniká tím, že baterie uvolní plyn na hodiny špičky. Baterie 5 GWh dá 55 / 46 MW, baterie 12 GWh 55 / 46 MW, baterie 2,6 GWh s plánem na dva dny 86 / 81 MW, obojí s přesnou předpovědí.

Přebytek před baterií, kotli a elektrolyzérem je 334 GWh. Z něj jde 309 GWh do vodíku, 13 GWh do kotlů, 12 GWh do baterie a 0,4 GWh je vývoz. Baterie bere ze sítě 521 GWh, ztráty jsou 63,9 GWh. Přebytek do vodíku tu zahrnuje i výrobu v přebytkových hodinách, kterou rozvrh nádrže vede jako výrobu ze sítě. Večer klesne dovoz o 78 GWh, roční dovoz o 13 GWh, zbytek se přesune do jiných hodin. Pravidlo jen z přebytku při stejné nádrži: dovoz 5 232 GWh, ztráty 36,0 GWh, pokles špičky po plynu 2 / 1 MW.

**Citlivost na předpověď.** Když hladinu místo předpovědi určí včerejší křivka, tedy jen známá informace, pokles špičky po plynu je ve výchozím nastavení 28 / 27 MW a při elektrolyzéru mimo prosinec až únor 56 / 0 MW, ztráty 59,2 GWh. V roce se studeným náhlým dnem nepředvídaná špička zůstane. Chyba skutečné předpovědi leží mezi oběma případy.

**Konzervativní cesta** baterii nemá. Stejné pravidlo by tam dalo 0,9 GWh, pokles zimní špičky 0 MW v mediánu a ztráty asi 17 GWh, v nejhorším roce pokles žádný.

### Elektrolyzér

Velikost určuje běh s elektrolyzérem mimo prosinec až únor, tabulka je z něj.

| Pravidlo | Baterie GWh | Elektrolyzér MW | Plné hodiny | Vývoz GWh | Vývoz z přebytku | Dovoz GWh | Přebytek do H2 GWh | Podíl přebytku na vodíku | Síť do H2 GWh |
|---|---|---|---|---|---|---|---|---|---|
| Vyrovnání dne | 0,0 | 308 | 6 710 | 57,2 | 17,1 % | 5 324 | 196 | 9,5 % | 1 870 |
| Vyrovnání dne | 0,0 | 314 | 6 582 | 55,1 | 16,5 % | 5 322 | 198 | 9,6 % | 1 868 |
| Vyrovnání dne | 0,0 | 550 | 3 758 | 9,0 | 2,7 % | 5 276 | 245 | 11,8 % | 1 822 |
| Vyrovnání dne | 0,0 | 631 | 3 275 | 4,1 | 1,2 % | 5 271 | 249 | 12,1 % | 1 817 |
| Vyrovnání dne | 0,0 | 1 000 | 2 067 | 0,1 | 0,0 % | 5 267 | 253 | 12,3 % | 1 813 |
| Vyrovnání dne | 2,6 | 308 | 6 710 | 13,3 | 4,0 % | 5 279 | 31 | 1,5 % | 2 035 |
| Vyrovnání dne | 2,6 | 314 | 6 582 | 12,9 | 3,9 % | 5 279 | 32 | 1,5 % | 2 035 |
| Vyrovnání dne | 2,6 | 550 | 3 758 | 3,3 | 1,0 % | 5 269 | 41 | 2,0 % | 2 025 |
| Vyrovnání dne | 2,6 | 631 | 3 275 | 1,7 | 0,5 % | 5 268 | 43 | 2,1 % | 2 024 |
| Vyrovnání dne | 2,6 | 1 000 | 2 067 | 0,0 | 0,0 % | 5 266 | 45 | 2,2 % | 2 022 |
| Jen přebytek | 2,6 | 308 | 6 710 | 6,5 | 1,9 % | 5 237 | 19 | 0,9 % | 2 048 |
| Jen přebytek | 2,6 | 314 | 6 582 | 6,2 | 1,9 % | 5 237 | 19 | 0,9 % | 2 047 |
| Jen přebytek | 2,6 | 550 | 3 758 | 1,5 | 0,4 % | 5 232 | 24 | 1,2 % | 2 043 |
| Jen přebytek | 2,6 | 631 | 3 275 | 0,8 | 0,2 % | 5 231 | 25 | 1,2 % | 2 042 |
| Jen přebytek | 2,6 | 1 000 | 2 067 | 0,0 | 0,0 % | 5 231 | 26 | 1,2 % | 2 041 |

Potřeba flotily je 2 067 GWh a přebytek 334 GWh. Podíl přebytku na vodíku je 11,8 % bez baterie a 2,0 % s baterií. Vývoz pod 1 % nyní dává 550 MW a 631 MW už pravidlo nevyžaduje. 314 MW je nejmenší elektrolyzér, který dodá roční vodík bez výroby ze sítě v prosinci až únoru, a vyveze 12,9 GWh, 3,9 % přebytku. Přechod z 314 na 550 MW sníží vývoz o 9,6 GWh a dovoz o stejnou hodnotu, tedy 236 MW navíc za 41 h využití. Na 631 MW je to další 1,6 GWh. Hlavní cíl zůstává nevyvážet, proto výchozí hodnota 550 MW platí, jen ji žádné ekonomické měřítko nepodpírá. Nulový vývoz by stál 1 177 MW.

### Nádrž při pevné kapacitě

Baterie 2,6 GWh a 650 MW, elektrolyzér 550 MW, rovnoměrný odběr flotily. Výrobu rozvrhuje hodinový lineární program po jednotlivých letech s předvídáním: nejdřív co nejméně vývozu, potom co nejméně výroby ze sítě v prosinci až únoru, potom nižší zimní špička. Baterie pak vyrovnává to, co zbude. Ceny DOE MYRDD 2015 (500 a 600 USD/kg cíl, 850 USD/kg stav), bez údržby. Anuitní faktor 0,0963 je náš vlastní výběr bez zdroje.

| Nádrž | Výroba H2 v prosinci až únoru GWh | Bilance prosinec až únor GWh | Bilance říjen až březen GWh | Zimní špička dovozu MW, průměr / nejhorší rok | Vývoz GWh | Dovoz GWh | Mil. USD/rok při 500 | 850 |
|---|---|---|---|---|---|---|---|---|
| 0 t | 510 | −1 513 | −2 777 | 925 / 981 | 5,9 | 5 274 | 0,0 | 0,0 |
| 5 t | 509 | −1 516 | −2 782 | 935 / 982 | 5,1 | 5 278 | 0,2 | 0,4 |
| 10 t | 509 | −1 515 | −2 781 | 935 / 982 | 3,5 | 5 276 | 0,5 | 0,8 |
| 25 t | 508 | −1 512 | −2 776 | 932 / 983 | 0,7 | 5 268 | 1,2 | 2,0 |
| 50 t | 507 | −1 505 | −2 768 | 911 / 977 | 0,4 | 5 263 | 2,4 | 4,1 |
| 75 t | 506 | −1 504 | −2 764 | 897 / 968 | 0,0 | 5 263 | 3,6 | 6,1 |
| 100 t | 504 | −1 504 | −2 766 | 893 / 959 | 0,0 | 5 262 | 4,8 | 8,2 |
| 250 t | 496 | −1 498 | −2 764 | 865 / 921 | 0,0 | 5 261 | 12,0 | 20,5 |
| 500 t | 483 | −1 489 | −2 767 | 839 / 890 | 0,0 | 5 260 | 24,1 | 40,9 |
| 1 000 t | 456 | −1 463 | −2 766 | 809 / 859 | 0,0 | 5 259 | 48,1 | 81,9 |
| 2 500 t | 376 | −1 390 | −2 729 | 766 / 792 | 0,2 | 5 260 | 120,4 | 204,6 |
| 5 000 t | 243 | −1 266 | −2 622 | 765 / 789 | 0,2 | 5 261 | 240,8 | 409,3 |
| plná sezónní, 10 035 t | 3 | −1 030 | −2 429 | 781 / 794 | 0,6 | 5 266 | 483,2 | 821,4 |

Výchozí zůstává malá nádrž asi 50 t podle stejného pravidla: nejmenší vývoz je prakticky hotový do 50 t. Zimní špička klesá i dál, pomalu. Plná sezónní nádrž je asi 200krát větší a kupuje hlavně přesun výroby ze zimy do zbytku roku. Výhrady k malé nádrži: 50 t je asi 11 h spotřeby flotily, rozvrh zná celý rok a denní tankovací profil část nádrže spotřebuje.

## 5. Dvě zimní špičky a jejich smíření

**Stránka, zimní špička:** návrhový případ podle metody studie. Řádek × koeficient, kalibrováno na rok 2023. Vítr a slunce 0, SMR 0,95, plyn výkon × 0,9 bez ohledu na palivo, elektrolýza vypnutá.

**Hodinový model, špička prosince až února:** největší hodinové zatížení, případně dovoz, ve skutečném průběhu daného povětrnostního roku se skutečným větrem a sluncem a s plynem jen do ročního rozpočtu.

**Výsledek.** Zatížení v roce 2050: stránka 1 616 MW, hodinově medián 1 936 MW (rozsah 1 786 až 1 985 MW) v progresivní cestě, 1 226 a 1 424 MW v konzervativní. Tepelné čerpadlo má nyní 3,5 až 5,5 kW na odběrné místo v hodině svého maxima místo dřívějších 8,2 kW: běžná spotřeba 2,5 MWh z 8,9 MWh jde tvarem spotřebičů a v tuhých mrazech čerpadlo běží rovnoměrně. Terénní údaj 1,7 kW je z mírnější Británie a na −18 °C se nepřenáší. Koeficient čerpadel a přímotopů je nyní z hodinového modelu, tyto řádky se tedy shodují.

| Řádek, MW ve špičce | Stránka, progresivní | Hodinově, medián | Stránka, konzervativní | Hodinově, medián |
|---|---|---|---|---|
| vytápění tepelnými čerpadly | 639 | 644 | 295 | 291 |
| přímotopy | 0 | 0 | 243 | 245 |
| osobní auta | 132 | 211 | 26 | 42 |
| nákladní doprava | 48 | 93 | 23 | 37 |
| domácnosti bez vytápění | 60 | 84 | 60 | 86 |
| služby a veřejný sektor | 105 | 126 | 105 | 139 |
| Třinecké železárny | 139 | 177 | 104 | 132 |
| Nová huť | 66 | 84 | 66 | 84 |
| ostatní průmysl a chemie | 187 | 227 | 147 | 179 |
| ostatní energetika (přidaná položka) | 86 | 114 | 86 | 114 |
| vlastní spotřeba zdrojů | 47 | 53 | 22 | 25 |
| datacentra | 55 | 80 | 5 | 8 |

**Proč se smějí lišit.** Stránka kalibruje všechny řádky na metodu studie: zatížení 2025 je tam 1 169 MW. Stejné hodinové tvary dají na řádcích roku 2025 1 309 MW, rozsah 1 236 až 1 419 MW. Rozdíl je tedy z větší části ve stejném poměru už dnes a jde hlavně na ploché průmyslové řádky a na večerní nabíjení aut. Hodinové tvary jsou celostátní a poměr k měřené špičce kraje nelze ověřit, protože roční maximum zatížení MSK se nesleduje. Výsledek hodinového dovozu tedy není dolní mez, stránka není horní mez a obě čísla se uvádějí vedle sebe.

**Plyn.** Progresivní bloky mají 433 MW v hodinovém modelu i na stránce, palivo jen 115,2 GWh, tedy 266 h plného výkonu. Dříve z energie vycházelo 115 MW.

**Bilance s baterií na stránce.** Nikdy se nepřičítá celý výkon. Zimní bilance progresivní cesty 2050 je −656 MW; s baterií −514 MW při změřeném poklesu špičky 142 MW v mediánu a −601 MW při 55 MW v nejhorším povětrnostním roce. Čísla jsou před plynem, protože stránka počítá plyn plným výkonem. Konzervativní zimní bilance je −412 MW.

**Chlazení.** Stejná intenzita na stupeň ve všech letech a strop řádek / 500 h, tedy 384 MW v progresivní cestě. Dříve se každý rok přeškáloval na stejné GWh a chladné léto 2016 dalo 939 MW. Průměr 5 let sedí na řádek, jednotlivé roky se liší. Strop 500 h je úsudek.

**Odstávka SMR.** Předpoklad: plánovaná odstávka v jarním období s nejnižší zbytkovou špičkou, od poloviny dubna. Sken začátků přes 5 let dal nejnižší špičku v rozmezí začátků od poloviny dubna do května. Druhý blok od poloviny září. Roční špička dovozu už tak neleží v odstávce.

## 6. Soběstačnost: výchozí mix a podmínky

### Výchozí mix, řádky P50, průměr 5 let

| Cesta | SMR | Vodík | Výroba GWh | Spotřeba GWh | Roční bilance GWh | Výroba / spotřeba | Říjen až březen GWh | Prosinec až únor GWh | Hodiny bez dovozu | Největší dovoz v zimě MW, nejhorší rok | Největší dovoz za rok MW | Dovoz GWh | Přebytek bez využití GWh |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Progresivní | 0 | flotila na bateriích | 3 920 | 11 343 | −7 423 | 34,6 % | −3 996 | −2 090 | 2,8 % | 1 175 | 1 175 | 7 423 | 1 |
| Progresivní | 0 | 50/50, sezónní nádrž | 3 920 | 12 818 | −8 898 | 30,6 % | −4 301 | −1 967 | 0,2 % | 1 144 | 1 144 | 8 893 | 0 |
| Progresivní | 0 | 50/50, rovnoměrná výroba | 3 920 | 12 818 | −8 898 | 30,6 % | −4 729 | −2 452 | 0,8 % | 1 380 | 1 380 | 8 895 | 0 |
| Progresivní | 1 | flotila na bateriích | 7 862 | 11 653 | −3 791 | 67,5 % | −2 044 | −1 151 | 12,3 % | 822 | 822 | 3 827 | 34 |
| Progresivní | 1 | 50/50, sezónní nádrž | 7 862 | 13 128 | −5 266 | 59,9 % | −2 432 | −1 007 | 2,1 % | 747 | 747 | 5 269 | 3 |
| Progresivní | 1 | 50/50, rovnoměrná výroba | 7 862 | 13 128 | −5 266 | 59,9 % | −2 773 | −1 512 | 6,8 % | 980 | 980 | 5 265 | 7 |
| Progresivní | 2 | flotila na bateriích | 11 804 | 11 963 | −159 | 98,7 % | −298 | −194 | 44,9 % | 424 | 424 | 929 | 648 |
| Progresivní | 2 | 50/50, sezónní nádrž | 11 804 | 13 438 | −1 634 | 87,8 % | −761 | −183 | 16,7 % | 347 | 347 | 1 942 | 140 |
| Progresivní | 2 | 50/50, rovnoměrná výroba | 11 804 | 13 438 | −1 634 | 87,8 % | −995 | −541 | 25,6 % | 583 | 583 | 1 876 | 201 |
| Konzervativní | 0 | bez flotily na vodík | 3 956 | 8 244 | −4 287 | 48,0 % | −2 139 | −1 058 | 0,0 % | 543 | 543 | 4 287 | 0 |
| Konzervativní | 1 | bez flotily na vodík | 7 898 | 8 554 | −656 | 92,3 % | −323 | −160 | 0,4 % | 79 | 272 | 656 | 0 |
| Konzervativní | 2 | bez flotily na vodík | 11 840 | 8 864 | 2 976 | 133,6 % | 383 | 153 | 100,0 % | 0 | 0 | 0 | 1 010 |

Vodík vyrobený mimo kraj, polovina flotily zůstává na bateriích: výroba 7 862 GWh, spotřeba 11 061 GWh, bilance −3 199 GWh.

Roční bilance v tabulce počítá s celým rozpočtem plynu. Hodinový model pouští plyn jen při schodku. Bilance sezón počítá i přebytek, který v dané hodině nikdo nevzal. U jednoho SMR je v rovnováze odečtena jeho vlastní spotřeba, blok dá čistě 3 632 GWh, ne 3 942 GWh.

### Co by muselo platit

Přidaný výkon nad řádky tabulky, řádky P50, čistý po vlastní spotřebě. U úrovně 2 je výpočet hodinový, průměr 5 let, požadavek je bilance sezóny aspoň 0. Vítr na mezi znamená doplnit vítr do 2 014 MW a zbytek pokrýt jinak.

| Cesta | SMR výchozí | Vodík | Úroveň | Bilance teď GWh | Jen vítr, přidat MW | Jen FVE, přidat MWp | Jen SMR, přidat | Vítr na mezi 2 014 MW | Půl na půl |
|---|---|---|---|---|---|---|---|---|---|
| Progresivní | 1 | flotila na bateriích | rok | −3 791 | 1 562 | 4 072 | 1,04 | 1 391 MW větru, potom 446 MW FVE nebo 0,11 SMR | 781 MW + 2 036 MWp |
| Progresivní | 1 | flotila na bateriích | říjen až březen | −2 044 | 1 400 | 7 182 | 2 celé | 1 391 MW větru, potom 1 SMR |  |
| Progresivní | 1 | flotila na bateriích | prosinec až únor | −1 151 | 1 475 | 10 619 | 2 celé | 1 391 MW větru, potom 1 SMR |  |
| Progresivní | 1 | 50/50, sezónní nádrž | rok | −5 266 | 2 169 | 5 656 | 1,45 | 1 391 MW větru, potom 2 030 MW FVE nebo 0,52 SMR | 1 085 MW + 2 828 MWp |
| Progresivní | 1 | 50/50, sezónní nádrž | říjen až březen | −2 432 | 1 947 | 8 535 | 2 celé | 1 391 MW větru, potom 1 SMR |  |
| Progresivní | 1 | 50/50, sezónní nádrž | prosinec až únor | −1 007 | 1 823 | 10 826 | 2 celé | 1 391 MW větru, potom 1 SMR |  |
| Progresivní | 1 | 50/50, rovnoměrná výroba | rok | −5 266 | 2 169 | 5 656 | 1,45 | 1 391 MW větru, potom 2 030 MW FVE nebo 0,52 SMR | 1 085 MW + 2 828 MWp |
| Progresivní | 1 | 50/50, rovnoměrná výroba | říjen až březen | −2 773 | 1 883 | 9 695 | 2 celé | 1 391 MW větru, potom 1 SMR |  |
| Progresivní | 1 | 50/50, rovnoměrná výroba | prosinec až únor | −1 512 | 1 925 | 13 894 | 2 celé | 1 391 MW větru, potom 1 SMR |  |
| Progresivní | 0 | 50/50, sezónní nádrž | rok | −8 898 | 3 666 | 9 558 | 2,45 | 1 391 MW větru, potom 5 931 MW FVE nebo 1,52 SMR | 1 833 MW + 4 779 MWp |
| Progresivní | 0 | 50/50, sezónní nádrž | říjen až březen | −4 301 | 3 261 | 15 154 | 3 celé | 1 391 MW větru, potom 2 SMR |  |
| Progresivní | 0 | 50/50, sezónní nádrž | prosinec až únor | −1 967 | 3 052 | 19 632 | 3 celé | 1 391 MW větru, potom 2 SMR |  |
| Progresivní | 2 | 50/50, sezónní nádrž | rok | −1 634 | 673 | 1 755 | 0,45 | 1 391 MW větru, potom 0 MW FVE nebo 0,00 SMR | 337 MW + 878 MWp |
| Progresivní | 2 | 50/50, sezónní nádrž | říjen až březen | −761 | 709 | 2 771 | 1 celé | 1 391 MW větru, potom 0 SMR |  |
| Progresivní | 2 | 50/50, sezónní nádrž | prosinec až únor | −183 | 569 | 2 440 | 1 celé | 1 391 MW větru, potom 0 SMR |  |
| Konzervativní | 0 | bez flotily na vodík | rok | −4 287 | 1 766 | 4 605 | 1,18 | 1 918 MW větru, potom 0 MW FVE nebo 0,00 SMR | 883 MW + 2 303 MWp |
| Konzervativní | 0 | bez flotily na vodík | říjen až březen | −2 139 | 1 636 | 7 072 | 2 celé | 1 918 MW větru, potom 0 SMR |  |
| Konzervativní | 0 | bez flotily na vodík | prosinec až únor | −1 058 | 1 601 | 9 237 | 2 celé | 1 918 MW větru, potom 0 SMR |  |

**Konzervativní cesta a vítr.** Roční schodek 4 287 GWh zavře 1 766 MW větru, celkem 1 862 MW, uvnitř meze 2 014 MW. Tempo 72,8 MW za rok je 8,0krát největší přírůstek kraje. Hodinově: bilance říjen až březen 183 GWh, prosinec až únor 120 GWh, bez dovozu 23,3 % hodin, největší dovoz 439 MW, přebytek bez využití 704 GWh.

Hodinově s přidanými zdroji, progresivní cesta, flotila 50/50, sezónní nádrž:

| Mix | Roční bilance GWh | Říjen až březen GWh | Prosinec až únor GWh | Hodiny bez dovozu | Největší dovoz MW, nejhorší rok | Dovoz GWh | Přebytek bez využití GWh |
|---|---|---|---|---|---|---|---|
| 1 SMR, vítr na mez 2 014 MW | −2 057 | −715 | −243 | 19,45 % | 635 | 2 457 | 400 |
| 3 SMR | 1 448 | 677 | 292 | 100,00 % | 0 | 0 | 1 448 |
| 5 SMR | 8 591 | 3 917 | 2 276 | 100,00 % | 0 | 0 | 8 591 |
| 3 SMR, vítr na mez 2 014 MW | 4 742 | 2 799 | 1 413 | 100,00 % | 0 | 0 | 4 742 |
| 3 SMR, vítr na mez, 3 GWp FVE | 7 528 | 3 689 | 1 754 | 100,00 % | 0 | 0 | 7 528 |

Vítr na mezi 2 014 MW, 1 SMR, kolik FVE navíc vyrovná bilanci:

| Vodík | Cíl | FVE navíc MWp | Roční bilance GWh | Říjen až březen GWh | Prosinec až únor GWh | Hodiny bez dovozu | Největší dovoz MW, nejhorší rok | Dovoz GWh | Přebytek bez využití GWh |
|---|---|---|---|---|---|---|---|---|---|
| 50/50, sezónní nádrž | říjen až březen | 2 445 | 129 | 0 | −35 | 31,4 % | 576 | 1 482 | 1 611 |
| 50/50, sezónní nádrž | prosinec až únor | 2 818 | 471 | 107 | 0 | 32,5 % | 559 | 1 411 | 1 881 |
| 50/50, sezónní nádrž | rok | 2 303 | 0 | −41 | −48 | 30,9 % | 581 | 1 512 | 1 512 |
| 50/50, rovnoměrná výroba | říjen až březen | 2 530 | 263 | 0 | −141 | 40,8 % | 809 | 2 061 | 2 324 |
| 50/50, rovnoměrná výroba | prosinec až únor | 3 825 | 1 448 | 373 | 0 | 43,1 % | 796 | 1 935 | 3 383 |
| 50/50, rovnoměrná výroba | rok | 2 241 | 0 | −83 | −172 | 40,1 % | 819 | 2 096 | 2 096 |
| flotila na bateriích | říjen až březen | 45 | −524 | 0 | −61 | 41,0 % | 711 | 1 722 | 1 198 |
| flotila na bateriích | prosinec až únor | 598 | −42 | 158 | 0 | 43,9 % | 700 | 1 548 | 1 506 |
| flotila na bateriích | rok | 646 | 0 | 171 | 5 | 44,1 % | 699 | 1 537 | 1 537 |

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
| Tabulka, progresivní | 623 MW | 23,3 MW | 2,6 × | 0,44 % | 1 678 MWp | 54,8 MWp | 0,7 × | 0,41 % |
| Půl na půl pro úroveň 1, flotila 50/50 | 1 708 MW | 66,6 MW | 7,3 × | 1,26 % | 4 506 MWp | 167,9 MWp | 2,0 × | 1,22 % |
| Vítr na mezi a zbytek FVE, flotila 50/50 | 2 014 MW | 78,9 MW | 8,7 × | 1,49 % | 3 708 MWp | 136,0 MWp | 1,6 × | 0,99 % |
| Jen FVE, flotila 50/50 | 623 MW | 23,3 MW | 2,6 × | 0,44 % | 7 334 MWp | 281,1 MWp | 3,4 × | 2,03 % |

## 7. Monte Carlo

Běhy losují řádky od P10 do P90 se společnými faktory, obrácenými znaménky a jedním rokem pro položky stejné události. Rok událostí závislých na povolování jde s faktorem povolování. Vlastní spotřeba a ztráty se v každém běhu počítají z losovaných řádků. Roční úroveň má 60 000 běhů, hodinové úrovně 2 000 běhů.

**SMR.** Dřív se bez SMR ocitlo 26 % běhů, protože P90 roku spuštění byl úsudkem 2055. Takový podíl říká něco o jednom odhadnutém roce, ne o projektu. Teď je SMR samostatný případ: progresivní cesta SMR podle své definice má, los mění jen výkon a rok do 2050, a případ bez SMR se uvádí zvlášť. Pravděpodobnost, že SMR nebude, tento výpočet nepřisuzuje.

| Případ | Úroveň 1: rok | Úroveň 2: říjen až březen | Úroveň 2: prosinec až únor | Úroveň 3: žádná hodina s dovozem | Roční bilance P10 / P50 / P90 GWh | Hodiny bez dovozu, medián (P10 až P90) | Největší dovoz MW, medián (P10 až P90) |
|---|---|---|---|---|---|---|---|
| Progresivní, 1 SMR, flotila 50/50, sezónní nádrž | pod 10 % | pod 10 % | pod 10 % | pod 1 % | −8 167 / −4 711 / −913 | 3,5 % (0 % až 19 %) | 723 (385 až 1 136) |
| Progresivní, 1 SMR, flotila 50/50, rovnoměrná výroba | pod 10 % | pod 10 % | pod 5 % | pod 1 % | −8 201 / −4 735 / −880 | 10,2 % (1 % až 32 %) | 919 (498 až 1 361) |
| Progresivní, 1 SMR, flotila na bateriích | pod 25 % | pod 25 % | pod 10 % | pod 1 % | −5 966 / −3 185 / 52 | 16,0 % (4 % až 41 %) | 753 (406 až 1 127) |
| Progresivní, bez SMR, flotila 50/50, sezónní nádrž | pod 1 % | pod 1 % | pod 1 % | pod 1 % | −11 673 / −8 209 / −4 382 | 0,4 % (0 % až 7 %) | 1 103 (675 až 1 543) |
| Progresivní, bez SMR, flotila na bateriích | pod 1 % | pod 1 % | pod 1 % | pod 1 % | −9 444 / −6 679 / −3 449 | 5,4 % (0 % až 18 %) | 1 118 (718 až 1 531) |
| Progresivní, 2 SMR, flotila 50/50, sezónní nádrž | 25 až 50 % | 25 až 50 % | 25 až 50 % | pod 25 % | −4 733 / −1 216 / 2 629 | 20,3 % (5 % až 100 %) | 349 (0 až 788) |
| Progresivní, 2 SMR, flotila na bateriích | 50 až 75 % | 25 až 50 % | 25 až 50 % | pod 10 % | −2 537 / 294 / 3 558 | 47,8 % (20 % až 100 %) | 386 (22 až 738) |
| Konzervativní, bez SMR | pod 1 % | pod 1 % | pod 1 % | pod 1 % | −6 550 / −4 312 / −2 071 | 0,0 % (0 % až 0 %) | 641 (341 až 1 000) |
| Konzervativní, 1 SMR navíc proti cestě | 25 až 50 % | 25 až 50 % | 25 až 50 % | pod 5 % | −3 053 / −815 / 1 432 | 1,9 % (0 % až 99 %) | 349 (77 až 701) |
| Konzervativní, 2 SMR navíc proti cestě | nad 90 % | nad 90 % | nad 90 % | 50 až 75 % | 386 / 2 703 / 4 996 | 100,0 % (59 % až 100 %) | 0 (0 až 344) |

**Citlivost podílu na neověřených volbách**, úroveň 1, podíl běhů:

| Varianta | Progresivní, 1 SMR, 50/50 | Progresivní, 1 SMR, na bateriích | Progresivní, bez SMR | Progresivní, 2 SMR | Konzervativní | Konzervativní, 1 SMR |
|---|---|---|---|---|---|---|
| korelace 0,6, základ | 5,9 % | 10,5 % | 0,3 % | 34,0 % | 0,6 % | 32,5 % |
| korelace 0 | 0,8 % | 3,9 % | 0,0 % | 26,5 % | 0,0 % | 26,8 % |
| korelace 0,3 | 3,0 % | 7,1 % | 0,1 % | 30,9 % | 0,2 % | 29,8 % |
| korelace 0,9 | 8,5 % | 13,1 % | 0,7 % | 35,4 % | 1,2 % | 34,3 % |
| bez losů mimo P10 až P90 | 2,3 % | 6,2 % | 0,0 % | 32,1 % | 0,0 % | 29,8 % |

Rozsah je 0,8 % až 8,5 % u progresivní cesty s 1 SMR a flotilou 50/50 a 0,0 % až 1,2 % u konzervativní. Proto se uvádí pásmo: progresivní pod 10 %, konzervativní pod 5 %. Medián součtu se od součtu P50 liší, protože řádky jsou nesymetrické.

## 8. Co v modelu chybělo

Doplněno jako případy na běhu s rovnoměrnou elektrolýzou bez nádrže, ne na výchozím nastavení. Hodnoty jsou průměr 5 let, v závorce rozsah let.

| Případ | Cesta | Dovoz GWh | Přebytek GWh | Zimní špička dovozu MW | Hodin nad 800 / 1 000 / 1 200 MW |
|---|---|---|---|---|---|
| rovnoměrná elektrolýza, bez nádrže | Progresivní | 5 265 (5 210 až 5 316) | 125 | 925 (900 až 981) | 1 928 / 0 / 0 |
| elektrolýza mimo prosinec až únor, sezónní nádrž | Progresivní | 5 269 (5 217 až 5 319) | 334 | 696 (669 až 747) | 0 / 0 / 0 |
| výpadek SMR v nejhorší zimní hodině | Progresivní | 5 265 (5 210 až 5 316) | 125 | 1 425 (1 400 až 1 481) | 1 928 / 0 / 0 |
| elektromobily a kamiony nabíjené přes den | Progresivní | 5 247 (5 190 až 5 298) | 26 | 912 (889 až 968) | 1 825 / 0 / 0 |
| polovina tepla čerpadel posunutá do 4 h | Progresivní | 5 265 (5 210 až 5 316) | 125 | 925 (900 až 981) | 1 930 / 0 / 0 |
| teplo čerpadel o 10 % méně, mírnější zimy | Progresivní | 5 183 (5 128 až 5 234) | 128 | 908 (882 až 963) | 1 791 / 0 / 0 |
| teplo čerpadel o 21 % méně, mírnější zimy | Progresivní | 5 093 (5 038 až 5 144) | 131 | 891 (865 až 945) | 1 604 / 0 / 0 |
| skutečný rok FVE a tepla, ne průměr | Progresivní | 5 265 (5 085 až 5 392) | 123 | 926 (900 až 1 003) | 1 925 / 189 / 0 |
| tvar větru ze stanice Brno místo celostátního | Progresivní | 5 312 (5 252 až 5 357) | 238 | 959 (942 až 983) | 2 279 / 0 / 0 |
| výchozí nastavení | Konzervativní | 4 287 (4 238 až 4 331) | 0 | 508 (484 až 543) | 0 / 0 / 0 |

**Co model neumí**, každý řádek s velikostí:

- **Přiměřenost, LOLE.** Bez sazby výpadků ze zdroje se nepočítá. Místo toho hodiny dovozu nad 800, 1 000 a 1 200 MW v nejhorším roce: 2 066, 7 a 0, roční špička 1 060 MW. Se skutečným rokem fotovoltaiky a tepla a rovnoměrnou elektrolýzou je v nejhorším roce 945 hodin nad 1 000 MW.
- **Mez sítě a dovozu.** Transformační kapacita kraje nebyla zjištěna. Není mez, není počet nedodaných hodin. Velikost určují hodiny výše.
- **Dostupnost dovozu ze sousedů.** Regionální dovoz předpokládá přiměřenost státu. Standard je 15 h nedodávky za rok, Vnitrostátní plán s.75. Velikost pro kraj neznámá.
- **Řízené nabíjení aut.** Nabíjení přes den při rovnoměrné elektrolýze: přebytek 26 proti 125 GWh, zimní špička 912 proti 925 MW. Skutečné pravidlo podle ceny není modelované.
- **Auta jako zásobník.** Výkon = auta × připojený podíl × kW, velikost zcela závisí na předpokladech, nepočítá se.
- **Teplárny a teplo.** Nové plynové bloky běží na špičku, studie je vede teplem. Účinek: hodiny plynu; v energii omezený rozpočtem 115,2 GWh.
- **Ocel na vodíku.** 3,48 MWh/t (Vogl a kol. 2018) proti 0,45 MWh/t: 1,5 mil. t by přidalo asi 4,5 TWh, řádově celý schodek.
- **Biometan.** Bez řádku. Měřítko 340 až 930 GWh, pokud by ho kraj neměl použít jinde. Studie počítá s vtláčením do sítě, ne s výrobou elektřiny.
- **Výroba v průmyslu.** Biocel, Třinec zčásti v řádcích. Velikost bez dat provozovatelů neznámá.
- **Regulace FVE.** Omezení výroby je jen vývoz, 0,4 GWh, zanedbatelné.
- **Ceny.** Hodiny plynu jsou předpoklad, ne výsledek ceny. Bez pružnosti poptávky. Rozhoduje o tom, zda je plynová cesta vůbec věrohodná.
- **Rezervy.** Největší blok 500 MW jde do státní rezervy. Účinek na energii žádný.
- **Klima a voda.** Řádek 55 GWh, účinek klimatu asi ±10 GWh, zanedbatelné.
- **Meziroční vítr.** Skutečné roky FVE a tepla mění dovoz 5 085 až 5 392 GWh. Vítr je v tom normovaný, celostátní index míchá výkon a větrnost. Tvar z Brna dá při rovnoměrné elektrolýze přebytek 238 proti 125 GWh.


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
| Vodík 55,1 kWh/kg místo 51,36 kWh/kg | 150,6 | 0,0 | 38812 t ročně |
| Datacentra drží 361,4 GWh od 2040, nerostou na 700,8 | −351,9 | −35,2 |  |
| Datacentra žádná | −726,6 | −72,7 |  |
| Druhý SMR | −3 631,9 | 0,0 | bez podkladu; v konzervativní cestě by to byl první |
| První SMR v konzervativní cestě | 0,0 | −3 631,9 | bez podkladu |
| Míra ztrát roste se zátěží, 30 % stálé a 70 % proměnné | 311,3 | 42,5 | rozdělení bez zdroje, bez zesílení sítě |
| Nová huť na 80 % výkonu | −139,9 | −139,9 |  |
| Nová huť se nepostaví | −699,8 | −699,8 |  |
| Třinec 450 kWh/t místo 300 | 404,4 | 202,2 |  |
| Třinec 180 kWh/t, tiskový údaj | −323,4 | −161,7 |  |
| Biometan 635 GWh na blocích, dřívější odvození | −635,0 | 0,0 | studie pro kraj číslo nedává |
| Vodík flotily vyrobený mimo kraj | −2 066,6 | 0,0 |  |
| Flotila celá na bateriích | −1 475,1 | 0,0 |  |

**Otevřené body bez rozhodnutí.** Biometan: dřívější odvození počítalo 866 GWh na 433 MW a 2 000 h, řádek syntetického plynu dával 231 GWh, zbylých 635 GWh nemělo řádek. Studie popisuje přestavbu bioplynových stanic na biometan a vtláčení do sítě, pro výrobu elektřiny v kraji číslo nedává, proto řádek nepřibyl. Syntetický plyn: elektřina na jeho výrobu není vyčíslena, studie ji uvádí jako vysokou. Uzel plynu 2035. Stanice flotily a tankovací profil.

## 10. Kontrola závěrů

**Které změny bez důkazu schodek zvětšují a které zmenšují?** Změny, které schodek zvětšují: Třinec 300 kWh/t (úsudek mezi 180 a 450 kWh/t), syntetický plyn (studie, ale jiná technologie), komprese (měření). Změny, které ho zmenšují: vlastní spotřeba podle vzorce, konzervativní ztráty, úspory, kotle. Nejslabší je Třinec a ztráty. Míra ztrát rostoucí se zátěží by přidala 311 GWh progresivní a 42 GWh konzervativní cestě, ale 30/70 nemá zdroj a vyšší zátěž by šla se zesílením sítě, proto je jen mezi rozhodnutími. Konzervativní cesta z toho profituje o rozdíl mezi 6,03 % a 3,547 %, tedy asi 190 GWh, a je třeba to říct: její dřívější vyšší ztráty byly mechanickým čtením dvojnásobné zátěže. Nové pravidlo baterie výrok neovlivní, roční bilance se mění o ztráty.

**Nezlepšují hodiny závěr?** Rozšíření mezí řádku o hodiny P10 a P90 měří tabulka:

| Cesta | Varianta | Vodík | Úroveň 1, podíl | Medián GWh | P90 GWh |
|---|---|---|---|---|---|
| Progresivní | základ | 50/50 | 6,1 % | −4 690 | −833 |
| Progresivní | základ | na bateriích | 11,0 % | −3 172 | 155 |
| Progresivní | meze řádků jen při 942 h a 2 471 h, vítr P10 2 014,8 h | 50/50 | 4,9 % | −4 874 | −1 101 |
| Progresivní | meze řádků jen při 942 h a 2 471 h, vítr P10 2 014,8 h | na bateriích | 8,7 % | −3 353 | −191 |
| Konzervativní | základ | na bateriích | 0,6 % | −4 313 | −2 056 |
| Konzervativní | meze řádků jen při 942 h a 2 471 h | na bateriích | 0,5 % | −4 325 | −2 095 |

Zvolené meze hodin zvyšují podíl splněných běhů nejvýš o několik procentních bodů, výrok nemění.

Je flotila započítaná dvakrát? Ne. Bateriová a vodíková část nákladní dopravy dávají dohromady 996,8 mil. km (po 50 %), MHD 21,547 mil. km a auta mají vodík 0. Řádky vodíku se v hodinovém modelu nepočítají do bateriové zátěže. Zbývá možný překryv 45,8 GWh.

### Zpětná kontrola metody

| Test | Výsledek |
|---|---|
| Čistá spotřeba 2015 na 2025, držení hodnoty 2015 | předpoklad 5 910,4 GWh, skutečnost 5 963,8 GWh, chyba −0,9 % |
| Výroba 2015 na 2025, držení hodnoty 2015 | předpoklad 6 794,1 GWh, skutečnost 2 805,2 GWh, chyba 142,2 %. V datech roku 2015 uzavírání parních zdrojů není, metoda by ho musela dostat jako datovanou událost |
| Pozorované změny, čistá spotřeba, 2014 až 2025 | za 5 let −8,3 až 12,3 %, za 10 let 0,9 až 3,5 % |
| Šířka P10 až P90 modelu, čistá spotřeba, po 10 letech (2035) | progresivní 26,7 %, konzervativní 25,6 % mediánu |
| Pozorované změny, výroba, 2014 až 2025 | za 5 let −47,2 až −21,7 %, za 10 let −58,7 až −52,4 % |
| Šířka P10 až P90 modelu, výroba, po 10 letech (2035) | progresivní 73,8 %, konzervativní 53,5 % mediánu |
| Pokryje pásmo výroby změnu, kterou kraj zažil? | Ne pro výrobu: pokles −58,7 % za 10 let je větší než polovina šířky pásma. Spotřebu pásmo pokrývá |
| Mimo vzorek: spotřeba sektorů, 1. pololetí 2026 proti 2025, ERÚ tab. 6.3 | změřeno −10,6 GWh za pololetí; křivka za celý rok −64,0 GWh progresivní, −66,6 GWh konzervativní |
| Mimo vzorek: výroba, 1. pololetí 2026 proti 2025, ERÚ tab. 6.1 | změřeno −334,9 GWh za pololetí; křivka za celý rok −307,1 GWh progresivní, −299,7 GWh konzervativní |

### Kontroly

| Kontrola | Hodnota |
|---|---|
| hodinový běh proti hodinový model, největší rozdíl MW | 0,000 |
| progresivni: výroba minus spotřeba P50 proti tabulce GWh | 0,002 |
| konzervativni: výroba minus spotřeba P50 proti tabulce GWh | 0,002 |
| progresivni vyroba: medián společného losování proti model stránky GWh | 0,048 |
| progresivni vyroba: šířka P10 až P90 proti model stránky GWh | 0,014 |
| progresivni spotreba: medián společného losování proti model stránky GWh | 0,017 |
| progresivni spotreba: šířka P10 až P90 proti model stránky GWh | 0,028 |
| konzervativni vyroba: medián společného losování proti model stránky GWh | 0,044 |
| konzervativni vyroba: šířka P10 až P90 proti model stránky GWh | 0,066 |
| konzervativni spotreba: medián společného losování proti model stránky GWh | 0,045 |
| konzervativni spotreba: šířka P10 až P90 proti model stránky GWh | 0,001 |

Další kontroly: křivky stránky proti modelu, součty po letech proti tabulce a test logiky stránky procházejí. Hodinové kontroly 29 z 29 v pořádku, včetně hodinové bilance pod 0,1 GWh a toho, že baterie nezvedla denní špičku. Roční bilance tabulky a hodinového výpočtu se liší o 0,07 GWh v progresivní a 0,00 GWh v konzervativní cestě.

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
