# # Zadanie rozgrzewkowe

# """
# Napisz program, który zapyta użytkownika o N ocen cząstkowych, a następnie wyliczy
# średnią z przedmiotu.
# N - liczba ocen wprowadzona przez użytkownika na początku działania programu
# Dodatkowa część:
# Następnie wyświetli ocenę końcową z przedmiotu jako zaokrąglenie średniej do całości.
# """

# liczba_ocen = int(input("Podaj liczbę ocen: ")) # zapytanie użytkownika o liczbę ocen
# suma_ocen = 0 # zmienna do przechowywania sumy ocen

# for i in range(liczba_ocen):                #  pętla pytająca użytkownika o oceny cząstkowe i wyliczająca sume                                     
#     ocena = float(input("Podaj ocenę: "))
#     suma_ocen = suma_ocen + ocena

# srednia = round(suma_ocen / liczba_ocen) # zmienna przechowywująca średnią ocen

# print(f"Średnia ocen to {srednia}")

# # LISTY

# oceny = [4, 5, 3, 4.5, 2, 1, 6, 5] # przykładowa lista, lista jest tworzona za pomocą []. To co jest wewnątrz to elementy

# # Indeksowanie
# #        0, 1, 2, 3  , 4, 5, 6, 7
# oceny = [4, 5, 3, 4.5, 2, 1, 6, 5]

# print(oceny[3]) # wyciąganie konkretnego elementu

# moja_ocena = oceny[0]

# print(len(oceny)) # -> funkcja len, zwraca liczbę całkowitą - liczbę elementów w liście

# oceny.append(3) # -> metoda wbudowana "append" dodaje element na koniec listy
# print(oceny)

# for element in oceny: # -> iterowanie po elementach odbywa się za pomocą pętli for
#     print(element)

# napis = "Ala ma kota"
# print(napis[5])

# print("========================")

# for litera in napis:
#     print(f"Litera {litera}")

# print("=========ZADANIE 1=========")

# '''
# Obliczanie średniej z wprowadzonych ocen.
# Program musi wczytywać oceny, aż napotka znak ‘q’ mówiący, że wprowadzono
# wszystkie oceny. Idealne miejsce na wykorzystanie pętli while.
# '''

# oceny = []

# while True: # pętla, dodająca oceny od użytkownika do listy, ewentualne przerwanie pętli, po wpisaniu "q"
#     ocena = input("Podaj ocenę: ")

#     if ocena == "q":
#         break

#     ocena = float(ocena)
#     oceny.append(ocena) 
#     print(oceny)

# suma = sum(oceny)
# srednia = suma / len(oceny)
# print(f"Średnia z Twoich ocen wynosi: {srednia}")

# print("======== Zadanie 2 ========")

# '''
# Odwrócenie wprowadzonych komunikatów.
# Program zapyta o liczbę elementów, które ma przyjąć, a następnie odczyta od użytkownika tyle komunikatów. 
# Na koniec wyświetli je w tej samej kolejności.

# Należy wykorzystać indeksy
# '''

# liczba_elementow = int(input("Podaj liczbę elementów: "))
# elementy = [] 

# for i in range(liczba_elementow):
#     komunikat = input(f"Podaj element numer {i}")
#     elementy.append(komunikat)

# # Przykład: elementy = ["sigma", "skibidi", "tung tung sahur"]

# for i in range(len(elementy)):
#     print(elementy[i])

# Chwila teorii -> iterowanie po listach

print("======== TEORIA ========")

elementy = [1,"sigma",3,True,5]

# for elem in elementy:
#     print(elem)

# for index in range(len(elementy)):
#     print(elementy[index])

liczby = [9, 1, 0, 2, 0, 3, 4, 5, 10, -1, 20, 32, -20, -3, -4]

# Zakres <start; stop) -> <2; 8) -> indeksy: 2, 3, 4, 5, 6, 7
nowa_lista = liczby[2:20] # wyciągnie wszystkie elementy (bo mamy 14 indeksów)
print(nowa_lista)

nowa_lista = liczby[10:3] # Nie ma liczby większej lub równej od 10 i jednocześnie mneijszej od 3
print(nowa_lista)

# ujemne indeksy
# Indeksy: 0,   1,  2,  3,  4,  5,  6,  7,  8,   9,   10,  11,  12,   13,  14 
liczby  =  [9,  1,  0,  2,  0,  3,  4,  5,  10,  -1,  20,  32,  -20,  -3,  -4]
# Indeksy: -15 -14 -13 -12 -11 -10 -9  -8   -7   -6   -5   -4   -3    -2   -1

nowa_lista = liczby [-13: -5]
print(nowa_lista)

nowa_lista_od_poczatku = liczby[:10]
print(nowa_lista_od_poczatku)

nowa_lista_od_konca = liczby[5:]
print(nowa_lista_od_konca)

# <start: stop: step)
lista_co_iles = liczby[0:15:2]
print(lista_co_iles)

# Warto zaznaczyć, że do listy możemy dokładać zmienne
a = 7
b = 10
liczby = [a, b, 20]
print(liczby)

# Jeśli znamy liczbę elementów w liście, możemy przypisać do każdego elementu zmienną w taki sposób

oceny_z_3_sprawdzianow = [5, 4.5, 3]
ocena1, ocena2, ocena3 = oceny_z_3_sprawdzianow
print(ocena1, ocena2, ocena3)

ocena1, ocena2 = oceny_z_3_sprawdzianow[:2]

print("============= ZADANIE 3 =============")

'''
Napisz program, który wymnoży ze sobą wszystkie elementy w liście. Lista ma zawierać
tylko liczby (całkowite lub float).
'''

liczby = [5, 6, -7, 5.23, 0.1]
wynik = 1

# for liczba in liczby: -> działanie na elementach listy
#     wynik *= liczba

# działanie na indeksach
for index in range(len(liczby)):
    wynik *= liczby[index]

print(wynik)


# Czy element znajduje się w liście?

liczby = [5, 6, -7, 5.23, 0.1]

if 2 in liczby:
    # Kod wykonywany, jeśli dwójka znajduje się w liście
    pass

if 2 not in liczby:
    # Kod wykonywany, jeśli dwójka nie znajduję się w liście
    pass


print("========== ZADANIE 4 ==========")

'''
Napisz program, który pyta użytkownika o 10 liczb, ale w liście nie mogą wystąpić
powtórzenia. Jeżeli użytkownik poda liczbę, która została podana wcześniej program
powinien wyświetlić stosowny komunikat oraz zapytać ponownie o liczbę.
Należy wykorzystać pętle while
'''

liczby = []

while len(liczby) < 10:
    a = int(input("Podaj liczbę: "))

    # sprawdzanie duplikatów
    if a in liczby:
        print("Wprowadzono już taką liczbę")
    else: # unikalna wartość
        liczby.append(a)

print(liczby)
