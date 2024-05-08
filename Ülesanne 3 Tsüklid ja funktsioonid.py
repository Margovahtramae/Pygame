import pygame
import sys

# Funktsioon ruutude joonistamiseks
def draw_grid(screen, rows, cols, square_size, line_color):
    for i in range(rows):
        for j in range(cols):
            pygame.draw.rect(screen, line_color, (j * square_size, i * square_size, square_size, square_size), 1)

# Mängu algseadistus
def main(rows, cols, square_size, line_color):
    # Initsialiseeri Pygame
    pygame.init()
    
    # Ekraani seadistamine
    screen = pygame.display.set_mode((cols * square_size, rows * square_size))
    pygame.display.set_caption("Ruutude mäng")
    
    # Mängutsükkel
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Tühjenda ekraan
        screen.fill((0, 255, 0))
        
        # Joonista ruudustik
        draw_grid(screen, rows, cols, square_size, line_color)
        
        # Uuenda ekraani
        pygame.display.flip()
    
    # Lõpeta Pygame
    pygame.quit()
    sys.exit()

# Määra parameetrid
rows = 24
cols = 32
square_size = 20
line_color = (255, 0, 0)

# Käivita mäng
main(rows, cols, square_size, line_color)

    
