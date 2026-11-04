# Hodinový model MSK 2050: baterie, vodík a disparita

Stav k 2026-11-04. Tabulka `polozky.csv` je čtena čerstvě, osobní auta jsou 100 % na baterie a vodík má jen MHD a nákladní doprava. Výsledky jsou průměr 5 povětrnostních let 2015 až 2019. Výsledek je odhad, tvary a meze mají z velké části stupeň D. Tento výpočet `polozky.csv` neměnil.

## Hlavní doporučení: baterie ke kritické mezi, zbytek přebytku na vodík

**Dnešní mix (1 SMR):** baterie 1,5 GWh a 375 MW, vodík v MHD 50 % a v nákladní dopravě 4,1 %, auta 0 %. Přebytek před baterií je jen 474 GWh za rok, po baterii 211 GWh, z toho vznikne 3 831 t H2. Roční mezera zůstává 3 285 GWh. Letní přebytek tedy dnešní schodek neřeší.

**S doplněním 2,9 GWp + 1,1 GW:** baterie 3,0 GWh a 750 MW, vodík v MHD 100 % a v nákladní dopravě 100,0 %, elektrolyzér 2 076 MW, zásoba 8 040 t (268 GWh). Roční mezera klesá na 33 GWh a podíl OZE na 66,8 %. 

**Jedno celkové doporučení:** baterie na kritické mezi a vodík jen z přebytku po ní, tedy první řádek tabulky pro dnešní mix a čtvrtý řádek, pokud kraj doplní zdroje. Důvod: z kombinací bez zimní výroby ze sítě a s baterií, která se ještě vyplácí cykly, dává nejmenší hodinovou disparitu. Roční nedodaný vodík v horších letech je 8,4 GWh v dnešním mixu a 7,2 GWh se zdroji navíc, pokryje ho přenos zásoby mezi lety.

Pravidlo výběru: baterie je největší velikost, u které přidaná GWh ještě dává aspoň 100 plných cyklů za rok. Veškerý přebytek po ní jde na vodík. Podíl vodíku je největší, který přebytek po baterii v průměru pokryje, bez výroby ze sítě. Pořadí plnění je MHD do 50 %, nákladní doprava do 100 %, MHD do 100 %. Elektrolyzér zachytí 95 % přebytku po baterii.

| Mix | MHD | Nákl. | Auta | Elektrolyzér MW | H2 t/rok | Zásoba t | Zásoba GWh | Baterie GWh | Baterie MW | Výroba GWh | Spotřeba GWh | Mezera GWh | Dovoz GWh | Omezeno GWh | Disparita GWh | Špička dovozu MW | Špička přebytku MW | Podíl OZE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 SMR, dnešní mix | 50 % | 4,1 % | 0 % | 688 | 3 831 | 1 160 | 39 | 1,50 | 375,0 | 8 332 | 11 617 | 3 285 | 3 304 | 19 | 3 323 | 1 763 | 901 | 34,4 % |
| bez SMR | 50 % | 1,1 % | 0 % | 426 | 1 553 | 520 | 17 | 0,00 | 0,0 | 4 390 | 11 503 | 7 114 | 7 123 | 10 | 7 133 | 2 032 | 773 | 35,0 % |
| 2 SMR | 50 % | 41,5 % | 0 % | 972 | 32 301 | 5 407 | 180 | 1,00 | 250,0 | 12 274 | 12 662 | 388 | 490 | 102 | 592 | 1 191 | 1 092 | 31,0 % |
| 1 SMR + 2,9 GWp + 1,1 GW | 100 % | 100,0 % | 0 % | 2 076 | 77 624 | 8 040 | 268 | 3,00 | 750,0 | 14 364 | 14 397 | 33 | 502 | 469 | 971 | 1 243 | 3 321 | 66,8 % |
| bez SMR + 2,9 GWp + 1,1 GW | 50 % | 31,4 % | 0 % | 2 341 | 24 634 | 5 171 | 172 | 8,00 | 2 000,0 | 10 457 | 12 531 | 2 073 | 2 178 | 104 | 2 282 | 1 808 | 3 170 | 79,5 % |
| 2 SMR + 2,9 GWp + 1,1 GW | 100 % | 100,0 % | 0 % | 710 | 77 624 | 5 108 | 170 | 0,25 | 62,5 | 18 208 | 14 316 | 3 892 | 97 | 3 988 | 4 085 | 774 | 5 168 | 42,9 % |
| 1 SMR + přepočtené OZE | 50 % | 75,0 % | 0 % | 2 190 | 57 915 | 7 230 | 241 | 4,00 | 1 000,0 | 13 227 | 13 677 | 450 | 630 | 180 | 811 | 1 302 | 2 615 | 63,9 % |
| Konzervativní cesta | 0 % | 0 % | 0 % | 0 | 0 | 0 | 0 | 0,00 | 0,0 | 4 139 | 8 289 | 4 150 | 4 150 | 0 | 4 150 | 869 | 0 | 15,6 % |

Disparita je dovoz plus omezená nebo vyvezená energie, roční mezera je |výroba minus spotřeba|. Platí mezera = |dovoz − omezeno|. Řádek „přepočtené OZE“ používá čerstvý výpočet soběstačnosti: schodek 4 911,8 GWh dělený napůl dá 2,34 GWp + 0,89 GW. Hodnoty 2,9 a 1,1 pocházejí z tabulky před návratem aut na baterie a kraj s nimi vychází skoro přesně vyrovnaný jen díky celé vodíkové flotile. Vítr 623 MW + 1 100 MW zůstává pod mezí 2 014 MW. Výsledky jsou průměr 5 let, špičky jsou nejvyšší hodnota z 5 let.

Podíl OZE: v čitateli jsou OZE přímo do spotřeby, vybitá energie podle podílu OZE v nabíjení a OZE do elektrolýzy. Ve jmenovateli je zatížení plus elektrolýza, bez ztrát baterie. Jako OZE se počítá FVE, vítr, voda, biomasa a bioplyn.

### Tři věci, které je třeba říct přímo

1. **Baterie roční mezeru nezmění, jen přidá ztráty.** V dnešním mixu bez vodíku je mezera 3 121 GWh bez baterie a 3 177 GWh s baterií 20 GWh. Disparita přitom klesne z 4 055 na 3 177 GWh. Baterie snižuje jen hodinovou disparitu.
2. **Podle čisté roční mezery je v dnešním mixu odpověď 0 % vodíku.** Vodík spotřebuje víc elektřiny než baterie: nákladní doprava 3 850 GWh na vodíku proti 1 117 GWh na bateriích. Kraj je v deficitu, takže každý vodík mezeru zvětšuje. Výjimkou jsou mixy s ročním přebytkem bez vodíku, tedy 2 SMR a 1 nebo 2 SMR se zdroji navíc, kde vodík mezeru zmenšuje, dokud přebytek nevyčerpá. Bez SMR se zdroji navíc platí totéž co dnes: nejmenší roční mezera je při 0 % vodíku.
3. **Míry se neshodují.** Tabulka níže ukazuje vítěze každé míry v mřížce s bateriemi až do 300 GWh. Hodinová disparita sama chce co největší baterii, protože nezná její cenu. Proto rozhoduje kritická mez.

### Vítěz každé míry, varianta (a): vodík jen z přebytku, nedodáno nejvýš 1 % potřeby

