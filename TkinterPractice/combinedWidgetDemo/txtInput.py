from tkinter import *
def btnsubmit_click():
    l=Label(text="Your name is:" +fname_var.get()+" "+lname_var.get()).place(x=30,y=80)

root=Tk()

root.title("InputDemo")
root.geometry("250x250")


fname_var=StringVar()
lname_var=StringVar()

lbl_fname=Label(text="First Name:").grid(row=0,column=0)
txt_fname=Entry(textvariable=fname_var).grid(row=0,column=1)

lbl_lname=Label(text="Last Name:").grid(row=1,column=0)
txt_lname=Entry(textvariable=lname_var).grid(row=1,column=1)
btnsubmit=Button(text="Submit",command=btnsubmit_click).place(x=50,y=50)

root.mainloop()
