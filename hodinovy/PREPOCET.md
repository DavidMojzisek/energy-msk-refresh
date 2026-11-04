# Přepočet bilance MSK 2050: hodiny, flotila, křivky a soběstačnost

Stav k 2026-11-04. Výpočet stojí na tabulce položek a hodinovém modelu pro 5 povětrnostních let 2015 až 2019. Soběstačnost znamená jen elektřinu vyrobenou v kraji. Palivo pro SMR a zemní plyn je dovezené i tehdy, když je bilance elektřiny kladná. Výchozí nastavení: baterie 3 GWh a 750 MW, elektrolyzér 631 MW, malá nádrž asi 50 t, flotila MHD 50 %, nákladní doprava 50 %, auta 0 %. Malá nádrž se v zimní bilanci chová jako rovnoměrná výroba, proto zimní čísla výchozího nastavení jsou z řádků rovnoměrné výroby.

## 1. Odpověď

**Kraj zůstane v roce 2050 závislý na dovozu elektřiny.** Platí to pro obě cesty a pro všechny tři úrovně, pokud nepřibudou elektrárny, které žádný podklad nedokládá. Progresivní cesta ve výchozím mixu vyrobí 7 978 GWh a spotřebuje 12 922 GWh, tedy 61,7 %. Chybí 4 944 GWh. Konzervativní cesta vyrobí 4 072 GWh ze 8 287 GWh, tedy 49,1 %, a chybí 4 214 GWh.

Podíl běhů Monte Carlo, které danou úroveň splní. Běhy losují řádky od P10 do P90 se společnými faktory, obrácenými znaménky a rokem SMR, jako model stránky. Roční úroveň má 60 000 běhů, hodinové úrovně 5 000 běhů.

| Případ | Úroveň 1: rok | Úroveň 2: říjen až březen | Úroveň 2: prosinec až únor | Úroveň 3: žádná hodina s dovozem | Hodiny bez dovozu, medián (P10 až P90) | Největší dovoz MW, medián (P10 až P90) |
|---|---|---|---|---|---|---|
| Progresivní, rok SMR podle losování, flotila 50/50, sezónní nádrž | 4,3 % | 4,6 % | 3,3 % | 0,0 % | 3,2 % (0 % až 20 %) | 1 611 (1 053 až 2 301) |
| Progresivní, rok SMR podle losování, flotila 50/50, rovnoměrná výroba | 4,3 % | 4,7 % | 3,0 % | 0,0 % | 12,1 % (0 % až 45 %) | 1 830 (1 217 až 2 577) |
| Progresivní, rok SMR podle losování, flotila na bateriích | 8,3 % | 7,9 % | 5,3 % | 0,0 % | 20,1 % (3 % až 56 %) | 1 695 (1 126 až 2 402) |
| Progresivní, bez SMR, flotila 50/50, sezónní nádrž | 0,1 % | 0,1 % | 0,1 % | 0,0 % | 0,4 % (0 % až 6 %) | 1 872 (1 327 až 2 539) |
| Progresivní, bez SMR, flotila na bateriích | 0,2 % | 0,2 % | 0,1 % | 0,0 % | 6,7 % (0 % až 24 %) | 1 949 (1 364 až 2 621) |
| Progresivní, 1 SMR jistě do 2050, flotila 50/50, sezónní nádrž | 5,3 % | 5,7 % | 4,5 % | 0,0 % | 5,5 % (1 % až 23 %) | 1 511 (1 001 až 2 208) |
| Progresivní, 1 SMR jistě do 2050, flotila na bateriích | 10,4 % | 9,2 % | 6,5 % | 0,0 % | 25,6 % (8 % až 58 %) | 1 603 (1 066 až 2 282) |
| Progresivní, 2 SMR, flotila 50/50, sezónní nádrž | 41,4 % | 40,9 % | 39,3 % | 0,9 % | 26,8 % (9 % až 97 %) | 999 (430 až 1 690) |
| Progresivní, 2 SMR, flotila na bateriích | 65,4 % | 61,6 % | 53,8 % | 0,8 % | 74,1 % (40 % až 95 %) | 1 096 (530 až 1 798) |
| Konzervativní, bez SMR | 0,5 % | 0,3 % | 0,3 % | 0,4 % | 0,0 % (0 % až 0 %) | 892 (342 až 1 590) |
| Konzervativní, 1 SMR navíc proti cestě | 41,1 % | 37,6 % | 30,2 % | 8,9 % | 5,4 % (0 % až 100 %) | 617 (29 až 1 345) |
| Konzervativní, 2 SMR navíc proti cestě | 97,1 % | 96,2 % | 94,3 % | 39,8 % | 99,9 % (92 % až 100 %) | 123 (0 až 851) |

V losovaném roku SMR nemá 26 % běhů v roce 2050 žádný blok.

**Rozpětí roční bilance progresivní cesty, flotila 50/50:** P10 −9 701, medián −5 371, P90 −1 303 GWh. I P90 je záporné. Medián je horší než součet P50, protože 26 % běhů SMR nestihne.

**Výrok.** Ročně je soběstačnost možná jen tehdy, když do roku 2050 stojí 3 SMR, nebo 1 SMR, vítr na mezi studie 2 014 MW a 1,6 GWp FVE navíc. V zimě to s malou nádrží nejde bez druhého a třetího SMR, nebo bez druhého SMR a větru na mezi, nebo bez větru na mezi a 3,3 GWp FVE navíc. S plnou sezónní nádrží by stačilo 2,7 GWp. Poslední varianta vyrovná bilanci prosince až února jen na papíře: dovoz zůstane 1 569 GWh ročně a 1 505 MW ve špičce, a 3 135 GWh přebytku nikdo nevezme. Hodinově je kraj skoro bez dovozu až při 3 SMR. Druhý a další SMR v kraji žádný podklad neuvádí a větrná varianta žádá tempo výstavby asi 9krát nad maximem kraje. Důkaz rozhoduje směr, ne přesnou velikost mezery. Podrobně v oddílu 5.

## 2. Bilance

| Cesta | Veličina, GWh | 2026 | 2030 | 2040 | 2050 |
|---|---|---|---|---|---|
| Progresivní | Výroba | 2 624 | 2 973 | 4 351 | 7 978 |
| Progresivní | Spotřeba | 7 050 | 7 535 | 9 763 | 12 922 |
| Konzervativní | Výroba | 2 632 | 3 333 | 3 139 | 4 072 |
| Konzervativní | Spotřeba | 7 090 | 7 296 | 8 091 | 8 287 |

