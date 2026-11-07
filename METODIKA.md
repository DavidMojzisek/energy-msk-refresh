# Metodika křivek výroby a spotřeby elektřiny v MSK

Technický popis k záložce Metodika. Stav 2026-11-05. Výsledky a jejich rozbor jsou v přepočtu `hodinovy/PREPOCET.md`.

## Co křivky znamenají

Křivka říká, kolik elektřiny by kraj vyráběl a spotřeboval, pokud by se vydal danou cestou. Není to předpověď, která z cest nastane.
Pásmo kolem křivky vyjadřuje nejistotu uvnitř jedné cesty. Rozdíl mezi cestami je volba, ne nejistota.
Pásmo je prostředních 80 % běhů simulace, tedy P10 až P90. Je to náš odhad nejistoty, ne statistický interval, protože budoucnost nemá výběr dat.
Soběstačnost znamená jen elektřinu vyrobenou v kraji, palivo pro SMR i plyn je dovezené.

## Jaká je to metoda

Metodu scénářů používáme v širokém smyslu a neúplně. Dvě cesty jsou dané předem a model je rozpracovává v číslech, což odpovídá rozpracování pevných scénářů (Bishop a kol. 2007, s. 12). Z pěti obecných fází (Kosow a Gaßner 2008, s. 25 až 30) jsou uděláné vymezení oblasti a klíčové faktory, rozbor faktorů je zjednodušený, tvorba scénářů udělaná není a přenos je částečný. Progresivní cesta je zadaná jako žádoucí obraz, výpočet je průzkumný (Slach a kol., s. 182; Kosow a Gaßner 2008, s. 31 až 32). Blok Co by muselo platit je podmíněný výpočet a jeden krok backcastingu, ne backcastingová studie (Dreborg 1996, s. 814, 824 a 826). Vše v části Postup, co nemá uvedený zdroj, je náš postup nebo úsudek.

## Postup

