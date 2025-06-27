# True - prawda, False - fałsz

# print(250 > 42) # 250 większe od 42 (True)
# print(400 >= 300) # 400 większe bądź równe 300 (True)
# print(250 < 250) # 250 większe od 250 (False)
# print(250 <= 250) # 250 jest większe bądź równe 250 (True)
# print(24 == 12) # 24 równa się 12 (False)
# print(40 != 20) # 40 jest różne od 20 (True)


# print(12 == 15) # Fałsz
# print(5 <= 15000) # Prawda
# print(120 != 120) # Fałsz
# print(60 <= 15) # Fałsz
# print(25.3421 <= 25.3421) # Prawda

'''
Zaimplementuj kod sprawdzający czy użytkownik, który poda swój wzrost może wejść na kolejkę.
Kryteria: Wzrost osoby(pobierana informacja od użytkownika, wyrażony w cm, musi być większy niż 150).
'''

print("Czy możesz korzystać z roller-coastera?")
wzrost = int(input("Podaj swój wzrost w cm: "))

# np. 160 cm wzrostu 
werdykt = wzrost > 150  # werdykt = True
print(werdykt) # True

# DZIAŁANIA LOGICZNE 

# NOT
# print(not True) # not - operator negacji, zaprzeczenia
# print(not False)

# print(not 50 == 51) # not False => True
# print(not 2 < 10) # not True => False

# print(not(not 4 > 10)) # not (not False) => not True => False


# AND 
# print(True and True) # True
# print(True and False) # False
# print(False and False) # False

# print(2 < 4 and 50 != 51) # True and True => True

# OR
# print(True or True) # True
# print(True or False) # True
# print(False or False) # False

# print(2 > 4 or 50 != 51) # False or True => True

not ( 2 > 3 and 3 > 2) # not (False and True) => not False => True

10 > 3 or (not 10 != 11) # 10 > 3 or (not True) => 10 > 3 or False => True or False => True

(not 11 == 10) and (11 >= 11.01 or 10 < 12) # (not False) and (False or True) => True and True => True


# Aby wejść do wagonika użytkownik musi być wyższy niż 150cm i jednocześnie niższy niż 215cm

print("Czy możesz korzystać z roller-coastera?")
wzrost = int(input("Podaj swój wzrost w cm: "))

# np. 160 cm wzrostu 
werdykt = wzrost > 150 and wzrost < 215 # werdykt = True and True => werdykt = True
# werdykt = 150 < wzrost < 215 # -> Ciekawostka, te równanie sprawdza czy liczba mieści się w określonym przedziale
print(werdykt)

# w lukę między równaniami wstaw odpowiedni operator logiczny, aby uzyskać oczekiwany wynik
print(True, 25 < 140 and 10 == 10) 
print(True, 100 >= 1 or 2 > 10)
print(False, 25 < 14 and 10 != 10)
print(False, -1 < 3 and 2 < 9 and 10 == 15)
print(True, 20.05 < 21 < 10 or -10 < 20 < 150 <= 150)
print(False, 1 < 10 and 2 < 15 and -50 == 42)
print(True, not 2 == 10)














