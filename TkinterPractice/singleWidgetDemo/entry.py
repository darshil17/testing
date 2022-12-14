from tkinter import *

root = Tk()
root.geometry("350x250")
root.title("Entry Widget EXample")
i = StringVar()
ii=StringVar()
def click():
    l = Label(root, text=i.get()+" "+ii.get(),font=("calibre",10,"bold"))
    l.grid(row=3,column=2)
    i.set("")
    ii.set("")
    """ e.delete(0,END)
    e1.delete(0,END) """
    


fn = Label(root, text="First Name:", font=("calibre",10,"bold"))
fn.grid(row=0,column=1)
e = Entry(root, width=30, textvariable=i, font=("calibre",10,"bold"))
e.grid(row=0,column=2)
ln = Label(root, text="Last Name:", font=("calibre",10,"bold"))
ln.grid(row=1,column=1)
e1 = Entry(root,width=30, textvariable=ii,font=("calibre",10,"bold"))
e1.grid(row=1,column=2)
b = Button(root,text="click", command=click)
b.grid(row=2,column=2)

root.mainloop()