"""
* Na zpracování máte 60 minut.
* Celkově je možné získat 20 bodů.
* Odevzdávejte do odevzdávárny v isu jako jeden .py soubor.


Praktická aplikace:

Vytvořte aplikaci pro půjčovnu automobilů, která bude reprezentována seznamem, ve kterém bude každý automobil reprezentován jako slovník s následujícími klíči:

'license_plate': registrační značka vozidla (řetězec)
'brand': značka automobilu (řetězec)
'model': model automobilu (řetězec)
'available': informace o tom, zda je automobil dostupný (bool)
'price_per_day': cena za pronájem automobilu na den (celé číslo)


Napište následující funkce:

* add_car(car): Pokud automobil s takovou registrační značkou neexistuje, přidá nový automobil do seznamu a vrátí True. Pokud automobil s takovou registrační značkou již existuje, automobil znovu nepřidá a vrátí False. (3 b.)
* rent_car(license_plate): Pokud automobil s danou registrační značkou existuje a je dostupný, nastaví ho jako nedostupný a vrátí True. Pokud automobil neexistuje nebo již není dostupný, vrátí False. (4 b.)
* get_available_cars(): Vrátí seznam všech automobilů, které jsou aktuálně dostupné. (4 b.)
* find_car(brand, model): Vrátí True nebo False na základě toho, zda existuje alespoň jeden automobil dané značky a modelu. (3 b.)
* cars_by_brand(brand): Vrátí seznam všech automobilů dané značky. (3 b.)
* remove_car(license_plate): Odstraní daný automobil. Pokud takový automobil existuje, odstraní ho a vrátí True, pokud neexistuje, vrátí False. (3 b.)

"""