import pygame
pygame.init()

pygame.mixer.music.load('xinnian.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.wait(200)
