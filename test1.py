"""
    * Na zpracování máte 60 minut.
    * Celkově je možné získat 20 bodů.
    * Odevzdávejte do odevzdávárny v isu jako jeden .py soubor.


Praktická aplikace:

Vytvořte aplikaci pro rezervaci letenek, která bude reprezentována seznamem ve kterém bude každý let reprezentován jako slovník s následujícími klíči:

'flight_number': číslo letu (řetězec)
'departure': místo odletu (řetězec)
'destination': místo příletu (řetězec)
'available_seats': počet volných sedadel (celé číslo)
'price': cena letu (celé číslo)


Napište následující funkce:

* add_flight(flight): Pokud let s takovým číslem letu neexistuje, přidá nový let do seznamu a vrátí True. Pokud let s takovým číslem letu již existuje, pak ho znovu nepřidá a vrátí False. (3 b.)
* book_flight(flight_number, num_seats): Rezervuje zadaný počet sedadel na letu. Pokud jsou dostupná, aktualizuje počet volných sedadel a vrátí True. Pokud není dostatečný počet volných sedadel, vrátí False. (4 b.) 
* get_available_flights(): Vrátí seznam všech letů s dostupnými sedadly. (4 b.)
* find_flights(departure, destination): Vrátí True nebo False na základě toho, jestli existuje daný let na základě odletového a příletového místa. (3 b.)
* flight_price(price): Vrátí všechny lety, které mají cenu pod zadanou hranici. (3 b.)
* remove_flight(flight_number): Odstraní daný let. Pokud takový let existuje, odstraní ho a vrátí True, pokud neexistuje, vrátí False. (3 b.)

"""

