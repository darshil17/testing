from tkinter import *
from tkinter import messagebox
def c_checked():
    l.pack()
def bclick():
    messagebox.showinfo("showinfo",e_text.get())
    l.pack()
root=Tk()
e_text=StringVar()
root.geometry("500x300")
root.title("First")
b=Button(text="Click me!",relief="groove",command=bclick).pack()
l=Label(text="Hello",textvariable=e_text)
#c=Canvas(bg="grey",height="200",width="200").pack()
c=Checkbutton(text="male",command=c_checked)
c.select()
c.pack()
e=Entry(textvariable=e_text).pack()
f=Frame(root,bg="yellow",height="300",width="300")
li=Listbox(f)
liitem=["darshil","manoj","jayanti"]
for i in liitem:
    li.insert(END,i)
li.pack()
f.pack()
msg=Message(text="Welcome").pack()
root.mainloop()
