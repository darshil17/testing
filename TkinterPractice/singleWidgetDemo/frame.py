from tkinter import *
root = Tk()

root.geometry("350x250")
root.title("Frame EXample")

f = Frame(root, bg="blue",height=200, width=150)
f.pack()
b = Button(f,text="Click")
b.pack()

f2 = Frame(f,bg="black",height=50,width=75)
f2.pack()
b2 = Button(f2,text="Click Here")
b2.pack()

root.mainloop()
