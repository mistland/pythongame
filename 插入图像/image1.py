import pygame
pygame.init()

windowsize = [400,300]
screen = pygame.display.set_mode(windowsize)

image = pygame.image.load('meizi.ico')
screen.blit(image, (windowsize[0] / 2, windowsize[1] / 2))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
pygame.quit()
