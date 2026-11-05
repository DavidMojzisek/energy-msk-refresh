# Poznámky k tabulce tabulka položek (2026-11-05)

Čísla ve sloupcích CSV mají desetinnou tečku a nemají oddělovač tisíců, aby je šlo strojově načíst. Texty používají čárku jako zdroje.
Stupeň se řídí nejslabším vstupem hodnoty P50 pro rok 2050. Meze P10 a P90 jsou téměř všude úsudek, i u řádků B a C, pokud citace neříká jinak. Stupeň A nemá žádný řádek, protože každý obsahuje výhled; základy z ERÚ jsou změřené.

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

ERÚ Roční zpráva 2025 (tab. 4.1, 4.3) uvádí vyšší hodnoty: výroba 2 814,8131 GWh (rozdíl 9,6 GWh, hlavně FVE), spotřeba 6 855,0524 GWh (rozdíl 4,4 GWh). Základ zůstává na čtvrtletních zprávách. Palivový rozklad bere Roční zprávu, tab. 4.5, s. 20, protože čtvrtletní zprávy paliva po krajích nemají. Tato tabulka je stupeň A a nahradila odhad z Dopadové studie Tab. 4.

## 2. Ztráty v sítích

- Báze sazby 3,547 % je spotřeba na prahu sítě, ne netto. Dopadová studie Tab. 1 s. 27: 6 018,9 − 5 805,4 = 213,5 a 213,5 / 6 018,9 = 3,547 %. Rovnice 7 na s. 74 má stejný tvar.
- Sazba je za bývalý Severomoravský kraj od ČEZ Distribuce (s. 74), MSK se nesleduje.
- Tab. 6.3 ztráty v sítích neobsahuje. ERÚ je dává jen do TBS (definice v každé zprávě, kap. 1) a celostátně je součet tab. 6.3 (56 871,0 GWh) menší než Spotřeba ČR bez ztrát (58 152,4 GWh).
- Výpočet: 5 963,8184 × 3,547 % / (1 − 3,547 %) = 219,3 GWh. Báze je tab. 6.2, protože rozdíl 6.3 − 6.2 (886,8 GWh) je lokální a vlastní spotřeba, která sítí neteče. Toto je volba modelu. Na bázi 6.3 by ztráty byly o cca 33 GWh vyšší.

## 3. Rozsah 7 090 GWh proti tab. 6.3

Hodnota 7 090 GWh a tabulka 6.3 ERÚ jsou stejná řada. Dopadová studie Tab. 6 s. 40 (7 090 283,3 MWh, 2023) a ERÚ 6.3 za 2023 Q1, Q2, Q4 dávají 5 438 907,3 MWh. Zbývá 1 651 376,0 MWh na Q3, což je věrohodné proti Q2 a Q4 (1 739 196,9 a 1 760 864,5), a odpovídá to i po sektorech (Průmysl 802,3, Energetika 253,2 GWh). Sezónnost sedí: Q3/Q2 je v 2024 0,949 a dopočtené v 2023 0,950. Přímý důkaz chybí, protože zpráva za Q3 2023 v podkladech není. ERÚ Roční zpráva 2025 (4.6.8) uvádí 2023 netto 5 805 315,2 MWh, takže Dopadová studie Tab. 1 a Obr. 28 a 38 patří k řadě 6.2. Pokles z 7 090 na 6 810 GWh je tedy skutečná změna ve stejné řadě.
Dopadová studie s. 40: sektorový pohled „zahrnuje kromě spotřeby podle kategorizace spotřeb navíc spotřebu provozovatelů přenosové a distribuční soustavy, lokální spotřebu a technologickou vlastní spotřebu“. Studie sama počítá bilanci z užšího čísla 5 805,4 GWh, takže její výhledy (Obr. 28, 38) jsou na jiné bázi než tab. 6.3.

## 4. Energetika a Průmysl v 2025

Vypadá to na přeřazení, ne na reálnou změnu, ale ERÚ to nikde neuvádí a v jeho zprávách poznámka k metodice není.

