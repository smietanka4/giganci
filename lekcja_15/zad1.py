'''
Napisz funkcję, która otrzyma jeden argument określający liczbę dziesiętną. Funkcja ma
wyświetlić ile wynosi podana liczba w zapisie binarnym.
'''

# def binary(liczba):
#       wynik = ''

#       while liczba > 0:
#            x = liczba % 2
#            liczba = liczba // 2
#            wynik = str(x) + wynik
#       return wynik

# wynik = binary(41)
# print(wynik)


def binarna(a):
      wynik = ''

      while not a < 1:
            b = a % 2 
            if b == 1:
                  wynik += '1'
                  a = a // 2
            if b == 0:
                  wynik += '0'
                  a = a // 2
      wynik = wynik[::-1]

      return wynik

wynik = binarna(41)
print(wynik)