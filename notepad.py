from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,asksaveasfile
import os
def openfile(event=None):
    global files
    files=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])
    if files=="":
        files=None
    else:
        root.title(os.path.basename(files)+" - Notepad")
        textarea.delete(1.0,END)
        f=open(files,"r")
        textarea.insert(1.0,f.read())
        f.close()
def newfile():
    global files 
    root.title("Untitled - Notepad")
    files=None
    textarea.delete(1.0,END)

def savefile():
    global files
    if files == None:
        files=asksaveasfile(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])
        if files=="":
            files=None
        else:
            f=open(files,"w")
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(files)+" - Notepad")
    else:
        f=open(files,"w")
        f.write(textarea.get(1.0,END))
        f.close()
def quitapp():
    quit()
def cut():
    textarea.event_generate("<<Cut>>")
def copy():
    textarea.event_generate("<<Copy>>")
def paste():
   textarea.event_generate("<<Paste>>")       
def about():
    messagebox.showinfo("Notepad","Notepad by darshil solanki")
              
root=Tk()
root.geometry("500x300")
root.title("Notepad")
root.bind("<Control-o>",openfile)

menubar=Menu()
root.config(menu=menubar)

file=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file)
file.add_command(label="New File..",command=newfile)
file.add_command(label="Open",command=openfile)
file.add_command(label="Save",command=savefile)
file.add_command(label="Exit",command=quitapp)

edit=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=edit)
edit.add_command(label="Cut",command=cut)
edit.add_command(label="Copy",command=copy)
edit.add_command(label="Paste",command=paste)

help=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=help)
help.add_command(label="About",command=about)


scroll=Scrollbar(root,orient=VERTICAL)
scroll.pack(side=RIGHT,fill=Y)
textarea=Text(root,font="Constantia",yscrollcommand=scroll.set)
scroll.config(command=textarea.yview)
textarea.pack(expand=True,fill=BOTH)
files=None

root.mainloop()