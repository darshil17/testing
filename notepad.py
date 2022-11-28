from tkinter import *
from tkinter import messagebox

def open(event=None):
    messagebox.showinfo("info","Opening files")

root=Tk()
root.geometry("500x300")
root.title("Notepad")
root.bind("<Control-o>",open)
menubar=Menu()
root.config(menu=menubar)

file=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file)
file.add_command(label="New File..")
file.add_command(label="Open",command=open)
file.add_command(label="Save")
file.add_command(label="Save As")
file.add_command(label="Exit",command=root.quit)

edit=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=edit)
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")

help=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=help)
help.add_command(label="About")



root.mainloop()