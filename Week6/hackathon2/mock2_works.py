import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
# from tkinter import messagebox
import datetime
# for input key verify
import re
# import sqlite3


# # database to store inputs, no reason for this except to see if can do it
# conn = sqlite3.connect('money.db')
# # create cursos
# c = conn.cursor

# # create table
# # THE FLIPPING execute doesnt work???? whyyyyy!!!!!
# c.execute("""CREATE TABLE spy (
#     {from_currency_variable} text,
#     {amount} interger,
#     {to_currency_variable} integer
#     )""")

# # databse commit changes
# conn.commit()
# # databse close connection
# conn.close()



# constructor of class
class CurrencyConverter():
    def __init__(self,url):
        # requests.get() loads the page then .json() will convert 
            self.data = requests.get(url).json()
        # store it in a data variable
            self.currencies = self.data['conversion_rates']
    

    def convert(self, from_currency, to_currency, amount): 
        initial_amount = amount 
        if from_currency != 'ILS' : 
            amount = amount / self.currencies[from_currency] 
  
        # rounding to 2 decimal places 
        amount = round(amount * self.currencies[to_currency], 2) 
        return amount

# UI class for currency converter
class App:
    
    # Frame created
    def __init__(self, converter):
        self.root = tk.Tk()
        # Date time for tab title
        time = datetime.datetime.now()
        time = time.strftime("Current Date: %d-%m-%Y   Current time: %H:%M")
        self.root.title('Real Time Currency Conversion            ' + time)
        self.currency_converter = converter
        # Background color which only affect tabs, must have magenta in code!
        self.root.configure(background = 'dark magenta')
        self.root.geometry("700x400")
        
        # Create Tabs
        # self.tabControl = ttk.Notebook(self.root)
        # self.tabControl.pack(pady=1)
        # ------NEED HELP CREATING FRAMES PROPERLY
        # --------------------------------------------
        # Create Two Frames - not doing this right or not linking them right
        # self.currency_frame = Frame(self.tabControl, width=700, height=400)
        # self.calculator_frame = Frame(self.tabControl, width=700, height=400)
        # self.bio_frame = Frame(self.tabControl, width=700, height=400)

        # self.currency_frame.pack(fill="both", expand=1)
        # self.calculator_frame.pack(fill="both", expand=1)
        # self.bio_frame.pack(fill="both", expand=1)
        # --------------------------------------------

        # NEED HELP CREATING TABS! TO THE WIDGET!!#
        # --------------------------------------------
        
        # Add Tabs
        # self.tabControl.add(self.root, text="Currencies")
        # self.tabControl.add(self.root, text="Calculator")
        # self.tabControl.add(self.root, text="Bio_Frame")
        # --------------------------------------------
        # self.tab1 = ttk.Frame(self.tabControl)
        # self.tabControl.add(self.tab1, text = "Converter")
       
        # self.tab2 = ttk.Frame(self.tabControl)
        # self.tabControl.add(self.tab2, text = "Calculator")
        
        # self.tabControl.pack(expand=1, fill="both")

        # # Create Two Frames
        # currency_frame = Frame(my_notebook, width=700, height=400)
        # calculator_frame = Frame(my_notebook, width=700, height=400)

        # currency_frame.pack(fill="both", expand=1)
        # calculator_frame.pack(fill="both", expand=1)

        # --------------------------------------------
        # 
        
         # background image + size option1 works
        # IMAGE_PATH = 'images/buddha1.jpg'
        # WIDTH, HEIGHT = 500, 200
        # img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
        # lbl = tk.Label(self, image=img)
        # lbl.img = img  # for when used inside a method/function.
        # lbl.place(relx=0.5, rely=0.5, anchor='center')  # Place image in center of parent.
        

        # responsive background image option2
        self.image = Image.open("images/bg2.jpg")
        self.img_copy= self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self.root, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    # method for image to be responsive 


        # Label
        self.intro_label = Label(self.root, text = 'Developer\'s Institute Hackacthon 2 \nCurrency converter', relief = tk.RAISED, borderwidth = 4)
        self.intro_label.config(font = ('Verdana',14,'bold'))
        self.root.iconbitmap('images/icon.ico')
        self.date_label = Label(self.root, text = f"1 New Israeli Shekel = {self.currency_converter.convert('ILS','USD',1)} USD \n Last Update : {self.currency_converter.data['time_last_update_utc']}", relief = tk.GROOVE, font = ('Verdana',12,'bold'), borderwidth = 5)

        self.intro_label.place(relx = .5 , rely = .25, anchor=CENTER)
        self.date_label.place(relx = .5 , rely = .47, anchor=CENTER)

        # Entry box
        valid = (self.root.register(self.restrictNumberOnly), '%d', '%P')
        self.amount_field = Entry(self.root,bd = 3, relief = tk.RIDGE, justify = tk.CENTER,validate='key', validatecommand=valid)
        self.converted_amount_field_label = Label(self.root, text = '', fg = 'black', bg = 'white', relief = tk.RIDGE, justify = tk.CENTER, width = 17, borderwidth = 3)

        # dropdown
        self.from_currency_variable = StringVar(self.root)
        self.from_currency_variable.set("ILS") # default value
        self.to_currency_variable = StringVar(self.root)
        self.to_currency_variable.set("USD") # default value

        font = ("Courier", 12, "bold")
        self.root.option_add('*TCombobox*Listbox.font', font)
        # here it selects the currency keys from api/json see if can get 
        # a better api for free that displays currency name instead of acronym
        self.from_currency_dropdown = ttk.Combobox(self.root, textvariable=self.from_currency_variable,values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 12, justify = tk.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self.root, textvariable=self.to_currency_variable,values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 12, justify = tk.CENTER)

        # placing of 4 lateral field boxes

        self.from_currency_dropdown.place(relx = .06 , rely = .65, anchor=W)
        self.amount_field.place(relx = .067 , rely = .75, anchor=W, height =35 )
        self.to_currency_dropdown.place(relx = .93 , rely = .65, anchor=E)
        self.converted_amount_field_label.place(relx = .923 , rely = .75, anchor=E, height =35)

        # Convert button
        self.convert_button = Button(self.root, text = "Convert", fg = "black", command = self.perform) 
        self.convert_button.config(font=('Courier', 16, 'bold'))
        self.convert_button.place(relx = .5 , rely = .65, anchor=CENTER)
    def _resize_image(self,event):
        new_width = event.width
        new_height = event.height
        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)
# Method that will take the user input and convert the amount into the desired currency
# and display it on the converted_amount entry box. Part of App class
    def perform(self):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = self.currency_converter.convert(from_curr,to_curr,amount)
        converted_amount = round(converted_amount, 2)

        self.converted_amount_field_label.config(text = str(converted_amount))


    # def restrictNumberOnly(self, action):
    #     vcmd = (self(self.callback))
    #     w = Entry(self.string, validate='all', validatecommand=(vcmd, '%P')) 
    #     w.pack()
    #     if str.isdigit(action) or action == "":
    #         return True
    #     else:
    #         return False


#    user can enter only a number/float in Amount Field
    def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return string=="" or (string.count('.')<=1 and result is not None)

# creates the main function:
# 1. Creates the Converter 2. Creates the UI for Converter
if __name__ == '__main__':
    url = 'https://v6.exchangerate-api.com/v6/21ead1dbb8d52ca2cdfe3088/latest/ILS'
    converter = CurrencyConverter(url)


    App(converter)
    mainloop()


