import random

class Postac:
      def __init__(self):
            self.nazwa = ""
            self.zycie = 1
            self.max_zycie = 1

      def atakuj(self, przeciwnik):

            atak = random.randint(0,3)

            if atak == 0:
                  print(f"{przeciwnik.nazwa} unika ataku {self.nazwa}")
            else:
                  print(f"{self.nazwa} atakuje {przeciwnik.nazwa}, zadając {atak} obrażeń")
                  przeciwnik.zycie -= atak
      
class Przeciwnik(Postac):
      def __init__(self, gracz):
            super().__init__()
            self.nazwa = random.choice(['zombie','szkielet','pająk','ork','darth vader'])
            self.zycie = random.randint(5, gracz.zycie)

class Gracz(Postac):
      def __init__(self):
            super().__init__()
            self.zycie = 10
            self.max_zycie = 10
            self.nazwa = input("Podaj nazwę gracza: ")

      def odpoczynek(self):
            self.zycie += 1
            if self.zycie > self.max_zycie:
                  self.zycie = self.max_zycie
            print(f"{self.nazwa} odpoczywa, życie: {self.zycie}/{self.max_zycie}")

      def walka(self, przeciwnik):
            walka = True
            while walka:
                  print(f"życie gracza: {self.zycie}")
                  print(f"życie {przeciwnik.nazwa}: {przeciwnik.zycie}")
                  akcja_walki = input("Akcja (atak, uciekaj): ")
                  akcja_walki.lower() # uodparniamy się na przypadkowego caps locka
                  if akcja_walki == 'atak':
                        self.atakuj(przeciwnik)
                        if przeciwnik.zycie <= 0:
                              print(f"{self.nazwa} zabija {przeciwnik.nazwa}")
                              return True
                        przeciwnik.atakuj(self)
                  elif akcja_walki == 'uciekaj':
                        print(f"{self.nazwa} ucieka")
                        przeciwnik.atakuj(self)
                        walka = False
                  else:
                        print("Nieznana akcja")

                  if self.zycie <= 0:
                        print(f'{self.nazwa} ginie')
                        return False
            return True
      

# Główna pętla gry
gracz = Gracz()

gra = True
while gra:
      akcja = input('Akcja (zwiedzaj / odpocznij): ')
      akcja.lower() # Uodparniamy się na przypadkowego caps locka użytkownika
      if akcja == 'zwiedzaj':
            losowanie = random.randint(0,1)
            if losowanie == 1:
                  print(f"{gracz.nazwa} znalazł jaskinie")
            else:
                  przeciwnik = Przeciwnik(gracz)
                  print(f"{gracz.nazwa} natrafił na {przeciwnik.nazwa}")
                  gra = gracz.walka(przeciwnik)
      elif akcja == 'odpocznij':
            gracz.odpoczynek()
      else:
            print("Nieznana akcja")
                  