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

def pasek_ladowania(gotowe, wszystko=100):
    # Znak '#' oznacza wykonaną część
    # Znak '-' oznacza niewykonaną część

    # Zmiana skali postępu z 'wszystko' na 10
    wykonane = round(10 * gotowe/wszystko)
    niewykonane = 10 - wykonane

    # Obliczanie ile znaków ma sie pojawic
    tekst_wykonane = "#" * wykonane
    tekst_niewykonane = "-" * niewykonane

    print(f'\r[{tekst_wykonane}{tekst_niewykonane}]', end=' ')

for i in range(100):
    pasek_ladowania(i)
    # pasek_ladowania(i)
    time.sleep(0.1)













