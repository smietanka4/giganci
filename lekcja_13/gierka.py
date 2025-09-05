# Import modulu pygame, dzieki ktoremu tworzymy aplikacje okienkowa
import pygame
 
# Inicjalizacja modułu
pygame.init()
# Utworzenie okna o określonych wymiarach
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
 
screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Nadanie nazwy oknu
pygame.display.set_caption('Pierwsza Gra')
 
# Utworzenie zegara, który nadzoruje stałe wartości fps
clock = pygame.time.Clock()
 
 
def load_image(img_path: str, position):
    image = pygame.image.load(img_path)
    surface = image.convert()
 
    transparent_color = (0, 0, 0)
    surface.set_colorkey(transparent_color)
 
    # Pozycja wyświetlania obiektu zapisana jest w rect
    rect = surface.get_rect(center=position)
 
    return [image, surface, rect]
 
 
def print_image(img_list) -> None:
    # [image, surface, rect]
    image, surface, rect = img_list
    screen_surface.blit(surface, rect)
    pass

def set_position_image(img_list, position):
    image, surface, rect = img_list
    rect = surface.get_rect(center=position)
    return [image, surface, rect]

def calculate_player_movement(keys):
    # Poruszanie postacią
    delta_x = 0
    delta_y = 0
    speed = 10

    if keys[pygame.K_w]:
        delta_y -= speed
    if keys[pygame.K_s]:
        delta_y += speed
    if keys[pygame.K_a]:
        delta_x -= speed
    if keys[pygame.K_d]:
        delta_x += speed

    return [delta_x, delta_y]
    
def limit_position(position): # -> limitowanie ruchu gracza
    x, y = position
    x = max(0, min(x, SCREEN_WIDTH))
    y = max(0, min(y, SCREEN_HEIGHT))
    return [x, y]
 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player = load_image('lekcja_13/grafiki/gracz.png', player_pos)
background_color = [255, 255, 255]
 
# Zmienna określająca, czy należy zamknąć okno
game_status = True
# Kod wykonywany póki aplikacja jest uruchomiona -> Główna pętla gry
while game_status:
 
    # Odczytanie zdarzeń zarejestrowanych przez komputer
    events = pygame.event.get()
 
    for event in events:
        # Naciśnięto X - zamykanie aplikacji
        if event.type == pygame.QUIT:
            game_status = False
        pass  # for event

    pressed_keys = pygame.key.get_pressed()

    # # # # # # # # # # # # # # # # # # # # 
    delta_x, delta_y = calculate_player_movement(pressed_keys)

    # Zmiana wartości współrzędnych
    player_pos[0] += delta_x
    player_pos[1] += delta_y

    player_pos = limit_position(player_pos)

    player = set_position_image(player, player_pos)

    # Uzupełnianie tła
    screen_surface.fill(background_color)
 
    # Wyświetlamy gracza
    print_image(player)
 
    # Odświeżenie wyświetlanego okna
    pygame.display.update()
 
    clock.tick(60)
    pass
 
print("Zamykanie aplikacji")
# Zamknięcie aplikacji
pygame.quit()
# Zamknięcie skryptu
quit()