- Skok v 2025 Q2 proběhl současně v MSK, Olomouckém (16,6 na 42,2 GWh), Plzeňském (15,2 na 26,2) a Středočeském kraji (97,9 na 162,8) a celostátně (997,9 na 1 281,0). Průmysl v týchž krajích klesl.
- V MSK je součet Průmysl + Energetika plynulý: 2024 Q2 1 043,7, 2025 Q2 1 021,0. Hladina se drží i v 2026 (364,8 a 361,4).
- Roční zpráva: Energetika +706,1 GWh, Průmysl −941,6 GWh celostátně.
- Důsledek: rok 2025 míchá jedno čtvrtletí před skokem a tři po něm. Průmysl a Energetika jsou v základu spolehlivé jen jako součet. Nepotvrzeno. Rozhodne dotaz na ERÚ.

## 5. Co se zavřelo

| Pokles PE v MSK | Co sedí | Důkaz |
|---|---|---|
| březen 2025, 1 296,2 na 1 067,2 MW (−229,0) | TAMEH Ostrava 229 MW | shoda výkonu s Dopadovou studií Tab. 18; ERÚ jméno neuvádí |
| březen 2026, 1 073,2 na 473,2 MW (−600,0) | Elektrárna Dětmarovice, tři bloky 200 MW | shoda výkonu s Tab. 18; web o konci uhlí |

Pokles je jeden krok v březnu 2026, ne mezi prosincem a červnem. ERÚ neudává jméno elektrárny, takže jde o odvození. Výroba: Český rozhlas (12. 6. 2025) píše, že ČEZ „definitivně zastavila výrobu elektřiny z černého uhlí“, ERÚ odebírá výkon o rok později. Výroba Dětmarovic v 2025 je odhadnuta na 360,8 GWh z rozdílu leden až březen 2025 a 2026.

## 6. Stav v regionu

- Nová huť: převzata 1. 10. 2025, oblouková pec do 1,5 mil. t ve fázi přípravy, vysoké pece stojí. Spotřebu zdroje neuvádějí.
- Třinec: pec odložena na nejdříve 2030 (Novinky 23. 4. 2025), v srpnu 2026 bez nového data. Elektřina: „zvýšení spotřeby elektřiny o 30 procent na 1 TWh ročně“ (Ekonomický deník 30. 1. 2025).
- Datacentra: projekt v MSK s výkonem a stavem se nenašel. Gigafactory v Dolní Lutyni se stavět nebude.
- SMR: Dětmarovice jsou zmiňovaná varianta, lokalita není vybraná, první SMR ČEZ je v Temelíně.

## 7. Fyzikální meze

| Mez | Hodnota | Stav |
|---|---|---|
| FVE potenciál | „až 165 GW p“, Dopadová studie s. 136 | P90 2050 je řádově pod ním, skutečná mez je síť, ta není číselně známa |
| Vítr potenciál | „až 2 014 MW“, s. 135 | P90 1 200 MW je pod mezí |
| Biomasa | „prakticky vyčerpán“, s. 169 | model drží 432 GWh, P90 475 |
| Malé vodní | spád „téměř vyčerpán“, s. 134 | bez nového výkonu |
| Tepelná čerpadla | 163 913 rodinných domů, s. 114 | regrese by dala 180 040 OM, omezeno na 97 % domů |
| Geotermální | s. 89 | nula |

Kapacita sítě a dostupnost tepelných čerpadel nejsou číselně ověřeny.

## 8. Křížová kontrola

Progresivní P50 2050: výroba 7 862 GWh, spotřeba 12 526 GWh včetně ztrát. Konzervativní: 3 956 a 8 244 GWh.
Dopadová studie netto 2050: očekávaný 7 229,9 GWh (Obr. 28), extrémní 9 917,3 GWh (Obr. 38, přiřazení barvy je výklad modelu), obojí bez 887 GWh lokální části a ztrát. Spotřeba progresivní cesty je výrazně vyšší než extrémní scénář. Hlavní důvody jsou vodík pro nákladní dopravu a MHD, datacentra a plná elektrifikace oceli, které studie nemá nebo má méně.

## 9. Řádky D podle velikosti P50 2050

