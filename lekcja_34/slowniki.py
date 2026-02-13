# Tworzenie słownika 
student = {
      'name': "Jan Kowalski",
      'age': 20
}

print(student)
# Słownik przechowuje pary klucz-wartość

# # # # # # # #

# Struktura JSON
{
      "name": "Jan Kowalski",
      "age": 22,
      "courses": ["Matematyka", "Informatyka"]      
}

# JSON przechowuje pary klucz-wartość

print("======================================")

gra = {
      "nazwa_gry": "Pokemon EMERALD",
      "data_wydania": 2004,
      "wydawca": "Nintendo",
      "gatunek": "przygodowa"
}

# Odwoływanie się do elementów słownika

print(gra["nazwa_gry"]) # Jak klucz nie istnieje to dostajemy błąd
print(gra.get("nazwa_gry")) # Jak klucz nie istnieje to otrzymujemy None

# Iterowanie po słowniku

print("======================================")
for value in gra.values():
      print(value)

print("======================================")
for key in gra.keys():
      print(key)

print("======================================")
for item in gra.items():
      print(item)

print("======================================")
for key, value in gra.items():
      print(f"Klucz: {key} | Wartość: {value}")


print("======================================")
# Dodawanie par do słownika
gra["opis"] = "Gra przygodowa polegająca na łapaniu pokemonów"
print(gra)

gra.setdefault("PEGI", 12)
print(gra)

print("======================================")
# Usunięcie i zwrócenie pary klucz-wartość
delated = gra.pop("opis")
print(delated)
print(gra)

# Usunięcie i zwrócenie ostatniej pary klucz-wartość
last_item = gra.popitem()
print(last_item)
print(gra)

# Usunięcie pary klucz-wartość
del gra["gatunek"]
print(gra)

# Usunięcie wszystkich par klucz-wartość ze słownika
# gra.clear()
# print(gra)

print("======================================")
# Bardziej estetyczne wyświetlanie słownika
from pprint import pprint

gra["opis"] = "Gra przygodowa polegająca na łapaniu pokemonów"
pprint(gra)

print("======================================")
'''
Policzenie podanej ilości wyrazów ciągu fibbonacciego za pomocą słownika

pierwszy wyraz = 0
drugi wyraz = 1
trzeci wyraz itd... = suma dwóch poprzednich

def fibonacci(n):
      if n <= 1:
            return n
      else:
            return fibonacci(n-1) + fibonacci(n-2)

'''

# result = {"numer indeksu": "liczba"}

# def fibonacci(n):