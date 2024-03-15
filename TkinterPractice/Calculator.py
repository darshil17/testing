import tkinter as tk
op=['+','-','/','*','%']
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    if current=="0" and str(number).isdigit():
        entry.insert(0, str(number))
    elif(current[-1] in op or (current[-1]=="." and str(number)==".")):
        entry.delete(0,tk.END)
        entry.insert(0,current[:len(current)-1]+str(number))
    else:
        entry.insert(0, current+str(number))
def clear():
    if(entry.get()!="0"):
        if len(entry.get())==1:
            entry.delete(0,0)
            entry.insert(0,"0")
        entry.delete(len(entry.get())-1,tk.END)
def allclear():
    entry.delete(0,tk.END)
    entry.insert(0,"0")
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
def on_key_press():
    pass

root = tk.Tk()
root.title("Calculator by Darshil Solanki")
root.geometry("385x350")
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)
entry.insert(0,"0")
entry.bind('<Key>', on_key_press)

button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_dot = tk.Button(root, text=".", padx=40, pady=20, command=lambda: button_click("."))
button_add = tk.Button(root, text="+", padx=40, pady=20, command=lambda: button_click("+"))
button_subtract = tk.Button(root, text="-", padx=40, pady=20, command=lambda: button_click("-"))
button_multiply = tk.Button(root, text="*", padx=40, pady=20, command=lambda: button_click("*"))
button_divide = tk.Button(root, text="/", padx=40, pady=20, command=lambda: button_click("/"))
button_modulo = tk.Button(root, text="%", padx=40, pady=20, command=lambda: button_click("%"))
button_allclear = tk.Button(root, text="AC", width=1,padx=40, pady=20, command=allclear)
button_clear = tk.Button(root, text="C", padx=40, pady=20, command=clear)
button_equal = tk.Button(root, text="=", padx=40, pady=20, command=equal)

button_1.grid(row=2, column=0)
button_2.grid(row=2, column=1)
button_3.grid(row=2, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)
button_0.grid(row=5, column=1)
button_dot.grid(row=5,column=0)
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_modulo.grid(row=5,column=3)
button_allclear.grid(row=1, column=1)
button_clear.grid(row=1, column=2)
button_equal.grid(row=5, column=2)

root.mainloop()