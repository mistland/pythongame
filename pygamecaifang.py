import pygame
pygame.init()

width =400
height = 300
windowsize = [width,height]
screen = pygame.display.set_mode(windowsize)

colour = pygame.color.Color('#646400')
row = 0
done = False
while not done:
    increment = 255/100
    while row <= height:
        pygame.draw.rect(screen, colour, (0,row,width,row + increment ))
        pygame.display.flip()
        if colour[2] + increment < 255:
            colour[2] += increment
        row += increment
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()
'''colour[0]ºìÉ«colour[1]ÂÌÉ«[2]À¶É«'''
