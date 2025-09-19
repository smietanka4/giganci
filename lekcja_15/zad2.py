'''
Napisz funkcję, która otrzyma jeden argument określający liczbę binarną. 
Funkcja ma wyświetlić ile wynosi podana liczba w zapisie dziesiętnym.
'''

def decimal(liczba):
      wynik = 0
      potega = 0

      while liczba > 0:
           x = liczba % 10 
           liczba = liczba // 10

           wynik +=  x * (2**potega)
           potega += 1

      return wynik

wynik = decimal(101001)
print(wynik)
