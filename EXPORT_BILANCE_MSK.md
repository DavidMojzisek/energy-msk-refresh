# Bilance elektřiny Moravskoslezského kraje do roku 2050: podrobný export modelu

Stav dat: 2026-11-04. Stránka modelu: https://davidmojzisek.github.io/energy-msk-refresh/

## 1. Poznámka pro AI agenta, který tento soubor čte

Tento soubor popisuje model roční výroby a spotřeby elektřiny v Moravskoslezském kraji (MSK) pro roky 2025 až 2050 a pro dvě pracovní cesty kraje. Čtenář s tebou bude o obsahu mluvit a bude si čísla ověřovat, proto se drž těchto pravidel.

- Odpovídej z tohoto souboru. Každé číslo uváděj se zdrojem a stranou, pokud je položka má.
- Ověřuj čísla proti jmenovaným zdrojům a číslům stran. Pokud zdroj nemáš k dispozici, řekni to a číslo nepotvrzuj.
- Když je hodnota jen odhad, řekni to přímo. Hodnota po roce 2025 je vždy výhled, nikdy měření.
- Cesty nejsou předpovědi. Neříkej, která nastane nebo která je lepší, pokud se to z dat nedá doložit.
- Část zdrojů je neveřejná, konkrétně studie zařízení na energetické využití odpadu (ZEVO). Zdroj je neveřejná studie, uvedena jsou jen čísla potřebná k výpočtu. O dalším obsahu této studie nic nevíš a nedomýšlej ho.

**Stupně důkazu.** Stupeň se vztahuje ke vstupům hodnoty P50. Meze P10 a P90 jsou téměř všude odhad, i u řádků B a C, pokud citace neříká jinak.

| Stupeň | Význam |
|---|---|
| A | Změřená data, například ERÚ nebo ČSÚ. |
| B | Publikovaná studie nebo plán. |
| C | Technický výpočet ze známých parametrů. |
| D | Odhad bez publikovaného zdroje, který čeká na ověření. Nikdo ho zatím nezávisle nepotvrdil. |

V tabulce položek je 56 řádků se stupněm D, 23 se stupněm C, 15 se stupněm B a žádný se stupněm A, protože každý řádek obsahuje výhled. Základy za rok 2025 z ERÚ jsou změřené. Tyto počty jsou odvozené sečtením řádků tabulky.

**Zápis čísel.** Hodnoty převzaté z datových tabulek mají desetinnou tečku a nemají oddělovač tisíců, přesně jako v datových souborech stránky. Texty, odvození a citace mají desetinnou čárku a mezeru mezi tisíci, jako zdroje. Čísla jsou převzata skriptem z datových tabulek modelu a nejsou zaokrouhlena. Jednotky jsou GWh za rok, pokud není uvedeno jinak. Odvozené součty jsou výslovně označené.

**Názvy dokumentů.** Dopadová studie je Dopadová studie energetické bezpečnosti a soběstačnosti MSK po odchodu od spalování uhlí z listopadu 2024. Vnitrostátní plán je Vnitrostátní plán České republiky v oblasti energetiky a klimatu z prosince 2024. Úplný seznam je v části 12. „Volba modelu č. N“ odkazuje na část 9.

## 2. Co je model a co jsou dvě cesty

Model říká, kolik elektřiny by kraj vyráběl a spotřeboval, pokud by se vydal danou cestou. Hranicí je území kraje a pouze elektřina. Výroba je brutto z tabulky 6.1 zpráv ERÚ. Spotřeba je součet sektorů z tabulky 6.3 zpráv ERÚ a ztráty v sítích jako samostatná položka. Výchozí rok je 2025.

Progresivní a konzervativní jsou pracovní názvy dvou cest pro kraj. Nejsou to předpovědi. Rozdíl mezi cestami je volba. Pásmo kolem křivky vyjadřuje nejistotu uvnitř jedné cesty. Pásmo je interval věrohodnosti 80 %, tedy P10 až P90. Není to statistický interval spolehlivosti, protože budoucnost nemá výběr dat.

**Progresivní cesta.** Vysoký přechod na elektrifikaci a využití obnovitelných zdrojů, stabilní a soběstačná síť, odolný region.

- Zdroje: maximální využití větru a slunce, náhrada zemního plynu syntetickým plynem z odpadu (volba modelu č. 31), stabilní distribuční síť, akumulace v bateriích na 3 dny, biomasa, bioplyn, SMR (malý modulární reaktor) přibližně 500 MW.
- Spotřeba: datacentra, Třinecké železárny, Nová huť (ocelářství), plná elektrifikace nebo vodík v nákladní dopravě, osobních autech, vlacích a MHD, vytápění.
- Výklad modelu: v roce 2050 je flotila 50 % vodík a 50 % baterie, viz volba modelu č. 27.

**Konzervativní cesta.** Procenta jsou relativní vůči progresivní cestě. Jsou to středové hodnoty pro rok 2050 (volba modelu č. 3).

| Oblast | Definice |
|---|---|
| Obnovitelné zdroje | 10 % oproti progresivní cestě, čteno jako nárůst nad dnešní stav |
| Plyn | 90 % CNG/LPG, pro výrobu elektřiny čteno jako zemní plyn, a 10 % syntetický (volba modelu č. 4) |
| Distribuční síť | dvojnásobná zátěž oproti progresivní cestě, čteno jako vyšší míra ztrát |
| Akumulace | záloha 10 % ze 3 dnů |
| SMR | není (volba modelu č. 6) |
| Biomasa, bioplyn, Nová huť | srovnatelné s progresivní cestou |
| Datacentra | 10 % z progresivní cesty |
| Třinecké železárny | 50 % elektrifikace |
| Doprava | nákladní 30 %, osobní 20 %, vlaky 95 %, MHD 80 % |
| Vytápění | 300 % oproti progresivní cestě, čteno jako energie na vstupu při stejném teple, ne jako elektřina (volba modelu č. 5) |

Čtyři z těchto procent nejdou použít čistě, viz část 10.

## 3. Hlavní výsledky

### Roční energie 2050, GWh

| Cesta | Strana | Základ 2025 | P10 simulace | P50 simulace | P90 simulace | Součet výchozích hodnot |
|---|---|---|---|---|---|---|
| progresivní | výroba | 2805.1634 | 4500.8 | 8110.9 | 10807.8 | 8331.812 |
| progresivní | spotřeba | 7069.9644 | 11185.9 | 14558.5 | 18123.1 | 14332.4 |
| konzervativní | výroba | 2805.1634 | 2755.4 | 4249.6 | 5686.2 | 4138.712 |
| konzervativní | spotřeba | 7069.9644 | 7130.3 | 8466.6 | 10043.3 | 8320 |

Pásmo P10, P50 a P90 je z výpočtu zveřejněného na stránce. Součet výchozích hodnot je odvozený součet sloupce P50 2050 z části 5. Odvozený rozdíl výroby a spotřeby z těchto součtů je -6000.588 GWh v progresivní cestě a -4181.288 GWh v konzervativní cestě.

P50 simulace a součet výchozích hodnot nejsou totéž. Medián součtu nesymetricky rozdělených položek se nerovná součtu jejich mediánů. Ve výrobě progresivní cesty k tomu přispívá SMR: rok spuštění má P90 2055, takže v části běhů do roku 2050 nic nevyrobí. Výroba a spotřeba se simulují zvlášť, proto z pásem nelze odvodit pásmo jejich rozdílu.

### Zimní špička, MW, výchozí hodnoty

| Cesta | Rok | Zatížení | Dostupný výkon | Bilance | Baterie | Bilance s bateriemi | Výdrž baterií, h | Vítr při měřeném mediánu | Bilance s měřeným větrem |
|---|---|---|---|---|---|---|---|---|---|
| progresivní | 2025 | 1186.0 | 1062.0 | -123.9 | 10 | -113.9 | 1.0 | 6.4 | -117.5 |
| progresivní | 2030 | 1284.0 | 496.3 | -787.7 | 50 | -737.7 | 1.0 | 18.4 | -769.3 |
| progresivní | 2040 | 1596.7 | 508.2 | -1088.5 | 207.7 | -880.8 | 72.0 | 76.2 | -1012.3 |
| progresivní | 2050 | 1742.0 | 681.9 | -1060.1 | 1212.1 | 152.0 | 82.3 | 119.8 | -940.3 |
| konzervativní | 2025 | 1186.0 | 1062.0 | -123.9 | 10 | -113.9 | 1.0 | 6.4 | -117.5 |
| konzervativní | 2030 | 1234.0 | 655.0 | -578.9 | 25 | -553.9 | 1.0 | 7.6 | -571.3 |
| konzervativní | 2040 | 1337.3 | 667.0 | -670.3 | 30.9 | -639.4 | 72.0 | 13.4 | -656.9 |
| konzervativní | 2050 | 1342.2 | 828.8 | -513.4 | 121.2 | -392.2 | 72.0 | 17.8 | -495.6 |

### Letní poledne, MW, výchozí hodnoty

| Cesta | Rok | Zatížení bez flexibilních | Dostupný výkon | Bilance před flexibilními | Rezerva v řízeném plynu | Nabíjení baterií | Elektrokotle | Potřeba elektrolýzy | Zbývá pro vodík |
|---|---|---|---|---|---|---|---|---|---|
| progresivní | 2025 | 783.4 | 364.8 | -418.6 | 0.0 | 0 | 0.0 | 0.0 | 0.0 |
| progresivní | 2030 | 828.3 | 550.9 | -277.4 | 133.2 | 0 | 0 | 8.4 | 0 |
| progresivní | 2040 | 1042.8 | 927.0 | -115.8 | 342.1 | 0 | 0 | 310.4 | 0 |
| progresivní | 2050 | 1153.0 | 1677.4 | 524.5 | 104.0 | 200.0 | 45.0 | 1166.7 | 279.5 |
| konzervativní | 2025 | 783.4 | 364.8 | -418.6 | 0.0 | 0 | 0.0 | 0.0 | 0.0 |
| konzervativní | 2030 | 807.5 | 421.1 | -386.5 | 171.5 | 0 | 0 | 1.7 | 0 |
| konzervativní | 2040 | 917.7 | 383.5 | -534.2 | 456.3 | 0 | 0 | 3.7 | 0 |
| konzervativní | 2050 | 948.9 | 406.4 | -542.5 | 612.3 | 0 | 0 | 4.6 | 0 |

### Energie a rozsah Dopadové studie

| Cesta | Rok | Zimní zatížení v rozsahu Dopadové studie, MW | Spotřeba podle křivek, GWh | Výroba podle křivek, GWh |
|---|---|---|---|---|
| progresivní | 2025 | 1070.3 | 7070.0 | 2805.2 |
| progresivní | 2030 | 1168.3 | 7512.0 | 3015.8 |
| progresivní | 2040 | 1481.0 | 10431.9 | 4499.3 |
| progresivní | 2050 | 1626.3 | 14332.4 | 8331.8 |
| konzervativní | 2025 | 1070.3 | 7070.0 | 2805.2 |
| konzervativní | 2030 | 1118.3 | 7289.6 | 3145.1 |
| konzervativní | 2040 | 1221.6 | 8119.6 | 3468.7 |
| konzervativní | 2050 | 1226.5 | 8320.0 | 4138.7 |

Hodnoty jsou odhady pro výchozí nastavení a tabulka nemá pásmo. Bilance je dostupný výkon minus zatížení. Záporná hodnota říká, kolik MW je třeba dovézt, ne zda je to možné. Baterie nejsou v hlavní bilanci, protože nejsou zdroj. Potřeba elektrolýzy vychází z řádků výroby vodíku a výroby syntetického plynu, ten má podle volby modelu č. 31 nulu. Energie v této tabulce vychází z křivek modelu, ne přímo ze sloupců P50 2030 a P50 2040 v části 5, důvod je v úvodu části 5.

### Dorovnání na soběstačnost, rok 2050

Soběstačnost je zde roční bilance, ne pokrytí v každé hodině. Přepočet nemění výchozí hodnoty položek. Používá 1 051,2 hodiny ročně u fotovoltaiky a 2 744,7 hodiny u větru. Nejrychlejší nárůst v minulosti byl 82,8 GWh za rok u fotovoltaiky a 23,9 GWh za rok u větru. Potenciál větru v kraji je podle Dopadové studie 2 014 MW. Slunce a vítr se v zimní špičce počítají nulou, takže dorovnání roční energie zimní schodek neřeší.

| Cesta | Výroba, GWh | Spotřeba, GWh | Schodek, GWh | Jen fotovoltaika navíc, GWp | Jen vítr navíc, GW | Tempo navíc, GWh za rok |
|---|---|---|---|---|---|---|
| Progresivní | 8 331,8 | 14 332,4 | 6 000,6 | 5,7 | 2,2 | 240,0 |
| Konzervativní | 4 138,7 | 8 320,0 | 4 181,3 | 4,0 | 1,5 | 167,3 |

## 4. Metoda

### Rozklad položky a stupeň důkazu

Roční elektřina je činnost krát intenzita, například instalované MW krát vyrobené MWh na MW. Každá položka začíná hodnotou za rok 2025. Pokud ERÚ položku neuvádí zvlášť, začíná od nejlepšího dostupného rozdělení. Pro roky 2030, 2040 a 2050 má položka hodnoty P10, P50 a P90, zdroj a stupeň důkazu.

### Křivka položky

Každá položka má tvar y(t) = D(t) · s(t), kde s(t) = s₀ + (s_T − s₀) · S(t).

- S(t) je logistická křivka 1 / (1 + exp(−k (t − t_m))), normovaná tak, že S(2025) = 0 a S(2050) = 1. Střed t_m se při výpočtu drží v rozmezí 2025 − 5/k až 2050 + 5/k.
- D(t) je vnější řídicí vliv s indexem D(2025) = 1, mezi roky 2025, 2030, 2040 a 2050 lineárně (část 6). Položka bez vlivu má D(t) = 1.
- s₀ je základ 2025. Cíl je s_T = y(2050) / D(2050). Sloupce P10 až P90 obsahují y včetně D a D se na ně znovu nenásobí.
- Plynulá položka: k a t_m se dopočtou metodou nejmenších čtverců z hodnot pro roky 2030 a 2040. Meze jsou t_m od 2015 do 2060 a k od 0,08 do 3.
- Velká událost: strmá S-křivka s k = 4 a t_m v roce události.
- Položka, která vzroste a klesne: součet dvou S-křivek s k = 0,5. První amplituda je 1,15 × (vrchol − základ), druhá dorovná cíl.
- Záporná položka úspor zůstává záporná, ostatní položky se oříznou na nulu.

### Člen odchylky

Změna cíle se přičítá členem (y_T,nové − y_T,výchozí) · σ(x), kde x = (t − 2030) / 20 omezené na 0 až 1 a σ(x) = 3x² − 2x³. Do roku 2030 tak křivka zůstává a v roce 2050 přesně trefí nový cíl. Člen používá posuvník na stránce a simulace u položek bez změny tvaru.

### Monte Carlo

- Simulace po letech, 10000 běhů, pevné semínko 20261104. Výroba a spotřeba se počítají zvlášť pro každou cestu.
- Cíl položky v roce 2050: y = P50 + (z / z₉₀) · (P90 − P50) pro z ≥ 0 a y = P50 + (z / z₉₀) · (P50 − P10) pro z < 0, kde z₉₀ = Φ⁻¹(0,9). Jedna položka drží v čase stejný kvantil.
- Společné faktory: elektrifikace, povolování, cena. Pro položku s faktorem je z = √0,6 · f + √(1 − 0,6) · e, kde f je los faktoru a e vlastní los. Položka bez faktoru má z = e. Počasí jako společný faktor v modelu není.
- Načasování plynulé položky: t_m se posune o z_t · 3 / z₉₀ let, tedy P10 až P90 o 3 roky kolem výchozího roku, nezávisle na faktorech.
- Načasování události: rok se losuje z P10, P50 a P90 roku stejným předpisem. Událost po roce 2050 se do roku 2050 neprojeví. Rok se v simulaci losuje pro každý řádek zvlášť, posuvník na stránce ho naopak sdílí.
- Ztráty v sítích se nesimulují přímo vedle ostatních položek. Jejich běh se násobí poměrem součtu ostatní spotřeby v běhu k výchozímu součtu.
- Pásmo je percentil 10, 50 a 90 součtu v každém roce. Celkový součet nikdy nevzniká sečtením P90 všech položek, protože by to pásmo přehnalo. Pásmo platí jen pro výchozí nastavení.

### Čtení meze a událostí v tabulce

- Vysoký los faktoru znamená rychlejší elektrifikaci, rychlejší povolování a vyšší cenu energií. U řádků hutní plyny, zemní plyn: stávající kogenerace, přímotopy a úspory a účinnost se kvantil faktoru čte obráceně.
- U skokových řádků Třinecké železárny, hutní plyny a energetické využití odpadu se hladina mezi milníky mění. Čtení: základ do skok_rok, potom skok na první milník v roce skok_rok nebo později, dále plynule mezi milníky.

### Převod na výkon: dva okamžiky

**Zimní špička.** Roční maximum zatížení v nejchladnějším období, počítané se slunečním výkonem nula, tedy zimní podvečer. Dopadová studie řeší stejný stav (s.56 až 57, s.73).

Měření tento okamžik upřesňuje. Celostátní zimní maxima 2023 až 2026 padla vždy mezi 8:45 a 13:15, ani jednou večer (ERÚ, kap. 9.1), a FVE tehdy dodávaly až 1 445,9 MW (19. 2. 2025, 8:45). Na grafech dne maxima se večerní zatížení drží zhruba o 5 až 10 % níž (ERÚ 2025 Q1 a 2026 Q1, s.37, odečteno z grafu). Večer je ale nejhorší pro bilanci, protože slunce nedodává nic. Skládáme tedy zatížení ročního maxima se slunečním výkonem nula. Pro dnešek je to o něco přísnější než skutečný večer. Dopadová studie dělá totéž, když FVE do špičky nepočítá.

**Letní poledne.** Slunečné poledne o víkendu, červen až srpen. Letní maximum ČR (červen až srpen, 2023 až 2026) padá v pracovní dny na 11:30 až 13:15, poledne pracovního dne je tedy letní špička, ne minimum. Odděleného odpoledního maxima v datech není. Nejnižší zatížení je v noci, kolem 3:30 až 5:45, ale tehdy nesvítí. Pro přebytek je proto správná volba poledne s nízkou spotřebou, tedy víkend. Medián denního maxima o víkendu je 0,926 až 0,936 ročního průměru, v pracovní den 1,111 až 1,128 (2024, 2025). Denní maximum víkendu je horní odhad poledne.

### Vzorec výkonu

- Spotřeba: MW = GWh × 1000 / 8 760 × koeficient.
- Výroba: MW = GWh × 1000 / 8 760 × dosažitelnost × 8 760 / hodiny řádku. Je to totéž jako instalované MW × dosažitelnost.
- Bilance = dostupný výkon − zatížení, rovnice 4 studie.
- Kontrolní tabulka bere GWh z křivek modelu, stejných jako na stránce, a P50 2050. Sčítání koeficientů P90 přes položky by pásmo přehnalo, tabulka je proto jen P50.

### Flexibilní zátěže

| Položka | Zimní špička | Letní poledne |
|---|---|---|
| Řádky výroba vodíku a výroba syntetického plynu | vypnuto, sklad přečká špičku | potřebný výkon = GWh / plné hodiny, P50 3 000 h, rozpětí 2 000 až 4 000 h |
| Elektrokotle | vypnuto, Dopadová studie s.165: „V zimním období se průmyslové elektrokotle příliš neuplatní“ | 30 % výkonu, teplo v létě je jen ohřev vody |
| Baterie | jen ve zvláštním sloupci s bateriemi | denní blok 1 GWh (Dopadová studie s.145) za 5 h = 200 MW, konzervativní 20 MW |

Přebytek se rozdělí v pořadí baterie, elektrokotle, elektrolýza. Sloupec Zbývá pro vodík je to, co zbude, nejvýš potřeba elektrolýzy. Vypnutí elektrolýzy v zimě je předpoklad o skladu vodíku, zatím nepodložený. Bez něj by zimní bilance byla horší o stovky MW.

**Baterie.** Energie je ze spotřeby progresivní cesty bez pružných položek: 10 618,0 GWh / 365 × 3 = 87,3 GWh, konzervativní 10 % = 8,73 GWh. Výkon je odvozen tak, aby úložiště vydrželo uvedené 3 dny: 87,3 GWh / 72 h = 1 212,1 MW, konzervativní 121,2 MW. Definice cest výkon neuvádí, je to výklad modelu. Zdroj pro něj není, stupeň D. Dopadová studie s.145 uvažuje 1 GW a 1 GWh, tedy jinou dobu. Starší roky: 10 MW (2025, s.145), 50 MW (2030, s.145), konzervativní 2030 25 MW úsudkem, 2040 poměrem ze řádku ztrát. Hlavní bilance baterie nezapočítává, protože nejsou zdroj. Sloupec Výdrž baterií říká, jak dlouho pokryjí deficit.

### Výchozí stav a ztráty v sítích

| Kontrola | Výsledek |
|---|---|
| Tab. 6.1, součet 4 čtvrtletí 2025 | 2 805,1634 GWh, shoda |
| Tab. 6.3, součet 4 čtvrtletí 2025 | 6 850,6486 GWh, shoda |
| Součet sloupců proti Celkem | ERÚ se liší o 0,1 MWh vlivem zaokrouhlení; dorovnáno v rezidualních řádcích |
| Ztráty nad tab. 6.3 | 219,3158 GWh, spotřeba celkem 7 069,9644 GWh |

ERÚ Roční zpráva 2025 (tab. 4.1, 4.3) uvádí vyšší hodnoty: výroba 2 814,8131 GWh (rozdíl 9,6 GWh, hlavně FVE), spotřeba 6 855,0524 GWh (rozdíl 4,4 GWh). Základ zůstává na čtvrtletních zprávách. Palivový rozklad bere Roční zprávu, tab. 4.5, s. 20, protože čtvrtletní zprávy paliva po krajích nemají. Tato tabulka je stupeň A a nahradila odhad z Dopadové studie Tab. 4.

- Báze sazby 3,547 % je spotřeba na prahu sítě, ne netto. Dopadová studie Tab. 1 s. 27: 6 018,9 − 5 805,4 = 213,5 a 213,5 / 6 018,9 = 3,547 %. Rovnice 7 na s. 74 má stejný tvar.
- Sazba je za bývalý Severomoravský kraj od ČEZ Distribuce (s. 74), MSK se nesleduje.
- Tab. 6.3 ztráty v sítích neobsahuje. ERÚ je dává jen do TBS (definice v každé zprávě, kap. 1) a celostátně je součet tab. 6.3 (56 871,0 GWh) menší než Spotřeba ČR bez ztrát (58 152,4 GWh).
- Výpočet: 5 963,8184 × 3,547 % / (1 − 3,547 %) = 219,3 GWh. Báze je tab. 6.2, protože rozdíl 6.3 − 6.2 (886,8 GWh) je lokální a vlastní spotřeba, která sítí neteče. Toto je volba modelu. Na bázi 6.3 by ztráty byly o cca 33 GWh vyšší.

### Rozsah: čistá spotřeba proti sektorům

Dopadová studie počítá zatížení z užší čisté spotřeby (tab. 6.2) a dosažitelný výkon snižuje o vlastní spotřebu a přímé dodávky (s.150). Tento model má spotřebu z tab. 6.3 plus ztráty a výrobu brutto. Rozdíl 6.3 − 6.2 je lokální a vlastní spotřeba: 1 284,9 GWh v 2023 a 886,8 GWh v 2025.

- Oba rozsahy se liší v MW zatížení a výkonu, ne v bilanci, protože lokální část je na obou stranách.
- Porovnání se studií proto vede přes zimní zatížení v rozsahu Dopadové studie = zatížení − 886,8 GWh × 1000 / 8 760 × 1,143 = zatížení − 115,7 MW. Koeficient 1,143 je vážený průměr dvou řádků sektoru Energetika.
- Část 886,8 GWh zůstává do 2050 konstantní, zdroj pro její vývoj není.
- Výkonová tabulka (část 3) je brutto na obou stranách. Jen zimní zatížení v rozsahu Dopadové studie je v rozsahu studie. Stránka nemá mísit tento sloupec s dostupným výkonem.

### Výsledek kalibrace

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
3. Přímotopy a léto byly po první kalibraci opraveny podle měření, ne podle cíle. Před úpravou vyšla zima +5,8 % a léto −22,8 %. Sezónní výkyv MOO + MOP je jen 522,1 GWh, zatímco řádky čerpadel a přímotopů mají 1 374,3 GWh. Řádek přímotopů vychází z tarifů (Tab.26) a nese tedy hlavně běžnou spotřebu. VO z vvn a vn mají poměr léto / rok 0,984, proto průmysl v létě 0,95.

**Proč 2025 nesedí přesně.** Hodnota +1,7 MW v Obr. 35 je prognóza z 2024 a počítá s TAMEH 229 MW, který ERÚ v březnu 2025 odebral, a s menší spotřebou. Není to měření. Řádky GWh × koeficient navíc dají o 53,0 MW méně výkonu než instalované MW (1 062,0 proti 1 115,0): ERÚ uvádí PSE 181,3 MW, řádky s hodinami z Tab.18 dají méně. Oprava by v 2050 poškodila řádek zemního plynu, proto zůstává.

**Nezávislé kontroly.**

- Celostátní poměr maxima k průměru je 1,5306 (2024) a 1,5132 (2025), z toho τ 5 739 a 5 789 h. Studie má 8 760 / 5 869 = 1,4926. Odchylka 1,4 až 2,6 % je stejného řádu jako chyba 2025.
- Dosažitelnost 0,825 na úbytku v Obr. 35: mezi 2023 a 2024 ubylo TAMEH 144 MW a menší zdroje 8 MW, Tab.29. 152 × 0,825 = 125 MW proti změně bilance −123,8 MW, ta ale obsahuje i růst zatížení.
- Měsíční poměr MSK proti ČR: leden 2025 1,127 proti 1,157, léto 0,903 proti 0,877. Kraj je plošší než ČR, letní cíl to bere v potaz přepočtem 1,029.

**Výkon v létě.** Měřené ERÚ za ČR, ne za kraj, při letních maximech 2024 až červen 2026: FVE ze 7 měsíců 0,525 / 0,619 / 0,640 instalovaného výkonu, vítr ze 6 měsíců 0,066 / 0,182 / 0,255. Hodnota větru za srpen 2024 v extrahovaném textu chybí. Paroplyn při letních maximech 2024 až 2025 běžel 0 MW, proto mají nové plynové bloky v létě P50 nula a jejich výkon je ve sloupci Rezerva v řízeném plynu. Elektrolýza z plynu nedává smysl.

**Vítr v zimě.** P10 a P50 jsou nula podle pravidla studie s.73, stejně jako slunce. Není to medián. Změřený medián při 14 zimních maximech ČR je 0,192 instalovaného výkonu, P10 0,034, P90 0,316. Do P90 jde měřená hodnota a tabulka má sloupec Bilance s měřeným větrem.

### Křížová kontrola 2050 se scénáři Dopadové studie

Jde jen o kontrolu proti jiným scénářům. Cílem není se s nimi shodovat.

| | Zatížení, rozsah studie | Dostupný výkon | Bilance |
|---|---|---|---|
| Dopadová studie očekávaný, Obr. 36 | 7 229,9 / (1 − 0,03547) / 5 869 = 1 277,2 MW | 1 325,4 MW | +48,2 MW |
| Dopadová studie extrémní, Obr. 40, Tab.46 | 1 752,0 MW | 1 731,5 − 378,0 = 1 353,5 MW | −398,5 MW |
| Progresivní cesta | 1626,3 MW | 566,2 MW | -1060,1 MW; s bateriemi 152,0 MW po 82,3 h; s měřeným větrem -940,3 MW |
| Konzervativní cesta | 1226,5 MW | 713,1 MW | -513,4 MW; s bateriemi -392,2 MW; s měřeným větrem -495,6 MW |

Dostupný výkon cest je po odečtení lokální části 115,7 MW, aby šel srovnat se studií. Hlavní příčiny rozdílu jsou v cestách: progresivní cesta má 433 MW plynu místo 683 MW, konzervativní nemá SMR. Přesný rozklad zbytku není k dispozici, Dopadová studie dosažitelný výkon po zdrojích pro 2050 netiskne. Obr. 36 a 40 Dětmarovice nepočítají, ty přidává až Tab.46. Metoda studie s τ na celé energii by dala progresivní cestě (14332,4 − 886,8) / 5,869 = 2290,9 MW, protože by započetla i elektrolýzu ve špičce.

**Léto 2050.** Progresivní cesta má přebytek 524,5 MW. Po bateriích a elektrokotlích zbývá elektrolýze 279,5 MW z potřebných 1166,7 MW. Polední přebytek sám roční objem vodíku nepokryje, stejně jako měsíční bilance v měsíční tabulce (část 8), kde schodek trvá celý rok. Konzervativní cesta má -542,5 MW a přebytek nemá, řízený plyn v záloze je 612,3 MW.

Dopadová studie netto 2050: očekávaný 7 229,9 GWh (Obr. 28), extrémní 9 917,3 GWh (Obr. 38, přiřazení barvy je výklad modelu), obojí bez 887 GWh lokální části a ztrát. Spotřeba progresivní cesty je výrazně vyšší. Hlavní důvody jsou výroba vodíku pro flotilu, datacentra a plná elektrifikace oceli, které studie nemá nebo má méně.

### Fyzikální meze

| Mez | Hodnota | Stav |
|---|---|---|
| FVE potenciál | „až 165 GW p“, Dopadová studie s. 136 | P90 2050 je řádově pod ním, skutečná mez je síť, ta není číselně známa |
| Vítr potenciál | „až 2 014 MW“, s. 135 | P90 1 200 MW je pod mezí |
| Biomasa | „prakticky vyčerpán“, s. 169 | model drží 432 GWh, P90 568,5 |
| Malé vodní | spád „téměř vyčerpán“, s. 134 | bez nového výkonu |
| Tepelná čerpadla | 163 913 rodinných domů, s. 114 | regrese by dala 180 040 OM, omezeno na 97 % domů |
| Geotermální | s. 89 | nula |

Kapacita sítě a dostupnost tepelných čerpadel nejsou číselně ověřeny.

### Co je ve výkonové bilanci stupeň D

Ve výkonových koeficientech je z 94 řádků 55 D, 31 C, 8 B, žádný A. Tyto počty se liší od počtů v části 1, protože jde o jiné vstupy.

Stupeň A nemá žádný řádek, protože každý přenáší měření na budoucí stav.

- Všechny koeficienty spotřeby kromě čerpadel. Měřený je jen celek a skupiny VO a maloodběr, ne položky.
- Největší vliv: osobní auta a nákladní doprava (večerní nabíjení), přímotopy, plné hodiny elektrolýzy, chlazení, výkon baterií.
- Hodnoty pro řádky se stupněm D jsou úsudek bez zdroje a čekají na ověření.

### Co model neukáže

- **Průběh hodin.** Dva okamžiky nejsou časová řada. Nabíjení a vybíjení baterie mezi nimi nejde sledovat.
- **Tmavé bezvětří (Dunkelflaute).** Vícedenní období bez slunce a větru s prázdnou baterií zde není, LOLE ani EENS se nepočítá. Výdrž baterie je jen podíl energie a deficitu.
- **Limity sítě.** Soustava v kraji se bere jako jeden uzel. Prezentace Město bez elektřiny ukazuje na modelové Porubě, že přenos uvnitř města může omezit dodávku dřív než součet.
- **Dovozní kapacita.** Záporná bilance říká, kolik MW je třeba dovézt, ne zda to přenosová soustava a sousedé mají. ČEPS MAF 2023 v prezentaci Město bez elektřiny s.5 uvádí LOLE a EENS za ČR v jiných scénářích, proto se nepřebírá.
- **Výpadek největšího bloku.** Kritérium n−1 pro SMR 500 MW není započtené.
- **Hodinový profil položek v kraji.** MSK maximum neměří. OTE publikuje normalizované typové diagramy po třídách, v modelu nejsou použity. Jsou nejbližším přímým zdrojem pro domácnosti a přímotopy.

### Známé nepřesnosti

- **Jeden koeficient na položku a cestu.** Hodiny plynových řádků se v řádcích mění podle roku. Nové plynové bloky progresivní 2030 asi o 50 MW výš než 93 MW × 0,9. Koeficienty míří na rok 2050.
- **Dětmarovice.** Koeficient 13,77 platí jen pro rok 2025, řádek je pak nulový.
- **FVE v 2025.** Řádek počítá 1 051 h, změřeno 926 h, takže 2025 vychází v létě o 12 % níž.
- **Skokové položky.** Výpočet modelu bere u Třince a hutních plynů jeden skok na cíl 2050, ne dva milníky. Rok události má S-křivku, v něm je tedy polovina změny.
- **Obrácené čtení faktoru.** Poznámky k tabulce předepisují u čtyř položek obrácené čtení kvantilu faktoru (viz výše). Výpočet pásma ve skriptu toto obrácení nemá, takže tyto položky se s faktorem hýbou stejným směrem jako ostatní.
- **Měsíční tabulka vodíku.** Vychází ze starších ročních součtů, viz část 8.

### Selhání proložení křivky

Kontrola porovnává plynulé položky. Uvedené řádky nesedí na tabulku v milníku o více než 10 % a 25 GWh. Hodnoty jsou převzaté z kontrolního výstupu modelu v GWh. Skokové položky tato kontrola nezahrnuje, viz úvod části 5.

| Položka | Cesta | Rok | Tabulka | Křivka |
|---|---|---|---|---|
| nové plynové bloky | konzervativní | 2030 | 896.8 | 671.0 |
| nové plynové bloky | konzervativní | 2040 | 1372.1 | 1632.8 |

## 5. Všechny položky

Každá položka má tabulku pro obě cesty v GWh za rok a pod ní odrážky. Pokud se text mezi cestami neliší, je uveden jednou. Prázdná pole jsou vynechána.

**Jak číst sloupce P50 2030 a P50 2040.** U skokových položek je to hladina po události, ne hodnota v daném roce. Například SMR má v progresivní cestě P50 2030 3942, ale rok spuštění má P50 2045, takže křivka v roce 2030 dává nulu. Základ platí do roku události, potom přichází hladina. Výpočet na stránce bere u skokových položek jeden skok na cíl 2050. Proto se tyto sloupce nesmí sčítat do ročního součtu pro roky 2030 a 2040. Pro ně platí energie podle křivek v části 3.

**Slova v odvozeních.** „Ze studie“ znamená Dopadovou studii, pokud není řečeno jinak. „Očekávaný“ a „extrémní“ jsou její scénáře. „Odečteno z grafu“ znamená, že číslo není v tisku, ale je čteno z obrázku. Strany jsou strany PDF.

**Zkratky.** ERÚ Energetický regulační úřad; ČSÚ Český statistický úřad; FVE fotovoltaika; VTE větrná elektrárna; VE vodní elektrárna; PE parní elektrárna; PSE paroplynová elektrárna; PPE paroplynová a plynová elektrárna; JE jaderná elektrárna; EDĚ Elektrárna Dětmarovice; TČ tepelné čerpadlo; OM odběrné místo; RD rodinný dům; VO velkoodběr; MOO a MOP maloodběr obyvatel a podnikatelů; DV dosažitelný výkon; TBS tuzemská brutto spotřeba; TVS, TVSe a TVSt technologická vlastní spotřeba, u výroby elektřiny a u výroby tepla; BEV bateriové vozidlo; FCHEV vodíkové vozidlo s palivovým článkem; COP topný faktor; SMR malý modulární reaktor; ZEVO zařízení na energetické využití odpadu.

**Historické maximum tempa** je největší změna za rok nalezená v historii. U fotovoltaiky pozemní je to průměr 2008 až 2012, protože roční maximum není v tisku a dělení fotovoltaiky v historii neexistuje.

### Výroba

#### černé uhlí: Dětmarovice

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 360.7952 | 0 | 0 | 0 | 0 | 0 | C |
| konzervativní | 360.7952 | 0 | 0 | 0 | 0 | 0 | C |

- **Meze 2030 a 2040, progresivní:** 2030 P10 0, P90 0; 2040 P10 0, P90 0
- **Meze 2030 a 2040, konzervativní:** 2030 P10 0, P90 0; 2040 P10 0, P90 0
- **Průběh:** skok
- **Společný faktor:** cena
- **Událost, progresivní:** Konec Elektrárny Dětmarovice, rok P10 2026, P50 2026, P90 2026
- **Událost, konzervativní:** Konec Elektrárny Dětmarovice, rok P10 2026, P50 2026, P90 2026
- **Jak se došlo:** Elektrárna je odstavená a o její další výrobě žádný zdroj nemluví, proto 0 GWh.
- **Ze zdrojů:** Dopadová studie, s. 103 a Tab. 29 s. 130; Český rozhlas Ostrava 12. 6. 2025
- **Odhad:** žádný
- **Podrobné odvození:** Ze studie: odstavení a výkon 600 MW. Vlastní krok a jiné zdroje: základ = součet (PE měsíc 2025 − PE týž měsíc 2026) za leden až březen: (308 102,3−175 709,7)+(322 193,6−156 562,5)+(211 308,3−148 536,8) MWh = 360,7952 GWh. Po uzavření 0 MW × 0 h = 0.
- **Zdroj:** ERÚ, čtvrtletní zprávy 2025 Q1 a 2026 Q1, tab. 7.8 (PE, měsíce); Dopadová studie s.103 (odstavení k 30.4.2025), Tab.18 s.100 (600,0 MW); https://ostrava.rozhlas.cz/detmarovice-ukoncily-eru-vykonneho-cernouhelneho-teplarenstvi-v-cesku-9493534 (12.6.2025)
- **Strana:** s.103; Tab.29 s.130; s.151
- **Citace:** očekávaný: „ČEZ, a.s. rozhodl o definitivním odstavení EDĚ k 30.4. 2025“; Tab.29 600,0 MW do 2026, 0,0 od 2027
- **Poznámka:** Dopadovou studii nelze použít: Základ není ve studii, ta končí 2023. Rok 2026 je první celý rok bez bloku. Rozhlas uvádí konec výroby na jaře 2025, ERÚ snižuje výkon o 600 MW až v březnu 2026. Základ je odhad z rozdílu měsíců, zahrnuje i vliv počasí. Zlepší: výroba EDĚ 2025 od ČEZ. Studie p.189 počítá se zálohou 567,0 MW, ta zde není, protože zdroje uvádějí demolici.
- **Koeficient, progresivní:** zima P10 9.6148, P50 13.7666, P90 13.7666; léto P10 0.0000, P50 0.0000, P90 0.0000; flexibilní ne; stupeň B
- **Koeficient, konzervativní:** zima P10 9.6148, P50 13.7666, P90 13.7666; léto P10 0.0000, P50 0.0000, P90 0.0000; flexibilní ne; stupeň B
- **Koeficient, odvození:** dosažitelný výkon 567,0 MW / (360,7952 GWh × 1000 / 8 760 = 41,2 MW) = 13,767. Platí jen pro 2025, záložní blok s malou výrobou.
- **Koeficient, zdroj:** Dopadová studie Tab.46 s.189; ERÚ, čtvrtletní zpráva 2025 Q1
- **Koeficient, strana:** Tab.46 s.189
- **Koeficient, citace:** Tab.46 „dosažitelný výkon EDĚ MW 567,0“
- **Koeficient, poznámka:** V létě 0: po březnu 2025 nevyrábí. Metoda GWh × koeficient zde nedává smysl mimo rok 2025.

#### černé uhlí: teplárny a průmysl

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 759.1048 | 0 | 0 | 0 | 0 | 0 | C |
| konzervativní | 759.1048 | 0 | 0 | 0 | 0 | 0 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 0, P90 0; 2040 P10 0, P90 0
- **Meze 2030 a 2040, konzervativní:** 2030 P10 0, P90 0; 2040 P10 0, P90 0
- **Průběh:** skok
- **Společný faktor:** cena
- **Událost, progresivní:** Konec uhlí v teplárnách, rok P10 2029, P50 2030, P90 2033
- **Událost, konzervativní:** Konec uhlí v teplárnách, rok P10 2030, P50 2032, P90 2036
- **Jak se došlo, progresivní:** Uhlí v teplárnách a průmyslu skončí, střední rok konce je 2030, proto 0 GWh.
- **Jak se došlo, konzervativní:** Uhlí v teplárnách a průmyslu skončí, střední rok konce je 2032, proto 0 GWh.
- **Ze zdrojů:** Dopadová studie, s. 131 (Třebovice 2030); Vnitrostátní plán, s. 28 a s. 339 (uhlí do 2033)
- **Odhad, progresivní:** Rok konce mimo Třebovice je zjednodušení. Hodnotu 2050 neovlivní.
- **Odhad, konzervativní:** Pozdější rok konce je úsudek. Hodnotu 2050 neovlivní.
- **Podrobné odvození:** Ze studie: rok 2030 pro Třebovice. Vlastní krok a jiné zdroje: základ = černé uhlí MSK 2025 1 119,9 GWh − Dětmarovice 360,7952 GWh = 759,1048 GWh. Po konci uhlí 0 MW × 0 h = 0.
- **Zdroj:** ERÚ Roční zpráva 2025, tab. 4.5, s. 20, https://eru.gov.cz/sites/default/files/obsah/prilohy/eruelektro2025.pdf; Vnitrostátní plán s.28 a s.339 (uhlí do roku 2033); Dopadová studie s.131 (Třebovice konec uhlí 2030); https://oenergetice.cz/teplarenstvi/veolia-energie-chysta-modernizaci-teplarny-karvina-za-miliardu-kc
- **Strana:** s.131; Tab.4 s.36
- **Citace:** očekávaný: „tak, aby v roce 2030 mohlo být v ETB ukončeno spalování uhlí“; Tab.4 Černé uhlí 1 910,8 (2023)
- **Poznámka, progresivní:** Jde o více zdrojů, skok je zjednodušení postupného konce 2029 až 2033. Mezi horní mezí 2033 a skutečností stojí nejasný rok v Karviné (neověřené zprávy 2028 až 2030).
- **Poznámka, konzervativní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Stejný zákonný a cenový tlak, pozdější konec je úsudek. Vnitrostátní plán s.346 ponechává zbytkové černé uhlí jen pro průmysl.
- **Koeficient, progresivní:** zima P10 2.1250, P50 2.6568, P90 3.0587; léto P10 0.5000, P50 0.7901, P90 1.1000; flexibilní ne; stupeň C
- **Koeficient, konzervativní:** zima P10 2.1250, P50 2.6568, P90 3.0587; léto P10 0.5000, P50 0.7901, P90 1.1000; flexibilní ne; stupeň C
- **Koeficient, odvození:** Zima: dosažitelnost 0,825 z kalibrace na DV 2023. a_kal = (1024,6 + 167,6 − 567,0 − 18,5 × 0,428) / (648,4 + 99,7) = 0,825. koef = dosažitelnost × 8 760 / 2721 h: 0,825 × 8 760 / 2721 = 2,657. Léto: PE MSK červen až srpen 2025 139,2 MW / (1904,3 − 360,8 GWh) × 1000 / 8 760 = 0,790.
- **Koeficient, zdroj:** Dopadová studie s.73, s.129, s.150; ERÚ, čtvrtletní zprávy 2025 tab. 7.8
- **Koeficient, strana:** rov.4 s.73; Tab.28 s.129; s.150
- **Koeficient, citace:** „Za stabilní zdroje se nepovažují intermitentní zdroje (FVE a VTE)“
- **Koeficient, poznámka:** Hodiny 2721 h: 1113,3 GWh / (473,2 − 64,0 MW), ERÚ prosinec 2025 bez Dětmarovic a biomasy. Stejný poměr v roce 2023 neplatí.

#### hnědé uhlí

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 41.1 | 0 | 0 | 0 | 0 | 0 | C |
| konzervativní | 41.1 | 0 | 0 | 0 | 0 | 0 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 0, P90 0; 2040 P10 0, P90 0
- **Meze 2030 a 2040, konzervativní:** 2030 P10 0, P90 0; 2040 P10 0, P90 0
- **Průběh:** skok
- **Společný faktor:** cena
- **Událost, progresivní:** Konec hnědého uhlí, rok P10 2028, P50 2030, P90 2033
- **Událost, konzervativní:** Konec hnědého uhlí, rok P10 2029, P50 2031, P90 2035
- **Jak se došlo, progresivní:** Hnědé uhlí skončí, střední rok konce je 2030, proto 0 GWh.
- **Jak se došlo, konzervativní:** Hnědé uhlí skončí, střední rok konce je 2031, proto 0 GWh.
- **Ze zdrojů:** Vnitrostátní plán, s. 28 a s. 339 (uhlí do 2033)
- **Odhad:** Rok konce je úsudek. Hodnotu 2050 neovlivní.
- **Podrobné odvození:** Ze studie: nic pro výhled. Vlastní krok a jiné zdroje: základ = hnědé uhlí MSK 2025 41,1 GWh (změřeno). Po konci 0.
- **Zdroj:** ERÚ Roční zpráva 2025, tab. 4.5, s. 20, https://eru.gov.cz/sites/default/files/obsah/prilohy/eruelektro2025.pdf; Vnitrostátní plán s.28, s.339; Dopadová studie s.36 (používá se ve středních a menších zdrojích tepla)
- **Strana:** Tab.4 s.36; s.36
- **Citace:** Tab.4 Hnědé uhlí 133,6 (2023); pouze statistika, výhled studie neuvádí
- **Poznámka, progresivní:** Dopadovou studii nelze použít: Výhled pro hnědé uhlí studie neuvádí, proto Vnitrostátní plán. Rok je úsudek v rámci limitu 2033 z Vnitrostátního plánu.
- **Poznámka, konzervativní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Dopadovou studii nelze použít: Výhled pro hnědé uhlí studie neuvádí, proto Vnitrostátní plán. Rok je úsudek.
- **Koeficient, progresivní:** zima P10 2.1250, P50 2.6568, P90 3.0587; léto P10 0.5000, P50 0.7901, P90 1.1000; flexibilní ne; stupeň C
- **Koeficient, konzervativní:** zima P10 2.1250, P50 2.6568, P90 3.0587; léto P10 0.5000, P50 0.7901, P90 1.1000; flexibilní ne; stupeň C
- **Koeficient, odvození:** Zima: dosažitelnost 0,825 z kalibrace na DV 2023. a_kal = (1024,6 + 167,6 − 567,0 − 18,5 × 0,428) / (648,4 + 99,7) = 0,825. koef = dosažitelnost × 8 760 / 2721 h: 0,825 × 8 760 / 2721 = 2,657. Léto: PE MSK červen až srpen 2025 139,2 MW / (1904,3 − 360,8 GWh) × 1000 / 8 760 = 0,790.
- **Koeficient, zdroj:** Dopadová studie s.73, s.129, s.150; ERÚ, čtvrtletní zprávy 2025 tab. 7.8
- **Koeficient, strana:** rov.4 s.73; Tab.28 s.129; s.150
- **Koeficient, citace:** „Za stabilní zdroje se nepovažují intermitentní zdroje (FVE a VTE)“
- **Koeficient, poznámka:** Hodiny 2721 h: 1113,3 GWh / (473,2 − 64,0 MW), ERÚ prosinec 2025 bez Dětmarovic a biomasy. Stejný poměr v roce 2023 neplatí.

#### zemní plyn: stávající kogenerace

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 159.4 | 20 | 60 | 245 | 155.0 | 207.4 | D |
| konzervativní | 159.4 | 150 | 244.8 | 400 | 155.0 | 207.4 | C |

- **Meze 2030 a 2040, progresivní:** 2030 P10 120, P90 180; 2040 P10 90, P90 245
- **Meze 2030 a 2040, konzervativní:** 2030 P10 130, P90 190; 2040 P10 130, P90 260
- **Průběh:** plynule
- **Společný faktor:** elektrifikace
- **Jak se došlo, progresivní:** Zbytek výkonu nahrazuje syntetický plyn, na zemní plyn zůstává 27,5 MW × 2 183 h za rok = 60 GWh.
- **Jak se došlo, konzervativní:** 3,4 % podíl kogenerace × 7,2 TWh celkové výroby ve studii = 244,8 GWh.
- **Ze zdrojů, progresivní:** Dopadová studie, Tab. 18 s. 100 (2 183 h)
- **Ze zdrojů, konzervativní:** Dopadová studie, Obr. 33 s. 125 (3,4 %, odečteno z grafu), s. 124 (7,2 TWh)
- **Odhad, progresivní:** 27,5 MW je úsudek bez zdroje.
- **Odhad, konzervativní:** Žádné číslo. Že konzervativní cesta bere tuto horní hodnotu, je naše volba.
- **Podrobné odvození, progresivní:** Ze studie: 71,0 MW, 2 183 h, 3,4 %, 7,2 TWh. Vlastní krok a jiné zdroje: základ = zemní plyn MSK 2025 159,4 GWh. 2030: 71,0 MW × 2 183 h = 155,0. 2040: 95 MW (lineárně 71,0 na cca 120) × 2 183 h = 207,4. 2050 horní: 3,4 % × 7,2 TWh = 244,8. Progresivní 2050 P50: 27,5 MW × 2 183 h, zbytek nahrazen syntetickým plynem; tento krok nemá zdroj.
- **Podrobné odvození, konzervativní:** Ze studie: 71,0 MW, 2 183 h, 3,4 %, 7,2 TWh. Vlastní krok a jiné zdroje: základ = zemní plyn MSK 2025 159,4 GWh. 2030: 71,0 MW × 2 183 h = 155,0. 2040: 95 MW (lineárně 71,0 na cca 120) × 2 183 h = 207,4. 2050 horní: 3,4 % × 7,2 TWh = 244,8.
- **Zdroj:** ERÚ Roční zpráva 2025, tab. 4.5, s. 20, https://eru.gov.cz/sites/default/files/obsah/prilohy/eruelektro2025.pdf; Dopadová studie Tab.34 s.138, Tab.18 s.100 (2 183 h), Obr.33 s.125
- **Strana:** Tab.34 s.138; Tab.18 s.100; Obr.33 s.125
- **Citace:** očekávaný: Tab.34 71,0 MW (2030); Tab.18 KJ na zemní plyn 2 183 h (2023); „cca 120 MW“ (s.138); Obr.33 popisek 3,4 % (odečteno z grafu); „cca 7,2 TWh“ (s.124) (tabulka jako obrázek)
- **Poznámka, progresivní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Výroba jde za teplem, takže přechod na tepelná čerpadla ji snižuje. ERÚ neuvádí, kolik plynu hoří v PE, celý objem je přiřazen sem. Kvantil faktoru se zde čte obráceně.
- **Poznámka, konzervativní:** Konzervativní cesta drží teplo ve spalování, proto vyšší. volba modelu č. 4: 90 % zemní plyn se uplatňuje na nové bloky, viz řádek nové plynové bloky. Kvantil faktoru se zde čte obráceně.
- **Koeficient, progresivní:** zima P10 2.6485, P50 3.3113, P90 3.8122; léto P10 0.4013, P50 1.0032, P90 1.6051; flexibilní ne; stupeň C
- **Koeficient, konzervativní:** zima P10 2.6485, P50 3.3113, P90 3.8122; léto P10 0.4013, P50 1.0032, P90 1.6051; flexibilní ne; stupeň C
- **Koeficient, odvození:** Zima: dosažitelnost 0,825 z kalibrace na DV 2023. a_kal = (1024,6 + 167,6 − 567,0 − 18,5 × 0,428) / (648,4 + 99,7) = 0,825. koef = dosažitelnost × 8 760 / 2183 h: 0,825 × 8 760 / 2183 = 3,311. Léto: PSE ČR při letních maximech 2025 asi čtvrtina výkonu, dosažitelnost 0,25.
- **Koeficient, zdroj:** Dopadová studie Tab.18 s.100; ERÚ, čtvrtletní zprávy tab. 9.3
- **Koeficient, strana:** rov.4 s.73; Tab.28 s.129; s.150
- **Koeficient, citace:** Tab.18 KJ na zemní plyn 2 183 h
- **Koeficient, poznámka:** Tab.18 2 183 h je z 2023. ERÚ udává PSE 181,3 MW, řádky dají méně, viz metodika.

#### hutní plyny (vysokopecní a koksárenský)

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 288.5289 | 0 | 0 | 80 | 144.3 | 144.3 | C |
| konzervativní | 288.5289 | 100 | 144.3 | 200 | 144.3 | 144.3 | C |

- **Meze 2030 a 2040, progresivní:** 2030 P10 100, P90 200; 2040 P10 100, P90 200
- **Meze 2030 a 2040, konzervativní:** 2030 P10 100, P90 200; 2040 P10 100, P90 200
- **Průběh:** skok
- **Společný faktor:** elektrifikace
- **Událost, progresivní:** Třinec: první oblouková pec, méně hutních plynů, rok P10 2030, P50 2033, P90 2040
- **Událost, konzervativní:** Třinec: první oblouková pec, méně hutních plynů, rok P10 2030, P50 2033, P90 2040
- **Jak se došlo, progresivní:** Třinec v roce 2050 plně elektrifikuje výrobu oceli a hutní plyny zmizí, proto 0 GWh.
- **Jak se došlo, konzervativní:** (1 904,3290 parní elektrárny − 1 119,9 černé uhlí − 41,1 hnědé uhlí − 430,2 biomasa − 24,6 ostatní paliva) GWh dnes × 50 % po první obloukové peci v Třinci = 144,3 GWh.
- **Ze zdrojů, progresivní:** Dopadová studie, s. 105 (jen polovina oceli do 2030)
- **Ze zdrojů, konzervativní:** ERÚ Roční zpráva 2025, tab. 4.5; Dopadová studie, s. 105 (50 % oceli)
- **Odhad, progresivní:** Plná elektrifikace do 2050 je naše čtení, zdroj ji neuvádí.
- **Odhad, konzervativní:** Základ je dopočtený zbytek, ne měření. Že 50 % oceli znamená 50 % plynů, je úsudek. 50 % elektrifikace v roce 2050 je dáno definicí cesty.
- **Podrobné odvození:** Ze studie: podíl 50 %. Vlastní krok a jiné zdroje: základ = PE 1 904,3290 − (černé uhlí 1 119,9 + hnědé uhlí 41,1 + biomasa 430,2 + ostatní paliva 24,6) = 288,5290 GWh. Po první EOP v Třinci: 288,5290 × 50 % = 144,3. Plná elektrifikace 2050 na 0.
- **Zdroj:** ERÚ Roční zpráva 2025, tab. 4.5, s. 20, https://eru.gov.cz/sites/default/files/obsah/prilohy/eruelektro2025.pdf, řádek Ostatní plyny 494,4 GWh; Dopadová studie Tab.4 s.36 (686,0 v 2023), s.105, s.141; https://www.novinky.cz/clanek/ekonomika-trinecke-zelezarny-brzdi-plany-stavba-elektricke-obloukove-pece-bude-mit-minimalne-dva-roky-zpozdeni-40518385
- **Strana:** s.105; Tab.4 s.36
- **Citace:** očekávaný: „do roku 2030 budou cca 50 % oceli vyrábět nízkoemisními technologiemi“; Tab.4 Ostatní plyny 686,0 (2023)
- **Poznámka, progresivní:** Vazba: roky jsou stejné jako u řádku Třinecké železárny. Podíl 50 % plyne z tvrzení, že EOP nahradí polovinu oceli. Koksovna Svoboda nejdříve 2034 (s.141), zbytek po ní zde není zvlášť. Kvantil faktoru se zde čte obráceně. Hutní plyny a důlní plyn jsou dvě rezidua, která se vyměňují: přebytek 31,4 GWh důlního plynu nad předpovědí 174,3 GWh může být zemní plyn spálený v PE.
- **Poznámka, konzervativní:** Konzervativní cesta 50 % elektrifikace, takže polovina zůstává i v 2050. Tatáž vazba na Třinec. Kvantil faktoru se zde čte obráceně. Hutní plyny a důlní plyn jsou dvě rezidua, která se vyměňují: přebytek 31,4 GWh důlního plynu nad předpovědí 174,3 GWh může být zemní plyn spálený v PE.
- **Koeficient, progresivní:** zima P10 2.1250, P50 2.6568, P90 3.0587; léto P10 0.5000, P50 0.7901, P90 1.1000; flexibilní ne; stupeň C
- **Koeficient, konzervativní:** zima P10 2.1250, P50 2.6568, P90 3.0587; léto P10 0.5000, P50 0.7901, P90 1.1000; flexibilní ne; stupeň C
- **Koeficient, odvození:** Zima: dosažitelnost 0,825 z kalibrace na DV 2023. a_kal = (1024,6 + 167,6 − 567,0 − 18,5 × 0,428) / (648,4 + 99,7) = 0,825. koef = dosažitelnost × 8 760 / 2721 h: 0,825 × 8 760 / 2721 = 2,657. Léto: PE MSK červen až srpen 2025 139,2 MW / (1904,3 − 360,8 GWh) × 1000 / 8 760 = 0,790.
- **Koeficient, zdroj:** Dopadová studie s.73, s.129, s.150; ERÚ, čtvrtletní zprávy 2025 tab. 7.8
- **Koeficient, strana:** rov.4 s.73; Tab.28 s.129; s.150
- **Koeficient, citace:** „Za stabilní zdroje se nepovažují intermitentní zdroje (FVE a VTE)“
- **Koeficient, poznámka:** Hodiny 2721 h: 1113,3 GWh / (473,2 − 64,0 MW), ERÚ prosinec 2025 bez Dětmarovic a biomasy. Stejný poměr v roce 2023 neplatí. Podíl uvnitř PE je rozdělen podle energie.

#### důlní plyn

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 205.728 | 0 | 0 | 30 | 160 | 80 | C |
| konzervativní | 205.728 | 0 | 0 | 30 | 160 | 80 | C |

- **Meze 2030 a 2040, progresivní:** 2030 P10 120, P90 200; 2040 P10 40, P90 120
- **Meze 2030 a 2040, konzervativní:** 2030 P10 120, P90 200; 2040 P10 40, P90 120
- **Průběh:** plynule
- **Společný faktor:** zadny
- **Jak se došlo:** Doly se zaplavují a studie odhaduje konec výroby v roce 2050, proto 0 GWh.
- **Ze zdrojů:** Dopadová studie, Tab. 37 s. 140 a s. 140 až 141
- **Odhad:** Žádné naše číslo. Rok konce je odhad studie, sama ho nazývá nepřesným.
- **Podrobné odvození:** Ze studie: 160,0 GWh v 2030, konec 2050, lineární průběh. Vlastní krok a jiné zdroje: základ = PSE 513,5280 − zemní plyn 159,4 − bioplyn 148,4 = 205,7280 GWh. 2030: 160,0 GWh z Tab.37. 2040: lineárně 160,0 na 0 v 2050 = 80,0. 2050: 0.
- **Zdroj:** ERÚ Roční zpráva 2025, tab. 4.5, s. 20, https://eru.gov.cz/sites/default/files/obsah/prilohy/eruelektro2025.pdf; Dopadová studie Tab.37 s.140, s.140-141, s.104
- **Strana:** Tab.37 s.140; s.140
- **Citace:** očekávaný: Tab.37 hrubá výroba 160,0 GWh (2030); „teoreticky odhadnuto na rok 2050“; „S vědomím určité nepřesnosti byl zvolen lineární průběh“ (s.141) (tabulka jako obrázek)
- **Poznámka:** Základ je reziduum PSE a je o 31,4 GWh vyšší než předpověď studie na 2025 (174,3 GWh). Studie konec 2050 sama nazývá nepřesným. Zlepší: výroba Green Gas DPB. Kvůli zaplavování dolů. Hutní plyny a důlní plyn jsou dvě rezidua, která se vyměňují: přebytek 31,4 GWh důlního plynu nad předpovědí 174,3 GWh může být zemní plyn spálený v PE.
- **Koeficient, progresivní:** zima P10 0.6746, P50 0.8434, P90 0.9709; léto P10 0.8000, P50 1.0000, P90 1.0200; flexibilní ne; stupeň C
- **Koeficient, konzervativní:** zima P10 0.6746, P50 0.8434, P90 0.9709; léto P10 0.8000, P50 1.0000, P90 1.0200; flexibilní ne; stupeň C
- **Koeficient, odvození:** Zima: dosažitelnost 0,825 z kalibrace na DV 2023. a_kal = (1024,6 + 167,6 − 567,0 − 18,5 × 0,428) / (648,4 + 99,7) = 0,825. koef = dosažitelnost × 8 760 / 8571 h: 0,825 × 8 760 / 8571 = 0,843. Léto: plochý provoz z Tab.18.
- **Koeficient, zdroj:** Dopadová studie Tab.18 s.100
- **Koeficient, strana:** rov.4 s.73; Tab.28 s.129; s.150
- **Koeficient, citace:** Tab.18 KJ na degazační plyn 8 571 h
- **Koeficient, poznámka:** Plochý provoz, 8 571 h.

#### ostatní paliva a odpadní teplo (přidaná položka)

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 24.6 | 0 | 15 | 30 | 20 | 20 | D |
| konzervativní | 24.6 | 0 | 15 | 30 | 20 | 20 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 10, P90 30; 2040 P10 5, P90 30
- **Meze 2030 a 2040, konzervativní:** 2030 P10 10, P90 30; 2040 P10 5, P90 30
- **Průběh:** plynule
- **Společný faktor:** zadny
- **Jak se došlo:** Bez výpočtu: z 24,6 GWh dnes na 15 GWh je náš odhad.
- **Ze zdrojů:** ERÚ Roční zpráva 2025, tab. 4.5 (jen dnešních 24,6 GWh)
- **Odhad:** Celá hodnota 2050 je úsudek bez zdroje.
- **Podrobné odvození:** Ze studie: nic. Vlastní krok a jiné zdroje: základ = ostatní pevná 1,9 + odpadní teplo 21,3 + topné oleje 0,8 + ostatní kapalná 0,6 = 24,6 GWh, vše změřeno. Dále úroveň 20 GWh.
- **Zdroj:** ERÚ Roční zpráva 2025, tab. 4.5, s. 20, https://eru.gov.cz/sites/default/files/obsah/prilohy/eruelektro2025.pdf
- **Poznámka:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Dopadovou studii nelze použít: Studie tato paliva zvlášť neuvádí. Položka přidána, protože ERÚ tato paliva v MSK vykazuje a jinak by nebyla kam zařadit. Výhled je úsudek. Odpadní teplo závisí na hutích.
- **Koeficient, progresivní:** zima P10 2.1250, P50 2.6568, P90 3.0587; léto P10 0.5000, P50 0.7901, P90 1.1000; flexibilní ne; stupeň C
- **Koeficient, konzervativní:** zima P10 2.1250, P50 2.6568, P90 3.0587; léto P10 0.5000, P50 0.7901, P90 1.1000; flexibilní ne; stupeň C
- **Koeficient, odvození:** Zima: dosažitelnost 0,825 z kalibrace na DV 2023. a_kal = (1024,6 + 167,6 − 567,0 − 18,5 × 0,428) / (648,4 + 99,7) = 0,825. koef = dosažitelnost × 8 760 / 2721 h: 0,825 × 8 760 / 2721 = 2,657. Léto: PE MSK červen až srpen 2025 139,2 MW / (1904,3 − 360,8 GWh) × 1000 / 8 760 = 0,790.
- **Koeficient, zdroj:** Dopadová studie s.73, s.129, s.150; ERÚ, čtvrtletní zprávy 2025 tab. 7.8
- **Koeficient, strana:** rov.4 s.73; Tab.28 s.129; s.150
- **Koeficient, citace:** „Za stabilní zdroje se nepovažují intermitentní zdroje (FVE a VTE)“
- **Koeficient, poznámka:** Hodiny 2721 h: 1113,3 GWh / (473,2 − 64,0 MW), ERÚ prosinec 2025 bez Dětmarovic a biomasy. Stejný poměr v roce 2023 neplatí.

#### fotovoltaika střešní

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 198.531 | 851.6 | 1058.4 | 1824.8 | 511.9 | 795.1 | D |
| konzervativní | 198.531 | 225.7 | 285.8 | 414.5 | 276.1 | 274.5 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 304.1, P90 760.3; 2040 P10 593.0, P90 1317.9
- **Meze 2030 a 2040, konzervativní:** 2030 P10 257.8, P90 315.4; 2040 P10 234.0, P90 361.2
- **Průběh:** plynule
- **Společný faktor:** povolovani
- **Historické maximum tempa, GWh za rok:** 69.6816
- **Jak se došlo, progresivní:** 26,1 GWe v Česku × podíl kraje 292,0 / 4 541,8 MW × 0,12 × 8 760 h využití × 60 % na střechách = 1 058,4 GWh.
- **Jak se došlo, konzervativní:** Stav 2026 je 317,0 MW × 1 051 h = 333,2 GWh; přidá se 10 % nárůstu k progresivní cestě, 333,2 + 10 % × (1 763,9 progresivní celkem − 333,2), a × 60 % na střechách = 285,8 GWh.
- **Ze zdrojů, progresivní:** Vnitrostátní plán, Tab. 98 s. 340 (26,1 GWe); Dopadová studie, s. 31 (0,12); ERÚ čtvrtletní zprávy 2025, tab. 6.1 (výkon kraje)
- **Ze zdrojů, konzervativní:** ERÚ čtvrtletní zpráva 2026 Q2, tab. 7.8 (317,0 MW); Vnitrostátní plán, Tab. 98 s. 340 (26,1 GWe); Dopadová studie, s. 31 (0,12); ERÚ čtvrtletní zprávy 2025, tab. 6.1 (výkon kraje)
- **Odhad, progresivní:** 60 % na střechách je úsudek. Držení dnešního podílu kraje do 2050 je úsudek.
- **Odhad, konzervativní:** 10 % je dáno definicí cesty, čtené jako nárůst nad dnešní stav, ne jako 10 % celku. 60 % na střechách je úsudek.
- **Podrobné odvození, progresivní:** Ze studie: využití 0,12 a mez 165 GWp. Vlastní krok a jiné zdroje: základ: pozemní = 250,8483 × 60,9 / 292,0 MW = 52,3173; střešní zbytek 198,5310 GWh. hodiny 0,12 × 8 760 = 1 051,2 h (změřeno 2025: 250,8483 GWh / 271,0 MW = 1 h, tedy méně). Podíl MSK = 292,0 / 4 541,8 MW = 6,43 %. 2030 P50: 10,1 GWe × 6,43 % × 1 051 h = 682,6; 2050 P50: 26,1 GWe × podíl × h = 1 763,9; P10 z WEM 6 a 21 GWe; P90 úsudek 15 a 45 GWe; 2040 lineárně. Podíl střešní: 75 % / 65 % / 60 %.
- **Podrobné odvození, konzervativní:** Ze studie: využití 0,12 a mez 165 GWp. Vlastní krok a jiné zdroje: základ: pozemní = 250,8483 × 60,9 / 292,0 MW = 52,3173; střešní zbytek 198,5310 GWh. stav 317,0 MW (červen 2026) × 1 051 h = 333,2; konzervativní = 333,2 + 10 % × (progresivní P50 − 333,2), P10 3 %, P90 25 %, poté podíl střešní.
- **Zdroj, progresivní:** ERÚ, čtvrtletní zprávy 2025 Q1 až Q4, tab. 6.1, řádek MSK (FVE); ERÚ 2025 tab. 7.8 a kap. 2; Vnitrostátní plán Tab.98 s.340 (WAM, WEM); Dopadová studie s.46, s.61, s.135-136 (165 GWp)
- **Zdroj, konzervativní:** ERÚ, čtvrtletní zprávy 2025 Q1 až Q4, tab. 6.1, řádek MSK (FVE); ERÚ 2025 tab. 7.8 a kap. 2; Vnitrostátní plán Tab.98 s.340 (WAM, WEM); Dopadová studie s.46, s.61, s.135-136 (165 GWp); ERÚ, čtvrtletní zpráva 2026 Q2 tab. 7.8; definice cest (část 2)
- **Strana:** s.31; s.136; s.61; Obr.33 s.125
- **Citace:** „cca 0,12 (tedy 12 %)“ (ČR, statistika); očekávaný: „až 165 GW p“; Obr.33 popisek 1,4 % (odečteno z grafu)
- **Poznámka, progresivní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Dopadovou studii nelze použít: Podíl 1,4 % ze 7,2 TWh (100,8 GWh) je pod dnešní výrobou, a progresivní cesta chce maximum OZE, proto Vnitrostátní plán. Dělení střecha a pozem je úsudek: ERÚ ho neuvádí, stav 60,9 MW z 2016 je brán jako pozemní. Zlepší: registr výroben ČEZ Distribuce podle typu. Mez: 165 GWp je daleko nad hodnotami, skutečnou mezí je síť (s.135-136). Tempo: Dopadová studie Tab.2 s.33, FVE MSK 2022 64 622,6, 2023 134 304,2 MWh; rozdíl 69 681,6 MWh = 69,6816 GWh/rok, nejvyšší v tisku (ERÚ tab. 6.1: 2024 196 517,3, 2025 250 848,3 MWh, rozdíl 54,3310 GWh). Celé přiřazeno střešní položce, dělení v historii neexistuje.
- **Poznámka, konzervativní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Dopadovou studii nelze použít: Podíl 1,4 % ze 7,2 TWh (100,8 GWh) je pod dnešní výrobou, a progresivní cesta chce maximum OZE, proto Vnitrostátní plán. Procento nejde použít čistě: doslovných 10 % progresivní P50 2050 (176,4 GWh) by bylo pod dnešním stavem a znamenalo by bourání. Proto 10 % nárůstu nad stav 2026. Tempo: Dopadová studie Tab.2 s.33, FVE MSK 2022 64 622,6, 2023 134 304,2 MWh; rozdíl 69 681,6 MWh = 69,6816 GWh/rok, nejvyšší v tisku (ERÚ tab. 6.1: 2024 196 517,3, 2025 250 848,3 MWh, rozdíl 54,3310 GWh). Celé přiřazeno střešní položce, dělení v historii neexistuje.
- **Koeficient, progresivní:** zima P10 0.0000, P50 0.0000, P90 0.1667; léto P10 4.3766, P50 5.1614, P90 5.3292; flexibilní ne; stupeň C
- **Koeficient, konzervativní:** zima P10 0.0000, P50 0.0000, P90 0.1667; léto P10 4.3766, P50 5.1614, P90 5.3292; flexibilní ne; stupeň C
- **Koeficient, odvození:** Zima: 0 podle studie, večer není slunce. P90 využití 0,02 / 0,12. Léto: FVE ČR při letních maximech (7 měsíců 2024 až 2026) / instalovaný výkon ČR: P10 0,525, P50 0,619, P90 0,640; koef = využití / 0,12.
- **Koeficient, zdroj:** Dopadová studie s.73; ERÚ, čtvrtletní zprávy 2024 až 2026 tab. 9.3 a kap. 2
- **Koeficient, strana:** s.73
- **Koeficient, citace:** „Za stabilní zdroje se nepovažují intermitentní zdroje (FVE a VTE)“
- **Koeficient, poznámka:** Měření je za ČR, ne za kraj. Letní maxima nejsou vždy jasná obloha. Řádek počítá 1 051 h, v 2025 bylo změřeno 926 h, takže 2025 vychází o 12 % níž.

#### fotovoltaika pozemní

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 52.3173 | 567.7 | 705.6 | 1216.5 | 170.6 | 428.1 | D |
| konzervativní | 52.3173 | 150.5 | 190.5 | 276.4 | 92.0 | 147.8 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 101.4, P90 253.4; 2040 P10 319.3, P90 709.6
- **Meze 2030 a 2040, konzervativní:** 2030 P10 85.9, P90 105.1; 2040 P10 126.0, P90 194.5
- **Průběh:** plynule
- **Společný faktor:** povolovani
- **Historické maximum tempa, GWh za rok:** 13.125
- **Jak se došlo, progresivní:** 26,1 GWe v Česku × podíl kraje 292,0 / 4 541,8 MW × 0,12 × 8 760 h využití × 40 % na zemi = 705,6 GWh.
- **Jak se došlo, konzervativní:** Stav 2026 je 317,0 MW × 1 051 h = 333,2 GWh; přidá se 10 % nárůstu k progresivní cestě, 333,2 + 10 % × (1 763,9 progresivní celkem − 333,2), a × 40 % na zemi = 190,5 GWh.
- **Ze zdrojů, progresivní:** Vnitrostátní plán, Tab. 98 s. 340 (26,1 GWe); Dopadová studie, s. 31 (0,12); ERÚ čtvrtletní zprávy 2025, tab. 6.1 (výkon kraje)
- **Ze zdrojů, konzervativní:** ERÚ čtvrtletní zpráva 2026 Q2, tab. 7.8 (317,0 MW); Vnitrostátní plán, Tab. 98 s. 340 (26,1 GWe); Dopadová studie, s. 31 (0,12); ERÚ čtvrtletní zprávy 2025, tab. 6.1 (výkon kraje)
- **Odhad, progresivní:** 40 % na zemi je úsudek. Držení dnešního podílu kraje do 2050 je úsudek.
- **Odhad, konzervativní:** 10 % je dáno definicí cesty, čtené jako nárůst nad dnešní stav, ne jako 10 % celku. 40 % na zemi je úsudek.
- **Podrobné odvození, progresivní:** Ze studie: využití 0,12 a mez 165 GWp. Vlastní krok a jiné zdroje: základ: pozemní = 250,8483 × 60,9 / 292,0 MW = 52,3173; střešní zbytek 198,5310 GWh. hodiny 0,12 × 8 760 = 1 051,2 h (změřeno 2025: 250,8483 GWh / 271,0 MW = 1 h, tedy méně). Podíl MSK = 292,0 / 4 541,8 MW = 6,43 %. 2030 P50: 10,1 GWe × 6,43 % × 1 051 h = 682,6; 2050 P50: 26,1 GWe × podíl × h = 1 763,9; P10 z WEM 6 a 21 GWe; P90 úsudek 15 a 45 GWe; 2040 lineárně. Podíl pozemní: 25 % / 35 % / 40 %.
- **Podrobné odvození, konzervativní:** Ze studie: využití 0,12 a mez 165 GWp. Vlastní krok a jiné zdroje: základ: pozemní = 250,8483 × 60,9 / 292,0 MW = 52,3173; střešní zbytek 198,5310 GWh. stav 317,0 MW (červen 2026) × 1 051 h = 333,2; konzervativní = 333,2 + 10 % × (progresivní P50 − 333,2), P10 3 %, P90 25 %, poté podíl pozemní.
- **Zdroj, progresivní:** ERÚ, čtvrtletní zprávy 2025 Q1 až Q4, tab. 6.1, řádek MSK (FVE); ERÚ 2025 tab. 7.8 a kap. 2; Vnitrostátní plán Tab.98 s.340 (WAM, WEM); Dopadová studie s.46, s.61, s.135-136 (165 GWp)
- **Zdroj, konzervativní:** ERÚ, čtvrtletní zprávy 2025 Q1 až Q4, tab. 6.1, řádek MSK (FVE); ERÚ 2025 tab. 7.8 a kap. 2; Vnitrostátní plán Tab.98 s.340 (WAM, WEM); Dopadová studie s.46, s.61, s.135-136 (165 GWp); ERÚ, čtvrtletní zpráva 2026 Q2 tab. 7.8; definice cest (část 2)
- **Strana:** s.31; s.135-136; Obr.33 s.125
- **Citace:** „cca 0,12 (tedy 12 %)“ (ČR, statistika); očekávaný: „až 165 GW p“; Obr.33 popisek 1,4 % (odečteno z grafu)
- **Poznámka, progresivní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Dopadovou studii nelze použít: Podíl 1,4 % ze 7,2 TWh (100,8 GWh) je pod dnešní výrobou, a progresivní cesta chce maximum OZE, proto Vnitrostátní plán. Dělení střecha a pozem je úsudek: ERÚ ho neuvádí, stav 60,9 MW z 2016 je brán jako pozemní. Zlepší: registr výroben ČEZ Distribuce podle typu. Mez: 165 GWp je daleko nad hodnotami, skutečnou mezí je síť (s.135-136). Tempo: Dopadová studie Tab.2 s.33, FVE MSK 2008 200,0, 2012 52 700,0 MWh; (52 700,0 − 200,0) / 4 = 13 125 MWh = 13,125 GWh/rok. Je to průměr čtyř let, roční maximum v tisku není a mohlo být vyšší. Přiřazení pozemní položce plyne z úsudku o 60,9 MW.
- **Poznámka, konzervativní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Dopadovou studii nelze použít: Podíl 1,4 % ze 7,2 TWh (100,8 GWh) je pod dnešní výrobou, a progresivní cesta chce maximum OZE, proto Vnitrostátní plán. Procento nejde použít čistě: doslovných 10 % progresivní P50 2050 (176,4 GWh) by bylo pod dnešním stavem a znamenalo by bourání. Proto 10 % nárůstu nad stav 2026. Tempo: Dopadová studie Tab.2 s.33, FVE MSK 2008 200,0, 2012 52 700,0 MWh; (52 700,0 − 200,0) / 4 = 13 125 MWh = 13,125 GWh/rok. Je to průměr čtyř let, roční maximum v tisku není a mohlo být vyšší. Přiřazení pozemní položce plyne z úsudku o 60,9 MW.
- **Koeficient, progresivní:** zima P10 0.0000, P50 0.0000, P90 0.1667; léto P10 4.3766, P50 5.1614, P90 5.3292; flexibilní ne; stupeň C
- **Koeficient, konzervativní:** zima P10 0.0000, P50 0.0000, P90 0.1667; léto P10 4.3766, P50 5.1614, P90 5.3292; flexibilní ne; stupeň C
- **Koeficient, odvození:** Zima: 0 podle studie, večer není slunce. P90 využití 0,02 / 0,12. Léto: FVE ČR při letních maximech (7 měsíců 2024 až 2026) / instalovaný výkon ČR: P10 0,525, P50 0,619, P90 0,640; koef = využití / 0,12.
- **Koeficient, zdroj:** Dopadová studie s.73; ERÚ, čtvrtletní zprávy 2024 až 2026 tab. 9.3 a kap. 2
- **Koeficient, strana:** s.73
- **Koeficient, citace:** „Za stabilní zdroje se nepovažují intermitentní zdroje (FVE a VTE)“
- **Koeficient, poznámka:** Měření je za ČR, ne za kraj. Letní maxima nejsou vždy jasná obloha. Řádek počítá 1 051 h, v 2025 bylo změřeno 926 h, takže 2025 vychází o 12 % níž.

#### vítr

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 91.8586 | 799.0 | 1710.5 | 3293.6 | 262.7 | 1088.5 | C |
| konzervativní | 91.8586 | 140.4 | 253.7 | 496.5 | 108.9 | 191.5 | C |

- **Meze 2030 a 2040, progresivní:** 2030 P10 84.2, P90 720.8; 2040 P10 479.4, P90 2177.0
- **Meze 2030 a 2040, konzervativní:** 2030 P10 97.0, P90 134.6; 2040 P10 121.8, P90 341.0
- **Průběh:** plynule
- **Společný faktor:** povolovani
- **Historické maximum tempa, GWh za rok:** 23.8517
- **Jak se došlo, progresivní:** 5,5 GWe v Česku × podíl kraje 41,8 / 368,9 MW × 2 744,7 h za rok = 1 710,5 GWh.
- **Jak se došlo, konzervativní:** 91,8586 GWh dnes + 10 % nárůstu k progresivní cestě × (1 710,5 − 91,8586) = 253,7 GWh.
- **Ze zdrojů, progresivní:** Vnitrostátní plán, Tab. 98 s. 340 (5,5 GWe); Dopadová studie, Tab. 9 s. 47 (2 744,7 h); ERÚ čtvrtletní zprávy 2025, tab. 6.1 (výkon kraje)
- **Ze zdrojů, konzervativní:** ERÚ čtvrtletní zprávy 2025, tab. 6.1 (dnešní výroba); Vnitrostátní plán, Tab. 98 s. 340; Dopadová studie, Tab. 9 s. 47
- **Odhad, progresivní:** Držení dnešního podílu kraje do 2050 je úsudek.
- **Odhad, konzervativní:** 10 % je dáno definicí cesty, čtené jako nárůst nad dnešek. Držení podílu kraje v progresivní hodnotě je úsudek.
- **Podrobné odvození, progresivní:** Ze studie: 2 744,7 h, 23 %, mez 2 014 MW. Vlastní krok a jiné zdroje: základ 91,8586 GWh. Hodiny P10 23 % × 8 760 = 2 014,8 h (změřeno 2025: 2 h); P50 a P90 2 744,7 h. Podíl MSK = 41,8 / 368,9 MW = 11,33 %. 2030: P10 41,8 MW; P50 41,8 + 53,9 = 95,7 MW; P90 + 166,9 MW = 262,6 MW. 2050 P50: 5,5 GWe × 11,33 % × 2 744,7 h = 1 710,5; P10: 3,5 GWe × podíl × 2 015 h; P90: 1 200 MW × 2 744,7 h. 2040 lineárně v GWe.
- **Podrobné odvození, konzervativní:** Ze studie: 2 744,7 h, 23 %, mez 2 014 MW. Vlastní krok a jiné zdroje: konzervativní = 91,8586 + 10 % × (progresivní P50 − 91,8586), P10 3 %, P90 25 %.
- **Zdroj, progresivní:** ERÚ, čtvrtletní zprávy 2025 Q1 až Q4, tab. 6.1, řádek MSK (VTE); Vnitrostátní plán Tab.98 s.340; Dopadová studie Tab.9 (2 744,7 h v 2023), s.135 (2 014 MW); https://ekonomickydenik.cz/investor-chce-u-bridlicne-postavit-az-27-vetrnych-elektraren-cast-mistnich-ziska-elektrinu-zdarma/
- **Zdroj, konzervativní:** ERÚ, čtvrtletní zprávy 2025 Q1 až Q4, tab. 6.1, řádek MSK (VTE); Vnitrostátní plán Tab.98 s.340; Dopadová studie Tab.9 (2 744,7 h v 2023), s.135 (2 014 MW); https://ekonomickydenik.cz/investor-chce-u-bridlicne-postavit-az-27-vetrnych-elektraren-cast-mistnich-ziska-elektrinu-zdarma/; definice cest (část 2)
- **Strana:** Tab.9 s.47; s.33; s.135; Obr.33 s.125
- **Citace:** Tab.9 2 744,7 h (2023); „Průměrný koeficient ročního využití VTE v ČR je 23 %“; očekávaný: „až 2 014 MW“; Obr.33 popisek 2,1 % (odečteno z grafu)
- **Poznámka, progresivní:** Dopadovou studii nelze použít: Podíl 2,1 % ze 7,2 TWh (151,2 GWh) neodpovídá maximu OZE v progresivní cestě, MW pro 2030 a 2050 studie neuvádí, proto Vnitrostátní plán a projekty. Mez: studie uvádí potenciál 2 014 MW (s.135), P90 1 200 MW je pod ním. Projekty u Břidličné a Horních Životic jsou ve fázi povolování, datum zpráv neověřeno. Regionální podíl z 2025 nemusí vydržet. Tempo: Dopadová studie Tab.2 s.33, VTE MSK 2018 54 839,1, 2019 78 690,8 MWh; rozdíl 23 851,7 MWh = 23,8517 GWh/rok, nejvyšší v tisku. Obsahuje i vliv větrnosti, výkon rostl jen na 28,4 MW (s.46).
- **Poznámka, konzervativní:** Dopadovou studii nelze použít: Podíl 2,1 % ze 7,2 TWh (151,2 GWh) neodpovídá maximu OZE v progresivní cestě, MW pro 2030 a 2050 studie neuvádí, proto Vnitrostátní plán a projekty. Stejný důvod jako u fotovoltaiky: doslovných 10 % P50 2050 je 171,1 GWh, jen málo nad dneškem. Čteno jako 10 % nárůstu. Tempo: Dopadová studie Tab.2 s.33, VTE MSK 2018 54 839,1, 2019 78 690,8 MWh; rozdíl 23 851,7 MWh = 23,8517 GWh/rok, nejvyšší v tisku. Obsahuje i vliv větrnosti, výkon rostl jen na 28,4 MW (s.46).
- **Koeficient, progresivní:** zima P10 0.0000, P50 0.0000, P90 1.0093; léto P10 0.2111, P50 0.5802, P90 0.8143; flexibilní ne; stupeň C
- **Koeficient, konzervativní:** zima P10 0.0000, P50 0.0000, P90 1.0093; léto P10 0.2111, P50 0.5802, P90 0.8143; flexibilní ne; stupeň C
- **Koeficient, odvození:** Zima: P10 a P50 = 0 podle pravidla studie. Změřený vítr při zimních maximech ČR (14 měsíců) je P10 0,034, P50 0,192, P90 0,316; do P90 jde 0,316 × 8 760 / 2 744,7 h. Léto: změřeno P10 0,066, P50 0,182, P90 0,255, stejný vzorec.
- **Koeficient, zdroj:** Dopadová studie s.73, Tab.9 s.47; ERÚ, čtvrtletní zprávy 2023 až 2026 tab. 9.3
- **Koeficient, strana:** s.73; Tab.9 s.47
- **Koeficient, citace:** „Za stabilní zdroje se nepovažují intermitentní zdroje (FVE a VTE)“
- **Koeficient, poznámka:** P50 v zimě je pravidlo studie, ne medián. Kontrolní tabulka má sloupec s měřeným mediánem.

#### malé vodní elektrárny

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 44.5996 | 43.7 | 55.5 | 66.5 | 55.5 | 55.5 | C |
| konzervativní | 44.5996 | 43.7 | 55.5 | 66.5 | 55.5 | 55.5 | C |

- **Meze 2030 a 2040, progresivní:** 2030 P10 43.7, P90 66.5; 2040 P10 43.7, P90 66.5
- **Meze 2030 a 2040, konzervativní:** 2030 P10 43.7, P90 66.5; 2040 P10 43.7, P90 66.5
- **Průběh:** plynule
- **Společný faktor:** zadny
- **Jak se došlo:** 18,5 MW × 3 000 h za rok = 55,5 GWh.
- **Ze zdrojů:** Dopadová studie, Tab. 18 s. 100 (18,5 MW), s. 134 (3 000 h)
- **Odhad:** žádný
- **Podrobné odvození:** Ze studie: 18,5 MW a hodiny. Vlastní krok a jiné zdroje: základ 44,5996 GWh. 18,5 MW × 3 000 h = 55,5; P10 18,5 MW × 2 360 h = 43,7; P90 18,5 MW × 3 597 h = 66,5.
- **Zdroj:** ERÚ, čtvrtletní zprávy 2025 Q1 až Q4, tab. 6.1, řádek MSK (VE); Dopadová studie Tab.18 s.100, s.134
- **Strana:** Tab.18 s.100; s.134
- **Citace:** očekávaný: 18,5 MW; „kolem 3 000 hodin ročně“; Tab.18 hodiny 2 360 až 3 597
- **Poznámka:** Mez: spád je podle s.134 téměř vyčerpán, nový výkon nepřibývá. Základ 2025 je suchý rok, proto P50 nad ním. Rozdíl mezi cestami není.
- **Koeficient, progresivní:** zima P10 0.8264, P50 1.2498, P90 2.0498; léto P10 0.4438, P50 0.5285, P90 0.8702; flexibilní ne; stupeň C
- **Koeficient, konzervativní:** zima P10 0.8264, P50 1.2498, P90 2.0498; léto P10 0.4438, P50 0.5285, P90 0.8702; flexibilní ne; stupeň C
- **Koeficient, odvození:** změřené měsíční využití VE v MSK. Zima: prosinec 2025 0,283, leden 2025 0,428, leden 2024 0,702. Léto: srpen 2024 0,152, srpen 2025 0,181, červenec 2024 0,298. koef = využití × 8 760 / 3 000 h.
- **Koeficient, zdroj:** ERÚ, čtvrtletní zprávy 2024 a 2025 tab. 7.8; Dopadová studie s.134
- **Koeficient, strana:** s.134
- **Koeficient, citace:** „kolem 3 000 hodin ročně“
- **Koeficient, poznámka:** Měsíční průměr, ne okamžik. Průtočné, řízení minimální.

#### biomasa

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 430.2 | 370 | 432 | 568.5 | 432 | 432 | C |
| konzervativní | 430.2 | 370 | 432 | 568.5 | 432 | 432 | C |

- **Meze 2030 a 2040, progresivní:** 2030 P10 370, P90 568.5; 2040 P10 370, P90 568.5
- **Meze 2030 a 2040, konzervativní:** 2030 P10 370, P90 568.5; 2040 P10 370, P90 568.5
- **Průběh:** plynule
- **Společný faktor:** cena
- **Jak se došlo:** 6,0 % podíl biomasy × 7,2 TWh celkové výroby ve studii = 432 GWh.
- **Ze zdrojů:** Dopadová studie, Obr. 33 s. 125 (6,0 %, odečteno z grafu), s. 124 (7,2 TWh)
- **Odhad:** žádný
- **Podrobné odvození:** Ze studie: 6,0 % × 7,2 TWh, 113,7 MW. Vlastní krok a jiné zdroje: základ = biomasa MSK 2025 430,2 GWh. Výhled: 6,0 % × 7,2 TWh = 432,0; P10 74 MW × 5 000 h = 370,0; P90 113,7 MW × 5 000 h = 568,5.
- **Zdroj:** ERÚ Roční zpráva 2025, tab. 4.5, s. 20, https://eru.gov.cz/sites/default/files/obsah/prilohy/eruelektro2025.pdf; Dopadová studie Obr.33 s.125, s.130, s.139, s.169
- **Strana:** Obr.33 s.125; s.124; s.130; s.169
- **Citace:** očekávaný: Obr.33 popisek 6,0 % (odečteno z grafu); „cca 7,2 TWh“; „113,7 MW“; extrémní: „prakticky vyčerpán“
- **Poznámka:** Mez: s.169 uvádí, že potenciál udržitelné biomasy pro elektřinu v MSK je prakticky vyčerpán. 5 000 h je úsudek. Převážně Lenzing Biocel Paskov, tedy mimo vazbu na městské teplo. Definice cest: srovnatelné.
- **Koeficient, progresivní:** zima P10 0.8601, P50 1.0754, P90 1.2380; léto P10 0.8000, P50 1.0000, P90 1.1500; flexibilní ne; stupeň C
- **Koeficient, konzervativní:** zima P10 0.8601, P50 1.0754, P90 1.2380; léto P10 0.8000, P50 1.0000, P90 1.1500; flexibilní ne; stupeň C
- **Koeficient, odvození:** Zima: dosažitelnost 0,825 z kalibrace na DV 2023. a_kal = (1024,6 + 167,6 − 567,0 − 18,5 × 0,428) / (648,4 + 99,7) = 0,825. koef = dosažitelnost × 8 760 / 6722 h: 0,825 × 8 760 / 6722 = 1,075. Léto: provoz vázaný na výrobu celulózy, úsudek.
- **Koeficient, zdroj:** Dopadová studie s.73, s.129, s.150; ERÚ, čtvrtletní zprávy 2025 tab. 7.8
- **Koeficient, strana:** rov.4 s.73; Tab.28 s.129; s.150
- **Koeficient, citace:** Tab.29 Lenzing Biocel Paskov 58,2; Bioblok TFM 5,8
- **Koeficient, poznámka:** Hodiny 6722 h: 430,2 GWh / 64,0 MW. Lenzing Biocel běží s výrobou, proto v létě koef kolem 1.

#### bioplyn

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 148.4 | 0 | 77.6 | 155.2 | 77.6 | 77.6 | D |
| konzervativní | 148.4 | 0 | 77.6 | 155.2 | 77.6 | 77.6 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 52.0, P90 148.4; 2040 P10 0, P90 155.2
- **Meze 2030 a 2040, konzervativní:** 2030 P10 52.0, P90 148.4; 2040 P10 0, P90 155.2
- **Průběh:** plynule
- **Společný faktor:** cena
- **Jak se došlo:** Úroveň roku 2030 držená do 2050: 11,5 MW × 6 748 h za rok = 77,6 GWh.
- **Ze zdrojů:** Dopadová studie, Tab. 38 s. 143 (11,5 MW), Tab. 18 (6 748 h)
- **Odhad:** Držení po 2030 je úsudek bez zdroje. Studie v očekávaném scénáři výrobu v 2033 končí.
- **Podrobné odvození:** Ze studie: 77 600 MWh, 23 MW, 6 748 h. Vlastní krok a jiné zdroje: základ = bioplyn MSK 2025 148,4 GWh. P50: 11,5 MW × 6 748 h = 77,6 GWh drženo po 2030. P10 2040 a 2050: 0. P90: 23 MW × 6 748 h = 155,2.
- **Zdroj:** ERÚ Roční zpráva 2025, tab. 4.5, s. 20, https://eru.gov.cz/sites/default/files/obsah/prilohy/eruelektro2025.pdf; Dopadová studie Tab.38 s.143, s.104, s.144; Vnitrostátní plán Tab.64 s.228
- **Strana:** Tab.38 s.143; s.104
- **Citace:** očekávaný: Tab.38 11,5 MW a 77600 MWh/rok (2030), 0 (2033); Tab.18 6 748 h; „cca 23 MW“ (s.104, při změně podpory) (tabulka jako obrázek)
- **Poznámka:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Závisí na podpoře. Studie v očekávaném scénáři končí 2033, ale definice cest bioplyn v obou cestách drží, proto držení úrovně 2030; to je úsudek bez zdroje bez zdroje. Definice cest: srovnatelné.
- **Koeficient, progresivní:** zima P10 0.8568, P50 1.0712, P90 1.2333; léto P10 0.8000, P50 1.0000, P90 1.2000; flexibilní ne; stupeň C
- **Koeficient, konzervativní:** zima P10 0.8568, P50 1.0712, P90 1.2333; léto P10 0.8000, P50 1.0000, P90 1.2000; flexibilní ne; stupeň C
- **Koeficient, odvození:** Zima: dosažitelnost 0,825 z kalibrace na DV 2023. a_kal = (1024,6 + 167,6 − 567,0 − 18,5 × 0,428) / (648,4 + 99,7) = 0,825. koef = dosažitelnost × 8 760 / 6748 h: 0,825 × 8 760 / 6748 = 1,071. Léto: plochý provoz z Tab.18.
- **Koeficient, zdroj:** Dopadová studie Tab.18 s.100
- **Koeficient, strana:** rov.4 s.73; Tab.28 s.129; s.150
- **Koeficient, citace:** Tab.18 KJ na bioplyn 6 748 h
- **Koeficient, poznámka:** Plochý provoz, 6 748 h.

#### geotermální energie

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 0 | 0 | 0 | 0 | 0 | 0 | B |
| konzervativní | 0 | 0 | 0 | 0 | 0 | 0 | B |

- **Meze 2030 a 2040, progresivní:** 2030 P10 0, P90 0; 2040 P10 0, P90 0
- **Meze 2030 a 2040, konzervativní:** 2030 P10 0, P90 0; 2040 P10 0, P90 0
- **Průběh:** plynule
- **Společný faktor:** zadny
- **Jak se došlo:** Studie s významnějším příspěvkem geotermálních elektráren do 2050 nepočítá, proto 0 GWh.
- **Ze zdrojů:** Dopadová studie, s. 89
- **Odhad:** žádný
- **Podrobné odvození:** Ze studie: nula. Vlastní krok a jiné zdroje: 0 MW × 0 h = 0.
- **Zdroj:** Dopadová studie s.89
- **Strana:** s.89
- **Citace:** „nelze uvažovat s významnějším příspěvkem geotermálních elektráren“
- **Poznámka:** Nula s důvodem: s.89 „nelze uvažovat s významnějším příspěvkem geotermálních elektráren k vyrovnání bilance elektřiny v MSK do roku 2050“.
- **Koeficient, progresivní:** zima P10 0.0000, P50 0.0000, P90 0.0000; léto P10 0.0000, P50 0.0000, P90 0.0000; flexibilní ne; stupeň B
- **Koeficient, konzervativní:** zima P10 0.0000, P50 0.0000, P90 0.0000; léto P10 0.0000, P50 0.0000, P90 0.0000; flexibilní ne; stupeň B
- **Koeficient, odvození:** nulová roční energie, koeficient nemá na co působit
- **Koeficient, zdroj:** Dopadová studie s.89, s.148, s.170
- **Koeficient, strana:** s.89; s.148; s.170
- **Koeficient, citace:** viz tabulka položek (část 5)
- **Koeficient, poznámka:** Položka v bilanci nulová.

#### SMR

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 0 | 3504 | 3942 | 4029.5 | 3942 | 3942 | C |
| konzervativní | 0 | 0 | 0 | 0 | 0 | 0 | B |

- **Meze 2030 a 2040, progresivní:** 2030 P10 3504, P90 4029.5; 2040 P10 3504, P90 4029.5
- **Meze 2030 a 2040, konzervativní:** 2030 P10 0, P90 0; 2040 P10 0, P90 0
- **Průběh, progresivní:** skok
- **Průběh, konzervativní:** plynule
- **Společný faktor, progresivní:** povolovani
- **Společný faktor, konzervativní:** zadny
- **Událost, progresivní:** Spuštění SMR, rok P10 2040, P50 2045, P90 2055
- **Jak se došlo, progresivní:** 500 MW × 90 % využití × 8 760 h za rok = 3 942 GWh.
- **Jak se došlo, konzervativní:** V konzervativní cestě SMR není, je to volba cesty, proto 0 GWh.
- **Ze zdrojů, progresivní:** Dopadová studie, s. 32 (90 %), s. 126 (rok 2045)
- **Ze zdrojů, konzervativní:** žádný (volba modelu č. 6)
- **Odhad, progresivní:** 500 MW je rozhodnutí cesty (volba modelu č. 6), žádný zdroj ho neuvádí. Studie má 350 MWe.
- **Odhad, konzervativní:** Žádné číslo, jen rozhodnutí cesty.
- **Podrobné odvození, progresivní:** Ze studie: 90 % a rok 2045; ne 350 MWe, výkon 500 MW je volba modelu č. 6. Vlastní krok a jiné zdroje: 500 MW × 7 884 h = 3 942,0; P10 500 MW × 7 008 h (80 %) = 3 504,0; P90 500 MW × 8 059 h (92 %) = 4 029,5.
- **Podrobné odvození, konzervativní:** Ze studie: nic, volba cesty. Vlastní krok a jiné zdroje: 0 MW × 0 h = 0.
- **Zdroj, progresivní:** volba modelu č. 6; Dopadová studie s.32 (89 %, trend 90 %), s.126 (2045), s.167; https://oenergetice.cz/jaderne-elektrarny/prvni-maly-modularni-reaktor-muze-stat-v-moravskoslezskem-kraji-uz-v-roce-2035 (14.5.2026)
- **Zdroj, konzervativní:** volba modelu č. 6; definice cest (část 2)
- **Strana, progresivní:** s.32; s.126
- **Citace, progresivní:** „cca na úrovni 89 %, s trendem zlepšení až k 90 %“; očekávaný: „350 MWe s uvedením do provozu v roce 2045“
- **Poznámka, progresivní:** Rok P90 je po horizontu, takže v části běhů SMR do 2050 nevznikne. Ministr uvádí možný začátek stavby 2035, ne provozu. Dětmarovice jsou zmiňovaná varianta, lokalita není vybraná. Jeden blok Rolls-Royce má podle studie 470 MWe, 500 MW je rozhodnutí cesty.
- **Poznámka, konzervativní:** Binární volba: v konzervativní cestě SMR není.
- **Koeficient, progresivní:** zima P10 0.9444, P50 1.0556, P90 1.1111; léto P10 0.0000, P50 1.0000, P90 1.1111; flexibilní ne; stupeň C
- **Koeficient, konzervativní:** zima P10 0.9444, P50 1.0556, P90 1.1111; léto P10 0.0000, P50 1.0000, P90 1.1111; flexibilní ne; stupeň C
- **Koeficient, odvození:** koef = dosažitelnost × 8 760 / 7 884 h. Zima 0,85; 0,95; 1,0. Léto P10 0 je odstávka paliva, P50 0,9 z řádku.
- **Koeficient, zdroj:** Dopadová studie s.32; volba modelu č. 6
- **Koeficient, strana:** s.32
- **Koeficient, citace:** „cca na úrovni 89 %, s trendem zlepšení až k 90 %“
- **Koeficient, poznámka:** Výpadek jediného bloku n−1 tu není, studie ho řeší zálohou.

#### nové plynové bloky

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 0 | 0 | 0 | 400 | 521.0 | 1067.2 | D |
| konzervativní | 0 | 849 | 2164.3 | 3415 | 896.8 | 1372.1 | C |

- **Meze 2030 a 2040, progresivní:** 2030 P10 279, P90 996.4; 2040 P10 500, P90 2404.8
- **Meze 2030 a 2040, konzervativní:** 2030 P10 279, P90 1195.7; 2040 P10 800, P90 2404.8
- **Průběh:** plynule
- **Společný faktor:** cena
- **Jak se došlo, progresivní:** V roce 2050 všech 433 MW spaluje syntetický plyn a biometan, na zemní plyn zbývá 0 GWh.
- **Jak se došlo, konzervativní:** 33,4 % podíl plynu × 7,2 TWh celkové výroby ve studii (odpovídá 683 MW × 3 521 h) × 90 % zemní plyn = 2 164,3 GWh.
- **Ze zdrojů, progresivní:** Dopadová studie, Tab. 30 s. 132 (433 MW)
- **Ze zdrojů, konzervativní:** Dopadová studie, Obr. 33 s. 125 (33,4 %, odečteno z grafu), s. 124 (7,2 TWh), Tab. 30 s. 132 (683 MW)
- **Odhad, progresivní:** Úplný přechod bloků na syntetický plyn je úsudek bez zdroje.
- **Odhad, konzervativní:** Převzetí objemu ze studie, která počítá jiný scénář, je úsudek. 90 % je rozhodnutí cesty (volba modelu č. 4), ne zdroj.
- **Podrobné odvození, progresivní:** Ze studie: MW, 33,4 %, 7,2 TWh, 5 602 h. Vlastní krok a jiné zdroje: Hodiny ze studie: 33,4 % × 7,2 TWh / 683 MW = 3 521 h. Třinec 93 MW × 5 602 h = 521,0. 283 MW × 3 521 h = 996,4. 2040: 433 MW × 3 521 h × 70 % zemní plyn = 1 067,2. 2050: 433 MW × 2 000 h = 866,0, celé na syntetický plyn a biometan, zemní plyn P50 0.
- **Podrobné odvození, konzervativní:** Ze studie: MW, 33,4 %, 7,2 TWh, 5 602 h. Vlastní krok a jiné zdroje: Hodiny ze studie: 33,4 % × 7,2 TWh / 683 MW = 3 521 h. Třinec 93 MW × 5 602 h = 521,0. 283 MW × 3 521 h = 996,4. Celkem 2050: 683 MW × 3 521 h = 2 404,8; × 90 % zemní plyn = 2 164,3 (volba modelu č. 4). P10 283 MW × 3 000 h; P90 683 MW × 5 000 h.
- **Zdroj, progresivní:** Dopadová studie Tab.30 s.132, Obr.33 s.125, Tab.18 s.100; https://gmk.center/en/news/trinecke-zelezarny-is-investing-over-180-million-in-a-combined-cycle-power-station/ (17.6.2026); https://ekonomickydenik.cz/uhli-zemni-plyn-teplarna-ostrava/
- **Zdroj, konzervativní:** Dopadová studie Tab.30 s.132, Obr.33 s.125, Tab.18 s.100; https://gmk.center/en/news/trinecke-zelezarny-is-investing-over-180-million-in-a-combined-cycle-power-station/ (17.6.2026); https://ekonomickydenik.cz/uhli-zemni-plyn-teplarna-ostrava/; volba modelu č. 4
- **Strana:** Tab.30 s.132; Obr.33 s.125; Tab.18 s.100
- **Citace:** očekávaný: Tab.30 PPE celkem 283 (2030), 433 (2031), 683 (2035), Energetika Třinec 93; Obr.33 popisek 33,4 % (odečteno z grafu); Tab.18 5 602 h (tabulka jako obrázek)
- **Poznámka, progresivní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Jen zemní plyn; druhá část je v řádku syntetický plyn. 2 000 h a podíly paliv jsou úsudek pro cestu s OZE a SMR. Třinec 62 MW: datum 2027 proti 2030 je rozpor zdrojů. Třebovice web 166 MWe, studie 190 MWe.
- **Poznámka, konzervativní:** Objem plynu definice cest neuvádí, procenta dávají jen podíl paliva, proto objem ze studie. Studie je jiný scénář, slouží jen pro parametr hodin a výkonu.
- **Koeficient, progresivní:** zima P10 1.9903, P50 2.2391, P90 2.3635; léto P10 0.0000, P50 0.0000, P90 1.2440; flexibilní ne; stupeň C
- **Koeficient, konzervativní:** zima P10 1.9903, P50 2.2391, P90 2.3635; léto P10 0.0000, P50 0.0000, P90 1.2440; flexibilní ne; stupeň C
- **Koeficient, odvození:** koef = dosažitelnost × 8 760 / 3 521 h: 0,9 × 8 760 / 3 521 = 2,239. Léto: PPE ČR 0 MW při letních maximech 2024 až 2025, tedy bez nucené výroby.
- **Koeficient, zdroj:** Dopadová studie Tab.30 s.132; ERÚ, čtvrtletní zprávy tab. 9.3
- **Koeficient, strana:** Tab.30 s.132
- **Koeficient, citace:** Tab.30 PPE celkem 283, 433, 683
- **Koeficient, poznámka:** Dosažitelnost 0,9 je úsudek. Roky 2030 a 2040 se liší od MW v řádku, viz metodika.

#### syntetický plyn z odpadu

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 0 | 148.5 | 231.0 | 288.0 | 0 | 154.0 | D |
| konzervativní | 0 | 148.5 | 231.0 | 288.0 | 0 | 152.5 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 0, P90 20; 2040 P10 50, P90 230
- **Meze 2030 a 2040, konzervativní:** 2030 P10 0, P90 20; 2040 P10 50, P90 230
- **Průběh:** plynule
- **Společný faktor:** cena
- **Jak se došlo:** Odpad vhodný pro ZEVO 360 000 t za rok minus 120 000 t pro spalovnu = 240 000 t. 240 000 t × výhřevnost podle neveřejné studie = 600 GWh paliva. 600 GWh × 70 % přeměna na plyn × 55 % účinnost bloku = 231,0 GWh.
- **Ze zdrojů:** Dopadová studie, s. 137 (360 000 t). Neveřejná studie ZEVO (120 000 t a výhřevnost), uvedena jsou jen čísla potřebná k výpočtu.
- **Odhad:** Přeměna 70 % a účinnost bloku 55 %. Jiné zdroje syntetického plynu, například důlní nebo koksárenský plyn, nejsou započítané, protože chybí podklad.
- **Podrobné odvození, progresivní:** Odpad vhodný pro ZEVO 360 000 t za rok minus 120 000 t pro spalovnu = 240 000 t. 240 000 t × výhřevnost podle neveřejné studie = 600 GWh paliva. 600 GWh × 70 % přeměna na plyn × 55 % účinnost bloku = 231,0 GWh. Rok 2040: asi dvě třetiny, náš odhad.
- **Podrobné odvození, konzervativní:** Odpad vhodný pro ZEVO 360 000 t za rok minus 120 000 t pro spalovnu = 240 000 t. 240 000 t × výhřevnost podle neveřejné studie = 600 GWh paliva. 600 GWh × 70 % přeměna na plyn × 55 % účinnost bloku = 231,0 GWh. Konzervativní podíl 10 % plynu by dal 240,5 GWh, omezeno dostupným odpadem. Rok 2040: asi dvě třetiny, náš odhad.
- **Zdroj:** Dopadová studie s.137 (360 kt); studie ZEVO, neveřejná (120 000 t a výhřevnost)
- **Strana:** s.137
- **Citace:** „připadá na MSK 360 kt paliva vhodného pro ZEVO“
- **Poznámka:** Účinnost přeměny 70 % (rozsah 55 až 80 %) a účinnost bloku 55 % (rozsah 45 až 60 %) jsou náš odhad bez zdroje. Jiné zdroje syntetického plynu, například důlní nebo koksárenský plyn, nejsou započítané, protože chybí podklad. Stejný odpad nelze použít dvakrát, proto je odečtena spalovna. Zdroj části vstupů je neveřejná studie, uvedena jsou jen čísla potřebná k výpočtu.
- **Koeficient, progresivní:** zima P10 3.5040, P50 3.9420, P90 4.1610; léto P10 0.0000, P50 0.0000, P90 2.1900; flexibilní ne; stupeň D
- **Koeficient, konzervativní:** zima P10 1.9903, P50 2.2391, P90 2.3635; léto P10 0.0000, P50 0.0000, P90 1.2440; flexibilní ne; stupeň C
- **Koeficient, odvození, progresivní:** koef = 0,9 × 8 760 / 2 000 h, hodiny pro 2050 z řádku.
- **Koeficient, odvození, konzervativní:** koef = 0,9 × 8 760 / 3 521 h = 2,239.
- **Koeficient, zdroj:** Dopadová studie Tab.30 s.132; tabulka položek (část 5)
- **Koeficient, strana:** Tab.30 s.132
- **Koeficient, citace, progresivní:** Tab.30 433
- **Koeficient, citace, konzervativní:** Tab.30 683
- **Koeficient, poznámka, progresivní:** Rok 2040 tímto vychází o 89 MW výš než 433 MW × 30 % × 0,9.
- **Koeficient, poznámka, konzervativní:** Dosažitelnost 0,9 je úsudek.

#### energetické využití odpadu

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 0 | 40.061 | 44.212 | 45.53 | 44.212 | 44.212 | B |
| konzervativní | 0 | 40.061 | 44.212 | 45.53 | 44.212 | 44.212 | B |

- **Meze 2030 a 2040, progresivní:** 2030 P10 40.061, P90 45.53; 2040 P10 40.061, P90 45.53
- **Meze 2030 a 2040, konzervativní:** 2030 P10 40.061, P90 45.53; 2040 P10 40.061, P90 45.53
- **Průběh:** skok
- **Společný faktor:** povolovani
- **Událost, progresivní:** Spuštění ZEVO, rok P10 2030, P50 2031, P90 2036
- **Událost, konzervativní:** Spuštění ZEVO, rok P10 2031, P50 2034, P90 2040
- **Jak se došlo:** Zařízení na 120 000 t odpadu za rok: dodávka 31 612 MWh + vlastní spotřeba 12 600 MWh = 44 212 MWh = 44,2 GWh.
- **Ze zdrojů:** Studie ZEVO, říjen 2026, neveřejná, uvedena jsou jen čísla potřebná k výpočtu.
- **Odhad:** Hodnota je ze studie. Rok spuštění je zčásti náš odhad a nepočítáme s tím, že se zařízení nepostaví.
- **Podrobné odvození:** Zařízení na 120 000 t odpadu za rok. Dodávka 31 612 MWh + vlastní spotřeba 12 600 MWh = 44 212 MWh brutto. Rozsah podle provozní varianty 40 061 až 45 530 MWh brutto.
- **Zdroj:** Technicko-ekonomická studie ZEVO 120 000 t/rok, říjen 2026, pracovní verze, neveřejná
- **Poznámka:** Zdroj je neveřejná studie, uvedena jsou jen čísla potřebná k výpočtu. Studie uvádí spuštění v lednu 2030 i v lednu 2031. Rok spuštění v konzervativní cestě a horní meze roku jsou náš odhad. Nahrazuje 72 GWh z Dopadové studie, s. 137. Pásmo nepočítá s tím, že se zařízení nepostaví.
- **Koeficient, progresivní:** zima P10 0.7665, P50 1.0402, P90 1.0950; léto P10 0.8000, P50 1.0000, P90 1.1000; flexibilní ne; stupeň D
- **Koeficient, konzervativní:** zima P10 0.7665, P50 1.0402, P90 1.0950; léto P10 0.8000, P50 1.0000, P90 1.1000; flexibilní ne; stupeň D
- **Koeficient, odvození:** Koeficient vychází z dosažitelnosti a provozních hodin zařízení. Zdroj je neveřejná studie, uvedena jsou jen čísla potřebná k výpočtu.
- **Koeficient, zdroj:** neveřejná studie ZEVO; Dopadová studie s.137
- **Koeficient, strana:** s.137
- **Koeficient, poznámka:** Stálý provoz, léto je úsudek.

#### baterie

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 0 | 0 | 0 | 0 | 0 | 0 | B |
| konzervativní | 0 | 0 | 0 | 0 | 0 | 0 | B |

- **Meze 2030 a 2040, progresivní:** 2030 P10 0, P90 0; 2040 P10 0, P90 0
- **Meze 2030 a 2040, konzervativní:** 2030 P10 0, P90 0; 2040 P10 0, P90 0
- **Průběh:** plynule
- **Společný faktor:** zadny
- **Jak se došlo:** Baterie elektřinu jen přesouvají, čistý přínos v roční výrobě je 0 GWh. Jejich ztráty má samostatný řádek.
- **Ze zdrojů:** žádný číselný vstup; pravidlo v metodice
- **Odhad:** žádný
- **Podrobné odvození:** Ze studie: nula v roční bilanci je pravidlo metodiky. Vlastní krok a jiné zdroje: 0 MWh čistého přínosu = 0.
- **Zdroj:** metodika modelu (část 4); Dopadová studie s.142, s.145, s.148, s.170
- **Strana:** s.145
- **Citace:** očekávaný: „až 50 MW s celkovou kapacitou 50 MWh“ (2030)
- **Poznámka:** Do roční výroby nevstupuje, jen ztrátami v řádku ztráty baterií (metodika modelu).
- **Koeficient, progresivní:** zima P10 0.0000, P50 0.0000, P90 0.0000; léto P10 0.0000, P50 0.0000, P90 0.0000; flexibilní ano; stupeň D
- **Koeficient, konzervativní:** zima P10 0.0000, P50 0.0000, P90 0.0000; léto P10 0.0000, P50 0.0000, P90 0.0000; flexibilní ano; stupeň D
- **Koeficient, odvození:** Energie v roce 0, proto koef 0. Výkon je ve výkonové tabulce (část 3): energie / 72 h.
- **Koeficient, zdroj:** Definice cest (část 2); tabulka položek, řádek ztráty baterií; Dopadová studie s.145
- **Koeficient, strana:** s.145
- **Koeficient, citace:** „o sumárním výkonu 1 GW a celkové kapacitě 1 GWh“
- **Koeficient, poznámka:** Baterie není zdroj, v zimě jen ve sloupci s bateriemi.

#### jiné skladování

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 0 | 0 | 0 | 0 | 0 | 0 | B |
| konzervativní | 0 | 0 | 0 | 0 | 0 | 0 | B |

- **Meze 2030 a 2040, progresivní:** 2030 P10 0, P90 0; 2040 P10 0, P90 0
- **Meze 2030 a 2040, konzervativní:** 2030 P10 0, P90 0; 2040 P10 0, P90 0
- **Průběh:** plynule
- **Společný faktor:** zadny
- **Jak se došlo:** Studie v kraji žádné velké úložiště neuvažuje, proto 0 GWh.
- **Ze zdrojů:** Dopadová studie, s. 148
- **Odhad:** žádný
- **Podrobné odvození:** Ze studie: nula. Vlastní krok a jiné zdroje: 0 MWh čistého přínosu = 0.
- **Zdroj:** metodika modelu (část 4); Dopadová studie s.142, s.145, s.148, s.170
- **Strana:** s.148
- **Citace:** očekávaný: bez přečerpávací elektrárny; gravitační a písková úložiště jen popis
- **Poznámka:** Přečerpávací ani jiné velké úložiště Dopadové studie v MSK neuvažuje (s.148), do bilance nevstupuje.
- **Koeficient, progresivní:** zima P10 0.0000, P50 0.0000, P90 0.0000; léto P10 0.0000, P50 0.0000, P90 0.0000; flexibilní ne; stupeň B
- **Koeficient, konzervativní:** zima P10 0.0000, P50 0.0000, P90 0.0000; léto P10 0.0000, P50 0.0000, P90 0.0000; flexibilní ne; stupeň B
- **Koeficient, odvození:** nulová roční energie, koeficient nemá na co působit
- **Koeficient, zdroj:** Dopadová studie s.89, s.148, s.170
- **Koeficient, strana:** s.89; s.148; s.170
- **Koeficient, citace:** viz tabulka položek (část 5)
- **Koeficient, poznámka:** Položka v bilanci nulová.

#### vodík zpět na elektřinu

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 0 | 0 | 0 | 0 | 0 | 0 | B |
| konzervativní | 0 | 0 | 0 | 0 | 0 | 0 | B |

- **Meze 2030 a 2040, progresivní:** 2030 P10 0, P90 0; 2040 P10 0, P90 0
- **Meze 2030 a 2040, konzervativní:** 2030 P10 0, P90 0; 2040 P10 0, P90 0
- **Průběh:** plynule
- **Společný faktor:** zadny
- **Jak se došlo:** Studie to má za velmi nepravděpodobné a nečísluje to, proto 0 GWh.
- **Ze zdrojů:** Dopadová studie, s. 142 a s. 170
- **Odhad:** žádný
- **Podrobné odvození:** Ze studie: nula. Vlastní krok a jiné zdroje: 0 MWh čistého přínosu = 0.
- **Zdroj:** metodika modelu (část 4); Dopadová studie s.142, s.145, s.148, s.170
- **Strana:** s.170
- **Citace:** extrémní: „velmi nepravděpodobná“
- **Poznámka:** Dopadová studie s.142 a s.170 ho nečísluje, extrémní scénář jej má za velmi nepravděpodobný. Ztráty cyklu jsou v řádcích výroby vodíku.
- **Koeficient, progresivní:** zima P10 0.0000, P50 0.0000, P90 0.0000; léto P10 0.0000, P50 0.0000, P90 0.0000; flexibilní ne; stupeň B
- **Koeficient, konzervativní:** zima P10 0.0000, P50 0.0000, P90 0.0000; léto P10 0.0000, P50 0.0000, P90 0.0000; flexibilní ne; stupeň B
- **Koeficient, odvození:** nulová roční energie, koeficient nemá na co působit
- **Koeficient, zdroj:** Dopadová studie s.89, s.148, s.170
- **Koeficient, strana:** s.89; s.148; s.170
- **Koeficient, citace:** viz tabulka položek (část 5)
- **Koeficient, poznámka:** Položka v bilanci nulová.

### Spotřeba

#### Třinecké železárny

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 769.2308 | 1000 | 1230.8 | 1939.2 | 1000 | 1000 | D |
| konzervativní | 769.2308 | 800 | 1000 | 1500 | 1000 | 1000 | C |

- **Meze 2030 a 2040, progresivní:** 2030 P10 800, P90 1500; 2040 P10 900, P90 1500
- **Meze 2030 a 2040, konzervativní:** 2030 P10 800, P90 1500; 2040 P10 800, P90 1500
- **Průběh:** skok
- **Společný faktor:** elektrifikace
- **Událost, progresivní:** Třinec: první oblouková pec, rok P10 2030, P50 2033, P90 2040
- **Událost, konzervativní:** Třinec: první oblouková pec, rok P10 2030, P50 2033, P90 2040
- **Jak se došlo, progresivní:** 769,2 GWh dnes (1 TWh / 1,30) + 2 pece × 230,8 GWh nárůst za jednu pec = 1 230,8 GWh.
- **Jak se došlo, konzervativní:** 769,2 GWh dnes + 50 % × (1 230,8 plná elektrifikace − 769,2) = 1 000 GWh.
- **Ze zdrojů:** Ekonomický deník 30. 1. 2025 (1 TWh, nárůst o 30 %)
- **Odhad, progresivní:** Plná elektrifikace a druhý stupeň stejně velký jako první jsou úsudek. Žádný zdroj 2050 neuvádí.
- **Odhad, konzervativní:** 50 % je dáno definicí cesty. 1 230,8 GWh je naše čtení plné elektrifikace.
- **Podrobné odvození, progresivní:** Ze studie: nic číselného. Vlastní krok a jiné zdroje: základ = 1 TWh / 1,30 = 769,2308 GWh. První EOP: 1 000,0 GWh (o 30 % na 1 TWh při 1,3 mil. t). Nárůst 230,8 GWh. Plná elektrifikace 2050: 769,2 + 2 × 230,8 = 1 230,8. P90: 769,2 + 2,6 mil. t × 0,45 MWh/t = 1 939,2.
- **Podrobné odvození, konzervativní:** Ze studie: nic číselného. Vlastní krok a jiné zdroje: 50 % elektrifikace: 769,2 + 50 % × (1 230,8 − 769,2) = 1 000,0 GWh; shodné s jednou EOP.
- **Zdroj, progresivní:** https://ekonomickydenik.cz/ekologizace-za-25-miliard-trinecke-zelezarny-investuji-do-nizkoemisni-budoucnosti/ (30.1.2025); https://trz.cz/assets/uploads/udrzitelnost/TZMS-NaseCestaKUhlikoveNeutralite.pdf; https://www.novinky.cz/clanek/ekonomika-trinecke-zelezarny-brzdi-plany-stavba-elektricke-obloukove-pece-bude-mit-minimalne-dva-roky-zpozdeni-40518385 (23.4.2025)
- **Zdroj, konzervativní:** https://ekonomickydenik.cz/ekologizace-za-25-miliard-trinecke-zelezarny-investuji-do-nizkoemisni-budoucnosti/ (30.1.2025); https://trz.cz/assets/uploads/udrzitelnost/TZMS-NaseCestaKUhlikoveNeutralite.pdf; https://www.novinky.cz/clanek/ekonomika-trinecke-zelezarny-brzdi-plany-stavba-elektricke-obloukove-pece-bude-mit-minimalne-dva-roky-zpozdeni-40518385 (23.4.2025); definice cest (část 2)
- **Strana:** s.110; s.151
- **Citace:** očekávaný: „vlivu spotřeby Green Werk Třineckých železáren“; číslo studie neuvádí
- **Poznámka, progresivní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Dopadovou studii nelze použít: Studie spotřebu ani nárůst nečísluje, proto tisk a podklady firmy. Tiskový údaj, 30 % z něj dává jen 0,18 MWh/t, což je málo proti běžným 0,4 až 0,5 MWh/t bez zdroje v podkladech; proto široká P90. Jiná souhrnná zpráva čte údaj jako 30 % nad 1 TWh, viz poznámky. Vazba na hutní plyny a na výrobu. Zlepší: EIA elektroocelárny Třinec. Plná elektrifikace v progresivní cestě je naše čtení, protože definice cest uvádí jen 50 % pro konzervativní cestu. Druhý stupeň leží mezi 2040 a 2050.
- **Poznámka, konzervativní:** Dopadovou studii nelze použít: Studie spotřebu ani nárůst nečísluje, proto tisk a podklady firmy. Tiskový údaj, 30 % z něj dává jen 0,18 MWh/t, což je málo proti běžným 0,4 až 0,5 MWh/t bez zdroje v podkladech; proto široká P90. Jiná souhrnná zpráva čte údaj jako 30 % nad 1 TWh, viz poznámky. Vazba na hutní plyny a na výrobu. Zlepší: EIA elektroocelárny Třinec.
- **Koeficient, progresivní:** zima P10 0.9882, P50 1.1364, P90 1.3835; léto P10 0.8102, P50 1.0263, P90 1.1343; flexibilní ne; stupeň D
- **Koeficient, konzervativní:** zima P10 0.9882, P50 1.1364, P90 1.3835; léto P10 0.8102, P50 1.0263, P90 1.1343; flexibilní ne; stupeň D
- **Koeficient, odvození:** Apriorní zima 1,00, 1,15, 1,40 × kalibrace 0,988; léto 0,75, 0,95, 1,05 × kalibrace 1,080. hutě běží nepřetržitě, oblouková pec kolísá.
- **Koeficient, zdroj:** ERÚ čtvrtletní zprávy 2024 a 2025, tab. 7.8 a kap. 9
- **Koeficient, strana:** rov.5 a 6 s.74
- **Koeficient, citace:** „Roční maximum zatížení elektrizační soustavy za MSK se nesleduje.“
- **Koeficient, poznámka:** Měsíční odběr VO z vvn v MSK je téměř plochý. Hodinový profil pece není k dispozici.

#### Nová huť

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 61.32 | 239.3 | 736.3 | 886.3 | 736.3 | 736.3 | D |
| konzervativní | 61.32 | 461.3 | 736.3 | 886.3 | 736.3 | 736.3 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 239.3, P90 886.3; 2040 P10 239.3, P90 886.3
- **Meze 2030 a 2040, konzervativní:** 2030 P10 461.3, P90 886.3; 2040 P10 461.3, P90 886.3
- **Průběh:** skok
- **Společný faktor:** elektrifikace
- **Událost, progresivní:** Nová huť: oblouková pec, rok P10 2031, P50 2034, P90 2042
- **Událost, konzervativní:** Nová huť: oblouková pec, rok P10 2031, P50 2034, P90 2045
- **Jak se došlo:** 61,3 GWh dnes (7 MW × 8 760 h) + oblouková pec 1,5 mil. t oceli × 0,45 MWh na tunu = 736,3 GWh.
- **Ze zdrojů:** tisk: SteelOrbis 19. 1. 2026, E15 (pec do 1,5 mil. t, ve fázi přípravy)
- **Odhad:** Dnešních 7 MW a 0,45 MWh na tunu jsou úsudek bez zdroje.
- **Podrobné odvození, progresivní:** Ze studie: nic číselného. Vlastní krok a jiné zdroje: základ: 7 MW × 8 760 h = 61,3200 GWh (úsudek). Oblouková pec do 1,5 mil. t: P50 61,3 + 1,5 mil. t × 0,45 MWh/t = 736,3; P10 61,3 + 1,0 mil. t × 0,178 MWh/t = 239,3; P90 61,3 + 1,5 mil. t × 0,55 MWh/t = 886,3.
- **Podrobné odvození, konzervativní:** Ze studie: nic číselného. Vlastní krok a jiné zdroje: základ: 7 MW × 8 760 h = 61,3200 GWh (úsudek). Oblouková pec do 1,5 mil. t: P50 61,3 + 1,5 mil. t × 0,45 MWh/t = 736,3; P10 61,3 + 1,0 mil. t × 0,178 MWh/t = 239,3; P90 61,3 + 1,5 mil. t × 0,55 MWh/t = 886,3. Konzervativní P10 61,3 + 400.
- **Zdroj, progresivní:** https://www.steelorbis.com/steel-news/latest-news/czech-based-nova-hu-plans-major-investments-and-eaf-preparation-in-2026-1430249.htm (19.1.2026); https://www.e15.cz/byznys/prumysl-a-energetika/veritele-poslali-liberty-ostrava-do-konkurzu-o-zkrachovalou-hut-maji-zajem-tri-kupci-1420502; Dopadová studie s.100-101
- **Zdroj, konzervativní:** https://www.steelorbis.com/steel-news/latest-news/czech-based-nova-hu-plans-major-investments-and-eaf-preparation-in-2026-1430249.htm (19.1.2026); https://www.e15.cz/byznys/prumysl-a-energetika/veritele-poslali-liberty-ostrava-do-konkurzu-o-zkrachovalou-hut-maji-zajem-tri-kupci-1420502; Dopadová studie s.100-101; definice cest (část 2)
- **Strana:** s.100-101
- **Citace:** očekávaný: dodávky TAMEH zastaveny v prosinci 2023; spotřebu neuvádí
- **Poznámka, progresivní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Dopadovou studii nelze použít: Studie spotřebu nečísluje a počítá s obnovou provozu Liberty, proto web a úsudek. Vlastní základ neznáme: vysoké pece stojí, nový vlastník od 1.10.2025, spotřebu nikdo neuvádí. Zlepší: odběr z ČEZ Distribuce. EOP je ve fázi přípravy.
- **Poznámka, konzervativní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Dopadovou studii nelze použít: Studie spotřebu nečísluje a počítá s obnovou provozu Liberty, proto web a úsudek. Definice cest: srovnatelné, proto stejná P50. Širší dolní mez a pozdější P90 jsou vlastní nejistota.
- **Koeficient, progresivní:** zima P10 0.9882, P50 1.1364, P90 1.3835; léto P10 0.8102, P50 1.0263, P90 1.1343; flexibilní ne; stupeň D
- **Koeficient, konzervativní:** zima P10 0.9882, P50 1.1364, P90 1.3835; léto P10 0.8102, P50 1.0263, P90 1.1343; flexibilní ne; stupeň D
- **Koeficient, odvození:** Apriorní zima 1,00, 1,15, 1,40 × kalibrace 0,988; léto 0,75, 0,95, 1,05 × kalibrace 1,080. jako Třinec.
- **Koeficient, zdroj:** ERÚ čtvrtletní zprávy 2024 a 2025, tab. 7.8 a kap. 9
- **Koeficient, strana:** rov.5 a 6 s.74
- **Koeficient, citace:** „Roční maximum zatížení elektrizační soustavy za MSK se nesleduje.“
- **Koeficient, poznámka:** Pec zatím nestojí, profil je převzatý.

#### ostatní průmysl a chemie

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 1571.4243 | 1421.4 | 1991.7 | 2357.1 | 1991.7 | 1991.7 | D |
| konzervativní | 1571.4243 | 1171.4 | 1571.4 | 1885.7 | 1621.4 | 1571.4 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 1421.4, P90 2171.4; 2040 P10 1421.4, P90 2042.9
- **Meze 2030 a 2040, konzervativní:** 2030 P10 1371.4, P90 1871.4; 2040 P10 1271.4, P90 1807.1
- **Průběh:** plynule
- **Společný faktor:** elektrifikace
- **Jak se došlo, progresivní:** 1 571,4243 GWh dnes + 420,245 GWh rozvojové plochy ze studie = 1 991,7 GWh.
- **Jak se došlo, konzervativní:** Drží hodnotu 2025 (1 571,4243 GWh, zaokrouhleno 1 571,4 GWh), protože rozvojové plochy ze studie patří jen do progresivní cesty.
- **Ze zdrojů, progresivní:** ERÚ čtvrtletní zprávy 2025, tab. 6.3 (Průmysl); Dopadová studie, s. 174 (420,245 GWh, extrémní scénář)
- **Ze zdrojů, konzervativní:** ERÚ čtvrtletní zprávy 2025, tab. 6.3 (Průmysl)
- **Odhad, progresivní:** Zařazení rozvojových ploch i držení po 2030 je úsudek. Základ je dopočtený zbytek.
- **Odhad, konzervativní:** Držení je úsudek bez zdroje. Základ je dopočtený zbytek.
- **Podrobné odvození, progresivní:** Ze studie: 420,245 GWh; jen progresivní. Vlastní krok a jiné zdroje: základ = reziduum: Průmysl 2 461,9753 − Třinec 769,2308 − Nová huť 61,3200 − doly 60,0000 = 1 571,4245 GWh. Progresivní P50 = základ + 420,245 GWh z rozvojových ploch (Tab.41-43), dále drženo. P90 s elektrifikací procesního tepla je úsudek.
- **Podrobné odvození, konzervativní:** Ze studie: 420,245 GWh; jen progresivní. Vlastní krok a jiné zdroje: základ = reziduum: Průmysl 2 461,9753 − Třinec 769,2308 − Nová huť 61,3200 − doly 60,0000 = 1 571,4245 GWh. Progresivní P50 = základ + 420,245 GWh z rozvojových ploch (Tab.41-43), dále drženo. P90 s elektrifikací procesního tepla je úsudek. Konzervativní P50 2040 a 2050 = základ.
- **Zdroj:** ERÚ, čtvrtletní zprávy 2025 Q1 až Q4, tab. 6.3, řádek MSK; Dopadová studie s.173-174
- **Strana:** s.174
- **Citace:** extrémní (kap. 6.4): „cca 420 245 MWh“
- **Poznámka:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Základ nese vadu rozdělení Průmysl a Energetika v 2025: tři čtvrtletí po přeřazení, jedno před ním. Přijetí rozvojových ploch do P50 i držení po 2030 je úsudek. Zahrnuje Hyundai, Biocel, MCHZ, Vítkovice; jejich spotřebu zdroje neuvádějí.
- **Koeficient, progresivní:** zima P10 0.9882, P50 1.1859, P90 1.3341; léto P10 0.8102, P50 1.0263, P90 1.1343; flexibilní ne; stupeň D
- **Koeficient, konzervativní:** zima P10 0.9882, P50 1.1859, P90 1.3341; léto P10 0.8102, P50 1.0263, P90 1.1343; flexibilní ne; stupeň D
- **Koeficient, odvození:** Apriorní zima 1,00, 1,20, 1,35 × kalibrace 0,988; léto 0,75, 0,95, 1,05 × kalibrace 1,080. měsíční VO z vn plus denní špička.
- **Koeficient, zdroj:** ERÚ čtvrtletní zprávy 2024 a 2025, tab. 7.8 a kap. 9
- **Koeficient, strana:** rov.5 a 6 s.74
- **Koeficient, citace:** „Roční maximum zatížení elektrizační soustavy za MSK se nesleduje.“
- **Koeficient, poznámka:** Víkend v létě snižuje odběr, přesný poměr pro kraj není znám.

#### doly

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 60.0 | 5 | 15 | 30 | 15 | 15 | D |
| konzervativní | 60.0 | 5 | 15 | 30 | 15 | 15 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 5, P90 30; 2040 P10 5, P90 30
- **Meze 2030 a 2040, konzervativní:** 2030 P10 5, P90 30; 2040 P10 5, P90 30
- **Průběh:** skok
- **Společný faktor:** zadny
- **Událost, progresivní:** Konec těžby OKD (ČSM), rok P10 2026, P50 2026, P90 2027
- **Událost, konzervativní:** Konec těžby OKD (ČSM), rok P10 2026, P50 2026, P90 2027
- **Jak se došlo:** Po konci těžby zbývá čerpání důlních vod, úsudek bez výpočtu = 15 GWh.
- **Ze zdrojů:** žádný pro hodnotu; oEnergetice a ČT24 jen ke konci těžby
- **Odhad:** Celá hodnota je úsudek, spotřebu dolů zdroje neuvádějí.
- **Podrobné odvození:** Ze studie: nic. Vlastní krok a jiné zdroje: základ: těžba 1 mil. t × 40 kWh/t = 40 + čerpání a větrání 20 = 60,0 GWh (úsudek). Po skončení těžby: čerpání vod 15 GWh.
- **Zdroj:** https://oenergetice.cz/uhli/dul-csm-se-chysta-na-ukonceni-tezby-a-likvidaci-okd-na-to-ma-33-miliardy-korun; https://ct24.ceskatelevize.cz/regiony/3274256-z-dolu-darkov-vyjel-posledni-vozik-cerneho-uhli-tezba-tam-definitivne-skoncila; Dopadová studie s.140
- **Poznámka:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Dopadovou studii nelze použít: Studie spotřebu dolů neuvádí. Spotřebu dolů zdroje neuvádějí. Konec ČSM 31.1.2026 je ze souhrnu vyhledávače, stránka neotevřena. Zlepší: údaj OKD nebo DIAMO. Může jít o sektor Energetika místo Průmyslu.
- **Koeficient, progresivní:** zima P10 0.9882, P50 1.0376, P90 1.1859; léto P10 0.9183, P50 1.0803, P90 1.1343; flexibilní ne; stupeň D
- **Koeficient, konzervativní:** zima P10 0.9882, P50 1.0376, P90 1.1859; léto P10 0.9183, P50 1.0803, P90 1.1343; flexibilní ne; stupeň D
- **Koeficient, odvození:** Apriorní zima 1,00, 1,05, 1,20 × kalibrace 0,988; léto 0,85, 1,00, 1,05 × kalibrace 1,080. plochý provoz, čerpání.
- **Koeficient, zdroj:** ERÚ čtvrtletní zprávy 2024 a 2025, tab. 7.8 a kap. 9
- **Koeficient, strana:** rov.5 a 6 s.74
- **Koeficient, citace:** „Roční maximum zatížení elektrizační soustavy za MSK se nesleduje.“
- **Koeficient, poznámka:** Úsudek, spotřebu dolů zdroje neuvádějí.

#### domácnosti bez vytápění

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 433.614 | 309.9 | 423.6 | 548.0 | 428.8 | 426.6 | D |
| konzervativní | 433.614 | 309.9 | 423.6 | 548.0 | 428.8 | 426.6 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 374.5, P90 473.1; 2040 P10 341.9, P90 508.6
- **Meze 2030 a 2040, konzervativní:** 2030 P10 374.5, P90 473.1; 2040 P10 341.9, P90 508.6
- **Průběh:** plynule
- **Společný faktor:** zadny
- **Řídicí vliv:** d_domacnosti
- **Jak se došlo:** 433,6 GWh dnes × 0,9770 počet domácností proti 2025 (úbytek obyvatel 0,8449 × menší domácnosti 1,1563) = 423,6 GWh.
- **Ze zdrojů:** ERÚ čtvrtletní zprávy 2025, tab. 6.3; Dopadová studie, Tab. 22 a Tab. 26 (odečtené položky); ČSÚ projekce obyvatel krajů; ČSÚ SLDB 2021
- **Odhad:** Velikost domácnosti (poloviční tempo poklesu) je úsudek. Stálá spotřeba na domácnost je úsudek. Základ je dopočtený zbytek.
- **Podrobné odvození, progresivní:** Ze studie: nic pro výhled. Vlastní krok a jiné zdroje: základ = reziduum: Domácnosti 1 487,7372 − TČ 441,4622 − přímotopy 597,661 − chlazení 15 = 433,6140 GWh. Výhled = základ × d_domacnosti. Revize: y = d_domacnosti × s, kde s je řádek s dnešními vstupy a d_domacnosti je v tabulce řídicích vlivů (část 6). 2030: P10 390,0 × 0,9603 = 374,5; P50 433,6 × 0,9889 = 428,8; P90 470,0 × 1,0066 = 473,1. 2040: P10 380,0 × 0,8997 = 341,9; P50 433,6 × 0,9838 = 426,6; P90 490,0 × 1,0380 = 508,6. 2050: P10 370,0 × 0,8377 = 309,9; P50 433,6 × 0,9770 = 423,6; P90 510,0 × 1,0746 = 548,0.
- **Podrobné odvození, konzervativní:** Ze studie: nic pro výhled. Vlastní krok a jiné zdroje: základ jako progresivní 433,6140 GWh. Výhled = základ × d_domacnosti. Revize: y = d_domacnosti × s, kde s je řádek s dnešními vstupy a d_domacnosti je v tabulce řídicích vlivů (část 6). 2030: P10 390,0 × 0,9603 = 374,5; P50 433,6 × 0,9889 = 428,8; P90 470,0 × 1,0066 = 473,1. 2040: P10 380,0 × 0,8997 = 341,9; P50 433,6 × 0,9838 = 426,6; P90 490,0 × 1,0380 = 508,6. 2050: P10 370,0 × 0,8377 = 309,9; P50 433,6 × 0,9770 = 423,6; P90 510,0 × 1,0746 = 548,0.
- **Zdroj:** ERÚ, čtvrtletní zprávy 2025 Q1 až Q4, tab. 6.3, řádek MSK; Dopadová studie Tab.22, Tab.26; ČSÚ, Projekce obyvatelstva v krajích ČR do roku 2080, kód 130052-24, 12.12.2024, Tab. 4_CZ080, řádek Počet obyvatel: celkem, https://csu.gov.cz/produkty/projekce-obyvatelstva-v-krajich-cr-do-roku-2080; ČSÚ, Základní výsledky SLDB 2021 Moravskoslezský kraj , s.17, s.22, s.79; https://scitani.gov.cz/velikost-hospodarici-domacnosti
- **Strana:** Tab.6 s.40; s.109
- **Citace:** Tab.6 Domácnosti 1 375 001,4 MWh (2023); výhled po sektorech studie odmítá jako nespolehlivý; „Celkový počet hospodařících domácností v kraji dosáhl hodnoty 541 267. Ve srovnání s předchozím sčítáním v roce 2011 se jejich počet zvýšil o 33,7 tisíce, tj. o 6,6 %.“; scitani.gov.cz „Moravskoslezský kraj“ „541 276“ „2,12“; s.79 „Počet obyvatel 1 257 090 1 278 726 1 265 019 1 205 836 1 162 841“
- **Poznámka, progresivní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Malá hodnota plyne z toho, že spotřebiče na tarifech vytápění jsou v jiných řádcích. Úsporu nese samostatný řádek. Do Domácností patří i domácí nabíjení aut; ERÚ ho nedělí, viz osobní auta. Hodnoty ve sloupcích jsou y včetně d_domacnosti, znovu nenásobit. Vliv d_domacnosti má stupeň D, viz řídicí vlivy (část 6).
- **Poznámka, konzervativní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Definice cest neuvádí rozdíl mezi cestami. Hodnoty ve sloupcích jsou y včetně d_domacnosti, znovu nenásobit. Vliv d_domacnosti má stupeň D, viz řídicí vlivy (část 6).
- **Koeficient, progresivní:** zima P10 1.2847, P50 1.7788, P90 2.2729; léto P10 0.7562, P50 1.0803, P90 1.2964; flexibilní ne; stupeň D
- **Koeficient, konzervativní:** zima P10 1.2847, P50 1.7788, P90 2.2729; léto P10 0.7562, P50 1.0803, P90 1.2964; flexibilní ne; stupeň D
- **Koeficient, odvození:** Apriorní zima 1,30, 1,80, 2,30 × kalibrace 0,988; léto 0,70, 1,00, 1,20 × kalibrace 1,080. večerní špička spotřebičů.
- **Koeficient, zdroj:** OTE, Normalizované TDD (stránka https://www.ote-cr.cz/cs/statistika/typove-diagramy-dodavek-elektriny, soubor nestažen)
- **Koeficient, strana:** rov.5 a 6 s.74
- **Koeficient, citace:** „Roční maximum zatížení elektrizační soustavy za MSK se nesleduje.“
- **Koeficient, poznámka:** Úsudek. Třídy TDD by daly přímé číslo, model je nepoužívá.

#### služby a veřejný sektor

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 995.8321 | 880 | 995.8 | 1250 | 995.8 | 995.8 | D |
| konzervativní | 995.8321 | 880 | 995.8 | 1250 | 995.8 | 995.8 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 920, P90 1080; 2040 P10 900, P90 1150
- **Meze 2030 a 2040, konzervativní:** 2030 P10 920, P90 1080; 2040 P10 900, P90 1150
- **Průběh:** plynule
- **Společný faktor:** zadny
- **Jak se došlo:** Drží hodnotu 2025 (995,8321 GWh, zaokrouhleno 995,8 GWh), protože zdroj pro výhled není a studie sektorové položky nepovažuje za spolehlivé.
- **Ze zdrojů:** ERÚ čtvrtletní zprávy 2025, tab. 6.3; Dopadová studie, s. 109
- **Odhad:** Držení je úsudek bez zdroje. Základ je dopočtený zbytek.
- **Podrobné odvození:** Ze studie: nic pro výhled. Vlastní krok a jiné zdroje: základ = reziduum: Služby 1 355,4723 + Ostatní 20,5593 − TČ 10,9755 − přímotopy 324,224 − chlazení 45 = 995,8321 GWh. Výhled drží základ, zdroj pro to není.
- **Zdroj:** ERÚ, čtvrtletní zprávy 2025 Q1 až Q4, tab. 6.3, řádek MSK
- **Strana:** Tab.6 s.40; s.109
- **Citace:** Tab.6 1 208 471,5 MWh (2023); výhled po sektorech studie odmítá jako nespolehlivý
- **Poznámka:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Sektor Ostatní z tab. 6.3 je přičten sem, nemá vlastní položku. Doprava v tab. 6.3 je pro železnici příliš malá; trakce je zřejmě zde (Doprava klesla 2016-2017 z 356 na 52 GWh, s.41). Studie s.109 uvádí, že položky sektorů nejsou spolehlivá základna pro odhad.
- **Koeficient, progresivní:** zima P10 1.0870, P50 1.3341, P90 1.5811; léto P10 0.6482, P50 0.9723, P90 1.4044; flexibilní ne; stupeň D
- **Koeficient, konzervativní:** zima P10 1.0870, P50 1.3341, P90 1.5811; léto P10 0.6482, P50 0.9723, P90 1.4044; flexibilní ne; stupeň D
- **Koeficient, odvození:** Apriorní zima 1,10, 1,35, 1,60 × kalibrace 0,988; léto 0,60, 0,90, 1,30 × kalibrace 1,080. konec pracovního dne, osvětlení.
- **Koeficient, zdroj:** ERÚ čtvrtletní zprávy 2024 a 2025, tab. 7.8 a kap. 9
- **Koeficient, strana:** rov.5 a 6 s.74
- **Koeficient, citace:** „Roční maximum zatížení elektrizační soustavy za MSK se nesleduje.“
- **Koeficient, poznámka:** Úsudek. P90 v létě je pracovní den.

#### vytápění tepelnými čerpadly

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 452.4378 | 788.0 | 1188.6 | 1635.4 | 651.3 | 1004.2 | D |
| konzervativní | 452.4378 | 296.9 | 549.2 | 876.3 | 529.1 | 577.8 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 437.2, P90 779.9; 2040 P10 591.9, P90 1380.4
- **Meze 2030 a 2040, konzervativní:** 2030 P10 405.4, P90 707.6; 2040 P10 366.8, P90 880.8
- **Průběh:** plynule
- **Společný faktor:** elektrifikace
- **Řídicí vliv:** d_vytapeni
- **Historické maximum tempa, GWh za rok:** 50.6766
- **Jak se došlo, progresivní:** 158 996 odběrných míst (97 % ze 163 913 domů) × 8,9 MWh + 29,6 GWh podnikatelé = 1 444,6 GWh × 0,8228 méně domácností a lepší zateplení = 1 188,6 GWh.
- **Jak se došlo, konzervativní:** 75 000 odběrných míst × 8,9 MWh = 667,5 GWh × 0,8228 méně domácností a lepší zateplení = 549,2 GWh.
- **Ze zdrojů, progresivní:** Dopadová studie, s. 113 až 114 (8,9 MWh, 163 913 domů), s. 165 (výjimka 3 %); ČSÚ projekce obyvatel krajů; ČSÚ SLDB 2021; Vnitrostátní plán, Tab. 21 s. 56
- **Ze zdrojů, konzervativní:** Dopadová studie, s. 113 až 114 (8,9 MWh); ČSÚ projekce obyvatel krajů; ČSÚ SLDB 2021; Vnitrostátní plán, Tab. 21 s. 56
- **Odhad, progresivní:** Poloviční tempo zateplení proti plánu, běžná spotřeba 2,5 MWh, velikost domácnosti a prodloužený trend podnikatelů jsou úsudek.
- **Odhad, konzervativní:** 75 000 míst je úsudek (poloviční tempo do 2030, pak zastavení). Poloviční tempo zateplení, běžná spotřeba 2,5 MWh a velikost domácnosti jsou úsudek.
- **Podrobné odvození, progresivní:** Ze studie: počty OM, sklon, 8,9 MWh, 163 913 RD, 3 %. Vlastní krok a jiné zdroje: základ: domácnosti (33 950 + 3 × 5 217,5) OM × 8,9 MWh = 441,4622; podnikatelé 405,5 OM × 27,1 MWh = 10,9755; součet 452,4378 GWh. P50: OM × 8,9 MWh + podnikatelé. 2030 75 690 OM; 2040 127 865 OM; 2050 163 913 RD × 97 % = 158 996 OM. P10 2050 bez zateplení: 163 913 × 85 % × 8,9 MWh = 1 240,0; 2030 P10 bez zateplení: 54 820 OM × 8,9 MWh = 487,9. Zateplení nese vliv d_vytapeni. P90 přidává velká TČ 53,7 PJ × 12,05 % / COP 3 × 50 % = 299,5. Revize: y = d_vytapeni × s, kde s je řádek s dnešními vstupy a d_vytapeni je v tabulce řídicích vlivů (část 6). 2030: P10 487,9 × 0,8960 = 437,2; P50 688,3 × 0,9463 = 651,3; P90 801,0 × 0,9736 = 779,9. 2040: P10 812,1 × 0,7289 = 591,9; P50 1 160,1 × 0,8656 = 1 004,2; P90 1 464,6 × 0,9425 = 1 380,4. 2050: P10 1 240,0 × 0,6355 = 788,0; P50 1 444,6 × 0,8228 = 1 188,6; P90 1 744,1 × 0,9377 = 1 635,4.
- **Podrobné odvození, konzervativní:** Ze studie: 33 950 OM a 8,9 MWh. Vlastní krok a jiné zdroje: základ: domácnosti (33 950 + 3 × 5 217,5) OM × 8,9 MWh = 441,4622; podnikatelé 405,5 OM × 27,1 MWh = 10,9755; součet 452,4378 GWh. 2030: 62 820 OM × 8,9 MWh; 2040 a 2050: 75 000 OM × 8,9 MWh = 667,5. Revize: y = d_vytapeni × s, kde s je řádek s dnešními vstupy a d_vytapeni je v tabulce řídicích vlivů (část 6). 2030: P10 452,4 × 0,8960 = 405,4; P50 559,1 × 0,9463 = 529,1; P90 726,8 × 0,9736 = 707,6. 2040: P10 503,2 × 0,7289 = 366,8; P50 667,5 × 0,8656 = 577,8; P90 934,5 × 0,9425 = 880,8. 2050: P10 467,2 × 0,6355 = 296,9; P50 667,5 × 0,8228 = 549,2; P90 934,5 × 0,9377 = 876,3.
- **Zdroj, progresivní:** Dopadová studie s.113-114, Tab.22; Vnitrostátní plán Tab.21-22 s.56-57, Tab.102 s.351-352; ČSÚ, Projekce obyvatelstva v krajích ČR do roku 2080, kód 130052-24, 12.12.2024, Tab. 4_CZ080, řádek Počet obyvatel: celkem, https://csu.gov.cz/produkty/projekce-obyvatelstva-v-krajich-cr-do-roku-2080; ČSÚ, Základní výsledky SLDB 2021 Moravskoslezský kraj , s.17, s.22, s.79; https://scitani.gov.cz/velikost-hospodarici-domacnosti; Vnitrostátní plán Tab.21 s.56, s.54-55
- **Zdroj, konzervativní:** Dopadová studie s.113-114, Tab.22; Vnitrostátní plán Tab.21-22 s.56-57, Tab.102 s.351-352; volba modelu č. 5; ČSÚ, Projekce obyvatelstva v krajích ČR do roku 2080, kód 130052-24, 12.12.2024, Tab. 4_CZ080, řádek Počet obyvatel: celkem, https://csu.gov.cz/produkty/projekce-obyvatelstva-v-krajich-cr-do-roku-2080; ČSÚ, Základní výsledky SLDB 2021 Moravskoslezský kraj , s.17, s.22, s.79; https://scitani.gov.cz/velikost-hospodarici-domacnosti; Vnitrostátní plán Tab.21 s.56, s.54-55
- **Strana, progresivní:** s.113-114; Tab.22 s.113; s.165
- **Strana, konzervativní:** s.113-114
- **Citace, progresivní:** „z 23 515 v roce 2020 na 33 950 v roce 2022“; „z 268 OM v roce 2020 na 323“; „8,9 MWh“; „163 913 rodinných domů“; extrémní: výjimka „(3 %)“ (tabulka jako obrázek); „Celkový počet hospodařících domácností v kraji dosáhl hodnoty 541 267. Ve srovnání s předchozím sčítáním v roce 2011 se jejich počet zvýšil o 33,7 tisíce, tj. o 6,6 %.“; scitani.gov.cz „Moravskoslezský kraj“ „541 276“ „2,12“; s.79 „Počet obyvatel 1 257 090 1 278 726 1 265 019 1 205 836 1 162 841“; Tab.21 „Měrná potřeba tepla na vytápění [MJ/( m2.rok)] 491 386 292 246“ (2020, 2030, 2040, 2050); s.54 „ten představuje ideální scénář“; s.55 „zvýšením renovační míry na přibližně dvojnásobek“
- **Citace, konzervativní:** „33 950 v roce 2022“; „8,9 MWh“ (očekávaný); „Celkový počet hospodařících domácností v kraji dosáhl hodnoty 541 267. Ve srovnání s předchozím sčítáním v roce 2011 se jejich počet zvýšil o 33,7 tisíce, tj. o 6,6 %.“; scitani.gov.cz „Moravskoslezský kraj“ „541 276“ „2,12“; s.79 „Počet obyvatel 1 257 090 1 278 726 1 265 019 1 205 836 1 162 841“; Tab.21 „Měrná potřeba tepla na vytápění [MJ/( m2.rok)] 491 386 292 246“ (2020, 2030, 2040, 2050); s.54 „ten představuje ideální scénář“; s.55 „zvýšením renovační míry na přibližně dvojnásobek“
- **Poznámka, progresivní:** Tarifní data obsahují i běžnou spotřebu na odběrném místě, řádek proto není čisté teplo. Mez: počet OM 2050 je omezen 163 913 rodinnými domy; regrese by jinak dala 180 040 OM. Podíl MSK na velkých TČ podle spotřeby je měřítko s rizikem. V P10 a P90: 2,5 MWh, COP 3 a 50 % jsou úsudek. Vazba: snižuje teplárenskou výrobu. Tempo: Dopadová studie s.113-114, domácnosti OM 2020 23 515, 2021 29 209, 2022 33 950; největší roční přírůstek 29 209 − 23 515 = 5 694 OM × 8,9 MWh = 50,6766 GWh/rok. Hodnoty ve sloupcích jsou y včetně d_vytapeni, znovu nenásobit. Vliv d_vytapeni má stupeň D, viz řídicí vlivy (část 6).
- **Poznámka, konzervativní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Procento 300 % se na elektřinu nepoužije (volba modelu č. 5): jde o energii na vstupu. Elektřina na teplo v této cestě zůstává pod progresivní. Počty OM jsou úsudek: poloviční tempo do 2030, pak zastavení. Tempo: Dopadová studie s.113-114, domácnosti OM 2020 23 515, 2021 29 209, 2022 33 950; největší roční přírůstek 29 209 − 23 515 = 5 694 OM × 8,9 MWh = 50,6766 GWh/rok. Hodnoty ve sloupcích jsou y včetně d_vytapeni, znovu nenásobit. Vliv d_vytapeni má stupeň D, viz řídicí vlivy (část 6).
- **Koeficient, progresivní:** zima P10 2.7670, P50 3.5576, P90 4.5458; léto P10 0.1620, P50 0.3241, P90 0.5402; flexibilní ne; stupeň C
- **Koeficient, konzervativní:** zima P10 2.7670, P50 3.5576, P90 4.5458; léto P10 0.1620, P50 0.3241, P90 0.5402; flexibilní ne; stupeň C
- **Koeficient, odvození:** Apriorní zima 2,80, 3,60, 4,60 × kalibrace 0,988; léto 0,15, 0,30, 0,50 × kalibrace 1,080. Měřený výkyv MOO + MOP v MSK 2025: základ léta 185,4 MW, nejchladnější měsíc +140,5 MW, průměr výkyvu 59,6 MW, poměr 2,36. Pak chladný den proti průměru měsíce asi 1,5 a soudobost a zhoršení COP, což je odhad bez zdroje.
- **Koeficient, zdroj:** ERÚ čtvrtletní zprávy 2024 a 2025, tab. 7.8 a kap. 9; Love et al. 2017, Applied Energy 204, 332-342, DOI 10.1016/j.apenergy.2017.07.026
- **Koeficient, strana:** rov.5 a 6 s.74
- **Koeficient, citace:** „Roční maximum zatížení elektrizační soustavy za MSK se nesleduje.“
- **Koeficient, poznámka:** Love: pohromadě 1,7 kW na odběrné místo, v noci 40 % špičky. Agregovaná špička je tam ráno.

#### přímotopy

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 921.885 | 0.0 | 0.0 | 284.8 | 843.3 | 389.3 | D |
| konzervativní | 921.885 | 330.8 | 626.8 | 806.9 | 843.3 | 717.3 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 723.2, P90 888.5; 2040 P10 225.1, P90 617.8
- **Meze 2030 a 2040, konzervativní:** 2030 P10 768.4, P90 927.6; 2040 P10 487.8, P90 855.4
- **Průběh:** plynule
- **Společný faktor:** elektrifikace
- **Řídicí vliv:** d_primotopy
- **Jak se došlo, progresivní:** Studie v extrémním scénáři nechává přímotopy klesnout na nulu a progresivní cesta to přebírá, proto 0,0 GWh.
- **Jak se došlo, konzervativní:** 886,964 GWh v 2030 − 20 let × 6,984 GWh ročního poklesu = 747,3 GWh × 0,8387 méně domácností a lepší zateplení = 626,8 GWh.
- **Ze zdrojů, progresivní:** Dopadová studie, s. 166
- **Ze zdrojů, konzervativní:** Dopadová studie, Tab. 26 s. 122 (886,964 GWh, pokles); ČSÚ projekce obyvatel krajů; ČSÚ SLDB 2021; Vnitrostátní plán, Tab. 21 s. 56
- **Odhad, progresivní:** Žádné číslo. Převzetí extrémního scénáře je naše volba.
- **Odhad, konzervativní:** Prodloužení poklesu za rok 2030, poloviční tempo zateplení, běžná spotřeba 2,5 MWh a velikost domácnosti jsou úsudek.
- **Podrobné odvození, progresivní:** Ze studie: 921 885, 886 964, sklon, nula. Vlastní krok a jiné zdroje: základ: Tab.26, rok 2025, celkem 921 885 MWh (podnikatelé 324 224, domácnosti 597 661). 2030: 886 964 MWh. Dále lineární pokles počtu OM (s.122). Progresivní: 2050 nula podle extrémního scénáře s.166, 2040 polovina z 886,964. Revize: y = d_primotopy × s, kde s je řádek s dnešními vstupy a d_primotopy je v tabulce řídicích vlivů (část 6). 2030: P10 800,0 × 0,9040 = 723,2; P50 887,0 × 0,9507 = 843,3; P90 910,0 × 0,9764 = 888,5. 2040: P10 300,0 × 0,7504 = 225,1; P50 443,5 × 0,8778 = 389,3; P90 650,0 × 0,9504 = 617,8. 2050: P10 0,0 × 0,6617 = 0,0; P50 0,0 × 0,8387 = 0,0; P90 300,0 × 0,9493 = 284,8.
- **Podrobné odvození, konzervativní:** Ze studie: 921 885, 886 964, sklon, nula. Vlastní krok a jiné zdroje: základ: Tab.26, rok 2025, celkem 921 885 MWh (podnikatelé 324 224, domácnosti 597 661). 2030: 886 964 MWh. Dále lineární pokles počtu OM (s.122). Konzervativní: pokles Tab.26 6,984 GWh/rok prodloužen na 2040 a 2050. Revize: y = d_primotopy × s, kde s je řádek s dnešními vstupy a d_primotopy je v tabulce řídicích vlivů (část 6). 2030: P10 850,0 × 0,9040 = 768,4; P50 887,0 × 0,9507 = 843,3; P90 950,0 × 0,9764 = 927,6. 2040: P10 650,0 × 0,7504 = 487,8; P50 817,1 × 0,8778 = 717,3; P90 900,0 × 0,9504 = 855,4. 2050: P10 500,0 × 0,6617 = 330,8; P50 747,3 × 0,8387 = 626,8; P90 850,0 × 0,9493 = 806,9.
- **Zdroj, progresivní:** Dopadová studie Tab.26 s.122, s.166; ČSÚ, Projekce obyvatelstva v krajích ČR do roku 2080, kód 130052-24, 12.12.2024, Tab. 4_CZ080, řádek Počet obyvatel: celkem, https://csu.gov.cz/produkty/projekce-obyvatelstva-v-krajich-cr-do-roku-2080; ČSÚ, Základní výsledky SLDB 2021 Moravskoslezský kraj , s.17, s.22, s.79; https://scitani.gov.cz/velikost-hospodarici-domacnosti; Vnitrostátní plán Tab.21 s.56, s.54-55
- **Zdroj, konzervativní:** Dopadová studie Tab.26 s.122; volba modelu č. 5; ČSÚ, Projekce obyvatelstva v krajích ČR do roku 2080, kód 130052-24, 12.12.2024, Tab. 4_CZ080, řádek Počet obyvatel: celkem, https://csu.gov.cz/produkty/projekce-obyvatelstva-v-krajich-cr-do-roku-2080; ČSÚ, Základní výsledky SLDB 2021 Moravskoslezský kraj , s.17, s.22, s.79; https://scitani.gov.cz/velikost-hospodarici-domacnosti; Vnitrostátní plán Tab.21 s.56, s.54-55
- **Strana:** Tab.26 s.122; s.166
- **Citace:** očekávaný: Tab.26 celkem 921 885 (2025), 886 964 (2030); „cca o 11 %“; extrémní: „Podíl přímotopů postupně klesne na nulu“ (tabulka jako obrázek); „Celkový počet hospodařících domácností v kraji dosáhl hodnoty 541 267. Ve srovnání s předchozím sčítáním v roce 2011 se jejich počet zvýšil o 33,7 tisíce, tj. o 6,6 %.“; scitani.gov.cz „Moravskoslezský kraj“ „541 276“ „2,12“; s.79 „Počet obyvatel 1 257 090 1 278 726 1 265 019 1 205 836 1 162 841“; Tab.21 „Měrná potřeba tepla na vytápění [MJ/( m2.rok)] 491 386 292 246“ (2020, 2030, 2040, 2050); s.54 „ten představuje ideální scénář“; s.55 „zvýšením renovační míry na přibližně dvojnásobek“
- **Poznámka, progresivní:** Základ je předpověď studie pro 2025 z dat 2020-2022, ne měření za 2025. Zlepší: spotřeba podle sazeb od ČEZ Distribuce. Část tarifní spotřeby jsou běžné spotřebiče. Kvantil faktoru se zde čte obráceně. Hodnoty ve sloupcích jsou y včetně d_primotopy, znovu nenásobit. Vliv d_primotopy má stupeň D, viz řídicí vlivy (část 6).
- **Poznámka, konzervativní:** Přímý ohřev zůstává, to je část významu 300 % z volba modelu č. 5. Kvantil faktoru se zde čte obráceně. Hodnoty ve sloupcích jsou y včetně d_primotopy, znovu nenásobit. Vliv d_primotopy má stupeň D, viz řídicí vlivy (část 6).
- **Koeficient, progresivní:** zima P10 1.3835, P50 1.8776, P90 2.5694; léto P10 0.4321, P50 0.8102, P90 1.0803; flexibilní ne; stupeň D
- **Koeficient, konzervativní:** zima P10 1.3835, P50 1.8776, P90 2.5694; léto P10 0.4321, P50 0.8102, P90 1.0803; flexibilní ne; stupeň D
- **Koeficient, odvození:** Apriorní zima 1,40, 1,90, 2,60 × kalibrace 0,988; léto 0,40, 0,75, 1,00 × kalibrace 1,080. Sezónní výkyv MOO + MOP 522,1 GWh je menší než řádky čerpadel a přímotopů, řádek tedy nese běžnou tarifní spotřebu. Čerpadla sezónní 70 %, úsudek: 316,7 GWh. Přímotopy sezónně (522,1 − 316,7) / 921,9 = 0,223. Zima: 0,777 × 1,5 + 0,223 × 2,36 × 1,5 = 1,95, zaokrouhleno 1,9. Léto: nesezónní podíl, zaokrouhleno 0,75.
- **Koeficient, zdroj:** ERÚ čtvrtletní zprávy 2024 a 2025, tab. 7.8 a kap. 9; Dopadová studie Tab.26 s.122
- **Koeficient, strana:** rov.5 a 6 s.74
- **Koeficient, citace:** „Roční maximum zatížení elektrizační soustavy za MSK se nesleduje.“
- **Koeficient, poznámka:** Základ řádku je předpověď studie z tarifů, ne měření vytápění. HDO může špičku dál snížit. První průchod s 2,4 a 0,25 byl horší v obou okamžicích.

#### elektrokotle v teplárnách

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 0 | 50 | 150 | 400 | 15 | 80 | D |
| konzervativní | 0 | 2 | 9 | 40 | 9 | 9 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 5, P90 40; 2040 P10 20, P90 200
- **Meze 2030 a 2040, konzervativní:** 2030 P10 2, P90 20; 2040 P10 2, P90 30
- **Průběh:** plynule
- **Společný faktor:** cena
- **Jak se došlo, progresivní:** 150 MW × 1 000 h za rok = 150 GWh.
- **Jak se došlo, konzervativní:** (18 + 12) MW kotle ze studie × 300 h za rok = 9 GWh.
- **Ze zdrojů, progresivní:** Dopadová studie, s. 121 a s. 166 (jen dnešní kotle 18 a 12 MW)
- **Ze zdrojů, konzervativní:** Dopadová studie, s. 121 a s. 166 (18 a 12 MW)
- **Odhad, progresivní:** 150 MW i 1 000 h jsou úsudek, celá hodnota je úsudek.
- **Odhad, konzervativní:** 300 h je úsudek podle řádu hodin se zápornou cenou na s. 121.
- **Podrobné odvození, progresivní:** Ze studie: 18 a 12 MW. Vlastní krok a jiné zdroje: 2030: (18 + 12) MW × 500 h = 15,0. 2040: 80 MW × 1 000 h = 80,0. 2050: 150 MW × 1 000 h = 150,0.
- **Podrobné odvození, konzervativní:** Ze studie: 18 a 12 MW. Vlastní krok a jiné zdroje: 30 MW × 300 h = 9,0.
- **Zdroj, progresivní:** Dopadová studie s.120-122, s.166
- **Zdroj, konzervativní:** Dopadová studie s.120-122
- **Strana:** s.121; s.166
- **Citace:** očekávaný: „Bude mít výkon 18 MW“; extrémní: kotel 12 MW; hodiny studie neuvádí
- **Poznámka, progresivní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Základ 0: studie uvádí, že v MSK nejsou v provozu; start kotle 18 MW v Třebovicích nebyl ověřen. Studie neuvádí hodiny, jen hodiny se zápornou cenou. Vazba: nahrazují teplo z kogenerace.
- **Poznámka, konzervativní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Bez dalších kotlů; s.122 výrobci další investice neuvažují. 300 h odpovídá řádu hodin s cenou pod nulou v s.121.
- **Koeficient, progresivní:** zima P10 0.0000, P50 0.0000, P90 0.2000; léto P10 0.0000, P50 2.6280, P90 8.7600; flexibilní ano; stupeň D
- **Koeficient, konzervativní:** zima P10 0.0000, P50 0.0000, P90 0.2000; léto P10 0.0000, P50 8.7600, P90 29.2000; flexibilní ano; stupeň D
- **Koeficient, odvození, progresivní:** Zima vypnuto. Léto: 1 000 h v řádku, plný výkon 8 760 / 1 000 = 8,76; P50 30 % výkonu, teplo v létě je jen ohřev vody, úsudek.
- **Koeficient, odvození, konzervativní:** Zima vypnuto. Léto: 300 h v řádku, plný výkon 8 760 / 300 = 29,2; P50 30 % výkonu, úsudek.
- **Koeficient, zdroj:** Dopadová studie s.57, s.121, s.165
- **Koeficient, strana:** s.57; s.165
- **Koeficient, citace:** „V zimním období se průmyslové elektrokotle příliš neuplatní“
- **Koeficient, poznámka:** Zima podle studie, léto úsudek.

#### chlazení

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 60.0 | 93.2 | 191.1 | 412.5 | 89.6 | 139.0 | D |
| konzervativní | 60.0 | 74.6 | 158.4 | 361.0 | 84.6 | 119.2 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 49.2, P90 150.4; 2040 P10 67.1, P90 254.0
- **Meze 2030 a 2040, konzervativní:** 2030 P10 49.2, P90 140.4; 2040 P10 57.5, P90 223.5
- **Průběh:** plynule
- **Společný faktor:** zadny
- **Řídicí vliv:** d_chlazeni
- **Jak se došlo, progresivní:** 540 000 domácností × 30 % × 0,5 MWh = 81 GWh + služby 8 % × 1 400 GWh = 112 GWh, součet 193 GWh × 0,9903 vliv počtu domácností = 191,1 GWh.
- **Jak se došlo, konzervativní:** 160 GWh úsudek × 0,9903 vliv počtu domácností = 158,4 GWh.
- **Ze zdrojů, progresivní:** ČSÚ projekce obyvatel krajů a ČSÚ SLDB 2021 (počet domácností)
- **Ze zdrojů, konzervativní:** ČSÚ projekce obyvatel krajů a ČSÚ SLDB 2021 (vliv počtu domácností)
- **Odhad, progresivní:** 30 %, 0,5 MWh, 8 % a 1 400 GWh jsou úsudek. Celá hodnota je úsudek, zdroje chlazení nečíslují.
- **Odhad, konzervativní:** 160 GWh je úsudek bez výpočtu. Celá hodnota je úsudek, zdroje chlazení nečíslují.
- **Podrobné odvození, progresivní:** Ze studie: nic. Vlastní krok a jiné zdroje: základ: domácnosti 15 GWh (1 % sektoru) + služby 45 GWh (3,3 % sektoru), úsudek. 2050 P50: 540 000 domácností × 30 % × 0,5 MWh = 81 + služby 8 % × 1 400 = 112; součet 193 GWh. Revize: y = d_chlazeni × s, kde s je řádek s dnešními vstupy a d_chlazeni je v tabulce řídicích vlivů (část 6). 2030: P10 50,0 × 0,9833 = 49,2; P50 90,0 × 0,9953 = 89,6; P90 150,0 × 1,0028 = 150,4. 2040: P10 70,0 × 0,9579 = 67,1; P50 140,0 × 0,9932 = 139,0; P90 250,0 × 1,0159 = 254,0. 2050: P10 100,0 × 0,9319 = 93,2; P50 193,0 × 0,9903 = 191,1; P90 400,0 × 1,0313 = 412,5.
- **Podrobné odvození, konzervativní:** Ze studie: nic. Vlastní krok a jiné zdroje: základ: domácnosti 15 GWh (1 % sektoru) + služby 45 GWh (3,3 % sektoru), úsudek. 2050 P50: 540 000 domácností × 30 % × 0,5 MWh = 81 + služby 8 % × 1 400 = 112; součet 193 GWh. Revize: y = d_chlazeni × s, kde s je řádek s dnešními vstupy a d_chlazeni je v tabulce řídicích vlivů (část 6). 2030: P10 50,0 × 0,9833 = 49,2; P50 85,0 × 0,9953 = 84,6; P90 140,0 × 1,0028 = 140,4. 2040: P10 60,0 × 0,9579 = 57,5; P50 120,0 × 0,9932 = 119,2; P90 220,0 × 1,0159 = 223,5. 2050: P10 80,0 × 0,9319 = 74,6; P50 160,0 × 0,9903 = 158,4; P90 350,0 × 1,0313 = 361,0.
- **Zdroj:** bez zdroje v Dopadové studii a ve Vnitrostátním plánu (nic nenalezeno); sektorové součty ERÚ, čtvrtletní zprávy 2025 Q1 až Q4, tab. 6.3, řádek MSK; ČSÚ, Projekce obyvatelstva v krajích ČR do roku 2080, kód 130052-24, 12.12.2024, Tab. 4_CZ080, řádek Počet obyvatel: celkem, https://csu.gov.cz/produkty/projekce-obyvatelstva-v-krajich-cr-do-roku-2080; ČSÚ, Základní výsledky SLDB 2021 Moravskoslezský kraj , s.17, s.22, s.79; https://scitani.gov.cz/velikost-hospodarici-domacnosti
- **Citace:** „Celkový počet hospodařících domácností v kraji dosáhl hodnoty 541 267. Ve srovnání s předchozím sčítáním v roce 2011 se jejich počet zvýšil o 33,7 tisíce, tj. o 6,6 %.“; scitani.gov.cz „Moravskoslezský kraj“ „541 276“ „2,12“; s.79 „Počet obyvatel 1 257 090 1 278 726 1 265 019 1 205 836 1 162 841“
- **Poznámka:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Dopadovou studii nelze použít: Studie chlazení neuvádí. Čistý úsudek, chlazení zdroje nečíslují. Počet domácností 540 000 sedí na SLDB 2021 (541 276). Zlepší: ČSÚ ENERGO, průzkum klimatizací. Hodnoty ve sloupcích jsou y včetně d_chlazeni, znovu nenásobit. Vliv d_chlazeni má stupeň D, viz řídicí vlivy (část 6).
- **Koeficient, progresivní:** zima P10 0.0000, P50 0.0494, P90 0.1976; léto P10 2.1606, P50 4.3213, P90 7.5622; flexibilní ne; stupeň D
- **Koeficient, konzervativní:** zima P10 0.0000, P50 0.0494, P90 0.1976; léto P10 2.1606, P50 4.3213, P90 7.5622; flexibilní ne; stupeň D
- **Koeficient, odvození:** Apriorní zima 0,00, 0,05, 0,20 × kalibrace 0,988; léto 2,00, 4,00, 7,00 × kalibrace 1,080. v zimě jen technologie, v létě slunečné poledne.
- **Koeficient, zdroj:** vlastní úsudek; Dopadová studie Tab.6 nečísluje chlazení
- **Koeficient, strana:** rov.5 a 6 s.74
- **Koeficient, citace:** „Roční maximum zatížení elektrizační soustavy za MSK se nesleduje.“
- **Koeficient, poznámka:** Hodnotu nepodporuje žádný zdroj. Horký týden může být nad P90.

#### osobní auta

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 6.0772 | 230.0 | 493.8 | 721.3 | 42.8 | 350.2 | D |
| konzervativní | 6.0772 | 59.5 | 187.6 | 502.4 | 24.0 | 105.1 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 22.5, P90 71.3; 2040 P10 126.6, P90 579.7
- **Meze 2030 a 2040, konzervativní:** 2030 P10 15.8, P90 40.0; 2040 P10 39.7, P90 302.9
- **Průběh:** plynule
- **Společný faktor:** elektrifikace
- **Řídicí vliv:** d_auta
- **Historické maximum tempa, GWh za rok:** 0.3259
- **Jak se došlo, progresivní:** 625 545 aut × 2,295 MWh na auto za rok = 1 435,6 GWh, × 50 % na baterie × 0,6879 úbytek obyvatel, více aut na osobu a účinnost = 493,8 GWh.
- **Jak se došlo, konzervativní:** 20 % z předchozí bateriové hodnoty progresivní cesty 938,2 GWh (1 363,8 × 0,6879) = 187,6 GWh.
- **Ze zdrojů, progresivní:** ČSÚ Statistická ročenka MSK 2025, tab. 17.1 (625 545 aut); Dopadová studie, s. 110 až 111 (13 500 km, 17 kWh/100 km); ČSÚ projekce obyvatel krajů; Krause et al. 2020, Tab. 4 a Tab. 6
- **Ze zdrojů, konzervativní:** ČSÚ Statistická ročenka MSK 2025, tab. 17.1 (625 545 aut); Dopadová studie, s. 110 až 111; ČSÚ projekce obyvatel krajů; Krause et al. 2020, Tab. 4 a Tab. 6
- **Odhad, progresivní:** 50 % je volba modelu (volba modelu č. 27), ne zdroj. Dorovnání aut na osobu na dnešní Česko a přenos účinnosti nových aut na celý park jsou úsudek.
- **Odhad, konzervativní:** 20 % je dáno definicí cesty, ne zdroj. 938,2 GWh stojí na úsudku 95 % aut na baterie a na odhadnutých vlivech.
- **Podrobné odvození, progresivní:** Ze studie: km, kWh, vozidla, 9,4 %. Vlastní krok a jiné zdroje: intenzita 13,5 tis. km × 17 kWh/100 km = 2,295 MWh. Základ 2 648 BEV × 2,295 = 6,0772. 2030: 119 000 až 330 000 × 9,4 %; P50 20 000 aut. Počet aut 625 545 včetně dodávkových (ČSÚ, 31.12.2024) místo 850 000 × 72 %. Bez vlivu 2050 P50: 625 545 × 95 % × 2,295 MWh = 1 363,8. Revize: y = d_auta × s, kde s je řádek s dnešními vstupy a d_auta je v tabulce řídicích vlivů (část 6). 2030: P10 25,7 × 0,8774 = 22,5; P50 45,9 × 0,9335 = 42,8; P90 71,2 × 1,0010 = 71,3. 2040: P10 287,1 × 0,6614 = 189,9; P50 646,0 × 0,8131 = 525,3; P90 861,4 × 1,0095 = 869,6. 2050: P10 1 004,9 × 0,4578 = 460,1; P50 1 363,8 × 0,6879 = 938,2; P90 1 435,6 × 1,0049 = 1 442,7. Revize vodík (volba modelu č. 27): 2030 beze změny, vodíkových aut je málo. 2040: třetina tehdy čistých aut jede na vodík, baterie je 2/3 z 287,1, 646,0 a 861,4; × 0,6614, 0,8131, 1,0095 = 126,6, 350,2, 579,7. 2050: plná flotila 625 545 × 2,295 MWh = 1 435,6; × 50 % = 717,8; × 0,6879 = 493,8. P10 35 % = 502,5 × 0,4578 = 230,0. P90 50 % = 717,8 × 1,0049 = 721,3. Nahrazuje 95 % výše.
- **Podrobné odvození, konzervativní:** Ze studie: km, kWh, vozidla, 9,4 %. Vlastní krok a jiné zdroje: 20 % × progresivní P50, nová čísla viz Revize. 2030: dolní mez plánu 119 000 × 9,4 % × 2,295 MWh. Revize: y = d_auta × s, kde s je řádek s dnešními vstupy a d_auta je v tabulce řídicích vlivů (část 6). 2030: P10 18,0 × 0,8774 = 15,8; P50 25,7 × 0,9335 = 24,0; P90 40,0 × 1,0010 = 40,0. 2040: P10 60,0 × 0,6614 = 39,7; P50 20 % × progresivní P50 525,3 = 105,1; P90 300,0 × 1,0095 = 302,9. 2050: P10 130,0 × 0,4578 = 59,5; P50 20 % × progresivní P50 938,2 = 187,6; P90 500,0 × 1,0049 = 502,4.
- **Zdroj, progresivní:** https://cdv.gov.cz/file/tz-nejvice-elektromobilu-je-v-praze-plynovych-aut-v-moravskoslezskem-kraji; Dopadová studie s.110-111; Vnitrostátní plán Tab.32 s.106, s.339; ČSÚ, Projekce obyvatelstva v krajích ČR do roku 2080, kód 130052-24, 12.12.2024, Tab. 4_CZ080, řádek Počet obyvatel: celkem, https://csu.gov.cz/produkty/projekce-obyvatelstva-v-krajich-cr-do-roku-2080; ČSÚ, Statistická ročenka Moravskoslezského kraje 2025, tab. 17.1, 17.102 a 27.102 (zdroj dat Ministerstvo dopravy), https://csu.gov.cz/produkty/statisticka-rocenka-moravskoslezskeho-kraje-2025; Krause et al., EU road vehicle energy consumption and CO2 emissions by 2050, Energy Policy 138 (2020) 111224, Tab.4 a Tab.6, doi 10.1016/j.enpol.2019.111224
- **Zdroj, konzervativní:** Definice cest (část 2); volba modelu č. 3; Vnitrostátní plán Tab.32; ČSÚ, Projekce obyvatelstva v krajích ČR do roku 2080, kód 130052-24, 12.12.2024, Tab. 4_CZ080, řádek Počet obyvatel: celkem, https://csu.gov.cz/produkty/projekce-obyvatelstva-v-krajich-cr-do-roku-2080; ČSÚ, Statistická ročenka Moravskoslezského kraje 2025, tab. 17.1, 17.102 a 27.102 (zdroj dat Ministerstvo dopravy), https://csu.gov.cz/produkty/statisticka-rocenka-moravskoslezskeho-kraje-2025; Krause et al., EU road vehicle energy consumption and CO2 emissions by 2050, Energy Policy 138 (2020) 111224, Tab.4 a Tab.6, doi 10.1016/j.enpol.2019.111224
- **Strana:** s.110-111
- **Citace:** očekávaný: 13,5 tis. km, „17 kWh / 100 km“, „850 tisíc vozidel“, „9,4 %“, „2,75 TWh“; tab. 17.1 „Osobní automobily včetně dodávkových | 600223 | 615713 | 625545“ (2022, 2023, 2024, k 31.12.); tab. 27.102 „Střední stav obyvatel“ Česko 10886531; tab. 27.3 „Střední stav obyvatel | osoby | 1187776 | 1190143 | 1184662“; tab. 17.102 „Česko / Czechia | 6638172“; Tab.4 „Small car 2015 (Baseline)“ 155 Wh/km, „Large Car 2015 (Baseline)“ 189 Wh/km; Tab.6 „Small Car 2050, Pessimistic“ 109, 0.30; „Small Car 2050, Optimistic“ 74, 0.52; „Large Car 2050, Pessimistic“ 135, 0.29; „Large Car 2050, Optimistic“ 96, 0.49
- **Poznámka, progresivní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Měřítko: 9,4 % = 850 000 / 9 mil. vozidel (s.111). Počet aut v MSK je změřený (ČSÚ, včetně dodávkových); 72 % vypadlo. Počet BEV je zřejmě z konce 2024. Základ je dělení z Dopravy, ačkoli domácí nabíjení je ve skutečnosti v Domácnostech. Tempo: Dopadová studie Tab.19 s.110, 2019 638,0, 2020 963,9 MWh; rozdíl 325,9 MWh = 0,3259 GWh/rok. Historie v Dopadové studii končí 9/2021 a je před rozjezdem trhu. Mimo Dopadovou studii: (2 648 − 487) BEV / 3,25 roku × 2,295 MWh = 1,526 GWh/rok, CDV, datum 2 648 nejisté. Hodnoty ve sloupcích jsou y včetně d_auta, znovu nenásobit. Vliv d_auta má stupeň D, viz řídicí vlivy (část 6). Podíl 50 % je volba modelu a nahradil 95 %. Spolu s vodíkem je tedy v P50 2050 100 % čistých aut. Vodíková část je v řádku výroba vodíku: osobní auta.
- **Poznámka, konzervativní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Procento lze použít čistě. Tempo: Dopadová studie Tab.19 s.110, 2019 638,0, 2020 963,9 MWh; rozdíl 325,9 MWh = 0,3259 GWh/rok. Historie v Dopadové studii končí 9/2021 a je před rozjezdem trhu. Mimo Dopadovou studii: (2 648 − 487) BEV / 3,25 roku × 2,295 MWh = 1,526 GWh/rok, CDV, datum 2 648 nejisté. Hodnoty ve sloupcích jsou y včetně d_auta, znovu nenásobit. Vliv d_auta má stupeň D, viz řídicí vlivy (část 6). Hodnoty beze změny. Cesta zůstává na bateriích a procento z definice cesty se vztahuje k předchozí bateriové hodnotě progresivní cesty (525,3 a 938,2), ne k nové 50% části.
- **Koeficient, progresivní:** zima P10 0.9882, P50 1.7788, P90 2.9646; léto P10 0.3241, P50 0.7562, P90 2.1606; flexibilní ne; stupeň D
- **Koeficient, konzervativní:** zima P10 0.9882, P50 1.7788, P90 2.9646; léto P10 0.3241, P50 0.7562, P90 2.1606; flexibilní ne; stupeň D
- **Koeficient, odvození:** Apriorní zima 1,00, 1,80, 3,00 × kalibrace 0,988; léto 0,30, 0,70, 2,00 × kalibrace 1,080. nabíjení po příjezdu domů; P10 řízené nabíjení, P90 léto nabíjení přes den.
- **Koeficient, zdroj:** Muratori 2018, Nature Energy 3, 193-201, DOI 10.1038/s41560-017-0074-z; arXiv 2112.04559
- **Koeficient, strana:** rov.5 a 6 s.74
- **Koeficient, citace:** „Roční maximum zatížení elektrizační soustavy za MSK se nesleduje.“
- **Koeficient, poznámka:** Zdroje potvrzují večerní shlukování, poměr k průměru neuvádějí. Číslo je úsudek.

#### nákladní doprava

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 4.2705 | 234.4 | 558.6 | 657.2 | 9.7 | 182.0 | D |
| konzervativní | 4.2705 | 112.5 | 268.1 | 600.0 | 7.8 | 81.9 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 4.8, P90 30.0; 2040 P10 56.7, P90 333.3
- **Meze 2030 a 2040, konzervativní:** 2030 P10 4.8, P90 20.0; 2040 P10 25.5, P90 200.0
- **Průběh:** plynule
- **Společný faktor:** elektrifikace
- **Řídicí vliv:** d_nakladni
- **Jak se došlo, progresivní:** (2,75 TWh vozidla ze studie − 1 435,6 GWh osobní auta) × 50 % na baterie × 0,85 úspornější nákladní auta = 558,6 GWh.
- **Jak se došlo, konzervativní:** 30 % z předchozí bateriové hodnoty progresivní cesty 893,8 GWh (1 051,5 × 0,85) = 268,1 GWh.
- **Ze zdrojů:** Dopadová studie, s. 111 (2,75 TWh); ČSÚ Statistická ročenka MSK 2025, tab. 17.1 (625 545 aut)
- **Odhad, progresivní:** 50 % je volba modelu (volba modelu č. 27), ne zdroj. 0,85 je úsudek bez zdroje. Dělení 2,75 TWh je náš dopočet.
- **Odhad, konzervativní:** 30 % je dáno definicí cesty, ne zdroj. 893,8 GWh stojí na úsudku 80 % na baterie a úsudku 0,85.
- **Podrobné odvození, progresivní:** Ze studie: 2,75 TWh. Vlastní krok a jiné zdroje: základ = reziduum: Doprava 54,8917 − auta 6,0772 − vlaky 25,08 − MHD 19,464 = 4,2705 GWh. 2050: studie 2,75 TWh − osobní 625 545 × 2,295 MWh = 2 750,0 − 1 435,6 = 1 314,4 GWh plné bateriové spotřeby; × 80 % baterie = 1 051,5, zbytek vodík. Revize: y = d_nakladni × s, kde s je řádek s dnešními vstupy a d_nakladni je v tabulce řídicích vlivů (část 6). 2030: P10 5,0 × 0,9500 = 4,8; P50 10,0 × 0,9700 = 9,7; P90 30,0 × 1,0000 = 30,0. 2040: P10 100,0 × 0,8500 = 85,0; P50 300,0 × 0,9100 = 273,0; P90 500,0 × 1,0000 = 500,0. 2050: P10 500,0 × 0,7500 = 375,0; P50 1 051,5 × 0,8500 = 893,8; P90 1 314,4 × 1,0000 = 1 314,4. Revize vodík (volba modelu č. 27): 2030 beze změny. 2040: 2/3 z 100, 300 a 500; × 0,85, 0,91, 1 = 56,7, 182,0, 333,3. 2050: 1 314,4 × 50 % = 657,2; × 0,85 = 558,6. P10: 657,2 × 500 / 1 051,5 = 312,5; × 0,75 = 234,4. P90: 657,2 × 1 = 657,2. Nahrazuje 80 % výše.
- **Podrobné odvození, konzervativní:** Ze studie: 2,75 TWh. Vlastní krok a jiné zdroje: 30 % × progresivní P50, nová čísla viz Revize. Revize: y = d_nakladni × s, kde s je řádek s dnešními vstupy a d_nakladni je v tabulce řídicích vlivů (část 6). 2030: P10 5,0 × 0,9500 = 4,8; P50 8,0 × 0,9700 = 7,8; P90 20,0 × 1,0000 = 20,0. 2040: P10 30,0 × 0,8500 = 25,5; P50 30 % × progresivní P50 273,0 = 81,9; P90 200,0 × 1,0000 = 200,0. 2050: P10 150,0 × 0,7500 = 112,5; P50 30 % × progresivní P50 893,8 = 268,1; P90 600,0 × 1,0000 = 600,0.
- **Zdroj, progresivní:** ERÚ, čtvrtletní zprávy 2025 Q1 až Q4, tab. 6.3, řádek MSK; Dopadová studie s.111; Vnitrostátní plán Tab.33 s.106; ČSÚ, Statistická ročenka Moravskoslezského kraje 2025, tab. 17.1, 17.102 a 27.102 (zdroj dat Ministerstvo dopravy), https://csu.gov.cz/produkty/statisticka-rocenka-moravskoslezskeho-kraje-2025; Le Corguillé, Hacker, Dolinga, Real-world data analysis of battery electric trucks operating in Germany, EVS38 (2025), https://www.oeko.de//fileadmin/oekodoc/Real-world-data-analysis-of-battery-electric-trucks-operating-in-Germany.pdf
- **Zdroj, konzervativní:** Definice cest (část 2); volba modelu č. 3; ČSÚ, Statistická ročenka Moravskoslezského kraje 2025, tab. 17.1, 17.102 a 27.102 (zdroj dat Ministerstvo dopravy), https://csu.gov.cz/produkty/statisticka-rocenka-moravskoslezskeho-kraje-2025; Le Corguillé, Hacker, Dolinga, Real-world data analysis of battery electric trucks operating in Germany, EVS38 (2025), https://www.oeko.de//fileadmin/oekodoc/Real-world-data-analysis-of-battery-electric-trucks-operating-in-Germany.pdf
- **Strana:** s.111
- **Citace:** očekávaný: „2,75 TWh“ pro celý vozový park; tab. 17.1 „Osobní automobily včetně dodávkových | 600223 | 615713 | 625545“ (2022, 2023, 2024, k 31.12.); tab. 27.102 „Střední stav obyvatel“ Česko 10886531; tab. 27.3 „Střední stav obyvatel | osoby | 1187776 | 1190143 | 1184662“; tab. 17.102 „Česko / Czechia | 6638172“; „The average consumption is 0.96 kWh/km.“; nic k vývoji v čase
- **Poznámka, progresivní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Dělení 2,75 TWh je dopočtené z počtu aut ČSÚ, který obsahuje i dodávky. Podíl 50 % je volba modelu a nahradil úsudek 80 %. Vodíková část je v řádku výroba vodíku: nákladní doprava. Hodnoty ve sloupcích jsou y včetně d_nakladni, znovu nenásobit. Vliv d_nakladni má stupeň D, viz řídicí vlivy (část 6).
- **Poznámka, konzervativní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Procento lze použít čistě. Hodnoty ve sloupcích jsou y včetně d_nakladni, znovu nenásobit. Vliv d_nakladni má stupeň D, viz řídicí vlivy (část 6). Hodnoty beze změny. Cesta zůstává na bateriích a procento z definice cesty se vztahuje k předchozí bateriové hodnotě progresivní cesty (273,0 a 893,8), ne k nové 50% části.
- **Koeficient, progresivní:** zima P10 0.6918, P50 1.0870, P90 1.5811; léto P10 0.4321, P50 0.7562, P90 1.2964; flexibilní ne; stupeň D
- **Koeficient, konzervativní:** zima P10 0.6918, P50 1.0870, P90 1.5811; léto P10 0.4321, P50 0.7562, P90 1.2964; flexibilní ne; stupeň D
- **Koeficient, odvození:** Apriorní zima 0,70, 1,10, 1,60 × kalibrace 0,988; léto 0,40, 0,70, 1,20 × kalibrace 1,080. depa a noční nabíjení.
- **Koeficient, zdroj:** vlastní úsudek
- **Koeficient, strana:** rov.5 a 6 s.74
- **Koeficient, citace:** „Roční maximum zatížení elektrizační soustavy za MSK se nesleduje.“
- **Koeficient, poznámka:** Hodnotu nepodporuje žádný zdroj.

#### vlaky

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 25.08 | 37.6 | 37.6 | 111.1 | 37.6 | 37.6 | B |
| konzervativní | 25.08 | 30 | 35.7 | 100 | 35.7 | 35.7 | B |

- **Meze 2030 a 2040, progresivní:** 2030 P10 25.1, P90 60; 2040 P10 37.6, P90 90
- **Meze 2030 a 2040, konzervativní:** 2030 P10 25.1, P90 55; 2040 P10 30, P90 80
- **Průběh:** plynule
- **Společný faktor:** elektrifikace
- **Jak se došlo, progresivní:** Spotřeba ze studie od roku 2027, 37 620 MWh, držená do 2050 = 37,6 GWh.
- **Jak se došlo, konzervativní:** 95 % z progresivní hodnoty 37,62 GWh = 35,7 GWh.
- **Ze zdrojů:** Dopadová studie, Tab. 24 s. 118
- **Odhad, progresivní:** Žádné číslo. Držení do 2050 je naše volba.
- **Odhad, konzervativní:** 95 % je dáno definicí cesty, ne zdroj.
- **Podrobné odvození, progresivní:** Ze studie: 25,08 a 37,62 GWh. Vlastní krok a jiné zdroje: základ 25 080 MWh, Tab.24. 2030: 37 620 MWh + elektrizace. P50 37,62 drženo. P90: 1 219 857 MWh × 12,05 % = 146,9; 37,62 + 50 % × 146,9 = 111,1.
- **Podrobné odvození, konzervativní:** Ze studie: 25,08 a 37,62 GWh. Vlastní krok a jiné zdroje: 95 % × 37,62 = 35,739.
- **Zdroj, progresivní:** Dopadová studie Tab.24 s.117-118; https://www.spravazeleznic.cz (tendr 1 219 857 MWh, jen souhrn vyhledávače, stránka neotevřena); ERÚ, čtvrtletní zprávy 2025 Q1 až Q4, tab. 6.3, řádek MSK
- **Zdroj, konzervativní:** Dopadová studie Tab.24 s.117-118; https://www.spravazeleznic.cz (tendr 1 219 857 MWh, jen souhrn vyhledávače, stránka neotevřena); ERÚ, čtvrtletní zprávy 2025 Q1 až Q4, tab. 6.3, řádek MSK; definice cest (část 2)
- **Strana:** Tab.24 s.118
- **Citace:** očekávaný: 25 080 (2025), 37 620 od 2027 [MWh]; „značně zkreslené“
- **Poznámka, progresivní:** Řádek počítá jen osobní dopravu v závazku a nárůst. Nákladní a komerční železnice není v Dopravě tab. 6.3 vidět, studie sama píše „značně zkreslené“. Zlepší: dodávky do měníren Správy železnic v MSK.
- **Poznámka, konzervativní:** Procento lze použít čistě.
- **Koeficient, progresivní:** zima P10 0.9882, P50 1.3835, P90 1.7788; léto P10 0.6482, P50 0.8643, P90 1.0803; flexibilní ne; stupeň D
- **Koeficient, konzervativní:** zima P10 0.9882, P50 1.3835, P90 1.7788; léto P10 0.6482, P50 0.8643, P90 1.0803; flexibilní ne; stupeň D
- **Koeficient, odvození:** Apriorní zima 1,00, 1,40, 1,80 × kalibrace 0,988; léto 0,60, 0,80, 1,00 × kalibrace 1,080. špička přepravy a topení.
- **Koeficient, zdroj:** vlastní úsudek
- **Koeficient, strana:** rov.5 a 6 s.74
- **Koeficient, citace:** „Roční maximum zatížení elektrizační soustavy za MSK se nesleduje.“
- **Koeficient, poznámka:** Hodnotu nepodporuje žádný zdroj.

#### MHD

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 19.464 | 11.9 | 11.9 | 33.9 | 22.8 | 17.8 | D |
| konzervativní | 19.464 | 15 | 19.0 | 65 | 19.0 | 19.0 | B |

- **Meze 2030 a 2040, progresivní:** 2030 P10 19.5, P90 30; 2040 P10 17.8, P90 45.0
- **Meze 2030 a 2040, konzervativní:** 2030 P10 15, P90 26; 2040 P10 15, P90 50
- **Průběh:** plynule
- **Společný faktor:** elektrifikace
- **Jak se došlo, progresivní:** 50 % z 23,702 GWh spotřeby ze studie = 11,9 GWh.
- **Jak se došlo, konzervativní:** 80 % z 23,702 GWh bateriové hodnoty progresivní cesty = 19,0 GWh.
- **Ze zdrojů:** Dopadová studie, Tab. 23 s. 116
- **Odhad, progresivní:** 50 % je volba modelu (volba modelu č. 27), ne zdroj. Bere se z celého řádku včetně tramvají, proto hodnota klesá pod dnešek.
- **Odhad, konzervativní:** 80 % je dáno definicí cesty, ne zdroj. Výsledek je pod dnešními 19,464 GWh.
- **Podrobné odvození, progresivní:** Ze studie: 19,464 a 23,702 GWh. Vlastní krok a jiné zdroje: základ 19 464 MWh (Tab.23, 2025). 2030 až 2050 P50: 23 702 MWh. P90 2050: 23,702 + 40 mil. km × 1,1 kWh/km = 67,7. Revize vodík (volba modelu č. 27): 2030: 23,702 − 800 000 km × 1,1 kWh/km = 22,822, protože Dopadová studie s.116 počítá 10 vodíkových vozidel v Tab.23. 2040: 75 % z 23,702 a z 60 = 17,8, 45,0. 2050: 50 % z 23,702 a z 67,702 = 11,9, 33,9.
- **Podrobné odvození, konzervativní:** Ze studie: 19,464 a 23,702 GWh. Vlastní krok a jiné zdroje: 80 % × 23,702 = 18,9616.
- **Zdroj, progresivní:** Dopadová studie Tab.23 s.115-116
- **Zdroj, konzervativní:** Dopadová studie Tab.23; definice cest (část 2)
- **Strana:** Tab.23 s.116
- **Citace:** očekávaný: 19 464 (2025), 23 702 (2030 až 2050) [MWh]
- **Poznámka, progresivní:** Řádek zahrnuje MHD i linkové autobusy. P50 je z Tab.23 a plnou elektrifikaci z definice cest neobsahuje, ta je jen v P90; 40 mil. km je úsudek bez zdroje. Zlepší: výkony od Odboru dopravy MSK a DPO. Podíl 50 % je volba modelu, podíl 2040 je úsudek. Řádek obsahuje tramvaje, 50 % se bere z celého řádku a P50 2050 proto klesá pod základ 19,464. Je to záměrné zjednodušení. Vodíková část je v řádku výroba vodíku: MHD.
- **Poznámka, konzervativní:** 80 % z Tab.23 je pod základem 19,464 GWh, tedy méně než dnes. Doslovné čtení ponecháno; alternativa je držet základ. Hodnoty beze změny. Cesta zůstává na bateriích a procento z definice cesty se vztahuje k předchozí bateriové hodnotě progresivní cesty (23,702), ne k nové 50% části.
- **Koeficient, progresivní:** zima P10 1.0870, P50 1.5811, P90 2.1741; léto P10 0.4321, P50 0.6482, P90 0.9723; flexibilní ne; stupeň D
- **Koeficient, konzervativní:** zima P10 1.0870, P50 1.5811, P90 2.1741; léto P10 0.4321, P50 0.6482, P90 0.9723; flexibilní ne; stupeň D
- **Koeficient, odvození:** Apriorní zima 1,10, 1,60, 2,20 × kalibrace 0,988; léto 0,40, 0,60, 0,90 × kalibrace 1,080. večerní špička, topení, víkendový jízdní řád.
- **Koeficient, zdroj:** vlastní úsudek
- **Koeficient, strana:** rov.5 a 6 s.74
- **Koeficient, citace:** „Roční maximum zatížení elektrizační soustavy za MSK se nesleduje.“
- **Koeficient, poznámka:** Hodnotu nepodporuje žádný zdroj.

#### datacentra

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 0 | 150 | 700.8 | 1401.6 | 40 | 361.4 | D |
| konzervativní | 0 | 35.0 | 70.1 | 140.2 | 4.0 | 36.1 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 0, P90 216.8; 2040 P10 100, P90 841.0
- **Meze 2030 a 2040, konzervativní:** 2030 P10 2.0, P90 8.0; 2040 P10 18.1, P90 72.3
- **Průběh:** plynule
- **Společný faktor:** povolovani
- **Jak se došlo, progresivní:** 100 MW × 80 % využití × 8 760 h za rok = 700,8 GWh.
- **Jak se došlo, konzervativní:** 10 % z progresivní hodnoty 700,8 GWh = 70,1 GWh.
- **Ze zdrojů:** cc.cz 24. 7. 2026 (80 až 120 MW, názor autora, ne projekt)
- **Odhad, progresivní:** 100 MW a 80 % jsou úsudek. V kraji není známý projekt s výkonem.
- **Odhad, konzervativní:** 10 % je dáno definicí cesty. Progresivní hodnota je úsudek.
- **Podrobné odvození, progresivní:** Ze studie: nic. Vlastní krok a jiné zdroje: základ 0. 2030 P90: 1,8 TWh × 12,05 % = 216,8. 2040 P50: 3 TWh × 12,05 % = 361,4. 2050 P50: 100 MW × 80 % × 8 760 h = 700,8; P90: 200 MW × 80 % × 8 760 h = 1 401,6.
- **Podrobné odvození, konzervativní:** Ze studie: nic. Vlastní krok a jiné zdroje: 10 % × progresivní P50; P10 5 %, P90 20 %. 2050: 70,1.
- **Zdroj, progresivní:** https://zpravy.kurzy.cz/862356-vysoke-ceny-energii-zabrzdi-podle-egu-plany-na-vystavbu-az-40--datovych-center-v-cr/ (EGU, souhrn); https://cc.cz/necekany-pohled-na-umirajici-ocelarnu-v-cesku-ma-neco-extra-cenneho-a-muze-z-ni-byt-obri-datacentrum/ (24.7.2026, 80 až 120 MW, názor autora); Dopadová studie a Vnitrostátní plán nic
- **Zdroj, konzervativní:** https://zpravy.kurzy.cz/862356-vysoke-ceny-energii-zabrzdi-podle-egu-plany-na-vystavbu-az-40--datovych-center-v-cr/ (EGU, souhrn); https://cc.cz/necekany-pohled-na-umirajici-ocelarnu-v-cesku-ma-neco-extra-cenneho-a-muze-z-ni-byt-obri-datacentrum/ (24.7.2026, 80 až 120 MW, názor autora); Dopadová studie a Vnitrostátní plán nic; definice cest (část 2)
- **Poznámka, progresivní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Dopadovou studii nelze použít: Studie datacentra neuvádí. Základ 0: existující provozy nejsou zvlášť známy a zůstávají ve službách. Měřítko je podíl MSK na spotřebě ČR 12,05 % (tab. 6.3). V MSK nebyl nalezen projekt s výkonem a stavem, proto plynule, ne skok. Největší nejistota mezi novými zátěžemi.
- **Poznámka, konzervativní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Dopadovou studii nelze použít: Studie datacentra neuvádí. Procento lze použít čistě.
- **Koeficient, progresivní:** zima P10 0.9388, P50 0.9882, P90 1.0376; léto P10 1.0263, P50 1.1127, P90 1.1884; flexibilní ne; stupeň D
- **Koeficient, konzervativní:** zima P10 0.9388, P50 0.9882, P90 1.0376; léto P10 1.0263, P50 1.1127, P90 1.1884; flexibilní ne; stupeň D
- **Koeficient, odvození:** Apriorní zima 0,95, 1,00, 1,05 × kalibrace 0,988; léto 0,95, 1,03, 1,10 × kalibrace 1,080. plochý provoz, v létě víc chlazení.
- **Koeficient, zdroj:** vlastní úsudek
- **Koeficient, strana:** rov.5 a 6 s.74
- **Koeficient, citace:** „Roční maximum zatížení elektrizační soustavy za MSK se nesleduje.“
- **Koeficient, poznámka:** Hodnotu nepodporuje žádný zdroj.

#### výroba vodíku

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 0 | 20 | 45.8 | 260.4 | 17.1 | 37.4 | B |
| konzervativní | 0 | 5 | 13.7 | 140 | 5.1 | 11.2 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 6.1, P90 34.8; 2040 P10 20, P90 150
- **Meze 2030 a 2040, konzervativní:** 2030 P10 3, P90 17.1; 2040 P10 5, P90 40
- **Průběh:** plynule
- **Společný faktor:** elektrifikace
- **Jak se došlo, progresivní:** 45 760 MWh ze studie = 45,8 GWh.
- **Jak se došlo, konzervativní:** 30 % z progresivní hodnoty 45,8 GWh = 13,7 GWh.
- **Ze zdrojů:** Dopadová studie, s. 119 a Tab. 25
- **Odhad, progresivní:** Žádné naše číslo. Studie neuvádí, pro koho výroba je, překryv s vodíkem pro vozidla nelze vyloučit.
- **Odhad, konzervativní:** 30 % je úsudek. Pro vodík není zadané, přebráno z nákladní dopravy.
- **Podrobné odvození, progresivní:** Ze studie: Tab.25 a 45 760 MWh. Vlastní krok a jiné zdroje: 2030: Tab.25 malá 6 105, střední 17 050, velká 34 815 MWh. 2040 P50: 17,05 + 10/3 × 6,105 = 37,4. 2050 P50: 45 760 MWh. Výpočet 45 760 ve studii není rozepsán, sedí 3 025 + 7 × 6 105 = 45 760, tedy malá varianta Tab.25. P90: stejný postup s velkou variantou, 16 665 + 7 × 34 815 = 260 370 MWh = 260,4.
- **Podrobné odvození, konzervativní:** Ze studie: Tab.25 a 45 760 MWh. Vlastní krok a jiné zdroje: 30 % × progresivní P50 (jako nákladní doprava) = 13,7.
- **Zdroj, progresivní:** Dopadová studie Tab.25 s.119; Vnitrostátní plán s.44, s.346
- **Zdroj, konzervativní:** Dopadová studie Tab.25 s.119; Vnitrostátní plán s.44, s.346; definice cest (část 2)
- **Strana:** Tab.25 s.119; s.119
- **Citace:** očekávaný: Tab.25 2030 6105, 17050, 34815 MWh; „45 760 MWh“ (2050); „6 105 MWh“ co 3 roky; 55 MWh/t
- **Poznámka, progresivní:** Základ 0: elektrolyzéry v MSK od 2027 podle Tab.25. Dřívější P90 551,5 vycházelo z 64 PJ vodíku v dopravě (Vnitrostátní plán), to je vodík pro flotilu a teď by se počítal dvakrát, proto je nahrazeno. Dopadová studie neuvádí, pro koho je 45 760 MWh, a odkaz [45] v Dopadové studii vede na nesouvisející dokument. Řádek zůstává jako vodík mimo flotilu, překryv s flotilou nelze vyloučit a nejvýš je to 45,8 GWh. Studie neuvádí, která varianta Tab.25 vstupuje do předpovědi, střední pro P50 2030 je volba modelu, P50 2050 je číslo studie a sedí na malou variantu.
- **Poznámka, konzervativní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Procento pro vodík není zadané, přebráno z nákladní dopravy.
- **Koeficient, progresivní:** zima P10 0.0000, P50 0.0000, P90 0.3000; léto P10 2.1900, P50 2.9200, P90 4.3800; flexibilní ano; stupeň D
- **Koeficient, konzervativní:** zima P10 0.0000, P50 0.0000, P90 0.3000; léto P10 2.1900, P50 2.9200, P90 4.3800; flexibilní ano; stupeň D
- **Koeficient, odvození:** Zima vypnuto, sklad přečká špičku. Léto: běh na plný výkon, koef = 8 760 / plné hodiny: 4 000 h = 2,19, 3 000 h = 2,92, 2 000 h = 4,38.
- **Koeficient, zdroj:** NATO ENSEC COE, Hydrogen as Fuel: Production and Costs (3 000 až 4 000 h), https://old2.enseccoe.org/en/newsroom/hydrogen-as-fuel-production-and-costs/473; arXiv 2208.07302 (1 600 až 2 860 h, alkalické); Dopadová studie s.119
- **Koeficient, strana:** s.119
- **Koeficient, citace:** studie hodiny elektrolyzéru neuvádí
- **Koeficient, poznámka:** Hodiny v MSK nejsou změřené. Koeficient udává potřebný výkon, ne přebytek, ten počítá kontrolní tabulka.

#### výroba vodíku: osobní auta

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 0 | 824.2 | 1494.6 | 2295.2 | 0.9 | 549.3 | D |
| konzervativní | 0 | 0 | 0 | 0 | 0 | 0 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 0.0, P90 3.5; 2040 P10 229.2, P90 818.0
- **Meze 2030 a 2040, konzervativní:** 2030 P10 0, P90 0; 2040 P10 0, P90 0
- **Průběh:** plynule
- **Společný faktor:** elektrifikace
- **Jak se došlo, progresivní:** 625 545 aut × 0,8449 obyvatelé × 1,1548 aut na osobu × 50 % × 13 500 km × 1,00 kg/100 km × 0,705 účinnost = 29 044,5 t vodíku × (48,26 výroba + 3,2 stlačení) kWh/kg = 1 494,6 GWh.
- **Jak se došlo, konzervativní:** Konzervativní cesta zůstává na bateriích, proto 0 GWh.
- **Ze zdrojů, progresivní:** ČSÚ Statistická ročenka MSK 2025, tab. 17.1 (625 545 aut); ČSÚ projekce obyvatel krajů; Dopadová studie, s. 110 až 111 (13 500 km); Krause et al. 2020, Tab. 4 a Tab. 6; IEA Global Hydrogen Review 2024 (48,26 kWh/kg); US DOE záznam 9013
- **Ze zdrojů, konzervativní:** žádný (volba modelu č. 27)
- **Odhad, progresivní:** 50 % je volba modelu (volba modelu č. 27). 1,00 kg/100 km, dorovnání aut na osobu a dosažení 48,26 kWh/kg až v 2050 jsou úsudek.
- **Odhad, konzervativní:** Žádné číslo, jen rozhodnutí cesty.
- **Podrobné odvození, progresivní:** 2030: NAP CM (4 000 + 1 200) × 9,4 % = 488,8 aut je P90, P50 je čtvrtina = 122,2, P10 nula. 122,2 × 13 500 km × 0,941 kg/100 km = 15,5 t; × 55,20 kWh/kg = 0,9 GWh. 2040: 625 545 × 0,9040 (pop_msk) × 1,0929 (auta_na_os) × 15,0 % = 92 704 aut; × 13 500 km × 1,00 kg/100 km × 0,823 (eff_auta) = 10 299,9 t; × (50,13 + 3,2) kWh/kg = 549,3 GWh. 2050: 625 545 × 0,8449 (pop_msk) × 1,1548 (auta_na_os) × 50,0 % = 305 169 aut; × 13 500 km × 1,00 kg/100 km × 0,705 (eff_auta) = 29 044,5 t; × (48,26 + 3,2) kWh/kg = 1 494,6 GWh.
- **Podrobné odvození, konzervativní:** Nula. Konzervativní cesta zůstává na bateriích.
- **Zdroj, progresivní:** Dopadová studie s.119 (55 MWh/t); US DOE, Technical Targets for Proton Exchange Membrane Electrolysis, https://www.energy.gov/eere/fuelcells/technical-targets-proton-exchange-membrane-electrolysis; IEA, Global Hydrogen Review 2024, Assumptions Annex, tabulka Hydrogen, https://iea.blob.core.windows.net/assets/36017d2f-747b-4993-b06d-33209fe143fa/GHR24AssumptionsAnnex.pdf; US DOE Hydrogen Program Record 9013 (2009), https://www.hydrogen.energy.gov/pdfs/9013_energy_requirements_for_hydrogen_gas_compression.pdf; Vnitrostátní plán tištěná s.107 (NAP CM); volba modelu č. 27; Dopadová studie s.110-111 (13,5 tis. km); ČSÚ, Statistická ročenka Moravskoslezského kraje 2025, tab. 17.1, https://csu.gov.cz/produkty/statisticka-rocenka-moravskoslezskeho-kraje-2025; Krause et al., Energy Policy 138 (2020) 111224, Tab.4 a Tab.6; https://h2.live/en/fuelcell-cars/toyota-mirai/
- **Zdroj, konzervativní:** volba modelu č. 27; definice cest (část 2)
- **Strana, progresivní:** s.110-111; s.119
- **Strana, konzervativní:** s.119
- **Citace, progresivní:** Dopadová studie s.119 „pro výrobu jedné tuny vodíku je zapotřebí 55 MWh elektrické energie“; DOE PEM „System, Energy Efficiency“ „55 (61%)“ (2022), „51 (65%)“ (2026), „46 (72%)“ (konečný cíl); IEA „Efficiency (LHV)“ „66%“ (2023), „69%“ (NZE 2030); DOE 9013 „2.23 and 3.0 kWh/kg H2 for compression to 440 bar and 880 bar“, „0.2 kWh/kg H2 for cooling“, „average compression energy of 3.1 kWh/kg H2“, „(1.7-6.4 kWh/kg H2)“, „2 to 4 kWh/kg H2“; Vnitrostátní plán „NAP CM počítá s v roce 2030 s možným nasazením 4 000 osobních automobilů na vodík, 1 200 lehkých užitkových automobilů, 250 autobusů, 600 nákladních vozidel“; tab. 17.1 „Osobní automobily včetně dodávkových | 600223 | 615713 | 625545“; Krause Tab.4 „Baseline 2050 Vehicle Specifications used for BEV and FCHEV“; h2.live „0.76 kg/100 km“
- **Citace, konzervativní:** Dopadová studie s.119 „Využití vodíku v osobní dopravě a železniční dopravě zatím nenabírá velkých obrátek“
- **Poznámka, progresivní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Sloupec ridic je prázdný, protože d_auta a d_nakladni jsou odvozené pro bateriové řádky. Vlivy jsou v odvození vypsané a hodnoty je už obsahují. Spotřeba 1,0 kg/100 km je úsudek mezi udávanými 0,76 (h2.live) a 0,79 až 0,89 (WLTP) a skutečnými asi 1,1; WLTP a 1,1 jsou známy jen ze souhrnu vyhledávače, stránky nešly otevřít. Zlepšení do 2050 bere eff_auta, protože Krause Tab.4 a Tab.6 platí pro BEV i FCHEV. Podíl vodíku 2040 je třetina tehdy čistých aut, úsudek. Podíl 50 % je volba modelu a dává 100 % čistých aut místo dřívějších 95 %. Vnitrostátní plán, tištěná s.46 očekává, že u osobních aut převáží elektromobilita. Dopadová studie s.119 píše, že v osobní dopravě jsou tyto projekty utlumovány. Elektrolyzér kWh/kg: dnes 55 (Dopadová studie, DOE stav 2022). 2030 P50 52 je úsudek mezi 55 a cílem DOE 51; P10 33,3 / 0,69 = 48,26 (IEA NZE 2030). 2050 P50 48,26 je tatáž hodnota dosažená později, P10 46 konečný cíl DOE, P90 55 bez zlepšení jako Dopadová studie. 2040 je polovina cesty. Komprese se nezlepšuje, záznam DOE 9013 je z roku 2009. Meze skládají vstupy jako nezávislé, stejně jako oddíl 12 poznámek.
- **Poznámka, konzervativní:** Nula z rozhodnutí o cestě, ne z měření. Řádek existuje, protože stránka čeká obě cesty.
- **Koeficient, progresivní:** zima P10 0.0000, P50 0.0000, P90 0.3000; léto P10 2.1900, P50 2.9200, P90 4.3800; flexibilní ano; stupeň D
- **Koeficient, konzervativní:** zima P10 0.0000, P50 0.0000, P90 0.3000; léto P10 2.1900, P50 2.9200, P90 4.3800; flexibilní ano; stupeň D
- **Koeficient, odvození:** Zima vypnuto, sklad přečká špičku. Léto: běh na plný výkon, koef = 8 760 / plné hodiny: 4 000 h = 2,19, 3 000 h = 2,92, 2 000 h = 4,38.
- **Koeficient, zdroj:** NATO ENSEC COE, Hydrogen as Fuel: Production and Costs (3 000 až 4 000 h), https://old2.enseccoe.org/en/newsroom/hydrogen-as-fuel-production-and-costs/473; arXiv 2208.07302 (1 600 až 2 860 h, alkalické); Dopadová studie s.119
- **Koeficient, strana:** s.119
- **Koeficient, citace:** studie hodiny elektrolyzéru neuvádí
- **Koeficient, poznámka:** Hodiny v MSK nejsou změřené. Koeficient udává potřebný výkon, ne přebytek, ten počítá kontrolní tabulka.

#### výroba vodíku: nákladní doprava

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 0 | 884.5 | 1925.0 | 2958.5 | 4.0 | 325.2 | D |
| konzervativní | 0 | 0 | 0 | 0 | 0 | 0 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 0.0, P90 16.3; 2040 P10 106.3, P90 620.8
- **Meze 2030 a 2040, konzervativní:** 2030 P10 0, P90 0; 2040 P10 0, P90 0
- **Průběh:** plynule
- **Společný faktor:** elektrifikace
- **Jak se došlo, progresivní:** 1 314,4 GWh / 1,3187 kWh/km × 50 % × 9,00 kg/100 km × 0,850 úspora = 38 125,9 t vodíku × (48,26 výroba + 2,23 stlačení) kWh/kg = 1 925,0 GWh.
- **Jak se došlo, konzervativní:** Konzervativní cesta zůstává na bateriích, proto 0 GWh.
- **Ze zdrojů, progresivní:** Dopadová studie, s. 111 (2,75 TWh); Oeko 2025 (1,3187 kWh/km); ICCT 2022 (9 kg/100 km, jen souhrn vyhledávače); IEA Global Hydrogen Review 2024 (48,26 kWh/kg); US DOE záznam 9013
- **Ze zdrojů, konzervativní:** žádný (volba modelu č. 27)
- **Odhad, progresivní:** 50 % je volba modelu (volba modelu č. 27). 0,850 a dosažení 48,26 kWh/kg až v 2050 jsou úsudek. Počet nákladních aut v kraji neznáme, kilometry jsou dopočtené.
- **Odhad, konzervativní:** Žádné číslo, jen rozhodnutí cesty.
- **Podrobné odvození, progresivní:** Vozokilometry nejsou v řádku přímo: 1 314,4 GWh plné bateriové spotřeby / 1,3187 kWh/km = 996,8 mil. km. 1,3187 = 0,96 + 0,183 × (40 − 20,4) / 10 podle Oeko, aby spotřeba bateriového auta odpovídala 40t soupravě, ke které patří 9 kg/100 km. 2030: NAP CM 600 × 9,4 % = 56,4 aut je P90, P50 je čtvrtina = 14,1, P10 nula. 14,1 × 60 000 km × 8,73 kg/100 km = 73,9 t; × 54,23 kWh/kg = 4,0 GWh. 2040: 996,8 mil. km × 7,61 % = 75,8 mil. km; × 9,00 kg/100 km × 0,910 (eff_nakladni) = 6 210,8 t; × (50,13 + 2,23) kWh/kg = 325,2 GWh. 2050: 996,8 mil. km × 50,00 % = 498,4 mil. km; × 9,00 kg/100 km × 0,850 (eff_nakladni) = 38 125,9 t; × (48,26 + 2,23) kWh/kg = 1 925,0 GWh.
- **Podrobné odvození, konzervativní:** Nula. Konzervativní cesta zůstává na bateriích.
- **Zdroj, progresivní:** Dopadová studie s.119 (55 MWh/t); US DOE, Technical Targets for Proton Exchange Membrane Electrolysis, https://www.energy.gov/eere/fuelcells/technical-targets-proton-exchange-membrane-electrolysis; IEA, Global Hydrogen Review 2024, Assumptions Annex, tabulka Hydrogen, https://iea.blob.core.windows.net/assets/36017d2f-747b-4993-b06d-33209fe143fa/GHR24AssumptionsAnnex.pdf; US DOE Hydrogen Program Record 9013 (2009), https://www.hydrogen.energy.gov/pdfs/9013_energy_requirements_for_hydrogen_gas_compression.pdf; Vnitrostátní plán tištěná s.107 (NAP CM); volba modelu č. 27; Dopadová studie s.111; Le Corguillé, Hacker, Dolinga, Real-world data analysis of battery electric trucks operating in Germany, EVS38 (2025), https://www.oeko.de//fileadmin/oekodoc/Real-world-data-analysis-of-battery-electric-trucks-operating-in-Germany.pdf; ICCT, Fuel-cell tractor-trailers: technology and fuel, 2022, https://theicct.org/publication/fuel-cell-tractor-trailer-tech-fuel-jul22/; Gebrüder Weiss a Hyundai XCIENT, https://www.hydronews.it/en/gebruder-weiss-positive-first-year-use-of-hydrogen-hyundai-xcient-fuel-cell/
- **Zdroj, konzervativní:** volba modelu č. 27; definice cest (část 2)
- **Strana, progresivní:** s.111; s.119
- **Strana, konzervativní:** s.119
- **Citace, progresivní:** Dopadová studie s.119 „pro výrobu jedné tuny vodíku je zapotřebí 55 MWh elektrické energie“; DOE PEM „System, Energy Efficiency“ „55 (61%)“ (2022), „51 (65%)“ (2026), „46 (72%)“ (konečný cíl); IEA „Efficiency (LHV)“ „66%“ (2023), „69%“ (NZE 2030); DOE 9013 „2.23 and 3.0 kWh/kg H2 for compression to 440 bar and 880 bar“, „0.2 kWh/kg H2 for cooling“, „average compression energy of 3.1 kWh/kg H2“, „(1.7-6.4 kWh/kg H2)“, „2 to 4 kWh/kg H2“; Vnitrostátní plán „NAP CM počítá s v roce 2030 s možným nasazením 4 000 osobních automobilů na vodík, 1 200 lehkých užitkových automobilů, 250 autobusů, 600 nákladních vozidel“; Oeko „The average consumption is 0.96 kWh/km.“; „If the vehicle weight is increased by 10 tonnes, consumption increases by an average of 0.183 kWh/km.“; hydronews „7.5 kg of H2“, „has travelled 70,000 km“ (leden 2021 až březen 2022)
- **Citace, konzervativní:** Dopadová studie s.119 „Využití vodíku v osobní dopravě a železniční dopravě zatím nenabírá velkých obrátek“
- **Poznámka, progresivní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Sloupec ridic je prázdný, protože d_auta a d_nakladni jsou odvozené pro bateriové řádky. Vlivy jsou v odvození vypsané a hodnoty je už obsahují. Počet nákladních aut v MSK není znám, proto vozokilometry z řádku nákladní doprava. Hodnota ICCT 9 kg/100 km dnes a +20 % při plném nákladu jsou jen ze souhrnu vyhledávače, stránka vrací 403, a je to model, ne měření. ICCT čeká 6,6 až 6,7 kg/100 km už v 2030, řádek bere 7,65 v 2050, aby seděl s eff_nakladni. P90 zahrnuje i čtení 0,96 kWh/km, tedy 1 369,2 mil. km. Nájezd 60 000 km je úsudek z 70 000 km za asi 14 měsíců. Čtvrtina NAP CM v 2030 je úsudek. Podíl 50 % je volba modelu. Elektrolyzér kWh/kg: dnes 55 (Dopadová studie, DOE stav 2022). 2030 P50 52 je úsudek mezi 55 a cílem DOE 51; P10 33,3 / 0,69 = 48,26 (IEA NZE 2030). 2050 P50 48,26 je tatáž hodnota dosažená později, P10 46 konečný cíl DOE, P90 55 bez zlepšení jako Dopadová studie. 2040 je polovina cesty. Komprese se nezlepšuje, záznam DOE 9013 je z roku 2009. Meze skládají vstupy jako nezávislé, stejně jako oddíl 12 poznámek.
- **Poznámka, konzervativní:** Nula z rozhodnutí o cestě, ne z měření. Řádek existuje, protože stránka čeká obě cesty.
- **Koeficient, progresivní:** zima P10 0.0000, P50 0.0000, P90 0.3000; léto P10 2.1900, P50 2.9200, P90 4.3800; flexibilní ano; stupeň D
- **Koeficient, konzervativní:** zima P10 0.0000, P50 0.0000, P90 0.3000; léto P10 2.1900, P50 2.9200, P90 4.3800; flexibilní ano; stupeň D
- **Koeficient, odvození:** Zima vypnuto, sklad přečká špičku. Léto: běh na plný výkon, koef = 8 760 / plné hodiny: 4 000 h = 2,19, 3 000 h = 2,92, 2 000 h = 4,38.
- **Koeficient, zdroj:** NATO ENSEC COE, Hydrogen as Fuel: Production and Costs (3 000 až 4 000 h), https://old2.enseccoe.org/en/newsroom/hydrogen-as-fuel-production-and-costs/473; arXiv 2208.07302 (1 600 až 2 860 h, alkalické); Dopadová studie s.119
- **Koeficient, strana:** s.119
- **Koeficient, citace:** studie hodiny elektrolyzéru neuvádí
- **Koeficient, poznámka:** Hodiny v MSK nejsou změřené. Koeficient udává potřebný výkon, ne přebytek, ten počítá kontrolní tabulka.

#### výroba vodíku: MHD

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 0 | 16.1 | 34.6 | 103.1 | 3.2 | 19.2 | D |
| konzervativní | 0 | 0 | 0 | 0 | 0 | 0 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 0.0, P90 7.6; 2040 P10 9.0, P90 56.5
- **Meze 2030 a 2040, konzervativní:** 2030 P10 0, P90 0; 2040 P10 0, P90 0
- **Průběh:** plynule
- **Společný faktor:** elektrifikace
- **Jak se došlo, progresivní:** 23,702 GWh / 1,1 kWh/km × 50 % × 7,49 kg/100 km × 0,850 úspora = 685,9 t vodíku × (48,26 výroba + 2,23 stlačení) kWh/kg = 34,6 GWh.
- **Jak se došlo, konzervativní:** Konzervativní cesta zůstává na bateriích, proto 0 GWh.
- **Ze zdrojů, progresivní:** Dopadová studie, Tab. 23 s. 116, s. 115 (1,1 kWh/km); JIVE 2 (7,49 kg/100 km); IEA Global Hydrogen Review 2024 (48,26 kWh/kg); US DOE záznam 9013
- **Ze zdrojů, konzervativní:** žádný (volba modelu č. 27)
- **Odhad, progresivní:** 50 % je volba modelu (volba modelu č. 27), bere se z celého řádku včetně tramvají. 0,850 je náhrada z nákladní dopravy, úsudek. Dosažení 48,26 kWh/kg až v 2050 je úsudek.
- **Odhad, konzervativní:** Žádné číslo, jen rozhodnutí cesty.
- **Podrobné odvození, progresivní:** Vozokilometry: 23,702 GWh z Dopadové studie Tab.23 / 1,1 kWh/km = 21,547 mil. km. 2030: P50 10 vozidel a 800 000 km z Dopadové studie s.116, P90 NAP CM 250 × 9,4 % = 23,5 vozidla × 80 000 km = 1,88 mil. km, P10 nula. 800 000 km × 7,265 kg/100 km = 58,1 t; × 54,23 kWh/kg = 3,15 GWh. 2040: 21,547 mil. km × 25 % = 5,387 mil. km; × 7,49 kg/100 km × 0,910 (eff_nakladni jako náhrada) = 367,2 t; × (50,13 + 2,23) kWh/kg = 19,2 GWh. 2050: 21,547 mil. km × 50 % = 10,774 mil. km; × 7,49 kg/100 km × 0,850 (eff_nakladni jako náhrada) = 685,9 t; × (48,26 + 2,23) kWh/kg = 34,6 GWh.
- **Podrobné odvození, konzervativní:** Nula. Konzervativní cesta zůstává na bateriích.
- **Zdroj, progresivní:** Dopadová studie s.119 (55 MWh/t); US DOE, Technical Targets for Proton Exchange Membrane Electrolysis, https://www.energy.gov/eere/fuelcells/technical-targets-proton-exchange-membrane-electrolysis; IEA, Global Hydrogen Review 2024, Assumptions Annex, tabulka Hydrogen, https://iea.blob.core.windows.net/assets/36017d2f-747b-4993-b06d-33209fe143fa/GHR24AssumptionsAnnex.pdf; US DOE Hydrogen Program Record 9013 (2009), https://www.hydrogen.energy.gov/pdfs/9013_energy_requirements_for_hydrogen_gas_compression.pdf; Vnitrostátní plán tištěná s.107 (NAP CM); volba modelu č. 27; Dopadová studie Tab.23 s.116, s.115 (1,1 kWh/km), s.116 (10 vozidel); JIVE 2, zpráva za období 5, https://cordis.europa.eu/project/id/779563/reporting; JIVE 1, https://www.sustainable-bus.com/fuel-cell-bus/jive-1-project-results-2024-hydrogen-buses-europe/
- **Zdroj, konzervativní:** volba modelu č. 27; definice cest (část 2)
- **Strana, progresivní:** s.115; Tab.23 s.116; s.119
- **Strana, konzervativní:** s.119
- **Citace, progresivní:** Dopadová studie s.119 „pro výrobu jedné tuny vodíku je zapotřebí 55 MWh elektrické energie“; DOE PEM „System, Energy Efficiency“ „55 (61%)“ (2022), „51 (65%)“ (2026), „46 (72%)“ (konečný cíl); IEA „Efficiency (LHV)“ „66%“ (2023), „69%“ (NZE 2030); DOE 9013 „2.23 and 3.0 kWh/kg H2 for compression to 440 bar and 880 bar“, „0.2 kWh/kg H2 for cooling“, „average compression energy of 3.1 kWh/kg H2“, „(1.7-6.4 kWh/kg H2)“, „2 to 4 kWh/kg H2“; Vnitrostátní plán „NAP CM počítá s v roce 2030 s možným nasazením 4 000 osobních automobilů na vodík, 1 200 lehkých užitkových automobilů, 250 autobusů, 600 nákladních vozidel“; Dopadová studie s.116 „Konkrétně se uvažuje o nasazení 10 vozidel. Celkový dopravní výkon je odhadován na 800 tis. km ročně.“; JIVE 2 „the average for all JIVE 2 buses was 7.49kg/100 km“, „ranging between 5.6 kg to 7.6 kg / 100 km for standard buses“; JIVE 1 „<9 kg/100 km for standard buses“
- **Citace, konzervativní:** Dopadová studie s.119 „Využití vodíku v osobní dopravě a železniční dopravě zatím nenabírá velkých obrátek“
- **Poznámka, progresivní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Sloupec ridic je prázdný, protože d_auta a d_nakladni jsou odvozené pro bateriové řádky. Vlivy jsou v odvození vypsané a hodnoty je už obsahují. Řádek MHD obsahuje i tramvaje a podíl autobusů v Tab.23 není uveden. 50 % se tu proto bere z celého řádku. Je to záměrné zjednodušení, P10 počítá s tím, že polovina řádku zůstane na trolejích. P90 přidává 40 mil. km autobusů z řádku MHD, úsudek. Horní mez spotřeby 9,1 kg/100 km je jen ze souhrnu vyhledávače. eff_nakladni je náhrada za chybějící odhad pro autobusy. Elektrolyzér kWh/kg: dnes 55 (Dopadová studie, DOE stav 2022). 2030 P50 52 je úsudek mezi 55 a cílem DOE 51; P10 33,3 / 0,69 = 48,26 (IEA NZE 2030). 2050 P50 48,26 je tatáž hodnota dosažená později, P10 46 konečný cíl DOE, P90 55 bez zlepšení jako Dopadová studie. 2040 je polovina cesty. Komprese se nezlepšuje, záznam DOE 9013 je z roku 2009. Meze skládají vstupy jako nezávislé, stejně jako oddíl 12 poznámek.
- **Poznámka, konzervativní:** Nula z rozhodnutí o cestě, ne z měření. Řádek existuje, protože stránka čeká obě cesty.
- **Koeficient, progresivní:** zima P10 0.0000, P50 0.0000, P90 0.3000; léto P10 2.1900, P50 2.9200, P90 4.3800; flexibilní ano; stupeň D
- **Koeficient, konzervativní:** zima P10 0.0000, P50 0.0000, P90 0.3000; léto P10 2.1900, P50 2.9200, P90 4.3800; flexibilní ano; stupeň D
- **Koeficient, odvození:** Zima vypnuto, sklad přečká špičku. Léto: běh na plný výkon, koef = 8 760 / plné hodiny: 4 000 h = 2,19, 3 000 h = 2,92, 2 000 h = 4,38.
- **Koeficient, zdroj:** NATO ENSEC COE, Hydrogen as Fuel: Production and Costs (3 000 až 4 000 h), https://old2.enseccoe.org/en/newsroom/hydrogen-as-fuel-production-and-costs/473; arXiv 2208.07302 (1 600 až 2 860 h, alkalické); Dopadová studie s.119
- **Koeficient, strana:** s.119
- **Koeficient, citace:** studie hodiny elektrolyzéru neuvádí
- **Koeficient, poznámka:** Hodiny v MSK nejsou změřené. Koeficient udává potřebný výkon, ne přebytek, ten počítá kontrolní tabulka.

#### výroba syntetického plynu

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 0 | 0 | 0 | 0 | 0 | 0 | C |
| konzervativní | 0 | 0 | 0 | 0 | 0 | 0 | C |

- **Meze 2030 a 2040, progresivní:** 2030 P10 0, P90 0; 2040 P10 0, P90 0
- **Meze 2030 a 2040, konzervativní:** 2030 P10 0, P90 0; 2040 P10 0, P90 0
- **Průběh:** plynule
- **Společný faktor:** cena
- **Jak se došlo:** Syntetický plyn se vyrábí z odpadu, ne z elektřiny, proto nula.
- **Ze zdrojů:** Volba modelu.
- **Odhad:** Vlastní spotřeba zařízení není započítaná. Jiné zdroje syntetického plynu, například důlní nebo koksárenský plyn, nejsou započítané, protože chybí podklad.
- **Podrobné odvození:** Syntetický plyn se vyrábí z odpadu, ne z elektřiny, proto je spotřeba elektřiny nula. Vlastní spotřeba zařízení není započítaná.
- **Zdroj:** Volba modelu
- **Poznámka:** Položka zůstává v tabulce, aby bylo vidět, že se na ni nezapomnělo. Jiné zdroje syntetického plynu, například důlní nebo koksárenský plyn, nejsou započítané, protože chybí podklad.
- **Koeficient, progresivní:** zima P10 0.0000, P50 0.0000, P90 0.3000; léto P10 2.1900, P50 2.9200, P90 4.3800; flexibilní ano; stupeň D
- **Koeficient, konzervativní:** zima P10 0.0000, P50 0.0000, P90 0.3000; léto P10 2.1900, P50 2.9200, P90 4.3800; flexibilní ano; stupeň D
- **Koeficient, odvození:** Zima vypnuto, sklad přečká špičku. Léto: běh na plný výkon, koef = 8 760 / plné hodiny: 4 000 h = 2,19, 3 000 h = 2,92, 2 000 h = 4,38.
- **Koeficient, zdroj:** NATO ENSEC COE, Hydrogen as Fuel: Production and Costs (3 000 až 4 000 h), https://old2.enseccoe.org/en/newsroom/hydrogen-as-fuel-production-and-costs/473; arXiv 2208.07302 (1 600 až 2 860 h, alkalické); Dopadová studie s.119
- **Koeficient, strana:** s.119
- **Koeficient, citace:** studie hodiny elektrolyzéru neuvádí
- **Koeficient, poznámka:** Hodiny v MSK nejsou změřené. Koeficient udává potřebný výkon, ne přebytek, ten počítá kontrolní tabulka.

#### vlastní spotřeba zdrojů

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 391.862 | 368.7 | 491.6 | 614.5 | 197.0 | 231.0 | C |
| konzervativní | 391.862 | 170.7 | 227.6 | 284.5 | 346.0 | 205.8 | C |

- **Meze 2030 a 2040, progresivní:** 2030 P10 147.7, P90 246.2; 2040 P10 173.3, P90 288.8
- **Meze 2030 a 2040, konzervativní:** 2030 P10 259.5, P90 432.5; 2040 P10 154.3, P90 257.2
- **Průběh:** plynule
- **Společný faktor:** zadny
- **Jak se došlo, progresivní:** Výroba × celostátní vlastní spotřeba: (519 GWh parní × 12,3451 % + 137,6 spalovací × 6,6352 % + 866 paroplynové × 1,9803 % + 3 942 jaderná × 5,4755 % + 55,5 voda × 0,9025 % + 1 710,5 vítr × 1,2331 % + 1 764 slunce × 0,8158 %) × 1,4367 kalibrace = 491,6 GWh.
- **Jak se došlo, konzervativní:** Výroba × celostátní vlastní spotřeba: (663,3 GWh parní × 12,3451 % + 322,4 spalovací × 6,6352 % + 2 404,8 paroplynové × 1,9803 % + 55,5 voda × 0,9025 % + 253,7 vítr × 1,2331 % + 476,3 slunce × 0,8158 %) × 1,4367 kalibrace = 227,6 GWh.
- **Ze zdrojů:** Dopadová studie, Tab. 1 s. 27 a s. 40; ERÚ čtvrtletní zpráva 2025 Q4, kap. 3.1 (celostátní míry). Výroba je z řádků této tabulky: parní = biomasa, odpad, ostatní paliva, hutní plyny; spalovací = zemní plyn, bioplyn; paroplynové = nové bloky, syntetický plyn
- **Odhad:** Přenos celostátních měr na kraj a kalibrace 1,4367 na dnešek jsou náš krok. Vstupy výroby nesou odhady svých řádků.
- **Podrobné odvození:** Ze studie: TVS 2023 a poměr k výrobě. Vlastní krok a jiné zdroje: základ: (TVSe 285,7 + TVSt 221,4) / 3 630,1 × 2 805,1634 = 391,8620 GWh. Výhled = součet (výroba × celostátní míra TVS 2025) × kalibrace 1,437: PE 12,35 %, PSE 6,64 %, PPE 1,98 %, JE 5,48 %, kalibrace = 391,9 / 272,7.
- **Zdroj:** Dopadová studie Tab.1 s.27, s.40; ERÚ, čtvrtletní zpráva 2025 Q4 kap. 3.1 (TVSe, TVSt)
- **Strana:** Tab.1 s.27; s.40
- **Citace:** Tab.1 TVSe 285,7, TVSt 221,4, výroba 3 630,1 GWh (2023, statistika); „lokální spotřebu a technologickou vlastní spotřebu“
- **Poznámka:** Vazba: počítá se z P50 řádků výroby v mediánovém roce událostí. Podle Dopadové studie s.40 je součástí tab. 6.3; celostátně však tab. 6.3 je menší než součet všech složek, takže plný obsah neověřen. Carve-out ze sektoru Energetika. ±25 % je úsudek.
- **Koeficient, progresivní:** zima P10 0.9882, P50 1.2847, P90 2.1741; léto P10 0.6482, P50 0.8643, P90 1.0803; flexibilní ne; stupeň D
- **Koeficient, konzervativní:** zima P10 0.9882, P50 1.2847, P90 2.1741; léto P10 0.6482, P50 0.8643, P90 1.0803; flexibilní ne; stupeň D
- **Koeficient, odvození:** Apriorní zima 1,00, 1,30, 2,20 × kalibrace 0,988; léto 0,60, 0,80, 1,00 × kalibrace 1,080. běží se zdroji; P90 odpovídá špičkovému provozu uhlí dnes.
- **Koeficient, zdroj:** Dopadová studie Tab.1 s.27, s.150
- **Koeficient, strana:** rov.5 a 6 s.74
- **Koeficient, citace:** „Roční maximum zatížení elektrizační soustavy za MSK se nesleduje.“
- **Koeficient, poznámka:** Lokální část, viz metodika.

#### ostatní energetika (přidaná položka)

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 1000.8438 | 600 | 1000.8 | 1050 | 1000.8 | 1000.8 | D |
| konzervativní | 1000.8438 | 600 | 1000.8 | 1050 | 1000.8 | 1000.8 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 800, P90 1050; 2040 P10 700, P90 1050
- **Meze 2030 a 2040, konzervativní:** 2030 P10 800, P90 1050; 2040 P10 700, P90 1050
- **Průběh:** plynule
- **Společný faktor:** zadny
- **Jak se došlo, progresivní:** Drží hodnotu 2025 (1 000,8438 GWh, zaokrouhleno 1 000,8 GWh), protože zdroj pro výhled není.
- **Jak se došlo, konzervativní:** Drží hodnotu 2025 (1 000,8438 GWh, zaokrouhleno 1 000,8 GWh), protože zdroj pro výhled není a cesta nemá zadanou odchylku.
- **Ze zdrojů:** ERÚ čtvrtletní zprávy 2025, tab. 6.3 (Energetika)
- **Odhad:** Držení je úsudek bez zdroje. Základ je dopočtený zbytek.
- **Podrobné odvození, progresivní:** Ze studie: nic pro výhled. Vlastní krok a jiné zdroje: základ = reziduum: Energetika 1 392,7058 − vlastní spotřeba 391,8620 = 1 000,8438 GWh. Výhled drží základ, zdroj pro to není.
- **Podrobné odvození, konzervativní:** Ze studie: nic pro výhled. Vlastní krok a jiné zdroje: základ 1 000,8438 GWh. Výhled drží základ, zdroj pro to není.
- **Zdroj, progresivní:** ERÚ, čtvrtletní zprávy 2025 Q1 až Q4, tab. 6.3, řádek MSK; ERÚ, čtvrtletní zprávy 2026 Q1 a Q2
- **Zdroj, konzervativní:** ERÚ, čtvrtletní zprávy 2025 Q1 až Q4, tab. 6.3, řádek MSK
- **Strana:** Tab.6 s.40
- **Citace:** Tab.6 Energetika 997 040,3 MWh (2023)
- **Poznámka, progresivní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Přidána, protože jinak sektor nejde uzavřít. Obsah ERÚ nedefinuje, obsahuje sem přeřazenou spotřebu (viz poznámky). Zlepší: dotaz na ERÚ.
- **Poznámka, konzervativní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Bez zadané odchylky.
- **Koeficient, progresivní:** zima P10 0.9882, P50 1.0870, P90 1.2847; léto P10 0.9183, P50 1.0803, P90 1.1884; flexibilní ne; stupeň D
- **Koeficient, konzervativní:** zima P10 0.9882, P50 1.0870, P90 1.2847; léto P10 0.9183, P50 1.0803, P90 1.1884; flexibilní ne; stupeň D
- **Koeficient, odvození:** Apriorní zima 1,00, 1,10, 1,30 × kalibrace 0,988; léto 0,85, 1,00, 1,10 × kalibrace 1,080. lokální a provozní spotřeba, plochá.
- **Koeficient, zdroj:** Dopadová studie Tab.6 s.40; ERÚ tab. 6.3
- **Koeficient, strana:** rov.5 a 6 s.74
- **Koeficient, citace:** „Roční maximum zatížení elektrizační soustavy za MSK se nesleduje.“
- **Koeficient, poznámka:** Obsah položky ERÚ nedefinuje. Lokální část, viz metodika.

#### ztráty v sítích

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 219.3158 | 428.6 | 476.9 | 611.1 | 267.5 | 330.2 | C |
| konzervativní | 219.3158 | 337.7 | 448.2 | 533.3 | 440.7 | 435.2 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 240.4, P90 342.7; 2040 P10 296.8, P90 423.2
- **Meze 2030 a 2040, konzervativní:** 2030 P10 332.0, P90 524.5; 2040 P10 327.9, P90 517.8
- **Průběh:** plynule
- **Společný faktor:** zadny
- **Jak se došlo, progresivní:** 12 968,7 GWh spotřeby v síti × 3,547 % / (100 % − 3,547 %) = 476,9 GWh.
- **Jak se došlo, konzervativní:** 6 985,0 GWh spotřeby v síti × 6,030 % (1,7 × 3,547 %) / (100 % − 6,030 %) = 448,2 GWh.
- **Ze zdrojů:** Dopadová studie, Tab. 1 s. 27 a rov. 7 s. 74 (3,547 %)
- **Odhad, progresivní:** Míra je za bývalý Severomoravský kraj. Spotřeba v síti nese odhady ostatních položek.
- **Odhad, konzervativní:** Míra je za bývalý Severomoravský kraj. Spotřeba v síti nese odhady ostatních položek. Násobek 1,7 je náš odhad.
- **Podrobné odvození, progresivní:** Ze studie: míra a báze. Vlastní krok a jiné zdroje: základ: 6.2 5 963,8184 × 3,547 % / (1 − 3,547 %) = 219,3158 GWh. Výhled: (součet položek spotřeby P50 − lokální část 886,8302) × r / (1 − r); 2050 síť 12 968,7 GWh, r 3,547 %.
- **Podrobné odvození, konzervativní:** Ze studie: míra a báze. Vlastní krok a jiné zdroje: základ: 6.2 5 963,8184 × 3,547 % / (1 − 3,547 %) = 219,3158 GWh. Výhled: (součet položek spotřeby P50 − lokální část 886,8302) × r / (1 − r); 2050 síť 6 985,0 GWh, r 6,030 %.
- **Zdroj:** Dopadová studie Tab.1 s.27, rov.7 s.74; ERÚ, čtvrtletní zprávy 2025 Q1 až Q4, tab. 6.3, řádek MSK; tab. 6.2; ERÚ, čtvrtletní zpráva 2025 Q4 kap. 1 a 3.2
- **Strana:** Tab.1 s.27; s.27; rov.7 s.74
- **Citace:** Tab.1 „3,547 %“ (2023), Čistá spotřeba 5 805,4, Spotřeba na prahu ES 6 018,9 GWh; „součet spotřeby elektřiny netto a ztrát v sítích“
- **Poznámka, progresivní:** Míra je na bázi spotřeby na prahu sítě, ne netto; platí 6 018,9 − 5 805,4 = 213,5 a 213,5 / 6 018,9 = 3,547 %. Lokální spotřeba se odečítá, neteče sítí. Míra je za bývalý Severomoravský kraj (s.74). Celostátně 3 161,7 / (53 868,6 + 3 161,7) = 5,54 %, s přenosem. Řádek je nad tab. 6.3.
- **Poznámka, konzervativní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Dvojnásobná zátěž nejde použít čistě: jde o zatížení, ne energii. Čteno jako vyšší míra: 30 % stálé ztráty + 70 % proměnné × 2 = 1,7 × 3,547 %. Rozdělení 30/70 je úsudek. Řádek je nad tab. 6.3.
- **Koeficient, progresivní:** zima P10 1.2000, P50 1.4926, P90 2.1000; léto P10 0.7000, P50 0.9000, P90 1.1000; flexibilní ne; stupeň D
- **Koeficient, konzervativní:** zima P10 1.2000, P50 1.4926, P90 2.1000; léto P10 0.7000, P50 0.9000, P90 1.1000; flexibilní ne; stupeň D
- **Koeficient, odvození:** 8 760 / 5 869 = 1,4926: studie drží ztráty jako stálé procento. P90 2,1 je kvadratický vliv proudu, úsudek. Léto 0,9 je úsudek.
- **Koeficient, zdroj:** Dopadová studie Tab.1 s.27, rov.7 s.74, s.175
- **Koeficient, strana:** rov.7 s.74; s.175
- **Koeficient, citace:** „roční době trvání maximálního zatížení MSK 5 869 hodin“
- **Koeficient, poznámka:** Zima je metoda studie, léto úsudek, proto D. Bez kalibračního faktoru.

#### ztráty baterií

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 0 | 56.1 | 350.2 | 700.6 | 2 | 60 | D |
| konzervativní | 0 | 7.3 | 31.4 | 158.6 | 1 | 8 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 0.5, P90 6; 2040 P10 10, P90 150
- **Meze 2030 a 2040, konzervativní:** 2030 P10 0.2, P90 3; 2040 P10 2, P90 40
- **Průběh:** plynule
- **Společný faktor:** zadny
- **Jak se došlo, progresivní:** Úložiště 3 dny ze spotřeby této cesty bez pružných položek: (15 344,4 − 4 726,4) GWh / 365 × 3 = 87,27 GWh; × 30 cyklů × (1 − 0,88) = 314,2; + 1 GWh × 300 cyklů × 0,12 = 36,0; součet 350,2. 2030: 50 MWh × 300 × 0,12 = 1,8.
- **Jak se došlo, konzervativní:** Záloha 10 % z progresivního úložiště: 8,73 GWh × 30 cyklů × 0,12 = 31,4.
- **Ze zdrojů:** Tři dny akumulace z definice cesty. Denní blok 1 GWh: Dopadová studie, s. 145.
- **Odhad:** Účinnost 0,88, počet cyklů a to, že se pružné položky vypnou.
- **Podrobné odvození, progresivní:** Úložiště 3 dny ze spotřeby této cesty bez pružných položek: (15 344,4 − 4 726,4) GWh / 365 × 3 = 87,27 GWh; × 30 cyklů × (1 − 0,88) = 314,2; + 1 GWh × 300 cyklů × 0,12 = 36,0; součet 350,2. 2030: 50 MWh × 300 × 0,12 = 1,8.
- **Podrobné odvození, konzervativní:** Záloha 10 % z progresivního úložiště: 8,73 GWh × 30 cyklů × 0,12 = 31,4.
- **Zdroj, progresivní:** Dopadová studie s.145, Obr.28 s.110; definice cest (část 2)
- **Zdroj, konzervativní:** Definice cest (část 2); Dopadová studie s.145
- **Strana:** s.145
- **Citace:** očekávaný: „přibližně o sumárním výkonu 1 GW a celkové kapacitě 1 GWh“; účinnost neuvádí
- **Poznámka:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to náš odhad. Účinnost 0,88 a počet cyklů nejsou ve zdrojích. Elektrolýza, výroba syntetického plynu a elektrokotle se při výpadku vypnou, proto se do tří dnů nepočítají.
- **Koeficient, progresivní:** zima P10 0.0000, P50 0.0000, P90 1.0000; léto P10 0.5000, P50 1.0000, P90 3.0000; flexibilní ano; stupeň D
- **Koeficient, konzervativní:** zima P10 0.0000, P50 0.0000, P90 1.0000; léto P10 0.5000, P50 1.0000, P90 3.0000; flexibilní ano; stupeň D
- **Koeficient, odvození:** V bilanci bez baterií 0. Léto nabíjení kolem průměru, úsudek.
- **Koeficient, zdroj:** tabulka položek (část 5); vlastní úsudek
- **Koeficient, strana:** s.145
- **Koeficient, citace:** účinnost neuvádí
- **Koeficient, poznámka:** Hodnotu nepodporuje žádný zdroj.

#### zemědělství a stavebnictví

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 77.3071 | 70 | 77.3 | 110 | 77.3 | 77.3 | D |
| konzervativní | 77.3071 | 65 | 77.3 | 100 | 77.3 | 77.3 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 70, P90 90; 2040 P10 70, P90 100
- **Meze 2030 a 2040, konzervativní:** 2030 P10 70, P90 88; 2040 P10 68, P90 95
- **Průběh:** plynule
- **Společný faktor:** zadny
- **Jak se došlo:** Drží hodnotu 2025 (77,3071 GWh, zaokrouhleno 77,3 GWh), protože zdroj pro výhled není a řada dlouho kolísá kolem 80 GWh.
- **Ze zdrojů:** ERÚ čtvrtletní zprávy 2025, tab. 6.3; Dopadová studie, Tab. 6 s. 40
- **Odhad:** Držení je úsudek bez zdroje.
- **Podrobné odvození, progresivní:** Ze studie: nic pro výhled. Vlastní krok a jiné zdroje: základ: Stavebnictví 34,4329 + Zemědělství 42,8742 = 77,3071 GWh. Výhled drží základ, zdroj pro to není.
- **Podrobné odvození, konzervativní:** Ze studie: nic pro výhled. Vlastní krok a jiné zdroje: základ 77,3071 GWh.
- **Zdroj, progresivní:** ERÚ, čtvrtletní zprávy 2025 Q1 až Q4, tab. 6.3, řádek MSK; Dopadová studie Tab.6 s.40
- **Zdroj, konzervativní:** ERÚ, čtvrtletní zprávy 2025 Q1 až Q4, tab. 6.3, řádek MSK
- **Strana:** Tab.6 s.40
- **Citace:** Tab.6 42 445,2 a 40 716,7 MWh (2023)
- **Poznámka, progresivní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Řada kolísá kolem 80 GWh, málo vlivné.
- **Poznámka, konzervativní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Bez zadané odchylky.
- **Koeficient, progresivní:** zima P10 0.7906, P50 0.9882, P90 1.2847; léto P10 0.6482, P50 1.0803, P90 1.5124; flexibilní ne; stupeň D
- **Koeficient, konzervativní:** zima P10 0.7906, P50 0.9882, P90 1.2847; léto P10 0.6482, P50 1.0803, P90 1.5124; flexibilní ne; stupeň D
- **Koeficient, odvození:** Apriorní zima 0,80, 1,00, 1,30 × kalibrace 0,988; léto 0,60, 1,00, 1,40 × kalibrace 1,080. bez výrazné špičky.
- **Koeficient, zdroj:** vlastní úsudek
- **Koeficient, strana:** rov.5 a 6 s.74
- **Koeficient, citace:** „Roční maximum zatížení elektrizační soustavy za MSK se nesleduje.“
- **Koeficient, poznámka:** Málo vlivné.

#### úspory a účinnost

| Cesta | Základ 2025 | P10 2050 | P50 2050 | P90 2050 | P50 2030 | P50 2040 | Stupeň |
|---|---|---|---|---|---|---|---|
| progresivní | 0 | -500 | -290 | -100 | -60 | -160 | D |
| konzervativní | 0 | -300 | -145 | -50 | -30 | -80 | D |

- **Meze 2030 a 2040, progresivní:** 2030 P10 -120, P90 -20; 2040 P10 -300, P90 -60
- **Meze 2030 a 2040, konzervativní:** 2030 P10 -80, P90 -10; 2040 P10 -180, P90 -20
- **Průběh:** plynule
- **Společný faktor:** cena
- **Jak se došlo, progresivní:** 10 % × (domácnosti 434 + služby 996 + ostatní průmysl 1 430) GWh = −286 GWh, zaokrouhleno na desítky = −290 GWh.
- **Jak se došlo, konzervativní:** 50 % z progresivní hodnoty −290 GWh = −145 GWh.
- **Ze zdrojů, progresivní:** žádné číslo ze zdroje; Vnitrostátní plán, s. 52 a s. 346 jen jako podklad
- **Ze zdrojů, konzervativní:** žádné číslo ze zdroje; Vnitrostátní plán, s. 52 jen jako podklad
- **Odhad, progresivní:** Celá hodnota je úsudek. 10 % nemá zdroj. 1 430 GWh neodpovídá dnešnímu řádku ostatního průmyslu.
- **Odhad, konzervativní:** Celá hodnota je úsudek. Polovina je úsudek, nemá zdroj.
- **Podrobné odvození, progresivní:** Ze studie: nic. Vlastní krok a jiné zdroje: 2050 P50: 10 % × (domácnosti 434 + služby 996 + ostatní průmysl cca 1 430) = −286, zaokrouhleno −290.
- **Podrobné odvození, konzervativní:** Ze studie: nic. Vlastní krok a jiné zdroje: 50 % × progresivní P50 = −145.
- **Zdroj, progresivní:** Vnitrostátní plán s.52, s.346
- **Zdroj, konzervativní:** Vnitrostátní plán s.52
- **Poznámka, progresivní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Dopadovou studii nelze použít: Studie úspory nečísluje. Záporná položka; P10 je nejsilnější úspora. Základ 0, úspory jsou změna oproti 2025. Procento je úsudek. Zateplení je již v tepelných čerpadlech, zde jen elektrospotřebiče a pohony. Kvantil faktoru se zde čte obráceně.
- **Poznámka, konzervativní:** P50 v tomto řádku nebo jeho část nepodporuje žádný zdroj, je to úsudek bez zdroje. Dopadovou studii nelze použít: Studie úspory nečísluje. Polovina je úsudek. Kvantil faktoru se zde čte obráceně.
- **Koeficient, progresivní:** zima P10 0.9882, P50 1.4823, P90 1.9764; léto P10 0.6482, P50 0.8643, P90 1.0803; flexibilní ne; stupeň D
- **Koeficient, konzervativní:** zima P10 0.9882, P50 1.4823, P90 1.9764; léto P10 0.6482, P50 0.8643, P90 1.0803; flexibilní ne; stupeň D
- **Koeficient, odvození:** Apriorní zima 1,00, 1,50, 2,00 × kalibrace 0,988; léto 0,60, 0,80, 1,00 × kalibrace 1,080. úspory následují spotřebiče a pohony.
- **Koeficient, zdroj:** vlastní úsudek
- **Koeficient, strana:** rov.5 a 6 s.74
- **Koeficient, citace:** „Roční maximum zatížení elektrizační soustavy za MSK se nesleduje.“
- **Koeficient, poznámka:** Záporná položka, koeficient je kladný.

## 6. Řídicí vlivy

Vliv D(t) je vnější index, který se k položce váže ve sloupci Řídicí vliv. Kombinovaný vliv je součin vstupních vlivů, viz odvození níže.

- **Čtení v modelu.** Sloupce p10 až p90 v tabulce položek (část 5) jsou y včetně D. D se na ně znovu nenásobí. Cíl adopce je s_T = y(2050) / D(2050).
- **Směr mezí.** U vlivů platí P10 ≤ hodnota ≤ P90, P10 tedy znamená nižší spotřebu. Kvantil faktoru se u přímotopů čte obráceně jako dosud.
- **Meze položky.** P10 = s_P10 × D_P10 a P90 = s_P90 × D_P90, protože jedna položka drží v běhu jeden kvantil (volba modelu č. 11). Meze kombinovaného vlivu berou vstupy jako nezávislé: D_P10 = D_P50 × exp(−√Σ ln(x_P50 / x_P10)²), u P90 obdobně. Prosté násobení všech P10 by pásmo přehnalo.

### pop_msk: Počet obyvatel MSK k 1.1., index 2025 = 1

| Rok | Hodnota | P10 | P90 | Stupeň | Odvození |
|---|---|---|---|---|---|
| 2025 | 1.0000 | 1.0000 | 1.0000 | A | Základ. Změřeno 1.1.2025: 1 176 380 + 6 233 = 1 182 613 osob (ČSÚ, součet z tisku). Projekce pro týž den: 1 182 589,7930. Rozdíl 23,2 osoby. Index = 1. |
| 2030 | 0.9622 | 0.9521 | 0.9727 | B | 1 137 904,4039 / 1 182 589,7930 = 0.9622. ČSÚ dává kraji jen jednu variantu, meze jsou úsudek: 2050 P10 950 000 a P90 1 050 000 osob, tedy násobek poklesu 1.2679 a 0.7228, stejný pro všechny roky. Opora mezí: změřeno 1.1.2026 1 176 380 proti projekci 1 172 172,7124 (o 4 207 výš); starší edice ČSÚ 0,98 mil. v 2050 (edice 2013) a pod 1 mil. až 2053 (edice 2019), obojí jen ze souhrnu vyhledávače. |
| 2040 | 0.9040 | 0.8783 | 0.9306 | B | 1 069 062,5895 / 1 182 589,7930 = 0.9040. ČSÚ dává kraji jen jednu variantu, meze jsou úsudek: 2050 P10 950 000 a P90 1 050 000 osob, tedy násobek poklesu 1.2679 a 0.7228, stejný pro všechny roky. Opora mezí: změřeno 1.1.2026 1 176 380 proti projekci 1 172 172,7124 (o 4 207 výš); starší edice ČSÚ 0,98 mil. v 2050 (edice 2013) a pod 1 mil. až 2053 (edice 2019), obojí jen ze souhrnu vyhledávače. |
| 2050 | 0.8449 | 0.8033 | 0.8879 | B | 999 144,3026 / 1 182 589,7930 = 0.8449. ČSÚ dává kraji jen jednu variantu, meze jsou úsudek: 2050 P10 950 000 a P90 1 050 000 osob, tedy násobek poklesu 1.2679 a 0.7228, stejný pro všechny roky. Opora mezí: změřeno 1.1.2026 1 176 380 proti projekci 1 172 172,7124 (o 4 207 výš); starší edice ČSÚ 0,98 mil. v 2050 (edice 2013) a pod 1 mil. až 2053 (edice 2019), obojí jen ze souhrnu vyhledávače. |

**Zdroj:** ČSÚ, Obyvatelstvo v Moravskoslezském kraji v roce 2025, https://csu.gov.cz/msk/obyvatelstvo-v-moravskoslezskem-kraji-v-roce-2025; ČSÚ, Projekce obyvatelstva v krajích ČR do roku 2080, kód 130052-24, 12.12.2024, Tab. 4_CZ080, řádek Počet obyvatel: celkem, https://csu.gov.cz/produkty/projekce-obyvatelstva-v-krajich-cr-do-roku-2080

**Zdroj:** ČSÚ, Projekce obyvatelstva v krajích ČR do roku 2080, kód 130052-24, 12.12.2024, Tab. 4_CZ080, řádek Počet obyvatel: celkem, https://csu.gov.cz/produkty/projekce-obyvatelstva-v-krajich-cr-do-roku-2080; ČSÚ, Obyvatelstvo v Moravskoslezském kraji v roce 2025, https://csu.gov.cz/msk/obyvatelstvo-v-moravskoslezskem-kraji-v-roce-2025

**Citace:** „K 31. 12. 2025 žilo na území Moravskoslezského kraje 1 176 380 obyvatel, z toho 50,9 % žen.“; „Celkově se počet obyvatel kraje od počátku roku snížil o 6 233 osob“; „Tab. 1 | Moravskoslezský kraj: Počet obyvatel podle věku (k 1. 1.) – obě pohlaví“; Tab. 4 „Počet obyvatel: celkem“ 2025 1182589.7930313854, 2030 1137904.4038508921, 2040 1069062.5894820732, 2050 999144.30260464922; úvod: „v jedné variantě“

**Citace:** „Tab. 1 | Moravskoslezský kraj: Počet obyvatel podle věku (k 1. 1.) – obě pohlaví“; Tab. 4 „Počet obyvatel: celkem“ 2025 1182589.7930313854, 2030 1137904.4038508921, 2040 1069062.5894820732, 2050 999144.30260464922; úvod: „v jedné variantě“

### velikost_dom: Inverzní velikost domácnosti (osoby na domácnost 2025 / rok), index 2025 = 1

| Rok | Hodnota | P10 | P90 | Stupeň | Odvození |
|---|---|---|---|---|---|
| 2025 | 1.0000 | 1.0000 | 1.0000 | D | Inverze velikosti domácnosti, projekce neexistuje. Osob na domácnost: 2011 1 205 836 / 507 567 = 2.3757; 2021 1 162 841 / 541 276 = 2.1483 (ČSÚ tiskne 2,12, jiná báze osob). Pokles 0.02274 os./rok. Úsudek: P50 poloviční tempo 0.01137, 2025 2.1029; P10 velikost stojí; P90 tři čtvrtiny tempa po 2025. |
| 2030 | 1.0278 | 1.0000 | 1.0423 | D | Inverze velikosti domácnosti, projekce neexistuje. Osob na domácnost: 2011 1 205 836 / 507 567 = 2.3757; 2021 1 162 841 / 541 276 = 2.1483 (ČSÚ tiskne 2,12, jiná báze osob). Pokles 0.02274 os./rok. Úsudek: P50 poloviční tempo 0.01137, 2025 2.1029; P10 velikost stojí; P90 tři čtvrtiny tempa po 2025. 2030: 2.1029 / (2.1029 − 5 × 0.01137) = 1.0278. |
| 2040 | 1.0883 | 1.0000 | 1.1385 | D | Inverze velikosti domácnosti, projekce neexistuje. Osob na domácnost: 2011 1 205 836 / 507 567 = 2.3757; 2021 1 162 841 / 541 276 = 2.1483 (ČSÚ tiskne 2,12, jiná báze osob). Pokles 0.02274 os./rok. Úsudek: P50 poloviční tempo 0.01137, 2025 2.1029; P10 velikost stojí; P90 tři čtvrtiny tempa po 2025. 2040: 2.1029 / (2.1029 − 15 × 0.01137) = 1.0883. |
| 2050 | 1.1563 | 1.0000 | 1.2543 | D | Inverze velikosti domácnosti, projekce neexistuje. Osob na domácnost: 2011 1 205 836 / 507 567 = 2.3757; 2021 1 162 841 / 541 276 = 2.1483 (ČSÚ tiskne 2,12, jiná báze osob). Pokles 0.02274 os./rok. Úsudek: P50 poloviční tempo 0.01137, 2025 2.1029; P10 velikost stojí; P90 tři čtvrtiny tempa po 2025. 2050: 2.1029 / (2.1029 − 25 × 0.01137) = 1.1563. |

**Zdroj:** ČSÚ, Základní výsledky SLDB 2021 Moravskoslezský kraj , s.17, s.22, s.79; https://scitani.gov.cz/velikost-hospodarici-domacnosti

**Citace:** „Celkový počet hospodařících domácností v kraji dosáhl hodnoty 541 267. Ve srovnání s předchozím sčítáním v roce 2011 se jejich počet zvýšil o 33,7 tisíce, tj. o 6,6 %.“; scitani.gov.cz „Moravskoslezský kraj“ „541 276“ „2,12“; s.79 „Počet obyvatel 1 257 090 1 278 726 1 265 019 1 205 836 1 162 841“

### d_domacnosti: Počet domácností MSK, index 2025 = 1

| Rok | Hodnota | P10 | P90 | Stupeň | Odvození |
|---|---|---|---|---|---|
| 2025 | 1.0000 | 1.0000 | 1.0000 | D | ODVOZENO, projekce domácností ČSÚ neexistuje. d_domacnosti = pop_msk × velikost_dom = 1.0000 × 1.0000 = 1.0000. Meze skládají vstupy jako nezávislé, viz poznámky, oddíl 12. |
| 2030 | 0.9889 | 0.9603 | 1.0066 | D | ODVOZENO, projekce domácností ČSÚ neexistuje. d_domacnosti = pop_msk × velikost_dom = 0.9622 × 1.0278 = 0.9889. Meze skládají vstupy jako nezávislé, viz poznámky, oddíl 12. |
| 2040 | 0.9838 | 0.8997 | 1.0380 | D | ODVOZENO, projekce domácností ČSÚ neexistuje. d_domacnosti = pop_msk × velikost_dom = 0.9040 × 1.0883 = 0.9838. Meze skládají vstupy jako nezávislé, viz poznámky, oddíl 12. |
| 2050 | 0.9770 | 0.8377 | 1.0746 | D | ODVOZENO, projekce domácností ČSÚ neexistuje. d_domacnosti = pop_msk × velikost_dom = 0.8449 × 1.1563 = 0.9770. Meze skládají vstupy jako nezávislé, viz poznámky, oddíl 12. |

**Zdroj:** ČSÚ, Projekce obyvatelstva v krajích ČR do roku 2080, kód 130052-24, 12.12.2024, Tab. 4_CZ080, řádek Počet obyvatel: celkem, https://csu.gov.cz/produkty/projekce-obyvatelstva-v-krajich-cr-do-roku-2080; ČSÚ, Základní výsledky SLDB 2021 Moravskoslezský kraj , s.17, s.22, s.79; https://scitani.gov.cz/velikost-hospodarici-domacnosti

**Citace:** „Celkový počet hospodařících domácností v kraji dosáhl hodnoty 541 267. Ve srovnání s předchozím sčítáním v roce 2011 se jejich počet zvýšil o 33,7 tisíce, tj. o 6,6 %.“; scitani.gov.cz „Moravskoslezský kraj“ „541 276“ „2,12“; s.79 „Počet obyvatel 1 257 090 1 278 726 1 265 019 1 205 836 1 162 841“

### auta_na_os: Osobní auta včetně dodávkových na osobu, index 2025 = 1

| Rok | Hodnota | P10 | P90 | Stupeň | Odvození |
|---|---|---|---|---|---|
| 2025 | 1.0000 | 1.0000 | 1.0000 | A | Změřeno 2024: 625 545 / 1 184 662 = 0.5280 aut včetně dodávek na osobu (2022 0,5053, 2023 0,5173); Česko 6 638 172 / 10 886 531 = 0.6098. Rok 2024 je brán jako 2025. Projekce neexistuje. ÚSUDEK: P50 lineární dorovnání na dnešní Česko v 2050, 0.6098 / 0.5280 = 1.1548; P10 0,95 (stárnutí); P90 0,70 aut na osobu, 0,70 / 0.5280 = 1.3257. Registr obsahuje i málo používaná auta a proběh na auto zůstává dnešní. |
| 2030 | 1.0310 | 0.9900 | 1.0651 | D | Změřeno 2024: 625 545 / 1 184 662 = 0.5280 aut včetně dodávek na osobu (2022 0,5053, 2023 0,5173); Česko 6 638 172 / 10 886 531 = 0.6098. Rok 2024 je brán jako 2025. Projekce neexistuje. ÚSUDEK: P50 lineární dorovnání na dnešní Česko v 2050, 0.6098 / 0.5280 = 1.1548; P10 0,95 (stárnutí); P90 0,70 aut na osobu, 0,70 / 0.5280 = 1.3257. Registr obsahuje i málo používaná auta a proběh na auto zůstává dnešní. |
| 2040 | 1.0929 | 0.9700 | 1.1954 | D | Změřeno 2024: 625 545 / 1 184 662 = 0.5280 aut včetně dodávek na osobu (2022 0,5053, 2023 0,5173); Česko 6 638 172 / 10 886 531 = 0.6098. Rok 2024 je brán jako 2025. Projekce neexistuje. ÚSUDEK: P50 lineární dorovnání na dnešní Česko v 2050, 0.6098 / 0.5280 = 1.1548; P10 0,95 (stárnutí); P90 0,70 aut na osobu, 0,70 / 0.5280 = 1.3257. Registr obsahuje i málo používaná auta a proběh na auto zůstává dnešní. |
| 2050 | 1.1548 | 0.9500 | 1.3257 | D | Změřeno 2024: 625 545 / 1 184 662 = 0.5280 aut včetně dodávek na osobu (2022 0,5053, 2023 0,5173); Česko 6 638 172 / 10 886 531 = 0.6098. Rok 2024 je brán jako 2025. Projekce neexistuje. ÚSUDEK: P50 lineární dorovnání na dnešní Česko v 2050, 0.6098 / 0.5280 = 1.1548; P10 0,95 (stárnutí); P90 0,70 aut na osobu, 0,70 / 0.5280 = 1.3257. Registr obsahuje i málo používaná auta a proběh na auto zůstává dnešní. |

**Zdroj:** ČSÚ, Statistická ročenka Moravskoslezského kraje 2025, tab. 17.1, 17.102 a 27.102 (zdroj dat Ministerstvo dopravy), https://csu.gov.cz/produkty/statisticka-rocenka-moravskoslezskeho-kraje-2025

**Citace:** tab. 17.1 „Osobní automobily včetně dodávkových | 600223 | 615713 | 625545“ (2022, 2023, 2024, k 31.12.); tab. 27.102 „Střední stav obyvatel“ Česko 10886531; tab. 27.3 „Střední stav obyvatel | osoby | 1187776 | 1190143 | 1184662“; tab. 17.102 „Česko / Czechia | 6638172“

### eff_auta: Spotřeba bateriového osobního auta na km, index 2025 = 1

| Rok | Hodnota | P10 | P90 | Stupeň | Odvození |
|---|---|---|---|---|---|
| 2025 | 1.0000 | 1.0000 | 1.0000 | B | Index na 17 kWh/100 km z Dopadové studie. Nová auta 2050 proti 2015: pesimistický případ (0,30 + 0,29) / 2 = 0.295, optimistický (0,52 + 0,49) / 2 = 0.505. Vlastní krok: P50 pesimistický případ, P10 optimistický, P90 bez zlepšení (1,0); lineárně od 2025 do 2050. Krause má potenciál nových aut proti roku 2015, ne vozový park; zpoždění parku a zlepšení 2015 až 2025 tu nejsou zvlášť. |
| 2030 | 0.9410 | 0.8990 | 1.0000 | C | Index na 17 kWh/100 km z Dopadové studie. Nová auta 2050 proti 2015: pesimistický případ (0,30 + 0,29) / 2 = 0.295, optimistický (0,52 + 0,49) / 2 = 0.505. Vlastní krok: P50 pesimistický případ, P10 optimistický, P90 bez zlepšení (1,0); lineárně od 2025 do 2050. Krause má potenciál nových aut proti roku 2015, ne vozový park; zpoždění parku a zlepšení 2015 až 2025 tu nejsou zvlášť. |
| 2040 | 0.8230 | 0.6970 | 1.0000 | C | Index na 17 kWh/100 km z Dopadové studie. Nová auta 2050 proti 2015: pesimistický případ (0,30 + 0,29) / 2 = 0.295, optimistický (0,52 + 0,49) / 2 = 0.505. Vlastní krok: P50 pesimistický případ, P10 optimistický, P90 bez zlepšení (1,0); lineárně od 2025 do 2050. Krause má potenciál nových aut proti roku 2015, ne vozový park; zpoždění parku a zlepšení 2015 až 2025 tu nejsou zvlášť. |
| 2050 | 0.7050 | 0.4950 | 1.0000 | C | Index na 17 kWh/100 km z Dopadové studie. Nová auta 2050 proti 2015: pesimistický případ (0,30 + 0,29) / 2 = 0.295, optimistický (0,52 + 0,49) / 2 = 0.505. Vlastní krok: P50 pesimistický případ, P10 optimistický, P90 bez zlepšení (1,0); lineárně od 2025 do 2050. Krause má potenciál nových aut proti roku 2015, ne vozový park; zpoždění parku a zlepšení 2015 až 2025 tu nejsou zvlášť. |

**Zdroj:** Krause et al., EU road vehicle energy consumption and CO2 emissions by 2050, Energy Policy 138 (2020) 111224, Tab.4 a Tab.6, doi 10.1016/j.enpol.2019.111224; Dopadová studie s.110

**Citace:** Tab.4 „Small car 2015 (Baseline)“ 155 Wh/km, „Large Car 2015 (Baseline)“ 189 Wh/km; Tab.6 „Small Car 2050, Pessimistic“ 109, 0.30; „Small Car 2050, Optimistic“ 74, 0.52; „Large Car 2050, Pessimistic“ 135, 0.29; „Large Car 2050, Optimistic“ 96, 0.49; Dopadová studie s.110 „průměrné spotřebě elektromobilu 17 kWh / 100 km“

### eff_nakladni: Spotřeba bateriového nákladního auta na km, index 2025 = 1

| Rok | Hodnota | P10 | P90 | Stupeň | Odvození |
|---|---|---|---|---|---|
| 2025 | 1.0000 | 1.0000 | 1.0000 | D | ÚSUDEK. Zdroj pro vývoj v čase nebyl nalezen, jen dnešní hladinu 0,96 kWh/km (Oeko, regionální rozvoz). P50 0,85, P10 0,75, P90 1,0 v 2050, lineárně. Studie ICCT s vývojem do 2040 vrátily chybu 403 a nebyly přečteny. |
| 2030 | 0.9700 | 0.9500 | 1.0000 | D | ÚSUDEK. Zdroj pro vývoj v čase nebyl nalezen, jen dnešní hladinu 0,96 kWh/km (Oeko, regionální rozvoz). P50 0,85, P10 0,75, P90 1,0 v 2050, lineárně. Studie ICCT s vývojem do 2040 vrátily chybu 403 a nebyly přečteny. |
| 2040 | 0.9100 | 0.8500 | 1.0000 | D | ÚSUDEK. Zdroj pro vývoj v čase nebyl nalezen, jen dnešní hladinu 0,96 kWh/km (Oeko, regionální rozvoz). P50 0,85, P10 0,75, P90 1,0 v 2050, lineárně. Studie ICCT s vývojem do 2040 vrátily chybu 403 a nebyly přečteny. |
| 2050 | 0.8500 | 0.7500 | 1.0000 | D | ÚSUDEK. Zdroj pro vývoj v čase nebyl nalezen, jen dnešní hladinu 0,96 kWh/km (Oeko, regionální rozvoz). P50 0,85, P10 0,75, P90 1,0 v 2050, lineárně. Studie ICCT s vývojem do 2040 vrátily chybu 403 a nebyly přečteny. |

**Zdroj:** Le Corguillé, Hacker, Dolinga, Real-world data analysis of battery electric trucks operating in Germany, EVS38 (2025), https://www.oeko.de//fileadmin/oekodoc/Real-world-data-analysis-of-battery-electric-trucks-operating-in-Germany.pdf

**Citace:** „The average consumption is 0.96 kWh/km.“; nic k vývoji v čase

### teplo_budovy: Měrná potřeba tepla budov, index 2025 = 1

| Rok | Hodnota | P10 | P90 | Stupeň | Odvození |
|---|---|---|---|---|---|
| 2025 | 1.0000 | 1.0000 | 1.0000 | D | Základ 2025 lineárně z tabulky: (491 + 386) / 2 = 438.5 MJ/m2.rok. Tabulka je progresivní scénář, sám plán ho nazývá ideálním a počítá s dvojnásobnou mírou renovace. ÚSUDEK: P50 polovina poklesu, P90 čtvrtina poklesu. Hodnota je za celý fond budov ČR, pro MSK zvlášť není. |
| 2030 | 0.9401 | 0.8803 | 0.9701 | D | Základ 2025 lineárně z tabulky: (491 + 386) / 2 = 438.5 MJ/m2.rok. 2030: 386 / 438.5 = 0.8803 = P10. Tabulka je progresivní scénář, sám plán ho nazývá ideálním a počítá s dvojnásobnou mírou renovace. ÚSUDEK: P50 polovina poklesu, P90 čtvrtina poklesu. Hodnota je za celý fond budov ČR, pro MSK zvlášť není. |
| 2040 | 0.8330 | 0.6659 | 0.9165 | D | Základ 2025 lineárně z tabulky: (491 + 386) / 2 = 438.5 MJ/m2.rok. 2040: 292 / 438.5 = 0.6659 = P10. Tabulka je progresivní scénář, sám plán ho nazývá ideálním a počítá s dvojnásobnou mírou renovace. ÚSUDEK: P50 polovina poklesu, P90 čtvrtina poklesu. Hodnota je za celý fond budov ČR, pro MSK zvlášť není. |
| 2050 | 0.7805 | 0.5610 | 0.8903 | D | Základ 2025 lineárně z tabulky: (491 + 386) / 2 = 438.5 MJ/m2.rok. 2050: 246 / 438.5 = 0.5610 = P10. Tabulka je progresivní scénář, sám plán ho nazývá ideálním a počítá s dvojnásobnou mírou renovace. ÚSUDEK: P50 polovina poklesu, P90 čtvrtina poklesu. Hodnota je za celý fond budov ČR, pro MSK zvlášť není. |

**Zdroj:** Vnitrostátní plán, Tab.21 s.56, s.54-55

**Citace:** Tab.21 „Měrná potřeba tepla na vytápění [MJ/( m2.rok)] 491 386 292 246“ (2020, 2030, 2040, 2050); s.54 „ten představuje ideální scénář“; s.55 „zvýšením renovační míry na přibližně dvojnásobek“

### teplo_tc: Spotřeba na odběrné místo s tepelným čerpadlem, index 2025 = 1

| Rok | Hodnota | P10 | P90 | Stupeň | Odvození |
|---|---|---|---|---|---|
| 2025 | 1.0000 | 1.0000 | 1.0000 | D | Na odběrném místě s TČ topí jen část z 8,9 MWh. Běžná spotřeba 2,5 MWh je úsudek převzatý z dřívějšího řádku. Podíl 2.5 / 8,9 = 0.2809. teplo_tc = 0.2809 + (1 − 0.2809) × teplo_budovy = 1.0000. |
| 2030 | 0.9569 | 0.9139 | 0.9785 | D | Na odběrném místě s TČ topí jen část z 8,9 MWh. Běžná spotřeba 2,5 MWh je úsudek převzatý z dřívějšího řádku. Podíl 2.5 / 8,9 = 0.2809. teplo_tc = 0.2809 + (1 − 0.2809) × teplo_budovy = 0.9569. |
| 2040 | 0.8799 | 0.7597 | 0.9400 | D | Na odběrném místě s TČ topí jen část z 8,9 MWh. Běžná spotřeba 2,5 MWh je úsudek převzatý z dřívějšího řádku. Podíl 2.5 / 8,9 = 0.2809. teplo_tc = 0.2809 + (1 − 0.2809) × teplo_budovy = 0.8799. |
| 2050 | 0.8422 | 0.6843 | 0.9211 | D | Na odběrném místě s TČ topí jen část z 8,9 MWh. Běžná spotřeba 2,5 MWh je úsudek převzatý z dřívějšího řádku. Podíl 2.5 / 8,9 = 0.2809. teplo_tc = 0.2809 + (1 − 0.2809) × teplo_budovy = 0.8422. |

**Zdroj:** Dopadová studie s.113; Vnitrostátní plán, Tab.21 s.56, s.54-55

**Citace:** Dopadová studie s.113 „Spotřeba na jedno odběrné místo se ustálila na hodnotě 8,9 MWh“; s.122 „celkovým počtem odběrných míst 131 tis.“; Tab.26 922 979 MWh (2022)

### teplo_pt: Spotřeba na odběrné místo s přímotopem, index 2025 = 1

| Rok | Hodnota | P10 | P90 | Stupeň | Odvození |
|---|---|---|---|---|---|
| 2025 | 1.0000 | 1.0000 | 1.0000 | D | 922 979 MWh / 131 000 OM = 7.0456 MWh/OM; běžná spotřeba 2,5 MWh (úsudek), podíl 2,5 / 7.0456 = 0.3548. teplo_pt = 0.3548 + (1 − 0.3548) × teplo_budovy = 1.0000. |
| 2030 | 0.9614 | 0.9228 | 0.9807 | D | 922 979 MWh / 131 000 OM = 7.0456 MWh/OM; běžná spotřeba 2,5 MWh (úsudek), podíl 2,5 / 7.0456 = 0.3548. teplo_pt = 0.3548 + (1 − 0.3548) × teplo_budovy = 0.9614. |
| 2040 | 0.8923 | 0.7844 | 0.9461 | D | 922 979 MWh / 131 000 OM = 7.0456 MWh/OM; běžná spotřeba 2,5 MWh (úsudek), podíl 2,5 / 7.0456 = 0.3548. teplo_pt = 0.3548 + (1 − 0.3548) × teplo_budovy = 0.8923. |
| 2050 | 0.8584 | 0.7168 | 0.9292 | D | 922 979 MWh / 131 000 OM = 7.0456 MWh/OM; běžná spotřeba 2,5 MWh (úsudek), podíl 2,5 / 7.0456 = 0.3548. teplo_pt = 0.3548 + (1 − 0.3548) × teplo_budovy = 0.8584. |

**Zdroj:** Dopadová studie s.122, Tab.26; Vnitrostátní plán, Tab.21 s.56, s.54-55

**Citace:** Dopadová studie s.113 „Spotřeba na jedno odběrné místo se ustálila na hodnotě 8,9 MWh“; s.122 „celkovým počtem odběrných míst 131 tis.“; Tab.26 922 979 MWh (2022)

### d_auta: Kombinovaný vliv pro osobní auta

| Rok | Hodnota | P10 | P90 | Stupeň | Odvození |
|---|---|---|---|---|---|
| 2025 | 1.0000 | 1.0000 | 1.0000 | D | d_auta = pop_msk × auta_na_os × eff_auta = 1.0000 × 1.0000 × 1.0000 = 1.0000. Proběh na auto zůstává 13,5 tis. km. |
| 2030 | 0.9335 | 0.8774 | 1.0010 | D | d_auta = pop_msk × auta_na_os × eff_auta = 0.9622 × 1.0310 × 0.9410 = 0.9335. Proběh na auto zůstává 13,5 tis. km. |
| 2040 | 0.8131 | 0.6614 | 1.0095 | D | d_auta = pop_msk × auta_na_os × eff_auta = 0.9040 × 1.0929 × 0.8230 = 0.8131. Proběh na auto zůstává 13,5 tis. km. |
| 2050 | 0.6879 | 0.4578 | 1.0049 | D | d_auta = pop_msk × auta_na_os × eff_auta = 0.8449 × 1.1548 × 0.7050 = 0.6879. Proběh na auto zůstává 13,5 tis. km. |

**Zdroj:** viz pop_msk, auta_na_os, eff_auta

**Citace:** viz vstupní vlivy v odvozeni

### d_nakladni: Kombinovaný vliv pro nákladní dopravu

| Rok | Hodnota | P10 | P90 | Stupeň | Odvození |
|---|---|---|---|---|---|
| 2025 | 1.0000 | 1.0000 | 1.0000 | D | d_nakladni = eff_nakladni = 1.0000. Objem přepravy držen na 1, směr v MSK není jasný (tab. 17.1: přeprava v kraji 30 713 tis. t v 2022, 27 728 tis. t v 2024), demografie se nepoužívá. |
| 2030 | 0.9700 | 0.9500 | 1.0000 | D | d_nakladni = eff_nakladni = 0.9700. Objem přepravy držen na 1, směr v MSK není jasný (tab. 17.1: přeprava v kraji 30 713 tis. t v 2022, 27 728 tis. t v 2024), demografie se nepoužívá. |
| 2040 | 0.9100 | 0.8500 | 1.0000 | D | d_nakladni = eff_nakladni = 0.9100. Objem přepravy držen na 1, směr v MSK není jasný (tab. 17.1: přeprava v kraji 30 713 tis. t v 2022, 27 728 tis. t v 2024), demografie se nepoužívá. |
| 2050 | 0.8500 | 0.7500 | 1.0000 | D | d_nakladni = eff_nakladni = 0.8500. Objem přepravy držen na 1, směr v MSK není jasný (tab. 17.1: přeprava v kraji 30 713 tis. t v 2022, 27 728 tis. t v 2024), demografie se nepoužívá. |

**Zdroj:** viz eff_nakladni; ČSÚ, Statistická ročenka Moravskoslezského kraje 2025, tab. 17.1, 17.102 a 27.102 (zdroj dat Ministerstvo dopravy), https://csu.gov.cz/produkty/statisticka-rocenka-moravskoslezskeho-kraje-2025

**Citace:** viz vstupní vlivy v odvozeni

### d_vytapeni: Kombinovaný vliv pro vytápění tepelnými čerpadly

| Rok | Hodnota | P10 | P90 | Stupeň | Odvození |
|---|---|---|---|---|---|
| 2025 | 1.0000 | 1.0000 | 1.0000 | D | d_vytapeni = d_domacnosti × teplo_tc = 1.0000 × 1.0000 = 1.0000. |
| 2030 | 0.9463 | 0.8960 | 0.9736 | D | d_vytapeni = d_domacnosti × teplo_tc = 0.9889 × 0.9569 = 0.9463. |
| 2040 | 0.8656 | 0.7289 | 0.9425 | D | d_vytapeni = d_domacnosti × teplo_tc = 0.9838 × 0.8799 = 0.8656. |
| 2050 | 0.8228 | 0.6355 | 0.9377 | D | d_vytapeni = d_domacnosti × teplo_tc = 0.9770 × 0.8422 = 0.8228. |

**Zdroj:** viz d_domacnosti, teplo_tc

**Citace:** viz vstupní vlivy v odvozeni

### d_primotopy: Kombinovaný vliv pro přímotopy

| Rok | Hodnota | P10 | P90 | Stupeň | Odvození |
|---|---|---|---|---|---|
| 2025 | 1.0000 | 1.0000 | 1.0000 | D | d_primotopy = d_domacnosti × teplo_pt = 1.0000 × 1.0000 = 1.0000. Zjednodušení ponechané záměrně: počet domácností se násobí i na 35 % řádku od podnikatelů. |
| 2030 | 0.9507 | 0.9040 | 0.9764 | D | d_primotopy = d_domacnosti × teplo_pt = 0.9889 × 0.9614 = 0.9507. Zjednodušení ponechané záměrně: počet domácností se násobí i na 35 % řádku od podnikatelů. |
| 2040 | 0.8778 | 0.7504 | 0.9504 | D | d_primotopy = d_domacnosti × teplo_pt = 0.9838 × 0.8923 = 0.8778. Zjednodušení ponechané záměrně: počet domácností se násobí i na 35 % řádku od podnikatelů. |
| 2050 | 0.8387 | 0.6617 | 0.9493 | D | d_primotopy = d_domacnosti × teplo_pt = 0.9770 × 0.8584 = 0.8387. Zjednodušení ponechané záměrně: počet domácností se násobí i na 35 % řádku od podnikatelů. |

**Zdroj:** viz d_domacnosti, teplo_pt

**Citace:** viz vstupní vlivy v odvozeni

### d_chlazeni: Kombinovaný vliv pro chlazení

| Rok | Hodnota | P10 | P90 | Stupeň | Odvození |
|---|---|---|---|---|---|
| 2025 | 1.0000 | 1.0000 | 1.0000 | D | Domácnosti 81 z 193 GWh, zbytek jsou služby bez vlivu. d_chlazeni = 81 / 193 × d_domacnosti + 112 / 193 = 0.4197 × 1.0000 + 0.5803 = 1.0000. Vážený součet, ne součin, váhy z progresivní 2050. Oteplování zůstává v podílu chlazených domácností. |
| 2030 | 0.9953 | 0.9833 | 1.0028 | D | Domácnosti 81 z 193 GWh, zbytek jsou služby bez vlivu. d_chlazeni = 81 / 193 × d_domacnosti + 112 / 193 = 0.4197 × 0.9889 + 0.5803 = 0.9953. Vážený součet, ne součin, váhy z progresivní 2050. Oteplování zůstává v podílu chlazených domácností. |
| 2040 | 0.9932 | 0.9579 | 1.0159 | D | Domácnosti 81 z 193 GWh, zbytek jsou služby bez vlivu. d_chlazeni = 81 / 193 × d_domacnosti + 112 / 193 = 0.4197 × 0.9838 + 0.5803 = 0.9932. Vážený součet, ne součin, váhy z progresivní 2050. Oteplování zůstává v podílu chlazených domácností. |
| 2050 | 0.9903 | 0.9319 | 1.0313 | D | Domácnosti 81 z 193 GWh, zbytek jsou služby bez vlivu. d_chlazeni = 81 / 193 × d_domacnosti + 112 / 193 = 0.4197 × 0.9770 + 0.5803 = 0.9903. Vážený součet, ne součin, váhy z progresivní 2050. Oteplování zůstává v podílu chlazených domácností. |

**Zdroj:** viz d_domacnosti; řádek chlazení

**Citace:** viz vstupní vlivy v odvozeni

### Co u vlivů zůstává úsudkem

- Meze počtu obyvatel, protože ČSÚ dává kraji jednu variantu.
- Velikost domácnosti: projekce domácností neexistuje, počet domácností je odvozený.
- Auta na osobu: dorovnání na dnešní Česko 0,6098 z 0,5280. Tento vliv zvyšuje spotřebu a je největší úsudek v řádku aut.
- Teplo: P50 je polovina poklesu z Vnitrostátního plánu, protože plán svůj scénář sám nazývá ideálním. Celý pokles je P10.
- Nákladní auta: vývoj spotřeby je čistý odhad, zdroj nebyl nalezen.
- Běžná spotřeba 2,5 MWh na odběrné místo, převzatá z dřívějšího řádku.

Bez vlivu zůstávají služby, vlaky, MHD a ostatní řádky, kde vliv nesedí jasně. Bez vlivu zůstává i proběh na auto. Spotřebiče domácností jsou v řádku úspory.

## 7. Velké události

Rok je uveden jako P10, P50 a P90. Svislá značka v grafu na stránce je na P50.

| Událost | Položka | Cesta | P10 | P50 | P90 |
|---|---|---|---|---|---|
| Konec Elektrárny Dětmarovice | černé uhlí: Dětmarovice | progresivní | 2026 | 2026 | 2026 |
| Konec Elektrárny Dětmarovice | černé uhlí: Dětmarovice | konzervativní | 2026 | 2026 | 2026 |
| Konec uhlí v teplárnách | černé uhlí: teplárny a průmysl | progresivní | 2029 | 2030 | 2033 |
| Konec uhlí v teplárnách | černé uhlí: teplárny a průmysl | konzervativní | 2030 | 2032 | 2036 |
| Konec hnědého uhlí | hnědé uhlí | progresivní | 2028 | 2030 | 2033 |
| Konec hnědého uhlí | hnědé uhlí | konzervativní | 2029 | 2031 | 2035 |
| Třinec: první oblouková pec, méně hutních plynů | hutní plyny (vysokopecní a koksárenský) | progresivní | 2030 | 2033 | 2040 |
| Třinec: první oblouková pec, méně hutních plynů | hutní plyny (vysokopecní a koksárenský) | konzervativní | 2030 | 2033 | 2040 |
| Spuštění SMR | SMR | progresivní | 2040 | 2045 | 2055 |
| Spuštění ZEVO | energetické využití odpadu | progresivní | 2030 | 2031 | 2036 |
| Spuštění ZEVO | energetické využití odpadu | konzervativní | 2031 | 2034 | 2040 |
| Třinec: první oblouková pec | Třinecké železárny | progresivní | 2030 | 2033 | 2040 |
| Třinec: první oblouková pec | Třinecké železárny | konzervativní | 2030 | 2033 | 2040 |
| Nová huť: oblouková pec | Nová huť | progresivní | 2031 | 2034 | 2042 |
| Nová huť: oblouková pec | Nová huť | konzervativní | 2031 | 2034 | 2045 |
| Konec těžby OKD (ČSM) | doly | progresivní | 2026 | 2026 | 2027 |
| Konec těžby OKD (ČSM) | doly | konzervativní | 2026 | 2026 | 2027 |

SMR má událost jen v progresivní cestě, konzervativní cesta ho nemá. Roky jsou zčásti úsudek, u každé položky to říká pole Odhad a Poznámka v části 5.

## 8. Sezónnost vodíku

Tato část platí pro progresivní cestu v roce 2050. Výpočet je měsíční a přibližný.

**Výsledek.** V měsíční tabulce při výchozích hodnotách není v létě žádný měsíční přebytek, a to ani bez vodíku. Podle ní nelze vodík flotily vyrobit z letního přebytku kraje. Jeho elektřina by musela přijít ze sítě mimo kraj nebo z vyšší výroby. Měsíc s nejmenším schodkem je srpen, bilance bez vodíku -22.8322 GWh.

**Vztah k letnímu poledni.** Tabulka v části 3 ukazuje v progresivní cestě 2050 polední přebytek 524.5 MW. Po bateriích a elektrokotlích z něj zbývá 279.5 MW z potřebných 1166.7 MW. Měsíční výsledek a polední výsledek si neodporují. Měsíční data krátké přebytky neukazují a polední přebytek roční objem vodíku nepokryje.

**Starší roční součty.** Měsíční tabulka vychází z ročního součtu výroby 8331.8120 GWh a spotřeby s vodíkem 14332.4000 GWh (odvozený součet tří hodnot: spotřeba bez vodíku, vodík flotily a 45.8 GWh vodíku mimo flotilu). Aktuální součty v části 3 jsou 8331.812 a 14332.4 GWh. Rozdíl tabulky proti aktuálním součtům je 0 GWh u výroby a 0 GWh u spotřeby (odvozené rozdíly). Přepočet by schodky mírně prohloubil, takže závěr o chybějícím přebytku při výchozích hodnotách platí. Čísla níže nejsou přepočítána.

### Měsíční tabulka, GWh

| Měsíc | SMR | FVE | Vítr | Ostatní | Výroba | Spotřeba bez vodíku | Bilance bez vodíku | Vodík rovnoměrně | Bilance s vodíkem |
|---|---|---|---|---|---|---|---|---|---|
| leden | 334.8000 | 47.6863 | 221.4841 | 77.7388 | 681.7093 | 1037.2363 | -355.5270 | 293.3704 | -648.8974 |
| únor | 302.4000 | 87.9249 | 100.5610 | 70.2157 | 561.1017 | 916.4095 | -355.3079 | 264.9797 | -620.2876 |
| březen | 334.8000 | 154.1550 | 149.5958 | 77.7388 | 716.2896 | 971.1588 | -254.8692 | 293.3704 | -548.2396 |
| duben | 324.0000 | 205.3427 | 167.2988 | 75.2311 | 771.8726 | 886.5783 | -114.7057 | 283.9068 | -398.6126 |
| květen | 334.8000 | 204.2541 | 103.3095 | 77.7388 | 720.1024 | 882.4138 | -162.3114 | 293.3704 | -455.6818 |
| červen | 324.0000 | 249.6958 | 111.7783 | 75.2311 | 760.7052 | 859.1441 | -98.4389 | 283.9068 | -382.3457 |
| červenec | 334.8000 | 216.7171 | 97.0901 | 77.7388 | 726.3460 | 828.0133 | -101.6672 | 293.3704 | -395.0376 |
| srpen | 334.8000 | 245.4230 | 96.1944 | 77.7388 | 754.1563 | 776.9885 | -22.8322 | 293.3704 | -316.2026 |
| září | 324.0000 | 141.6589 | 138.7360 | 75.2311 | 679.6260 | 810.3877 | -130.7617 | 283.9068 | -414.6686 |
| říjen | 334.8000 | 111.6528 | 179.4937 | 77.7388 | 703.6853 | 948.1665 | -244.4812 | 293.3704 | -537.8516 |
| listopad | 324.0000 | 63.0298 | 186.1768 | 75.2311 | 648.4377 | 958.1882 | -309.7505 | 283.9068 | -593.6574 |
| prosinec | 334.8000 | 36.4595 | 158.7815 | 77.7388 | 607.7799 | 957.7151 | -349.9352 | 293.3704 | -643.3056 |
| rok | 3942.0000 | 1764.0000 | 1710.5000 | 915.3120 | 8331.8120 | 10832.4000 | -2500.5880 | 3454.2000 | -5954.7880 |

### Předpoklady a citlivost

Data: ERÚ čtvrtletní zprávy 2025, oddíl 7.8. Technologie dávají 2 805 163,5 MWh, netto spotřeba 5 963 818,3 MWh, obojí sedí na tab. 6.1 a 6.2. Rozsah 7.8 je netto, používá se jen tvar. Měsíce jsou v měsíční tabulce (část 8).

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

Vodík v případech P90 přebytek po odečtení rovnoměrného zatížení vyčerpá na nulu. Měsíční data neukazují krátké přebytky: polední slunce při nízké spotřebě nebo větrné dny mohou přebytek dát i v měsíci se schodkem. Velikost těchto přebytků z dat nelze zjistit, potřebný by byl hodinový profil. Výsledek také neříká nic o přebytcích mimo kraj.

Sezónní zásobník, hypotéza pro případ výroby jen v létě a rovnoměrné spotřeby, odvozeno:
- Výroba duben až září, 4 392 hodin. Zásoba 67 856 t × (1 − 4 392 / 8 760) = 33 835 t, 1 126,7 GWh při 33,3 kWh/kg.
- Objem 1,45 mil. m³ při 350 bar a 23,3 kg/m³, 0,87 mil. m³ při 700 bar a 39 kg/m³. Hustoty nejsou z podkladů, ověřit.
- Příkon elektrolyzérů 3 454,2 GWh / 4 392 h = 786,5 MW, tedy víc než SMR 500 MW. Toto zatížení by letní schodek prohloubilo.
- Výroba jen květen až srpen, 2 952 hodin: 44 990 t, 1 170,1 MW.

### Řádky vodíku a flotily v progresivní cestě, GWh

| Položka | P10 2050 | P50 2050 | P90 2050 | Stupeň |
|---|---|---|---|---|
| osobní auta | 230.0 | 493.8 | 721.3 | D |
| nákladní doprava | 234.4 | 558.6 | 657.2 | D |
| MHD | 11.9 | 11.9 | 33.9 | D |
| výroba vodíku: osobní auta | 824.2 | 1494.6 | 2295.2 | D |
| výroba vodíku: nákladní doprava | 884.5 | 1925.0 | 2958.5 | D |
| výroba vodíku: MHD | 16.1 | 34.6 | 103.1 | D |
| výroba vodíku | 20 | 45.8 | 260.4 | B |

Odvozený součet P50 tří řádků vodíku flotily je 3454.2 GWh. Výpočet: vozidla × km × kg H2/100 km × kWh/kg. Elektřina na vodík flotily odpovídá 67 856 t H2 za rok. Konzervativní cesta má v nových řádcích nulu.

### Vstupy výpočtu vodíku

| Vstup | P50 | P10 až P90 | Zdroj |
|---|---|---|---|
| Osobní auto dnes, kg/100 km | 1,0 | 0,79 až 1,10 | úsudek; h2.live 0,76; WLTP 0,79 až 0,89 a skutečnost 1,1 jen ze souhrnu vyhledávače |
| Těžké auto dnes, kg/100 km | 9,0 | 7,5 až 10,8 | ICCT 2022 jen ze souhrnu vyhledávače, model; XCIENT 7,5 |
| Autobus dnes, kg/100 km | 7,49 | 5,6 až 9,1 | JIVE 2, CORDIS; 9,1 jen ze souhrnu vyhledávače |
| Zlepšení vozidla do 2050 | 0,705 auta, 0,85 ostatní | viz řídicí vlivy (část 6) | eff_auta (Krause platí pro BEV i FCHEV), eff_nakladni (úsudek) |
| Elektrolyzér dnes, kWh/kg | 55 | | Dopadová studie s.119, DOE stav 2022 |
| Elektrolyzér 2050, kWh/kg | 48,26 | 46 až 55 | 33,3 / 0,69, IEA; DOE konečný cíl; Dopadová studie |
| Komprese, kWh/kg | 3,2 pro 700 bar, 2,23 pro 350 bar | 1,7 až 6,4 a 1,7 až 4 | DOE záznam 9013 z roku 2009 |

### Volby modelu k flotile

- 50 % se bere z celé flotily, takže P50 2050 má 100 % čistých aut místo dřívějších 95 %.
- Ve 2040 je vodík třetina čistých vozidel. Je to úsudek. Z toho plyne strmý růst: u aut z 92 704 vozidel v 2040 na 305 169 v 2050.
- Vozokilometry nákladní dopravy: 1 314,4 GWh / 1,3187 kWh/km = 996,8 mil. km. Hodnota 1,3187 je Oeko přepočtené na 40 t, aby seděla k 9 kg/100 km pro tutéž soupravu. S 0,96 kWh/km by P50 vyšlo o 37,4 % víc, to je zahrnuto v P90.
- MHD obsahuje tramvaje, 50 % se bere z celého řádku. Je to záměrné zjednodušení, P50 baterií proto klesá pod základ 19,464.

## 9. Volby modelu

Čísla jsou stálá označení voleb a ostatní části na ně odkazují. Pořadí odpovídá rejstříku voleb. Čísla 18 a 19 chybí, protože se týkají jen grafiky a zveřejnění stránky.

| Č. | Volba modelu | Důvod |
|---|---|---|
| 1 | Pásmo je 80 % (P10 až P90). | Širší pásmo by u odhadů předstíralo přesnost, která není k dispozici. |
| 2 | Chybějící odborné odhady jsou vstupy stupně D a zatím je nikdo nezávisle neověřil. | Bez nich by pásmo nešlo spočítat. Stupeň D je v tabulce vidět. |
| 3 | Procenta konzervativní cesty jsou středové hodnoty pro rok 2050 vůči progresivní cestě. Mají vlastní nejistotu. | Pevný násobek by nejistoty cest úplně svázal. |
| 4 | Plyn v konzervativní cestě je 90 % zemní plyn a 10 % syntetický. CNG/LPG se pro výrobu elektřiny čte jako zemní plyn. | Procenta jsou součást definice cesty, čtení paliva je výklad modelu. |
| 5 | „Vytápění 300 %“ se čte jako energie na vstupu při stejném teple, ne jako elektřina. Elektřina odpovídá jen části vytápění, která je v konzervativní cestě elektrická. | Trojnásobek odpovídá přechodu z tepelných čerpadel na spalování nebo přímý ohřev. Doslovné čtení by dalo konzervativní cestě víc elektřiny na teplo než elektrifikované. Výklad není nezávisle potvrzen. |
| 6 | SMR je v progresivní cestě 500 MW, v konzervativní není. Rok spuštění je nejistý. | Je to součást definice cest. |
| 7 | Odpad 300 tisíc tun za rok není vstup cesty. Položka využití odpadu vychází z jiných zdrojů. | Údaj je jen orientační poznámka v pracovních podkladech. |
| 8 | Výroba je výroba brutto z ERÚ, tabulka 6.1. | Je k dispozici po krajích a technologiích. |
| 9 | Spotřeba je součet sektorů z ERÚ, tabulka 6.3, plus ztráty v sítích jako položka. | Tabulka 6.3 má sektory a sedí na ČSÚ, viz níže. Tabulka 6.2 je o 879 GWh nižší a neobsahuje vše. |
| 10 | Výchozí rok je 2025. Rok 2026 se do křivek nebere, známe jen pololetí. | Celý rok 2026 by byl odhad. |
| 11 | Agregace je Monte Carlo s 10 000 běhy a pevným semínkem. Jedna položka drží v čase stejný kvantil. | Výsledek jde zopakovat a křivka položky v běhu neskáče. |
| 12 | Společné faktory jsou tempo elektrifikace, tempo povolování a cena energií. | Položky se stejnou příčinou se hýbou spolu. |
| 13 | Velké události mají v grafu svislou značku na mediánovém roce. | Rok události má být v grafu čitelný. |
| 14 | Hlavní graf je roční energie. Graf zimní špičky v MW následuje až po kontrole ročních křivek. | Špička z ročních hodnot přímo neplyne a potřebuje vlastní postup. |
| 15 | Seznam položek je podle metodiky. Položka bez měřitelného vlivu může mít hodnotu nula, ale zůstává v tabulce. | Je vidět, že se na ni nezapomnělo. |
| 16 | Stránka je jeden offline soubor. Posuvník nastavuje hodnotu položky v roce 2050, výchozí je P50 a průběh položky se přeškáluje. | První verze je minimalistická, další prvky přibývají postupně. |
| 17 | Pásmo součtů platí jen pro výchozí nastavení. Po změně posuvníku se ukáže vlastní křivka vedle výchozí. | Pásmo pro vlastní nastavení by vyžadovalo nový výpočet. |
| 20 | Hlavním zdrojem výchozích hodnot je Dopadová studie. Každá výchozí hodnota má stranu v PDF a doslovnou citaci, aby ji šlo ručně zkontrolovat. Jiný zdroj jen tam, kde studie hodnotu nemá. | Každá hodnota má jít zkontrolovat proti studii. |
| 21 | V hlavním grafu lze vypínat každou cestu a výrobu nebo spotřebu. Aspoň jedna volba ve dvojici zůstává zapnutá. | Graf má jít zúžit na jednu cestu nebo stranu bilance. |
| 22 | Každá velká událost má posuvník roku od 2026 do 2050. Položky se stejnou událostí sdílejí rok. | Pec v Třinci snižuje hutní plyny a zvyšuje spotřebu ve stejném roce. |
| 23 | Stránka má jednoduchou a podrobnou verzi, výchozí je jednoduchá. V jednoduché jsou skupiny položek a posuvník skupiny mění položky ve stejném poměru vůči výchozím hodnotám. Přepíše tím ruční nastavení položek dané skupiny. | Stejný poměr zachová výchozí skladbu skupiny. |
| 24 | Průběh všech položek je jeden vzorec z části 4. Podrobná verze má u plynulých položek i rok poloviny změny. | Všechny položky se tak počítají stejným postupem. |
| 25 | Nejistota roku poloviny změny je u plynulých položek P10 až P90 o 3 roky kolem výchozího roku a nezávisí na společných faktorech. Společný faktor má korelaci 0,6. | Vlastní odhad bez zdroje. Bez nejistoty načasování by pásmo v letech před 2050 bylo příliš úzké. |
| 27 | V progresivní cestě je v roce 2050 flotila 50 % vodík a 50 % baterie. Flotilou rozumíme osobní auta, nákladní dopravu a MHD, vlaky zůstávají na trolejích. Vodík se vyrábí v kraji z elektřiny a tato elektřina se počítá do spotřeby. Vodík se nevrací zpět na elektřinu. Konzervativní cesta zůstává na bateriích. | Podíl je součást definice cesty, rozsah flotily a konzervativní cesta jsou výklad modelu. |
| 28 | Ze studie ZEVO jsou veřejně jen čísla potřebná k výpočtu: výroba, množství odpadu a rok spuštění. Stránka i export uvádějí, že část zdroje je neveřejná. | Studie je pracovní verze a není veřejná. |
| 29 | Hlavní graf má přepínač Roční energie, Zimní špička a Letní poledne. Výkon v MW se počítá z ročních hodnot a koeficientů položek, bez pásma. | Sčítání mezí koeficientů by pásmo přehnalo. |
| 30 | Nad posuvníky položek je přepínač a posuvníky velkých trendů: obyvatelé, auta na obyvatele, účinnost aut, potřeba tepla budov a počet domácností. Změna trendu se přičítá rovnoměrně od roku 2025. Pásmo se nepřepočítává. | Výchozí křivka zůstává přesně podle tabulky. |
| 31 | Syntetický plyn je z odpadu, elektřina na jeho výrobu je nula. Množství omezuje dostupný odpad po odečtení spalovny. Jiné zdroje, například důlní nebo koksárenský plyn, nejsou započítané, protože chybí podklad. | Účinnosti přeměny jsou odhad modelu. |
| 32 | Přepínač „Dorovnat na soběstačnost“ ukazuje schodek a kolik fotovoltaiky nebo větru by ho pokrylo. Výchozí hodnoty položek se nemění, jde o přepočet. | Soběstačnost je zde roční bilance, ne pokrytí v každé hodině. |
| 33 | SMR se na stránce nastavuje počtem modulů po 500 MW, od 0 do 4. Výchozí je 1 v progresivní cestě a 0 v konzervativní. Jeden modul je 3 942 GWh za rok. Rok spuštění je společný pro všechny moduly. | Výpadek největšího bloku model nepočítá. |
| 34 | Stránka má záložku Nedostatky se známými problémy, chybějícími podklady a volbami bez opory ve zdrojích. | Je to součást definice cest. |
| 35 | Záměr vodíku: přebytek, který se nevejde do baterie, vyrábí vodík pro dopravu a energie zůstává v kraji. Vodík uskladněný v létě sníží výrobu vodíku v zimě, a tím zlepší zimní bilanci. Baterie je krátkodobá a její velikost se určí podle toho, kde se ještě vyplatí. Hodinový model tento postup počítá. | Velikost přebytku je nutné ověřit výpočtem. |
| 26 | Hodnoty tabulky pro roky 2030 a 2040 už neurčují křivku přímo, jen z nich dopočítáme k a t_m. Kde to nesedí o více než 10 % a 25 GWh, je to v seznamu selhání proložení v části 4. | Přesné proložení není u každé položky možné. |

### Vyřešený rozpor: spotřeba 2024

ČSÚ uvádí pro MSK 6 809,0 GWh a součet tabulky 6.2 ERÚ dával 5 931,2 GWh. Součet tabulky 6.3 ERÚ dává 6 810,2 GWh, tedy skoro totéž co ČSÚ. Tabulka 6.2 má jiný rozsah než 6.3. Přesný důvod zbývajícího rozdílu 1,2 GWh není ověřen.

## 10. Rozpory ve zdrojích a co není zjištěno

### Rozpory, doslovně

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

Rozpor s hlavním zdrojem: Dopadová studie s.137 píše „nelze předpokládat významnou demografickou změnu“, ČSÚ dává pokles o 15,5 % do 2050. Studie to uvádí jen u odpadu, číslo nedává.

Rozpor se zdroji: Dopadová studie s.119 píše, že v osobní a železniční dopravě „jsou tyto projekty spíše utlumovány“. Vnitrostátní plán, tištěná s.46 čeká, že „u osobních automobilů zřejmě převáží elektromobilita“. Polovina osobních aut na vodík je tedy volba modelu, ne závěr zdrojů.

Studie ZEVO uvádí spuštění v lednu 2030 i v lednu 2031, model proto pracuje s nejistým rokem spuštění.

Procenta konzervativní cesty, která nejdou použít čistě: OZE 10 % (čteno jako nárůst nad stav 2026), síť dvojnásobná zátěž (vyšší míra ztrát), vytápění 300 % (volba modelu č. 5), MHD 80 % (hodnota vychází pod základ, ponecháno doslovně).

### Rozsah 7 090 GWh proti tabulce 6.3

Hodnota 7 090 GWh a tabulka 6.3 ERÚ jsou stejná řada. Dopadová studie Tab. 6 s. 40 (7 090 283,3 MWh, 2023) a ERÚ 6.3 za 2023 Q1, Q2, Q4 dávají 5 438 907,3 MWh. Zbývá 1 651 376,0 MWh na Q3, což je věrohodné proti Q2 a Q4 (1 739 196,9 a 1 760 864,5), a odpovídá to i po sektorech (Průmysl 802,3, Energetika 253,2 GWh). Sezónnost sedí: Q3/Q2 je v 2024 0,949 a dopočtené v 2023 0,950. Přímý důkaz chybí, protože zpráva za Q3 2023 v podkladech není. ERÚ Roční zpráva 2025 (4.6.8) uvádí 2023 netto 5 805 315,2 MWh, takže Dopadová studie Tab. 1 a Obr. 28 a 38 patří k řadě 6.2. Pokles z 7 090 na 6 810 GWh je tedy skutečná změna ve stejné řadě.
Dopadová studie s. 40: sektorový pohled „zahrnuje kromě spotřeby podle kategorizace spotřeb navíc spotřebu provozovatelů přenosové a distribuční soustavy, lokální spotřebu a technologickou vlastní spotřebu“. Studie sama počítá bilanci z užšího čísla 5 805,4 GWh, takže její výhledy (Obr. 28, 38) jsou na jiné bázi než tab. 6.3.

### Energetika a Průmysl v roce 2025

Vypadá to na přeřazení, ne na reálnou změnu, ale ERÚ to nikde neuvádí a v jeho zprávách není nalezena poznámka k metodice.

- Skok v 2025 Q2 proběhl současně v MSK, Olomouckém (16,6 na 42,2 GWh), Plzeňském (15,2 na 26,2) a Středočeském kraji (97,9 na 162,8) a celostátně (997,9 na 1 281,0). Průmysl v týchž krajích klesl.
- V MSK je součet Průmysl + Energetika plynulý: 2024 Q2 1 043,7, 2025 Q2 1 021,0. Hladina se drží i v 2026 (364,8 a 361,4).
- Roční zpráva: Energetika +706,1 GWh, Průmysl −941,6 GWh celostátně.
- Důsledek: rok 2025 míchá jedno čtvrtletí před skokem a tři po něm. Průmysl a Energetika jsou v základu spolehlivé jen jako součet. Nepotvrzeno. Rozhodne dotaz na ERÚ.

### Co se zavřelo

| Pokles PE v MSK | Co sedí | Důkaz |
|---|---|---|
| březen 2025, 1 296,2 na 1 067,2 MW (−229,0) | TAMEH Ostrava 229 MW | shoda výkonu s Dopadovou studií Tab. 18; ERÚ jméno neuvádí |
| březen 2026, 1 073,2 na 473,2 MW (−600,0) | Elektrárna Dětmarovice, tři bloky 200 MW | shoda výkonu s Tab. 18; web o konci uhlí |

Pokles je jeden krok v březnu 2026, ne mezi prosincem a červnem. ERÚ neudává jméno elektrárny, takže jde o odvození. Výroba: Český rozhlas (12. 6. 2025) píše, že ČEZ „definitivně zastavila výrobu elektřiny z černého uhlí“, ERÚ odebírá výkon o rok později. Výroba Dětmarovic v 2025 je odhadnuta na 360,8 GWh z rozdílu leden až březen 2025 a 2026.

### Stav v regionu

- Nová huť: převzata 1. 10. 2025, oblouková pec do 1,5 mil. t ve fázi přípravy, vysoké pece stojí. Spotřebu zdroje neuvádějí.
- Třinec: pec odložena na nejdříve 2030 (Novinky 23. 4. 2025), v srpnu 2026 bez nového data. Elektřina: „zvýšení spotřeby elektřiny o 30 procent na 1 TWh ročně“ (Ekonomický deník 30. 1. 2025).
- Datacentra: projekt v MSK s výkonem a stavem nebyl nalezen. Gigafactory v Dolní Lutyni se stavět nebude.
- SMR: Dětmarovice jsou zmiňovaná varianta, lokalita není vybraná, první SMR ČEZ je v Temelíně.

### Co není zjištěno

- Spotřeba Nové hutě, dolů a chemie. Výroba Dětmarovic v 2025. Definice sektoru Energetika u ERÚ. Ztrátová sazba přímo za MSK. Trakční elektřina železnice v MSK.
- Nezjištěno: vývoj spotřeby těžkých nákladních aut (studie ICCT nešly otevřít), údaje starších edic projekce ČSÚ (jen souhrn vyhledávače), hodnota 2025 v řadě aut na osobu (bráno 2024), objem nákladní přepravy do 2050.
- Nezjištěno: účel 45 760 MWh, protože odkaz [45] v Dopadové studii vede na nesouvisející dokument a Strategie MSK 2021 nebyla nalezena. Počet nákladních aut a autobusů v MSK. Podíl tramvají v Tab. 23. Hodinové přebytky. Místo pro sezónní zásobník v kraji.

## 11. Otevřené otázky

1. **Znamená syntetický plyn plyn z odpadu?** Pracovní definice progresivní cesty má u plynu „náhrada zemního plynu za syntetický- využívání odpadu“. Model to čte jako plyn z odpadu (volba modelu č. 31). Syntetický plyn se vyrábí z odpadu, ne z elektřiny. Dostupný odpad je 360 000 t za rok (Dopadová studie, s. 137) minus 120 000 t pro spalovnu. Výroba elektřiny v roce 2050 je 231.0 GWh místo 866,0 GWh a konzervativně místo 240,5 GWh. Spotřeba elektřiny na výrobu plynu je nula místo 1 076,4 a 397,5 GWh. Jiné zdroje syntetického plynu, například důlní nebo koksárenský plyn, nejsou započítané, protože chybí podklad. Řádek výroba syntetického plynu má proto v progresivní cestě P50 2050 0 GWh a řádek syntetický plyn z odpadu 231.0 GWh se stupněm D. Otevřené zůstává, zda je toto čtení správné, a účinnosti přeměny jsou odhad bez zdroje.
2. **Co s vodíkem, když není letní přebytek (část 8)?** Možnosti jsou čtyři. Nechat řádky beze změny a rozpor uvést. Postavit více zdrojů. Část vodíku dovézt. Snížit podíl vodíku ve flotile. Model žádnou z nich nevybírá.
3. **Možný překryv 45,8 GWh s vodíkem flotily.** Dopadová studie neříká, pro koho je 45 760 MWh. Není to tedy prokazatelně vodík flotily a řádek výroba vodíku zůstává. Překryv nelze vyloučit a nejvýš je to 45,8 GWh. Odkaz [45] ve studii vede na nesouvisející dokument.
4. **Vlastní spotřeba zařízení ZEVO není přičtena.** Výroba 44.212 GWh je brutto a obsahuje vlastní spotřebu 12 600 MWh. Řádek vlastní spotřeba zdrojů tuto hodnotu zvlášť nepřičítá.
5. **Výkon baterií je stále předpoklad a mění znaménko zimní bilance.** V progresivní cestě 2050 je zimní bilance -1060.1 MW a s bateriemi 152.0 MW po 82.3 h. Výkon 1212.1 MW je odvozen z 87,3 GWh / 72 h a je to stupeň D. Dopadová studie s.145 uvažuje 1 GW a 1 GWh, tedy jinou dobu. Baterie také pokryjí špičku jen po omezenou dobu a model nesleduje, zda jsou nabité.
6. **Zimní vítr je počítán jako nula.** P10 a P50 jsou nula podle pravidla Dopadové studie s.73, není to medián. Změřený medián při 14 zimních maximech ČR je 0,192 instalovaného výkonu. S touto hodnotou je zimní bilance 2050 -940.3 MW v progresivní cestě a -495.6 MW v konzervativní cestě.
7. **Hodiny plynových řádků podle roku.** Koeficient je jeden na položku a cestu a míří na rok 2050, ale hodiny plynových řádků se mění podle roku. Nové plynové bloky v progresivní cestě 2030 vycházejí asi o 50 MW výš než 93 MW × 0,9.

## 12. Seznam zdrojů

Strany u položek jsou strany PDF. Část zdrojů je neveřejná, a to studie ZEVO. U některých webových zdrojů je v poli Poznámka u položky uvedeno, že byl dostupný jen souhrn vyhledávače. U webových článků je uveden popis obsahu, ne vždy přesný titulek.

| Název | Vydavatel nebo autor | Datum | Odkaz |
|---|---|---|---|
| Dopadová studie energetické bezpečnosti a soběstačnosti MSK po odchodu od spalování uhlí | VŠB-TUO, CEET, pro Moravskoslezské energetické centrum, p. o. | listopad 2024 | URL není v podkladech uvedena |
| Vnitrostátní plán České republiky v oblasti energetiky a klimatu | Česká republika, plán podle nařízení EU 2018/1999 | prosinec 2024 | URL není v podkladech uvedena |
| Město bez elektřiny, Podzimní škola (prezentace) | VŠB-TUO, REFRESH, EnergyLab | 4. až 6. listopadu 2026 | URL není v podkladech uvedena |
| Technicko-ekonomická studie ZEVO 120 000 t/rok, pracovní verze | neveřejná | říjen 2026 | neveřejná. Zdroj je neveřejná studie, uvedena jsou jen čísla potřebná k výpočtu. |
| ERÚ Roční zpráva 2025 | Energetický regulační úřad | neuvedeno | https://eru.gov.cz/sites/default/files/obsah/prilohy/eruelektro2025.pdf |
| Čtvrtletní zprávy o provozu elektrizační soustavy, 2023 až 2026 Q2 (zpráva za Q3 2023 v podkladech není) | Energetický regulační úřad | průběžně | URL není v podkladech uvedena |
| Projekce obyvatelstva v krajích ČR do roku 2080, kód 130052-24 | ČSÚ | 12.12.2024 | https://csu.gov.cz/produkty/projekce-obyvatelstva-v-krajich-cr-do-roku-2080 |
| Obyvatelstvo v Moravskoslezském kraji v roce 2025 | ČSÚ | neuvedeno | https://csu.gov.cz/msk/obyvatelstvo-v-moravskoslezskem-kraji-v-roce-2025 |
| Statistická ročenka Moravskoslezského kraje 2025 | ČSÚ | neuvedeno | https://csu.gov.cz/produkty/statisticka-rocenka-moravskoslezskeho-kraje-2025 |
| Základní výsledky SLDB 2021 Moravskoslezský kraj | ČSÚ | neuvedeno | URL není v podkladech uvedena |
| Velikost hospodařící domácnosti, výsledky sčítání | ČSÚ | neuvedeno | https://scitani.gov.cz/velikost-hospodarici-domacnosti |
| EU road vehicle energy consumption and CO2 emissions by 2050, Energy Policy 138, 111224 | Krause et al. | 2020 | doi 10.1016/j.enpol.2019.111224 |
| Real-world data analysis of battery electric trucks operating in Germany, EVS38 | Le Corguillé, Hacker, Dolinga (Oeko) | 2025 | https://www.oeko.de//fileadmin/oekodoc/Real-world-data-analysis-of-battery-electric-trucks-operating-in-Germany.pdf |
| Global Hydrogen Review 2024, Assumptions Annex | IEA | 2024 | https://iea.blob.core.windows.net/assets/36017d2f-747b-4993-b06d-33209fe143fa/GHR24AssumptionsAnnex.pdf |
| Technical Targets for Proton Exchange Membrane Electrolysis | US DOE | neuvedeno | https://www.energy.gov/eere/fuelcells/technical-targets-proton-exchange-membrane-electrolysis |
| Hydrogen Program Record 9013 | US DOE | 2009 | https://www.hydrogen.energy.gov/pdfs/9013_energy_requirements_for_hydrogen_gas_compression.pdf |
| Fuel-cell tractor-trailers: technology and fuel | ICCT | 2022 | https://theicct.org/publication/fuel-cell-tractor-trailer-tech-fuel-jul22/ |
| Hydrogen as Fuel: Production and Costs | NATO ENSEC COE | neuvedeno | https://old2.enseccoe.org/en/newsroom/hydrogen-as-fuel-production-and-costs/473 |
| JIVE 2, zpráva za období 5 | CORDIS | neuvedeno | https://cordis.europa.eu/project/id/779563/reporting |
| JIVE 1, výsledky projektu | Sustainable Bus | neuvedeno | https://www.sustainable-bus.com/fuel-cell-bus/jive-1-project-results-2024-hydrogen-buses-europe/ |
| Applied Energy 204, 332-342 | Love et al. | 2017 | DOI 10.1016/j.apenergy.2017.07.026 |
| Nature Energy 3, 193-201 | Muratori | 2018 | DOI 10.1038/s41560-017-0074-z |
| Preprint arXiv 2208.07302 | arXiv | neuvedeno | arXiv 2208.07302, odkaz není v podkladech uveden |
| Preprint arXiv 2112.04559 | arXiv | neuvedeno | arXiv 2112.04559, odkaz není v podkladech uveden |
| Normalizované typové diagramy dodávek, stránka přehledu, soubor nebyl použit | OTE | neuvedeno | https://www.ote-cr.cz/cs/statistika/typove-diagramy-dodavek-elektriny |
| Článek o odpadu a výrobě elektřiny, 200 tis. t, 23 000 MWh | Technický týdeník | neuvedeno | URL není v podkladech uvedena |
| Článek o elektrické peci v Třinci a spotřebě elektřiny, „zvýšení spotřeby elektřiny o 30 procent na 1 TWh ročně“ | Ekonomický deník | 30.1.2025 | https://ekonomickydenik.cz/ekologizace-za-25-miliard-trinecke-zelezarny-investuji-do-nizkoemisni-budoucnosti/ |

### Webové zdroje uvedené u položek

| Popis | Vydavatel | Datum | URL |
|---|---|---|---|
| Článek o ocelárně a možném datacentru | cc.cz | neuvedeno | https://cc.cz/necekany-pohled-na-umirajici-ocelarnu-v-cesku-ma-neco-extra-cenneho-a-muze-z-ni-byt-obri-datacentrum/ |
| Tisková zpráva o elektromobilech a plynových autech v krajích | Centrum dopravního výzkumu | neuvedeno | https://cdv.gov.cz/file/tz-nejvice-elektromobilu-je-v-praze-plynovych-aut-v-moravskoslezskem-kraji |
| Článek o konci těžby na dole Darkov | ČT24 | neuvedeno | https://ct24.ceskatelevize.cz/regiony/3274256-z-dolu-darkov-vyjel-posledni-vozik-cerneho-uhli-tezba-tam-definitivne-skoncila |
| Článek o větrných elektrárnách u Břidličné | Ekonomický deník | neuvedeno | https://ekonomickydenik.cz/investor-chce-u-bridlicne-postavit-az-27-vetrnych-elektraren-cast-mistnich-ziska-elektrinu-zdarma/ |
| Článek o přechodu ostravské teplárny z uhlí na zemní plyn | Ekonomický deník | neuvedeno | https://ekonomickydenik.cz/uhli-zemni-plyn-teplarna-ostrava/ |
| Článek o paroplynovém zdroji v Třinci | GMK Center | 17.6.2026 | https://gmk.center/en/news/trinecke-zelezarny-is-investing-over-180-million-in-a-combined-cycle-power-station/ |
| Údaje o spotřebě vodíku u Toyoty Mirai | H2.LIVE | neuvedeno | https://h2.live/en/fuelcell-cars/toyota-mirai/ |
| Článek o malém modulárním reaktoru v MSK | oEnergetice | 14.5.2026 | https://oenergetice.cz/jaderne-elektrarny/prvni-maly-modularni-reaktor-muze-stat-v-moravskoslezskem-kraji-uz-v-roce-2035 |
| Článek o modernizaci teplárny Karviná | oEnergetice | neuvedeno | https://oenergetice.cz/teplarenstvi/veolia-energie-chysta-modernizaci-teplarny-karvina-za-miliardu-kc |
| Článek o konci těžby na dole ČSM | oEnergetice | neuvedeno | https://oenergetice.cz/uhli/dul-csm-se-chysta-na-ukonceni-tezby-a-likvidaci-okd-na-to-ma-33-miliardy-korun |
| Článek o konci výroby v Dětmarovicích | Český rozhlas Ostrava | 12.6.2025 | https://ostrava.rozhlas.cz/detmarovice-ukoncily-eru-vykonneho-cernouhelneho-teplarenstvi-v-cesku-9493534 |
| Naše cesta k uhlíkové neutralitě | Třinecké železárny | neuvedeno | https://trz.cz/assets/uploads/udrzitelnost/TZMS-NaseCestaKUhlikoveNeutralite.pdf |
| Článek o konkurzu Liberty Ostrava | E15 | neuvedeno | https://www.e15.cz/byznys/prumysl-a-energetika/veritele-poslali-liberty-ostrava-do-konkurzu-o-zkrachovalou-hut-maji-zajem-tri-kupci-1420502 |
| Článek o provozu vodíkového Hyundai XCIENT | Hydronews | neuvedeno | https://www.hydronews.it/en/gebruder-weiss-positive-first-year-use-of-hydrogen-hyundai-xcient-fuel-cell/ |
| Článek o odložení elektrické obloukové pece v Třinci | Novinky | 23.4.2025 | https://www.novinky.cz/clanek/ekonomika-trinecke-zelezarny-brzdi-plany-stavba-elektricke-obloukove-pece-bude-mit-minimalne-dva-roky-zpozdeni-40518385 |
| Tendr na elektřinu, stránka nebyla otevřena | Správa železnic | neuvedeno | https://www.spravazeleznic.cz |
| Článek o plánech Nové hutě a přípravě obloukové pece | SteelOrbis | 19.1.2026 | https://www.steelorbis.com/steel-news/latest-news/czech-based-nova-hu-plans-major-investments-and-eaf-preparation-in-2026-1430249.htm |
| Článek o plánech datových center v ČR | Kurzy.cz | neuvedeno | https://zpravy.kurzy.cz/862356-vysoke-ceny-energii-zabrzdi-podle-egu-plany-na-vystavbu-az-40--datovych-center-v-cr/ |
