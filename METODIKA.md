# Metodika křivek výroby a spotřeby elektřiny v MSK

Technický popis k záložce Metodika. Stav 2026-11-04. Výsledky a jejich rozbor jsou v přepočtu `hodinovy/PREPOCET.md`.

## Co křivky znamenají

Křivka říká, kolik elektřiny by kraj vyráběl a spotřeboval, pokud by se vydal danou cestou. Není to předpověď, která z cest nastane.
Pásmo kolem křivky vyjadřuje nejistotu uvnitř jedné cesty. Rozdíl mezi cestami je volba, ne nejistota.
Pásmo je interval věrohodnosti 80 %, tedy P10 až P90. Není to statistický interval spolehlivosti, protože budoucnost nemá výběr dat.
Soběstačnost znamená jen elektřinu vyrobenou v kraji. Palivo pro SMR a zemní plyn je dovezené i při kladné bilanci.

## Postup

1. **Hranice a bilance.** Území kraje, jen elektřina, roky 2025 až 2050 po jednom roce. Výroba je brutto z tabulky 6.1 ERÚ. Spotřeba je součet sektorů z tabulky 6.3 ERÚ plus ztráty v sítích jako samostatná položka.
2. **Výchozí stav.** Každá položka začíná změřenou hodnotou za rok 2025 z ERÚ. Pokud ERÚ položku neuvádí zvlášť, začíná od nejlepšího dostupného rozdělení a je to popsané u položky.
3. **Rozklad položky.** Roční elektřina = činnost × intenzita. Například fotovoltaika = instalované MW × hodiny za rok. Fotovoltaika počítá 942 h (průměr MSK 2022 až 2025, P10 889, P90 995, meze odhad), vítr 2 471 h (průměr MSK 2013 až 2025, P10 2 184, P90 2 810).
4. **Odhad s intervalem.** Pro roky 2030, 2040 a 2050 má každá položka hodnoty P10, P50 a P90, zdroj a stupeň důkazu.
5. **Vývoj v čase.** Sloupec `krivka` určuje tvar. Prázdný je logistická křivka (Fisher a Pry 1971) normovaná tak, že S(2025) = 0 a S(2050) = 1, s k a t_m dopočtenými z hodnot pro roky 2030 a 2040. `pchip` je monotónní interpolace přes milníky (Fritsch a Carlson 1980). `tvrdy_skok` je kalendářní skok. `dva_skoky` jsou dva stupně. Velká událost je strmá logistická křivka s k = 4. Položka, která vzroste a klesne, je součet dvou křivek. Vnější vliv je násobek D(t) s D(2025) = 1.
6. **Změna posuvníkem.** Změna cíle se přičítá členem (y_T,nové − y_T,výchozí) · σ(x), kde x = (t − 2030) / 20 omezené na 0 až 1 a σ(x) = 3x² − 2x³. Ztráty v sítích jdou úměrně s ostatní spotřebou.
7. **Agregace.** Simulace Monte Carlo po letech, 10 000 běhů. Losuje se cíl v roce 2050 z P10 až P90 a načasování. Celkový součet nikdy nevzniká sečtením P90 všech položek. Položky se stejnou příčinou se losují částečně společně, korelace 0,6. Pásmo spotřeby v roce 2030 nesmí být užší než pozorované rozpětí pětileté změny 20,6 procentního bodu.
8. **Dva okamžiky.** Zimní špička a letní poledne přepočítávají položky na výkon koeficienty, popis je v `sezonni_metodika.md`. V zimní špičce je vítr podle studie nula, je to nejhorší případ, ne běžná zima.
9. **Hodinový model.** Každá hodina roku 2050 pro 5 povětrnostních let 2015 až 2019, úrovně z tabulky položek, tvary z PVGIS, OPSD a OTE. Přebytek jde do baterie, potom do elektrolyzéru a zbytek je vývoz. Schodek kryje baterie, potom plyn do ročního rozpočtu a zbytek dovoz. Meze: jeden uzel bez sítě, celostátní tvary, baterie bez předvídání.
10. **Výchozí návrh.** Baterie 3 GWh a 750 MW z mediánu denního výkyvu zbytkového zatížení, základ, ne nákladové optimum. Elektrolyzér 631 MW a 3 220 plných hodin při vývozu pod 1 %. Výkon elektrolyzéru = řádky vodíku flotily × (1 + míra ztrát sítě) × 1 000 / plné hodiny. Malá nádrž asi 50 t.
11. **Křížová kontrola.** Výsledek se srovnává s Dopadovou studií a Vnitrostátním plánem. Rozdíl se vysvětlí, ale cílem není se s nimi shodovat. Změny proti studii jsou v přepočtu.

## Stupně důkazu

| Stupeň | Co to je | Příklad |
|---|---|---|
| A | Změřená data | ERÚ, ČSÚ, ČEZ Distribuce |
| B | Publikovaná studie nebo plán | Dopadová studie, Vnitrostátní plán, ČEPS |
| C | Technický výpočet ze známých parametrů | Výkon reaktoru × využití |
| D | Odhad bez publikovaného zdroje | Zatím nezávisle neověřený úsudek |

Stupeň se zapisuje ke každé položce a řídí se nejslabším vstupem.

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
- Ztráty v sítích se řídí součtem spotřeby.

## Výstupy

1. Tabulka položek: vstupy, P10, P50, P90, zdroj, stupeň důkazu, poznámka.
2. Skript, který z tabulky vypočte křivky a pásma.
3. Graf křivek s pásmem, svislými značkami událostí a skutečností do roku 2025.
4. Hodinový přepočet s odpovědí na otázku soběstačnosti.
