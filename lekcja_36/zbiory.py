# ZBIORY (Sets)

# Tworzenie zbiorów
zbiór = {1,2,3,4,2}
pusty_zbior = set()

print(zbiór)

# METODY

# Dodawanie elementów 
zbiór.add(9)
print(zbiór)

# Usuwanie elementów ze zbioru
zbiór.remove(1)
print(zbiór)

# Usunięcie elementu jeśli istnieje
zbiór.discard(44)
print(zbiór)

# Usunięcie pierwszego elementu i zwrócenie go
element = zbiór.pop()
print(element)
print(zbiór)

# Usunięcie wszystkich wartości ze zbioru
zbiór.clear()
print(zbiór)