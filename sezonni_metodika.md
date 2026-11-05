# Zimní špička a letní poledne v MSK: metodika výkonové bilance (2026-11-04)

Roční GWh neřeknou, zda kraj pokryje špičku. Tento postup převádí roční hodnoty z tabulka položek na MW ve dvou okamžicích. Koeficienty jsou v koeficientech položek, výsledky v výkonová tabulka. Oddíl křížové kontroly a počet stupňů se přepisují při každém výpočtu. Kalibrace se týká roku 2023 a základu 2025 a na řádcích vodíku nezávisí.

## Dva okamžiky

**Zimní špička.** Roční maximum zatížení v nejchladnějším období, počítané se slunečním výkonem nula, tedy zimní podvečer. Dopadová studie řeší stejný stav (s.56 až 57, s.73).

Měření upřesňuje definici. Celostátní zimní maxima 2023 až 2026 padla vždy mezi 8:45 a 13:15, ani jednou večer (ERÚ, kap. 9.1), a FVE tehdy dodávaly až 1 445,9 MW (19. 2. 2025, 8:45). Na grafech dne maxima se večerní zatížení drží zhruba o 5 až 10 % níž (ERÚ 2025 Q1 a 2026 Q1, s.37, odečteno z grafu). Večer je ale nejhorší pro bilanci, protože slunce nedodává nic. Skládáme tedy zatížení ročního maxima se slunečním výkonem nula. Pro dnešek je to o něco přísnější než skutečný večer. Dopadová studie dělá totéž, když FVE do špičky nepočítá.

**Letní poledne.** Slunečné poledne o víkendu, červen až srpen. Letní maximum ČR (červen až srpen, 2023 až 2026) padá v pracovní dny na 11:30 až 13:15, poledne pracovního dne je tedy letní špička, ne minimum. Odděleného odpoledního maxima v datech není. Nejnižší zatížení je v noci, kolem 3:30 až 5:45, ale tehdy nesvítí. Pro přebytek je proto správná volba poledne s nízkou spotřebou, tedy víkend. Medián denního maxima o víkendu je 0,926 až 0,936 ročního průměru, v pracovní den 1,111 až 1,128 (2024, 2025). Denní maximum víkendu je horní odhad poledne.

## Vzorec

- Spotřeba: MW = GWh × 1000 / 8 760 × koeficient.
- Výroba: MW = GWh × 1000 / 8 760 × dosažitelnost × 8 760 / hodiny řádku. Je to totéž jako instalované MW × dosažitelnost.
- Bilance = dostupný výkon − zatížení, rovnice 4 studie.
- Kontrolní tabulka bere GWh z křivek výpočet modelu, stejných jako na stránce, a P50 2050. Sčítání koeficientů P90 přes položky by pásmo přehnalo, tabulka je proto jen P50.

## Flexibilní položky

| Položka | Zimní špička | Letní poledne |
|---|---|---|
| Řádky výroba vodíku a výroba syntetického plynu | vypnuto, malá nádrž přečká špičku | elektrolyzér = řádky flotily × (1 + míra ztrát sítě) × 1 000 / plné hodiny z hodinového výpočtu. Řádek výroba vodíku ze studie běží jako rovnoměrná zátěž mimo tento výkon |
| Elektrokotle | vypnuto, jen přebytek do limitu výkonu, Dopadová studie s.165: „V zimním období se průmyslové elektrokotle příliš neuplatní“ | 30 % výkonu, teplo v létě je jen ohřev vody |
| Baterie | změřený pokles špičky z hodinového modelu, nikdy celý výkon | nabíjení do jmenovitého výkonu, konzervativní cesta 10 MW |

Přebytek se v této jedné hodině rozdělí v pořadí elektrolýza do svého výkonu, baterie, elektrokotle, zbytek je nevyužitý. Je to jen pohled na jednu hodinu, velikost ani řízení baterie a roční čísla neovlivňuje. Vypnutí elektrolýzy v zimě je předpoklad o malé nádrži, zatím nepodložený. Bez něj by zimní bilance byla horší o výkon elektrolyzéru.

