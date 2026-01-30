import random
my_list = []

for i in range(20):
    liczba = random.randint(1, 100)
    my_list.append(liczba)

print(my_list)


def bubble_sort(arr):
    n = len(arr)
    # iterujemy przez wszystkie elementy listy
    for i in range(n):
        # ostatnie i elementów są już posortowane
        for j in range(0, n-i-1):
            # porównujemy sąsiadów
            if arr[j] > arr[j+1]:
                # zamieniamy miejscami, jeśli kolejność jest nieprawidłowa
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

bubble_sort(my_list)
print("Posortowana lista: ", my_list)
