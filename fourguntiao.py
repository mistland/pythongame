import Tkinter as tk
window = tk.Tk()

colour = "#ddFFFF"
'''sider = tk.Scale(window,from_=0,to=100)
sider.pack()'''
canvas = tk.Canvas(window,height=300,width=300,bg=colour)
canvas.pack()
window.mainloop()
