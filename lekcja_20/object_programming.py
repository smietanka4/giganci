from uzytkownik import Uzytkownik

user1 = Uzytkownik()
user1.imie = "Jan"
user1.nazwisko = "Kowalski"
user1.wiek = 30

user2 = Uzytkownik()
user2.imie = "Adam"
user2.nazwisko = "Nowak"
user2.wiek = 12


user3 = Uzytkownik()
user3.imie = "Piotr"
user3.nazwisko = "Murarz"
user3.wiek = 18

user1.info()
user2.info()
user3.info()

user1.zmien_wiek(19)
user1.info()
