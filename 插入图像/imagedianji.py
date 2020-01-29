import pygame
pygame.init()

windowsize = [400,300]
screen = pygame.display.set_mode(windowsize)
clock = pygame.time.Clock()

image = pygame.image.load('meizi.ico')
bg = pygame.image.load('bg.jpg')

pos = (0,0)
screen.blit(bg, (0,0))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            screen.blit(bg,(0,0))
            screen.blit(image,pos)
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
    clock.tick(10)
pygame.quit()
