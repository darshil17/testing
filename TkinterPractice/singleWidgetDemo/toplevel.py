from tkinter import *
root = Tk()
root.geometry("350x250")
root.title("toplevel Example")
def open_toplevel():
    top = Toplevel()
    top.title("Toplevel Window")
    top.geometry("200x250")
    l = Label(top,text="This is toplevel widget")
    l.pack()
    b1 = Button(top,text="Exit",command=top.destroy)
    b1.pack()
    top.mainloop()

b = Button(root,text="Open Toplevel", command=open_toplevel)
b.pack()
root.mainloop()