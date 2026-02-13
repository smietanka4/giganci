'''
1 Stwórz 2 listy składające się z 3 liczb każda
2 Połącz stworzone wcześniej listy (Nie chcemy tworzyć nowej listy)
3 Usuń elementy z indeksami 2 i 5 , który element należy usunąć najpierw?
4 Usuń największą i najmniejszą liczbę z listy
5 Dodaj liczbę do listy
'''

'''
6 Posortuj listę
7 Utwórz kopię listy
8 Odwróć kolejność elementów w kopii
9 Dodaj do każdej wartości w pierwszej listy 1, a w kopii listy odejmij 1
10 Wyświetl obie listy
'''

# 1. Stwórz 2 listy składające się z 3 liczb każda
lista1 = [1,5,8]
lista2 = [2,3,9]

# 2. Połącz stworzone wcześniej listy (Nie chcemy tworzyć nowej listy)
lista1.extend(lista2)
print(lista1)

# 3. Usuń elementy z indeksami 2 i 5 , który element należy usunąć najpierw?
lista1.pop(5)
lista1.pop(2)
print(lista1)

# 4. Usuń największą i najmniejszą liczbę z listy
lista1.remove(max(lista1))
lista1.remove(min(lista1))
print(lista1)

# 5. Dodaj liczbę do listy
lista1.append(5)
print(lista1)

# 6. Posortuj listę
lista1.sort()
print(lista1)

# 7. Utwórz kopię listy
kopia_listy = lista1.copy()
print(kopia_listy)

# 8. Odwróć kolejność elementów w kopii
kopia_listy.reverse()
print(kopia_listy)

# 9. Dodaj do każdej wartości w pierwszej liście 1, a w kopii listy odejmij 1
for i in range(len(lista1)):
    lista1[i] += 1
for i in range(len(kopia_listy)):
    kopia_listy[i] -= 1

# 10. Wyświetl obie listy
print(lista1)
print(kopia_listy)


print("===== ZADANIE DODATKOWE =====")
'''
Posiadając listę uszkodzonych produktów, np:

magazyn = ["cegła", "szkło", "szkło", "drewno", "szkło", "drewno"]

Naszym zadaniem jest usunąć z listy wszystkie wystąpienia słowa "szkło".
Napisz kod, który modyfikuje oryginalną listę (nie twórz nowej zmiennej)
'''

magazyn = ["cegła", "szkło", "szkło", "drewno", "szkło", "drewno"]

# while "szkło" in magazyn:
#     magazyn.remove("szkło")

for produkt in reversed(magazyn):
    if produkt == "szkło":
        magazyn.remove(produkt)

print(magazyn)