1. **Hranice a bilance.** Území kraje, jen elektřina, roky 2025 až 2050 po jednom roce. Výroba je brutto z tabulky 6.1 ERÚ. Spotřeba je součet sektorů z tabulky 6.3 ERÚ plus ztráty v sítích jako samostatná položka.
2. **Výchozí stav.** Každá položka začíná změřenou hodnotou za rok 2025 z ERÚ. Pokud ERÚ položku neuvádí zvlášť, začíná od nejlepšího dostupného rozdělení a je to popsané u položky.
3. **Rozklad položky.** Roční elektřina = činnost × intenzita. Například fotovoltaika = instalované MW × hodiny za rok. Fotovoltaika počítá 942 h (průměr MSK 2022 až 2025, P10 889, P90 995, meze odhad), vítr 2 471 h (průměr MSK 2013 až 2025, P10 2 184, P90 2 810).
4. **Odhad s intervalem.** Pro roky 2030, 2040 a 2050 má každá položka hodnoty P10, P50 a P90, zdroj a stupeň důkazu.
5. **Vývoj v čase.** Tabulka určuje tvar každé položky. Základní tvar je logistická křivka. Fisher a Pry 1971 ji použili pro nahrazení jedné technologie druhou, Cherp a kol. 2021 popisují S-křivky u větru a slunce po státech. Použití na položky kraje, normování S(2025) = 0 a S(2050) = 1 a dopočet k a t_m z hodnot pro roky 2030 a 2040 je náš postup. Další tvary jsou monotónní kubická interpolace přes milníky (Fritsch a Carlson 1980), kalendářní skok a dva stupně. Velká událost je strmá logistická křivka s k = 4. Položka, která vzroste a klesne, je součet dvou křivek. Vnější vliv je násobek D(t) s D(2025) = 1.
6. **Změna posuvníkem.** Změna cíle se přičítá členem (y_T,nové − y_T,výchozí) · σ(x), kde x = (t − 2030) / 20 omezené na 0 až 1 a σ(x) = 3x² − 2x³. Ztráty v sítích a vlastní spotřeba zdrojů jsou vzorce z ostatních řádků, stejné v obou cestách.
7. **Agregace.** Simulace Monte Carlo po letech, 10 000 běhů. Losuje se cíl v roce 2050 z P10 až P90 a načasování. Celkový součet nikdy nevzniká sečtením P90 všech položek. Mnoho přípustných hodnot vstupů, případně s Monte Carlo, popisují u citlivostní analýzy Bishop a kol. 2007 (s. 19). Položky se stejnou příčinou se losují částečně společně, společný faktor je náš postup a korelace 0,6 náš úsudek. SMR je v progresivní cestě daný, případ bez SMR se počítá zvlášť. Podíl běhů se uvádí jako pásmo. Pásmo spotřeby v roce 2030 nesmí být užší než pozorované rozpětí pětileté změny 20,6 procentního bodu.
8. **Dva okamžiky.** Bilance výkonu v nejhorším okamžiku je podle Dopadové studie (s. 73, rovnice 4). Studie odhaduje zatížení kraje z roční spotřeby a doby trvání maxima (s. 74), přepočet položek koeficienty je náš postup, popis je v `sezonni_metodika.md`. Studie do špičky počítá jen stabilní zdroje, proto je v zimní špičce vítr nula. Je to nejhorší případ, ne běžná zima.
9. **Hodinový model.** Model je náš vlastní zjednodušený výpočet a pravidla velikosti baterie a elektrolyzéru jsou naše, ne převzatá metoda. Každá hodina roku 2050 pro 5 povětrnostních let 2015 až 2019, úrovně z tabulky položek, tvary z PVGIS, OPSD a OTE. Baterie každou půlnoc z křivky na další den najde nejnižší rovnou hladinu, kterou udrží; přebytek má přednost a v hodinách s nízkým zbytkovým zatížením nabíjí i ze sítě. Přebytek bere elektrolyzér podle rozvrhu malé nádrže, elektrokotle do 70 MW, což je náš součet z údajů studie, a baterie, zbytek je vývoz. Tepelná čerpadla v tuhých mrazech běží rovnoměrně, denní průběh slábne od +5 °C do −10 °C, je to úsudek. Odstup nabíjení ze sítě 100 MW pod denní hladinou je také úsudek. Schodek kryje baterie, potom plyn do ročního rozpočtu a zbytek dovoz. Meze: jeden uzel bez sítě, celostátní tvary, předpověď na den dokonalá, rozvrh plynu, elektrolýzy ze sítě a nádrže zná celý rok dopředu. Denní špička nestoupne jen při dokonalé předpovědi, se včerejší křivkou některé dny stoupne, velikost je v přepočtu.
10. **Výchozí nastavení.** Baterie 2,7 GWh a 675 MW z mediánu denního výkyvu zbytkového zatížení, 4 h, základ, ne nákladové optimum. Elektrolyzér 197 MW a 6 294 plných hodin, nejmenší výkon s vývozem pod 1 % přebytku ve výchozím nastavení. Výkon elektrolyzéru = řádky vodíku flotily × (1 + míra ztrát sítě) × 1 000 / plné hodiny. Malá nádrž 20 t.
11. **Křížová kontrola.** Výsledek se srovnává s Dopadovou studií a Vnitrostátním plánem. Změny proti studii jsou v přepočtu.

## Stupně důkazu

| Stupeň | Co to je | Příklad |
|---|---|---|
| A | Změřená data | ERÚ, ČSÚ, ČEZ Distribuce |
| B | Publikovaná studie nebo plán | Dopadová studie, Vnitrostátní plán, ČEPS |
| C | Technický výpočet ze známých parametrů | Výkon reaktoru × využití |
| D | Odhad bez publikovaného zdroje | Zatím nezávisle neověřený úsudek |

Stupeň se zapisuje ke každé položce a řídí se nejslabším vstupem hodnoty P50 pro rok 2050. Meze P10 a P90 jsou téměř všude úsudek a stupeň se k nim nevztahuje.

## Položky

### Výroba

- Stávající zdroje: černé uhlí, hnědé uhlí, zemní plyn, hutní plyny (vysokopecní a koksárenský), důlní plyn
- OZE: fotovoltaika střešní, fotovoltaika pozemní, vítr, malé vodní elektrárny, biomasa, bioplyn, geotermální energie
- Nové zdroje: SMR, nové plynové bloky, syntetický plyn z odpadu, energetické využití odpadu
- Skladování a zálohy: baterie, jiné skladování, vodík zpět na elektřinu. Nejsou to zdroje, do roční bilance vstupují jen ztrátami.

### Spotřeba

- Těžký průmysl: Třinecké železárny, Nová huť, ostatní průmysl a chemie, doly
- Budovy: domácnosti bez vytápění, služby a veřejný sektor, vytápění tepelnými čerpadly, přímotopy, elektrokotle v teplárnách, chlazení
- Doprava: osobní auta, nákladní doprava, vlaky, MHD
- Nové zátěže: datacentra, výroba vodíku, výroba syntetického plynu
- Soustava: vlastní spotřeba zdrojů, ztráty v sítích, ztráty baterií
- Ostatní: zemědělství a stavebnictví, úspory a účinnost jako záporná položka

