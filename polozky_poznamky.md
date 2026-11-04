# Poznámky k tabulce polozky.csv (2026-11-04)

Čísla ve sloupcích CSV mají desetinnou tečku a nemají oddělovač tisíců, aby je šlo strojově načíst. Texty používají čárku jako zdroje.
Stupeň se vztahuje ke vstupům P50. Meze P10 a P90 jsou téměř všude úsudek, i u řádků B a C, pokud citace neříká jinak. Stupeň A nemá žádný řádek, protože každý obsahuje výhled; základy z ERÚ jsou změřené.

Pro model:
- Vysoký los faktoru znamená rychlejší elektrifikaci, rychlejší povolování a vyšší cenu energií. U řádků hutní plyny, zemní plyn: stávající kogenerace, přímotopy a úspory a účinnost se kvantil faktoru čte obráceně.
- U skokových řádků Třinecké železárny, hutní plyny a energetické využití odpadu se hladina mezi milníky mění. Čtení: základ do skok_rok, potom skok na první milník v roce skok_rok nebo později, dále plynule mezi milníky.

## 1. Výchozí stav

| Kontrola | Výsledek |
|---|---|
| Tab. 6.1, součet 4 čtvrtletí 2025 | 2 805,1634 GWh, shoda |
| Tab. 6.3, součet 4 čtvrtletí 2025 | 6 850,6486 GWh, shoda |
| Součet sloupců proti Celkem | ERÚ se liší o 0,1 MWh vlivem zaokrouhlení; dorovnáno v rezidualních řádcích |
| Ztráty nad tab. 6.3 | 219,3158 GWh, spotřeba celkem 7 069,9644 GWh |

ERÚ Roční zpráva 2025 (tab. 4.1, 4.3) uvádí vyšší hodnoty: výroba 2 814,8131 GWh (rozdíl 9,6 GWh, hlavně FVE), spotřeba 6 855,0524 GWh (rozdíl 4,4 GWh). Základ podle zadání zůstává na čtvrtletních zprávách. Palivový rozklad bere Roční zprávu, tab. 4.5, s. 20, protože čtvrtletní zprávy paliva po krajích nemají. Tato tabulka je stupeň A a nahradila odhad z doc 01 Tab. 4.

## 2. Ztráty v sítích

- Báze sazby 3,547 % je spotřeba na prahu sítě, ne netto. Doc 01 Tab. 1 s. 27: 6 018,9 − 5 805,4 = 213,5 a 213,5 / 6 018,9 = 3,547 %. Rovnice 7 na s. 74 má stejný tvar.
- Sazba je za bývalý Severomoravský kraj od ČEZ Distribuce (s. 74), MSK se nesleduje.
- Tab. 6.3 ztráty v sítích neobsahuje. ERÚ je dává jen do TBS (definice v každé zprávě, kap. 1) a celostátně je součet tab. 6.3 (56 871,0 GWh) menší než Spotřeba ČR bez ztrát (58 152,4 GWh).
- Výpočet: 5 963,8184 × 3,547 % / (1 − 3,547 %) = 219,3 GWh. Báze je tab. 6.2, protože rozdíl 6.3 − 6.2 (886,8 GWh) je lokální a vlastní spotřeba, která sítí neteče. Toto je moje volba. Na bázi 6.3 by ztráty byly o cca 33 GWh vyšší.

## 3. Rozsah 7 090 GWh proti tab. 6.3

