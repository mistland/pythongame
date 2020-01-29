import Tkinter as tk
import pygame
window = tk.Tk()
pygame.init()

pygame.mixer.music.load('music.mp3')#载入音乐文件

started = False
playing = False #音乐是否在播放，音乐是否停止播放

def buttonclick():
    global playing
    global started
    if not playing: #检查是否停止播放
        if not started:#检查是否未开始播放
            pygame.mixer.music.play(-1)
            started = True
        else:
            pygame.mixer.music.unpause()#继续播放音乐
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
    

        
            
        
