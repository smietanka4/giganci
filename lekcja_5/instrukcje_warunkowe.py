# Czy telefon jest już naładowany?
# min_akceptowalny_poziom_baterii <= obecny_poziom_baterii <= max_akceptowalny_poziom_baterii

# Czy za oknem pada deszcz?
# pogoda_za_oknem == "deszcz"

print("Wykonam się za każdym razem")
warunek = True  # prawda

if warunek:
    # Kod wykona się tylko wtedy kiedy warunek jest prawdziwy 
    print("Warunek był prawdziwy")
    print("Mogę dodać wiele linijek kodu")

print("Wykonam się za każdym razem, brak wcięcia")

"""
Program obliczający wynik z dzielenia
Nie wolno dzielić przez zero! (czyli nasz program musi sprawdzać przez jaką liczbe dzielimy)
Jak warunek będzie spełniony to dopiero wtedy wykonujemy operacje dzielenia
"""

# Zadanie 1

dzielna = int(input("Wprowadź dzielną: "))
dzielnik = int(input("Wprowadź dzielnik: "))

if dzielnik != 0:
    wynik = dzielna / dzielnik
    print(f"Wynik z dzielenia to {wynik}")

if dzielnik == 0:
    print("Pamiętaj cholero nie dziel przez zero!")

# Instrukcja warunkowa if-else

warunek = True

if warunek: # jeżeli
    # Nasz kod wykonywany, jeśli warunek jest prawdziwy
    pass
else: # w przeciwnym razie
    # Nasz kod wykonywany, jeśli poprzednie warunki nie zostały spełnione
    pass

# Ulepszone zadanie 1 z pomocą else

dzielna = int(input("Wprowadź dzielną: "))
dzielnik = int(input("Wprowadź dzielnik: "))

if dzielnik != 0:
    wynik = dzielna / dzielnik
    print(f"Wynik z dzielenia to {wynik}")
else:
    print("Pamiętaj cholero nie dziel przez zero!")


# Zadanie 2

wiek = int(input("Podaj swój wiek: "))
wzrost = int(input("Podaj swój wzrost: "))

# if wiek >= 12: -> Niepotrzebnie dużo roboty
#     if wzrost >= 130 and wzrost <= 195:
#         print("Możesz wchodzić do rollercoastera")
#     else:
#         print("Nie możesz wejść na rollercoaster")
# else:
#     print("Nie możesz wejść na rollercoaster") 


# przyklad: wiek = 13 i wzrost = 130
if wiek >= 12 and 130 <= wzrost <= 195:
    print("Możesz wchodzić do rollercoastera")
else:
    print("Nie możesz wejść na rollercoaster")


# Instrukcja warunkowa if-elif-else

warunek = False
warunek2 = True

if warunek:
    # Nasz kod wykonywany będzie, tylko wtedy jeśli warunek jest prawdziwy
    print("Warunek 1 został spełniony")
elif warunek2: # else if
    # Kod wykonywany tylko wtedy jeśli poprzednie warunki nie zostały spełnione
    # oraz warunek2 został spełniony
    print("Warunek 1 nie został spełniony, ale warunek 2 został spełniony")
else: 
    print("Żaden z warunków nie został spełniony")

# Zadanie 3
'''
Jaką liczbę całkowitą wprowadzono: pozytywną, negatywną, czy równą zero?
Liczba może przyjąć tylko jedną z podanych opcji. 
Idealne wykorzystanie instrukcji if-elif.
'''













    