**Baterie.** Velikost je z hodinového výpočtu: medián denního výkyvu zbytkového zatížení a 4 h. Je to základ návrhu, ne nákladové optimum. V roce 2040 je 56,7 % této velikosti. Konzervativní cesta nese jen dnešních 10 MW. Zimní pokles špičky je změřený jen pro rok 2050, hodnoty jsou v přepočtu. Hlavní bilance baterie nezapočítává, protože nejsou zdroj.

## Rozsah: čistá spotřeba proti sektorům

Dopadová studie počítá zatížení z užší čisté spotřeby (tab. 6.2) a dosažitelný výkon snižuje o vlastní spotřebu a přímé dodávky (s.150). Tento model má spotřebu z tab. 6.3 plus ztráty a výrobu brutto. Rozdíl 6.3 − 6.2 je lokální a vlastní spotřeba: 1 284,9 GWh v 2023 a 886,8 GWh v 2025.

- Oba rozsahy se liší v MW zatížení a výkonu, ne v bilanci, protože lokální část je na obou stranách.
- Porovnání se studií proto vede přes zimní zatížení v rozsahu Dopadové studie = zatížení − 886,8 GWh × 1000 / 8 760 × 1,143 = zatížení − 115,7 MW. Koeficient 1,143 je vážený průměr dvou řádků sektoru Energetika.
- Část 886,8 GWh zůstává do 2050 konstantní, zdroj pro její vývoj není.
- Výkonová tabulka je brutto na obou stranách. Jen zimní zatížení v rozsahu Dopadové studie je v rozsahu studie. Stránka nemá mísit tento sloupec s dostupným výkonem.

## Kalibrace

Zatížení MSK nikdo neměří. Dopadová studie s.73 až 74: „Roční maximum zatížení elektrizační soustavy za MSK se nesleduje“. Hodnota kolem 1 020 MW v Obr. 10, 34, 35 je tedy vypočtená ze stejného vzorce a v grafech nemá popisek. Kalibrace ukazuje shodu s metodou studie, ne s měřením.

**Rozpor uvnitř studie.** Rovnice 7 přičítá TVSe, ale grafy vycházejí bez ní:

- 2023 bez TVSe: 6 018,9 GWh / 5 869 h = 1 025,5 MW. S TVSe: (6 018,9 + 285,7) / 5 869 = 1 074,2 MW, což se s grafy neshoduje.
- Rozhoduje Tab.46 s.189: 9 917,3 / (1 − 0,03547) / 5 869 = 1 751,9 MW proti tištěným 1 752,0 MW. Kalibrace proto cílí na 1 025,5 MW.

| Veličina | Cíl | Bez kalibrace | Po kalibraci | Chyba |
|---|---|---|---|---|
| Zimní zatížení 2023, rozsah studie | 1 025,5 MW | 1 037,3 MW | 1 025,5 MW | 0 %, z konstrukce (před kalibrací +1,2 %) |
| Zimní zatížení 2025, rozsah studie | 5 963,8184 / (1 − 0,03547) / 5 869 = 1 053,5 MW | 1 082,6 MW | 1 070,3 MW | +1,6 % |
| Bilance 2023 | 1 024,6 − 1 025,5 = −0,9 MW | | −0,9 MW | 0, z konstrukce, volný parametr 1 |
| Letní poledne 2025, rozsah studie | 680,2 MW | 631,3 MW | 680,2 MW | 0 %, z konstrukce (před kalibrací −7,2 %) |
| Bilance 2025 podle instalovaných MW | | | −54,2 MW | viz níže |
| Bilance 2025 podle GWh × koeficient | | | −123,9 MW | o 69,7 MW horší než předchozí řádek |

**Co se upravilo a jak.**

