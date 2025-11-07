class Zwierze():
    def __init__(self, wiek, imie):
        self.wiek = wiek
        self.imie = imie
    
    def wydajDzwiek(self):
        print(f"{self.imie} wydaje dzwiek")
    
    def jedz(self):
        print(f"{self.imie} je")

zwierz1 = Zwierze(12, "Fokus")
zwierz1.wydajDzwiek()
zwierz1.jedz()

class Pies(Zwierze):
    def __init__(self, wiek, imie, rasa):
        super().__init__(wiek, imie) # Dziedziczenie
        self.rasa = rasa

    def wypiszRase(self):
        print(f'{self.imie} jest rasy: {self.rasa}')
        
print()
pies1 = Pies(10, "Klementyna", "Kundel")
pies1.wydajDzwiek()
pies1.jedz()
pies1.wypiszRase()

class Kot(Zwierze):
    def __init__(self, wiek, imie, rasa):
        super().__init__(wiek, imie)
        self.rasa = rasa

    def wypiszRase(self):
        print(f"{self.imie} jest rasy: Brytyjski")

print()
kot1 = Kot(18, "Tygrys", "Dachowiec")
kot1.wydajDzwiek()
kot1.jedz()
kot1.wypiszRase()

print("===== Zadanie 1 =====")

'''
Stworzyć klasę Ptak i dodać metodę lec(), klasa ma dziedziczyć po klasie
Zwierze, oraz dodać kolejna klasę Orzel, dziedziczaca po Ptak, która ma
mieć metodę poluj(), w której wywołujemy metodę lec() z klasy nadrzędnej.
Następnie tworzymy obiekt klasy Orzel i wywołajmy wszystkie metody:

1. Stworzyć klase Ptak, dziedziczaca po Zwierze i dodać metodę lec()
2. Stworzyć klase Orzel, dziedziczaca po Ptak i dodac metode poluj(),
    w której wywołamy metodę lec() z klasy nadrzędnej

3. Stworzyć obiekt Orzel i wywołać wszystkie metody.
'''

class Zwierze():
    def __init__(self, wiek, imie):
        self.wiek = wiek
        self.imie = imie
    
    def wydajDzwiek(self):
        print(f"{self.imie} wydaje dzwiek")
    
    def jedz(self):
        print(f"{self.imie} je")

class Ptak(Zwierze):
    def __init__(self, wiek, imie):
        super().__init__(wiek, imie)

    def lec(self):
        print(f"{self.imie}, leci")

class Orzel(Ptak):
    def __init__(self,wiek,imie):
        super().__init__(wiek,imie)

    def poluj(self):
        self.lec()
        print(f"{self.imie} poluje")

orzel1 = Orzel(5, "Ares")
orzel1.wydajDzwiek()
orzel1.poluj()
orzel1.jedz()



