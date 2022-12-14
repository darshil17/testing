from tkinter import *

root = Tk()
root.geometry("350x250")
root.title("Radiobutton Example")
radio = IntVar()
def selection():
    """ selection = "you have selected " + str(radio.get())
    label = Label.config(text=selection) """
    a1 = radio.get()
    if(a1 == 1):
        l = Label(root,text="BCA")
        l.pack()
    elif(a1==2):
        l = Label(root,text=r1.cget("text"))
        l.pack()
    elif(a1==3):
        l = Label(root,text=r2.cget("text"))
        l.pack()


r = Radiobutton(root, text="BCA", variable=radio,value=1, command=selection)
r.pack()
r1 = Radiobutton(root, text="MSCIT", variable=radio,value=2,command=selection)
r1.pack()
r2 = Radiobutton(root, text="MBA", variable=radio, value=3,command=selection)
r2.pack()

# label = Label(root)

root.mainloop()
