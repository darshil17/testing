from tkinter import *

root = Tk()
root.geometry("350x250")
root.title("Scrollbar Example")
sb = Scrollbar(root,orient=VERTICAL)
sb.pack(side=RIGHT, fill=BOTH)

root.mainloop()