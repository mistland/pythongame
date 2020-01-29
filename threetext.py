import Tkinter as tk
window = tk.Tk()
def changestring():
    stringcopy = entry.get()
    stringcopy = stringcopy[::-1]
    entry.delete(0,tk.END)
    entry.insert(0,stringcopy)
entry = tk.Entry(window)
button = tk.Button(window,text="change",command=changestring)
entry.pack()
button.pack()
window.mainloop()

    