Bilance 2050: progresivní −4 944,2 GWh, konzervativní −4 214,4 GWh. Proti tabulce před tímto přepočtem je u progresivní cesty výroba o 353,8 GWh nižší a spotřeba o 1 313,5 GWh vyšší. Výrobu snižují změřené hodiny FVE a větru. Spotřebu zvedá návrat flotily na 50/50 a baterie 3 GWh.

Zimní špička 2050: progresivní −1 141,7 MW, konzervativní −513,0 MW. Letní poledne před pružnými zátěžemi: progresivní 491,3 MW, konzervativní −541,7 MW.

## 3. Co se změnilo v tabulce a křivkách

**Hodiny.** FVE 942 h (P10 889, P90 995, odhad), vítr 2 471 h (P10 2 184, P90 2 810), stejné MW. Řádek P10 je MW z P10 krát hodiny P10, řádek P90 obdobně. Mez P10 a P90 tedy skládá nejistotu výkonu a počasí jednoho roku.

**Flotila.** MHD 50 %, nákladní doprava 50 %, auta 0 %. Řádek nákladní dopravy je zpět na 558,6 GWh, vodík pro nákladní dopravu 1 925,0 GWh, pro MHD 34,6 GWh. Řádek krát 2 dává flotilu na bateriích 1 117,2 GWh.

**Ztráty v sítích.** Řádek je podle svého odvození vzorec ze součtu spotřeby, proto je 426,4 GWh místo 380,3 GWh. Bez toho by hodinový model tiše snížil míru ztrát. Přírůstek ztrát baterií o 13,0 GWh je v řádku ponechán stranou, vzorec by dal o 0,5 GWh víc. Míra v hodinovém modelu je 3,673 %.

**Křivky.** Tabulka u každého řádku říká, který tvar řádek má. Hodnoty 2050 jsou beze změny.

| Tvar | Řádky |
|---|---|
| Monotónní interpolace přes milníky (Fritsch a Carlson 1980, doi 10.1137/0717021) | biomasa, bioplyn, malé vodní, vlaky, FVE střešní a pozemní, chlazení, ztráty v sítích, nové plynové bloky, vlastní spotřeba, obě cesty; elektrokotle, tepelná čerpadla a ostatní průmysl jen konzervativní |
| Stejná interpolace s rokem zahájení projektů | ostatní průmysl progresivní: 18,0; 89,0; 105,0; 143,2 GWh v letech 2026 až 2029 z Tab.41 a 42 studie, s.173-174, v roce 2030 plných 420,3 GWh |
| Tvrdý kalendářní skok | Dětmarovice, doly, obě cesty |
| Dva stupně | Třinec a hutní plyny, progresivní: 2033 a 2045. Rok 2045 je odhad, střed intervalu 2040 až 2050 |
| Logistika zůstává | řádky, které milníky procházejí, a řádky, které vzrostou a klesnou (stávající kogenerace, MHD progresivní, domácnosti) |

Nové plynové bloky v konzervativní cestě mají uzly jen 2030, 2040 a 2050. Tab.30 s.132 dává pro 2035 výkon 683 MW, ne energii, a uzel v GWh by v roce 2040 vyžadoval pokles. Zimní výkon z fixního koeficientu proto zůstává v roce 2035 podhodnocený, odhad je asi 243 MW.

**Rok 2026 proti změřenému 1. pololetí 2026.** Jedno pololetí, bez očištění o počasí.

| Veličina, změna proti 2025, GWh | Změřeno v 1. pololetí | Křivka dříve | Křivka teď | Rozdíl dříve | Rozdíl teď |
|---|---|---|---|---|---|
| Spotřeba sektorů, progresivní | −10,6 | +337,8 | −19,6 | +348,3 | −9,0 |
| Spotřeba sektorů, konzervativní | −10,6 | +100,5 | +19,5 | +111,1 | +30,1 |
| Výroba, progresivní | −334,9 | −84,2 | −180,7 | +250,6 | +154,2 |
| Výroba, konzervativní | −334,9 | −56,1 | −173,1 | +278,8 | +161,8 |

Sloupec Změřeno je změna za pololetí v GWh, křivka je změna za celý rok, proto rozdíl v GWh výrobě lichotí: změřené pololetí je −20,6 %, křivka progresivní cesty za rok −6,4 %. Spotřeba teď sedí v mezích tohoto testu, jedno pololetí to ale nepotvrzuje. Výroba sedí lépe, ne dobře. Dětmarovice už v roce 2026 jsou celé pryč. Zbytek rozdílu dělají hlavně nové plynové bloky, u nichž se křivka v roce 2026 proti dřívějšku zhoršila (+108,2 GWh proti +50,5 GWh progresivní, +189,9 GWh proti +143,8 GWh konzervativní), protože milník 2030 je dán tabulkou a v roce 2026 žádný takový blok neběží, a FVE (+74,1 GWh), jejíž druhé pololetí test nevidí. Plynové bloky by potřebovaly vlastní rok spuštění, model ho zatím nemá.

**Pásmo 2030.** Pravidlo: šířka P10 až P90 spotřeby v roce 2030 nesmí být menší než pozorované rozpětí pětileté změny čisté spotřeby 2014 až 2025, tedy 20,6 procentního bodu (−8,3 % až +12,3 %). Je-li menší, odchylky od mediánu se vynásobí poměrem do roku 2030 a od 2030 do 2040 násobek klesá na 1. Hindcast to podporuje: násobek je 1,250 u konzervativní a 1,109 u progresivní cesty. Pravidlo platí pro obě cesty stejně, protože po nové křivce kleslo pod rozpětí i pásmo progresivní. Medián ani rok 2050 se nemění. Test je na celku a na 7 počátcích, jednotlivé položky hindcast neumožňují.

**Elektrolyzér.** Platí jedna definice: výkon = řádky vodíku flotily × (1 + míra ztrát sítě) × 1 000 / plné hodiny. Plné hodiny jsou z hodinového výpočtu (3 220 h, přebytek do sítě pod 1 %, baterie první, 3 GWh). Výsledek je 631 MW v tabulce, na stránce i v hodinovém výpočtu. Řádek 45,8 GWh ze studie je vodík mimo flotilu a běží jako rovnoměrná zátěž mimo tento výkon. Nulový vývoz by stál 1 173 MW.

