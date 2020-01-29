import random
import pygame
pygame.init()

windowsize = [400,300]
screen = pygame.display.set_mode(windowsize)
clock = pygame.time.Clock()

image = pygame.image.load('meizi.ico')
bg = pygame.image.load('bg.jpg')

screen.blit(bg, (0,0))

done = False
while not done:
    x= random.randint(0, windowsize[0])
    y= random.randint(0, windowsize[1])
    angle = random.randint(0,360)
    rotatedimage = pygame.transform.rotate(image, angle)#Ðý×ªÍ¼Ïñ
    screen.blit(rotatedimage, (x,y))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
    clock.tick(10)
pygame.quit()
