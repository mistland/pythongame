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

    #�����ڴ�ʱ������λ�ý��ڣ�0��0������������ֹ������㿪ʼ���ߣ������˵�����20
    if pos[0] != 0 and pos[1] != 0:
        points.append(pos)
        
    if len(points) >= 20:
         del points[0]

    #���������㣬�������켣
    if len(points) >= 2:
        pygame.draw.aalines(screen, whilte, False, points)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        pygame.display.flip()
        clock.tick(30)
pygame.quit()
