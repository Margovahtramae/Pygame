import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine")
screen.fill([204, 255, 204])

#lisame teksti
font = pygame.font.Font(None, 30)
text = font.render("Hello PyGame", True, [0,0,0])
screen.blit(text, [200,200])

#lisame teksti
font = pygame.font.Font(pygame.font.match_font('arial'), 50)
text = font.render("Hello PyGame", True, [0,0,0])

#tekstikasti suurus
text_width = text.get_rect().width
text_height = text.get_rect().height

screen.blit(text, [320,240])

#lisame teksti
font = pygame.font.Font(pygame.font.match_font('arial'), 50)
font.set_underline(True)
text = font.render("Hello PyGame", True, [0,0,0])

#tekstikasti suurus
text_width = text.get_rect().width
text_height = text.get_rect().height

screen.blit(text, [320-text_width/2,240-text_height/2])




# Seab muutuja "running" väärtuseks "True"
running = True


# Mängutsükkel
while running:
    # Käsitseb sündmusi
    for event in pygame.event.get():
        # Kui kasutaja vajutab sulgemisnuppu
        if event.type == pygame.QUIT:
            # Muudab muutuja "running" väärtuseks "False", mis peatab mängutsükli
            running = False

    pygame.display.flip()

# Lõpetab pygame'i kasutamise
pygame.quit()