### Vazby, které se počítají společně

- Elektrifikace oceláren snižuje výrobu z hutních plynů a zvyšuje spotřebu elektřiny.
- Vodík spotřebuje elektřinu v kraji a nevrací se zpět na elektřinu.

## Realistický scénář

Třetí křivka vychází ze dvou cest jako z krajních bodů. Není to předpověď ani nejpravděpodobnější vývoj. Je to důsledek zvolených předpokladů. Předpoklad, že jsou obě cesty krajní, je náš. Křivka nemění horní graf ani tabulku položek.

### Vzorec a jedna osa

Plynulá položka se v každém roce počítá mezi řádkem konzervativní cesty K a progresivní cesty P:

R(t) = (1 − a) · K(t) + a · P(t), a = Σ w · x / Σ w

Poloha a je vážený průměr indikátorů x dané skupiny položek. Všechny indikátory leží na jedné ose: x = 0 je popis stavu konzervativní cesty, x = 1 popis stavu progresivní cesty. Hodnota 1 znamená příznivý vývoj, ne menší schodek, protože elektrifikace zvyšuje spotřebu.

Všechny indikátory na 0 nebo na 1, bez odchylek a s pecí v Nové huti, u konzervativní cesty navíc s plynovými bloky 683 MW, dají přesně krajní cestu. V roce 2050 je to výroba 3 956 a spotřeba 8 262 GWh, nebo výroba 7 862 a spotřeba 12 526 GWh.

Rovnice je dohoda o interpolaci. Zdroj dokládající lineární převod ze společenského indexu na výstavbu jsme nenašli. Nenašli jsme ani použitelnou elasticitu nebo práh pro vítr a slunce v regionu. Hledání bylo cílené, ne systematické. Literatura dokládá S-křivky v čase, ne v poloze a (Grubler a kol. 2016, Odenweller a kol. 2022). Skupiny s podobným průměrem preferencí mohou dopadnout velmi odlišně (Granovetter 1978).

Ze 47 položek je 21 plynulých a jsou v 8 skupinách. Dalších 18 položek má v obou cestách stejné hodnoty. Dvě jsou vzorce z vypočtených řádků: vlastní spotřeba zdrojů a ztráty v sítích. Šest řádků patří událostem: SMR, nové plynové bloky, datacentra, Třinecké železárny, hutní plyny a Nová huť.

| Skupina | Položky | Výchozí a |
|---|---|---|
| Vítr a pozemní fotovoltaika | vítr, fotovoltaika pozemní, ztráty baterií | 0,411 |
| Střešní fotovoltaika | fotovoltaika střešní | 0,289 |
| Teplo a chlazení | tepelná čerpadla, přímotopy, stávající kogenerace, elektrokotle, chlazení, uhlí v teple | 0,340 |
| Osobní auta | osobní auta | 0,442 |
| Nákladní doprava a vodík | nákladní doprava, MHD, vlaky, řádky výroby vodíku | 0,409 |
| Ostatní průmysl | ostatní průmysl a chemie | 0,378 |
| Úspory | úspory a účinnost | 0,353 |
| Využití odpadu | energetické využití odpadu, liší se jen rok spuštění | 0,549 |

### Váhy a jejich původ

Seznam 34 indikátorů, popisy stavů a kategorie jsou z pracovní tabulky indikátorů. Vazby na položky a váhy jsou z pracovního podkladu k indikátorům, po opravě. Kotvy a výchozí hodnoty jsou naše. Všechno to je neověřený odhad.

Tabulka vah má 50 kladných vah: 41 z podkladu a 9 našich. Nákladní doprava, úspory a rok spuštění využití odpadu v podkladu vazbu nemají, proto je tu vazba náš úsudek. Vážený průměr váhy normuje, takže součet nad 1 nevadí a položka nepřestřelí druhou cestu. Váha vyjadřuje směnu mezi indikátory, ne jejich důležitost (OECD a JRC 2008, s. 33; Paruolo a kol. 2013).

Oprava dala deseti indikátorům váhu 0:

