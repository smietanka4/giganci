"Napisz drugą funkcję, która ma wyświetlić wszystkie liczby pierwsze z podanego przedziału."

def is_prime(liczba):
      if liczba <= 1:
            return False
      else:
            for i in range(2,liczba):
                  if liczba % i == 0:
                        return False
      return True

def generuj_pierwsze(a, b): # 3 , 9
      for i in range(a, b+1): # i = 3, 
            if is_prime(i): # czy 3 jest pierwszą?
                  print(i)

generuj_pierwsze(3, 9)