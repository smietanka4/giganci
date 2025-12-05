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

# dodanie obiektu czcionki
pygame.font.init()
moja_czcionka = pygame.font.SysFont('Comic Sans MS', 30)


# ===== Obiekty =====
# elementy stroju
nakrycie_glowy = Element.NakrycieGlowy()
ubranie_element = Element.Stroj()
oczy_element = Element.Oczy()
bron_element = Element.Bron()

def wypisz_tekst(ekran, tekst, pozycja):
      napis = moja_czcionka.render(tekst, False, (75, 239, 234))
      ekran.blit(napis, pozycja)

# główna pętla gry
gra_dziala = True
zapisywanie = False
id = 1
while gra_dziala:
      # obsługa zdarzeń
      for zdarzenie in pygame.event.get():
            # naciśnięcie klawiszy
            if zdarzenie.type == pygame.KEYDOWN:
                  if zdarzenie.key == pygame.K_ESCAPE:
                        gra_dziala = False 
                  if zdarzenie.key == pygame.K_q:
                        nakrycie_glowy.wybierzNastepny()
                  if zdarzenie.key == pygame.K_w:
                        oczy_element.wybierzNastepny()
                  if zdarzenie.key == pygame.K_e:
                        ubranie_element.wybierzNastepny()
                  if zdarzenie.key == pygame.K_r:
                        bron_element.wybierzNastepny()
                  if zdarzenie.key == pygame.K_SPACE:
                        zapisywanie = True
                  
            # naciśnięcie przycisku X
            elif zdarzenie.type == pygame.QUIT:
                  gra_dziala = False

      # rysowanie tła
      ekran.blit(obraz_tla, (0,0))
      # rysowanie bazy postaci
      ekran.blit(obraz_bazy_postaci, (270,130))
      ekran.blit(nakrycie_glowy.wybranyObraz(), (270,130))
      ekran.blit(ubranie_element.wybranyObraz(), (270,130))
      ekran.blit(oczy_element.wybranyObraz(), (270,130))
      ekran.blit(bron_element.wybranyObraz(), (270,130))

      # zapisywanie
      if zapisywanie:
            pygame.image.save(ekran, f'lekcja_24_25/postac_{id}.png')
            id += 1
            zapisywanie = False

      wypisz_tekst(ekran, f'[Q] Glowa: {nakrycie_glowy.wybrany}', (80,130))
      wypisz_tekst(ekran, f'[W] Oczy: {oczy_element.wybrany}', (80,170))
      wypisz_tekst(ekran, f'[E] Strój: {ubranie_element.wybrany}', (80,210))
      wypisz_tekst(ekran, f'[R] Broń: {bron_element.wybrany}', (80,250))
      wypisz_tekst(ekran, f'[SPACE] Save', (80, 290))


      # wyczyszczenie ekranu
      pygame.display.flip()
      # ustalenie stałych fps na 60
      zegar.tick(60)

# koniec pętli while

# zamknięcie aplikacji
pygame.quit()