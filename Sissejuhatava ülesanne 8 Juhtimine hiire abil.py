import pygame, random  # Impordib pygame ja random moodulid, pygame on mängude tegemiseks ja random on juhuslike numbrite genereerimiseks
pygame.init()  # Initsialiseerib kõik pygame moodulid

# Värvid (määratletud RGB väärtustega)
red = [255, 0, 0]  # Punane värv
green = [0, 255, 0]  # Roheline värv
blue = [0, 0, 255]  # Sinine värv
pink = [255, 153, 255]  # Roosa värv
lGreen = [153, 255, 153]  # Heleroheline värv
lBlue = [153, 204, 255]  # Helesinine värv

# Ekraani seaded
screenX = 640  # Ekraani laius pikslites
screenY = 480  # Ekraani kõrgus pikslites
screen = pygame.display.set_mode([screenX, screenY])  # Luuakse ekraani pindala antud mõõtmetega
pygame.display.set_caption("Hiir")  # Seadistatakse akna tiitel
screen.fill(lBlue)  # Täidetakse ekraan helesinise värviga
clock = pygame.time.Clock()  # Luuakse kell objekti, et hallata kaadrisagedust

gameover = False  # Mängu oleku muutuja, mis näitab, kas mäng on lõppenud
while not gameover:  # Peamine mängu tsükkel, mis kestab kuni gameover on False
    clock.tick(10)  # Seadistatakse mängu tsüklite sagedus 10 kaadrit sekundis
    # Mängu sulgemine ristist
    for event in pygame.event.get():  # Läbitakse kõik sündmused, mis on toimunud
        if event.type == pygame.QUIT:  # Kui sündmus on akna sulgemine
            gameover = True  # Määratakse gameover True-ks, et lõpetada mängutsükkel

    click = pygame.mouse.get_pressed()  # Saadakse hiireklõpsude olek (nupud, mis on vajutatud)
    print(click)  # Prinditakse hiireklõpsude olek konsooli
    
    mousePos = pygame.mouse.get_pos()  # Saadakse hiirekursor asukoht ekraanil
    print(mousePos)  # Prinditakse hiirekursor asukoht konsooli
        
    pygame.display.flip()  # Uuendatakse ekraani, et näidata kõiki joonistatud objekte
    screen.fill(lBlue)  # Täidetakse ekraan helesinise värviga igal tsüklil

pygame.quit()  # Lõpetatakse pygame moodulite töö ja suletakse mäng