- E05 a E25 v podkladu mění jen zimní výkon a položku energie nemění.
- E09 a E28 působí jen po blackoutu a tuto událost model nemá.
- E12 je demografie, ta se přičítá přímo jako odchylka.
- E18 má za ukazatel elektromobily, tedy samu položku modelu.
- E19 předpokládá položku sítě, kterou model nemá, a rentabilita SMR nezávisí na počtu obyvatel kraje.
- E23 je definice rozdílu mezi cestami.
- E27 by činil výsledek modelu závislým na hodnocení téhož modelu.
- E32 je důsledek přechodu a saldo migrace už je v demografii.

SMR navíc nebere E06, protože podpora obnovitelných zdrojů neměří přijetí jádra. Dvojice se stejnými vazbami E02 a E10 i E20 a E31 zůstaly, protože mají různé ukazatele. Překryv znamená dvojí započtení (OECD a JRC 2008, s. 32) a zůstává přiznaný.

Každý indikátor má ukazatel, dvě kotvy a zdroj, nebo označení odhad. Kotvy jsou úsudek. Výchozí x je od 0,154 do 0,65. Jistota je u jednoho indikátoru vysoká, u 15 střední, u 13 nízká a 5 je odhad. Šest výchozích hodnot je přepsaných, protože dnešní stav neříká dost o období do roku 2050: E06, E07, E24, E25, E26 a E34. Důvod je u každého indikátoru. Bez dat platí 0,5 a označení odhad.

Citlivost na výpočet polohy mění schodek 2050 větve bez SMR málo, z 5 129 na 5 021 až 5 220 GWh. Výroba se přitom pohybuje od 3 202 do 3 860 GWh a spotřeba od 8 223 do 9 080 GWh. Varianty jsou geometrický průměr, stejné váhy, zjednodušené váhy 3 a 1, skóre z tabulky indikátorů, mocniny a s exponentem 1,5 a 1/1,5 a S-křivka v a jako ilustrace. Úzký rozsah schodku znamená, že výroba a spotřeba se hýbou spolu, ne že je výsledek přesný.

### Události a prahy

Velká událost je celý řádek, nikdy zlomek. Skóre z indikátorů není pravděpodobnost. Scénářům se pravděpodobnost obvykle nepřiřazuje (Morgan a Keith 2008). Kde se v praxi získává, ptají se experti přímo (AEMO 2023). Naše odhady přímým dotazem nevznikly, jsou subjektivní a podmíněné.

| Událost | Odhad | Volba podle indikátorů nebo odhadů | Výchozí stav | Schodek 2050 po změně, GWh |
|---|---|---|---|---|
| SMR | 25 %, rozpětí 15 až 40 %, aspoň jeden blok v provozu do konce roku 2049 | Výchozí skóre 0,464 odpovídá 25 %, konce 0 a 1 zůstávají, ano od 50 % | bez SMR | s SMR 1 993 |
| Plynové bloky bez SMR | 30 % pro aspoň jeden blok bez doloženého řízení | Přepínač | 283 MW | 683 MW 3 898 |
| Velká datová centra | žádné obhajitelné číslo | Skóre 0,389, ano od 0,75 | řádek konzervativní cesty, 70,1 GWh | 5 783 |
| Třinec, první pec | 60 %, rozpětí 40 až 75 % | Ano od 50 % | první pec | žádná pec 4 607 |
| Třinec, plná elektrifikace | žádné obhajitelné číslo | Skóre 0,46, ano od 0,75 | ne | 5 653 |
| Nová huť | 45 %, rozpětí 25 až 60 % | Ano od 50 % | bez pece | s pecí 5 829 |

Výchozí schodek je 5 129 GWh. Každý řádek mění jen jednu událost. Výchozí stav bere u každého odhadu častější stav. Datová centra a plná elektrifikace jsou ve výchozím stavu ne.

Odhad 25 % je úsudek z řetězu kroků: první blok ve Wales, Temelín, potom Dětmarovice. Lokalita Dětmarovice není vybraná a rozhodnutí o stavbě chybí. Výchozí rok spuštění je 2048, plán kraje a studie uvádějí 2045. Spuštění po roce 2050 znamená do roku 2050 větev bez SMR.

Třinec má tři stavy. Řádek P je plná elektrifikace, 1 549,2 GWh a hutní plyny 0 GWh. Řádek K je první pec, 1 159,2 GWh a hutní plyny 144,3 GWh. Žádná pec nechává hodnoty roku 2025, 769,2 GWh a hutní plyny 288,5 GWh, a leží mimo osu cest. Pec a hutní plyny jsou jedna událost.

