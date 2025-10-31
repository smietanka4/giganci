'''
Stwórzmy klasę samochód, która będzie zawierać informacje o marce, modelu, typieSilnika, mocKM.
I do tego metodę wyświetl(), która wyświetli te informacje
'''

class Samochod(): # Klasa
      licznik1 = 0 # Licznik1 jest powiązany z klasą nie z obiektem (wartość globalna)

      def __init__(self, marka, model, typSilnika, mocKm): # Konstruktor
            print("Utworzenie obiektu Samochod")
            self.licznik2 = 9 # każdy utworzony obiekt, ma swój licznik2
            Samochod.licznik1 += 1 # dodajemy do licznika1 za każdym razem jak stworzymy obiekt z klasy Samochod 
            self.marka = marka
            self.model = model
            self.typSilnika = typSilnika
            self.mocKm = mocKm

      def wyswietl(self): # metoda wyswietl()
            print(self.marka)
            print(self.model)
            print(self.typSilnika, ":", self.mocKm)

print(Samochod.licznik1)
auto1 = Samochod("Honda", "Accord VII", "iVTEC 2.4 Benzyna", 240) # Obiekt
print(Samochod.licznik1)
auto2 = Samochod("Mazda", "6", "1.6 Benzyna", 200)
print(Samochod.licznik1)
print(auto1.licznik2)
print(auto2.licznik2)

# auto1.wyswietl()

print("====== Zadanie 2 ======")

'''
Celem zadania jest stworzenie 2 klas: Kolo i Kwadrat. 
Klasy mają być odpowiedzialne za przechowywanie odpowiednich dla danej figury
geometrycznej wymiarów oraz posiadać metody wyświetlające pole i obwód tych
figur.

pole koła: (Pi=3.14) * (r**2)
obwód koła: 2 * Pi * r
'''

class Kolo():
      def __init__(self, r):
            self.promien = r
            self.pole = 3.14 * r * r
            self.obwod = 2 * 3.14 * r

      def wyswietlPole(self):
            print(f"Pole koła o promieniu {self.promien} wynosi {self.pole}")

      def wyswietlObwod(self):
            print(f"Obwód koła o promieniu {self.promien} wynosi {self.obwod}")

class Kwadrat():
      def __init__(self, x):
            self.bok = x
            self.pole = x*x
            self.obwod = 4*x

      def wyswietlPole(self):
            print(f"Pole kwadratu o boku {self.bok} wynosi {self.pole}")

      def wyswietlObwod(self):
            print(f"Obwód kwadratu o boku {self.bok} wynosi {self.obwod}")

kolo = Kolo(4)
kolo.wyswietlObwod()
kolo.wyswietlPole()

kwadrat = Kwadrat(67)
kwadrat.wyswietlObwod()
kwadrat.wyswietlPole()