| Mix | Míra | MHD | Nákl. | Baterie GWh | MW | Elektrolyzér MW | Mezera | Dovoz | Omezeno | Špička dovozu | Špička přebytku | OZE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 SMR, dnešní mix | roční mezera | 0 % | 0 % | 0,00 | 0 | 0 | 3 121 | 3 588 | 467 | 1 772 | 1 523 | 31,2 % |
| 1 SMR, dnešní mix | hodinová disparita | 0 % | 0 % | 20,00 | 5 000 | 0 | 3 177 | 3 177 | 0 | 1 772 | 0 | 34,8 % |
| 1 SMR, dnešní mix | dovoz | 0 % | 0 % | 20,00 | 5 000 | 0 | 3 177 | 3 177 | 0 | 1 772 | 0 | 34,8 % |
| 1 SMR, dnešní mix | špička dovozu | 50 % | 10 % | 0,00 | 0 | 1 000 | 3 428 | 3 474 | 46 | 1 752 | 979 | 34,0 % |
| 1 SMR, dnešní mix | špička přebytku | 0 % | 0 % | 20,00 | 5 000 | 0 | 3 177 | 3 177 | 0 | 1 772 | 0 | 34,8 % |
| bez SMR | roční mezera | 0 % | 0 % | 0,00 | 0 | 0 | 7 063 | 7 148 | 85 | 2 034 | 1 023 | 34,5 % |
| bez SMR | hodinová disparita | 0 % | 0 % | 5,00 | 1 250 | 0 | 7 074 | 7 074 | 0 | 2 034 | 0 | 35,2 % |
| bez SMR | dovoz | 0 % | 0 % | 5,00 | 1 250 | 0 | 7 074 | 7 074 | 0 | 2 034 | 0 | 35,2 % |
| bez SMR | špička dovozu | 100 % | 0 % | 0,00 | 0 | 1 000 | 7 110 | 7 124 | 14 | 2 032 | 820 | 35,0 % |
| bez SMR | špička přebytku | 0 % | 0 % | 5,00 | 1 250 | 0 | 7 074 | 7 074 | 0 | 2 034 | 0 | 35,2 % |
| 2 SMR | roční mezera | 50 % | 20 % | 87,27 | 1 212 | 1 000 | 13 | 216 | 212 | 1 232 | 1 355 | 31,0 % |
| 2 SMR | hodinová disparita | 100 % | 10 % | 300,00 | 12 500 | 1 000 | 114 | 0 | 114 | 276 | 1 176 | 32,1 % |
| 2 SMR | dovoz | 100 % | 10 % | 300,00 | 12 500 | 1 000 | 114 | 0 | 114 | 276 | 1 176 | 32,1 % |
| 2 SMR | špička dovozu | 100 % | 10 % | 300,00 | 12 500 | 1 000 | 114 | 0 | 114 | 276 | 1 176 | 32,1 % |
| 2 SMR | špička přebytku | 50 % | 50 % | 0,00 | 0 | 2 000 | 607 | 617 | 10 | 1 174 | 732 | 31,3 % |
| 1 SMR + 2,9 GWp + 1,1 GW | roční mezera | 0 % | 90 % | 150,00 | 6 250 | 4 000 | 2 | 10 | 12 | 942 | 1 367 | 70,9 % |
| 1 SMR + 2,9 GWp + 1,1 GW | hodinová disparita | 0 % | 90 % | 300,00 | 12 500 | 4 000 | 4 | 0 | 4 | 0 | 1 367 | 71,0 % |
| 1 SMR + 2,9 GWp + 1,1 GW | dovoz | 100 % | 0 % | 300,00 | 12 500 | 100 | 2 421 | 0 | 2 421 | 0 | 5 245 | 64,7 % |
| 1 SMR + 2,9 GWp + 1,1 GW | špička dovozu | 100 % | 0 % | 300,00 | 12 500 | 100 | 2 421 | 0 | 2 421 | 0 | 5 245 | 64,7 % |
| 1 SMR + 2,9 GWp + 1,1 GW | špička přebytku | 0 % | 90 % | 150,00 | 6 250 | 4 000 | 2 | 10 | 12 | 942 | 1 367 | 70,9 % |
| bez SMR + 2,9 GWp + 1,1 GW | roční mezera | 0 % | 0 % | 0,00 | 0 | 0 | 996 | 3 930 | 2 934 | 1 839 | 4 780 | 62,6 % |
| bez SMR + 2,9 GWp + 1,1 GW | hodinová disparita | 0 % | 0 % | 300,00 | 12 500 | 0 | 1 359 | 1 368 | 9 | 1 839 | 3 239 | 85,1 % |
| bez SMR + 2,9 GWp + 1,1 GW | dovoz | 0 % | 0 % | 300,00 | 12 500 | 0 | 1 359 | 1 368 | 9 | 1 839 | 3 239 | 85,1 % |
| bez SMR + 2,9 GWp + 1,1 GW | špička dovozu | 100 % | 70 % | 0,00 | 0 | 2 000 | 3 021 | 3 318 | 297 | 1 770 | 2 973 | 72,8 % |
| bez SMR + 2,9 GWp + 1,1 GW | špička přebytku | 50 % | 20 % | 87,27 | 1 212 | 4 000 | 1 833 | 1 878 | 45 | 1 819 | 2 373 | 81,5 % |
| 2 SMR + 2,9 GWp + 1,1 GW | roční mezera | 100 % | 100 % | 40,00 | 1 667 | 1 000 | 3 746 | 0 | 3 746 | 0 | 5 106 | 44,3 % |
| 2 SMR + 2,9 GWp + 1,1 GW | hodinová disparita | 100 % | 100 % | 40,00 | 1 667 | 1 000 | 3 746 | 0 | 3 746 | 0 | 5 106 | 44,3 % |
| 2 SMR + 2,9 GWp + 1,1 GW | dovoz | 50 % | 30 % | 40,00 | 1 667 | 250 | 5 732 | 0 | 5 732 | 121 | 5 599 | 35,1 % |
| 2 SMR + 2,9 GWp + 1,1 GW | špička dovozu | 0 % | 40 % | 40,00 | 1 667 | 500 | 5 475 | 0 | 5 475 | 0 | 5 544 | 36,5 % |
| 2 SMR + 2,9 GWp + 1,1 GW | špička přebytku | 100 % | 100 % | 20,00 | 5 000 | 1 000 | 3 746 | 0 | 3 746 | 274 | 5 103 | 44,3 % |
| 1 SMR + přepočtené OZE | roční mezera | 50 % | 60 % | 2,00 | 500 | 2 000 | 8 | 969 | 977 | 1 337 | 3 590 | 60,1 % |
| 1 SMR + přepočtené OZE | hodinová disparita | 100 % | 40 % | 300,00 | 12 500 | 4 000 | 144 | 12 | 156 | 876 | 2 305 | 67,7 % |
| 1 SMR + přepočtené OZE | dovoz | 100 % | 40 % | 300,00 | 12 500 | 4 000 | 144 | 12 | 156 | 876 | 2 305 | 67,7 % |
| 1 SMR + přepočtené OZE | špička dovozu | 100 % | 40 % | 300,00 | 12 500 | 4 000 | 144 | 12 | 156 | 876 | 2 305 | 67,7 % |
| 1 SMR + přepočtené OZE | špička přebytku | 0 % | 90 % | 2,00 | 500 | 4 000 | 783 | 804 | 20 | 1 288 | 2 062 | 63,5 % |

