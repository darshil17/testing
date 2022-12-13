from tkinter import *
from tkinter import messagebox
def btnClick_Click():
    messagebox.showinfo("Info.","Your name is:"+txtid_txt.get())

root=Tk()

root.title("formDemo")
root.geometry("250x250")

txtid_txt=StringVar()

lblframe=LabelFrame(text="form")
lbltxtid=Label(lblframe,text="Enter Your name:").pack(side=TOP)
txtid=Entry(lblframe,textvariable=txtid_txt).pack(side=LEFT)
btnClick=Button(lblframe,text="Enter",command=btnClick_Click).pack(side=RIGHT)

lblframe.pack()
root.mainloop()
