import pygame

pygame.init()

prozor = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Igrica he he")

x = 50
y = 400
isJump = False
jumpCount = 10
brzina = 1

run = True

while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    prozor.fill((255, 255, 255))
    pygame.draw.rect(prozor, (255, 0, 0), (x, y, 20, 20))

    pygame.display.update()