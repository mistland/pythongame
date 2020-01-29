import pygame
import random
pygame.init()

#随机生成颜色函数
def rancolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

#设置窗口
windowsize = [400,300]
screen = pygame.display.set_mode(windowsize)
clock = pygame.time.Clock()

black = pygame.color.Color('#000000')
colour = rancolor()

count = 0
click = False
limit = 30
pos = (0,0)

#创建一个游戏循环，并在屏幕上产生爆炸效果
done = False
while not done:
    screen.fill(black)

    if click and count < limit:
        pygame.draw.circle(screen, colour, pos, count)
        count += 1
        if count >= limit:
            click = False

    #获取鼠标点击位置，同时允许窗口关闭
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            click = True
            count = 0
            colour = rancolor()
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
            
