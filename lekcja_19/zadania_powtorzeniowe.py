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