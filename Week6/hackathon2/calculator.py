from tkinter import *

root=Tk()

root.title("Simple Calculator")
e= Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3)
e.insert(0, ' ')

def button_click(number):
    # e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clears():
    e.delete(0, END)

def b_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def b_equal():
    second_number = e.get()
    e.delete(0,END)
    if math == "multiply":
        e.insert(0, f_num * int(second_number))
    elif math == "subtract":
        e.insert(0, f_num * int(second_number))
    elif math == "divide":
        e.insert(0, f_num * int(second_number))
    elif math == "addition":
        e.insert(0, f_num + int(second_number))

def b_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    e.delete(0, END)

def b_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtract"
    f_num = int(first_number)
    e.delete(0, END)

def b_divide():
    first_number = e.get()
    global f_num
    global math
    math = "divide"
    f_num = int(first_number)
    e.delete(0, END)

# Define buttons

button_1 = Button(root, text='1', padx=40, pady=20, command = lambda:button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command = lambda:button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command = lambda:button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command = lambda:button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command = lambda:button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command = lambda:button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command = lambda:button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command = lambda:button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command = lambda:button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command = lambda:button_click(0))

button_sum= Button(root, text='+', padx=39, pady=20, command = b_add)
button_sub= Button(root, text='-', padx=41, pady=20, command = b_subtract)
button_mul= Button(root, text='x', padx=40, pady=20, command = b_multiply)
button_divide= Button(root, text='/', padx=41, pady=20, command = b_divide)


button_equal = Button(root, text='=', padx=91, pady=18, command = b_equal)
button_clear = Button(root, text='CLEAR', padx=79, pady=17, command = button_clears)
# Place buttons in grid
button_9.grid(row=1, column=2)
button_8.grid(row=1, column=1)
button_7.grid(row=1, column=0)

button_6.grid(row=2, column=2)
button_5.grid(row=2, column=1)
button_4.grid(row=2, column=0)

button_3.grid(row=3, column=2)
button_2.grid(row=3, column=1)
button_1.grid(row=3, column=0)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_sum.grid(row=5, column=0 )
button_equal.grid(row=5, column=1, columnspan=2)

button_sub.grid(row=6, column=0 )
button_mul.grid(row=6, column=1 )
button_divide.grid(row=6, column=2 )

root.mainloop()