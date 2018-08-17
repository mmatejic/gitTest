import time
from threading import Thread

import pygame

pygame.init()

prozor = pygame.display.set_mode((1000, 500))
pozadina = pygame.image.load("background.png")
pygame.display.set_caption("Igrica he he")
isJump = False
jumpCount = 9
delay = 0.002
pozadinaCounter = 0
class Igrac():
    x = 50
    y = 420
    velicina = 20
    boja = (255, 0, 0)
    brzina = 1
    hitbox = pygame.Rect(x, y, velicina, velicina)

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
    while run:
        time.sleep(1)
        delay *= 0.95

def pomerajPrepreku(p):
    global delay
    global pozadinaCounter
    while run:
        time.sleep(delay)
        if p.x < -50:
            p.x = 1050
        p.x -= p.brzina
        pozadinaCounter -= 3
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
    prozor.fill((255, 255, 255))
    prepreka.hitbox = pygame.Rect(prepreka.x + prepreka.velicina, prepreka.y, prepreka.velicina, prepreka.velicina)
    igrac.hitbox = pygame.Rect(igrac.x + prepreka.velicina, igrac.y, 20, 20)
    prozor.blit(pozadina, (pozadinaCounter, 0))
    text_to_screen(prozor, ('Brzina: ' + str("%.5f" % delay)))
    pygame.draw.rect(prozor, igrac.boja, (igrac.x, igrac.y, igrac.velicina, igrac.velicina))
    prozor.blit(prepreka.slika, (prepreka.x, prepreka.y))
    pygame.display.flip()

def text_to_screen(screen, text, x = 50, y = 50, size = 50, color = (200, 000, 000)):
    text = str(text)
    font = pygame.font.SysFont('Comic Sans MS', size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))

def gameOver():
    global delay
    global run
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
                    delay = 0.003
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

def main():
    global run
    global delay
    prepreka.x = 520
    prepreka.y = 390

    osveziEkran()
    while run:
        pygame.time.delay(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not t1.isAlive():
            t1.start()
        if igrac.hitbox.colliderect(prepreka.hitbox):
            gameOver()
        osveziEkran()

main()
