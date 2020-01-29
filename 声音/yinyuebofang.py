import Tkinter as tk
import pygame
window = tk.Tk()
pygame.init()

pygame.mixer.music.load('music.mp3')#���������ļ�

started = False
playing = False #�����Ƿ��ڲ��ţ������Ƿ�ֹͣ����

def buttonclick():
    global playing
    global started
    if not playing: #����Ƿ�ֹͣ����
        if not started:#����Ƿ�δ��ʼ����
            pygame.mixer.music.play(-1)
            started = True
        else:
            pygame.mixer.music.unpause()#������������
            button.config(text = 'pause')

    else:
        pygame.mixer.music.pause()
        button.config(text = 'play')
        
    playing = not playing

def setvolume(val):
    volume = float(slider.get())
    pygame.mixer.music.set_volume(volume / 100)

slider = tk.Scale(window, from_=100, to=0, command=setvolume)
button = tk.Button(window, text='play', command=buttonclick)

slider.pack()    
slider.set(100)
button.pack()
window.mainloop()
    

        
            
        
