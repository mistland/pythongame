# -*- coding:utf-8 -*-
import pygame
pygame.init()

windowsize = [400,300]
screen = pygame.display.set_mode(windowsize)
'''设置窗口大小'''

pygame.display.set_caption("circles")
"""设置窗口标题"""

colour = pygame.color.Color('#ffffff')
'''定义颜色'''

done = False
while not done:
    pygame.draw.circle(screen,colour,[200,150],50)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()

    
