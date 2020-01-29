import pygame
pygame.init()

windowsize = [400,300]
screen = pygame.display.set_mode(windowsize)
colour = pygame.color.Color('#0a32f4')

done = False
while not done:
    pygame.draw.rect(screen,colour,[10,20,30,40])
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.quit:
            done = True
pygame.quit()
'''[10,20,30,40]长方形一个角（10，20），宽30高40'''
