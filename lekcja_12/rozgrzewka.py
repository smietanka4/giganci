'''
Napisz funkcję, która otrzymuje 3 parametry:
- proporcje_szerokosc
- proporcje_wysokosc
- piksele_szerokosc

Funkcja otrzymuje oczekiwane proporcje ekranu (np. 16:9, 4:3) oraz piksele_szerokosc.
Zadaniem funkcji jest obliczyć ile pikseli powinna mieć wysokość, aby proporcje ekranu
były poprawne. Zwracana liczba powinna być liczbą całkowitą
16:9 -> 1920 x 1080
16:9 -> 1280 x 720
4:3 -> 1920 x 1440
'''

def oblicz_wysokosc(proporcje_szerokosc, proporcje_wysokosc, piksele_szerokosc):
    return int(piksele_szerokosc / proporcje_szerokosc * proporcje_wysokosc)

