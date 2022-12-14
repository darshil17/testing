from tkinter import *
root = Tk()
root.geometry("350x250")
root.title("Scale Example")
v1 = DoubleVar()

def show():
    l = Label(root, text=v1.get())
    l.pack()
sc = Scale(root, from_=10, to=500, variable=v1, orient=HORIZONTAL)
sc.pack()

b = Button(root, text="show scale", command=show)
b.pack(side=RIGHT, fill=BOTH)
root.mainloop()