Varianta (b), kde síť dokrmí elektrolýzu do roční potřeby, je v `vysledky/spoj_vitezove.csv`. Mřížka je v `vysledky/spoj_mrizka.csv`: krok nákladní dopravy 10 %, MHD 0, 50 a 100 %, 15 baterií, 6 elektrolyzérů. Mnoho vítězů sedí na okraji mřížky (300 GWh, 4 000 MW), proto to nejsou navržené velikosti. Mřížka nezná cenu. U hodnot blízko nule pomáhá i to, že řízený plyn pak nemusí vyčerpat rozpočet, výroba je proto místy nižší než v tabulce.

## Kritická mez baterie

Baterie je krátkodobý zásobník s denním cyklem. Práh je **100 plných cyklů za rok na přidanou GWh**. Je to náš úsudek. Při střední ceně 2050 podle NREL to znamená asi 242 USD za přesunutou MWh: (100 USD/kWh + 310 USD/kW / 4 h) × (0,0963 + 0,04) / 100 cyklů. Hodnotu přesunuté MWh v kraji v roce 2050 zdroj nemám, proto tabulka ukazuje i jiné prahy. NREL počítá údržbu s jedním cyklem denně, takže 365 cyklů je návrhová horní hranice.

| Mix | Práh 200 | Práh 150 | Práh 100 | Práh 50 | Práh 20 | Mezní cykly na koleni | Mezní cykly dalšího kroku | Průměrné cykly | USD/MWh střed |
|---|---|---|---|---|---|---|---|---|---|
| 1 SMR, dnešní mix | 0,00 | 1,00 | **1,50** | 3,00 | 4,00 | 122 | 97 | 154 | 157 |
| bez SMR | 0,00 | 0,00 | **0,00** | 0,50 | 1,50 | n/a | 76 | 0 | n/a |
| 2 SMR | 0,25 | 0,50 | **1,00** | 3,00 | 4,00 | 136 | 97 | 172 | 141 |
| 1 SMR + 2,9 GWp + 1,1 GW | 1,00 | 2,00 | **3,00** | 6,00 | 10,00 | 126 | 96 | 172 | 141 |
| bez SMR + 2,9 GWp + 1,1 GW | 3,00 | 6,00 | **8,00** | 12,00 | 20,00 | 129 | 94 | 184 | 131 |
| 2 SMR + 2,9 GWp + 1,1 GW | 0,00 | 0,00 | **0,25** | 1,50 | 3,00 | 118 | 95 | 118 | 205 |
| 1 SMR + přepočtené OZE | 1,00 | 2,00 | **4,00** | 6,00 | 12,00 | 119 | 92 | 173 | 140 |

Velikosti jsou v GWh, trvání 4 h. Velikost je zaokrouhlená na krok mřížky, mezní cykly jsou mezi sousedními body. Mix bez SMR má na prahu 100 velikost 0, protože přebytek je příliš malý a řídký. Trvání 8 h je v `vysledky/koleno_krivky.csv`.

**Rezerva 87,27 GWh na tři dny** je jiná věc: záložní pravidlo, ne přesun přebytku. Tímto měřítkem se nevyplatí v žádném mixu:

| Mix | Koleno GWh | Cykly rezervy za rok | Mezní cykly nad kolenem | USD/MWh nízká cena | USD/MWh střed | Mezní USD/MWh střed |
|---|---|---|---|---|---|---|
| 1 SMR, dnešní mix | 1,50 | 4,8 | 2,2 | 1 254 | 2 980 | 6 494 |
| bez SMR | 0,00 | 0,9 | 0,9 | 6 934 | 16 478 | 16 478 |
| 2 SMR | 1,00 | 7,6 | 5,6 | 792 | 1 882 | 2 497 |
| 1 SMR + 2,9 GWp + 1,1 GW | 3,00 | 13,1 | 7,5 | 456 | 1 084 | 1 855 |
| bez SMR + 2,9 GWp + 1,1 GW | 8,00 | 21,6 | 5,2 | 277 | 659 | 2 544 |
| 2 SMR + 2,9 GWp + 1,1 GW | 0,25 | 2,6 | 2,2 | 2 331 | 5 540 | 6 351 |
| 1 SMR + přepočtené OZE | 4,00 | 15,6 | 8,0 | 384 | 913 | 1 715 |

Výpočet platí pro 72 h a 1 212,1 MW. Rezervu by musela obhájit hodnota záložního výkonu, tu tento model neocení. Rezerva držená plná navíc přebytek nebere vůbec.

Samovybíjení: grid doklad nemám. List výrobce malé LFP baterie uvádí nejvýš 3 % za měsíc při 25 °C (Victron). Jako citlivost nezměnil koleno, viz níže. Pomocná spotřeba chlazení zde není.

## Logika sezónní zásoby: přínos pro zimu

Přebytek jde nejdřív do baterie, pak do elektrolyzéru, zbytek se omezí nebo vyveze. Flotila bere vodík rovnoměrně ze zásoby, sledované po hodinách. Síť vyrábí jen objem, který přebytek nedodá, a to v hodinách s nejmenším dovozem mimo prosinec až únor. Zásoba se cyklicky opakuje a nikdy neklesne pod nulu. Porovnává se s vodíkem vyráběným rovnoměrně a s flotilou jen na baterie, vše při baterii na koleni.

**1 SMR, dnešní mix**, baterie 1,5 GWh

| Podíly % | H2 t | Z přebytku GWh | Ze sítě GWh | Zima el. zásoba | Zima el. rovnoměrně | Špička zima zásoba MW | Špička zima rovnoměrně | Špička zima baterie | Bilance zima zásoba GWh | Bilance zima rovnoměrně | Bilance zima baterie | Dovoz rok zásoba | Dovoz rok baterie | Zásoba t |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 % | 0 | 0 | 0 | 0 | 0 | 1 534 | 1 534 | 1 534 | -1 059 | -1 059 | -1 059 | 3 359 | 3 359 | 0 |
| MHD 50 | 686 | 36 | 0 | 3 | 9 | 1 533 | 1 537 | 1 534 | -1 059 | -1 065 | -1 059 | 3 348 | 3 359 | 176 |
| MHD 50, nákl. 5 | 4 498 | 201 | 34 | 13 | 58 | 1 527 | 1 554 | 1 534 | -1 054 | -1 099 | -1 059 | 3 329 | 3 359 | 1 366 |
| MHD 50, nákl. 10 | 8 311 | 205 | 230 | 13 | 107 | 1 522 | 1 572 | 1 534 | -1 039 | -1 134 | -1 059 | 3 471 | 3 359 | 2 268 |
| MHD 50, nákl. 25 | 19 749 | 217 | 817 | 14 | 255 | 1 507 | 1 625 | 1 534 | -997 | -1 237 | -1 059 | 3 898 | 3 359 | 5 199 |
| MHD 50, nákl. 50 (tabulka) | 38 812 | 239 | 1 793 | 17 | 501 | 1 483 | 1 715 | 1 534 | -938 | -1 410 | -1 059 | 4 611 | 3 359 | 9 883 |
| MHD 50, nákl. 100 | 76 938 | 314 | 3 714 | 26 | 993 | 1 435 | 1 895 | 1 534 | -878 | -1 757 | -1 059 | 6 020 | 3 359 | 18 823 |
| MHD 100, nákl. 100 | 77 624 | 316 | 3 747 | 26 | 1 002 | 1 434 | 1 898 | 1 534 | -875 | -1 763 | -1 059 | 6 044 | 3 359 | 18 984 |

