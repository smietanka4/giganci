print("======= ZADANIE 1 =======")

'''
Utwórz trzy zmienne, do których wpisz wartość 3 jako odpowiedni typ:
- x_int - jako liczba całkowita
- x_float - jako liczba z przecinkiem
- x_str - jako napis
'''

x_int = 3
print(type(x_int))
x_float = 3.0
print(type(x_float))
x_str = "3"
print(type(x_str))

print("======= ZADANIE 2 =======")

'''
Utwórz zmienną napis_liczba, która przechowuje wartość "290".
Utwórz zmienną x. Użyj konwersji z typu str na typ int, aby zmienna x
przechowywała to co napis_liczba, ale jako typ liczby całkowitej
'''

napis_liczba = "290"
x = int(napis_liczba)
print(type(x))

print("======= ZADANIE 3 =======")

'''
Utwórz 3 zmienne:
- pole_trojkata
- podstawa_trojkata
- wysokosc_trojkata

Do podstawa_trojkata oraz wysokosc_trojkata powinny trafić wartości odczytane z
konsoli (od użytkownika).

Oblicz pole takiego trójkąta i zapisz wynik w zmiennej pole_trojkata
Wyświetl wynik jako komunikat:

"Pole trójkąta o podstawie XX oraz wysokości XX wynosi XX"
'''


podstawa_trojkata = float(input("Podaj dlugość podstawy trójkąta"))
wysokosc_trojkata = float(input("Podaj wysokość trójkąta"))
pole_trojkata = (podstawa_trojkata * wysokosc_trojkata / 2)

print(f"Pole trójkąta o podstawie {podstawa_trojkata} oraz wysokości {wysokosc_trojkata} wynosi {pole_trojkata}")

print("======= ZADANIE 4 =======")

'''
Zapytaj użytkownika o jego wiek i na tej podstawie wyświetla w konsoli jeden z
komunikatów:
- Jesteś pełnoletni/a
- Nie jesteś jeszcze pełnoletni/a. Brakuje Ci XX lat do 18 roku życia

Zamiast XX powinna pojawić się wartość liczbowa
'''

wiek = int(input("Podaj swój wiek (w latach): "))

if wiek >= 18:
      print("Jesteś pełnoletni/a")
else:
      print(f"Nie jesteś jeszcze pełnoletni/a. Brakuje Ci {18-wiek} lat do 18 roku życia")

print("======= ZADANIE 5 =======")

'''
Cena atrakcji turystycznej zależy od miesiąca. Napisz program, który zapyta
użytkownika o liczbę biletów oraz miesiąc, w którym chce odwiedzić park
rozrywki i na tej podstawie obliczy koszt transakcji.
Koszt biletu w danym miesiącu (miesiąc jako numer -> koszt biletu):
- 1 -> 50 zł
- 2 -> 50 zł
- 3 -> 100 zł
- 4 -> 100 zł
- 5 -> 200 zł
- 6 -> 200 zł
- 7 -> 250 zł
- 8 -> 200 zł
- 9 -> 200 zł
- 10 -> 100 zł
- 11 -> 100 zł
- 12 -> 50 zł
Wyświetl komunikat:
"Cena biletów: XX zł"

XX to wartość liczbowa

Jeśli wprowadzono niepoprawny numer miesiąc program powinien wyświetlić
informację:
"Wprowadzono niepoprawny numer miesiąca. Spróbuj ponownie"
'''

liczba_biletow = int(input("Podaj liczbę biletów: "))

poprawnosc = True

while poprawnosc:
      miesiac = int(input("Podaj miesiac odwiedzenia atrakcji: "))
      if miesiac > 12 or miesiac < 1:
            print("Wprowadzono niepoprawny numer miesiąca. Spróbuj ponownie")
      else:
            if miesiac == 1 or miesiac == 2 or miesiac == 12:
                  cena_biletu = 50
                  kwota = liczba_biletow * cena_biletu
            elif miesiac == 3 or miesiac == 4 or miesiac == 10 or miesiac == 11:
                  cena_biletu = 100
                  kwota = liczba_biletow * cena_biletu
            elif miesiac == 5 or miesiac == 6 or miesiac == 8 or miesiac == 9:
                  cena_biletu = 200
                  kwota = liczba_biletow * cena_biletu
            else:
                  cena_biletu = 250
                  kwota = liczba_biletow * cena_biletu

            print(f"Cena biletów: {kwota} zł")
            poprawnosc = False

print("======= ZADANIE 6 =======")

'''
Napisz program, który zapyta użytkownika o liczbę, a następnie wypisze na
ekranie tyle wyników z rzutu kością sześcienną.
Rzut kością sześcienną to wynik z losowania liczby od 1 do 6 (włącznie).
'''

import random

liczba_rzutow = int(input("Podaj liczbę rzutów kostką: "))

for _ in range(liczba_rzutow):
      print(random.randint(1, 6))

print("======= ZADANIE 7 =======")

'''
Napisz funkcję, która przyjmuje 2 argumenty:
- tekst, typu str
- n, typu int
a zwraca nowy napis, który powstaje poprzez połączenie text n razy.
'''

def laczenie_slow(tekst: str, n: int) -> str:
      nowy_tekst = ""
      for _ in range(n):
            nowy_tekst += tekst
      return nowy_tekst

print(laczenie_slow("Kotek", 3))


print("======= ZADANIE 8 =======")

'''
Przygotuj funkcję, która otrzymuje jeden argument: n - liczbę elementów.
Funkcja ma zwrócić listę n - losowych elementów od 0 do 100
Wywołaj ją kilka razy, aby sprawdzić, czy za każdym razem zwraca różne wartości
'''

import random

def losowa_tablica(n: int) -> list:
      lista = []
      for _ in range(n):
            lista.append(random.randint(0, 100))
      return lista

print(losowa_tablica(10))
print(losowa_tablica(9))
print(losowa_tablica(8))