Nová huť má v obou cestách stejný řádek, 736,3 GWh, a je to odchylka mimo osu cest. Záměr prošel zjišťovacím řízením bez plného posouzení, dotace je přislíbená a rozhodnutí o stavbě chybí. Bez pece zůstává hodnota roku 2025, 61,3 GWh.

### Pravidlo pro plyn

Plynové bloky nejdou od začátku po řádku své větve. Reaktor spuštěný v roce 2048 nemůže měnit plyn v roce 2030. Obě větve proto mají společný plyn:

G(t) = (1 − s) · L(t) + s · P(t)

Tady s je skóre SMR, výchozí 0,464. L(t) je konečný výkon větve bez reaktoru. Ve výchozím stavu je to řádek K omezený hodnotou roku 2030, 896,8 GWh a 283 MW, při volbě 683 MW celý řádek K. V roce 2030 je G 722,4 GWh v obou větvích.

- S reaktorem jde plyn od roku před spuštěním po řádku P. Jeho útlum je posunutý o odklad proti roku 2045. V roce 2050 je to 387,4 GWh a plynové bloky 433 MW.
- Bez reaktoru se 10 let před plánovaným spuštěním začne přecházet na L(t). V roce 2050 je to 896,8 GWh a plynové bloky 283 MW. Těch 10 let je úsudek.

Před spuštěním se větve liší málo. Větev s SMR má nejvýš o 141 GWh větší schodek, v roce 2047, protože společný plyn klesá s řádkem P a bez reaktoru plyn přechází na L(t).

Výchozích 283 MW tvoří doložené a oznámené projekty bez bloků s nejistou lokalitou. Plyn navíc se uměle nepřidává. Bloky bez doloženého řízení mají odhad 30 % pro aspoň jeden. Bez reaktoru může být potřeba výkonu větší a tuto hodnotu nikdo neuvádí. Volba 683 MW dává v roce 2050 2 164,3 GWh a schodek 3 898 GWh.

Výchozí schodek 5 129 GWh je větší než v obou cestách, 4 664 GWh v progresivní a 4 306 GWh v konzervativní. Chybí tu reaktor z progresivní cesty i plynové bloky navíc z konzervativní cesty.

### Demografie a oteplení jako odchylky

Obě odchylky leží mimo osu cest, stejně jako Nová huť a plynové bloky 283 MW. Křivka proto smí vyjít mimo rozsah cest. Menší schodek přitom není vždy dobrá zpráva, vzniká i tehdy, když z kraje odchází průmysl nebo lidé.

Obě cesty počítají s projekcí ČSÚ, 999 tisíc obyvatel v roce 2050, a EUROPOP2025 dává také 999 tisíc. Výchozí odchylka je proto nula. Varianty Eurostatu jsou 965 až 1 022 tisíc. Změřený stav k 1. 1. 2026 je o 4 207 osob nad projekcí. Odchylka roste lineárně do roku 2050 a působí stejnými vzorci jako velké trendy, na osobní auta, domácnosti bez vytápění, tepelná čerpadla, přímotopy a chlazení.

Klima položek odpovídá povětrnostním rokům 2015 až 2019. Výchozí další oteplení je +1,2 °C v roce 2050 a roste lineárně. Je to odhad: CMIP6 pro ČR dává +1,1 °C při SSP2-4.5 a +1,5 °C při SSP5-8.5, pozorovaný trend je +1,2 až +1,5 °C a široké rozpětí +0,5 až +2,1 °C. Data jsou za ČR a přebírají se pro kraj.

Oteplení násobí vytápění a teplárenskou výrobu poměrem z hodinového modelu. Při +1,2 °C je násobek 0,909 u tepelných čerpadel, 0,933 u přímotopů a 0,892 u stávající kogenerace. Chlazení násobek nemá, oteplení je už v podílu chlazených domácností.

### Pásmo

Pásmo je prostředních 80 % z 6 000 běhů simulace, tedy P10 až P90, pro výchozí nastavení. Posuvníky ho nemění. Hodnoty pro rok 2050 v GWh, P10, P50 a P90:

| | Všechny běhy | Větev bez SMR | Větev s SMR |
|---|---|---|---|
| Výroba | 3 224, 4 721, 7 456 | 3 124, 4 206, 5 785 | 6 376, 7 185, 8 561 |
| Spotřeba | 7 585, 9 119, 10 881 | 7 509, 9 057, 10 798 | 7 799, 9 341, 11 086 |
| Schodek | 1 349, 4 198, 6 621 | 2 680, 4 785, 6 862 | 56, 2 038, 4 056 |