**1 SMR + 2,9 GWp + 1,1 GW**, baterie 3,0 GWh

| Podíly % | H2 t | Z přebytku GWh | Ze sítě GWh | Zima el. zásoba | Zima el. rovnoměrně | Špička zima zásoba MW | Špička zima rovnoměrně | Špička zima baterie | Bilance zima zásoba GWh | Bilance zima rovnoměrně | Bilance zima baterie | Dovoz rok zásoba | Dovoz rok baterie | Zásoba t |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 % | 0 | 0 | 0 | 0 | 0 | 1 339 | 1 339 | 1 339 | 285 | 285 | 285 | 973 | 973 | 0 |
| MHD 50 | 686 | 36 | 0 | 8 | 9 | 1 338 | 1 342 | 1 339 | 280 | 279 | 285 | 967 | 973 | 58 |
| MHD 50, nákl. 5 | 4 498 | 235 | 0 | 51 | 58 | 1 333 | 1 360 | 1 339 | 252 | 244 | 285 | 939 | 973 | 380 |
| MHD 50, nákl. 10 | 8 311 | 435 | 0 | 95 | 107 | 1 329 | 1 378 | 1 339 | 223 | 209 | 285 | 911 | 973 | 702 |
| MHD 50, nákl. 25 | 19 749 | 1 034 | 0 | 225 | 255 | 1 314 | 1 432 | 1 339 | 136 | 104 | 285 | 829 | 973 | 1 683 |
| MHD 50, nákl. 50 (tabulka) | 38 812 | 2 032 | 0 | 439 | 501 | 1 290 | 1 522 | 1 339 | -5 | -71 | 285 | 700 | 973 | 3 338 |
| MHD 50, nákl. 100 | 76 938 | 4 026 | 1 | 773 | 993 | 1 244 | 1 704 | 1 339 | -202 | -419 | 285 | 505 | 973 | 7 947 |
| MHD 100, nákl. 100 | 77 624 | 4 056 | 7 | 777 | 1 002 | 1 243 | 1 707 | 1 339 | -203 | -425 | 285 | 502 | 973 | 8 052 |

Přínos existuje, ale v dnešním mixu ho platí roční dovoz. Při podílech tabulky (MHD a nákladní 50 %) zásoba zlepší zimní bilanci z -1 410 GWh na -938 GWh a sníží zimní špičku dovozu z 1 715 MW na 1 483 MW. Jenže z 2 032 GWh pochází ze sítě 1 793 GWh a roční dovoz je 4 611 GWh proti 3 359 GWh u baterií. Zlepšení zimy je přesun dovozu do jiných měsíců, ne úspora.

Výroba ze sítě po měsících, dnešní mix, podíly tabulky, GWh:

| led | úno | bře | dub | kvě | čvn | čvc | srp | zář | říj | lis | pro |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 191 | 234 | 242 | 83 | 210 | 221 | 215 | 221 | 176 | 0 |

Ostatní mixy a podíly jsou v `vysledky/vodik_srovnani_sklad_rovnomerne_baterie.csv` a `vysledky/vodik_site_po_mesicich.csv`. Elektrolýza v zimě u doporučených velikostí jde jen z přebytků, ne ze sítě.

### Kompromis baterie a vodík

**1 SMR, dnešní mix**

| Baterie GWh (4 h) | Cykly | Přebytek po baterii | MHD | Nákl. | H2 t | Dovoz | Omezeno | Disparita | Mezera | OZE |
|---|---|---|---|---|---|---|---|---|---|---|
| 0,00 | 0 | 482 | 50 % | 10,6 % | 8 745 | 3 469 | 34 | 3 502 | 3 435 | 34,0 % |
| 1,00 | 170 | 282 | 50 % | 5,8 % | 5 121 | 3 347 | 24 | 3 371 | 3 323 | 34,3 % |
| 2,00 | 139 | 155 | 50 % | 2,8 % | 2 815 | 3 270 | 15 | 3 285 | 3 255 | 34,5 % |
| 3,00 | 115 | 79 | 50 % | 1,0 % | 1 430 | 3 223 | 10 | 3 233 | 3 214 | 34,6 % |
| 5,00 | 78 | 22 | 30 % | 0,0 % | 407 | 3 190 | 7 | 3 197 | 3 183 | 34,7 % |
| 10,00 | 41 | 3 | 3 % | 0,0 % | 48 | 3 179 | 1 | 3 180 | 3 178 | 34,8 % |
| 20,00 | 21 | 0 | 0 % | 0,0 % | 0 | 3 177 | 0 | 3 177 | 3 177 | 34,8 % |
| 50,00 | 8 | 0 | 0 % | 0,0 % | 0 | 3 177 | 0 | 3 177 | 3 177 | 34,8 % |
| 87,27 | 5 | 0 | 0 % | 0,0 % | 0 | 3 177 | 0 | 3 177 | 3 177 | 34,8 % |
| 300,00 | 1 | 0 | 0 % | 0,0 % | 0 | 3 177 | 0 | 3 177 | 3 177 | 34,8 % |

**1 SMR + 2,9 GWp + 1,1 GW**

| Baterie GWh (4 h) | Cykly | Přebytek po baterii | MHD | Nákl. | H2 t | Dovoz | Omezeno | Disparita | Mezera | OZE |
|---|---|---|---|---|---|---|---|---|---|---|
| 0,00 | 0 | 5 110 | 100 % | 100,0 % | 77 624 | 981 | 1 058 | 2 039 | 77 | 63,2 % |
| 1,00 | 224 | 4 855 | 100 % | 100,0 % | 77 624 | 756 | 804 | 1 561 | 48 | 64,8 % |
| 2,00 | 194 | 4 668 | 100 % | 100,0 % | 77 624 | 592 | 615 | 1 207 | 23 | 65,9 % |
| 3,00 | 172 | 4 525 | 100 % | 100,0 % | 77 624 | 502 | 469 | 971 | 33 | 66,8 % |
| 5,00 | 136 | 4 335 | 100 % | 100,0 % | 77 624 | 393 | 288 | 682 | 105 | 67,9 % |
| 10,00 | 90 | 4 059 | 50 % | 95,7 % | 73 661 | 260 | 228 | 488 | 31 | 68,9 % |
| 20,00 | 52 | 3 868 | 50 % | 91,1 % | 70 192 | 173 | 222 | 394 | 49 | 69,4 % |
| 50,00 | 24 | 3 677 | 50 % | 86,6 % | 66 724 | 84 | 206 | 290 | 122 | 70,0 % |
| 87,27 | 14 | 3 605 | 50 % | 84,9 % | 65 421 | 49 | 199 | 248 | 150 | 70,2 % |
| 300,00 | 4 | 3 504 | 50 % | 82,5 % | 63 587 | 0 | 190 | 190 | 190 | 70,6 % |

