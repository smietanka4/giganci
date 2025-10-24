class Uzytkownik():
    imie = ""
    nazwisko = ""
    wiek = 0

    def info(self):
        print(self.imie, self.nazwisko)
        if (self.wiek >= 18):
            print(f"{self.imie} ma {self.wiek} lat, jest pełnoletni")
        else:
            print(f"{self.imie} ma {self.wiek} lat, jest niepełnoletni")

    def zmien_wiek(self, nowy_wiek):
        self.wiek = nowy_wiek

'''
Napisz klasę Przedmiot, która będzie posiadać następujące zmienne:
oceny - lista ocen (musimy stworzyć ją funkcją inaczej wszystkie obiekty będą
korzystały z tej samej listy, rozwiązaniem jest konstruktor ale my jeszcze go nie
znamy) srednia -> średnia wszystkich ocen
Oraz metody:
stworz_liste()
dodaj_ocene(ocena)
wyswietl_oceny()
wyswietl_srednia()
Stwórz kilka obiektów klasy przedmiot np. matematyka, j_polski, historia i
wywołaj ich metody:
'''

class Przedmiot():
    srednia = 0

    def stworz_liste(self): # robimy to dlatego, żeby każdy stworzony obiekt miał oddzielną listę ocen
        self.oceny = []

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)
        self.srednia = sum(self.oceny) / len(self.oceny)