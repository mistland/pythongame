import pygame
pygame.init()
clock = pygame.time.Clock()

crash = pygame.mixer.Sound('asd.mp3')
hit = pygame.mixer.Sound('xinnian.mp3')

count = 0
while count < 200:
    if count % 4 == 0:
        crash.play(1)
    else:
        hit.play(1)
    count += 1
    clock.tick(2)
