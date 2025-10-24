from uzytkownik import Przedmiot

matematyka = Przedmiot()
matematyka.stworz_liste()
matematyka.dodaj_ocene(2)
matematyka.dodaj_ocene(3)


print(matematyka.oceny, matematyka.srednia)