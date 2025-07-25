'''
Napisz program, który będzie pytać użytkownika o liczbe i zliczać ich sumę, aż do
wprowadzenia przez użytkownika hasła “koniec”.
Po wpisaniu tego hasła program, powinien opuścić pętle while i wyświetlić sumę tych
ocen.
'''

suma = 0
        
while True:
    wejscie = input("Podaj liczbę lub wpisz 'koniec', aby zakończyć: ")
    if wejscie == "koniec":
        break
    else:
        liczba = float(wejscie)
        suma += liczba

print(f"Suma Twoich liczb wynosi {suma}")

# Pętla -> for

# Wersja nr 1: Podajemy tylko jeden parametr: stop
range(10) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# Wersja nr 2: Podajemy dwa parametry: start, stop
range(2, 10) # 2, 3, 4, 5, 6, 7, 8, 9

# Wersja nr 3: Podajemy wszystkie parametry: start, stop, step 
range(2, 10, 3) # 2, 5, 8

for elem in range(2, 10, 3):
    print(elem)
    pass

# -9, -6, -3, 0, 3
for i in range(-9, 4, 3):
    print(i)

'''
Napisz program, który wypisze ile lat miałeś/aś w kolejnych latach kalendarzowych od
Twojego roku urodzenia. Program powinien wykorzystać zmienną wiek oraz pętle for z
instrukcją range.
'''

''' -> Oczekiwany rezultat dla roku_urodzenia 1998:
W roku 1998 miałeś/aś 0 lat
W roku 1999 miałeś/aś 1 lat
W roku 2000 miałeś/aś 2 lat
...
W roku 2020 miałeś/aś 22 lat
W roku 2021 miałeś/aś 23 lat
'''

wiek = int(input("Podaj swój wiek: ")) # wiek = 19

for i in range(wiek+1): # 1. i = 0; 2. i = 1
    dany_rok = 2025 - wiek + i # 1. dany_rok = 2006, 2. dany_rok = 2007
    wiek_w_danym_roku = i  # 1. 0, 2. 1
    print(f"W roku {dany_rok} miałeś/aś {wiek_w_danym_roku} lat")


# Zagnieżdżanie pętli

for a in range(5):
    print(f"a = {a}")
    for b in range(20,70,10):
        print(f"b = {b}")
        pass # for b
    pass # for a


'''
Napisz program, który wypisze w konsoli tabliczkę mnożenia. Wykorzystaj funkcję:
str(liczba).center(liczba_znaków) do wyrównania tekstu.
'''

for a in range(1, 11):
    line = ""
    for b in range(1, 11):
        line += str(a*b).center(4) + "|"
        pass # for b
    print(line)
    pass # for a 


