import math
import pygame
pygame.init()

pygame.mixer.music.load("music.mp3")#载入并播放音乐
pygame.mixer.music.play()

count = 0
while pygame.mixer.music.get_busy():
    volume = abs(math.sin(count))#sin函数用于设置阴凉的波形，abs()函数确保波形值是正数
    pygame.mixer.music.set_volume(volume)#音乐的音量可以用pygame.mixer.music.set_volume()设置，0·1，1为最大
    count += 0.2
    pygame.time.delay(200)