Nejmenší disparita pod touto logikou v každém mixu, bez ohledu na cenu baterie:

| Mix | Baterie GWh | MHD | Nákl. | H2 t | Disparita | Dovoz | Omezeno | Mezera | Cykly |
|---|---|---|---|---|---|---|---|---|---|
| 1 SMR, dnešní mix | 20,00 | 0 % | 0,0 % | 0 | 3 177 | 3 177 | 0 | 3 177 | 21 |
| bez SMR | 5,00 | 0 % | 0,0 % | 0 | 7 074 | 7 074 | 0 | 7 074 | 15 |
| 2 SMR | 300,00 | 50 % | 13,8 % | 11 230 | 33 | 0 | 33 | 33 | 4 |
| 1 SMR + 2,9 GWp + 1,1 GW | 300,00 | 50 % | 82,5 % | 63 587 | 190 | 0 | 190 | 190 | 4 |
| bez SMR + 2,9 GWp + 1,1 GW | 300,00 | 12 % | 0,0 % | 164 | 1 373 | 1 366 | 7 | 1 358 | 9 |
| 2 SMR + 2,9 GWp + 1,1 GW | 30,00 | 100 % | 100,0 % | 77 624 | 3 770 | 0 | 3 770 | 3 770 | 7 |
| 1 SMR + přepočtené OZE | 300,00 | 50 % | 43,1 % | 33 543 | 115 | 11 | 104 | 94 | 6 |

## Otázka 1: baterie pro přebytky z léta

**Baterie léto do zimy přenést neumí.** Pravidlo „nabíjet duben až září, vybíjet říjen až březen“ dá 87,27 GWh jen 0,94 cyklu za rok a 15 160 USD/MWh při střední ceně, nízká 6 379 USD/MWh. Se zdroji navíc a 1 000 GWh je to 0,94 cyklu a 14 597 USD/MWh. V dnešním mixu je navíc přebytek krátký a denní: letní půlrok má 174 GWh z 265 GWh za rok, ale v noci je stále schodek, takže se baterie bez pravidla vybije hned.

**Jak to děláme teď:** 87,27 GWh je záložní pravidlo tří dnů, ne velikost pro přebytek. Podíl OZE při současném nastavení je v progresivní cestě 30,1 % (denní blok 1,0 GWh, 200 MW, rezerva stojí plná). Volně cyklovaná rezerva dá 31,1 % a 2,7 cyklu. Bez baterie 29,3 %. Konzervativní cesta 15,6 %, přebytek nemá. Roční řádek `ztráty baterií` 350,2 GWh je proti 31,8 GWh z modelu příliš vysoký, protože počítá s cykly, které přebytek nedovolí.

**Podíl s vlivem SMR a bez něj.** S SMR v plném běhu je 30,1 %. Když SMR ustoupí dřív než OZE, je 31,3 % a to je i strop: 4 039,6 GWh OZE / 12 893,4 GWh spotřeby. OZE: FVE, vítr, voda, biomasa, bioplyn. Odpad, syntetický plyn z odpadu a SMR ne.

Saturace a kolena, trvání 4 h, bez ceny:

| Scénář | Podíl bez baterie | Podíl na konci mřížky | Přebytek GWh | Zbývá omezeno GWh | Koleno 100 cyklů | 20 cyklů | 1 cyklus | 95 % zisku GWh | 99 % zisku GWh |
|---|---|---|---|---|---|---|---|---|---|
| P tabulka (vodík rovnoměrně) | 29,3 % | 31,1 % | 265 | 0 | 1,00 | 3,00 | 6,00 | 4,0 | 5,0 |
| P bez vodíku (flotila baterie) | 31,2 % | 34,8 % | 467 | 0 | 1,50 | 4,00 | 10,00 | 5,0 | 10,0 |
| P tabulka + 2,9 GWp + 1,1 GW | 48,7 % | 68,5 % | 3 828 | 927 | 6,00 | 15,00 | 200,00 | 500,0 | 500,0 |
| P bez vodíku + 2,9 GWp + 1,1 GW | 48,6 % | 64,5 % | 4 544 | 2 466 | 5,00 | 15,00 | 100,00 | 150,0 | 300,0 |
| K tabulka | 15,6 % | 15,6 % | 0 | 0 | 0,00 | 0,00 | 0,00 | 0,0 | 0,0 |

Mřížka jde do 5 000 GWh. Podíl jen roste, proto vnitřní optimum bez ceny neexistuje. Se zdroji navíc zůstává i při největší baterii část přebytku omezena, protože ji není kdy vybít. Přehled pro několik velikostí:

**P tabulka (vodík rovnoměrně)**, trvání 4 h

| GWh | MW | Podíl OZE | Omezeno | Dovoz | Cykly | Mezní cykly | Mezní p.b./GWh | USD/MWh | Mezní USD/MWh |
|---|---|---|---|---|---|---|---|---|---|
| 0,00 | 0 | 29,3 % | 265 | 4 826 | 0,0 | n/a | n/a | n/a | n/a |
| 1,00 | 250 | 30,2 % | 131 | 4 709 | 117,6 | 102,3 | 0,793 | 206 | 237 |
| 2,00 | 500 | 30,7 % | 55 | 4 642 | 92,1 | 55,7 | 0,432 | 263 | 434 |
| 3,00 | 750 | 30,9 % | 19 | 4 610 | 72,1 | 31,9 | 0,247 | 336 | 759 |
| 5,00 | 1 250 | 31,1 % | 2 | 4 595 | 46,3 | 3,5 | 0,027 | 523 | 6 858 |
| 8,00 | 2 000 | 31,1 % | 0 | 4 593 | 29,1 | 0,2 | 0,002 | 831 | 106 099 |
| 20,00 | 5 000 | 31,1 % | 0 | 4 593 | 11,6 | 0,0 | 0,000 | 2 078 | n/a |
| 87,27 | 21 818 | 31,1 % | 0 | 4 593 | 2,7 | 0,0 | 0,000 | 9 067 | n/a |
| 300,00 | 75 000 | 31,1 % | 0 | 4 593 | 0,8 | 0,0 | 0,000 | 31 170 | n/a |

**P tabulka + 2,9 GWp + 1,1 GW**, trvání 4 h

| GWh | MW | Podíl OZE | Omezeno | Dovoz | Cykly | Mezní cykly | Mezní p.b./GWh | USD/MWh | Mezní USD/MWh |
|---|---|---|---|---|---|---|---|---|---|
| 0,00 | 0 | 48,7 % | 3 828 | 2 322 | 0,0 | n/a | n/a | n/a | n/a |
| 1,00 | 250 | 50,7 % | 3 532 | 2 061 | 260,4 | 245,5 | 1,904 | 93 | 99 |
| 2,00 | 500 | 52,4 % | 3 283 | 1 842 | 239,8 | 211,7 | 1,642 | 101 | 114 |
| 3,00 | 750 | 53,9 % | 3 064 | 1 649 | 224,1 | 192,7 | 1,495 | 108 | 126 |
| 5,00 | 1 250 | 56,4 % | 2 695 | 1 324 | 199,4 | 152,1 | 1,180 | 121 | 159 |
| 8,00 | 2 000 | 59,0 % | 2 322 | 1 004 | 165,7 | 98,9 | 0,767 | 146 | 245 |
| 20,00 | 5 000 | 61,9 % | 1 899 | 703 | 84,9 | 17,8 | 0,138 | 285 | 1 360 |
| 87,27 | 21 818 | 65,1 % | 1 431 | 369 | 24,2 | 3,7 | 0,028 | 1 001 | 6 624 |
| 300,00 | 75 000 | 67,5 % | 1 079 | 112 | 8,1 | 0,9 | 0,007 | 3 001 | 25 752 |

