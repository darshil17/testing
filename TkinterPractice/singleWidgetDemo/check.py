from tkinter import *
root = Tk()

root.geometry("500x300")
root.title("Checkbutton Example")
c = Checkbutton(root, text="BCA",onvalue="1",offvalue="0")
c.pack()
c.select()
c1 = Checkbutton(root, text="MSCIT",onvalue="1",offvalue="0")
c1.pack()
c2 = Checkbutton(root, text="MBA",onvalue="1",offvalue="0")
c2.pack()
c2.select()

root.mainloop()
