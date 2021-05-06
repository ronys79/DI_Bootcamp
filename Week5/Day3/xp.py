# Exercise 1 : Built-In Functions

# Instructions
# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them take a look at the python 
# documentation online.

# Write a program which prints some of python’s built-in 
# functions such as abs(), int(), raw_input().

# Create your own documentation explaining what your classes functionality is, 
# you can do this by using the __doc__ dunder method take a look on google for help.

# # 1. abs
# integer = 20
# print(abs(integer))

# # 2. int()
# string_num = "20"
# print(int(string_num))
# x
# # input()
# data = input('What would you like printed below: ')
# print(data)

# ----------
class Answer():
    '''     1. The abs() function returns the absolute value of the specified number.
    
    2. The int() function converts the specified value into an integer number.

            The int() function returns an integer object constructed from a number or string x, 
            or return 0 if no arguments are given.
            
    3. The print() function prints the specified message to the screen, or other standard output device.
            The message can be a string, or any other object, the object will be converted into a string before written to the screen.'''
    
    def __init__(self, num):
        self.num = num

    def abs_answer(self):
        return abs(self.num)

    def int_answer(self):
        return int(self.num)

    def print_answer(self):
        return print1(self.num)

        
a1= Answer(2)
print(a1.abs_answer())
print (Answer.__doc__)

# print (int1("1"))
# print (int1.__doc__)

# print(print("You did it, next xp"))

# 1. abs
# integer = 20
# print(abs(integer))

# Exercise 2: Currencies
# Instructions
# Create the code which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.
# >>> c1 = Currency('dollar', 5)
# >>> c2 = Currency('dollar', 10)
# >>> c4 = Currency('shekel', 1)
# >>> c3 = Currency('shekel', 10)

# class Currency():
#     def __init__(self, money_type, amount):
#         self.money_type = money_type
#         self.amount = amount

#     def __str__(self):
#         return f' {self.amount} {self.money_type}'
    
#     def __repr__(self):
#         return f' {self.amount} {self.money_type}'
 
#     def __int__(self):
#         return self.amount

#     def __add__(self, other):
#         if self.money_type == other.money_type:
#             return self.amount + other.amount
#         else:
#             print('Wrong currencies type')

# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 10)