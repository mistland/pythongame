# -*- coding:utf-8 -*-
import Tkinter as tk
import random
window = tk.Tk()
def randomnoun():
    nouns = ["猫","蛋糕","狗","帽子","头","变态"]
    noun = random.choice(nouns)
    return noun
def randomverb():
    verbs = ["喜欢","是","肯定是","拿开","取下","吃掉"]
    verb = random.choice(verbs)
    return verb
def buttonclick():
    name = nameentry.get()
    verb = randomverb()
    noun = randomnoun()
    sentence = name + " " + verb + " " + noun
    result.delete(0,tk.END)
    result.insert(3,sentence)
namelabel = tk.Label(window,text="名字：")
nameentry = tk.Entry(window)
button = tk.Button(window,text="开始构建",command=buttonclick)
result = tk.Entry(window)
namelabel.pack()
nameentry.pack()
button.pack()
result.pack()
window.mainloop()
