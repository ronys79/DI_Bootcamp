import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import datetime
# for input key verify
import re
# aaa
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
  
        # limiting to 2 decimal places 
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
        self.tabControl = ttk.Notebook(self.root)
        self.tabControl.pack(pady=1)

        # Create Frames 
        self.currency_frame = Frame(self.tabControl, width=700, height=400)
        self.calculator_frame = Frame(self.tabControl, width=700, height=400)
        self.currency_frame.pack(fill="both", expand=1)

        # responsive background image
        self.image = Image.open("images/bg2.jpg")
        self.img_copy= self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self.currency_frame, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        
        # Label
        self.intro_label = Label(self.currency_frame, text = 'Developer\'s Institute Hackacthon 2 \nCurrency converter', relief = tk.RAISED, borderwidth = 4)
        self.intro_label.config(font = ('Verdana',14,'bold'))
        self.root.iconbitmap('images/icon.ico')
        self.date_label = Label(self.currency_frame, text = f"1 New Israeli Shekel = {self.currency_converter.convert('ILS','USD',1)} USD \n Last Update : {self.currency_converter.data['time_last_update_utc']}", relief = tk.GROOVE, font = ('Verdana',12,'bold'), borderwidth = 5)

        self.intro_label.place(relx = .5 , rely = .25, anchor=CENTER)
        self.date_label.place(relx = .5 , rely = .47, anchor=CENTER)

        # Entry box
        valid = (self.root.register(self.restrictNumberOnly), '%d', '%P')
        self.amount_field = Entry(self.currency_frame,bd = 3, relief = tk.RIDGE, justify = tk.CENTER,validate='key', validatecommand=valid)
        self.converted_amount_field_label = Label(self.currency_frame, text = '', fg = 'black', bg = 'white', relief = tk.RIDGE, justify = tk.CENTER, width = 17, borderwidth = 3)

        # dropdown
        self.from_currency_variable = StringVar(self.currency_frame)
        self.from_currency_variable.set("ILS") # default value
        self.to_currency_variable = StringVar(self.currency_frame)
        self.to_currency_variable.set("USD") # default value

        font = ("Courier", 12, "bold")
        self.root.option_add('*TCombobox*Listbox.font', font)
        # here it selects the currency keys from api/json see if can get 
        # a better api for free that displays currency name instead of acronym
        self.from_currency_dropdown = ttk.Combobox(self.currency_frame, textvariable=self.from_currency_variable,values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 12, justify = tk.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self.currency_frame, textvariable=self.to_currency_variable,values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 12, justify = tk.CENTER)

        # placing of 4 lateral field boxes

        self.from_currency_dropdown.place(relx = .06 , rely = .65, anchor=W)
        self.amount_field.place(relx = .067 , rely = .75, anchor=W, height =35 )
        self.to_currency_dropdown.place(relx = .93 , rely = .65, anchor=E)
        self.converted_amount_field_label.place(relx = .923 , rely = .75, anchor=E, height =35)

        # Convert button
        self.convert_button = Button(self.currency_frame, text = "Convert", fg = "black", command = self.perform) 
        self.convert_button.config(font=('Courier', 16, 'bold'))
        self.convert_button.place(relx = .5 , rely = .65, anchor=CENTER)

# Method that will take the user input and convert the amount into the desired currency
# and display it on the converted_amount entry box. Part of App class
    def perform(self):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = self.currency_converter.convert(from_curr,to_curr,amount)
        converted_amount = round(converted_amount, 2)

        self.converted_amount_field_label.config(text = str(converted_amount))

#    user can enter only a number/float in Amount Field working
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