Úsudek. Pořadí je podle GWh, u dvou cest větší hodnota. Důvod je u každé položky ve sloupci odvozeni.

1. ostatní průmysl a chemie, 1 992
2. Třinecké železárny, 1 549
3. vítr, 1 540
4. vytápění tepelnými čerpadly, 1 189
5. výroba vodíku: nákladní doprava, 1 175
6. ostatní energetika, 1 001
7. služby a veřejný sektor, 996
8. fotovoltaika střešní, 948
9. osobní auta, 938
10. nákladní doprava, 782
11. Nová huť, 736
12. datacentra, 701
13. fotovoltaika pozemní, 632
14. přímotopy, 627
15. domácnosti bez vytápění, 424

## 10. Rozpory ve zdrojích, doslovně

| Téma | Zdroj A | Zdroj B |
|---|---|---|
| Netto 2050 | Dopadová studie Obr. 28 s. 110: 7 229,9 | Dopadová studie Obr. 38 s. 164: 7 275,7 |
| Výroba 2023 | Dopadová studie Tab. 1 s. 27: 3 630,1 GWh | Dopadová studie s. 33: „3 703 GWh“; ERÚ Roční zpráva: 3 703 220,8 MWh |
| Co je netto | Dopadová studie s. 31: „včetně ztrát elektřiny po cestě k zákazníkovi“ | Dopadová studie s. 27: spotřeba na prahu „součet spotřeby elektřiny netto a ztrát v sítích“ |
| Konec Dětmarovic | Dopadová studie s. 103: „k 30.4. 2025“ | Dopadová studie Tab. 29 s. 130: 600,0 MW do 2026; ERÚ: březen 2026 |
| Blok B2 | Dopadová studie s. 103: „V roce 2019“ | Dopadová studie s. 7: „v roce 2020“ |
| Elektřina Třinec | Ekonomický deník 30. 1. 2025: „o 30 procent na 1 TWh ročně“, tedy 0,18 MWh/t | souhrn vyhledávače: 30 % navrch nad cca 1 TWh; primární zdroj nenalezen |
| Třinec 62 MW | trz.cz: „v roce 2027“ | gmk.center 17. 6. 2026: druhá polovina 2030 |
| Třebovice | Dopadová studie s. 151: „190 MWe“ | ekonomickydenik.cz: do 166 MWe |
| Odpad | Dopadová studie s. 137: 150 tis. t, „72 000 MWh“ | Technický týdeník: 200 tis. t, 23 000 MWh |

Procenta konzervativní cesty, která nejdou použít čistě: OZE 10 % (čteno jako nárůst nad stav 2026), síť dvojnásobná zátěž (násobek míry ztrát je vypuštěný, volba modelu č. 42), vytápění 300 % (volba modelu č. 5), MHD 80 % (hodnota vychází pod základ, ponecháno doslovně).

## 11. Nezjištěno

Spotřeba Nové hutě, dolů a chemie. Výroba Dětmarovic v 2025. Definice sektoru Energetika u ERÚ. Ztrátová sazba přímo za MSK. Trakční elektřina železnice v MSK.

## 12. Řídicí vlivy

Tvar křivky: y(t) = D(t) · s(t), s(t) = s0 + (s_T − s0) · S(t), D(2025) = 1. D je v tabulce řídicích vlivů, řádek ho jmenuje ve sloupci ridic. Počet obyvatel a další vnější vlivy jsou vyměnitelné vstupy s uvedeným zdrojem.

- **Čtení v modelu.** Sloupce p10 až p90 v tabulce položek jsou y včetně D. D se na ně znovu nenásobí. Cíl adopce je s_T = y(2050) / D(2050).
- **Směr mezí.** U vlivů platí P10 ≤ hodnota ≤ P90, P10 tedy znamená nižší spotřebu. Kvantil faktoru se u přímotopů čte obráceně jako dosud.
- **Meze položky.** P10 = s_P10 × D_P10 a P90 = s_P90 × D_P90, protože jedna položka drží v běhu jeden kvantil (volba modelu č. 11). Meze kombinovaného vlivu berou vstupy jako nezávislé: D_P10 = D_P50 × exp(−√Σ ln(x_P50 / x_P10)²), u P90 obdobně. Prosté násobení všech P10 by pásmo přehnalo.

