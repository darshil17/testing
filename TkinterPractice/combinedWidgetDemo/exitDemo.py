from tkinter import *
from tkinter import messagebox
def btnhello_click():
    messagebox.showinfo("info","Welcome to Tkinter!")

root=Tk()

root.title("exitDemo")
root.geometry("250x250")

btnhello=Button(text="Hello!",command=btnhello_click).pack()
btnquit=Button(text="Quit",command=root.destroy).pack()

root.mainloop()