Ano, je to stejná řada. Doc 01 Tab. 6 s. 40 (7 090 283,3 MWh, 2023) a ERÚ 6.3 za 2023 Q1, Q2, Q4 dávají 5 438 907,3 MWh. Zbývá 1 651 376,0 MWh na Q3, což je věrohodné proti Q2 a Q4 (1 739 196,9 a 1 760 864,5), a odpovídá to i po sektorech (Průmysl 802,3, Energetika 253,2 GWh). Sezónnost sedí: Q3/Q2 je v 2024 0,949 a dopočtené v 2023 0,950. Přímý důkaz chybí, protože zpráva za Q3 2023 v podkladech není. ERÚ Roční zpráva 2025 (4.6.8) uvádí 2023 netto 5 805 315,2 MWh, takže doc 01 Tab. 1 a Obr. 28 a 38 patří k řadě 6.2. Pokles z 7 090 na 6 810 GWh je tedy skutečná změna ve stejné řadě.
Doc 01 s. 40: sektorový pohled „zahrnuje kromě spotřeby podle kategorizace spotřeb navíc spotřebu provozovatelů přenosové a distribuční soustavy, lokální spotřebu a technologickou vlastní spotřebu“. Studie sama počítá bilanci z užšího čísla 5 805,4 GWh, takže její výhledy (Obr. 28, 38) jsou na jiné bázi než tab. 6.3.

## 4. Energetika a Průmysl v 2025

Vypadá to na přeřazení, ne na reálnou změnu, ale ERÚ to nikde neuvádí a v jeho zprávách jsem poznámku k metodice nenašel.

- Skok v 2025 Q2 proběhl současně v MSK, Olomouckém (16,6 na 42,2 GWh), Plzeňském (15,2 na 26,2) a Středočeském kraji (97,9 na 162,8) a celostátně (997,9 na 1 281,0). Průmysl v týchž krajích klesl.
- V MSK je součet Průmysl + Energetika plynulý: 2024 Q2 1 043,7, 2025 Q2 1 021,0. Hladina se drží i v 2026 (364,8 a 361,4).
- Roční zpráva: Energetika +706,1 GWh, Průmysl −941,6 GWh celostátně.
- Důsledek: rok 2025 míchá jedno čtvrtletí před skokem a tři po něm. Průmysl a Energetika jsou v základu spolehlivé jen jako součet. Nepotvrzeno. Rozhodne dotaz na ERÚ.

## 5. Co se zavřelo

| Pokles PE v MSK | Co sedí | Důkaz |
|---|---|---|
| březen 2025, 1 296,2 na 1 067,2 MW (−229,0) | TAMEH Ostrava 229 MW | shoda výkonu s doc 01 Tab. 18; ERÚ jméno neuvádí |
| březen 2026, 1 073,2 na 473,2 MW (−600,0) | Elektrárna Dětmarovice, tři bloky 200 MW | shoda výkonu s Tab. 18; web o konci uhlí |

Pokles je jeden krok v březnu 2026, ne mezi prosincem a červnem. ERÚ neudává jméno elektrárny, takže jde o odvození. Výroba: Český rozhlas (12. 6. 2025) píše, že ČEZ „definitivně zastavila výrobu elektřiny z černého uhlí“, ERÚ odebírá výkon o rok později. Dětmarovice 2025 odhaduji na 360,8 GWh z rozdílu leden až březen 2025 a 2026.

## 6. Stav v regionu

- Nová huť: převzata 1. 10. 2025, oblouková pec do 1,5 mil. t ve fázi přípravy, vysoké pece stojí. Spotřebu zdroje neuvádějí.
- Třinec: pec odložena na nejdříve 2030 (Novinky 23. 4. 2025), v srpnu 2026 bez nového data. Elektřina: „zvýšení spotřeby elektřiny o 30 procent na 1 TWh ročně“ (Ekonomický deník 30. 1. 2025).
- Datacentra: projekt v MSK s výkonem a stavem jsem nenašel. Gigafactory v Dolní Lutyni se stavět nebude.
- SMR: Dětmarovice jsou zmiňovaná varianta, lokalita není vybraná, první SMR ČEZ je v Temelíně.

## 7. Fyzikální meze

| Mez | Hodnota | Stav |
|---|---|---|
| FVE potenciál | „až 165 GW p“, doc 01 s. 136 | P90 2050 je řádově pod ním, skutečná mez je síť, ta není číselně známa |
| Vítr potenciál | „až 2 014 MW“, s. 135 | P90 1 200 MW je pod mezí |
| Biomasa | „prakticky vyčerpán“, s. 169 | držíme 432 GWh, P90 568,5 |
| Malé vodní | spád „téměř vyčerpán“, s. 134 | bez nového výkonu |
| Tepelná čerpadla | 163 913 rodinných domů, s. 114 | regrese by dala 180 040 OM, omezeno na 97 % domů |
| Geotermální | s. 89 | nula |

