import time
from threading import Thread

import pygame

pygame.init()

pauzaFlag = False
kasnjenjeKonst = 0.001
prozor = pygame.display.set_mode((1000, 500))
pozadina = pygame.image.load("background.png")
pauza = pygame.image.load("pauza.png")
pygame.display.set_caption("Jumping car")
isJump = False
jumpCount = 9
delay = kasnjenjeKonst
pozadinaCounter = 0
poeni = 0
class Igrac():
    x = 50
    y = 370
    velicinaX = 170
    velicinaY = 70
    boja = (255, 0, 0)
    brzina = 1
    hitbox = pygame.Rect(x, y, velicinaX, velicinaY)
    slika = pygame.image.load("auto.png")

class Prepreka():
    x = 1050
    y = 390
    velicina = 50
    boja = (0, 0, 255)
    brzina = 3
    hitbox = pygame.Rect(x, y, velicina, velicina)
    slika = pygame.image.load('kutija.jpg')

    def __init__(self):
        Thread(target=pomerajPrepreku, args=(self, )).start()

def uvecavajBrzinu():
    global delay
    global pauzaFlag
    while run:
        if not pauzaFlag:
            time.sleep(1)
            delay *= 0.95

def tredPoeni():
    global poeni
    global pauzaFlag
    while run:
        if not pauzaFlag:
            time.sleep(delay)
            poeni += 1

def pomerajPrepreku(p):
    global delay
    global pozadinaCounter
    while run:
        if not pauzaFlag:
            time.sleep(delay)
            if p.x < -50:
                p.x = 1050
            p.x -= p.brzina
            pozadinaCounter -= prepreka.brzina
            if pozadinaCounter < -980:
                pozadinaCounter = 0

def skoci():
    global isJump
    global jumpCount
    global t1
    brojac = 20
    while brojac >= 0:
        time.sleep(0.03)
        if not isJump:
            isJump = True
        else:
            if jumpCount >= -9:
                neg = 1
                if jumpCount < 0:
                    neg = -1
                igrac.y -= (jumpCount ** 2) * 0.5 * neg
                jumpCount -= 1
            else:
                isJump = False
                jumpCount = 9
        brojac -= 1
    t1 = Thread(target=skoci, args=())

def osveziEkran():
    global delay
    global pozadinaCounter
    global poeni
    prozor.fill((255, 255, 255))
    prepreka.hitbox = pygame.Rect(prepreka.x, prepreka.y, prepreka.velicina, prepreka.velicina)
    igrac.hitbox = pygame.Rect(igrac.x, igrac.y, igrac.velicinaX, igrac.velicinaY)
    #pygame.draw.rect(prozor, (0, 0, 0), pygame.Rect(50, 50, 50, 50), 5)
    prozor.blit(pozadina, (pozadinaCounter, 0))
    prozor.blit(pauza, (950, 0))
    poeniPrint(prozor, ('Poeni: ' + str(poeni)))
    prozor.blit(igrac.slika, (igrac.x, igrac.y))
    prozor.blit(prepreka.slika, (prepreka.x, prepreka.y))
    pygame.display.flip()

def poeniPrint(screen, text, x = 5, y = 5, size = 15, color = (0, 0, 0)):
    text = str(text)
    font = pygame.font.SysFont('Comic Sans MS', size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))

def gameOver():
    global delay
    global run
    global poeni
    gameOver = pygame.image.load('gameOver.png')
    prozor.fill((0, 0, 0))
    playAgainRect = pygame.Rect(150, 300, 75, 75)
    quitRect = pygame.Rect(275, 300, 75, 75)
    prozor.blit(gameOver, (100, 166))
    prozor.blit(pygame.image.load('playAgain.png'), (150, 300))
    prozor.blit(pygame.image.load('quit.png'), (275, 300))
    pygame.display.flip()
    cekaj = True
    while cekaj:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos
                if playAgainRect.collidepoint(x, y):
                    cekaj = False
                    delay = kasnjenjeKonst
                    poeni = 0
                    main()
                elif quitRect.collidepoint(x, y):
                    run = False
                    cekaj = False
                    pygame.quit()
                    quit()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()


run = True
igrac = Igrac()
prepreka = Prepreka()
t1 = Thread(target=skoci, args=())
brzinaTred = Thread(target=uvecavajBrzinu, args=()).start()
poeniTred = Thread(target=tredPoeni, args=()).start()

def main():
    global run
    global delay
    global pauzaFlag
    osveziEkran()
    while run:
        pygame.time.delay(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if pygame.Rect(950, 0, 50, 50).collidepoint(x, y):
                    pauzaFlag = True
                    while pauzaFlag:
                        for r in pygame.event.get():
                            if r.type == pygame.MOUSEBUTTONDOWN:
                                pauzaFlag = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not t1.isAlive():
            t1.start()
        if igrac.hitbox.colliderect(prepreka.hitbox):
            gameOver()
        osveziEkran()

main()
