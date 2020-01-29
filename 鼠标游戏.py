import random
import pygame
pygame.init()

windowsize = [400,300]
screen = pygame.display.set_mode(windowsize)
clock = pygame.time.Clock()

black = pygame.color.Color('#000000')
white = pygame.color.Color('#ffffff')
btncolour = pygame.color.Color('#a45c8f')

btnwidth = 50
btnlength = 20
btnx = (windowsize[0] - btnwidth) / 2
btny = (windowsize[1] - btnlength) / 2
toggled = False
pos = (0,0)

points = 0

done = False
while not done:
     if toggled:
          screen.fill(black)
     else:
         screen.fill(white)
     pygame.draw.rect(screen, btncolour, [btnx, btny, btnwidth, btnlength])
     if btnx <= pos[0] <= btnx + btnwidth and btny <= pos[1] <= btny + btnlength:
        toggled = not toggled
        pos = [0,0]
        points += 3
        btnx += random.randint(-1 - points, 1 + points)
        btny += random.randint(-1 - points, 1 + points)
          
     for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            done = True
     pygame.display.flip()
     clock.tick(10)
pygame.quit()
print points

