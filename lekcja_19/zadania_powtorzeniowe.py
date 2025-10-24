# Zadanie 1 -> FizzBuzz

for liczba in range(1,101):
      if liczba % 3 == 0 and liczba % 5 == 0:
            print("FizzBuzz")
      elif liczba % 5 == 0:
            print("Buzz")
      elif liczba % 3 == 0:
            print("Fizz")
      else:
            print(liczba)

# Zadanie 2 -> wzór
liczba = int(input("Podaj ilość powtórzeń: "))

for num in range(liczba):
      for j in range(num):
            print(num, end=" ")
      print()

# Zadanie 3 -> min i max
# Trzeba zrobić za pomocą pętli

lista = [2,1,3,7,-67,0]

najwieksza = lista[0]
najmniejsza = lista[0]

for liczba in lista:
      if liczba > najwieksza:
            najwieksza = liczba

      if liczba < najmniejsza:
            najmniejsza = liczba

print(lista) 
print(f"Największa liczba to {najwieksza}")
print(f"Najmniejsza liczba to {najmniejsza}")

# Zadanie 4

'''
Program ma zliczyć ile danych liter znajduje się w zdaniu
Przykładowe wyświetlanie:

ABC przykładowy tekst na potrzeby naszego programu
Slowa: 7 Litery: 44 ilość liter: {'a': 5, 'b': 2, 'c': 1, 'p': 3, 'r': 4, 'z': 3, 'y': 3,
'k': 2, 'l': 1, 'd': 1, 'o': 4, 'w': 1, 't': 3, 'e': 3, 's': 2, 'n': 2, 'g': 2, 'm': 1, 'u': 1}
'''

tekst = input("Podaj przykładowy tekst: ")
print(tekst)

slownik = {}
slowa = 1
litery = 0

for znak in tekst:
      znak = znak.lower()
      if znak == " ":
            slowa += 1
      else:
            litery += 1
            if znak in slownik:
                  slownik[znak] += 1
            else:
                  slownik[znak] = 1

print(f"Słowa: {slowa}, Litery: {litery}, ilość liter: {slownik}")

