# Funkcje

def powitanie(imie): # -> definiowanie funkcji
    print(f"Hej, Gigancie {imie}!")

powitanie("Karol")

nick = "smietanka4"
powitanie(nick)

def powitanie2(imie, powtorzenia): # -> funkcja może przyjmować wiele argumentów
    for i in range(powtorzenia):
        print(f"Hej, {imie}!")

powitanie2("Karol", 2)

print("====== Zadanie 1 ======")

'''
Przygotuj funkcję obliczającą pole prostokąta. 
Funkcja ma przyjmować długości boków, a następnie obliczać i
wyświetlać pole figury.
'''

def prostokat(bok_a, bok_b):
    pole = bok_a * bok_b
    print(f"Pole prostokąta o bokach {bok_a}x{bok_b} = {pole}")

prostokat(3,4)

print("======= Zadanie przykładowe =======") # -> Wartości domyślne argumentów

import time

# def pasek_ladowania(gotowe, wszystko=100):
#     # Znak '#' oznacza wykonaną część
#     # Znak '-' oznacza niewykonaną część

#     # Zmiana skali postępu z 'wszystko' na 10
#     wykonane = round(10 * gotowe/wszystko)
#     niewykonane = 10 - wykonane

#     # Obliczanie ile znaków ma sie pojawic
#     tekst_wykonane = "#" * wykonane
#     tekst_niewykonane = "-" * niewykonane

#     print(f'\r[{tekst_wykonane}{tekst_niewykonane}]', end=' ')

# for i in range(100):
#     pasek_ladowania(i)
#     # pasek_ladowania(i)
#     time.sleep(0.1)

# Przekazywanie wartości funkcji, trzy sposoby

print("========= ZADANIE 2 =========")

'''
Napisz funkcję, która przyjmuje dwa argumenty: n - liczba powtórzeń, a -
liczba startowa. Funkcja ma generować kolejne kwadraty liczb, zaczynając od a. Ma
wyświetlić n kolejnych liczb.
'''

# przykład: n = 5, a = 3 -> 3*3 = 9, 4*4 = 16, 5*5 = 25, 6*6 = 36, 7*7 = 49

def kwadraty(a, n):
    for i in range(a, a + n):
        print(f"{i} ** 2 = {i ** 2}")

kwadraty(3, 5)

# Wartości zwracane

def sum(a,b): 
    suma = a + b
    return suma # -> return (z ang. "zwracać", zwraca nam jakąś wartość)

suma1 = sum(3,5)
suma2 = sum(4,4)
print(suma1, suma2)

print("====== ZADANIE 3 ======")

'''
Napisz funkcję tworzącą powitanie, które wykorzystuje jako argument imie a zwraca
pełen tekst powitania.
'''

def powitanie_return(imie):
    return f"Hej {imie}! :)"

print(powitanie_return("Karol"))

print("====== ZADANIE 4 ======")

'''
Napisz funkcję obliczającą objętość graniastosłupa prawidłowego o podstawie kwadratu. 
'''

def pole_podstawy(a):
    return a*a

def obj_graniastoslupa(bok_podstawy, wysokosc):
    pole = pole_podstawy(bok_podstawy)
    return pole * wysokosc

print(obj_graniastoslupa(3, 10))

















