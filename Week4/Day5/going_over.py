# Exercise
# In the python shell, Create a variable called `my_age`, use python to know how old you will be in 123879 years

# my_age = 41
# add_years = 123879
# print(my_age+ add_years)

# random test string + number then print
# x = "My favorite number is " + str(8)
# print(x)

# Exercise

# In the python shell, Create a variable called first_name and a variable called last_name, and 
# then print your full name using those two variables

# first_name = "Rony"
# last_name = "Serrato"
# print(first_name+last_name)

# my_age = 43
# print("My name is Rick, and I am " + str(my_age) + " years old.")

# birthday_day = 8

# birthday_month = 2

# birthday_year = 1979

# print("I was born the",f"{birthday_day}/{birthday_month}/{birthday_year}")

# a = "a"
# b = "A"
# if a > b:
#     print("a is greater than b")
# elif a < b:
#     print("a is lower than b")
# else:
#     print("They must be equal")

# print("Finished")

# my_hobbies = ["sport", "code", "food", "icecreams", "netflix"]
# if  "fish" in my_hobbies:
#     print('fish isnt there')


# If the number is a multiple of three, print "Fizz"
# If the number is a multiple of five, print "Buzz".
# If the number is a multiple is a multiples of both three and five, print "FizzBuzz" instead.

# user_number = int(input("Please enter a number "))
# if user_number % 3 == 0 and user_number % 5 == 0:
#     print('FizzBuzz')
# elif user_number % 3 == 0:
#     print("Fizz")
# elif user_number % 5 == 0:
#     print("Buzz")
# else:
#     Print('invalid entry')

# print("Hello World \n" * 5)
# x = (99^3) * 8
# print(x)

# computer_brand = 'HP'
# print(f'I have a {computer_brand} computer')

# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. 
# The sentence must contain all the variables created in parts 1, 2 and 3.
# Have your code print the info message.
# Run your code

# name = 'Rony'
# age = 41
# shoe_size = 42
# info = f"My name is {age} my show size is {shoe_size}"
# print(info)
# print(type(shoe_size))

# Exercise 7 : Odd Or Even
# Instructions
# Write code that asks the user for a number and determines whether this number is odd or even.

# first_number = int(input("Write number: "))

# if first_number % 2 == 0:
#     print('number is even')
# else:
#     print('number is odd')

# print('Hello Wolrd\n'*5 + 'I love python\n'*5)

# Exercise 2 : What Is The Season ?
# Instructions

# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)

# month_number = int(input("Write the number of a month: "))
# if 3 <= month_number <= 5:
#     print('spring')
# elif 6 <= month_number <= 8:
#     print('Summer')
# elif 9 <= month_number <= 11:
#     print('Autumn')
# else:
#     print('Winter')


# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.

# Then, print the first and last characters of the given text.

# Construct the string character by character: Print the first character, 
# then the second, then the third, until the full string is printed. For example:

# user_string = input("write 10 letters: ")

# Exercise 1 : Favorite Numbers
# Instructions

# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

# my_fav_numbers = {23,79,7}

# my_fav_numbers.add(13)
# my_fav_numbers.add(41)
# my_fav_numbers.pop()

# friend_fav_numbers = {1,2,3}

# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

# s 

# for num in range(0,21):
#     print(num)

# Exercise 5: Shopping List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Empty the basket.
# Print(basket)

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.insert(0,"Apples")
# basket.count("Apples")
# basket.clear()
# print(basket)

# user_input = input('Fav fruits: ').split(" ")

# fav_fruits = input('Name a fruit: ')

# if fav_fruits in user_input:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print('You chose a new fruit. I hope you enjoy')

# Exercise 10: Who Ordered A Pizza ?

# pizza_top = []

# while True:
#     pizza_input = input("what topping or enter quit to exit: ")
#     if pizza_input == "quit":
#         break
#     else: 
#         pizza_top.append(pizza_input)
#         print(f"The toppings added are {pizza_input}")

# print(f'The topings are {pizza_top}. Total will be 10$+ {2.5*len(pizza_top)}')

# Exercise 12 : Who Is Under 16?
#  if they are less 
# than 16 years old remove them from the list.
# At the end, print the final list.

# list_users = ['Rony', 'Nessim', 'John', "Mr.X"]

# for user in reversed(list_users):
#     age = input(f'Hi {user}, How old are you? ')
#     if int(age) < 16:
#         list_users.remove(user)
#     else:
#         continue
# print(list_users)

# Exercise 14
# Instructions
# Using the list sandwich_orders from Exercise 13, make sure the sandwich ‘pastrami’ appears in 
# the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, 
# and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.


# sandwich_orders = ['Turkey', 'Chicken', 'Tuna', 'Veggie']
# finished_sandwiches = []

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print('I made your ' + current_sandwich + " sandwich")
#     finished_sandwiches.append(current_sandwich)
# print(finished_sandwiches) 
       
# sandwich_orders = ['Turkey', 'Chicken', 'Tuna', 'Veggie', 'Pastrami', 'Pastrami', 'Pastrami']
# finished_sandwiches = []
# print('We are out of Pastrami')

