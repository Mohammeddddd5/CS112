from tkinter import *

root = Tk()
root.title("Nubby's Calculator")
entry = Text(root, width=50, borderwidth=1, height=10, bg="#3B3B3B", foreground="white", bd=0, heigh=5)
root.configure(bg="#3B3B3B")
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = entry.get("1.0", "end-1c")  # Retrieve all text from the Text widget
    entry.delete("1.0", "end")  # Clear all text from the Text widget
    entry.insert("1.0", str(current) + str(number))  # Insert new text

def button_clear():
    entry.delete("1.0", "end")

def button_add():
    global fnum
    global math
    math = "addition"
    fnum = float(entry.get("1.0", "end-1c"))
    entry.delete("1.0", "end")

def button_subtract():
    global fnum
    global math
    math = "subtraction"
    fnum = float(entry.get("1.0", "end-1c"))
    entry.delete("1.0", "end")

def button_multiply():
    global fnum
    global math
    math = "multiplication"
    fnum = float(entry.get("1.0", "end-1c"))
    entry.delete("1.0", "end")

def button_divide():
    global fnum
    global math
    math = "division"
    fnum = float(entry.get("1.0", "end-1c"))
    entry.delete("1.0", "end")

def button_equal():
    second_num = float(entry.get("1.0", "end-1c"))
    entry.delete("1.0", "end")
    if math == "addition":
        entry.insert("end", fnum + second_num)
    elif math == "subtraction":
        entry.insert("end", fnum - second_num)
    elif math == "multiplication":
        entry.insert("end", fnum * second_num)
    elif math == "division":
        if second_num == 0:
            entry.insert("end", "Error: Division by zero")
        else:
            entry.insert("end", fnum / second_num)


button1 = Button(root, text="1", padx=67, pady=30, command=lambda: button_click(1), bg="#3B3B3B", borderwidth=0, foreground="white", border=0)
button1.grid(row=3, column=0)

button2 = Button(root, text="2", padx=67, pady=30, command=lambda: button_click(2), bg="#3B3B3B", borderwidth=0, foreground="white", border=0)
button2.grid(row=3, column=1)

button3 = Button(root, text="3", padx=67, pady=30, command=lambda: button_click(3), bg="#3B3B3B", borderwidth=0, foreground="white", border=0)
button3.grid(row=3, column=2)

button4 = Button(root, text="4", padx=67, pady=30, command=lambda: button_click(4), bg="#3B3B3B", borderwidth=0, foreground="white", border=0)
button4.grid(row=2, column=0)

button5 = Button(root, text="5", padx=67, pady=30, command=lambda: button_click(5), bg="#3B3B3B", borderwidth=0, foreground="white", border=0)
button5.grid(row=2, column=1)

button6 = Button(root, text="6", padx=67, pady=30, command=lambda: button_click(6), bg="#3B3B3B", borderwidth=0, foreground="white", border=0)
button6.grid(row=2, column=2)

button7 = Button(root, text="7", padx=67, pady=30, command=lambda: button_click(7), bg="#3B3B3B", borderwidth=0, foreground="white", border=0)
button7.grid(row=1, column=0)

button8 = Button(root, text="8", padx=67, pady=30, command=lambda: button_click(8), bg="#3B3B3B", borderwidth=0, foreground="white", border=0)
button8.grid(row=1, column=1)

button9 = Button(root, text="9", padx=67, pady=30, command=lambda: button_click(9), bg="#3B3B3B", borderwidth=0, foreground="white", border=0)
button9.grid(row=1, column=2)

button0 = Button(root, text="0", padx=67, pady=30, command=lambda: button_click(0), bg="#3B3B3B", borderwidth=0, foreground="white", border=0)
button0.grid(row=4, column=0)

addition = Button(root, text="+", padx=67, pady=30, command=lambda: button_add(), bg="#3B3B3B", borderwidth=0, foreground="white", border=0)
addition.grid(row=5,column=0)

equal = Button(root, text="=", padx=140, pady=30, command=lambda: button_equal(), bg="#3B3B3B", borderwidth=0, foreground="white", border=0)
equal.grid(row=5,column=1,columnspan=2)

subtract = Button(root, text="-", padx=67, pady=30, command=lambda: button_subtract(), bg="#3B3B3B", borderwidth=0, foreground="white", border=0)
subtract.grid(row=4,column=1)

multiply = Button(root, text="x", padx=67, pady=30, command=lambda: button_multiply(), bg="#3B3B3B", borderwidth=0, foreground="white", border=0)
multiply.grid(row=6,column=0)

divide = Button(root, text="/", padx=67, pady=30, command=lambda: button_divide(), bg="#3B3B3B", borderwidth=0, foreground="white", border=0)
divide.grid(row=4,column=2)

clear = Button(root, text="Clear", padx=130, pady=30, command=lambda: button_clear(), bg="#3B3B3B", borderwidth=0, foreground="white", border=0)
clear.grid(row=6,column=1,columnspan=2)

root.mainloop()