from tkinter import *
from tkinter import messagebox
def btnClick_Click():
    
    messagebox.showinfo("Info.",pswdentry_var.get())

root=Tk()

root.title("PasswordDemo")
root.geometry("250x250")


frame=Frame()

pswdentry_var=StringVar()
txt_pswdentry=Entry(frame, show="*",textvariable=pswdentry_var).pack()
btnClick=Button(frame,text="Submit",command=btnClick_Click).pack(side=RIGHT)

frame.pack()

root.mainloop()
