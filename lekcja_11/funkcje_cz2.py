# Funkcje cz. 2

print("======= Zadanie Rozgrzewkowe =======")

'''
Przygotuj funkcję, która jako argument otrzymuje string oraz listę stringów, a zwraca
napis, gdzie pomiędzy elementy z listy dokładana jest zawartość pierwszego
argumentu. Wskazówka: skorzystaj z metody join
'''

# foo(‘?’, [‘ala’, ‘ma’, ‘kota’]) -> ‘ala?ma?kota’

def foo(fraza, slowa):
    return fraza.join(slowa)

print(foo("?", ["ala", "ma", "kota"]))

print("======= Zadanie 1 =======")

'''
Napisz funkcję, która otrzyma dwa argumenty: pierwszym będzie liczba, którą chcemy
podzielić bez reszty a drugim argumentem będzie dzielnik. Należy sprawdzić czy
można dokonać dzielenia a jeśli tak zwrócić informację czy liczba jest podzielna bez
reszty czy nie.
'''

# Sprawdzamy czy dzielnik jest równy 0 
# Jeśli tak, zwracamy nie można dzielić przez 0
# Jeśli nie, to sprawdzamy czy liczba jest podzielna przez dzielnik
# W przeciwnym wypadku, wypisujemy że liczba nie jest podzielna przez dzielnik

def podzielna(liczba, dzielnik):
    if dzielnik == 0:
        return "Nie można dzielić przez 0"
    elif liczba % dzielnik == 0:
        return f"Liczba {liczba} jest podzielna przez {dzielnik}"
    else:
        return f"Liczba {liczba} NIE jest podzielna przez {dzielnik}"
    
print(podzielna(2,3))
print(podzielna(9,0))
print(podzielna(51,17))


print("======= TYPE HINTING =======")
# Type hinting -> podpowiadanie typów

def prostokat(a: float, b: float) -> float:
    obwod = 2*a + 2*b
    return obwod

print(prostokat(5.5 , 4.5))

print("====== ZADANIE 2 ======")

'''
Napisz funkcję, która przyjmuje następujące argumenty: imie (str), wiek (int), wzrost_m
(float), a zwraca napis (string): “Jan, lat 20, 1.75 m wzrostu” - oczywiście argumenty należy
podstawić do szablonu. Wzrost ma zawsze pokazywać dwa miejsca po przecinku.
'''

def komunikat(imie: str, wiek: int, wzrost: float) -> str:
    return f"{imie}, {wiek} lat, {wzrost:.2f} m wzrostu"

print(komunikat("Tomek", 22, 1.7545678))
print(komunikat("Ola", 23, 1.5))










