# dodanie modułu pygame
import pygame
# zaimportowanie stworzonego pliku Element.py
import Element

pygame.init()

# Stałe
SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 600

# wczytanie obrazów do zmiennych
obraz_tla = pygame.image.load('lekcja_24_25\images/background.png')
obraz_bazy_postaci = pygame.image.load("lekcja_24_25\images/base.png")

# utworzenie obiektów ekranu oraz FPS
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

# elementy stroju
nakrycie_glowy = Element.NakrycieGlowy()
ubranie_element = Element.Stroj()
oczy_element = Element.Oczy()
bron_element = Element.Bron()

# główna pętla gry
gra_dziala = True
while gra_dziala:
      # obsługa zdarzeń
      for zdarzenie in pygame.event.get():
            # naciśnięcie klawiszy
            if zdarzenie.type == pygame.KEYDOWN:
                  if zdarzenie.key == pygame.K_ESCAPE:
                        gra_dziala = False 
            # naciśnięcie przycisku X
            elif zdarzenie.type == pygame.QUIT:
                  gra_dziala = False

      # rysowanie tła
      ekran.blit(obraz_tla, (0,0))
      # rysowanie bazy postaci
      ekran.blit(obraz_bazy_postaci, (270,130))

      # wyczyszczenie ekranu
      pygame.display.flip()
      # ustalenie stałych fps na 60
      zegar.tick(60)

# koniec pętli while

# zamknięcie aplikacji
pygame.quit()