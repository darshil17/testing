from tkinter import *

root = Tk()

root.geometry("350x250")
root.title("Menubutton Example")

mb = Menubutton(root, text="Courses")
mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu



mb.menu.add_checkbutton(label="BCA")
mb.menu.add_checkbutton(label="MSCIT")
mb.menu.add_checkbutton(label="MBA") 

# mb.menu.add_command(label="BCA" )
# mb.menu.add_command(label="MSCIT")
# mb.menu.add_command(label="MBA")

mb.pack()


root.mainloop()
