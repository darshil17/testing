from tkinter import *
from tkinter import messagebox

root = Tk()
messagebox.showinfo("Infromation","Quit this applicaation now")
messagebox.showerror("Type Error","Application not supported")
messagebox.showwarning("Warning", "Do you want to Chnage Pwd")
messagebox.askokcancel("Ask ok Cancel", "This is OkCancel Messagebox")
messagebox.askquestion("Question","Are you ready to install application?")
messagebox.askyesno("Yes No", "Reaaly want to quit application")
messagebox.askretrycancel("Retry Cancel","Do you want to copy this file ?")
root.mainloop()