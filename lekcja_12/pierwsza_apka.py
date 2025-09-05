import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pierwsza Gra')

clock = pygame.time.Clock()


# Funkcja odpowiedzialna za wczytanmie grafiki obrazu oraz przygotowanie jej do wykorzystania w aplikacji
def load_image(img_path: str, position): 
    image = pygame.image.load(img_path) # -> obraz
    surface = image.convert() # -> powierzchnia

    transparent_color = (0,0,0)
    surface.set_colorkey(transparent_color)
    

    # Pozycja wyświetlania obiektu zapisana jest w rect
    rect = surface.get_rect(center=position) # -> skrót od rectangle - prostokąt

    return [image, surface, rect]
    
def print_image(img_list) -> None:
    image, surface, rect = img_list
    screen_surface.blit(surface, rect)
    pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player = load_image('lekcja_12/grafiki/player.png', player_pos)

# Zmienna określająca, czy należy zamknąć okno
game_status = True

while game_status:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game_status = False
        pass

    screen_surface.fill([120, 50, 255]) # zmiana tła gry (te cyferki w środku to RGB, kolejno R -> red, G -> green, B -> blue)

    # Wyświetlamy gracza
    print_image(player)

    # Odświeżamy wyświetlane okno
    pygame.display.update()
    clock.tick(60)
    pass

print("Zamykanie aplikacji")
pygame.quit()
quit()