Kapacitu sítě a dostupnost tepelných čerpadel z METODIKA bod 9 číselně ověřit neumím.

## 8. Křížová kontrola

Progresivní P50 2050: výroba 8 995 GWh, spotřeba 13 461 GWh včetně ztrát. Konzervativní: 4 176 a 9 142 GWh. Doc 01 netto 2050: očekávaný 7 229,9 (Obr. 28), extrémní 9 917,3 (Obr. 38, přiřazení barvy je můj výklad), obojí bez 887 GWh lokální části a ztrát. Progresivní cesta je tedy nad extrémním scénářem o zhruba 2 TWh. Důvod: syntetický plyn 1 076, datacentra 701 a plná elektrifikace oceli, které studie nemá nebo má méně.

## 9. Řádky D podle velikosti P50 2050

Úsudek. Pořadí je podle GWh, u dvou cest větší hodnota.

1. ostatní průmysl a chemie, 1 992 (rozvojové plochy z extrémního scénáře, držení v čase)
2. osobní auta, 1 334 (podíl 72 %, počet aut v MSK neověřen)
3. Třinecké železárny progresivní, 1 231 (plná elektrifikace je naše čtení, intenzita viz 10)
4. výroba syntetického plynu, 1 076 (účinnosti a podíl v kraji bez zdroje). Otázka na zadavatele: KONTEXT píše „syntetický- využívání odpadu“. Pokud jde o plyn z odpadu, tento řádek klesne k nule.
5. nákladní doprava, 1 076 (podíl osobních aut 72 % a baterií 80 %)
6. fotovoltaika střešní, 1 058 (dělení střecha a pozem)
7. ostatní energetika, 1 001 (obsah neznámý)
8. služby a veřejný sektor, 996 (držení základu)
9. syntetický plyn a biometan, 866 (hodiny a podíl paliva)
10. Nová huť, 736 (základ 7 MW a intenzita pece)
11. fotovoltaika pozemní, 706 (dělení střecha a pozem)
12. datacentra, 701 (žádný projekt v MSK)
13. vytápění TČ konzervativní, 668
14. konzervativní ztráty v sítích, 498 (čtení „dvojnásobné zátěže“)
15. domácnosti bez vytápění, 434; ostatní menší: bioplyn, chlazení, úspory, elektrokotle, ztráty baterií, zemní plyn progresivní, doly, zemědělství a stavebnictví, odpad konzervativní, ostatní paliva.

## 10. Rozpory ve zdrojích, doslovně

| Téma | Zdroj A | Zdroj B |
|---|---|---|
| Netto 2050 | doc 01 Obr. 28 s. 110: 7 229,9 | doc 01 Obr. 38 s. 164: 7 275,7 |
| Výroba 2023 | doc 01 Tab. 1 s. 27: 3 630,1 GWh | doc 01 s. 33: „3 703 GWh“; ERÚ Roční zpráva: 3 703 220,8 MWh |
| Co je netto | doc 01 s. 31: „včetně ztrát elektřiny po cestě k zákazníkovi“ | doc 01 s. 27: spotřeba na prahu „součet spotřeby elektřiny netto a ztrát v sítích“ |
| Konec Dětmarovic | doc 01 s. 103: „k 30.4. 2025“ | doc 01 Tab. 29 s. 130: 600,0 MW do 2026; ERÚ: březen 2026 |
| Blok B2 | doc 01 s. 103: „V roce 2019“ | doc 01 s. 7: „v roce 2020“ |
| Elektřina Třinec | Ekonomický deník 30. 1. 2025: „o 30 procent na 1 TWh ročně“, tedy 0,18 MWh/t | souhrn vyhledávače: 30 % navrch nad cca 1 TWh; primární zdroj nenalezen |
| Třinec 62 MW | trz.cz: „v roce 2027“ | gmk.center 17. 6. 2026: druhá polovina 2030 |
| Třebovice | doc 01 s. 151: „190 MWe“ | ekonomickydenik.cz: do 166 MWe |
| Odpad | doc 01 s. 137: 150 tis. t, „72 000 MWh“ | Technický týdeník: 200 tis. t, 23 000 MWh |

