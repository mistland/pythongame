import math
import pygame
pygame.init()

pygame.mixer.music.load("music.mp3")#���벢��������
pygame.mixer.music.play()

count = 0
while pygame.mixer.music.get_busy():
    volume = abs(math.sin(count))#sin�����������������Ĳ��Σ�abs()����ȷ������ֵ������
    pygame.mixer.music.set_volume(volume)#���ֵ�����������pygame.mixer.music.set_volume()���ã�0��1��1Ϊ���
    count += 0.2
    pygame.time.delay(200)
