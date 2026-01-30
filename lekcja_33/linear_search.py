import random
my_list = []

for i in range(20):
    liczba = random.randint(1, 100)
    my_list.append(liczba)

print(my_list)

print("================")

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1