Procenta konzervativní cesty, která nejdou použít čistě: OZE 10 % (čteno jako nárůst nad stav 2026), síť dvojnásobná zátěž (vyšší míra ztrát), vytápění 300 % (ROZHODNUTÍ 5), MHD 80 % (hodnota vychází pod základ, ponecháno doslovně).

## 11. Nezjištěno

Spotřeba Nové hutě, dolů a chemie. Výroba Dětmarovic v 2025. Definice sektoru Energetika u ERÚ. Počet osobních aut v MSK. Ztrátová sazba přímo za MSK. Trakční elektřina železnice v MSK. Technická poznámka: pomocná rešerše vytvořila `work/` a `pdf2txt.sh` v kořeni úkolu, smazání je na vás.

## 12. Řídicí vlivy (revize 2026-11-04)

Nový tvar křivky: y(t) = D(t) · s(t), s(t) = s0 + (s_T − s0) · S(t), D(2025) = 1. D je v `ridici_vlivy.csv`, řádek ho jmenuje ve sloupci `ridic`.

- **Čtení v modelu.** Sloupce p10 až p90 v `polozky.csv` jsou y včetně D. D se na ně znovu nenásobí. Cíl adopce je s_T = y(2050) / D(2050).
- **Směr mezí.** U vlivů platí P10 ≤ hodnota ≤ P90, P10 tedy znamená nižší spotřebu. Kvantil faktoru se u přímotopů čte obráceně jako dosud.
- **Meze položky.** P10 = s_P10 × D_P10 a P90 = s_P90 × D_P90, protože jedna položka drží v běhu jeden kvantil (ROZHODNUTÍ 11). Meze kombinovaného vlivu berou vstupy jako nezávislé: D_P10 = D_P50 × exp(−√Σ ln(x_P50 / x_P10)²), u P90 obdobně. Prosté násobení všech P10 by pásmo přehnalo.

| Řádek | Vliv | Progresivní P50 2050, staré | nové | Konzervativní P50 2050, staré | nové |
|---|---|---|---|---|---|
| osobní auta | d_auta 0,6879 | 1 334,3 | 938,2 | 266,9 | 187,6 |
| nákladní doprava | d_nakladni 0,8500 | 1 076,4 | 893,8 | 322,9 | 268,1 |
| domácnosti bez vytápění | d_domacnosti 0,9770 | 433,6 | 423,6 | 433,6 | 423,6 |
| vytápění tepelnými čerpadly | d_vytapeni 0,8228 | 1 444,6 | 1 188,6 | 667,5 | 549,2 |
| přímotopy | d_primotopy 0,8387 | 0 | 0,0 | 747,3 | 626,8 |
| chlazení | d_chlazeni 0,9903 | 193 | 191,1 | 160 | 158,4 |

Co se změnilo v řádcích kromě D:
- Osobní auta: počet 625 545 včetně dodávkových (ČSÚ, MD, 31.12.2024) nahradil 850 000 × 72 % = 612 000. Bez D tak P50 2050 vzrostla na 1 363,8.
- Nákladní doprava: zbytek ze studie je 2 750,0 − 1 435,6 = 1 314,4 místo 1 345,5, protože počet aut je jiný. Dodávky jsou v autech. Objem přepravy držím na 1.
- Tepelná čerpadla: P10 2030 a 2050 obsahovaly zateplení přímo, teď ho nese jen vliv, jinak by se počítalo dvakrát.
- Konzervativní auta a nákladní doprava zůstávají 20 % a 30 % progresivní P50 (ROZHODNUTÍ 3). Tepelná čerpadla, přímotopy a chlazení mají v této cestě vlastní hodnoty, násobí se stejným vlivem.
- Stupeň tepelných čerpadel (progresivní) a přímotopů (obě cesty) klesl z C na D kvůli vlivu.
- `tempo_max_GWh_rok`: FVE střešní 69,6816; FVE pozemní 13,125 (průměr 2008 až 2012, roční maximum není v tisku); vítr 23,8517; tepelná čerpadla 50,6766; osobní auta 0,3259. Aritmetika je v poznámce řádku. Dělení FVE v historii neexistuje.