**Možný překryv.** Řádek vodíku 45,8 GWh ze studie zůstává a sčítá se s flotilou, překryv je nejvýš 45,8 GWh, tedy 2,3 % vodíku flotily. Poznámka je v řádcích.

## 4. Hodinový výpočet, dnešní mix, 1 SMR

### Denní výkyv zbytkového zatížení

E_den = součet kladných odchylek od denního průměru / √0,88, výkon = největší hodinová odchylka. Spotřeba bez elektrolýzy minus neřízené zdroje včetně SMR, 1 825 dnů. Velikost je základ návrhu, ne nákladové optimum.

| Statistika | E_den GWh | Výkon MW | Baterie na mřížce GWh | Výkon E/4 MW | Pokryje mediánový výkon |
|---|---|---|---|---|---|
| Medián | 2,67 | 581 | 3,0 | 750 | ano |
| P90 | 4,47 | 808 | 5,0 | 1 250 | ano |
| P95 | 4,87 | 856 | 5,0 | 1 250 | ano |
| Maximum | 6,20 | 1 132 | 8,0 | 2 000 | ano |

Základem pásu je medián: 3,0 GWh a 750 MW, což pokryje mediánový výkon 581 MW. Při této velikosti baterie 99,4 cyklu za rok. Baterie se nabíjí jen z přebytku, kterého je 390 GWh za rok, takže výkyv neříká, kolik se ho skutečně vyrovná.

### Podle velikosti baterie

Baterie první, průměr 5 let. Noc je 18:00 až 06:00 v pevném čase SEČ. Kryté noci jsou podíl nocí se schodkem, plně / aspoň z poloviny.

| GWh | Cykly | Mezní cykly na GWh | Noc úspora 308 MW | 750 MW | Noci léto | Noci zima | Přebytek do H2 308 MW | 750 MW | Dovoz 308 MW | 750 MW | Vývoz 308 MW | 750 MW | Ztráty baterie GWh |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0,0 | 0 | n/a | 0 | 0 | 0,0 % / 0,0 % | 0,0 % / 0,0 % | 267 | 383 | 5 027 | 4 910 | 123 | 7 | 0,0 |
| 0,5 | 174 | 174 | 15 | 19 | 0,0 % / 0,4 % | 0,3 % / 0,7 % | 205 | 287 | 5 001 | 4 920 | 86 | 5 | 11,8 |
| 1,0 | 155 | 136 | 37 | 35 | 0,4 % / 1,3 % | 0,7 % / 1,9 % | 155 | 210 | 4 983 | 4 928 | 59 | 3 | 21,1 |
| 1,5 | 139 | 106 | 61 | 47 | 1,0 % / 3,2 % | 1,1 % / 4,0 % | 112 | 151 | 4 973 | 4 935 | 42 | 3 | 28,3 |
| 2,0 | 124 | 81 | 87 | 55 | 1,3 % / 5,2 % | 2,4 % / 5,5 % | 77 | 105 | 4 968 | 4 940 | 31 | 2 | 33,9 |
| 2,5 | 111 | 60 | 111 | 60 | 2,3 % / 7,8 % | 3,2 % / 6,5 % | 50 | 72 | 4 965 | 4 943 | 23 | 2 | 37,9 |
| 3,0 | 99 | 40 | 128 | 64 | 3,6 % / 11,6 % | 3,6 % / 7,8 % | 33 | 49 | 4 962 | 4 946 | 18 | 2 | 40,7 |
| 4,0 | 80 | 22 | 148 | 68 | 5,4 % / 15,2 % | 4,8 % / 9,0 % | 15 | 24 | 4 958 | 4 949 | 10 | 1 | 43,7 |
| 5,0 | 66 | 9 | 155 | 71 | 6,7 % / 15,7 % | 5,4 % / 9,5 % | 8 | 14 | 4 955 | 4 949 | 6 | 1 | 45,0 |
| 6,0 | 56 | 5 | 158 | 72 | 7,2 % / 16,0 % | 5,4 % / 9,6 % | 5 | 9 | 4 953 | 4 949 | 4 | 0 | 45,6 |
| 8,0 | 42 | 2 | 161 | 73 | 7,6 % / 16,2 % | 5,4 % / 9,7 % | 3 | 4 | 4 951 | 4 950 | 2 | 0 | 46,3 |
| 10,0 | 34 | 1 | 162 | 73 | 7,6 % / 16,5 % | 5,4 % / 9,8 % | 1 | 2 | 4 951 | 4 950 | 1 | 0 | 46,6 |
| 15,0 | 23 | 0 | 163 | 74 | 7,9 % / 16,6 % | 5,4 % / 9,8 % | 0 | 0 | 4 950 | 4 950 | 0 | 0 | 46,7 |
| 20,0 | 17 | 0 | 163 | 74 | 7,9 % / 16,6 % | 5,4 % / 9,8 % | 0 | 0 | 4 950 | 4 950 | 0 | 0 | 46,8 |

308 MW je nejmenší elektrolyzér, který dodá roční vodík bez výroby ze sítě v prosinci až únoru. Při 750 MW dovoz s baterií roste, protože baterie bere přebytek elektrolyzéru a ten pak bere ze sítě.

### Elektrolyzér, baterie první

| Baterie GWh | Pravidlo | Elektrolyzér MW | Plné hodiny | Vývoz GWh průměr | nejhorší rok | Dovoz GWh | Přebytek do H2 GWh | Síť do H2 GWh |
|---|---|---|---|---|---|---|---|---|
| 0,0 | pod 1 % vyvezeno, průměr 5 let | 805 | 2 524 | 3,9 | 7,6 | 4 907 | 386 | 1 646 |
| 0,0 | nulový vývoz | 1 354 | 1 500 | 0,0 | 0,0 | 4 903 | 390 | 1 642 |
| 1,5 | pod 1 % vyvezeno, průměr 5 let | 711 | 2 857 | 3,9 | 5,9 | 4 936 | 150 | 1 882 |
| 1,5 | nulový vývoz | 1 227 | 1 656 | 0,0 | 0,0 | 4 932 | 154 | 1 878 |
| 3,0 | pod 1 % vyvezeno, průměr 5 let | 631 | 3 220 | 3,9 | 5,9 | 4 948 | 47 | 1 985 |
| 3,0 | nulový vývoz | 1 173 | 1 732 | 0,0 | 0,0 | 4 944 | 51 | 1 981 |
| 5,0 | pod 1 % vyvezeno, průměr 5 let | 448 | 4 535 | 3,9 | 8,2 | 4 952 | 11 | 2 021 |
| 5,0 | nulový vývoz | 1 173 | 1 732 | 0,0 | 0,0 | 4 948 | 15 | 2 017 |

