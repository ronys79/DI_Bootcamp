# Exercise 1 : What Are You Learning ?

# def display_message():
#     print("Hi everyone, I am learming python!")

# display_message()

# Exercise 2: What’s Your Favorite Book ?

# def favorite_book(title):
#     print('One of my favorite books is', title)

# favorite_book("The secret garden")

# Exercise 3 : Some Geography
# Instructions

# Give the country parameter a default value.
# Call your function.

# def describe_city(city, country="Spain"):
#     print(city, 'is in', country)

# print(describe_city('Tarrifa'))

# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates another 
# number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, 
# otherwise show a fail message and display both numbers.

# from random import randint

# user_input = int(input("Enter a number "))
# random_num = (randint(0,100))

# def user_number():
#     if user_input == random_num:
#         print('Correct!!')
#     else: 
#         print(f'the number to guess was {random_num} and your number was {user_input}')

# user_number()

# Exercise 5 : Let’s Create Some Personalized Shirts !

# def make_shirt(size, tshirt_msg):
#     print('the shirt size is', size, 'plus it has on it', tshirt_msg)

# make_shirt('small', 'I am pythoning today like a KING!!')
# make_shirt(size = 'large', tshirt_msg = 'I love Python')

# Bonus: Call the function make_shirt() using keyword arguments. !!! GET HELP FROM CHAIM!!!

# Exercise 6 : Magicians …

# Write a function called make_great() that modifies the list of magicians by adding the phrase 
# "the Great" to each magician’s name.
# Call the function make_great().
# Call the funcyion show_magicians() to see that the list has actually been modified.

# magician_name = ["Harry Houdini", "David Copperfield", "Doug Henning", "Lance Burton"]

# def show_magicians():
#     for magician in magician_name:
#         print(magician)

# show_magicians()

# great_magician = []
# def make_great():
#     for magician in magician_name:
#         great_magician.append(f'The Great {magician}')
#     print(great_magician)

# make_great()

# ------------------------

# XP part 2

# Exercise 7: When Will I Retire ?
# Instructions
# The point of the exercise is to check if a person can retire depending on their age and their gender.
# Note : Retirement age in Israel is 67 for men, and 62 for women (born after April, 1947).


# Hard-code the current year and month in your code (there are better ways of doing this, 
# but for now it will be enough.)
# After calculating the age of a person, the function should return the age (the age is an integer).
# Create a function can_retire(gender, date_of_birth).
# It should call the get_age function (with what arguments?) in order to receive an age.
# Now it has all the information it needs in order to determine if the person with the given gender and date of birth is able to retire or not.
# Calculate. You may need to do a little more hard-coding here.
# Return True if the person can retire, and False if he/she can’t.
# Some Hints

# Ask for the user’s gender as “m” or “f”.
# Ask for the user’s date of birth in the form of “yyyy/mm/dd”, eg. “1993/09/21”.
# Call can_retire to get a definite value for whether the person can or can’t retire.
# Display a message informing the user whether they can retire or not.
# As always, test your code to ensure it works.

# Key words: if , is , in , men or women
# user_year = input("What year were you born?")
# user_gender = input("Type M for male or F for Female")
# def get_age(year, month, day):

#     if user_gender == 'male':
