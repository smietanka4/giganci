import random


# ZMIENNE

kosci = [2,1,3,6,4]
nazwy_punktow = ["Jedynki", "Dwójki", "Trójki", "Czwórki", "Piątki", "Szóstki"]
punkty = ['','','','','','']

# FUNKCJE

def rzuc_koscmi(numery_kosci: str):
      # Funkcja do losowania podanych przez użytkownika kości
      for i in numery_kosci:
            index = int(i) - 1
            kosci[index] = random.randint(1,6)

def pokaz_kosci():
      # Funkcja do wyświetlania kości
      print("============================")
      for i in range(len(kosci)):
            print(f'{i+1}. {kosci[i]}')
      print("============================")
      
def sprawdz_czy_przerzucamy():
      # Funkcja sprawdzająca czy chcemy przerzucić kości? Jeżeli tak zwracamy prawdę, jeżeli nie to Fałsz
      print("Czy chcesz przerzucić kości? (t/n)")
      wybor = input()
      if wybor == 't' or wybor == 'T':
            return True
      else:
            return False

def pokaz_tabele_punktow():
      # Funkcja wyświetlająca tabele punktową
      print("============================")
      for i in range(len(punkty)):
            print(f'{i+1}. {nazwy_punktow[i]}\t{punkty[i]}')
      print("============================")
      
def wstaw_punkty():
      # Główna funkcja wstawiająca punkty
      pole = int(input('Gdzie chcesz wstawić punkty (podaj numer rubryki): '))
      if punkty[pole-1] == '':
            if 1 <= pole <= 6:
                  wstaw_w_liczbowym(pole)
      else:
            print("Wybrałeś pole, w którym już wstawiłeś punkty")
            wstaw_punkty()

def wstaw_w_liczbowym(liczba):
      # Górna część tabeli, oblicza nam punkty dla wyborów od 1 do 6
      liczba_punktow = 0
      for kosc in kosci:
            if kosc == liczba:
                  liczba_punktow += kosc
      punkty[liczba-1] = liczba_punktow

# GŁÓWNY PROGRAM
for tura in range(len(punkty)):
      rzuc_koscmi("12345")
      pokaz_tabele_punktow()
      pokaz_kosci()

      for _ in range(2):
            czy_przerzut = sprawdz_czy_przerzucamy()
            if czy_przerzut:
                  kosci_do_przerzutu = input("Wypisz numery kości, które chcesz przerzucić (bez spacji): ")
                  rzuc_koscmi(kosci_do_przerzutu)
                  pokaz_kosci()
            else:
                  break

      pokaz_tabele_punktow()
      pokaz_kosci()
      wstaw_punkty()
      pokaz_tabele_punktow()

