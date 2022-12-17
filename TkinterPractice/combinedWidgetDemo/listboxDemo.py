from tkinter import *
root = Tk()

root.geometry("500x300")
root.title("Listbox Demo")

li=['DR','MR','MRS','Miss','Mx','Sir']
lb=Listbox()
for i in li:
    lb.insert(END,i)
lb.pack()

root.mainloop()
