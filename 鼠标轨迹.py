import pygame
pygame.init()

windowsize = [400,300]
screen = pygame.display.set_mode(windowsize)
clock = pygame.time.Clock()

points = []

whilte = pygame.color.Color('#ffffff')
black = pygame.color.Color('#000000')

done = False
while not done:
    screen.fill(black)
    pos = pygame.mouse.get_pos()

    #当窗口打开时，鼠标的位置将在（0，0）处，下面阻止从这个点开始画线，限制了点数量20
    if pos[0] != 0 and pos[1] != 0:
        points.append(pos)
        
    if len(points) >= 20:
         del points[0]

    #至少两个点，画出鼠标轨迹
    if len(points) >= 2:
        pygame.draw.aalines(screen, whilte, False, points)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        pygame.display.flip()
        clock.tick(30)
pygame.quit()
