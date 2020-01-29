# -*- coding:utf-8 -*-
import Tkinter as tk
import time
window = tk.Tk()

clicks = 0
start = 0
goal = 10

def buttonclick():
    global clicks
    global start

    if clicks == 0:
        start = time.time() 
        clicks = clicks + 1
    elif clicks + 1 >= goal:
        score = time.time() - start
        label.config(text="时间：" + str(score))
        clicks = 0
    else:
        clicks = clicks + 1
        slider.set(clicks)
button = tk.Button(window,text="click me",command=buttonclick)
slider = tk.Scale(window,from_=0,to=goal)
label = tk.Label(window)

button.pack()
slider.pack()
label.pack()
window.mainloop()