Zdroje: ČSÚ projekce krajů do 2080 (obyvatelstvo: 1 182 589,7930 v 2025, 999 144,3026 v 2050), ČSÚ SLDB 2021, Statistická ročenka MSK 2025, Krause et al. 2020 (spotřeba bateriových aut), doc 05 Tab.21 (teplo budov), Oeko 2025 (dnešní hladina nákladních aut).

Co zůstává úsudkem:
- Meze počtu obyvatel, protože ČSÚ dává kraji jednu variantu.
- Velikost domácnosti: projekce domácností neexistuje, počet domácností je odvozený.
- Auta na osobu: dorovnání na dnešní Česko 0,6098 z 0,5280. Tento vliv zvyšuje spotřebu a je největší úsudek v řádku aut.
- Teplo: P50 je polovina poklesu z doc 05, protože plán svůj scénář sám nazývá ideálním. Celý pokles je P10.
- Nákladní auta: vývoj spotřeby je čistý odhad, zdroj jsem nenašel.
- Běžná spotřeba 2,5 MWh na odběrné místo, převzatá z dřívějšího řádku.

Ponecháno záměrně beze změny: služby, vlaky, MHD a ostatní řádky, kde vliv nesedí jasně. Proběh na auto. Spotřebiče domácností, ty jsou v řádku úspory.

Zastaralé po revizi, podle zadání nepřepočítáno:
- Ztráty v sítích se počítají ze součtu spotřeby. Dopočet by dal progresivní 414,9 místo 446,0 a konzervativní 473,1 místo 497,8.
- Součet spotřeby P50 2050 bez tohoto dopočtu: progresivní 12 614,8 místo 13 461,4, konzervativní 8 757,1 místo 9 141,6. Oddíl 8 a pořadí v oddílu 9 tedy platí pro stará čísla.
- Úspory berou 10 % ze staré hodnoty domácností 434, rozdíl je asi 1 GWh.
- Oddíly 9 a 11: počet aut v MSK je už zjištěn (ČSÚ 625 545 včetně dodávkových), zbytek seznamu v oddílu 11 platí.
- `grafy_polozek.pdf` a `web/` jsem nepřestavoval.

Rozpor s hlavním zdrojem: doc 01 s.137 píše „nelze předpokládat významnou demografickou změnu“, ČSÚ dává pokles o 15,5 % do 2050. Studie to uvádí jen u odpadu, číslo nedává.

Nezjištěno: vývoj spotřeby těžkých nákladních aut (studie ICCT nešly otevřít), údaje starších edic projekce ČSÚ (jen souhrn vyhledávače), hodnota 2025 v řadě aut na osobu (bráno 2024), objem nákladní přepravy do 2050.

## 13. Flotila 50 % vodík a 50 % baterie, progresivní cesta 2050 (ROZHODNUTÍ 27)

Výsledek: měsíční přebytek v létě v progresivní cestě při P50 není, ani bez vodíku. Vodík tedy nelze vyrobit z letního přebytku kraje. Jeho elektřina by musela přijít ze sítě mimo kraj nebo z vyšší výroby.

| Řádek, progresivní | P50 2050, staré | nové | P10 až P90, nové | Stupeň |
|---|---|---|---|---|
| osobní auta | 938,2 | 493,8 | 230,0 až 721,3 | D |
| nákladní doprava | 893,8 | 558,6 | 234,4 až 657,2 | D |
| MHD | 23,7 | 11,9 | 11,9 až 33,9 | D, dříve B |
| výroba vodíku: osobní auta | nový | 1 494,6 | 824,2 až 2 295,2 | D |
| výroba vodíku: nákladní doprava | nový | 1 925,0 | 884,5 až 2 958,5 | D |
| výroba vodíku: MHD | nový | 34,6 | 16,1 až 103,1 | D |
| výroba vodíku, mimo flotilu | 45,8 (P90 551,5) | 45,8 (P90 260,4) | 20 až 260,4 | B |