Potřeba flotily je 2 032 GWh elektřiny a přebytek jen 390 GWh. **Při baterii 3,0 GWh jde z přebytku do vodíku 47 GWh a ze sítě 1 985 GWh. Vodík je tedy z 98 % z dovozu, ne z přebytku.** Flotila 50/50 zvedá dovoz ze 3 532 GWh při flotile na bateriích na 4 948 GWh.

### Nádrž při pevné kapacitě

Baterie 3,0 GWh a 750 MW, elektrolyzér 631 MW, rovnoměrný odběr flotily. Výrobu rozvrhuje hodinový lineární program po jednotlivých letech s předvídáním: nejdřív co nejméně vývozu, potom co nejméně výroby ze sítě v prosinci až únoru, potom nižší zimní špička. Ceny DOE MYRDD 2015 (500 a 600 USD/kg cíl, 850 USD/kg stav), bez údržby. Anuitní faktor 0,0963 je náš vlastní výběr bez zdroje, stejný jako dříve.

| Nádrž | Plné hodiny | Výroba H2 v prosinci až únoru GWh | z toho ze sítě GWh | Bilance prosinec až únor GWh | Bilance říjen až březen GWh | Zimní špička dovozu MW, průměr / nejhorší rok | Vývoz GWh | Dovoz GWh | Zisk bilance na tunu GWh/t | Zisk špičky na tunu MW/t | Mil. USD/rok při 500 | 600 | 850 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 t | 3 220 | 501 | 500 | −1 486 | −2 637 | 1 499 / 1 725 | 23,5 | 4 968 | n/a | n/a | 0,0 | 0,0 | 0,0 |
| 5 t | 3 220 | 501 | 499 | −1 486 | −2 635 | 1 408 / 1 625 | 16,6 | 4 961 | −0,069 | 18,23 | 0,2 | 0,3 | 0,4 |
| 10 t | 3 220 | 500 | 499 | −1 487 | −2 636 | 1 348 / 1 560 | 12,0 | 4 956 | −0,170 | 15,06 | 0,5 | 0,6 | 0,8 |
| 25 t | 3 220 | 500 | 498 | −1 487 | −2 639 | 1 267 / 1 493 | 5,7 | 4 950 | −0,053 | 9,28 | 1,2 | 1,4 | 2,0 |
| 50 t | 3 220 | 498 | 496 | −1 488 | −2 642 | 1 267 / 1 493 | 3,9 | 4 948 | −0,053 | 4,64 | 2,4 | 2,9 | 4,1 |
| 75 t | 3 220 | 497 | 495 | −1 486 | −2 641 | 1 267 / 1 493 | 3,9 | 4 948 | −0,005 | 3,09 | 3,6 | 4,3 | 6,1 |
| 100 t | 3 220 | 496 | 494 | −1 483 | −2 641 | 1 267 / 1 493 | 3,9 | 4 948 | 0,021 | 2,32 | 4,8 | 5,8 | 8,2 |
| 250 t | 3 220 | 488 | 486 | −1 472 | −2 638 | 1 267 / 1 493 | 3,9 | 4 948 | 0,054 | 0,93 | 12,0 | 14,4 | 20,5 |
| 500 t | 3 220 | 475 | 473 | −1 457 | −2 634 | 1 267 / 1 493 | 3,9 | 4 948 | 0,057 | 0,46 | 24,1 | 28,9 | 40,9 |
| 1 000 t | 3 220 | 449 | 447 | −1 432 | −2 629 | 1 267 / 1 493 | 3,9 | 4 948 | 0,053 | 0,23 | 48,1 | 57,8 | 81,9 |
| 2 500 t | 3 220 | 370 | 368 | −1 362 | −2 594 | 1 267 / 1 493 | 3,9 | 4 948 | 0,050 | 0,09 | 120,4 | 144,4 | 204,6 |
| 5 000 t | 3 220 | 239 | 237 | −1 252 | −2 513 | 1 267 / 1 493 | 3,9 | 4 948 | 0,047 | 0,05 | 240,8 | 288,9 | 409,3 |
| plná sezónní, 10 543 t | 3 220 | 2 | 0 | −1 034 | −2 343 | 1 267 / 1 493 | 3,9 | 4 948 | 0,043 | 0,02 | 507,6 | 609,2 | 863,0 |

Výroba po měsících, průměr 5 let, GWh:

| Nádrž | I | II | III | IV | V | VI | VII | VIII | IX | X | XI | XII |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 t | 173 | 156 | 173 | 167 | 173 | 167 | 173 | 173 | 167 | 173 | 167 | 173 |
| 100 t | 173 | 153 | 175 | 166 | 176 | 164 | 172 | 173 | 166 | 173 | 171 | 170 |
| 250 t | 172 | 149 | 177 | 167 | 181 | 158 | 176 | 174 | 162 | 175 | 174 | 166 |
| 500 t | 172 | 141 | 181 | 169 | 188 | 146 | 183 | 170 | 163 | 176 | 181 | 161 |
| 1 000 t | 164 | 130 | 186 | 175 | 202 | 124 | 189 | 171 | 162 | 186 | 186 | 154 |
| 2 500 t | 125 | 97 | 202 | 218 | 222 | 66 | 188 | 183 | 183 | 208 | 192 | 148 |
| 5 000 t | 70 | 73 | 222 | 268 | 257 | 60 | 187 | 189 | 194 | 220 | 195 | 96 |
| plná sezónní | 0 | 2 | 232 | 306 | 296 | 73 | 215 | 226 | 227 | 257 | 198 | 0 |

