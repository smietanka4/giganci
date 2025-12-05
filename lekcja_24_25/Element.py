import pygame

# klasa pomocniczna Obraz
class Obraz(pygame.sprite.Sprite):
      def __init__(self, sciezka):
            super().__init__()
            self.obraz = pygame.image.load(sciezka)

# klasa bazowa
class Element():
      def __init__(self, typ):
            # wskaźnik wybranego elementu ubioru
            self.wybrany = 0
            # lista obrazów
            self.lista_obrazow = []

            # używamy pętli żeby wczytać wszystkie obrazy z folderu
            for i in range(1,4):
                  sciezka = f'lekcja_24_25/images/{typ}{i}.png'
                  wczytany_obraz = Obraz(sciezka)
                  self.lista_obrazow.append(wczytany_obraz)

      def wybierzNastepny(self):
            self.wybrany += 1
            if self.wybrany > 2:
                  self.wybrany = 0
            
      def wybranyObraz(self):
            return self.lista_obrazow[self.wybrany].obraz
      
class NakrycieGlowy(Element):
      def __init__(self):
            super().__init__('head')

class Stroj(Element):
      def __init__(self):
            super().__init__('body')

class Oczy(Element):
      def __init__(self):
            super().__init__("eye")

class Bron(Element):
      def __init__(self):
            super().__init__("weapon")