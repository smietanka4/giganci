'''
1. Napisz program aplikacji graficznej, która co 3 sekundy zmienia kolor tła. Nowy kolor tła powinien być losowany.
Pamiętaj o wykorzystaniu liczby klatek do wykrycia kiedy mijają kolejne 3 sekundy
Pamiętaj o budowaniu koloru RGB:
RGB składa się z trzech kolorów, każdy może przyjąć wartość od 0 do 255 (włącznie)
RGB = [R, G, B] możesz przechowywać to jako listę
'''

import pygame
import random

# Inicjalizacja
pygame.init()


# Stałe
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

# Zmienne
frame_count = 0
background_color = [random.randint(0,255) for _ in range(3)]

# Główna pętla
running = True

while running:
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  running = False

      frame_count += 1
      if frame_count >= 3 * FPS:
            background_color = [random.randint(0,255) for _ in range(3)]
            frame_count = 0


      screen_surface.fill(background_color)
      pygame.display.update()
      clock.tick(FPS)

pygame.quit()

quit()