1. Zimní koeficienty spotřeby jsou násobené jedním faktorem 0,9882, který nastaví rok 2023 na 1 025,5 MW. Letní faktor je 1,0803. Ztráty v sítích se nenásobí.
2. Jeden volný parametr je dosažitelnost tepelných zdrojů mimo Dětmarovice: (1 024,6 + 167,6 − 567,0 − 18,5 × 0,428) / (648,4 + 99,7) = 0,825. Instalované MW jsou z Tab.28 a Tab.18, Dětmarovice 567,0 MW z Tab.46.
3. Přímotopy a léto jsou po první kalibraci opravené podle měření, ne podle cíle. Před úpravou vyšla zima +5,8 % a léto −22,8 %. Sezónní výkyv MOO + MOP je jen 522,1 GWh, zatímco řádky čerpadel a přímotopů mají 1 374,3 GWh. Řádek přímotopů vychází z tarifů (Tab.26) a nese tedy hlavně běžnou spotřebu. VO z vvn a vn mají poměr léto / rok 0,984, proto průmysl v létě 0,95.

**Proč 2025 nesedí přesně.** Hodnota +1,7 MW v Obr. 35 je prognóza z 2024 a počítá s TAMEH 229 MW, který ERÚ v březnu 2025 odebral, a s menší spotřebou. Není to měření. Řádky GWh × koeficient navíc dají o 53,0 MW méně výkonu než instalované MW (1 062,0 proti 1 115,0): ERÚ uvádí PSE 181,3 MW, řádky s hodinami z Tab.18 dají méně. Oprava by v 2050 poškodila řádek zemního plynu, proto zůstává.

**Nezávislé kontroly.**

- Celostátní poměr maxima k průměru je 1,5306 (2024) a 1,5132 (2025), z toho τ 5 739 a 5 789 h. Studie má 8 760 / 5 869 = 1,4926. Odchylka 1,4 až 2,6 % je stejného řádu jako chyba 2025.
- Dosažitelnost 0,825 na úbytku v Obr. 35: mezi 2023 a 2024 ubylo TAMEH 144 MW a menší zdroje 8 MW, Tab.29. 152 × 0,825 = 125 MW proti změně bilance −123,8 MW, ta ale obsahuje i růst zatížení.
- Měsíční poměr MSK proti ČR: leden 2025 1,127 proti 1,157, léto 0,903 proti 0,877. Kraj je plošší než ČR, letní cíl to bere v potaz přepočtem 1,029.

**Výkon v létě.** Měřené ERÚ za ČR, ne za kraj, při letních maximech 2024 až červen 2026: FVE ze 7 měsíců 0,525 / 0,619 / 0,640 instalovaného výkonu, vítr ze 6 měsíců 0,066 / 0,182 / 0,255. Hodnota větru za srpen 2024 v extrahovaném textu chybí. Paroplyn při letních maximech 2024 až 2025 běžel 0 MW, proto mají nové plynové bloky v létě P50 nula a jejich výkon je ve sloupci Rezerva v řízeném plynu. Elektrolýza z plynu nedává smysl.

**Vítr v zimě.** P10 a P50 jsou nula podle pravidla studie s.73, stejně jako slunce. Není to medián. Změřený medián při 14 zimních maximech ČR je 0,192 instalovaného výkonu, P10 0,034, P90 0,316. Do P90 jde měřená hodnota a tabulka má sloupec Bilance s měřeným větrem.

## Křížová kontrola 2050 (jen kontrola, jiné scénáře)

<!-- AUTO-2050 začátek: přepisuje skript -->
| | Zatížení, rozsah studie | Dostupný výkon | Bilance |
|---|---|---|---|
| Dopadová studie očekávaný, Obr. 36 | 7 229,9 / (1 − 0,03547) / 5 869 = 1 277,2 MW | 1 325,4 MW | +48,2 MW |
| Dopadová studie extrémní, Obr. 40, Tab.46 | 1 752,0 MW | 1 731,5 − 378,0 = 1 353,5 MW | −398,5 MW |
| Progresivní cesta | 1551,9 MW | 879,8 MW | -672,1 MW; s baterií podle hodinového modelu -665,1 MW, nejhorší rok -672,0 MW; s měřeným větrem -552,3 MW |
| Konzervativní cesta | 1145,7 MW | 733,9 MW | -411,7 MW; s měřeným větrem -393,3 MW |

