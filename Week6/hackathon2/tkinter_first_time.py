# from tkinter import *

# root = Tk()

# # Creates the label widget
# myLabel = Label(root, text='Hello World!')
# myLabe2 = Label(root, text='My name is Rony')

# # Simple pack the label created into the screen
# myLabel.pack()

# # stays active till loop ends when window closed
# root.mainloop()

# from _typeshed import OpenBinaryModeReading
# from tkinter import *

# root = Tk()

# # Creates the label widget
# myLabel1 = Label(root, text='Hello World!')
# myLabel2 = Label(root, text='My name is Rony')

# # create collomns and rows
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=0, column=0)
# # stays active till loop ends when window closed
# root.mainloop()

# DRY CODE

# from _typeshed import OpenBinaryModeReading
# from tkinter import *

# root = Tk()

# # Creates the label widget
# myLabel1 = Label(root, text='Hello World!').grid(row=0, column=0)
# myLabel2 = Label(root, text='My name is Rony').grid(row=0, column=0)

# # stays active till loop ends when window closed
# root.mainloop()

#BUTTON BASICS
# from tkinter import * 

# root = Tk()

# def myClick():
#     myLabel = Label (root, text='I LOVE YOU')
#     myLabel.pack()
# myButton = Button(root, text='MY BUBALEH', command=myClick)

# myButton.pack()
# root.mainloop()

# INPUT BOXES BASIC

from tkinter import * 

root = Tk()

e = Entry(root, width=25, bg='white')
e.pack()
# Default txt inside txt box
e.insert(0, "insert your name: ")

def myClick():
    myLabel = Label (root, text=e.get())
    myLabel.pack()
myButton = Button(root, text='MY BUBALEH', command=myClick)

myButton.pack()
root.mainloop()
