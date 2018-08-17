import time
from threading import Thread

import pygame

pygame.init()

prozor = pygame.display.set_mode((500, 500))
pozadina = pygame.image.load("background.png")
pygame.display.set_caption("Igrica he he")
isJump = False
jumpCount = 8
##pozadina je 980px
class Igrac():
    x = 50
    y = 420
    velicina = 20
    boja = (255, 0, 0)
    brzina = 1
    hitbox = pygame.Rect(x, y, 20, 20)

class Prepreka():
    x = 520
    y = 420
    velicina = 20
    boja = (0, 0, 255)
    brzina = 1
    hitbox = pygame.Rect(x, y, 20, 20)

    def __init__(self):
        Thread(target=pomerajPrepreku, args=(self, ), daemon=True).start()

def pomerajPrepreku(p):
    while run:
        time.sleep(0.003)
        if p.x < -20:
            p.x = 520
        p.x -= p.brzina

def skoci():
    global isJump
    global jumpCount

    global t1
    brojac = 18
    while brojac >= 0:
        time.sleep(0.03)
        if not isJump:
            isJump = True
        else:
            if jumpCount >= -8:
                neg = 1
                if jumpCount < 0:
                    neg = -1
                igrac.y -= (jumpCount ** 2) * 0.5 * neg
                jumpCount -= 1
            else:
                isJump = False
                jumpCount = 8
        brojac -= 1
    t1 = Thread(target=skoci, args=())
run = True
igrac = Igrac()
prepreka = Prepreka()
t1 = Thread(target=skoci, args=())
pozadinaCounter = 0
while run:
    pygame.time.delay(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not t1.isAlive():
        t1.start()
    if igrac.hitbox.colliderect(prepreka.hitbox):
        run = False
    prozor.fill((255, 255, 255))
    prepreka.hitbox = pygame.Rect(prepreka.x+prepreka.velicina, prepreka.y, 20, 20)
    igrac.hitbox = pygame.Rect(igrac.x+prepreka.velicina, igrac.y, 20, 20)
    prozor.blit(pozadina, (pozadinaCounter, 0))
    pozadinaCounter -= 1
    if pozadinaCounter < -981:
        pozadinaCounter = 0
    pygame.draw.rect(prozor, igrac.boja, (igrac.x, igrac.y, igrac.velicina, igrac.velicina))
    pygame.draw.rect(prozor, prepreka.boja, (prepreka.x, prepreka.y, prepreka.velicina, prepreka.velicina))
    pygame.display.flip()