Dostupný výkon cest je po odečtení lokální části 80,1 MW, aby šel srovnat se studií. Hlavní příčiny rozdílu jsou v cestách: progresivní cesta má 433 MW plynu místo 683 MW, konzervativní nemá SMR. Přesný rozklad zbytku není k dispozici, Dopadová studie dosažitelný výkon po zdrojích pro 2050 netiskne. Obr. 36 a 40 Dětmarovice nepočítají, ty přidává až Tab.46. Metoda studie s τ na celé energii by dala progresivní cestě (12525,9 − 886,8) / 5,869 = 1983,1 MW, protože by započetla i elektrolýzu ve špičce.

**Léto 2050.** Progresivní cesta má přebytek 440,0 MW. Elektrolyzér z něj bere 197,0 MW ze svých 197,0 MW, baterie 243,0 MW a elektrokotle 0,0 MW. Polední přebytek sám roční objem vodíku nepokryje, stejně jako měsíční bilance v měsíční tabulce, kde schodek trvá celý rok. Konzervativní cesta má -540,6 MW a přebytek nemá, řízený plyn v záloze je 614,7 MW.
<!-- AUTO-2050 konec -->

## Co je stupeň D

<!-- AUTO-STUPNE začátek -->
Z 94 řádků je 55 D, 31 C, 8 B, žádný A.
<!-- AUTO-STUPNE konec -->

Stupeň A nemá žádný řádek, protože každý přenáší měření na budoucí stav.

- Všechny koeficienty spotřeby kromě čerpadel. Měřený je jen celek a skupiny VO a maloodběr, ne položky.
- Největší vliv: osobní auta a nákladní doprava (večerní nabíjení), přímotopy, plné hodiny elektrolýzy, chlazení, výkon baterií.
- Hodnoty pro řádky se stupněm D jsou náš odhad a zatím je nikdo neověřil.

## Co to neukáže

- **Průběh hodin.** Dva okamžiky nejsou časová řada. Hodiny počítá hodinový model, viz přepočet.
- **Tmavé bezvětří (Dunkelflaute).** Vícedenní období bez slunce a větru s prázdnou baterií zde není, LOLE ani EENS se nepočítá. Výdrž baterie je jen podíl energie a deficitu.
- **Limity sítě.** Soustava v kraji se bere jako jeden uzel. Prezentace Město bez elektřiny ukazuje na modelové Porubě, že přenos uvnitř města může omezit dodávku dřív než součet.
- **Dovozní kapacita.** Záporná bilance říká, kolik MW je třeba dovézt, ne zda to přenosová soustava a sousedé mají. ČEPS MAF 2023 v prezentaci Město bez elektřiny s.5 uvádí LOLE a EENS za ČR v jiných scénářích, proto se nepřebírá.
- **Výpadek největšího bloku.** Kritérium n−1 pro SMR 500 MW zde není započtené, případ výpadku je v přepočtu, oddíl 8.
- **Hodinový profil položek v kraji.** MSK maximum neměří. OTE publikuje normalizované typové diagramy po třídách, v modelu nejsou použity. Jsou nejbližším přímým zdrojem pro domácnosti a přímotopy.

## Známé nepřesnosti

- **Jeden koeficient na položku a cestu.** Plynové bloky a syntetický plyn mají v zimě koeficient nula, jejich výkon je z Tab.30 a na energii řádku nezávisí.
- **Dětmarovice.** Koeficient 13,77 platí jen pro rok 2025, řádek je pak nulový.
- **FVE v 2025.** Řádek počítá 942 h, změřeno 926 h, takže 2025 vychází v létě o 2 % níž.
- **Skokové položky.** Výpočet modelu bere u Třince a hutních plynů jeden skok na cíl 2050, ne dva milníky. Rok události má S-křivku, v něm je tedy polovina změny.