| Zdroj nejistoty | Co se losuje | Šířka schodku, jen tento zdroj, GWh | O kolik se celek zúží bez něj, GWh |
|---|---|---|---|
| Míry naplnění | x podle jistoty, se společným faktorem a faktorem kategorie | 475 | 35 |
| Váhy | násobek každé váhy | 102 | 10 |
| Tvar vazby | a na g, mimo skóre událostí | 861 | 113 |
| Velké události | SMR, rok spuštění, plyn bez doloženého řízení, obě pece | 3 975 | 1 542 |
| Demografie a oteplení | oteplení +0,5 až +2,1 °C, obyvatelé 965 až 1 022 tisíc | 85 | 0 |
| Technická nejistota řádků | rozsahy řádků obou cest se stejným losem | 3 595 | 1 462 |
| Všechny zdroje | | 5 271 | |

Losované podíly událostí jsou úsudek. SMR má 25 % běhů a rok spuštění 2045, 2047 nebo 2049 s podíly 20, 28 a 52 %. Plynové bloky 683 MW jsou ve 30 % běhů, v ostatních 283 MW. Pece mají společné rozdělení: obě 30 %, jen Třinec 30 %, jen Nová huť 15 %, žádná 25 %. Síly faktorů a rozptyly jsou také úsudek.

Společné faktory rozšiřují výrobu i spotřebu a schodek zužují, protože výroba a spotřeba rostou spolu. Při nezávislých indikátorech je šířka výroby 266, spotřeby 539 a schodku 562 GWh. S výchozími faktory je to 574, 881 a 475 GWh, se silnějšími 717, 1 054 a 435 GWh.

Co pásmo neznamená:

- Není to statistický interval. Budoucnost nemá výběr dat a většina rozsahů je náš odhad.
- Tabulka není rozklad rozptylu (OECD a JRC 2008, kap. 7). Sloupce se nesčítají, zdroje na sebe působí a malé hodnoty v posledním sloupci jsou v mezích šumu simulace.
- Výchozí křivka není střed pásma. Její schodek 5 129 GWh je jeden stav událostí, P50 všech běhů je 4 198 GWh.
- Datová centra a plná elektrifikace Třince v pásmu nejsou, obhajitelné číslo pro ně neexistuje. Jejich účinek je v tabulce událostí.
- Los SMR nezávisí na losovaných indikátorech, má vždy podíl 25 %.
- Největší část tvoří události a rozsah řádků. Rozsah řádků je z velké části náš odhad a může se překrývat s indikátory.
- Výroba má v součtu dva vrcholy, s reaktorem a bez něj, schodek jeden. Kvantily dva vrcholy neukážou (Hyndman 1996), proto jsou větve uvedené zvlášť.

### Hodinový výpočet výchozího stavu

Výchozí řádky roku 2050 v obou větvích procházejí hodinovým modelem, 5 povětrnostních let 2015 až 2019. Čísla jsou průměr let, pokud není uvedeno jinak.

| Rok 2050 | Bez SMR | S SMR |
|---|---|---|
| Roční výpočet: výroba, GWh | 3 531,3 | 6 963,9 |
| Roční výpočet: spotřeba, GWh | 8 660,8 | 8 956,4 |
| Hodinově: dovoz, GWh | 5 124,6 | 1 982,4 |
| Hodinově: přebytek bez využití, GWh | 0,0 | 0,0 |
| Hodinově: plyn, GWh | 1 012,0 | 502,6 |
| Elektřina ze sítě pro vodík, GWh | 507,8 | 507,7 |
| Nabíjení baterie ze sítě, GWh | 273,5 | 150,4 |
| Největší hodinový dovoz, nejhorší rok, MW | 902,2 | 480,3 |
| Největší zatížení, MW | 1 419,1 | 1 452,8 |
| Plynové bloky, MW | 283 | 433 |

Zařízení je v obou větvích stejné a je to úsudek, není hledané znovu. Baterie je 5,12 GWh a 1 000 MW, lineárně mezi cestami podle polohy větru. Elektrolyzér je 81 MW a nádrž 8,2 t, úměrně vodíku flotily, tedy 0,409 progresivní cesty.

Výpočet platí jen pro výchozí nastavení a po změně posuvníků se nepřepočítává. Největší hodinový dovoz je podhodnocený, protože rozvrh plynu zná celý rok dopředu. Skutečná špička by byla vyšší. Platí i meze hodinového modelu z bodu 9 části Postup. Zimní špička a letní poledne se pro tuto křivku nepočítají.

