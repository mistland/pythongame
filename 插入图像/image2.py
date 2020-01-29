import pygame
pygame.init()

windowsize = [800,700]
screen = pygame.display.set_mode(windowsize)

bilibili = pygame.image.load('bilibili.jpg')
tv = pygame.image.load('tv.jpg')
x = 0
y = 0
screen.blit(bilibili, (x + 10, y + 50))
screen.blit(tv, (x + 7, y))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
pygame.quit()
