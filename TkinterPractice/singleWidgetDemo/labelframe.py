from tkinter import *

root = Tk()

root.geometry("350x250")
root.title("LabelFrame Example")

lf = LabelFrame(root, text="Select Subjects")
lf.pack()

cb1 = Checkbutton(lf, text="Hindi")
cb1.pack()
cb2 = Checkbutton(lf, text="English")
cb2.pack()
cb3 = Checkbutton(lf, text="Maths")
cb3.pack()

root.mainloop()