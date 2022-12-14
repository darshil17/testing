from tkinter import *
root = Tk()
root.geometry("500x300")
root.title("Canvas Example")

C = Canvas(root,height=300,width=250,bg="yellow",bd="2",borderwidth="5")

line = C.create_line(50,220,230,110,fill="blue")
arc = C.create_arc(110,240,180,125,start=0,extent=30,fill="red")
oval = C.create_oval(20,80,200,150,fill="green")


C.pack()
root.mainloop()