Vliv poměru výkonu k energii na koleno 100 cyklů, GWh:

| Scénář | 2 h | 4 h | 8 h | 24 h | 72 h | 168 h | 720 h |
|---|---|---|---|---|---|---|---|
| P tabulka (vodík rovnoměrně) | 0,50 | 1,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| P tabulka + 2,9 GWp + 1,1 GW | 6,00 | 6,00 | 8,00 | 1,00 | 0,00 | 0,00 | 0,00 |

Cena: NREL 2025 update, 4h systém v roce 2050, 108, 178 a 307 USD/kWh v dolarech 2024, tab. 2. Rozdělení na energii a výkon je odečteno z obr. 6 (40 a 280, 100 a 310, 217 a 360) a zpět dává 110, 177,5 a 307. Životnost 15 let a údržba 4 % ročně jsou NREL. Diskont 5 % je náš odhad. Účinnost 0,88 podle zadání, NREL má 85 %. Pro evropské ceny údaj nemám.

## Otázka 2: vodík z přebytku

Měrná data z `h2_params.json` a řádků tabulky: nákladní doprava 100 % = 76 252 t a 50,49 kWh/kg. MHD 100 % = 1 372 t a 50,49 kWh/kg. Na 1 % nákladní dopravy tedy připadá 762,5 t a na 1 % MHD 13,7 t. Ke spotřebě se přičítají ztráty v síti stejnou mírou jako v tabulce, 3,677 %.

Elektrolyzér jen z přebytku, flotila zcela na bateriích, baterie 1 GWh a 200 MW:

| MW | Dnešní mix GWh | t H2 | Plné hodiny | Se zdroji navíc GWh | t H2 | Plné hodiny |
|---|---|---|---|---|---|---|
| 100 | 81 | 1 548 | 810 | 383 | 7 316 | 3 830 |
| 200 | 144 | 2 759 | 722 | 739 | 14 111 | 3 693 |
| 300 | 193 | 3 686 | 643 | 1 066 | 20 361 | 3 553 |
| 500 | 253 | 4 832 | 506 | 1 641 | 31 344 | 3 281 |
| 750 | 280 | 5 346 | 373 | 2 224 | 42 495 | 2 966 |
| 1 000 | 285 | 5 452 | 285 | 2 687 | 51 338 | 2 687 |
| 2 000 | 286 | 5 468 | 143 | 3 808 | 72 754 | 1 904 |
| 3 000 | 286 | 5 468 | 95 | 4 203 | 80 284 | 1 401 |
| 5 000 | 286 | 5 468 | 57 | 4 267 | 81 507 | 853 |

Přepočet používá 50,49 kWh/kg. Konzervativní cesta nemá v žádné hodině přebytek, vodík z přebytku je tam 0 t.

**Nepříjemný výsledek pro dnešní mix.** Elektrolyzér 688 MW pracuje jen 279 plných hodin za rok, protože přebytek je krátký a špičatý. Přebytek dá 4,1 % nákladní dopravy, ne 50 % z tabulky. Bez SMR je to jen 1 553 t. V tabulce výše (baterie 1 GWh) zachytí 300 MW 193 z 286 GWh při 643 plných hodinách, menší elektrolyzér tedy dává smysl. Cenu elektrolyzéru zde nepočítám.

**Zásoba.** Předpoklad: stlačený vodík v nádržích 350 bar, 23,3 kg/m³. Hustota je z poznámek tabulky a nebyla ověřena. Dnešní mix: 1 160 t, 38,6 GWh, asi 50 tis. m³. Se zdroji navíc: 8 040 t, 267,7 GWh, asi 345 tis. m³. Přenos mezi lety zvětší zásobu na 1 668 t a 12 801 t. GWh jsou výhřevnost 33,3 kWh/kg. Podzemní zásobník Třanovice leží v kraji a má pro zemní plyn objem 530 mil. m³, ale doklad o vhodnosti pro vodík jsem nenašel. Solné kaverny v Česku nemám doložené, nákladový rozsah EWI 0,66 až 1,75 EUR/kg proto nepřebírám jako platný pro kraj.

**Vozidla, která zůstanou na bateriích.** Auta 938,2 GWh. Nákladní plně na bateriích 558,6 / 0,5 = 1 117,2 GWh, MHD 11,9 / 0,5 = 23,8 GWh. Dnešní mix po doporučení: nákladní 1 071,2 GWh, MHD 11,9 GWh; bilance 8 332 GWh výroby proti 11 617 GWh spotřeby. Se zdroji navíc jsou nákladní i MHD na vodíku, bilance 14 364 proti 14 397 GWh. Řádek MHD obsahuje i tramvaje, podíl 100 % MHD je proto jen horní mez, ne návrh.

**Citlivost na počasí**, H2 z přebytku při pevné velikosti, GWh za rok:

| Mix | Režim | Potřeba | 2015 | 2016 | 2017 | 2018 | 2019 | Podíl OZE |
|---|---|---|---|---|---|---|---|---|
| 1 SMR, dnešní mix | tvar roku, roční součty P50 | 201 | 190 | 201 | 183 | 201 | 187 | 34,2 až 34,6 % |
| 1 SMR, dnešní mix | i meziroční výnos a teplo | 201 | 201 | 186 | 154 | 201 | 201 | 33,6 až 35,3 % |
| 1 SMR + 2,9 GWp + 1,1 GW | tvar roku, roční součty P50 | 4 063 | 4 027 | 4 063 | 4 063 | 4 063 | 4 063 | 66,2 až 67,2 % |
| 1 SMR + 2,9 GWp + 1,1 GW | i meziroční výnos a teplo | 4 063 | 4 063 | 3 922 | 3 906 | 4 063 | 4 063 | 65,7 až 67,3 % |

Další citlivosti, s přepočtem kolena a podílu:

