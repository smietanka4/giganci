# while warunek:
#     # Miejsce dla kodu
#     pass

# Napisz program, który wyświetli 10 razy "Cześć Gigancie"

# Prymitywna wersja dla nobków 😭
print("Cześć Gigancie")
print("Cześć Gigancie")
print("Cześć Gigancie")
print("Cześć Gigancie")
print("Cześć Gigancie")
print("Cześć Gigancie")
print("Cześć Gigancie")
print("Cześć Gigancie")
print("Cześć Gigancie")
print("Cześć Gigancie")

powtorzenia = 0

while powtorzenia < 10:
    print("Cześć Gigancie !")
    powtorzenia += 1

# ZADANIE 1 - wyświetlanie komunikatów

'''
Napisz program, który wczyta od użytkownika liczbę całkowitą i wyświetli na ekranie
dokładnie tyle komunikatów “Giganci Programowania”. Należy zaprezentować kilka wersji dostępnych rozwiązań.
'''

# I wariant

liczba = int(input("Wprowadź liczbę: "))

while liczba > 0:
    print("Giganci programowania")
    liczba -= 1

# II wariant

liczba = int(input("Wprowadź liczbę: "))
stop = 0

while liczba > stop:
    print("Giganci progromawania")
    stop += 1

# ZADANIE 2 - timer bomby

'''
Przekształć poprzednie rozwiązanie tak aby po wpisaniu liczby przez użytkownika
program wypisywał kolejne liczby, aż do zera. Po tym w konsoli powinien pojawić się
napis “BOOM!”.
'''

import time # moduł, który odpowiada za pracę z czasem w pythonie

liczba = int(input("Wprowadź liczbę: "))

while liczba > 0:
    print(liczba)
    liczba -= 1
    time.sleep(1) # .sleep -> to metoda z modułu time, który wyżej zaimportowaliśmy. 
                  #           Służy do zaczekania podanej ilości sekund przed wykonaniem następnego kodu.
print("BOOM!")
 

# ZADANIE 3 - zgadywanka

'''
Zgadywanie liczby wylosowanej przez komputer.
Program losuje liczbę, zadaniem użytkownika jest odgadnąć ją. Komputer
odpowiada “za mało”, “za dużo” lub w przypadku trafienia wyświetla informację o
wygranej i liczbie tur potrzebnych do wygranej.
'''

# Import modułu, który pozwala na losowanie wartości
import random
# Zakres w którym losujemy wartość
MINIMUM = 0
MAXIMUM = 100
# Wylosowanie wartości i zapisanie jej do zmiennej
wylosowana_liczba = random.randint(MINIMUM, MAXIMUM)
# Wyświetlenie wylosowanej wartości
# Tylko w celach sprawdzenia działania
print(wylosowana_liczba)
# Zmienne używane do kontroli działania programu
odpowiedz = None
licznik_tur = 0
# Pętla działająca tak długo, aż odpowiedź użytkownika jest różna od wylosowanej liczby
while odpowiedz != wylosowana_liczba:
# Odczytanie odpowiedzi użytkownika
    odpowiedz = int(input("Podaj liczbę: "))
    # Zwiększenie licznika tur, aby śledzić która to tura
    licznik_tur += 1
    # Dla niepoprawnych odpowiedzi wyświetli się podpowiedź
    if odpowiedz < wylosowana_liczba:
        print("za mało :p")
    elif odpowiedz > wylosowana_liczba:
        print("za dużo :b")

    # Jeśli opuściliśmy pętle to oznacza, że udało się uzyskać poprawną odpowiedź
print("Gratulacje udało Ci się odgadnąć wylosowaną liczbę!")
print("Liczba: " + str(wylosowana_liczba))
print(f"Tura: {licznik_tur}")


# PĘTLA NIESKOŃCZONA
while True: # -> warunek = True, zawsze prawdziwy, czyli kod cały czas się wykonuje
    print("You can't stop me now!")
