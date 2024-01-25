import time
import pygame

pygame.init()
scr = pygame.display.set_mode((600, 300))
pygame.display.set_caption('RU tik-tok')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

runn = True
while runn:

    scr.fill((235, 21, 208))

    pygame.display.update()
    print('+')
 #   time.sleep(0.5)
  #  scr.fill((255,255,255))
   # pygame.display.update()
    #time.sleep(0.5)
    #scr.fill((0,0,0))

    for event in pygame.event.get():
 #       scr.fill((255,255,255))
        pygame.display.update()
#        print('update')
   #     scr.fill((0,0,0))
        if event.type == pygame.QUIT:
            runn = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                scr.fill((33, 21, 235))
                print('f1')
    