| Mix | Citlivost | Koleno GWh | Přebytek po baterii | MHD | Nákl. | H2 t | Dovoz | Omezeno | OZE |
|---|---|---|---|---|---|---|---|---|---|
| 1 SMR, dnešní mix | základ | 1,50 | 211 | 50 % | 4,1 % | 3 831 | 3 304 | 19 | 34,4 % |
| 1 SMR, dnešní mix | výpadek SMR od 1. 9. | 2,00 | 159 | 50 % | 2,9 % | 2 893 | 3 274 | 15 | 34,5 % |
| 1 SMR, dnešní mix | výpadek SMR od 1. 4. | 1,50 | 192 | 50 % | 3,7 % | 3 481 | 3 292 | 20 | 34,4 % |
| 1 SMR, dnešní mix | vítr z PVGIS 10 m a křivky | 2,00 | 282 | 50 % | 5,8 % | 5 111 | 3 368 | 21 | 34,2 % |
| 1 SMR, dnešní mix | meziroční výnos a teplo | 1,50 | 212 | 50 % | 4,1 % | 3 839 | 3 304 | 23 | 34,4 % |
| 1 SMR, dnešní mix | nabíjení aut a nákladních přes poledne | 0,50 | 128 | 50 % | 2,1 % | 2 318 | 3 220 | 14 | 34,8 % |
| 1 SMR, dnešní mix | účinnost baterie 0,85 (NREL) | 1,50 | 208 | 50 % | 4,1 % | 3 781 | 3 310 | 19 | 34,4 % |
| 1 SMR, dnešní mix | samovybíjení 3 % za měsíc (odhad z listu výrobce) | 1,50 | 211 | 50 % | 4,1 % | 3 830 | 3 304 | 19 | 34,4 % |
| 1 SMR + 2,9 GWp + 1,1 GW | základ | 3,00 | 4 525 | 100 % | 100,0 % | 77 624 | 502 | 469 | 66,8 % |
| 1 SMR + 2,9 GWp + 1,1 GW | výpadek SMR od 1. 9. | 3,00 | 4 569 | 100 % | 100,0 % | 77 624 | 541 | 515 | 66,5 % |
| 1 SMR + 2,9 GWp + 1,1 GW | výpadek SMR od 1. 4. | 3,00 | 4 494 | 100 % | 100,0 % | 77 624 | 477 | 435 | 67,0 % |
| 1 SMR + 2,9 GWp + 1,1 GW | vítr z PVGIS 10 m a křivky | 6,00 | 4 508 | 100 % | 100,0 % | 77 624 | 603 | 456 | 66,3 % |
| 1 SMR + 2,9 GWp + 1,1 GW | meziroční výnos a teplo | 3,00 | 4 529 | 100 % | 100,0 % | 77 624 | 505 | 526 | 66,6 % |
| 1 SMR + 2,9 GWp + 1,1 GW | nabíjení aut a nákladních přes poledne | 3,00 | 4 447 | 100 % | 100,0 % | 77 624 | 439 | 394 | 67,4 % |
| 1 SMR + 2,9 GWp + 1,1 GW | účinnost baterie 0,85 (NREL) | 3,00 | 4 513 | 100 % | 100,0 % | 77 624 | 507 | 457 | 66,7 % |
| 1 SMR + 2,9 GWp + 1,1 GW | samovybíjení 3 % za měsíc (odhad z listu výrobce) | 3,00 | 4 525 | 100 % | 100,0 % | 77 624 | 502 | 468 | 66,8 % |

Nabíjení aut a nákladních přes poledne samo pohltí část přebytku. V dnešním mixu tím bere vodíku a baterii podklad. Je to konkurence, kterou doporučení výše nepočítá.

## Metoda

Jeden uzel, 8 760 h, pevný čas SEČ, bez 29. února. Pořadí: spotřeba, OZE a stálé zdroje, baterie, elektrolyzér, plyn, dovoz, přebytek se omezí nebo vyveze. Baterie je chamtivá bez předvídání, účinnost 0,88 rozdělená na odmocninu při nabití a vybití, rok se opakuje do ustálení. Plyn má pevný roční rozpočet z tabulky a pokrývá největší zbytkový schodek do mezního výkonu.

| Položka | Tvar | Stupeň |
|---|---|---|
| Domácnosti bez vytápění | OTE TDD4, posun dne v týdnu | B |
| Služby a veřejný sektor | OTE TDD1 | B |
| Tepelná čerpadla | denostupně pod 13 °C × denní průběh TDD7, 15 % ohřev vody rovnoměrně, děleno COP = 3 + 0,08 × T v mezích 1,5 až 5 | D |
| Přímotopy | totéž bez COP | D |
| Chlazení | max(0, T − 22 °C), 10 % rovnoměrně | D |
| Auta | večerní nabíjení, vrchol 18 až 20 h | D |
| Nákladní | noční depo a večer, víkend 60 % | D |
| MHD | noční depo, ve dne stálá část | D |
| Elektrokotle | rovnoměrně květen až září | D |
| Průmysl, datacentra, vlaky, energetika, zemědělství | rovnoměrně | D |
| Úspory | záporně podle TDD4 a TDD1 | D |
| Ztráty v síti | úměrně zatížení bez lokální části 886,83 GWh, míra z řádku | C |
| FVE | PVGIS 2015 až 2019, 35° jih, Ostrava, 1 kWp, škálováno na roční GWh | B |
| Vítr | skutečná výroba ČR, OPSD 2015 až 2019, škálováno na roční GWh | B |
| Voda | měsíce ERÚ 2025, v měsíci rovnoměrně | C |
| SMR | 500 MW, 876 h výpadek v kuse od 1. 6. (druhý modul od 1. 9.) | D |
| Biomasa, bioplyn, odpad, ostatní | rovnoměrně | D |
| Stávající kogenerace | podle denostupňů, 20 % rovnoměrně | D |
| Elektrolýza | jen z přebytku po baterii; varianta se sítí mimo zimu | D |

Řádek `ztráty baterií` model nahrazuje vlastním výpočtem, proto se do zatížení nepočítá. Řádky vodíku flotily jsou rovnoměrné jen ve scénáři „tabulka“. Plyn konzervativní cesty má výkon 680,3 MW z koeficientů v `sezonni_profily.csv`.

## Kontrola

- Roční součty proti `polozky.csv` P50 2050: 270 kontrol pro obě cesty a 5 let, 0 přes 0,06 GWh. Spotřeba 13 243,6 GWh minus ztráty baterií 350,2 GWh = zatížení 12 893,4 GWh. Výroba 8 331,8 GWh. Soubor `validace.csv`.
- Bilance se uzavírá v každé hodině: podmínka v `model.py` s mezí 1e-6 MW při každém běhu. Soubor `vysledky/hodiny_doporuceni_SMR1_2017.csv` má kontrolní sloupec.
- Měsíce proti `vodik_sezonnost.csv`, GWh, rozdíl model minus tabulka:

| Měsíc | FVE tab. | FVE model | Vítr tab. | Vítr model | SMR tab. | SMR model | Spotřeba tab. | Spotřeba model | Rozdíl |
|---|---|---|---|---|---|---|---|---|---|
| leden | 48 | 64 | 221 | 200 | 335 | 372 | 1 076 | 1 096 | 20 |
| únor | 88 | 84 | 101 | 154 | 302 | 336 | 951 | 948 | -3 |
| březen | 154 | 141 | 150 | 180 | 335 | 372 | 1 008 | 954 | -53 |
| duben | 205 | 185 | 167 | 154 | 324 | 360 | 920 | 830 | -90 |
| květen | 204 | 198 | 103 | 127 | 335 | 372 | 915 | 844 | -71 |
| červen | 250 | 223 | 112 | 93 | 324 | 0 | 891 | 835 | -56 |
| červenec | 217 | 217 | 97 | 94 | 335 | 294 | 859 | 873 | 14 |
| srpen | 245 | 221 | 96 | 75 | 335 | 372 | 806 | 895 | 89 |
| září | 142 | 161 | 139 | 99 | 324 | 360 | 841 | 818 | -22 |
| říjen | 112 | 122 | 179 | 151 | 335 | 372 | 984 | 853 | -131 |
| listopad | 63 | 82 | 186 | 170 | 324 | 360 | 994 | 904 | -90 |
| prosinec | 36 | 64 | 159 | 212 | 335 | 372 | 994 | 1 012 | 18 |

