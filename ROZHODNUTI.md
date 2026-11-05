# Rozhodnutí

Rejstřík voleb modelu. Vše lze změnit. Nové rozhodnutí přibývá na konec.

| # | Rozhodnutí | Důvod |
|---|---|---|
| 1 | Pásmo je 80 % (P10 až P90). | Širší pásmo by u odhadů předstíralo přesnost, kterou nemáme. |
| 2 | Chybějící odborné odhady jsou vstupy stupně D a zatím je nikdo nezávisle neověřil. | Bez nich by pásmo nešlo spočítat. Stupeň D je v tabulce vidět. |
| 3 | Procenta konzervativní cesty jsou středové hodnoty pro rok 2050 vůči progresivní cestě. Mají vlastní nejistotu. | Pevný násobek by nejistoty cest úplně svázal. |
| 4 | Plyn v konzervativní cestě je 90 % zemní plyn a 10 % syntetický. CNG/LPG z definice cesty se pro výrobu elektřiny čte jako zemní plyn. | Procenta jsou součást definice cesty, výklad paliva je náš. |
| 5 | „Vytápění 300 %“ se čte jako energie na vstupu při stejném teple, ne jako elektřina. Elektřina odpovídá jen části vytápění, která je v konzervativní cestě elektrická. | Trojnásobek odpovídá přechodu z tepelných čerpadel na spalování nebo přímý ohřev. Doslovné čtení by dalo konzervativní cestě víc elektřiny na teplo než elektrifikované. |
| 6 | SMR je v progresivní cestě 500 MW, v konzervativní není. Rok spuštění je nejistý. | Je to součást definice cest. |
| 7 | Odpad 300 tisíc tun za rok není vstup cesty. Položka využití odpadu vychází z jiných zdrojů. | Údaj je jen orientační poznámka v definici cesty. |
| 8 | Výroba je výroba brutto z ERÚ, tabulka 6.1. | Je k dispozici po krajích a technologiích. |
| 9 | Spotřeba je součet sektorů z ERÚ, tabulka 6.3, plus ztráty v sítích jako položka. | Tabulka 6.3 má sektory a sedí na ČSÚ, viz níže. Tabulka 6.2 je o 879 GWh nižší a neobsahuje vše. |
| 10 | Výchozí rok je 2025. Rok 2026 se do křivek nebere, známe jen pololetí. | Celý rok 2026 by byl odhad. |
| 11 | Agregace je Monte Carlo s 10 000 běhy a pevným semínkem. Jedna položka drží v čase stejný kvantil. | Výsledek jde zopakovat a křivka položky v běhu neskáče. |
| 12 | Společné faktory jsou tempo elektrifikace, tempo povolování a cena energií. | Položky se stejnou příčinou se hýbou spolu. |
| 13 | Velké události mají v grafu svislou značku na mediánovém roce. | Rok události má být v grafu čitelný. |
| 14 | Hlavní graf je roční energie. Zimní špička a letní poledne jsou další pohledy, viz rozhodnutí 29. | Špička z ročních hodnot přímo neplyne a potřebuje vlastní postup. |
| 15 | Seznam položek je podle metodiky. Položka bez měřitelného vlivu může mít hodnotu nula, ale zůstává v tabulce. | Je vidět, že se na ni nezapomnělo. |
| 16 | Stránka je jeden soubor s daty uvnitř. Posuvník nastavuje hodnotu položky v roce 2050, výchozí je P50 a průběh položky se přeškáluje. | První verze je minimalistická, další prvky přibývají postupně. |
| 17 | Pásmo součtů platí jen pro výchozí nastavení a po změně posuvníku se nepřepočítává. | Pásmo pro vlastní nastavení by vyžadovalo nový výpočet. |
| 18 | Vektorové piktogramy a grafiku lze použít tam, kde se hodí. Rastrové obrázky a loga ne. | Stránka má zůstat lehká a vektorová. |
| 19 | Stránka se zveřejňuje průběžně na GitHub Pages. | Stránka má být dostupná bez instalace. |
| 20 | Hlavním zdrojem výchozích hodnot je Dopadová studie. Každá výchozí hodnota má stranu v PDF a doslovnou citaci, aby ji šlo ručně zkontrolovat. Jiný zdroj jen tam, kde studie hodnotu nemá. | Každá hodnota má jít zkontrolovat proti studii. |
| 21 | V hlavním grafu lze vypínat výrobu nebo spotřebu. Aspoň jedna z nich zůstává zapnutá. | Graf má jít zúžit na jednu stranu bilance. |
| 22 | Každá velká událost má posuvník roku od 2026 do 2050. Položky se stejnou událostí sdílejí rok. | Pec v Třinci snižuje hutní plyny a zvyšuje spotřebu ve stejném roce. |
| 23 | Stránka má jednoduché posuvníky po skupinách a podrobné po položkách, ty jsou sbalené. Posuvník skupiny mění položky ve stejném poměru vůči výchozím hodnotám. Přepíše tím ruční nastavení položek dané skupiny. | Stejný poměr zachová výchozí skladbu skupiny. |
| 24 | Průběh položek je logistická křivka, monotónní interpolace přes milníky, nebo kalendářní skok, podle sloupce v tabulce. Podrobná verze má u plynulých položek i rok poloviny změny. | Všechny položky se tak počítají popsaným postupem. |
| 25 | Nejistota roku poloviny změny je u plynulých položek P10 až P90 o 3 roky kolem výchozího roku a nezávisí na společných faktorech. Společný faktor má korelaci 0,6. | Vlastní odhad bez zdroje. Bez nejistoty načasování by pásmo v letech před 2050 bylo příliš úzké. |
| 26 | Hodnoty tabulky pro roky 2030 a 2040 určují u logistických položek k a t_m. Kde to nesedí o více než 10 % a 25 GWh, je to v seznamu kontroly křivek. | Přesné proložení není u každé položky možné. |
| 27 | V progresivní cestě je v roce 2050 flotila 50 % vodík a 50 % baterie. Flotilou rozumíme nákladní dopravu a MHD. Osobní auta na vodík nejezdí a zůstávají na bateriích, vlaky na trolejích. Vodík se vyrábí v kraji z elektřiny a tato elektřina se počítá do spotřeby. Vodík se nevrací zpět na elektřinu. Konzervativní cesta zůstává na bateriích. | Podíl je součást definice cesty, rozsah flotily a konzervativní cesta jsou výklad modelu. |
| 28 | Ze studie o energetickém využití odpadu jsou veřejně jen čísla potřebná k výpočtu: výroba, množství odpadu, rok spuštění a výhřevnost. Stránka i export uvádějí, že část zdroje je neveřejná. | Zdroj je neveřejná studie, uvedena jsou jen čísla potřebná k výpočtu. |
| 29 | Hlavní graf má přepínač Roční energie, Zimní špička a Letní poledne. Výkon v MW se počítá z ročních hodnot a koeficientů položek, bez pásma. | Sčítání mezí koeficientů by pásmo přehnalo. |
| 30 | Pod posuvníky položek je sbalený přepínač a posuvníky velkých trendů: obyvatelé, auta na obyvatele, účinnost aut, účinnost nákladních aut, potřeba tepla budov a počet domácností. Změna trendu se přičítá rovnoměrně od roku 2025. Pásmo se nepřepočítává. | Výchozí křivka zůstává přesně podle tabulky. |
| 31 | Syntetický plyn je z odpadu, elektřina na jeho výrobu není vyčíslena a řádek je nula. Množství omezuje dostupný odpad po odečtení spalovny. Jiné zdroje, například důlní nebo koksárenský plyn, nejsou započítané, protože chybí podklad. | Účinnosti přeměny jsou odhad modelu. |
| 32 | Nahrazeno rozhodnutím 41. | Viz rozhodnutí 41. |
| 33 | SMR se na stránce nastavuje počtem modulů po 500 MW, od 0 do 4. Výchozí je 1 v progresivní cestě a 0 v konzervativní. Jeden modul je 3 942 GWh za rok. Rok spuštění je společný pro všechny moduly. | Výpadek největšího bloku je jen případ v přepočtu, oddíl 8. |
| 34 | Stránka má záložku Nedostatky se známými problémy, chybějícími podklady a volbami bez opory ve zdrojích. | Slabá místa mají být vidět. |
| 35 | Přebytek, který se nevejde do baterie, vyrábí vodík pro dopravu a energie zůstává v kraji. Hodinový model tento postup počítá. | Výpočet ukázal, že přebytek flotilu neuživí, viz rozhodnutí 40. |
| 36 | Nahrazeno rozhodnutími 37 až 40. | Dřívější návrh s menší baterií a malým podílem vodíku neplatí. |
| 37 | Baterie v progresivní cestě je v roce 2050 2,6 GWh a 650 MW, trvání 4 hodiny. Řádek ztráty baterií je 67,4 GWh, nabito minus vybito. Přebytek má přednost, v hodinách s nízkým zbytkovým zatížením se nabíjí i ze sítě podle křivky na další den, denní špička nestoupne. Pravidlo jen z přebytku zůstává jako varianta. | Základ je medián denního výkyvu zbytkového zatížení 2,64 GWh a 582 MW. Je to základ návrhu, ne nákladové optimum. Změřený pokles zimní špičky před plynem: medián 142 MW, nejhorší rok 55 MW. |
| 38 | Elektrolyzér je 550 MW a 3 758 plných hodin, vývoz je pod 1 % přebytku. Výkon = řádky vodíku flotily × (1 + míra ztrát sítě) × 1 000 / plné hodiny. Nulový vývoz by stál 1 177 MW. | Tabulka, stránka a hodinový výpočet mají jednu definici a jednu hodnotu. Řádek 45,8 GWh ze studie je rovnoměrná zátěž mimo tento výkon. |
| 39 | Výchozí je malá provozní nádrž asi 50 t. Plná sezónní nádrž 10 035 t zůstává ukázaná jako drahá možnost. | Nejmenší vývoz je prakticky hotový do 50 t. Plná nádrž hlavně přesouvá výrobu ze zimy do zbytku roku. |
| 40 | Flotila je MHD 50 %, nákladní doprava 50 %, auta 0 %. Stránka přímo říká, že vodík je asi z 98 % z elektřiny ze sítě. | Přebytek je jen 334 GWh za rok, flotila potřebuje 2 067 GWh. |
| 41 | Místo přepínače dorovnání je na stránce blok Co by muselo platit s ročními a zimními požadavky, mezí větru 2 014 MW a tempem výstavby proti historickému maximu. V grafu zůstává jen decentní výplň schodku. | Dorovnání bylo jen šrafování a neříkalo, zda je to proveditelné. |
| 42 | Ztráty v sítích se řídí vzorcem ze součtu spotřeby, stejným v obou cestách, r = 3,547 %: 431,8 GWh v progresivní a 267,1 GWh v konzervativní cestě. | Míra rostoucí se zátěží nemá zdroj pro rozdělení 30/70 a vyšší zátěž by šla se zesílením sítě. Účinek varianty je v otevřených rozhodnutích. |
| 43 | Rezerva pro výpadek nemá přepínač. Metodika má tabulku podílu zatížení krát hodiny. | Rezerva bilanci nemění a žádný zdroj neuvádí kritickou zátěž kraje v MW. |
| 44 | Zimní špička má vítr nula podle studie. Druhý stav se nepřidává. | Je to nejhorší případ, ne běžná zima. Metodika to říká jednou větou. |
| 45 | Hodiny pro rok 2050 jsou fotovoltaika 942 h a vítr 2 471 h, stejné MW. | Průměr změřených let ERÚ pro MSK, fotovoltaika 2022 až 2025, vítr 2013 až 2025. Čísla studie zůstávají citovaná. |
| 46 | Jedna volba cesty řídí křivky, bilanci, bloky i posuvníky: Progresivní, Konzervativní. Přepínač Ukázat i druhou cestu jen přidá do grafu křivky druhé cesty. | Dvě volby na dvou místech byly matoucí. |
| 47 | Otevřené a nezapracované: podíl větru kraje 13,07 %, přesun 420 GWh ostatního průmyslu, kWh na km u aut, vodík 55,1 kWh/kg, datacentra, druhý SMR, využití SMR 90 % proti měřeným 79 až 84,4 %, míra ztrát rostoucí se zátěží. | Přesný účinek každého je v přepočtu, oddíl 9. Hodnoty zůstávají, dokud se nerozhodne. |
| 48 | Třinec počítá 300 kWh/t, oblouková pec v obou cestách stejně, stupeň D. | Tiskový údaj dává 180 kWh/t, Nová huť 450 kWh/t. 300 kWh/t je úsudek o čistém nárůstu. |
| 49 | Syntetický plyn z odpadu je 115,2 GWh, 0,48 MWh/t podle studie s.137. Elektřina na jeho výrobu je viditelně neznámá. | Studie s.169 uvádí vysokou spotřebu bez čísla. |
| 50 | Vodík počítá 51,36 kWh/kg: elektrolyzér 48,26 a změřená komprese 3,1. | 2,23 kWh/kg je v DOE 9013 modelový údaj. Hodnota 55,1 kWh/kg zůstává otevřená. |
| 51 | Elektrokotle nejvýš 70 MW podle studie s.166, berou jen přebytek po baterii. | Řádek je výsledek hodinového běhu, ne vstup. |
| 52 | SMR je v progresivní cestě daný. Los mění výkon a rok do 2050, případ bez SMR je samostatný. Podíl běhů se uvádí jako pásmo. | Dřívější podíl bez SMR plynul z jednoho odhadnutého roku 2055. |
| 53 | Plynové bloky mají výkon z Tab.30 nezávisle na energii: 433 MW v progresivní, 683 MW v konzervativní cestě. Palivo je rozpočet řádků. Biometan řádek nemá. | Studie pro kraj číslo nedává, 635 GWh je v otevřených bodech. |
| 54 | Vlastní spotřeba zdrojů je vzorec z výroby v každém roce a běhu, včetně SMR. | Jeden blok dá čistě 3 632 GWh. |
| 55 | Plánovaná odstávka SMR je od poloviny dubna, druhý blok od poloviny září. | Předpoklad, sken nejnižší zbytkové špičky přes 5 let. |
| 56 | Stupeň se řídí nejslabším vstupem hodnoty P50 pro rok 2050. | Jedno pravidlo místo dvou. |

## Vyřešený rozpor: spotřeba 2024

ČSÚ uvádí pro MSK 6 809,0 GWh a součet tabulky 6.2 ERÚ dával 5 931,2 GWh. Součet tabulky 6.3 ERÚ dává 6 810,2 GWh, tedy skoro totéž co ČSÚ. Tabulka 6.2 má jiný rozsah než 6.3. Přesný důvod zbývajícího rozdílu 1,2 GWh není ověřen.