### Meze

- Slovo realistický platí jen při těchto předpokladech. Lichý počet scénářů může svádět ke čtení prostředního jako nejpravděpodobnějšího (metodika PBL). Mezilehlé stavy navíc mohou být za S-křivek málo pravděpodobné (Odenweller a kol. 2022, u vodíku).
- Vítr a pozemní fotovoltaika mají stejnou polohu, i když je přijetí může rozdělovat. Ve Velké Británii působil stejný ukazatel na povolování větru a slunce opačně (Roddis a kol. 2018). Čísla z této práce na kraj nepřenášíme.
- Řada ukazatelů měří dnešní stav a jen přibližuje indikátor, například podíl vysokoškoláků místo montážní kapacity. Část dat je za celou ČR. Zpětná kontrola proti skutečnosti neproběhla.
- Výchozí vítr 312 MW v roce 2050 je 10,8 MW za rok proti největšímu ročnímu přírůstku kraje 9,1 MW. Znamenalo by to rekord každý rok po celých 25 let. Fotovoltaika 867 MWp je 22,4 MWp za rok proti rekordu 83,3 MWp. Zdroj rekordů: ERÚ, Roční zpráva 2025, kap. 4.6.8.
- Model bere investice a umístění podniků jako dané vstupy. Dostupnost a cena elektřiny je ve skutečnosti ovlivňují. Studie z Indie a z Evropy ukazují, že vazba existuje (Allcott a kol., Panhans a kol. 2017). Jejich čísla na kraj nepřenášíme.

Literatura k této části, přečtený text: OECD a JRC 2008, Handbook on Constructing Composite Indicators; Paruolo, Saisana, Saltelli 2013, JRSS A 176(3); Grubler, Wilson, Nemet 2016, ERSS 22; Odenweller a kol. 2022, Nature Energy 7; Granovetter 1978, AJS 83(6); Hyndman 1996, The American Statistician 50(2); Roddis a kol. 2018, Applied Energy 226; Panhans, Lavric, Hanley 2017, ERE 68(4); AEMO 2023, 2024 ISP Delphi Panel, není to recenzovaná metoda; Allcott, Collard-Wexler, O'Connell, AER 106(3), čten pracovní text, ne verze v časopise. Jen abstrakt nebo veřejná část: Morgan a Keith 2008, Climatic Change 90; metodika PBL, nástroj Scenario analysis.

## Zdroje k metodě

Plné údaje a stav přečtení jsou v záložce Metodika, blok Literatura k metodě. Přečtené: Bishop a kol. 2007, Dreborg 1996, Slach a kol. (kapitola 9), Kosow a Gaßner 2008 (vybrané strany). Jen výtah, záznam nebo citace jinde: Börjeson a kol. 2006, Cherp a kol. 2021, Craig a kol. 2002, Fisher a Pry 1971, Fritsch a Carlson 1980, Robinson 1990.

## Dlaždice

Dlaždice nad grafem toků přepisují řádky zvolené cesty ve vybraném roce na počty, například turbín, aut nebo domů. Počítají se ze stejných čísel jako graf a mění se s posuvníky. Je to přepočet, ne sčítání. Plynové bloky a baterie mají velikost danou cestou a rokem. Výkon turbíny 6,2 MW je z jednoho záměru v kraji, domácí elektrárna 10 kWp a plocha pozemní fotovoltaiky jsou odhad, nájezd nákladního auta 60 000 km za rok je úsudek. Rok 2025 se u nákladních aut neuvádí, řádek je tam dopočet. U zařízení, kde na to je zdroj, ukazuje bublina řádovou cenu výstavby v eurech a dnešních cenách, jen pro nově postavené zařízení, bez připojení k síti, financování a výměn. Ceny v bublinách se nesčítají, součet investic a nákladů počítá zvlášť oddíl Ekonomika. U aut a datových center cena v bublině není.

Panel Technologie na stránce mění šest technických hodnot pro obě cesty i realistický scénář: spotřebu elektroauta a nákladního elektroauta na km, topný faktor tepelného čerpadla, elektřinu na kilogram vodíku, plné hodiny větru a ztráty v sítích. Ve výchozí poloze dává panel přesně čísla tabulky. U topného faktoru, který tabulka neuvádí, je výchozí dnešní měřený průměr 3,4. Změna se zavádí podle sigma(t) od roku 2030 do roku 2050. Zdroje rozsahů jsou na stránce v panelu Technologie, v rozkliknutí pod posuvníky.