Spotřeba modelu je v zimě vyšší a na podzim nižší, protože tabulka má tvar 2025 a model tepelná čerpadla podle teploty. Měsíce SMR se liší výpadkem v červnu. Nic jsem nedolaďoval.

- Tvar proti zatížení ČR (OPSD 2015 až 2019), skladba položek 2025: korelace po hodinách 0,699 až 0,747, po měsících 0,929 až 0,963. Maximum k průměru 1,754 až 2,129 proti 1,375 až 1,462 u ČR. Složený tvar je špičatější než ČR, podle našeho úsudku hlavně kvůli přímotopům v teplotním tvaru.
- Zimní špička zatížení bez elektrolýzy: model 1 983 až 2 409 MW podle roku proti 1 825,6 MW v `sezonni_kontrola.csv`, o 9 až 32 % víc. Důvod je nízký COP v mrazu a hodinová teplota. Letní průměr 1 169 až 1 185 MW proti letnímu poledni 1 187,4 MW. Špičky dovozu v tabulkách jsou proto spíš horní odhad.
- Vítr: hodinová korelace OPSD s renewables.ninja je 0,925 a 0,911 (2015, 2016). S větrem z PVGIS 10 m a výkonové křivky pro Břidličnou je přebytek větší, viz citlivost, a korelace s OPSD je jen 0,56 až 0,63.

## Meze

- Jeden uzel: limity sítě v kraji ani dovozní kapacita nejsou v modelu. Přebytek kraje může mít odběr mimo kraj, pak se neomezuje a výhodnost vodíku klesá.
- Vítr je tvar celé ČR, ne Jeseníky. FVE je jedna orientace, východ a západ by špičku snížily, velikost vlivu jsem nepočítal.
- Výpadek SMR je volba. Vedlejší volby jsou uvedené v citlivosti.
- Elektrokotle 150 GWh jsou pevné, neberou přebytek. Pokud by ho braly, vodíku by zůstalo méně.
- TDD je rok 2026 posunutý na týden, svátky sedí jen přibližně. Tvary dopravy jsou odhad.
- Cena elektrolyzéru, zásobníku a vozidel chybí. Práh 100 cyklů proto neřeší, zda je vodík levnější než dovoz.
- Doplnění 2,9 GWp + 1,1 GW znamená tempo stavby, které je podle stránky nad historickým maximem. Tady se neposuzuje.
- Pět let počasí, 2015 až 2019. Roky 2014 a 2020 až 2023 má jen PVGIS, ne OPSD.
- Hodnota 87,27 GWh je z textu řádku `ztráty baterií`. Stejný postup na dnešní tabulce dá 91,1 GWh (odhad), v modelu zůstává 87,27 GWh podle zadání.

## Grafy

- `grafy/koleno_mezni_cykly.pdf`. Co je vyneseno: plné cykly za rok na přidanou GWh podle velikosti baterie, 7 mixů. Jak se počítá: rozdíl vybité energie mezi sousedními velikostmi, průměr 5 let, trvání 4 h, vodík podle doporučení. Zjištění: práh 100 cyklů protínají mixy mezi 0 a 8 GWh, u rezervy 87,27 GWh je mezní cyklů pod 10. Data: `vysledky/koleno_krivky.csv`.
- `grafy/kompromis_baterie_vodik.pdf`. Co je vyneseno: vodík z přebytku a hodinová disparita podle baterie. Jak se počítá: pro každou baterii největší podíl vodíku, který přebytek pokryje. Zjištění: větší baterie bere vodíku surovinu, disparita přitom dál klesá. Data: `vysledky/kompromis_baterie_vodik.csv`.
- `grafy/zasoba_vodiku.pdf`. Co je vyneseno: stav sezónní zásoby během roku u doporučených velikostí. Jak se počítá: kumulace výroby z přebytku minus rovnoměrný odběr, průměr 5 let. Zjištění: zásoba se plní na jaře, v červnu klesá kvůli výpadku SMR a vyčerpává se od listopadu do února. Data: `vysledky/doporuceni_mixy.csv a model.py`.
- `grafy/zimni_bilance.pdf`. Co je vyneseno: zimní bilance prosinec až únor podle podílů vodíku. Jak se počítá: tři případy: zásoba, rovnoměrná výroba, flotila na bateriích. Zjištění: zásoba je v zimě lepší než rovnoměrná výroba. Data: `vysledky/vodik_srovnani_sklad_rovnomerne_baterie.csv`.
- `grafy/q1_podil_oze.pdf`. Co je vyneseno: podíl OZE podle velikosti baterie. Jak se počítá: bez vodíku podle scénáře, trvání 4 h, průměr 5 let. Zjištění: v dnešním mixu podíl přestává růst po několika GWh. Data: `vysledky/q1_baterie_sweep.csv`.

## Zdroje

- PVGIS 5.3 seriescalc, Evropská komise JRC, SARAH3, Ostrava 49,83 N 18,28 E a Břidličná 49,91 N 17,37 E, 2014 až 2023. https://re.jrc.ec.europa.eu/ Licenci jsem nekontroloval, data jsou veřejná.
- Open Power System Data, time_series 2020-10-06, sloupce CZ_wind_onshore_generation_actual a CZ_load_actual_entsoe_transparency, původ ENTSO-E Transparency. https://data.open-power-system-data.org/time_series/2020-10-06/ Licenci je třeba ověřit u balíčku.
- OTE, Normalizovane_TDD_15MIN_2026_CZ.zip. https://www.ote-cr.cz/cs/statistika/typove-diagramy-dodavek-elektriny/normalizovane-tdd Třídy TDD podle dokumentu OTE ve výpisu vyhledávače, TDD1 C01d až C03d, TDD4 D01d a D02d, TDD7 D45d, D57d a D56d.
- renewables.ninja, Wind v1.1, jen kontrola korelace, CC BY-NC 4.0. https://www.renewables.ninja/downloads
- NREL, Cole, Ramasamy, Turan: Cost Projections for Utility-Scale Battery Storage: 2025 Update, NREL/TP-6A40-93281, tab. 2, obr. 6 a 8. https://docs.nrel.gov/docs/fy25osti/93281.pdf
- Victron Energy, technický list LFP 25,6 V, samovybíjení. https://www.victronenergy.com/media/pg/Lithium_NG_battery_25%2C6_V/en/technical-data.html
- Třanovice: tzb-info a kurzy.cz ve výpisu vyhledávače. https://www.tzb-info.cz/ceny-paliv-a-energii/124821-cesi-maji-sanci-nahlednout-do-bezne-nepristupnych-energetickych-zarizeni
- EWI Köln, náklady podzemního skladování vodíku, jen kontext. https://ewi.uni-koeln.de/en/?p=17110
- Vnitřní: `polozky.csv`, `sezonni_profily.csv`, `sezonni_kontrola.csv`, `vodik_sezonnost.csv`, Dopadová studie s.145 (1 GW, 1 GWh).

Nezískáno: měřené hodinové zatížení a vítr v kraji, hodnota přesunuté MWh pro 2050, samovybíjení velké baterie, cena nádrží na vodík, vhodnost Třanovic pro vodík.
