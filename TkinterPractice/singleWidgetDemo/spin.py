from tkinter import *

root = Tk()
root.geometry("350x250")
root.title("Spinbox Example")
s = Spinbox(root, from_=1, to=100)
s.pack()
root.mainloop()