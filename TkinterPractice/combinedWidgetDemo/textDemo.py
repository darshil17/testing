from tkinter import *
from tkinter import scrolledtext


root=Tk()

root.title("Demo")
root.geometry("250x250")


pw = PanedWindow(orient=VERTICAL)
pw.pack(expand=True, fill=BOTH)

stext = scrolledtext.ScrolledText(master=pw,bg='white', height=10)
stext.insert(END,"This is ScrolledText")
stext.pack()

txt=Text(pw,height=30)
scb=Scrollbar(txt).pack(side=RIGHT,fil=Y)
stext.insert(END,"This is Text and scrollbar")
txt.pack()

pw.add(txt)
pw.add(stext)

root.mainloop()
