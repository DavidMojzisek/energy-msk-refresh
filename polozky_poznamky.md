# Poznámky k tabulce polozky.csv (2026-11-04)

Čísla ve sloupcích CSV mají desetinnou tečku a nemají oddělovač tisíců, aby je šlo strojově načíst. Texty používají čárku jako zdroje.
Stupeň se vztahuje ke vstupům P50. Meze P10 a P90 jsou téměř všude úsudek, i u řádků B a C, pokud citace neříká jinak.

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

Ano, je to stejná řada. Doc 01 Tab. 6 s. 40 (7 090 283,3 MWh, 2023) a ERÚ 6.3 za 2023 Q1, Q2, Q4 dávají 5 438 907,3 MWh. Zbývá 1 651 376,0 MWh na Q3, což je věrohodné proti Q2 a Q4 (1 739 196,9 a 1 760 864,5), a odpovídá to i po sektorech (Průmysl 802,3, Energetika 253,2 GWh). Přímý důkaz chybí, protože zpráva za Q3 2023 v podkladech není. Pokles z 7 090 na 6 810 GWh je tedy skutečná změna ve stejné řadě.
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
4. výroba syntetického plynu, 1 076 (účinnosti a podíl v kraji bez zdroje)
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
