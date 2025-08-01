# Zadanie rozgrzewkowe

"""
Napisz program, który zapyta użytkownika o N ocen cząstkowych, a następnie wyliczy
średnią z przedmiotu.
N - liczba ocen wprowadzona przez użytkownika na początku działania programu
Dodatkowa część:
Następnie wyświetli ocenę końcową z przedmiotu jako zaokrąglenie średniej do całości.
"""

# liczba_ocen = int(input("Podaj liczbę ocen: ")) # zapytanie użytkownika o liczbę ocen
# suma_ocen = 0 # zmienna do przechowywania sumy ocen

# for i in range(liczba_ocen):                #  pętla pytająca użytkownika o oceny cząstkowe i wyliczająca sume                                     
#     ocena = float(input("Podaj ocenę: "))
#     suma_ocen = suma_ocen + ocena

# srednia = round(suma_ocen / liczba_ocen) # zmienna przechowywująca średnią ocen

# print(f"Średnia ocen to {srednia}")

# LISTY

oceny = [4, 5, 3, 4.5, 2, 1, 6, 5] # przykładowa lista, lista jest tworzona za pomocą []. To co jest wewnątrz to elementy

# Indeksowanie
#        0, 1, 2, 3  , 4, 5, 6, 7
oceny = [4, 5, 3, 4.5, 2, 1, 6, 5]

print(oceny[3]) # wyciąganie konkretnego elementu

moja_ocena = oceny[0]

print(len(oceny)) # -> funkcja len, zwraca liczbę całkowitą - liczbę elementów w liście

oceny.append(3) # -> metoda wbudowana "append" dodaje element na koniec listy
print(oceny)

for element in oceny: # -> iterowanie po elementach odbywa się za pomocą pętli for
    print(element)

napis = "Ala ma kota"
print(napis[5])

print("========================")

for litera in napis:
    print(f"Litera {litera}")

print("=========ZADANIE 1=========")

'''
Obliczanie średniej z wprowadzonych ocen.
Program musi wczytywać oceny, aż napotka znak ‘q’ mówiący, że wprowadzono
wszystkie oceny. Idealne miejsce na wykorzystanie pętli while.
'''

oceny = []

while True: # pętla, dodająca oceny od użytkownika do listy, ewentualne przerwanie pętli, po wpisaniu "q"
    ocena = input("Podaj ocenę: ")

    if ocena == "q":
        break

    ocena = float(ocena)
    oceny.append(ocena) 
    print(oceny)

suma = sum(oceny)
srednia = suma / len(oceny)
print(f"Średnia z Twoich ocen wynosi: {srednia}")

print("======== Zadanie 2 ========")

'''
Odwrócenie wprowadzonych komunikatów.
Program zapyta o liczbę elementów, które ma przyjąć, a następnie odczyta od użytkownika tyle komunikatów. 
Na koniec wyświetli je w tej samej kolejności.

Należy wykorzystać indeksy
'''

liczba_elementow = int(input("Podaj liczbę elementów: "))
elementy = [] 

for i in range(liczba_elementow):
    komunikat = input(f"Podaj element numer {i}")
    elementy.append(komunikat)

# Przykład: elementy = ["sigma", "skibidi", "tung tung sahur"]

for i in range(len(elementy)):
    print(elementy[i])

# Chwila teorii -> iterowanie po listach

print("======== TEORIA ========")

elementy = [1,"sigma",3,True,5]

for elem in elementy:
    print(elem)

for index in range(len(elementy)):
    print(elementy[index])