# while 'Pastrami'in sandwich_orders:
#     sandwich_orders.remove("Pastrami") 

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print('I made your ' + current_sandwich + " sandwich")
#     finished_sandwiches.append(current_sandwich)

# print(finished_sandwiches)    

# is_magician = False
# is_expert = True

# if is_magician and is_expert:
#     print('You are a master magician')
# elif is_magician and not is_expert:
#     print('at least you getting there')
# else:
#     print('You need magic power')

# birth_year = input('What year where you born? ')

# age =  2021 - int(birth_year)
# print(age)

# username = input("Type in your username: ")
# password = input("Type your pasword: ")
# secret_password = len(password) * "*"

# print(f'Hi your {username} is {secret_password} long')

# random test for errors
# fruits = [9,2,3,4,6,7,8]
# new_fruit = sum(fruits[2:4])
# print(new_fruit)

# my_tuple = (1+3, 2.7, 'Thursday')
# print(my_tuple)

# Exercise
# Given this list: list1 = [5, 10, 15, 20, 25, 50, 20], find value 20 in the list, and if it is present, 
# replace it with 200. Only update the first occurrence of a value

# list1 = [5, 10, 15, 20, 25, 50, 20]
# list2= []
# if "20" in list1:
#     list2 = list1.replace(20, 200)
#     print(list2)

# strings = ["a", "ab", "aa", "c"]
# new_strings = []
# for string in strings:
#     new_string = string.replace("a", "1")
#     new_strings.append(new_string)
#     print(new_strings)

# Exercise
# Given this list: list1 = [5, 10, 15, 20, 25, 50, 20], find value 20 in the list, 
# and if it is present, replace it with 200. Only update the first occurrence of a value

# Hint : Look at the index method

#     Expected output:
#     list1 = [5, 10, 15, 200, 25, 50, 20]

# list1 = [5, 10, 15, 20, 25, 50, 20]
# if "20" in list1:
#     newlist = list1.pop(-1)
#     print(newlist)

# aLsit = [100, 200, 300, 400, 500]
# aLsit.reverse()
# print(aLsit)



# list1 = ["M", "na", "i", "Ke"] 
# list2 = ["y", "me", "s", "lly"]
# list3 = [a + b for a, b in zip(list1, list2)]
# print(list3)

# Given this list: list1 = [5, 10, 15, 20, 25, 50, 20], find value 20 in the list, 
# and if it is present, replace it with 200. Only update the first occurrence of a value

# list1 = [5, 10, 15, 20, 25, 50, 20]
# list2= str(set(list1))
# print(list2)
# Hint : Look at the index method

#     Expected output:
#     list1 = [5, 10, 15, 200, 25, 50, 20]

# # using list comprehension + zip()
# # interlist element concatenation
# res = [i + j for i, j in zip(test_list1, test_list2)]
  
# # printing result 
# print ("The list after element concatenation is : " +  str(res))

# Unpack the following tuple into 4 variables

# a_tuple = (10, 20, 30, 40)
# (a, b, c) = a_tuple
# print(a)
# print(b)
# print(c)

# a_tuple = (10, 20, 30, 40)
# (a, b, c, d) = a_tuple
# print(a)
# print(b)
# print(c)
# print(d)

# n = 0
# while n < 5:
#     n+=1
#     print(n)
 
# Strategy:  Iterate over a copy
# status =[]
# user = []
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status

# Some Built-In Functions That Use For Loops
# Functions like min, max or sum are using for loops behind the scenes; to practice, 
# you can try to program them by yourself.
# sum = input("number: ")
# sum = int(sum)

# for num in sum:
#     final = sum + 1
#     print(final)

# lst = []
# num = int(input('How many numbers: '))
# for n in range(num):
#     numbers = int(input('Enter number '))
#     lst.append(numbers)
# print("Sum of elements in given list is :", sum(lst))

# l = [1,2,3,4,5]
# sum = 0
# for x in l:
#     sum = sum + x

# num = int(input("give a number "))

# for i in range(0,11):
#     print(num, "x", i, "=", num * i)

# Example
# password = ''
# while password != 'hello-world-123':
#   password = input('What is the top secret password? ')

# print('You guessed the right password!')


# Exercise

# Print the numbers from 1 to 10 using while loop

# number = 0
# while number < 10:
#     number += 1
#     print(number)

# current_number = 1 
# while current_number <= 5:    
#     print(current_number)   
#     current_number += 1

#Scroll to bottom to see solution
# You are working for the school Principal. We have a database of school students:
# school = {'Bobby','Tammy','Jammy','Sally','Danny'}
# print(type(school))
#during class, the teachers take attendance and compile it into a list. 
# attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']
# print(type(attendance_list))
#using what you learned about sets, create a piece of code that the school principal can use to 
# immediately find out who missed class so they can call the parents. (Imagine if the list had 1000s of students. 
# The principal can use the lists generated by the teachers + the school database to use python and 
#  his/her job easier): Find the students that miss class!
# print(school.difference(attendance_list))

# day = ["shalom"]
# def shabat(day):
#     for i in day:
#         print(f'shabat {i}')
# shabat(day)

