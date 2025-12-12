import pygame
import time
import random
from Jablko import Jablko
from Kierunek import Kierunek
from Waz import Waz

# stałe
SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 608

tlo = pygame.Surface((SZEROKOSC_EKRANU, WYSOKOSC_EKRANU))

for i in range(25):
      for j in range(19):
            obraz = pygame.image.load("lekcja_26_27/images/background.png")
            maska = (random.randrange(0,20), random.randrange(0,20), random.randrange(0,20))

            obraz.fill(maska, special_flags=pygame.BLEND_ADD)
            tlo.blit(obraz, (i*32,j*32))

# ustawienia
pygame.init()

# obiekty
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
fps = pygame.time.Clock()

jablko = Jablko()
jablka = pygame.sprite.Group()
jablka.add(jablko)

# Wąż
waz = Waz()
PORUSZ_WEZEM = pygame.USEREVENT + 1
pygame.time.set_timer(PORUSZ_WEZEM, 200)

gra_dziala = True
while gra_dziala:
      # obsługa zdarzeń
      for event in pygame.event.get():
            print(event)
            if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_ESCAPE:
                        gra_dziala = False
                  if event.key == pygame.K_w:
                        waz.zmien_kierunek(Kierunek.GORA)
                  if event.key == pygame.K_s:
                        waz.zmien_kierunek(Kierunek.DOL)
                  if event.key == pygame.K_a:
                        waz.zmien_kierunek(Kierunek.LEWO)
                  if event.key == pygame.K_d:
                        waz.zmien_kierunek(Kierunek.PRAWO)

            elif event.type == PORUSZ_WEZEM:
                  waz.aktualizuj()

            elif event.type == pygame.QUIT:
                  gra_dziala = False

      ekran.blit(tlo, (0,0))
      ekran.blit(waz.glowa, waz.rect)

      for jablko in jablka:
            ekran.blit(jablko.obraz, jablko.rect)

      pygame.display.update()
      fps.tick(60)

time.sleep(2)
pygame.quit()

      