**Kde přínos na tunu padá.** Zimní špička dovozu klesne celá už do 25 t, o 232 MW, což je rovnoměrný příkon elektrolyzéru. Dalších tun ji nesníží. Vývoz klesne na minimum do 50 t. Zimní energetická bilance je jiná věc: roste skoro lineárně asi o 0,05 GWh na tunu až do plné sezónní nádrže, zlom tam není. Prvních 25 t tedy stojí asi 1 až 2 mil. USD ročně a přinese celé snížení špičky. Plná sezónní nádrž je asi 400krát větší a kupuje jen přesun výroby ze zimy do zbytku roku, tedy dovoz mimo zimu místo dovozu v zimě. Celkový dovoz se s kapacitou nad 50 t nemění. Výchozí je proto malá nádrž asi 50 t a plná sezónní nádrž zůstává jako drahá možnost. Model má rovnoměrný odběr flotily, skutečný denní tankovací profil by část malé nádrže spotřeboval.

### Řádek ztráty baterií

Pro progresivní cestu a baterii 3,0 GWh je řádek 40,7 GWh (nabito minus vybito, 99,4 cyklu).

## 5. Soběstačnost: výchozí mix a podmínky

### Výchozí mix, řádky P50, průměr 5 let

| Cesta | SMR | Vodík | Výroba GWh | Spotřeba GWh | Roční bilance GWh | Výroba / spotřeba | Říjen až březen GWh | Prosinec až únor GWh | Hodiny bez dovozu | Největší dovoz MW, nejhorší rok | Dovoz GWh | Přebytek bez využití GWh |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Progresivní | 0 | flotila na bateriích | 4 036 | 11 486 | −7 450 | 35,1 % | −4 062 | −2 194 | 3,8 % | 2 046 | 7 410 | 0 |
| Progresivní | 0 | 50/50, sezónní nádrž | 4 036 | 12 922 | −8 886 | 31,2 % | −4 376 | −2 069 | 0,2 % | 1 993 | 8 852 | 0 |
| Progresivní | 0 | 50/50, rovnoměrná výroba | 4 036 | 12 922 | −8 886 | 31,2 % | −4 771 | −2 544 | 1,1 % | 2 225 | 8 847 | 0 |
| Progresivní | 1 | flotila na bateriích | 7 978 | 11 486 | −3 508 | 69,5 % | −1 922 | −1 134 | 20,3 % | 1 785 | 3 532 | 32 |
| Progresivní | 1 | 50/50, sezónní nádrž | 7 978 | 12 922 | −4 944 | 61,7 % | −2 292 | −999 | 3,1 % | 1 687 | 4 948 | 4 |
| Progresivní | 1 | 50/50, rovnoměrná výroba | 7 978 | 12 922 | −4 944 | 61,7 % | −2 632 | −1 485 | 11,2 % | 1 919 | 4 928 | 5 |
| Progresivní | 2 | flotila na bateriích | 11 920 | 11 486 | 434 | 103,8 % | 153 | −74 | 71,3 % | 1 285 | 638 | 1 069 |
| Progresivní | 2 | 50/50, sezónní nádrž | 11 920 | 12 922 | −1 002 | 92,2 % | −416 | −147 | 23,2 % | 1 187 | 1 204 | 204 |
| Progresivní | 2 | 50/50, rovnoměrná výroba | 11 920 | 12 922 | −1 002 | 92,2 % | −572 | −435 | 52,6 % | 1 419 | 1 408 | 395 |
| Konzervativní | 0 | bez flotily na vodík | 4 072 | 8 287 | −4 214 | 49,1 % | −2 111 | −1 049 | 0,0 % | 876 | 4 214 | 0 |
| Konzervativní | 1 | bez flotily na vodík | 8 014 | 8 287 | −272 | 96,7 % | −137 | −72 | 3,0 % | 734 | 286 | 13 |
| Konzervativní | 2 | bez flotily na vodík | 11 956 | 8 287 | 3 670 | 144,3 % | 696 | 228 | 100,0 % | 234 | 0 | 1 622 |

Vodík vyrobený mimo kraj, polovina flotily zůstává na bateriích: výroba 7 978 GWh, spotřeba 10 896 GWh, bilance −2 918 GWh.

Roční bilance v tabulce počítá s celým rozpočtem plynu. Hodinový model pouští plyn jen při schodku, proto konzervativní cesta se 2 SMR ukazuje v roční bilanci 3 670 GWh, ale jen 1 621 GWh v hodinách. Řádky s plynem v konzervativní cestě jsou zemní plyn, tedy dovezené palivo. Podíly úrovně 1 a hodinových úrovní proto u konzervativní cesty nejsou přímo srovnatelné. Bilance sezón počítá i přebytek, který v dané hodině nikdo nevzal. Baterie je v konzervativní cestě nulová, v progresivní 3,0 GWh.

### Co by muselo platit

Přidaný výkon nad řádky tabulky, řádky P50. U úrovně 2 je výpočet hodinový, průměr 5 let, a požadavek je bilance sezóny aspoň 0. U SMR je přidaný celý blok 500 MW s 3 942 GWh za rok a odstávkou v létě. Vítr na mezi znamená doplnit vítr do 2 014 MW a zbytek pokrýt jinak.

