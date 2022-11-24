from tkinter import *
from tkinter import messagebox
def c_checked():
    l.pack()
def bclick():
    messagebox.showinfo("showinfo","button clicked")
    l.pack()
root=Tk()
root.geometry("500x300")
root.title("First")
b=Button(text="Click me!",relief="groove",command=bclick).pack()
l=Label(text="Hello")
#c=Canvas(bg="grey",height="200",width="200").pack()
c=Checkbutton(text="male",command=c_checked)
c.select()
c.pack()
root.mainloop()