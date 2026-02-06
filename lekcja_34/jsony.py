import json

gra = {
      "nazwa_gry": "Pokemon EMERALD",
      "data_wydania": 2004,
      "wydawca": "Nintendo",
      "gatunek": "przygodowa"
}


# Konwertuje obiekt Python (np. słownik) do łańcucha znaków w formacie JSON
# json.dumps() 
s = json.dumps(gra)
print(s)
print(type(s))

# Konwertuje łańcuch znaków w formacie JSON na odpowiadający mu obiekt Python (np. słownik)
# json.dumps() 
a = json.loads(s)
print(a)
print(type(a))

# Zapisuje obiekt python do pliku w formacie JSON
# json.dump()

# Wczytuje dane JSON z pliku i konwertuje je na odpowiadający mu obiekt Python
# json.load()

# Jak otwierać pliki w pythonie (poprawnie)
'''
with open("nazwa_pliku.txt", "r", encoding='utf-8') as plik:
      zawartosc = plik.read()
      print(zawartosc)
      
r (read) - odczyt
w (write) - zapisywanie, edytowanie, nadpisujemy jego zawartość
a (append) - dopisuje dane na końcu pliku

'''
from pprint import pprint

with open("lekcja_34/spis_gier.json", "r", encoding='utf-8') as file:
      spis_gier = json.load(file)

spis_gier["spis_gier"].append(gra)
pprint(spis_gier["spis_gier"])

print("==============================")
with open("lekcja_34/gry.json", "w") as file:
      json.dump(spis_gier, file, indent=4, sort_keys=True)








