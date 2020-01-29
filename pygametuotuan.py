import math
import pygame
pygame.init()

windowsize = [400,300]
screen = pygame.display.set_mode(windowsize)
clock = pygame.time.Clock()

width = 200
height = 200
x = windowsize[0] / 2 - width / 2
y = windowsize[1] / 2 - height / 2
colour = pygame.color.Color('#57b0f6')
black = pygame.color.Color('#000000')

count = 0
fileno = 0
done = False
while not done:
    screen.fill(black)
    pygame.draw.ellipse(screen, colour, [x,y,width,height])
    width += math.cos(count) * 10
    x -= (math.cos(count) * 10) / 2
    height += math.sin(count) * 10
    y -= (math.sin(count) * 10) / 2
    count += 0.5

    pygame.display.flip()

    if fileno < 5:
       pygame.image.save(screen,"circle" + str(fileno) + ".png")
       fileno += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    clock.tick(24)
pygame.quit()
'''两个函数可以使用它们的参数生成波形，随值的增加，返回的值组成一个平缓的波形，x,y的位置也会调整补偿宽度高度的改变'''
