import pygame, random
pygame.init()

#värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]
 
#ekraani seaded
screenX = 640
screenY = 480
screen=pygame.display.set_mode([screenX,screenY])
pygame.display.set_caption("Hiir")
screen.fill(lBlue)
clock = pygame.time.Clock()

gameover = False
while not gameover:
    clock.tick(10)
    #mängu sulgemine ristist
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

    click = pygame.mouse.get_pressed()
    print(click)
    
    mousePos = pygame.mouse.get_pos()
    print(mousePos)
        
    pygame.display.flip()
    screen.fill(lBlue)

pygame.quit()