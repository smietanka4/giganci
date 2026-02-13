# Napisz program w którym stworzysz listę z 10 liczbami, a następnie wypiszesz co drugą z nich

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13]

for i in range(0,len(lista),2):
    print(lista[i])


# METODY LIST
print("====== METODY LIST ======")

# 1. Tworzenie listy
przykladowa_lista = [8, "kot", 67, 8.5, "fortnite", [1,1,2]]
print(przykladowa_lista)

# 2. Dodawanie elementów do listy
przykladowa_lista.append(2)
print(przykladowa_lista)

# 3. Poszerzanie listy o dowolny element po którym można iterować, np. lista, krotka, słownik, zbiór - metoda extend()
przykladowa_lista.extend(["pies", 3.14, "pi"])
print(przykladowa_lista)

# 4. Dodawanie elementu pod wskazany index 
przykladowa_lista.insert(2, "sigma")
print(przykladowa_lista)

# 5. Usuwanie danego elementu z listy
przykladowa_lista.remove("pies")
print(przykladowa_lista)

# 6. Usunięcie elementu spod podanego indeksu
przykladowa_lista.pop(1)
print(przykladowa_lista)

# 7. Znajdowanie indeksu elementu - index()
id = przykladowa_lista.index("fortnite")
print(id)

id = przykladowa_lista.index("fortnite",3,5) # index(objekt, start, stop)

# 8. Metoda zliczająca wystąpienia danej wartości w liście
count = przykladowa_lista.count("fortnite")
print(count)

# 9. Sortowanie listy - sort()
# ważne jest aby wszystkie elementy listy miały typy, które można ze sobą porównać
przykladowa_lista.remove("sigma")
przykladowa_lista.remove("fortnite")
przykladowa_lista.remove("pi")
przykladowa_lista.pop(3)

przykladowa_lista.sort()
print(przykladowa_lista)


# 10. Odwrócenie kolejności listy
przykladowa_lista.reverse()
print(przykladowa_lista)

print(przykladowa_lista[::-1])

# 11. Kopiowanie listy
kopia_listy = przykladowa_lista.copy()
print("Kopia listy")
print(kopia_listy)

print("Lista")
print(przykladowa_lista)

# 12. Czyszczenie listy
przykladowa_lista.clear()
print(przykladowa_lista)




