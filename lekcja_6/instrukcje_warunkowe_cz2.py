wprowadzone_haslo = input("Podaj hasło: ")
poprawnosc_hasla = "Masło" == wprowadzone_haslo

if poprawnosc_hasla:
    # Kod dla poprawnego hasła
    print("Hasło poprawnie")
else:
    # Kod dla niepoprawnego hasła
    print("Hasło niepoprawne")

# Zmienne a,b,c, ..., z przechowują liczby całkowite
# if a == 20 or b < 10 and c > -5 and ... or 20 < z < 120:
    # Kod wykonywany jeśli powyższy warunek został spełniony

# Zadanie 1 - czy dane słowo zawiera?

'''
Napisz program, który sprawdzi, czy w podanym przez użytkownika wyrazie znajduje się jedna z następujących liter lub ciągów znaków:
    -> litera "a"
    -> litera "d"
    -> ciąg znaków "as"
    -> ciąg znaków "zzz"
Jeśli znajdzie choć jedno z nich, program powinien wyświetlić komunikat, że wyraz zawiera poszukiwany fragment.
'''

# wyraz = "slowo"

# if "o" in wyraz: # Sprawdza czy znak "o" znajduje się w podanym wyrazie
#     print(True) 

wyraz = input("Podaj wyraz: ")
if ("a" or 'd' or 'as' or 'zzz') in wyraz:
    print(wyraz, 'posiada jedno z wyszukiwanych haseł')
else:
    print(wyraz, 'NIE posiada żadnego z wyszukiwanych haseł')


# Zadanie 2 - system logowania
print("=== ZADANIE 2 ===")
'''
Napisz program, który będzie działał jak podstawowy system logowania:
Wykonaj poniższe kroki:
    1. Zapisz dane do logowania w zmiennych:
        ○ LOGIN = "gigant@trener.pl"
        ○ HASLO = "qwerty"
    2. Poproś użytkownika o podanie loginu (za pomocą input()).
    3. Poproś użytkownika o podanie hasła.
    4. Sprawdź, czy wprowadzone dane są zgodne z zapisanymi loginem i hasłem:
        ○ jeśli tak - wyświetl komunikat: "Poprawnie zalogowano"
        ○ jeśli nie - wyświetl komunikat: "Niepoprawny login lub hasło"
'''


import getpass

login = "gigant@trener.pl"
haslo = "qwerty"

login_user = input("Podaj login: ")
haslo_user = getpass.getpass("Podaj hasło: ")

if login == login_user and haslo == haslo_user:
    print("Poprawnie zalogowano")
else:
    print("Niepoprawny login lub hasło")

# Zagnieżdżone instrukcje warunkowe

'''
if warunek:
    if warunek2:
        # Kod wykonywany tylko wtedy jeśli warunek == True and warunek2 == True
    elif warunek3:
        # Kod wykonywany tylko wtedy jeśli warunek == True and warunek3 == True
    else:
        # Kod wykonywany tylko wtedy jeśli warunek == True, a pozostałe warunki == False
else:
    # Kod wykonywany tylko wtedy jeśli warunek == False
'''

# Zadanie 3 - logowanie dwuetapowe

'''
Stwórz program, który obsłuży proces dwuetapowego logowania. 
-> Użytkownik zostanie poproszony o wprowadzenie czterocyfrowego PINu. 
    ->Jeśli poda błędny PIN, program wyświetli odpowiedni komunikat o błędzie. 
    ->W przypadku poprawnego PINu, użytkownik zostanie następnie poproszony o podanie hasła słownego.

PIN: „1234”
Hasło: „Masło”
'''

print("=== ZADANIE 3 ===")

PIN = "1234"
HASLO = "Masło"

user_pin = getpass.getpass("Podaj czterocyfrowy pin: ")

if user_pin == PIN:
    user_haslo = getpass.getpass("Podaj hasło: ")
    if user_haslo == HASLO:
        print("Poprawnie zalogowano")
    else:
        print("Podałeś niepoprawne hasło")
else:
    print("Podałeś niepoprawny pin")


# ZADANIE 4 - matematyczny pomocnik do trójkątów

print("=== ZADANIE 4 ===")