# for item in "Zero to mastery":
#     item = item + 1
#     print(item)

# my_list = [1,2,3]
# for item in my_list:
#     print(item)
#     item += 1

# lst=["koala", "cat", "fox", "panda", "chipmunk", "sloth", "penguin", "dolphin"]
# #Type your answer here.
# for i in lst:
#     print(i, end=" ")

# Write a while loop that adds all the numbers up to 100 (inclusive).
# counter=0
# total=0

# #Construct your while loop here.
# while counter <= 100:
#     total= total+counter 
#     counter= counter+1
# print(total)

# Using while loop, if statement and str() function; iterate through the list and if there is a 100, print it with its index number. i.e.: "There is a 100 at index no: 5"
# lst=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
# #Type your code here.
# i = 0
# while i < len(lst):
#     if lst[i] == 100:
#         print("There is a 100 at index no: " + str(i))
#     i = i+1

# Using while loop and an if statement write a function named name_adder which appends all the elements in a list to a new list unless the element is an empty string: "".
# lst1=["Joe", "Sarah", "Mike", "Jess", "", "Matt", "", "Greg"]

#Type your code here.

# def name_adder(list):
#     i = 0
#     new_list = []
#     while i < len(list):
#         if list[i] != "":
#             new_list.append(list[i])
#         i = i+1
#     return new_list

# print(name_adder(lst1))

# This time inside a function named name_adder, write a while loop that stops appending items to the new list as soon as it encounters an empty string: "". And prints "There is an empty string and returns the new list."
# lst1=["Sam", "", "Ben", "Olivia", "Alicia"]
# i=0

# #Type your answer here.    
# def name_adder(list):
#     i = 0
#     new_list = []
#     while i < len(list):
#         if list[i] != "":
#             new_list.append(list[i])
#         else:
#             break
#         i = i+1
#     return new_list
# print(name_adder(lst1))

# # class Dog():

# #     # Initializer / Instance Attributes
# #     def __init__(self):
# #         print("A new dog has been initialized !")

# # shelter_dog = Dog()

# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# ## create an instance of the class
# p = Point(3,4)

# ## access the attributes
# print("p.x is:", p.x)
# print("p.y is:", p.y)

# # class Dog():
# #     # Initializer / Instance Attributes
# #     def __init__(self, name_of_the_dog):
# #         print("A new dog has been initialized !")
# #         print("His name is", name_of_the_dog)
# #         self.name = name_of_the_dog

# #     def bark(self):
# #         print("{} barks ! WAF".format(self.name))

# #     def walk(self, number_of_meters):
# #         print("{} walked {} meters".format(self.name, number_of_meters))

# # shelter_dog = Dog("Rex")
# # shelter_dog.walk(10)

# class BankAccount:

#     def __init__(self, account_number, balance=0):
#         self.account_number = account_number
#         self.balance = balance
#         self.transactions = []

#     def view_balance(self):
#         self.transactions.append("View Balance")
#         print(f"Balance for account {self.account_number}: {self.balance}")

#     def deposit(self, amount):
#         if amount <= 0:
#             print("Invalid amount")
#         elif amount < 100:
#             print("Minimum deposit is 100")
#         else:
#             self.balance += amount
#             self.transactions.append(f"Deposit: {amount}")
#             print("Deposit Succcessful")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient Funds")
#         else:
#             self.balance -= amount
#             self.transactions.append(f"Withdraw: {amount}")
#             print("Withdraw Approved")
#             return amount

#     def view_transactions(self):
#         print("Transactions:")
#         print("-------------")
#         for transaction in self.transactions:
#             print(transaction)


# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show_details(self):
#         print("Hello my name is " + self.name)

#     def new_name(self, name):
#         self.name = name
#         print(f'Your new name is: {self.name}')



# first_person = Person("John", 36)
# first_person.new_name('Rony')
# first_person.show_details()

# class Circle:
#     color = "red"

# class NewCircle(Circle):
#     color = "blue"

# c= Circle
# nc = NewCircle
# print(c.color)

# class Circle:
#     def __init__(self, diameter):
#       self.diameter = diameter

#     def grow(self, factor=2):
#         """grows the circle's diameter by factor"""
#         self.diameter = self.diameter * factor

# class NewCircle(Circle):
#     def grow(self, factor=2):
#         """grows the area by factor..."""
#         self.diameter = (self.diameter * factor * 2)

# nc = NewCircle(1)
# print(nc.diameter)

# nc.grow()

# print(nc.diameter)

# class Door():
#     def __init__(self, is_opened):
#         self.is_opened = is_opened

#     def open_door(self):
#         print('door has been opened')
#         self.is_opened = True

#     def close_door(self):
#         print('door has been closed')
#         self.is_opened = False


# class BlockedDoor(Door):
#     def open_door(self):
#         print('door is blocked and cannot be opened or closed')

#     def close_door(self):
# #         self.open_door()

# Given a list of numbers, write a function that returns the sum of every number. 
# BUT you can have a malicious string inside the list.

# my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]

# def sum_malicious(g)

# def names(*agrs):
#     for name in agrs:
#         print(name)

# def dogs(*agrs):
#     for 