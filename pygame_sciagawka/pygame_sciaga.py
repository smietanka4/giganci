import pygame
import random
import sys

# --- 1. INICJALIZACJA I USTAWIENIA ---
pygame.init() # "Budzik" - bez tego moduły pygame'a nie zadziałają

SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 608
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU]) # Tworzenie okna gry pygame
pygame.display.set_caption("Sciagawka") # Ustawianie wyświetlanego tytułu u góry okna

# Kolory (RGB)
BIALY = (255, 255, 255)
CZARNY = (0, 0, 0)

# --- 2. GENEROWANIE TŁA (Twoja logika Surface) ---
# Surface to "płótno". Tworzymy jedno duże tło raz, żeby nie obciążać procesora w pętli.
tlo = pygame.Surface((SZEROKOSC_EKRANU, WYSOKOSC_EKRANU))
for i in range(25):
    for j in range(19):
        # Tworzymy mały kafelek 32x32
        kafel = pygame.Surface((32, 32))
        # Losujemy odcień zieleni
        maska = (random.randrange(0, 20), random.randrange(100, 150), random.randrange(0, 20))
        kafel.fill(maska)
        # .blit() - nakładamy kafel na duże tło (tlo)
        tlo.blit(kafel, (i * 32, j * 32))

# --- 3. TEKST NA EKRANIE ---
# KROK 1: Wybór czcionki systemowej (Nazwa, rozmiar, pogrubienie)
czcionka = pygame.font.SysFont("Arial", 22, bold=True)

# KROK 2: .render() - zamiana tekstu na obrazek (Surface)
# (tekst, antyaliasing, kolor tekstu)
instrukcja = czcionka.render("Strzałki: move_ip | R: transform (obrót) | ESC: Wyjście", True, BIALY)

# --- 4. OBIEKT I JEGO .RECT ---
# Tworzymy obrazek gracza
gracz_oryginal = pygame.Surface((64, 64), pygame.SRCALPHA)
pygame.draw.rect(gracz_oryginal, (255, 0, 0), (0, 0, 64, 64)) # Czerwony kwadrat
pygame.draw.circle(gracz_oryginal, (255, 255, 255), (32, 15), 8) # "Oczy" dla orientacji

# .get_rect() - To kluczowa metoda! 
# Tworzy niewidzialny prostokąt o wymiarach obrazka. 
# Dzięki center=(...) od razu ustawiamy go na środku ekranu.

# W Pygame musimy odróżnić dwie rzeczy:
# Surface (Powierzchnia): To, co widzimy (kolory, piksele, obrazek .png).
# Rect (Prostokąt): To, gdzie to jest i ile miejsca zajmuje.
gracz_rect = gracz_oryginal.get_rect(center=(SZEROKOSC_EKRANU // 2, WYSOKOSC_EKRANU // 2))

# Zmienne pomocnicze
kat = 0
gracz_wyswietlany = gracz_oryginal
fps = pygame.time.Clock()

# --- 5. WŁASNE ZDARZENIE (Z Twojego projektu) ---
# USEREVENT + n pozwala tworzyć własne sygnały czasowe (np. do ruchu węża)
AUTO_RUCH = pygame.USEREVENT + 1
pygame.time.set_timer(AUTO_RUCH, 1000) # Co 1000ms (1 sekunda)

# --- 6. GŁÓWNA PĘTLA GRY ---
gra_dziala = True
while gra_dziala:
    # A. OBSŁUGA ZDARZEŃ
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gra_dziala = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gra_dziala = False

            # .move_ip(x, y) - MOVE IN PLACE.
            # Zmienia współrzędne wewnątrz istniejącego Recta. 
            # To najszybszy sposób na ruch w Pygame.
            if event.key == pygame.K_LEFT:  
                gracz_rect.move_ip(-32, 0)
            if event.key == pygame.K_RIGHT: 
                gracz_rect.move_ip(32, 0)
            if event.key == pygame.K_UP:   
                gracz_rect.move_ip(0, -32)
            if event.key == pygame.K_DOWN:  
                gracz_rect.move_ip(0, 32)
            
            # .transform 
            if event.key == pygame.K_r:
                kat += 45
                # Zawsze zapamiętujemy środek przed obrotem!
                stary_srodek = gracz_rect.center
                
                # Obracamy oryginał (bo wielokrotne obracanie kopii niszczy jakość)
                gracz_wyswietlany = pygame.transform.rotate(gracz_oryginal, kat)
                
                # Po obrocie Rect się powiększył (bo obrazek jest pod kątem).
                # Tworzymy nowy Rect i "przypinamy" go do starego środka.
                gracz_rect = gracz_wyswietlany.get_rect(center=stary_srodek)

        # Obsługa własnego zdarzenia (Timer)
        elif event.type == AUTO_RUCH:
            print("Zdarzenie czasowe: Tik-Tak!")

    # B. RYSOWANIE (Kolejność warstw ma znaczenie!)
    ekran.blit(tlo, (0, 0)) # Najpierw tło
    
    # Wyświetlamy tekst (KROK 3: .blit())
    # Rysujemy czarny pasek pod tekstem dla czytelności
    pygame.draw.rect(ekran, CZARNY, (0, 0, SZEROKOSC_EKRANU, 40))
    ekran.blit(instrukcja, (10, 8))
    
    # Rysujemy gracza - podajemy powierzchnię i jego Rect
    ekran.blit(gracz_wyswietlany, gracz_rect)

    # C. AKTUALIZACJA
    pygame.display.update() # Odświeżenie obrazu na monitorze
    fps.tick(60) # Stałe 60 klatek na sekundę

pygame.quit()