# # Add images with  Tkinter
# from tkinter import *
# from PIL import ImageTk,Image
# root = Tk()
# root.title('Who is the most special ever!')
# # simple icon to pop up window tab
# root.iconbitmap("images\heart.ico") 

# # add image to txt part of pop up. define the image and then load it up
# my_img = ImageTk.PhotoImage(Image.open("images/buddha2.jpg"))
# my_label = Label(image=my_img)
# my_label.pack()

# root.mainloop()

# PHOTO VIEWER
from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title('Who is the most special ever!')
# simple icon to pop up window tab

# add image to txt part of pop up. define the image and then load it up
my_img1 = ImageTk.PhotoImage(Image.open("images/buddha1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/buddha2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/buddha3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/buddha4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/buddha5.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan= 3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda:forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    my_label.grid(row=0, column=0, columnspan= 3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back():
    global my_label
    global button_forward
    global button_back


button_back = Button(root, text="<<", command=back)
button_exit = Button(root, text="EXIT PROGRAM", command=root.quit)
button_forward = Button(root, text=">>", command=lambda:forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()

