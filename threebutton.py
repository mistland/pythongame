import Tkinter as tk
"""引用Tkinter并重命名为tk"""
window = tk.Tk()
cliked = 0
def buttonclick():
    global cliked
    cliked = cliked + 1
    button.config(text=str(cliked))
button = tk.Button(window,text="bilibili",command=buttonclick)
button.pack()
window.mainloop()

    
