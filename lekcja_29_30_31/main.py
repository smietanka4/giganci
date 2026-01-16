import pygame
from Platforma import Platforma
from Kulka import Kulka
from Klocek import Klocek
 
#wysokość i szerokość ekranu
SZEROKOSC_EKRANU = 1024 
WYSOKOSC_EKRANU = 800
zycia = 3
poziom = 0
 
#ustawienia pygame
pygame.init()
pygame.font.init()
 
#obiekty ekranu, zegara i tła, czcionki
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
obraz_tla = pygame.image.load('lekcja_29_30_31/images/background.png')
czcionka = pygame.font.SysFont('Comic Sans MS', 28)
 
# poziomy gry
poziom1 = [
      [0, 0, 1, 1, 2, 2, 1, 1, 0, 0],
      [0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
      [0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
      [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
      [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
]

poziom2 = []

klocki = pygame.sprite.Group()
def dodaj_klocki():
      wczytany_poziom = None
      if poziom == 0:
             wczytany_poziom = poziom1
      if poziom == 1:
             wczytany_poziom = poziom2

      for i in range(10):
             for j in range(6):
                    if wczytany_poziom[j][i] != 0:
                           klocek = Klocek(32+i*96, 32+j*48, wczytany_poziom[j][i])
                           klocki.add(klocek)

dodaj_klocki()

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

      # sprawdzenie czy wszystkie klocki zostały zniszczone
      if len(klocki.sprites()) == 0:
            poziom += 1
            if poziom >= 2: 
                  break
            kulka.zresetuj_pozycje()
            platforma.zresetuj_pozycje()
            dodaj_klocki()
        
      # aktualizacja kulki
      kulka.aktualizuj(platforma, klocki)

      if kulka.przegrana:
            '''
            System żyć:
                  -> Jeżeli masz jeszcze życia, to ...
                  -> Jeżeli nie masz żyć to ...
            '''
            zycia -= 1
            if zycia <= 0:
                  break
            kulka.zresetuj_pozycje()
            platforma.zresetuj_pozycje()


      # aktualizacja platformy
      klocki.update()
      platforma.aktualizuj()

      #wyświetl tło
      ekran.blit(obraz_tla, (0,0))
      
      # wyświetlanie klocków
      for klocek in klocki:
            ekran.blit(klocek.obraz, klocek.rect)

      #wyświetl platformę
      ekran.blit(platforma.obraz, platforma.rect)
      ekran.blit(kulka.obraz, kulka.rect)

      # wyświetlanie wyniku
      tekst = czcionka.render(f'Życia: {zycia}', False, (115, 255, 0))
      ekran.blit(tekst, (16, 16))
      
      pygame.display.update()
      zegar.tick(30)
 
pygame.quit()