import pygame  # Imporditakse pygame moodul, et kasutada selle funktsioone mängude loomiseks
import random  # Imporditakse random moodul, et genereerida juhuslikke väärtusi

pygame.init()  # Initsialiseeritakse kõik pygame moodulid

# Värvide genereerimise funktsioon
def get_random_color():
    return [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    # Funktsioon tagastab juhuslikult genereeritud värvi RGB formaadis

# Ekraani seaded
screenX = 640  # Ekraani laius pikslites
screenY = 480  # Ekraani kõrgus pikslites
screen = pygame.display.set_mode([screenX, screenY])  # Luuakse ekraani pindala antud mõõtmetega
pygame.display.set_caption("Ringid")  # Seadistatakse akna tiitel
clock = pygame.time.Clock()  # Luuakse kell objekti, et hallata kaadrisagedust

# Ringide hoidmiseks
rings = []  # List, kuhu salvestatakse ringide andmed
initial_radius = 10  # Algne ringi raadius
radius_increment = 10  # Raadiuse kasv iga klõpsuga
max_rings = 10  # Maksimaalne lubatud ringide arv ekraanil korraga

gameover = False  # Mängu oleku muutuja, mis näitab, kas mäng on lõppenud
while not gameover:  # Peamine mängu tsükkel, mis kestab kuni gameover on False
    clock.tick(30)  # Seadistatakse mängu tsüklite sagedus 30 kaadrit sekundis
    
    for event in pygame.event.get():  # Läbitakse kõik sündmused, mis on toimunud
        if event.type == pygame.QUIT:  # Kui sündmus on akna sulgemine
            gameover = True  # Määratakse gameover True-ks, et lõpetada mängutsükkel
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Kui sündmus on hiireklõps
            mouse_pos = pygame.mouse.get_pos()  # Saadakse hiirekursor asukoht ekraanil
            color = get_random_color()  # Genereeritakse juhuslik värv
            if len(rings) >= max_rings:
                rings.pop(0)  # Eemaldatakse vanim ring, kui ringide arv ületab maksimumi
            new_radius = initial_radius + len(rings) * radius_increment  # Arvutatakse uue ringi raadius
            rings.append({'pos': mouse_pos, 'color': color, 'radius': new_radius})  # Lisatakse uus ring listi
    
    screen.fill((255, 255, 255))  # Ekraani täitmine valge värviga
    
    for ring in rings:  # Läbitakse kõik ringid listis
        pygame.draw.circle(screen, ring['color'], ring['pos'], ring['radius'])  # Joonistatakse ring ekraanile
    
    pygame.display.flip()  # Uuendatakse ekraani, et näidata kõiki joonistatud objekte

pygame.quit()  # Lõpetatakse pygame moodulite töö ja suletakse mäng