| Cesta | SMR výchozí | Vodík | Úroveň | Bilance teď GWh | Jen vítr, přidat MW | Jen FVE, přidat MWp | Jen SMR, přidat | Vítr na mezi 2 014 MW | Půl na půl |
|---|---|---|---|---|---|---|---|---|---|
| Progresivní | 1 | flotila na bateriích | rok | −3 508 | 1 420 | 3 724 | 0,89 | 1 391 MW větru, potom 75 MW FVE nebo 0,02 SMR | 710 MW + 1 862 MWp |
| Progresivní | 1 | flotila na bateriích | říjen až březen | −1 922 | 1 258 | 6 471 | 1 celé | 1 391 MW větru, potom 0 SMR |  |
| Progresivní | 1 | flotila na bateriích | prosinec až únor | −1 134 | 1 414 | 10 090 | 2 celé | 1 391 MW větru, potom 1 SMR |  |
| Progresivní | 1 | 50/50, sezónní nádrž | rok | −4 944 | 2 001 | 5 249 | 1,25 | 1 391 MW větru, potom 1 600 MW FVE nebo 0,38 SMR | 1 000 MW + 2 624 MWp |
| Progresivní | 1 | 50/50, sezónní nádrž | říjen až březen | −2 292 | 1 794 | 7 708 | 2 celé | 1 391 MW větru, potom 1 SMR |  |
| Progresivní | 1 | 50/50, sezónní nádrž | prosinec až únor | −999 | 1 807 | 10 406 | 2 celé | 1 391 MW větru, potom 1 SMR |  |
| Progresivní | 1 | 50/50, rovnoměrná výroba | rok | −4 944 | 2 001 | 5 249 | 1,25 | 1 391 MW větru, potom 1 600 MW FVE nebo 0,38 SMR | 1 000 MW + 2 624 MWp |
| Progresivní | 1 | 50/50, rovnoměrná výroba | říjen až březen | −2 632 | 1 726 | 8 872 | 2 celé | 1 391 MW větru, potom 1 SMR |  |
| Progresivní | 1 | 50/50, rovnoměrná výroba | prosinec až únor | −1 485 | 1 854 | 13 223 | 2 celé | 1 391 MW větru, potom 1 SMR |  |
| Progresivní | 0 | 50/50, sezónní nádrž | rok | −8 886 | 3 596 | 9 433 | 2,25 | 1 391 MW větru, potom 5 785 MW FVE nebo 1,38 SMR | 1 798 MW + 4 717 MWp |
| Progresivní | 0 | 50/50, sezónní nádrž | říjen až březen | −4 376 | 3 231 | 14 954 | 3 celé | 1 391 MW větru, potom 2 SMR |  |
| Progresivní | 0 | 50/50, sezónní nádrž | prosinec až únor | −2 069 | 3 168 | 20 158 | 3 celé | 1 391 MW větru, potom 2 SMR |  |
| Progresivní | 2 | 50/50, sezónní nádrž | rok | −1 002 | 406 | 1 064 | 0,25 | 1 391 MW větru, potom 0 MW FVE nebo 0,00 SMR | 203 MW + 532 MWp |
| Progresivní | 2 | 50/50, sezónní nádrž | říjen až březen | −416 | 369 | 1 313 | 1 celé | 1 391 MW větru, potom 0 SMR |  |
| Progresivní | 2 | 50/50, sezónní nádrž | prosinec až únor | −147 | 461 | 1 922 | 1 celé | 1 391 MW větru, potom 0 SMR |  |
| Konzervativní | 0 | bez flotily na vodík | rok | −4 214 | 1 706 | 4 474 | 1,07 | 1 918 MW větru, potom 0 MW FVE nebo 0,00 SMR | 853 MW + 2 237 MWp |
| Konzervativní | 0 | bez flotily na vodík | říjen až březen | −2 111 | 1 599 | 6 945 | 2 celé | 1 918 MW větru, potom 0 SMR |  |
| Konzervativní | 0 | bez flotily na vodík | prosinec až únor | −1 049 | 1 608 | 9 295 | 2 celé | 1 918 MW větru, potom 0 SMR |  |

Hodinově s přidanými zdroji, progresivní cesta, flotila 50/50, sezónní nádrž:

| Mix | Roční bilance GWh | Říjen až březen GWh | Prosinec až únor GWh | Hodiny bez dovozu | Největší dovoz MW, nejhorší rok | Dovoz GWh | Přebytek bez využití GWh |
|---|---|---|---|---|---|---|---|
| 1 SMR, vítr na mez 2 014 MW | −1 518 | −527 | −230 | 23,07 % | 1 596 | 1 972 | 454 |
| 3 SMR | 2 744 | 1 438 | 564 | 99,94 % | 493 | 1 | 2 745 |
| 5 SMR | 10 634 | 5 460 | 2 738 | 100,00 % | 0 | 0 | 10 634 |
| 3 SMR, vítr na mez 2 014 MW | 6 185 | 3 646 | 1 709 | 100,00 % | 0 | 0 | 6 185 |
| 3 SMR, vítr na mez, 3 GWp FVE | 9 011 | 4 548 | 2 052 | 100,00 % | 0 | 0 | 9 011 |

Vítr na mezi 2 014 MW, 1 SMR, kolik FVE navíc vyrovná bilanci:

| Vodík | Cíl | FVE navíc MWp | Roční bilance GWh | Říjen až březen GWh | Prosinec až únor GWh | Hodiny bez dovozu | Největší dovoz MW, nejhorší rok | Dovoz GWh | Přebytek bez využití GWh |
|---|---|---|---|---|---|---|---|---|---|
| 50/50, sezónní nádrž | říjen až březen | 1 680 | 43 | 0 | −90 | 31,2 % | 1 513 | 1 085 | 1 128 |
| 50/50, sezónní nádrž | prosinec až únor | 2 679 | 982 | 304 | 0 | 35,3 % | 1 273 | 800 | 1 781 |
| 50/50, sezónní nádrž | rok | 1 634 | 0 | −14 | −94 | 31,0 % | 1 516 | 1 102 | 1 102 |
| 50/50, rovnoměrná výroba | říjen až březen | 1 718 | 70 | 0 | −179 | 56,6 % | 1 743 | 1 789 | 1 858 |
| 50/50, rovnoměrná výroba | prosinec až únor | 3 315 | 1 566 | 473 | 0 | 60,5 % | 1 505 | 1 569 | 3 135 |
| 50/50, rovnoměrná výroba | rok | 1 643 | 0 | −22 | −188 | 56,3 % | 1 747 | 1 804 | 1 804 |
| flotila na bateriích | říjen až březen | 0 | −79 | 205 | −19 | 57,8 % | 1 694 | 1 499 | 1 421 |
| flotila na bateriích | prosinec až únor | 161 | 69 | 254 | 0 | 59,5 % | 1 686 | 1 430 | 1 499 |
| flotila na bateriích | rok | 86 | 0 | 231 | −9 | 58,7 % | 1 690 | 1 461 | 1 461 |

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
| Tabulka, progresivní | 623 MW | 23,3 MW | 2,6 × | 0,45 % | 1 678 MWp | 54,8 MWp | 0,7 × | 0,41 % |
| Půl na půl pro úroveň 1, flotila 50/50 | 1 624 MW | 63,3 MW | 7,0 × | 1,21 % | 4 302 MWp | 159,8 MWp | 1,9 × | 1,18 % |
| Vítr na mezi a zbytek FVE, flotila 50/50 | 2 014 MW | 78,9 MW | 8,7 × | 1,51 % | 3 278 MWp | 118,8 MWp | 1,4 × | 0,88 % |
| Jen FVE, flotila 50/50 | 623 MW | 23,3 MW | 2,6 × | 0,45 % | 6 927 MWp | 264,8 MWp | 3,2 × | 1,94 % |