'''
Napisz program, który wczyta od użytkownika długości trzech boków trójkąta, a następnie:

1. Sprawdzi, czy taki trójkąt może istnieć:
    ○ Każdy bok musi być większy od zera.
    ○ Suma długości dwóch krótszych boków musi być większa niż długość najdłuższego.
    ○ Jeśli te warunki nie są spełnione - wyświetl odpowiedni komunikat i zakończ program.

2. Wyświetli:
    ○ Najkrótszy i najdłuższy bok.
    ○ Rodzaj trójkąta ze względu na długości boków:
        ➤ równoboczny - wszystkie boki równe
        ➤ równoramienny - dwa boki równe
        ➤ różnoboczny - wszystkie boki różne
    ○ Obwód trójkąta.
    ○ Rodzaj trójkąta ze względu na kąty:
        ➤ prostokątny - spełnia twierdzenie Pitagorasa -> kwadrat_najdluzszego_boku == suma_kwadratow_dwoch_krotszych_bokow
        ➤ rozwartokątny - największy kąt > 90°
        ➤ ostrokątny - wszystkie kąty < 90°
'''

# Długości boków będą zmiennymi a, b, c
a = float(input("Podaj pierwszy bok trójkąta: "))
b = float(input("Podaj drugi bok trójkąta: "))
c = float(input("Podaj trzeci bok trójkąta: "))

# Podsumowanie:
print(f"Podano boki: {a}, {b}, {c}")

# Zmienne wymagane do więcej niż jednej części
najkrotszy = min(a,b,c)
najdluzszy = max(a,b,c)
obwod = a + b + c
sredni = obwod - najdluzszy - najkrotszy


if (a > 0 and b > 0 and c > 0) and  (najdluzszy > najkrotszy + sredni):
    print("Taki trójkąt istnieje")
else:
    print("Podane boki nie utworzą trójkąta")
    exit() # Wcześniejsze zakończenie programu

# Część numer 1: Najkrótszy i najdłuższy bok
print(f"Najkrótszy bok: {najkrotszy}")
print(f"Najdłuższy bok: {najdluzszy}")

# Część numer 2: Rodzaj trójkąta boki
# Równoboczny - wszystkie boki są takie same
# Różnoboczny - wszystkie boki są różne
# Równoramienny - dwa boki takie same (pozostałe przypadki)
if a == b == c: # Równoboczny
    print("Trójkąt równoboczny")
elif a!=b and a!=c and b!=c: # Różnoboczny
    print("Trójkąt różnoboczny")
else: # Równoramienny
    print("Trójkąt równoramienny")

# Część numer 3: Obwód
print(f"Obwód trójkąta: {obwod}")

# Część numer 4: Rodzaj trójkąta kąty
# Twierdzenie pitagorasa:
# najdluzszy^2 ?? sredni_bok^2 + najkrotszy^2
# prostokątny: == obie wartosci sa sobie rowne
# rozwartokątny: > kwadrat najdłuższego boku jest większy
# ostrokątny: < suma kwadratów dwóch boków jest większa

kwadrat_najdluzszego_boku = najdluzszy ** 2
suma_kwadratow_dwoch_bokow = sredni ** 2 + najkrotszy ** 2
if kwadrat_najdluzszego_boku == suma_kwadratow_dwoch_bokow:
    print("Trójkąt prostokątny")
elif kwadrat_najdluzszego_boku > suma_kwadratow_dwoch_bokow:
    print("Trójkąt rozwartokątny")
else:
    print("Trójkąt ostrokątny")

# ZADANIE 5 - średnia ocen
'''
Napisz program, który wczyta od użytkownika oceny końcowe z pięciu
przedmiotów: matematyka, polski, angielski, informatyka, wf. Następnie wyliczy
średnią ocen i wyświetli komunikat czy otrzymamy pasek na świadectwie
'''
print("Podaj oceny końcowe z następujących przedmiotów: ")
ocena_matma = float(input("Matematyka: "))
ocena_polski = float(input("Język Polski: "))
ocena_angielski = float(input("Angielski: "))
ocena_informatyka = float(input("Informatyka: "))
ocena_wf = float(input("WF: "))

suma_ocen = ocena_matma + ocena_polski + ocena_angielski + ocena_informatyka + ocena_wf
srednia_ocen = suma_ocen / 5

if srednia_ocen >= 4.75:
    print("Gratulacje, otrzymasz pasek na świadectwie!")
else:
    print("Niestety nie otrzymasz paska na świadectwie.")
    print("Powodzenia w przyszłym roku!")
print("Twoja średnia to:", srednia_ocen)




 


