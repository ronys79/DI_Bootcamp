# import random
# import time

# colours = ['Green', 'Red', 'Yellow']

# counter = 0

# active = True
# while active:
#     time.sleep(5)
#     if counter < 5:
#         random_colour = random.choice(colours)
#         if random_colour == 'Green':
#             print ("You can pass")
#             counter += 1
#         elif random_colour == 'Yellow':
#             print ("Slow it down")
#             counter += 1
#         elif random_colour == 'Red':
#             print ("Stop at red")
#             counter += 1
#     else:
#         print ("Done")
#         break

# for i in range(1,2501, 5):
#     if i = %7 == 0:
#         print(i)

# names = ['chaim', 'shimon', 'lila', 'ronny', 'micheal', 'jonathan', 'eliyahu', 'shmuel']
# names.sort()

# for index, name in enumerate(names):
#     for name in names:
#         print(f'{index +1} and {name}')


# names = ['chaim', 'shimon', 'lila', 'ronny', 'micheal', 'jonathan', 'eliyahu', 'shmuel']
# names.sort()

# for name in names:
#     for letter in name:
#         if 'a' in letter:
#             print(letter)

# create a list which contains both numbers and letters loop throught the list and append all the numbers to a number 
# list and all the letters to a letter list and print ou the 2 lists

# mixed_list = ['chaim', 11, 23, 'shimon', 'lila', 'ronny', 'micheal', 'jonathan', 'eliyahu', 'shmuel']
# num_list = []
# letter_list = []

# for i in the_list:
#     if i.isalpha():
#         str_list.append(i)
#     else:
#         number_list.append(i)

# for item in mixed_list:
#     if isinstance(item, int):
#         num_list.append(item)
#     else:
#         letter_list.append(item)
# print(f'Nums: {num_list}, letters: {letter_list}')

# print(num_list)
# print(letter_list)

# Exercise 3: Print A Range Of Numbers
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.

# for i in range(21):
#     print(i)

# Exercise 6 : Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

# name= ''

# while name != "Rony":
#     name = input('What is your name: ')

# Exercise 7
# Instructions
# Given a list, use a loop to print out every element which has an even index.

# my_list = ['chaim', 'shimon', 'lila', 'ronny', 'micheal', 'jonathan', 'eliyahu', 'shmuel']

# for i, item in enumerate(my_list):
#     if i %2 == 0:
#         print(item)

# Exercise 9: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).

# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).

# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

# fruits_added = 'Placeholder'
# choosen_fruits = []

# while fruits_added != 'x':
#     if fruits_added != 'x':
#         fruits_added = input('What fruit would you like to, when done click (x): ')
#         choosen_fruits.append(fruits_added)
#     else: print('Thank you come again')

# print(choosen_fruits)

# Exercise 10: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

topping = 'Placeholder'
toppings = []
price = 10
while topping[0].lower() != 'q':
    topping = input('Pizza what?')
    toppings.append(topping)
    if topping[0].lower() != 'q':
        print(f'We have add a {topping} to your pizza')
        price += 2.5
print(f'price is {price}')

# Exercise 11: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.
# 


age_cinema = input('Enter ages separated with spaces : ').split()
total = 0
age_group1 = 0
age_group2 = 0
age_group3 = 0

for age in age_cinema:
    if int(age) < 3:
        age_group1 += 1
    if 3 <= int(age) < 12:
        age_group2 += 1
        total += 10
    elif int(age) >= 12:
        age_group3 += 1
        total += 15
print (f'So: {age_group1} under 3, {age_group2} between 3 and 12, {age_group3} over 12 makes ${total}')

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Write a program that asks every user for their age, and prints a list of the teens who are permitted to watch the movie.

age_teenager = int(input('How old are you? '))
name_teens = []
allowed_teens = []

for name in name_teens:
    name_teens =  input('What is your name? ')
    if  16 > age_teenager < 21:
        name_teens.append(allowed_teens)



# list12 = ['Johnny', 'Bill', 'Tom']
# list12_copy = list12.copy()
# for name in list12:
#     age = input('{} !, how old are you ? '.format(name))
#     if int(age) < 16:
#         list12_copy.remove(name)
# print("Remaining people are:", list12_copy)
