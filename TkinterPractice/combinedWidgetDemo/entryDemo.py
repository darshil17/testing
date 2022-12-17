from tkinter import *
def btnsubmit_click():
    if(fname_var.get()!="" and lname_var.get()!="" and nname_var.get()!=""):
        l=Label(text="Your name is:" +fname_var.get()+" "+lname_var.get()).place(x=30,y=120)
        l1=Label(text="Your Nick name is:" + nname_var.get()).place(x=30,y=140)

root=Tk()

root.title("EntryInputDemo")
root.geometry("250x250")


fname_var=StringVar()
lname_var=StringVar()
nname_var=StringVar()

lbl_fname=Label(text="First Name:").grid(row=0,column=0)
txt_fname=Entry(textvariable=fname_var).grid(row=0,column=1)

lbl_lname=Label(text="Last Name:").grid(row=1,column=0)
txt_lname=Entry(textvariable=lname_var).grid(row=1,column=1)

lbl_nname=Label(text="Nick Name:").grid(row=2,column=0)
txt_nname=Entry(textvariable=nname_var).grid(row=2,column=1)

btnsubmit=Button(text="Submit",command=btnsubmit_click).place(x=50,y=90)

root.mainloop()
