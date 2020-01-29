import pygame
pygame.init()
pygame.mixer.init()

sound = pygame.mixer.Sound('asd.mp3')
sound.play()
pygame.time.wait(int(sound.get_length()) * 1000)
