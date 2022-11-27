from tkinter import *
from tkinter import messagebox
def c_checked():
    l.pack()
def bclick():
    messagebox.showinfo("showinfo",e_text.get())
    l.pack()
root=Tk()

menubar=Menu()
file=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file)
file.add_command(label="New File..")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save As")
file.add_command(label="Exit",command=root.destroy)

edit=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=edit)
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")

help=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=help)
help.add_command(label="About")

root.config(menu=menubar)

 
menubutton = Menubutton( text = "Language")  
  
menubutton.menu=Menu(menubutton,tearoff=0) 

menubutton["menu"]=menubutton.menu
  
menubutton.menu.add_checkbutton(label = "Hindi", variable=IntVar())  
  
menubutton.menu.add_checkbutton(label = "English", variable = IntVar())  
  
menubutton.pack()  

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
