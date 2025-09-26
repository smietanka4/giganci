def glowne_menu():
    '''
    Funkcja powinna wyświetlać 4 podpunkty:
    1. Wpłata
    2. Wypłata
    3. Sprawdzenie stanu konta
    4. Zakończ
    '''
    print("Wybierz opcję")
    print("1. Wpłata")
    print("2. Wypłata")
    print("3. Sprawdzenie stanu konta")
    print("4. Zakończ")

    opcja = int(input("Twój wybór to: "))
    return opcja

def pobierz_kwote(tekst): 
    return int(input(tekst))

def pokaz_stan_konta(saldo):
    print(f'Stan konta wynosi {saldo} złotych')

def wplata(saldo):
    '''
    Dodawanie gotówki do salda na koncie i pokazanie stanu konta. 
    Sprawdzamy czy wpłacana kwota nie jest mniejsza od zera.
    '''
    kwota_wplaty = pobierz_kwote("Ile chcesz wpłacić?")
    if kwota_wplaty > 0:
        saldo += kwota_wplaty
    else:
        print("Wprowadzona kwota jest niepoprawna.")
    pokaz_stan_konta(saldo)
    return saldo

def wyplata(saldo):
    '''
    Odejmować gotówkę z salda na koncie o podaną wartość.
    Sprawdzamy czy podana kwota nie jest większa od tego ile mamy na koncie.
    Pokazać stan konta
    '''
    kwota_wyplaty = pobierz_kwote("Ile chcesz wypłacić?")
    if kwota_wyplaty > saldo or kwota_wyplaty < 0:
        print("Operacja nieudana, za mało środków na koncie")
        return saldo
    else:
        saldo -= kwota_wyplaty
        print(f'Wypłacono {kwota_wyplaty} złotych')
        pokaz_stan_konta(saldo)
        return saldo
    
# powyżej nich będziemy pisać wszystkie funkcje naszego programu
wybor = 0
saldo = 0

# poniżej będzie główna pętla programu
while wybor != 4:
    wybor = glowne_menu()
    if wybor == 1: # Wpłata
        saldo = wplata(saldo)
        pass
    elif wybor == 2: # Wypłata
        saldo = wyplata(saldo)
        pass
    elif wybor == 3: # Pokazaniem stanu konta
        pokaz_stan_konta(saldo)
        pass
    elif wybor == 4:
        print("Wyłączanie bankomatu")
        pass
    else:
        print("Niepoprawne dane")
        pass
    pass


    
    
