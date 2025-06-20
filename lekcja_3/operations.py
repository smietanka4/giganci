# OPERACJE MATEMATYCZNE

a = 8
b = 4

print(+a) # jednoargumentowy operator pozytywny, po prostu jest dla kompletności (nic nie robi)
print(a+b) # dwuargumentowy operator dodawania
print(-a) # jednoargumentowy operator negacji, zamienia wynik na ujemny
print(a-b) # dwuargumentowy operator odejmowania, od wartości z lewej odejmuje wartość z prawej
print(a*b) # dwuargumentowy operator mnożenia
print(a / b) # dwuargumentowy operator dzielenia, wartość z lewej strony dzieli przez wartość z prawej 
print(10 / 1) # (zawsze zwraca FLOAT!!)
print(a % b) # operator dzielenia modulo, zwraca resztę z dzielenia wartości z lewej strony przez wartość z prawej
print(a // 2) # operator dzielenia całkowitego, wynik dzielenia zaokrąglony w dół, zwraca Int
print(a**b) # operator potęgowania

a = a + 2 # a = a(9) + 2
print(a)

a += 2 # do wartości z lewej strony dodaje wartość z prawej strony 
print(a)

# b = b * 4
b *= 4 # b = 4 * 4 => b = 16
print(b)

b *= a # b = 16 * 8 => b = 128
print(b)

b /= 64 # b = 128 / 64 => b = 2
print(b)

a %= 3 # a = 8 % 3 => a = 2
print(a)

print(True + True) # 2, bo True = 1
print(False + True) # 1
print(False + False) # 0, bo False = 0
print(3 * True) # 3

print("Witaj" + "Gigancie") # dodawanie stringów łączy je w jeden string (do stringa możemy dodawać tylko stringi)
print("test " * 3)

tekst = "the binding of "
nowy_tekst = "Isaac"
tekst += nowy_tekst # tekst = tekst + nowy_tekst
print(tekst)

n = 3
m = 4

print("Wynik mnożenia ", n, "przez", m, "to", n*m)
# to jest niepotrzebne i nieschludne, lepiej użyć f-stringów
print(f"Wynik dodawania {n} i {m} to {n+m}")


'''
Funkcje Wbudowane
'''

# MATEMATYCZNE
print(abs(-10)) # wartość bezwzględna z liczby, tutaj 10
print(max(1,2,3,2,8,-5)) # najwieksza wartość z podanych argumentów, tutaj 8
print(min(1,2,3,2,8,-5)) # najmniejsza wartość z podanych argumentów, tutaj -5
print(round(3.5644)) # zaokrąglenie liczby 

# ITEROWALNE
print(len("Hello World!")) # zwraca długość obiektu - dla stringa to jest ilość znaków, tutaj 12 (bo spacja też się liczy)


# ZADANIA
'''
Pobrać od użykownika: imie, nazwisko, rok_urodzenia i wypisać na konsoli informacje tak jak poniżej. Używamy f-stringów


Dane: Jan, Kowalski, 2000
Oczekiwany wynik: Jan Kowalski ma 25 lat.
'''

imie = str(input("Podaj swoje imię: "))
nazwisko = str(input("Podaj swoje nazwisko: "))
rok_urodzenia = int(input("Podaj swój rok_urodzenia: "))
print(f"{imie} {nazwisko} ma {2025 - rok_urodzenia} lat.")