'''
Waszym zadaniem jest napisać funkcję, która zwróci informacje prawda/fałsz czy
podana liczba jest liczbą pierwszą
'''

def is_prime(liczba):
      if liczba <= 1:
            return False
      else:
            for i in range(2,liczba):
                  if liczba % i == 0:
                        return False
      return True

print(is_prime(1))