## Ekonomika

Část Kolik cesty stojí na konci záložky Bilance převádí položky obou cest a realistického scénáře bez reaktoru na zařízení a zařízení na eura. Cesty ani jejich čísla se nemění. Peníze jsou reálné, v cenách roku 2025, bez daní, řádové. Ve výchozím nastavení jsou čísla mediány předem spočítaného losování s P10 až P90. Po změně posuvníků se karta i cena nad hlavním grafem přepočítají na stránce stejným výpočtem při středních vstupech: zásoby zařízení po ročnících, splátky investic do roku 2050, provoz, palivo, povolenky a dovoz. Losování se pro jiné nastavení nepočítá, pásma proto platí jen pro výchozí nastavení. Topný faktor mění elektřinu tepelného čerpadla, teplo dodané domu zůstává. Výkon plynových bloků a velikost baterií jsou v ceně pevné podle hodinového výpočtu, úspory nemají investici, síť na straně nové spotřeby v ceně není a přebytek elektřiny nemá hodnotu.

- Zásoba a tok: počty zařízení jsou stejné jako v dlaždicích. Každý ročník má svou životnost, potom se vyřadí a obnoví. Investice roku = (přírůstek + obnova) × měrná investice roku. Měrné investice se mění podle výhledu zdrojů, mezi milníky log-lineárně, za posledním milníkem zůstávají. Vstupy mají nízký, střední a vysoký scénář zdroje. Celá investice se připíše roku uvedení do provozu.
- Investice jsou ve třech skupinách: zařízení elektroenergetiky, příplatky za vozidla a tepelná čerpadla a elektrické pece v ocelárnách.
- Splátky: splátka = I · r(1 + r)^n / ((1 + r)^n − 1), n je životnost. Do porovnání jdou jen splátky let 2026 až 2050. Splátky po roce 2050 jsou uvedené zvlášť.
- Diskont: současná hodnota = Σ C(t) / (1 + r)^(t − 2025) přes roky 2026 až 2050, reálná sazba r = 3 %, referenční hodnota EU pro projekty, pokud chybí národní hodnota (Economic Appraisal Vademecum 2021-2027), citlivost 5 a 7 %.
- Úroveň A, elektroenergetika kraje: splátky elektráren, baterií, elektrolyzérů a posílení sítě pro novou fotovoltaiku a vítr, provoz, palivo a povolenky ETS1 elektráren a dovoz elektřiny za velkoobchodní cenu. Cesty dodají různé množství elektřiny, proto stránka uvádí i náklad na megawatthodinu dodané elektřiny.
- Úroveň B jen jako rozdíl mezi cestami: rozdíl A plus rozdíl příplatků za tepelná čerpadla proti plynovému kotli a za elektromobily a elektrická nákladní auta proti spalovacím, minus rozdíl ušetřeného benzínu, nafty, plynu v domech a povolenek ETS2. Pece jsou mimo obě úrovně.
- Překryvy: každé zařízení se počítá jednou a má jednoho plátce. Elektřina pro auta, tepelná čerpadla a vodík je zaplacená v úrovni A a v B se znovu neodečítá. U vozidel a tepelných čerpadel se počítá jen příplatek. Konec uhlí v teplárnách se v B nepřipisuje, protože chybí náhradní teplo.
- Nejistota: výběr latinskou hyperkrychlí (McKay a kol. 1979), 4 000 losování. Investice a provoz trojúhelníkově mezi nízkým a vysokým scénářem zdroje. U cen leží nízký scénář zdroje na 10. a vysoký na 90. percentilu losování. Jedno losování platí pro všechny roky a všechny cesty, rozdíl cest se počítá v každém losování zvlášť. P10, medián a P90 jsou jen výsledky losování. Cena elektřiny je pořadově svázaná s nákladem paroplynu metodou Imana a Conovera, síla vazby 0,7 je náš předpoklad, varianty 0,0 a 0,9. Ceny povolenek ETS2 od roku 2030 jsou náš předpoklad bez zdroje.
- Zdroje cen: katalogy technologií dánské energetické agentury, Fraunhofer ISE, IEA World Energy Outlook 2025, pro reaktor SMR IEA, pro nákladní auta ICCT. Srovnání s ekonomikou a rozpočtem kraje: ČSÚ a schválený rozpočet kraje na rok 2025, odkazy jsou na stránce u čísel.
