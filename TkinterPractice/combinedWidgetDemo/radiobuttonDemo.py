from tkinter import *
def radio_changed():
    i=radio.get()
    if(i==1):
        txt_var.set("BCA")
    else if(i==2):
        txt_var.set("MCA")
    else if(i==3):
        txt_var.set(r3.cget("text"))

root = Tk()
root.geometry("500x300")
root.title("Radiobutton Demo")

txt_var=StringVar()
radio=IntVar()

r1 = Radiobutton(root, text="BCA",variable=radio,value=1,command=radio_changed)
r1.pack()
r2 = Radiobutton(root, text="MSCIT",variable=radio,value=2,command=radio_changed)
r2.pack()
r3 = Radiobutton(root, text="MBA",variable=radio,value=3,command=radio_changed)
r3.pack()

l=Label(root,textvariable=txt_var).pack()

root.mainloop()
