import pygame
from Kierunek import Kierunek

class Waz(pygame.sprite.Sprite):
      def __init__(self):
            self.oryginalna_glowa = pygame.image.load("lekcja_26_27/images/head.png")
            # obraz pomocniczny, będzie się on zmieniał przy zmianie kierunku gracza
            self.glowa = pygame.transform.rotate(self.oryginalna_glowa, 0)

            # współrzędne głowy
            self.rect = self.glowa.get_rect(center=(12*32+16, 9*32+16))

            self.kierunek = Kierunek.GORA
            self.nowy_kierunek = Kierunek.GORA

      def zmien_kierunek(self, kierunek):
            zmiana_mozliwa = True
            if kierunek == Kierunek.GORA and self.kierunek == Kierunek.DOL:
                  zmiana_mozliwa = False
            if kierunek == Kierunek.DOL and self.kierunek == Kierunek.GORA:
                  zmiana_mozliwa = False
            if kierunek == Kierunek.LEWO and self.kierunek == Kierunek.PRAWO:
                  zmiana_mozliwa = False
            if kierunek == Kierunek.PRAWO and self.kierunek == Kierunek.LEWO:
                  zmiana_mozliwa = False
            
            if zmiana_mozliwa:
                  self.nowy_kierunek = kierunek
            
      def aktualizuj(self):
            self.kierunek = self.nowy_kierunek
            self.glowa = pygame.transform.rotate(self.oryginalna_glowa,self.kierunek.value*90)

            if self.kierunek == Kierunek.GORA:
                  self.rect.move_ip(0, -32)
            if self.kierunek == Kierunek.PRAWO:
                  self.rect.move_ip(32, 0)
            if self.kierunek == Kierunek.LEWO:
                  self.rect.move_ip(-32, 0)
            if self.kierunek == Kierunek.DOL:
                  self.rect.move_ip(0, 32)





            

 