Elektřina na vodík flotily je 3 454,2 GWh, 67 856 t H2 za rok. Součet spotřeby P50 2050 stoupl z 12 614,8 na 15 277,6 GWh, tedy 6 283,0 GWh nad výrobou 8 994,6 GWh. Konzervativní cesta má hodnoty beze změny, nové řádky mají nulu. Základy 7 069,9644 a 2 805,1634 GWh sedí.

Výpočet: vozidla × km × kg H2/100 km × kWh/kg. Celá aritmetika je ve sloupci odvozeni.

| Vstup | P50 | P10 až P90 | Zdroj |
|---|---|---|---|
| Osobní auto dnes, kg/100 km | 1,0 | 0,79 až 1,10 | úsudek; h2.live 0,76; WLTP 0,79 až 0,89 a skutečnost 1,1 jen ze souhrnu vyhledávače |
| Těžké auto dnes, kg/100 km | 9,0 | 7,5 až 10,8 | ICCT 2022 jen ze souhrnu vyhledávače, model; XCIENT 7,5 |
| Autobus dnes, kg/100 km | 7,49 | 5,6 až 9,1 | JIVE 2, CORDIS; 9,1 jen ze souhrnu vyhledávače |
| Zlepšení vozidla do 2050 | 0,705 auta, 0,85 ostatní | viz ridici_vlivy.csv | eff_auta (Krause platí pro BEV i FCHEV), eff_nakladni (úsudek) |
| Elektrolyzér dnes, kWh/kg | 55 | | doc 01 s.119, DOE stav 2022 |
| Elektrolyzér 2050, kWh/kg | 48,26 | 46 až 55 | 33,3 / 0,69, IEA; DOE konečný cíl; doc 01 |
| Komprese, kWh/kg | 3,2 pro 700 bar, 2,23 pro 350 bar | 1,7 až 6,4 a 1,7 až 4 | DOE záznam 9013 z roku 2009 |

Co jsem rozhodl a zadání to neříká:
- 50 % se bere z celé flotily, takže P50 2050 má 100 % čistých aut místo dřívějších 95 %.
- Ve 2040 je vodík třetina čistých vozidel. Je to úsudek. Z toho plyne strmý růst: u aut z 92 704 vozidel v 2040 na 305 169 v 2050.
- Vozokilometry nákladní dopravy: 1 314,4 GWh / 1,3187 kWh/km = 996,8 mil. km. Hodnota 1,3187 je Oeko přepočtené na 40 t, aby seděla k 9 kg/100 km pro tutéž soupravu. S 0,96 kWh/km by P50 vyšlo o 37,4 % víc, to je zahrnuto v P90.
- MHD obsahuje tramvaje, 50 % se bere z celého řádku. Je to záměrné zjednodušení, P50 baterií proto klesá pod základ 19,464.
- `ridic` je u nových řádků prázdný, vlivy jsou přímo v hodnotách.

45 760 MWh z doc 01: studie neříká, pro koho je. Není to tedy prokazatelně vodík flotily a řádek zůstává. Překryv nelze vyloučit a nejvýš je to 45,8 GWh. Číslo sedí na 3 025 + 7 × 6 105, tedy malou variantu Tab. 25; dopočet je můj. Dřívější P90 551,5 vycházelo z 64 PJ vodíku v dopravě, to už vodík flotily je, a proto jsem ho nahradil 16 665 + 7 × 34 815 = 260 370 MWh.

### Sezónnost

Data: ERÚ čtvrtletní zprávy 2025, oddíl 7.8. Technologie dávají 2 805 163,5 MWh, netto spotřeba 5 963 818,3 MWh, obojí sedí na tab. 6.1 a 6.2. Rozsah 7.8 je netto, používám jen tvar. Měsíce jsou v `vodik_sezonnost.csv`.