Stupeň řádků s vlivem řídí nejslabší vstup hodnoty P50 pro rok 2050. Platné hodnoty řádků jsou v tabulce položek a v přepočtu.

Zdroje: ČSÚ projekce krajů do 2080 (obyvatelstvo: 1 182 589,7930 v 2025, 999 144,3026 v 2050), ČSÚ SLDB 2021, Statistická ročenka MSK 2025, Krause et al. 2020 (spotřeba bateriových aut), Vnitrostátní plán Tab.21 (teplo budov), Oeko 2025 (dnešní hladina nákladních aut).

Co zůstává úsudkem:
- Meze počtu obyvatel, protože ČSÚ dává kraji jednu variantu.
- Velikost domácnosti: projekce domácností neexistuje, počet domácností je odvozený.
- Auta na osobu: dorovnání na dnešní Česko 0,6098 z 0,5280. Tento vliv zvyšuje spotřebu a je největší úsudek v řádku aut.
- Teplo: P50 je polovina poklesu z Vnitrostátního plánu, protože plán svůj scénář sám nazývá ideálním. Celý pokles je P10.
- Nákladní auta: vývoj spotřeby je čistý odhad, zdroj se nenašel.
- Běžná spotřeba 2,5 MWh na odběrné místo, převzatá z dřívějšího řádku.

Ponecháno záměrně beze změny: služby, vlaky, MHD a ostatní řádky, kde vliv nesedí jasně. Proběh na auto. Spotřebiče domácností, ty jsou v řádku úspory.

Rozpor s hlavním zdrojem: Dopadová studie s.137 píše „nelze předpokládat významnou demografickou změnu“, ČSÚ dává pokles o 15,5 % do 2050. Studie to uvádí jen u odpadu, číslo nedává.

Nezjištěno: vývoj spotřeby těžkých nákladních aut (studie ICCT nešly otevřít), údaje starších edic projekce ČSÚ (jen souhrn vyhledávače), hodnota 2025 v řadě aut na osobu (bráno 2024), objem nákladní přepravy do 2050.

## 13. Flotila 70 % baterie a 30 % vodík, progresivní cesta 2050 (volba modelu č. 27)

Flotila je nákladní doprava a MHD, každá z nich 70 % na baterie a 30 % na vodík. Osobní auta na vodík nejezdí. Veškerý vodík flotily se vyrábí v kraji z elektřiny a tato elektřina je ve spotřebě. Konzervativní cesta zůstává na bateriích, řádky vodíku flotily mají nulu.

Výsledek: přebytek kraje pokrývá jen malou část vodíku, většina elektřiny na něj jde ze sítě. Čísla jsou v přepočtu, oddíl 4.

Výpočet: vozidla × km × kg H2/100 km × kWh/kg. Celá aritmetika je ve sloupci odvozeni.

| Vstup | P50 | P10 až P90 | Zdroj |
|---|---|---|---|
| Těžké auto dnes, kg/100 km | 9,0 | 7,5 až 10,8 | ICCT 2022 jen ze souhrnu vyhledávače, model; XCIENT 7,5 |
| Autobus dnes, kg/100 km | 7,49 | 5,6 až 9,1 | JIVE 2, CORDIS; 9,1 jen ze souhrnu vyhledávače |
| Zlepšení vozidla do 2050 | 0,85 | viz řídicí vlivy | eff_nakladni (úsudek) |
| Elektrolyzér dnes, kWh/kg | 55 | | Dopadová studie s.119, DOE stav 2022 |
| Elektrolyzér 2050, kWh/kg | 48,26 | 46 až 55 | 33,3 / 0,69, IEA; DOE konečný cíl; Dopadová studie |
| Komprese, kWh/kg | 3,1 | 1,7 až 6,4 | DOE záznam 9013 z roku 2009, změřený průměr demonstračních stanic; 2,23 je tam jen modelová hodnota |

