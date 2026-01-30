from stos import Stack

'''
Napisz funkcję, która sprawdzi, czy dany ciąg znaków jest palindromem,
korzystając z naszej implementacji stosu.
'''

# trochę inna implementacja niż ta co pokazywaliśmy sobie na lekcji :)

def is_palindrom(string):
    stack = Stack()
    for char in string(): # umieszczamy każdy znak z podanego napisu na stosie
        stack.push(char)
    reversed_string = "" 
    while not stack.is_empty(): # tworzymy odwrócony napis wyciągając po kolei litery ze stosu
        reversed_string += stack.pop() # Last In - First Out
    return string == reversed_string # porównujemy 
