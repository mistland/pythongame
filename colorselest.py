import Tkinter as tk
window = tk.Tk()

def sliderupdate(s):
    red = redslider.get()
    green = greenslider.get()
    blue = blueslider.get()
    colour = "#%02x%02x%02x" % (red, green, blue)
    canvas.config(bg=colour)
    text.delete(0,tk.END)
    text.insert(0,colour)

redslider = tk.Scale(window, from_=0, to=255, command=sliderupdate)
greenslider = tk.Scale(window, from_=0, to=255, command=sliderupdate)
blueslider = tk.Scale(window, from_=0, to=255, command=sliderupdate)
canvas = tk.Canvas(window, width=200, height=200)
text = tk.Entry(window)

redslider.grid(row=1, column=1)
greenslider.grid(row=1, column=2)
blueslider.grid(row=1, column=3)
canvas.grid(row=2, column=1, columnspan=3)
text.grid(row=3,column=1,columnspan=3)
tk.mainloop()
