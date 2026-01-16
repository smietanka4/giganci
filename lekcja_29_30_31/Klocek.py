import pygame
import copy

class Klocek(pygame.sprite.Sprite):
      def __init__(self, x, y, zdrowie):
            super(Klocek, self).__init__()
            self.obraz_oryginalny = pygame.image.load("lekcja_29_30_31/images/brick.png")
            self.rect = pygame.Rect(x, y, 96, 48)
            self.zdrowie = zdrowie

      # aktualizacja
      def aktualizuj(self):
            maska_koloru = 0
            if self.zdrowie == 3:
                  maska_koloru = (0, 185, 0)
            if self.zdrowie == 2:
                  maska_koloru = (255, 165, 0)
            if self.zdrowie == 1:
                  maska_koloru = (200, 0, 0)
            self.obraz = copy.copy(self.obraz_oryginalny)
            self.obraz.fill(maska_koloru, special_flags=pygame.BLEND_ADD)

      def update(self):
            self.aktualizuj()

      # funkcja wywoływana podczas zderzenia z kulką
      def uderzenie(self):
            self.zdrowie -= 1
            if self.zdrowie <= 0:
                  self.kill()