# Metodika křivek výroby a spotřeby elektřiny v MSK (návrh, 2026-11-04)

Zatím neobsahuje žádné odhady hodnot. Schvaluje se nejdřív postup, potom položky a nakonec čísla.

## Co křivky znamenají

Křivka říká, kolik elektřiny by kraj vyráběl a spotřeboval, pokud by se vydal danou cestou. Není to předpověď, která z cest nastane.
Pásmo kolem křivky vyjadřuje nejistotu uvnitř jedné cesty. Rozdíl mezi cestami je volba, ne nejistota.
Pásmo je interval věrohodnosti 80 %, tedy P10 až P90. Není to statistický interval spolehlivosti, protože budoucnost nemá výběr dat. V textu to řekneme přímo.

## Postup

1. **Hranice a bilance.** Území kraje, jen elektřina, roky 2025 až 2050 po jednom roce. Výroba je brutto z tabulky 6.1 ERÚ. Spotřeba je součet sektorů z tabulky 6.3 ERÚ plus ztráty v sítích jako samostatná položka. Skutečnost i odhady používají stejnou definici.
2. **Výchozí stav.** Každá položka začíná změřenou hodnotou za rok 2025 z ERÚ. Pokud ERÚ položku neuvádí zvlášť, začíná od nejlepšího dostupného rozdělení a zdokumentuje se.
3. **Rozklad položky.** Roční elektřina = činnost × intenzita. Například fotovoltaika = instalované MW × vyrobené MWh na MW. Elektromobily = počet aut × km za rok × kWh na km. Odhaduje se činnost a intenzita, ne přímo výsledek.
4. **Odhad s intervalem.** Pro roky 2030, 2040 a 2050 má každý vstup hodnoty P10, P50 a P90, zdroj a stupeň důkazu.
5. **Vývoj v čase.** Každá položka má tvar y(t) = D(t) · s(t), kde s(t) = s₀ + (s_T − s₀) · S(t). S(t) je logistická křivka normovaná tak, že S(2025) = 0 a S(2050) = 1. D(t) je vnější vliv s indexem D(2025) = 1, například demografie nebo účinnost. Parametry k a t_m se dopočtou z hodnot pro roky 2030 a 2040. Velká událost je strmá S-křivka s k = 4 a t_m v roce události. Položka, která vzroste a klesne, je součet dvou S-křivek. Změna cíle uživatelem se přičítá členem (y_T,nové − y_T,výchozí) · σ(x), kde x = (t − 2030) / 20 omezené na 0 až 1 a σ(x) = 3x² − 2x³. Do roku 2030 tak křivka zůstává a v roce 2050 přesně trefí nový cíl. Ztráty v sítích jdou úměrně s ostatní spotřebou.
6. **Velké události.** Odstavení uhelných bloků, spuštění SMR, změna výroby oceli nebo velké datacentrum jsou skoky se samostatným rokem a jeho nejistotou. V grafu mají svislou značku s popisem na nejpravděpodobnějším roce.
7. **Agregace.** Simulace Monte Carlo po letech, 10 000 běhů. Losuje se cíl v roce 2050 z P10 až P90 a načasování t_m. Celkový součet nikdy nevzniká sečtením P90 všech položek, protože by to pásmo přehnalo.
8. **Společné faktory.** Položky závislé na stejné příčině se losují společně: tempo elektrifikace, cena energií, tempo povolování, počasí. Úplná nezávislost by naopak pásmo uměle zúžila.
9. **Kontrola fyzikálních mezí.** Plocha pro fotovoltaiku a vítr, potenciál biomasy, kapacita sítě, dostupnost tepelných čerpadel. Hodnota nad mezí se opraví, ne ořízne bez poznámky.
10. **Křížová kontrola.** Výsledek se srovná s Dopadovou studií a Vnitrostátním plánem. Rozdíl se vysvětlí, ale cílem není se s nimi shodovat.
11. **Citlivost.** Pro každou cestu se ukáže, které položky nejvíc rozšiřují pásmo. Tam se má hledat lepší důkaz.

## Stupně důkazu

| Stupeň | Co to je | Příklad |
|---|---|---|
| A | Změřená data | ERÚ, ČSÚ, ČEZ Distribuce |
| B | Publikovaná studie nebo plán | Dopadová studie, Vnitrostátní plán, ČEPS |
| C | Technický výpočet ze známých parametrů | Výkon reaktoru × využití |
| D | Odborný odhad | Nezávislé odhady P10, P50, P90 od dvou a více lidí, poté společná shoda |

Stupeň se zapisuje ke každému vstupu. Bez zdroje nebo jmenovaného odhadu vstup do výpočtu nevstoupí.

## Položky

Tučně jsou položky navíc proti pracovnímu seznamu v `KONTEXT_SCENARE.md`.

### Výroba

- Stávající zdroje: černé uhlí, **hnědé uhlí**, zemní plyn, **hutní plyny (vysokopecní a koksárenský)**, **důlní plyn**
- OZE: fotovoltaika střešní, fotovoltaika pozemní, vítr, **malé vodní elektrárny**, biomasa, bioplyn, **geotermální energie**
- Nové zdroje: SMR, nové plynové bloky, syntetický plyn a biometan, **energetické využití odpadu**
- Skladování a zálohy: baterie, **jiné skladování**, **vodík zpět na elektřinu**. Nejsou to zdroje, do roční bilance vstupují jen ztrátami.

### Spotřeba

- Těžký průmysl: Třinecké železárny, Nová huť, **ostatní průmysl a chemie**, **doly**
- Budovy: **domácnosti bez vytápění**, **služby a veřejný sektor**, vytápění tepelnými čerpadly, **přímotopy**, **elektrokotle v teplárnách**, **chlazení**
- Doprava: osobní auta, nákladní doprava, vlaky, MHD
- Nové zátěže: datacentra, **výroba vodíku**, **výroba syntetického plynu**
- Soustava: **vlastní spotřeba zdrojů**, **ztráty v sítích**, **ztráty baterií**
- Ostatní: **zemědělství a stavebnictví**, **úspory a účinnost** jako záporná položka

### Vazby, které se musí počítat společně

- Elektrifikace oceláren snižuje výrobu z hutních plynů a zvyšuje spotřebu elektřiny.
- Vodík a syntetický plyn spotřebují elektřinu dřív, než část z ní vrátí.
- Teplárna vyrábí elektřinu podle poptávky po teple, takže přechod na tepelná čerpadla mění i výrobu.
- Velikost datacenter a elektrifikace zvyšují nároky na síť, kterou má konzervativní cesta dvakrát více zatíženou.

## Výstupy

1. Tabulka položek: vstupy, P10, P50, P90, zdroj, stupeň důkazu, poznámka.
2. Skript, který z tabulky vypočte křivky a pásma.
3. Graf se čtyřmi křivkami, pásmy, svislými značkami událostí a skutečností do roku 2025.
4. Graf citlivosti a srovnání s publikovanými scénáři.
