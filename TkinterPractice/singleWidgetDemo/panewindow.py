from tkinter import *

root =Tk()
root.geometry("350x250")
root.title("PanedWindow Example")
pw = PanedWindow(orient=VERTICAL)
pw.pack(expand=True, fill=BOTH)

chk = Checkbutton(pw, text="Click")
chk.pack()

btn = Button(pw, text="Click Me")
btn.pack()
pw.add(btn)
pw.add(chk)
root.mainloop()