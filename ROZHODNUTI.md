# Rozhodnutí

Zadavatel 2026-11-04 předal všechna rozhodnutí a odhady Claude. Vše zde lze změnit. Nové rozhodnutí přibývá na konec.

| # | Rozhodnutí | Důvod |
|---|---|---|
| 1 | Pásmo je 80 % (P10 až P90). | Širší pásmo by u odhadů předstíralo přesnost, kterou nemáme. |
| 2 | Chybějící odborné odhady zatím dává Claude. Jsou to vstupy stupně D, ověří je lidé. | Bez nich by pásmo nešlo spočítat. Stupeň D je v tabulce vidět. |
| 3 | Procenta konzervativní cesty jsou středové hodnoty pro rok 2050 vůči progresivní cestě. Mají vlastní nejistotu. | Pevný násobek by nejistoty cest úplně svázal. |
| 4 | Plyn v konzervativní cestě je 90 % zemní plyn a 10 % syntetický. CNG/LPG z pracovního seznamu se pro výrobu elektřiny čte jako zemní plyn. | Podle upřesnění zadavatele, výklad paliva je náš. |
| 5 | „Vytápění 300 %“ se čte jako energie na vstupu při stejném teple, ne jako elektřina. Elektřina odpovídá jen části vytápění, která je v konzervativní cestě elektrická. | Trojnásobek odpovídá přechodu z tepelných čerpadel na spalování nebo přímý ohřev. Doslovné čtení by dalo konzervativní cestě víc elektřiny na teplo než elektrifikované. Výklad ověří zadavatel. |
| 6 | SMR je v progresivní cestě 500 MW, v konzervativní není. Rok spuštění je nejistý. | Upřesnění zadavatele. |
| 7 | Odpad 300 tisíc tun za rok není vstup cesty. Položka využití odpadu vychází z jiných zdrojů. | Podle zadavatele je to jen poznámka. |
| 8 | Výroba je výroba brutto z ERÚ, tabulka 6.1. | Je k dispozici po krajích a technologiích. |
| 9 | Spotřeba je součet sektorů z ERÚ, tabulka 6.3, plus ztráty v sítích jako položka. | Tabulka 6.3 má sektory a sedí na ČSÚ, viz níže. Tabulka 6.2 je o 879 GWh nižší a neobsahuje vše. |
| 10 | Výchozí rok je 2025. Rok 2026 se do křivek nebere, známe jen pololetí. | Celý rok 2026 by byl odhad. |
| 11 | Agregace je Monte Carlo s 10 000 běhy a pevným semínkem. Jedna položka drží v čase stejný kvantil. | Výsledek jde zopakovat a křivka položky v běhu neskáče. |
| 12 | Společné faktory jsou tempo elektrifikace, tempo povolování a cena energií. | Položky se stejnou příčinou se hýbou spolu. |
| 13 | Velké události mají v grafu svislou značku na mediánovém roce. | Požadavek zadavatele. |
| 14 | Hlavní graf je roční energie. Graf zimní špičky v MW následuje až po kontrole ročních křivek. | Špička z ročních hodnot přímo neplyne a potřebuje vlastní postup. |
| 15 | Seznam položek je podle `METODIKA.md`. Položka bez měřitelného vlivu může mít hodnotu nula, ale zůstává v tabulce. | Je vidět, že se na ni nezapomnělo. |
| 16 | Stránka je jeden offline soubor `web/bilance.html`. Posuvník nastavuje hodnotu položky v roce 2050, výchozí je P50 a průběh položky se přeškáluje. | První verze je minimalistická, další prvky přibývají postupně. |
| 17 | Pásmo součtů platí jen pro výchozí nastavení. Po změně posuvníku se ukáže vlastní křivka vedle výchozí. | Pásmo pro vlastní nastavení by vyžadovalo nový výpočet. |
| 18 | Vektorové piktogramy a grafiku z FlowSim používáme tam, kde se hodí. Loga CEET a VŠB-TUO ani rastrové obrázky ne. | Pokyn zadavatele. Soubor licenci neuvádí, ale podle zadavatele je volná. |
| 19 | Stránka se zveřejňuje průběžně na GitHub Pages. | Pokyn zadavatele. |
| 20 | Hlavním zdrojem výchozích hodnot je Dopadová studie. Každá výchozí hodnota má stranu v PDF a doslovnou citaci, aby ji šlo ručně zkontrolovat. Jiný zdroj jen tam, kde studie hodnotu nemá. | Pokyn zadavatele, kolega hodnoty kontroluje proti studii. |
| 21 | V hlavním grafu lze vypínat každou cestu a výrobu nebo spotřebu. Aspoň jedna volba ve dvojici zůstává zapnutá. | Pokyn zadavatele. |
| 22 | Každá velká událost má posuvník roku od 2026 do 2050. Položky se stejnou událostí sdílejí rok. | Pokyn zadavatele. Pec v Třinci snižuje hutní plyny a zvyšuje spotřebu ve stejném roce. |
| 23 | Stránka má jednoduchou a podrobnou verzi, výchozí je jednoduchá. V jednoduché jsou skupiny položek a posuvník skupiny mění položky ve stejném poměru vůči výchozím hodnotám. Přepíše tím ruční nastavení položek dané skupiny. | Pokyn zadavatele. Stejný poměr zachová výchozí skladbu skupiny. |
| 24 | Průběh všech položek je jeden vzorec z `METODIKA.md`, bod 5. Podrobná verze má u plynulých položek i rok poloviny změny. | Schváleno zadavatelem. |
| 25 | Nejistota roku poloviny změny je u plynulých položek P10 až P90 o 3 roky kolem výchozího roku a nezávisí na společných faktorech. Společný faktor má korelaci 0,6. | Vlastní odhad, zdroj nemám. Bez nejistoty načasování by pásmo v letech před 2050 bylo příliš úzké. |
| 27 | V progresivní cestě je v roce 2050 flotila 50 % vodík a 50 % baterie. Flotilou rozumíme nákladní dopravu a MHD. Osobní auta na vodík nejezdí a zůstávají na bateriích, vlaky na trolejích. Vodík se vyrábí v kraji z elektřiny a tato elektřina se počítá do spotřeby. Vodík se nevrací zpět na elektřinu. Konzervativní cesta zůstává na bateriích. | Pokyn zadavatele, rozsah flotily a konzervativní cesta jsou náš výklad. |
| 28 | Ze studie ZEVO jsou veřejně jen čísla potřebná k výpočtu: výroba, množství odpadu a rok spuštění. Ekonomika a doslovné citace zveřejněné nejsou. Stránka i export uvádějí, že část zdroje je neveřejná. | Pokyn zadavatele, studie je pracovní verze pro klienta. |
| 29 | Hlavní graf má přepínač Roční energie, Zimní špička a Letní poledne. Výkon v MW se počítá z ročních hodnot a koeficientů v `sezonni_profily.csv`, bez pásma. | Pokyn zadavatele. Sčítání mezí koeficientů by pásmo přehnalo. |
| 30 | Nad posuvníky položek je přepínač a posuvníky velkých trendů: obyvatelé, auta na obyvatele, účinnost aut, potřeba tepla budov a počet domácností. Změna trendu se přičítá rovnoměrně od roku 2025. Pásmo se nepřepočítává. | Pokyn zadavatele. Výchozí křivka zůstává přesně podle tabulky. |
| 31 | Syntetický plyn je z odpadu, elektřina na jeho výrobu je nula. Množství omezuje dostupný odpad po odečtení spalovny. Jiné zdroje, například důlní nebo koksárenský plyn, nejsou započítané, protože chybí podklad. | Pokyn zadavatele. Účinnosti přeměny jsou náš odhad. |
| 32 | Přepínač „Dorovnat na soběstačnost“ ukazuje schodek a kolik fotovoltaiky nebo větru by ho pokrylo. Výchozí hodnoty položek se nemění, jde o přepočet. | Pokyn zadavatele. Soběstačnost je zde roční bilance, ne pokrytí v každé hodině. |
| 33 | SMR se na stránce nastavuje počtem modulů po 500 MW, od 0 do 4. Výchozí je 1 v progresivní cestě a 0 v konzervativní. Jeden modul je 3 942 GWh za rok. Rok spuštění je společný pro všechny moduly. | Pokyn zadavatele. Výpadek největšího bloku model nepočítá. |
| 34 | Stránka má záložku Nedostatky se známými problémy, chybějícími podklady a volbami bez opory ve zdrojích. | Pokyn zadavatele. |
| 35 | Záměr vodíku: přebytek, který se nevejde do baterie, vyrábí vodík pro dopravu a energie zůstává v kraji. Vodík uskladněný v létě sníží výrobu vodíku v zimě, a tím zlepší zimní bilanci. Baterie je krátkodobá a její velikost se určí podle toho, kde se ještě vyplatí. Hodinový model tento postup počítá. | Pokyn zadavatele. Velikost přebytku je nutné ověřit výpočtem. |
| 36 | Do položek je dosazený návrh hodinového výpočtu pro dnešní mix: baterie 1,5 GWh a 375 MW, vodík v MHD 50 % a v nákladní dopravě 4,1 %, auta 0 %. Konzervativní cesta bez přesunu přebytku. Tři dny akumulace ze zadání nejsou v návrhu, protože se jako přesun přebytku nevyplatí. | Cíl je co nejmenší hodinová disparita s vodíkem z přebytku. Práh 100 cyklů za rok je náš odhad. Hodnota zálohy pro výpadek není oceněná. |
| 26 | Hodnoty tabulky pro roky 2030 a 2040 už neurčují křivku přímo, jen z nich dopočítáme k a t_m. Kde to nesedí o více než 10 % a 25 GWh, je to v `web/kontrola_krivek.txt`. | Přesné proložení není u každé položky možné. |

## Vyřešený rozpor: spotřeba 2024

ČSÚ uvádí pro MSK 6 809,0 GWh a součet tabulky 6.2 ERÚ dával 5 931,2 GWh. Součet tabulky 6.3 ERÚ dává 6 810,2 GWh, tedy skoro totéž co ČSÚ. Tabulka 6.2 má jiný rozsah než 6.3. Přesný důvod zbývajícího rozdílu 1,2 GWh není ověřen.
