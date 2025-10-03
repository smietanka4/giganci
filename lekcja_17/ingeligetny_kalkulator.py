zero = ["0", "zero", "zera", "zerem", "zeri"]
jeden = ["1", "jeden", "jedynka", "jedynkę", "raz"]
dwa = ['2', 'dwa', 'dwójkę', 'dwójka']
trzy = ['3', 'trzy', 'trójka', 'trójkę']
cztery = ['4', 'cztery', 'czwórkę', 'czwórka']
pięć = ['5', 'pięć', 'piątkę', 'piątka']
sześć = ['6', 'szcześć', 'szóstkę', 'szóstka']
siedem = ['7', 'siedem','siódemkę',' siódemka']
osiem = ['8', 'osiem', 'ósemkę', 'ósemka']
dziewięć = ['9', 'dziewięć', 'dziewiątka',' dziewiątkę']
dziesięć = ['10', 'dziesiątka', 'dziesięć', 'dziesiątkę', 'dychę']
plus = ['+', "dodaj", "plus", "dodać"]
minus = ['-', 'minus', 'odjąć', 'odjąc','odjac', 'odjać', 'odejmij']
mnożenie = ["*", 'x', 'razy', 'mnożone','pomnożone', 'pomnożyć']
dzielenie = ['/', ':', 'dzielone','dzielnik', 'podziel']

# BAZA 
baza = [zero, jeden, dwa, trzy, cztery, pięć, sześć, siedem, osiem, dziewięć, dziesięć, plus, minus, mnożenie, dzielenie]

# Funkcje

def przetlumacz(slowo):
   for baza_symbolu in baza:
      for slowo_bazy_symbolu in baza_symbolu:
         if slowo == slowo_bazy_symbolu:
            return baza_symbolu[0] # zwraca my pierwszy element listy w której znaleźliśmy pasujące słowo
   return "" # jeśli słowo, które próbujemy przetłumaczyć na liczbę lub operator nie występuje w naszych tablicach to je pomijamy

def oblicz(liczba1, liczba2, operacja):
    if operacja == '+':
        return liczba1 + liczba2
    elif operacja == '-':
        return liczba1 - liczba2
    elif operacja == '*':
        return liczba1 * liczba2
    elif operacja == "/":
        return liczba1/liczba2

def oblicz_z_tekstu(tekst):
    wynik = 0 
    liczba = ''
    operacja = ''

    for znak in tekst:
      if znak.isdigit():
            liczba += znak
      elif liczba:
            if operacja == '':
                  wynik = int(liczba)
            else:
                  wynik = oblicz(wynik, int(liczba), operacja)
            liczba = ''
            operacja = znak

    if liczba:
        wynik = oblicz(wynik, int(liczba), operacja)

    return wynik
            
# Główny program

kontynuacja = True
while kontynuacja == True:

      dzialanie = ""
      tekst = input("podaj tekst: ")

      # Jak w jednej linijce napisać kod aby przeszukiwał słowa w liście słów?

      for slowo in tekst.split(" "):
            dzialanie += przetlumacz(slowo)

      print(dzialanie)
      print(oblicz_z_tekstu(dzialanie))

      kontynuowanie = input("Czy chcesz kontynuować działanie programu (tak/nie)?")
      if kontynuowanie == 'nie':
          print("Kalkulator się wyłącza.")
          kontynuacja = False
          
          