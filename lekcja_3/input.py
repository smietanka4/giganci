nazwa_zmiennej = "Giganci Programowania"
print(nazwa_zmiennej)

'''
po lewej - nazwa zmiennej, 
= - operator przypisania, 
po prawej - to co chcemy przypisać
'''

# pobranie wartości z konsoli od użytkownika
# input()

# warto to jednak gdzieś zapisać
# x = input()

imie = input("Podaj swoje imię: ")

# input zawsze zwraca wartość string
wiek = input("Podaj swój wiek: ")
print(type(wiek))
wiek = int(input("Podaj swój wiek: ")) # widzimy, że typ w linijce wyzej to string, więc aby uzyskać liczbę dajemy int()
print(type(wiek))