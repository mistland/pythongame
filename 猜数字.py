# -*- coding:utf-8 -*-
import random
import Tkinter as tk
window = tk.Tk()

maxno = 10
score = 0
rounds = 0

def buttoncilck():
    global score
    global rounds
    try:
        guess = int (guessbox.get())
        if 0 < guess <= maxno:
            result = random.randrange(1,maxno + 1)
            if guess == result:
                score = score + 1
            rounds = rounds + 1
        else:
            result = "输入错误"
    except:
        result = "输入错误"
    resultlabel.config(text=result)
    scorelabel.config(text=str(score) + "/" + str(rounds))
    guessbox.delete(0,tk.END)

guesslabel = tk.Label(window, text="enter a number from 1 to" + str(maxno))
guessbox = tk.Entry(window)
resultlabel = tk.Label(window)
scorelabel = tk.Label(window)
button = tk.Button(window, text="guess",command=buttoncilck)

guesslabel.pack()
guessbox.pack()
resultlabel.pack()
scorelabel.pack()
button.pack()

window.mainloop()
'''try...except声明语句将运行try里面的代码，如果出现错误停止try执行except'''