Předpoklady: SMR a ostatní zdroje rovnoměrně podle dnů, FVE a vítr podle tvaru 2025, spotřeba podle tvaru netto 2025. Tvar 2025 neobsahuje růst tepelných čerpadel a elektromobilů, takže letní spotřeba je přibližná. Vodík rovnoměrně znamená 394,3 MW po celý rok. Spotřeba bez vodíku je 11 777,6 GWh a vynechává tři nové řádky i 45,8 GWh mimo flotilu.

| Případ | Rok bez vodíku, GWh | Přebytek, GWh za rok | Podíl z 3 454,2 | Měsíc s nejmenším schodkem |
|---|---|---|---|---|
| Základ 2025 | −2 783,0 | 0,0 | 0 % | srpen −34,3 |
| Základ s vodíkem | −6 237,2 | 0,0 | 0 % | srpen −327,7 |
| FVE na instalovaný MW | −2 783,0 | 0,0 | 0 % | srpen −45,8 |
| Tvary 2024 | −2 783,0 | 0,0 | 0 % | srpen −92,0 |
| Vytápění v zimě, chlazení v létě | −2 783,0 | 0,9 | 0,0 % | srpen +0,9 |
| FVE a vítr oba na P90 | +77,4 | 837,3 | 24,2 % | srpen +232,4 |
| Totéž a vytápění v zimě | +77,4 | 987,9 | 28,6 % | srpen +267,7 |

Vodík v případech P90 přebytek po odečtení rovnoměrného zatížení vyčerpá na nulu. Měsíční data neukazují krátké přebytky: polední slunce při nízké spotřebě nebo větrné dny mohou přebytek dát i v měsíci se schodkem. Velikost těchto přebytků z dat nezjistím, potřeboval by hodinový profil. Výsledek také neříká nic o přebytcích mimo kraj.

Sezónní zásobník, hypotéza pro případ výroby jen v létě a rovnoměrné spotřeby, odvozeno:
- Výroba duben až září, 4 392 hodin. Zásoba 67 856 t × (1 − 4 392 / 8 760) = 33 835 t, 1 126,7 GWh při 33,3 kWh/kg.
- Objem 1,45 mil. m³ při 350 bar a 23,3 kg/m³, 0,87 mil. m³ při 700 bar a 39 kg/m³. Hustoty nejsou z podkladů, ověřit.
- Příkon elektrolyzérů 3 454,2 GWh / 4 392 h = 786,5 MW, tedy víc než SMR 500 MW. Toto zatížení by letní schodek prohloubilo.
- Výroba jen květen až srpen, 2 952 hodin: 44 990 t, 1 170,1 MW.

Zastaralé po revizi, nepřepočítáno: řádek ztráty v sítích (446,0) nereaguje na nové zatížení a část elektrolyzérů může být přímo na vn nebo vvn. Oddíly 8 a 9 platí pro stará čísla, progresivní cesta je teď daleko nad extrémním scénářem doc 01. `web/` a skupiny stránky jsem neměnil.

Nezjištěno: účel 45 760 MWh, protože odkaz [45] v doc 01 vede na nesouvisející dokument a Strategii MSK 2021 jsem nenašel. Počet nákladních aut a autobusů v MSK. Podíl tramvají v Tab. 23. Hodinové přebytky. Místo pro sezónní zásobník v kraji.

Rozpor se zdroji: doc 01 s.119 píše, že v osobní a železniční dopravě „jsou tyto projekty spíše utlumovány“. Doc 05 tištěná s.46 čeká, že „u osobních automobilů zřejmě převáží elektromobilita“. Polovina osobních aut na vodík je tedy pokyn scénáře, ne závěr zdrojů.

## Syntetický plyn z odpadu

Syntetický plyn se vyrábí z odpadu, ne z elektřiny. Dostupný odpad je 360 000 t za rok (Dopadová studie, s. 137) minus 120 000 t pro spalovnu. Výroba elektřiny v roce 2050 je 231.0 GWh místo 866,0 GWh a konzervativně místo 240,5 GWh. Spotřeba elektřiny na výrobu plynu je nula místo 1 076,4 a 397,5 GWh. Jiné zdroje syntetického plynu, například důlní nebo koksárenský plyn, nejsou započítané, protože chybí podklad.