Už vlastní cesta tabulky žádá u větru 623 MW, tedy 2,6krát víc za rok, než kraj kdy postavil.


### Verdikt po částech

| Tvrzení | Výsledek | Stupeň důkazu |
|---|---|---|
| Úroveň 1, progresivní s flotilou 50/50, výchozí mix | Nesplněno. Chybí 4 944 GWh, splní 4,3 % běhů | Směr silný, velikost střední. Rozhodují SMR, FVE a D řádky spotřeby |
| Úroveň 1, progresivní s flotilou na bateriích | Nesplněno. Chybí 3 508 GWh, splní 8,3 % běhů. Stačil by vítr na mezi 2 014 MW a 86 MWp FVE, nebo druhý SMR | Střední |
| Úroveň 1, konzervativní | Nesplněno. Chybí 4 214 GWh, splní 0,5 % běhů, a to i s 2 395 GWh plynu | Silný |
| Co by úroveň 1 splnilo, flotila 50/50 | Buď další 2 SMR, nebo vítr na mezi 2 014 MW a asi 1,6 GWp FVE navíc, nebo 1,0 GW větru a 2,6 GWp FVE navíc. Obnovitelné varianty žádají tempo větru 7 až 9krát nad maximem kraje a podíl přírůstku nad horní kvartil referenční třídy | Tempo A, referenční třída orientační, druhý SMR bez zdroje |
| Úroveň 2, zima | Nesplněno. Prosinec až únor −1 485 GWh při 1 SMR a malé nádrži, −999 GWh se sezónní nádrží. Splní 3,0 % a 3,3 % běhů. Vítr samotný by překročil mez 2 014 MW a FVE samotná by potřebovala přes 10 GWp. Bez druhého SMR to jde jen s větrem na mezi a 3,3 GWp FVE navíc, a to jen v bilanci | Směr silný. Tvar větru je celostátní, ne krajský |
| Úroveň 3, hodiny | Nesplněno. Bez dovozu 11,2 % hodin při 1 SMR a malé nádrži, nejvíc 1 919 MW. Skoro všechny hodiny až od 3 SMR, tehdy 2 745 GWh přebytku nikdo nevezme | Střední. Jeden uzel, profily 2015 až 2019, síť nepočítána |
| Bez SMR | Úroveň 1 splní 0,1 % běhů s flotilou 50/50, chybí 8 886 GWh. Rok SMR je největší jednotlivá nejistota | C, rok 2055 jako P90 je úsudek |
| 2 SMR | S flotilou 50/50 úroveň 1 splní 41,4 % běhů, s flotilou na bateriích 65,4 %. Prosinec až únor 39,3 % a 53,8 % | Druhý blok bez zdroje |

## 6. Útok na vlastní výpočet

Nelichotí hindcast nebo křivka závěru? Ne. Křivky ani pásmo 2030 rok 2050 nemění, kontrola to hlídá. Lichotit může jen rozšíření mezí řádku o hodiny P10 a P90, a test to měří:

| Cesta | Varianta | Vodík | Úroveň 1, podíl | Medián GWh | P90 GWh |
|---|---|---|---|---|---|
| Progresivní | základ | 50/50 | 4,3 % | −5 352 | −1 333 |
| Progresivní | základ | na bateriích | 8,1 % | −3 811 | −304 |
| Progresivní | meze řádků jen při 942 h a 2 471 h, vítr P10 2 014,8 h | 50/50 | 3,2 % | −5 509 | −1 623 |
| Progresivní | meze řádků jen při 942 h a 2 471 h, vítr P10 2 014,8 h | na bateriích | 6,2 % | −3 976 | −647 |
| Progresivní | SMR nejpozději 2050 | 50/50 | 5,1 % | −4 747 | −1 009 |
| Progresivní | SMR nejpozději 2050 | na bateriích | 9,8 % | −3 251 | −39 |
| Konzervativní | základ | na bateriích | 0,5 % | −4 212 | −2 075 |
| Konzervativní | meze řádků jen při 942 h a 2 471 h | na bateriích | 0,4 % | −4 234 | −2 114 |

Zvolené meze hodin zvyšují podíl splněných běhů asi o 1 až 2 procentní body, výrok nemění. Ani posun P90 roku SMR na 2050 ho nemění.

Je flotila započítaná dvakrát? Ne. Bateriová a vodíková část nákladní dopravy dávají dohromady 996,8 mil. km (po 50 %), MHD 21,547 mil. km a auta mají vodík 0. Řádky vodíku se v hodinovém modelu nepočítají do bateriové zátěže. Zbývá možný překryv 45,8 GWh.

Drží Monte Carlo společné faktory a obrácená znaménka? Ano. Společné losování používá stejné funkce a stejné obrácené položky jako model stránky, s jednou sadou faktorů pro výrobu i spotřebu. Medián se od modelu stránky liší jen šumem losování, viz níže.

Co by závěr posunulo opačně: neprovedené změny, které jsou otevřené rozhodnutí (regionální podíl větru +262,4 GWh, ostatní průmysl +434,5 GWh, Třinec až −329,2 GWh). Dohromady by to bylo asi +368 GWh, mezeru to nezavře. Zvláštní rozhodnutí potřebují datacentra 700,8 GWh, pro která zdroj není. S P10 by mezera klesla o 569,5 GWh.

### Kontroly

| Kontrola | Hodnota |
|---|---|
| hodinový běh proti hodinový model, největší rozdíl MW | 0,000 |
| míra ztrát progresivní proti hodinový model | 0,000 |
| progresivni: výroba minus spotřeba P50 proti tabulce GWh | 0,000 |
| konzervativni: výroba minus spotřeba P50 proti tabulce GWh | 0,000 |
| progresivni vyroba: medián společného losování proti model stránky GWh | 7,374 |
| progresivni vyroba: šířka P10 až P90 proti model stránky GWh | 2,254 |
| progresivni spotreba: medián společného losování proti model stránky GWh | 15,745 |
| progresivni spotreba: šířka P10 až P90 proti model stránky GWh | 26,634 |
| konzervativni vyroba: medián společného losování proti model stránky GWh | 6,030 |
| konzervativni vyroba: šířka P10 až P90 proti model stránky GWh | 5,158 |
| konzervativni spotreba: medián společného losování proti model stránky GWh | 12,072 |
| konzervativni spotreba: šířka P10 až P90 proti model stránky GWh | 15,791 |

