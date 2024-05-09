import pygame #laeme pygame teegi
pygame.init() #pygame käivitamine

screen=pygame.display.set_mode([640,480],pygame.RESIZABLE) #tekitame akna 640x480, mis on suuruse muutmise võimalusega
pygame.display.set_caption("My Screen") #kuvame erkaani nime

screen.fill([204, 255, 255]) #muudame taustavärvi


#joonistamine
pygame.draw.line(screen, [255,0,0], [100,100], [200,200], 2) #joonistame punase joone koordinaatidest [100,100] kuni [200,200] paksusega 2
pygame.draw.rect(screen, [0, 225, 0], [50, 80, 200, 300], 2) #joonistame rohelise ristküliku, mille ülemine vasak nurk on [50, 80], laius 200 ja kõrgus 300, joone paksus 2
pygame.draw.circle(screen, [0, 0, 255], [150,200], 100, 1) #joonistame sinise ringi, mille keskpunkt on [150,200], raadius 100 ja joone paksus 1
pygame.draw.polygon(screen, [255, 0, 255], [[50,50],[100,50],[100,150],[250,50],[350,250],[50,250]], 2) #joonistame lilla täisnurga mitmest tipust koosneva kujundi, joone paksus 2
pygame.draw.ellipse(screen, [0, 225, 0], [50, 80, 200, 300], 2) #joonistame rohelise ellipsi, mis mahutatakse ristkülikusse [50, 80, 200, 300], joone paksus 2
pygame.draw.arc(screen,[0,0,0], [100,100,250,200], 0, 3.14*1.5, 1) #joonistame kaare, mis on must, määratletud ristkülikuga [100,100,250,200], algusnurk 0, lõppnurk 3.14*1.5 radiaani, joone paksus 1

pygame.display.flip() #värskendame ekraani

while True: #algatame lõpmatu tsükli, et aken püsiks avatud
    for event in pygame.event.get(): #kontrollime sündmuseid
        if event.type == pygame.QUIT: #kui sündmuse tüüp on QUIT
            pygame.quit() #lõpetame pygame
       



