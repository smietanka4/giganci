# Konwersje miedzy strukturami
zbior = {1,2,3}
krotka = (4,5,6)
lista = [7,8,8,9]

print("Konwersja zbioru na liste")
print(list(zbior))
print(type(list(zbior)))

print("Krotki na liste")
print(list(krotka))
print(type(list(krotka)))

print("Konwersja zbioru na krotke")
print(tuple(krotka))
print(type(tuple(krotka)))

print("Konwersja listy na krotke")
print(tuple(lista))
print(type(tuple(lista)))

print("Konwersja krotki na zbiór")
print(set(krotka))
print(type(set(krotka)))

print("Konwersja listy na zbiór")
print(set(lista))
print(type(set(lista)))