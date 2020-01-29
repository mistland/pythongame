import Tkinter as tk
window = tk.Tk()
def checkpassword():
    password = "awsl"
    enteredpassword = passwordentry.get()
    if password == enteredpassword:
        confirmLabel.config(text="correct")
    else:
        confirmLabel.config(text="incorrect")
passwordlabel = tk.Label(window,text="password:")
passwordentry = tk.Entry(window,show="*")
button = tk.Button(window,text="enter",command=checkpassword)
confirmLabel = tk.Label(window)
passwordlabel.pack()
passwordentry.pack()
button.pack()
confirmLabel.pack()
window.mainloop()

    
