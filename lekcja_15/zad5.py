'''
Napisz funkcję, która jako argument otrzymuje tekst i sprawdzi czy jest on palindromem
wyświetlając: „{podane słowo} jest palindromem” lub „{podane słowo} nie jest
palindromem”
'''

def czy_palindrom(text):
    palindrom = ""
    palindrom = text[::-1]
    if palindrom == text:
        print(f'{text} jest palindromem')
    else:
        print(f"{text} nie jest palindromem")

czy_palindrom("Sedes")

# wykorzystać metodę .toUpper i .toLower