Volby modelu nad rámec definice cesty:
- 30 % se bere z celé nákladní dopravy a MHD, zbylých 70 % zůstává na bateriích.
- Ve 2040 je vodík 4,6 % km nákladní dopravy, v roce 2050 je to 30 %. Je to úsudek. Znamená to rychlou obnovu parku po roce 2040.
- Vozokilometry nákladní dopravy: 1 314,4 GWh / 1,3187 kWh/km = 996,8 mil. km. Hodnota 1,3187 je Oeko přepočtené na 40 t, aby seděla k 9 kg/100 km pro tutéž soupravu. S 0,96 kWh/km by P50 vyšlo o 37,4 % víc, to je zahrnuto v P90.
- MHD obsahuje tramvaje, 70 % na bateriích a 30 % na vodíku se bere z celého řádku. Je to záměrné zjednodušení, P50 baterií proto klesá pod základ 19,464.
- ridic je u nových řádků prázdný, vlivy jsou přímo v hodnotách.

45 760 MWh z Dopadové studie: studie neříká, pro koho je. Není to tedy prokazatelně vodík flotily a řádek zůstává. Překryv nelze vyloučit a nejvýš je to 45,8 GWh. Číslo sedí na 3 025 + 7 × 6 105, tedy malou variantu Tab. 25; dopočet je náš. Horní mez 260 370 MWh je 16 665 + 7 × 34 815.

Měsíční bilance je ve měsíční tabulka. Vychází z tvarů ERÚ 2025, je přibližná a krátké přebytky neukazuje. Hodiny jsou v přepočtu.

Nezjištěno: účel 45 760 MWh, protože odkaz [45] v Dopadové studii vede na nesouvisející dokument a Strategii MSK 2021 se nenašel. Počet nákladních aut a autobusů v MSK. Podíl tramvají v Tab. 23. Místo pro nádrž v kraji.

Rozpor se zdroji: Dopadová studie s.119 píše, že v osobní a železniční dopravě „jsou tyto projekty spíše utlumovány“. Vnitrostátní plán, tištěná s.46 čeká, že „u osobních automobilů zřejmě převáží elektromobilita“. Model proto osobní auta na vodík nepočítá.

## Syntetický plyn z odpadu

Syntetický plyn se vyrábí z odpadu, ne z elektřiny. Dostupný odpad je 360 000 t za rok (Dopadová studie, s. 137) minus 120 000 t pro spalovnu, tedy 240 000 t. Výroba elektřiny v roce 2050 je 115,2 GWh při 0,48 MWh/t podle stejné strany studie. Elektřina na výrobu plynu není vyčíslena, studie s. 169 ji uvádí jako vysokou, řádek je proto nula a skutečnost je větší. Jiné zdroje syntetického plynu, například důlní nebo koksárenský plyn, nejsou započítané, protože chybí podklad.

## Návrh z hodinového výpočtu

Řádek ztráty baterií odpovídá baterii 2,7 GWh a 675 MW, nabito minus vybito 57,8 GWh při 156,9 cyklu. Velikost je medián denního výkyvu zbytkového zatížení, základ návrhu, ne nákladové optimum. Baterie vyrovnává den a nabíjí se i ze sítě. Vodík ve flotile je dán definicí cesty: MHD 30 %, nákladní doprava 30 %, osobní auta na vodík nejezdí.

## Hodiny FVE a větru a křivky

Hodiny: FVE 942 h (P10 889, P90 995, odhad), vítr 2 471 h (P10 2 184, P90 2 810), měření ERÚ pro MSK, MW beze změny. Čísla studie 0,12, 23 % a 2 744,7 h zůstávají citovaná, pro rok 2050 se nepoužívají. Ztráty v sítích jsou podle svého odvození přepočítané ze součtu spotřeby. Křivky: sloupec krivka v tabulce říká, který tvar řádek používá: prázdný je logistika nebo skok, pchip je monotónní interpolace přes milníky (Fritsch a Carlson 1980), uzly přidává rok zahájení projektů, tvrdy_skok je kalendářní skok, dva_skoky jsou dva stupně. Hodnoty 2050 se křivkou nemění.
