import pygame
from Platforma import Platforma
from Kulka import Kulka
 
#wysokość i szerokość ekranu
SZEROKOSC_EKRANU = 1024 
WYSOKOSC_EKRANU = 800
 
#ustawienia pygame
pygame.init()
 
#obiekty ekranu, zegara i tła
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
obraz_tla = pygame.image.load('lekcja_29_30_31/images/background.png')
 
#obiekt platformy
platforma = Platforma()

#obiekt kulki
kulka = Kulka()

#główna pętla
gra_dziala = True
while gra_dziala:
      for zdarzenie in pygame.event.get():
            if zdarzenie.type == pygame.KEYDOWN:
                  if zdarzenie.key == pygame.K_ESCAPE:
                        gra_dziala = False
            elif zdarzenie.type == pygame.QUIT:
                        gra_dziala = False
 
    #sterowanie platformą
      wcisniete_klawisze=pygame.key.get_pressed()
      if wcisniete_klawisze[pygame.K_a]:
            platforma.ruszaj_platforma(-1)
      if wcisniete_klawisze[pygame.K_d]:
            platforma.ruszaj_platforma(1)
        
      # aktualizacja kulki
      kulka.aktualizuj(platforma)

      if kulka.przegrana:
             '''
             System żyć:
                  -> Jeżeli masz jeszcze życia, to ...
                  -> Jeżeli nie masz żyć to ...
             '''

      # aktualizacja platformy
      platforma.aktualizuj()

      #wyświetl tło
      ekran.blit(obraz_tla, (0,0))
      
      #wyświetl platformę
      ekran.blit(platforma.obraz, platforma.rect)
      ekran.blit(kulka.obraz, kulka.rect)
      
      pygame.display.update()
      zegar.tick(30)
 
pygame.quit()