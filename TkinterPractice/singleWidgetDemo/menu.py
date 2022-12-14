from tkinter import *
root = Tk()

root.geometry("350x250")
root.title("menu Example")
menubar = Menu(root)

file = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file)
file.add_command(label="New File")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_separator()
file.add_command(label="Exit", command=root.destroy)

edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
root.config(menu=menubar)
root.mainloop()