Další kontroly: křivky stránky proti modelu, součty po letech proti tabulce a test logiky stránky procházejí. Hodinové kontroly 28 z 28 v pořádku, včetně hodinové bilance pod 0,1 GWh. Roční bilance tabulky a hodinového výpočtu progresivní cesty se liší o 0,0 GWh.

## 7. Změny proti studii

Řádky, které se tímto přepočtem změnily. Hodnoty P50 2050 v GWh.

| Řádek | Cesta | Staré P50 | Nové P50 | Staré P10 až P90 | Nové P10 až P90 | Důvod |
|---|---|---|---|---|---|---|
| fotovoltaika střešní | progresivni | 1 058,4 | 948,5 | 851,6 až 1 824,8 | 720,2 až 1 727,2 | Studie uvádí 0,12, tedy 1 051,2 h za ČR. Měření MSK 2022 až 2025 je 942 h. Číslo studie zůstává citované. |
| fotovoltaika střešní | konzervativni | 285,8 | 256,1 | 225,7 až 414,5 | 190,9 až 392,3 | Studie uvádí 0,12, tedy 1 051,2 h za ČR. Měření MSK 2022 až 2025 je 942 h. Číslo studie zůstává citované. |
| fotovoltaika pozemní | progresivni | 705,6 | 632,3 | 567,7 až 1 216,5 | 480,1 až 1 151,5 | Stejně jako střešní FVE. |
| fotovoltaika pozemní | konzervativni | 190,5 | 170,7 | 150,5 až 276,4 | 127,3 až 261,6 | Stejně jako střešní FVE. |
| vítr | progresivni | 1 710,5 | 1 539,9 | 799,0 až 3 293,6 | 866,1 až 3 372,0 | Studie uvádí 2 744,7 h za MSK 2023 a 23 % za ČR. Měření MSK 2013 až 2025 je 2 471 h. |
| vítr | konzervativni | 253,7 | 236,7 | 140,4 až 496,5 | 129,9 až 506,7 | Studie uvádí 2 744,7 h za MSK 2023 a 23 % za ČR. Měření MSK 2013 až 2025 je 2 471 h. |
| nákladní doprava | progresivni | 1 071,4 | 558,6 | 449,6 až 1 260,5 | 234,4 až 657,2 | Studie uvádí 2,75 TWh pro celý park, 50 % na vodíku je definice flotily. |
| výroba vodíku: nákladní doprava | progresivni | 157,8 | 1 925,0 | 72,5 až 242,6 | 884,5 až 2 958,5 | Studie uvádí 55 MWh/t, řádek 50,49 kWh/kg podle zdrojů v poznámce. Podíl vodíku je 50 %. |
| ztráty v sítích | progresivni | 380,3 | 426,4 | 341,8 až 487,3 | 383,2 až 546,4 | Míra studie 3,547 % je beze změny, mění se součet spotřeby ze vzorce. |
| ztráty baterií | progresivni | 27,7 | 40,7 | 15,0 až 60,0 | 22,0 až 88,2 | Studie řádek nemá. Baterie 3 GWh, nabito minus vybito z hodinového výpočtu. |

Studie sama je ve všech výše uvedených případech citovaná beze změny. Roky 2030 a 2040 se u těchto řádků změnily stejným postupem, hodnoty jsou v tabulce.

Křivka se změnila, hodnoty v milnících ne: viz tabulka v oddílu 3. Ostatní průmysl používá rok zahájení z Tab.41 a 42 studie, kumulace je náš součet. Výroba vodíku 45,8 GWh zůstává číslo studie.

Řádky, které se od studie odchylovaly už před tímto přepočtem, s vlastním vysvětlením v poznámce řádku:

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
| Třinecké železárny | progresivni | 1 230,8 | Studie spotřebu ani nárůst nečísluje, proto tisk a podklady firmy. |
| Třinecké železárny | konzervativni | 1 000,0 | Studie spotřebu ani nárůst nečísluje, proto tisk a podklady firmy. |
| Nová huť | progresivni | 736,3 | Studie spotřebu nečísluje a počítá s obnovou provozu Liberty, proto web a úsudek. |
| Nová huť | konzervativni | 736,3 | Studie spotřebu nečísluje a počítá s obnovou provozu Liberty, proto web a úsudek. |
| doly | progresivni | 15,0 | Studie spotřebu dolů neuvádí. |
| doly | konzervativni | 15,0 | Studie spotřebu dolů neuvádí. |
| chlazení | progresivni | 191,1 | Studie chlazení neuvádí. |
| chlazení | konzervativni | 158,4 | Studie chlazení neuvádí. |
| datacentra | progresivni | 700,8 | Studie datacentra neuvádí. |
| datacentra | konzervativni | 70,1 | Studie datacentra neuvádí. |
| úspory a účinnost | progresivni | −290,0 | Studie úspory nečísluje. |
| úspory a účinnost | konzervativni | −145,0 | Studie úspory nečísluje. |

## 8. Nejistoty a meze

- Tvary hodin jsou celostátní nebo z Ostravy a jen z 5 let. Rok 2015 až 2019 je o několik procent větrnější, úroveň ale určuje řádek.
- Jeden uzel bez limitů sítě. Baterie bez předvídání, nádrž s předvídáním na rok.
- Přes polovinu řádků má stupeň D. Meze P10 a P90 jsou většinou úsudek. Faktor korelace 0,6 je odhad.
- Tvar SMR: odstávka v létě, celý blok 500 MW. V hodinovém Monte Carlu je losovaná výroba bloku zespodu omezená na 3 130 GWh (odstávka nejvýš 2 500 h), protože odstávka by jinak přetekla konec roku. Týká se to méně než 1 % běhů, roční úroveň omezení nemá. Studie uvádí 350 MW a jeden blok 470 MW.
- Nové plynové bloky v křivce startují před rokem 2030 bez skutečného bloku.
- Cherp et al. 2021 je přečtený jen ve výtahu a je to národní měřítko.
- Tepelná čerpadla a auta nereagují na cenu ani řízení. Datacentra nemají zdroj.
