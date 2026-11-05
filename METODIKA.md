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

## Zdroje k metodě

Plné údaje a stav přečtení jsou v záložce Metodika, blok Literatura k metodě. Přečtené: Bishop a kol. 2007, Dreborg 1996, Slach a kol. (kapitola 9), Kosow a Gaßner 2008 (vybrané strany). Jen výtah, záznam nebo citace jinde: Börjeson a kol. 2006, Cherp a kol. 2021, Craig a kol. 2002, Fisher a Pry 1971, Fritsch a Carlson 1980, Robinson 1990.
