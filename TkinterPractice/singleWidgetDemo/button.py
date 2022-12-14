from tkinter import *
root  = Tk()

root.geometry("500x300")
root.title("Button Example")

def my_click():
    l = Label(root,text="Button Clicked").pack()

b = Button(root,text="click",command=my_click,fg="#eb4034").pack()

root.mainloop()
