# liczba = 2 # int
# zmiennoprzecinkowa = 2.4 # float
# tekst = "Giganci programowania" # string
# logiczna = True # bool

# liczba = int(input("Podaj liczbe")) # -> zawsze zwraca ciąg znaków jako typ, czyli str
# napis = "giganci"
# print(napis+str(liczba))

liczbaA = 2
liczbaB = 3
wynik = liczbaA + liczbaB #wynik = 5
print(wynik)
wynik2 = liczbaA * 4 #wynik2 = 8
print(wynik2)
wynik += 1 #wynik = 6
print(wynik)
wynik2 -= 1 #wynik2 = 7
print(wynik2)

warunek = liczbaA < 4 #warunek = True
print(warunek)
zmienna1 = True
zmienna2 = False
zmienna3 = zmienna1 and zmienna2 #zmienna3 = False
zmienna4 = zmienna1 or zmienna2 #zmienna4 = True

liczba = 23
if liczba == 12:
      print("liczba to 12")
elif liczba == 13:
      print("pechowa liczba")
else:
      print("liczba jest różna od 12 i od 13")


liczby = [1, 3, 4, 12, 8, 5, 8, 1]
for liczba in liczby: #wyświetli wszystkie elementy listy
      print(liczba)
for x in range(10): #wyświetli liczby 0-9
      print(x)

liczba = 0
while liczba < 20: #w pętli zostaną wyświetlone liczby parzyste 0-18
      print(liczba)
      liczba += 2



def oblicz_pole_trapezu(a, b, h):
      pole = (a + b) / 2 * h
      return pole

wynik = oblicz_pole_trapezu(2, 4, 6)
wynik2 = oblicz_pole_trapezu(12, 35, 17)
print(wynik, wynik2)

slownik = {}
print(type(slownik))

slownik = {'key': 'value'}

slownik = {'k': 1, 'm': [1,1,3], 'l': 'sigma'}

if 'k' in slownik:
      slownik['k'] += 2
      
print(slownik['k'])
      
