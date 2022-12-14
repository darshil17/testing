from tkinter import *

root = Tk()
root.geometry("350x250")
root.title("Text Example")
fact = """Hi all My name is 
Darshil Solanki"""
t = Text(root, height=5, width=50)
t.insert(END,fact)
t.pack()


root.mainloop()