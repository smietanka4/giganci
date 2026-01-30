'''
def suma(n):
    if n <= 0: # warunek stopu
        return n
    else:
        print(n)
        return n + suma(n-1)
    
print(suma(10))

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(8))
'''

'''
Zadaniem ucznia jest napisanie programu, który losuje liczbę z zakresu od 1 do
100, a następnie komputer będzie zgadywał tę liczbę, a my będziemy mu udzielać
podpowiedzi w postaci "za mało" lub "za dużo" w zależności od tego, czy
zgadnięta liczba jest mniejsza czy większa od wylosowanej liczby.

Komputer będzie korzystał z algorytmu binary search, a program zakończy się, gdy
komputer zgadnie liczbę.
'''