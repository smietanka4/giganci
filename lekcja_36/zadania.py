'''
1. Stwórz krotkę, listę, słownik i zbiór zawierający po 3 elementy
2. Za pomocą funkcji len() sprawdź długości poszczególnych obiektów
3. Za pomocą pętli for wypisz wszystkie elementy każdego z obiektów
4. Teraz wypisz wartości słownika zamiast kluczy
5. Wypisz te same elementy w odwrotnej kolejności, czy zawsze jest to możliwe
bezpośrednio? W razie problemów skorzystaj z pomocy chataGPT
'''

# 1.
krotka = (2,5,1)
lista = [3,0,1]
slownik = {
    "klucz1": 1,
    "klucz2": 12,
    "klucz3": 1
}
zbior = {5,9,3,4}

# 2.

print(f"Długość krotki: {len(krotka)}")
print(f"Długość listy: {len(lista)}")
print(f"Długość słownika: {len(slownik)}")
print(f"Długość zbioru: {len(zbior)}")

# 3.
print("Elementy listy")
for i in lista:
    print(i)

print("Elementy krotki")
for i in krotka:
    print(i)

print("Elementy słownika")
for i in slownik:
    print(i)

print("Elementy zbioru")
for i in zbior:
    print(i)

# 4.
print("Wartości słownika")
for i in slownik.values():
    print(i)

# 5.
print("Elementy listy")
for i in lista[::-1]:
    print(i)

print("Elementy krotki")
for i in krotka[::-1]:
    print(i)

print("Elementy słownika")
for i in reversed(slownik):
    print(i)

print("Elementy zbioru")
for i in list(zbior)[::-1]:
    print(i)

'''
6. Dodaj do listy elementy z krotki, zbioru i wartości słownika.
7. Dodaj do listy 2 liczby - wartość maksymalna i minimalna listy.
8. Sprawdź długość listy.
9.Zamień listę na krotkę- krotka2 i sprawdź jej długość.
10.Zamień krotkę na zbiór - zbior2 i sprawdź jego długość, z czego wynika
różnica?
'''

# 6. 
lista.extend(krotka)
lista.extend(zbior)
lista.extend(slownik.values())
print(lista)

# 7. 
lista.append(min(lista))
lista.append(max(lista))
print(lista)

# 8. 
print(f"Długość listy: {len(lista)}")

# 9.
krotka2 = tuple(lista)
print(krotka2)
print(f"Dlugosc krotki {len(krotka2)}")

# 10.
zbior2 = set(krotka2)
print(zbior2)
print(f"Dlugosc zbioru {len(zbior2)}")