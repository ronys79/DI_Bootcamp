# my_age = 41
# time_pass = 123879
# age_future = my_age + time_pass
# print(age_future)

# a=101
# x=100

# if a > x:
#     print(f"{a} is greater than {x}")
# if a < x:
#     print(f"{a} is not greater than{x}")
# elif a == x:
#     print(f"{a} equals {x}")

# print("what you doing?")

# name = input('Please state your name: ')

# if name == 'Frank':
#   print('You are Frank Sinatra')
# elif name == 'Miles':
#   print('You are Miles Davis')
# elif name == 'Tony':
#   print('You are Tony Benett')
# else:
#   print('I do not know who you are!')

# Ask the user for a number betwee 1 and 100
# If the number is a multiple of three, print "Fizz"
# If the number is a multiple of five, print "Buzz".
# If the number is a multiple is a multiples of both three and five, print "FizzBuzz" instead.

# user_number = input('Please enter a number: ')
# user_number = int(user_number)
# # if user_number.isnumeric()
# if user_number % 3 == 0 and user_number % 5 == 0:
#     print("FizzBuzz")
# elif user_number % 3 == 0:
#     print('Fizz')
# elif user_number % 5 == 0:
#     print('Buzz')
# else:
#     print('invalid')

# print("Hello World\n" * 5)
    
# print((99^3) * 8)
# import calendar as c

# print(c.month_name[1])

# x = (1 == True)
# y = (1 == False)
# a = True + 4
# b = False + 10

# print("x is", x)
# print("y is", y)
# print("a:", a)
# print("b:", b)

# my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
#            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
#            Ut enim ad minim veniam, quis nostrud exercitation ullamco 
#            laboris nisi ut aliquip ex ea commodo consequat. 
#            Duis aute irure dolor in reprehenderit in voluptate velit 
#            esse cillum dolore eu fugiat nulla pariatur. 
#            Excepteur sint occaecat cupidatat non proident, 
#            sunt in culpa qui officia deserunt mollit anim id est laborum.
#            """
# print(len(my_text))

# Exercise 5: Longest Word Without A Specific Character
# Instructions
# Keep asking the user to input the longest sentence they can without the character “A”.
# Each time a user successfully sets a new longest sentence, print a congratulations message.

# dog = "xdasds"
#  if "x" is in dog:
#       print "Yes!"

# user_sentence = input ("input the longest sentence they can without the character 'A'." )
# if "a" in user_sentence:
#     print("Try again, you did it with an a")
# else:
#     print("well done!")

# fruits = ["Apple", "Banana", "Kiwi", "Mango"]

# # various len functions
# print (len(fruits))
# fruits.append("Melon")
# fruits.remove("Apple")
# print (fruits)
# -----
# Exercise
# Access the value of key "history"
# sampleDict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }

# print(sampleDict['class']['student']['marks']['history'])

# my_books = {
#   "title": "Harry Potter",
#   "author": "JK Rowling",
# }

# for aaa, b in my_books.items():
#     print("the" + aaa + "is" + b)

# for (a, b) in enumerate('abcd'):
#     print(f'At index {a} the letter is {b}')

# wallet = 0

# while wallet < 100:
#     print(f'you got {wallet} left till 100')
#     wallet += 10
# else:
#     print("you broke now!")

# for letter in 'Leonardo':
#     if letter == 'a':
#         break
#     print(letter, end='') # end='' renders each letter next to the other

# while True:
#     s = input('Enter something : ')
#     if s == 'quit':
#         break
#     print('Length of the string is', len(s))
# print('Done')

# for letter in 'Leonardo':
#     if letter == 'L':
#         continue
#     print(letter, end='')

# my_list = []

# for i in [x, y, z]:
#     for j in [100, 200, 300]:
#         my_list.append(i*j)

# print(my_list)

#Make a dictionery open up 
# for key, value in person_dict.items():print(f'{key}:{value}')

# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }

# for key in sampleDict:
#     if name_d == "Kelly" and salary_d == 8000:
#         del sampleDict[name_d], [salary_d]
# keysToRemove = ["name", "salary"]


# keys_to_remove = ["name", "salary"]
# for key in keys_to_remove:
#   del sampleDict[key]

# print(sampleDict)

# sentence = input("Enter a sentence :")
# print(" " reversed(sentence.split()))

# REverseinp= input('enter a sentence')
# print(" ".join(reversed(REverseinp.split())))

# for letter in text:
#     cypher_text += chr(ord(letter) + 3)

# Exercise
# Write a function calculation() such that it can accept two variables and 
# calculate the addition and subtraction of it. And also it must return both addition and subtraction 
# in a single return call

# For example:

# def calculation(a, b):
#     return a + b, a - b

# res = calculation(40, 10)
# print(res)
picture[...

]

for image in picture:
    for pixel in image:
        if (pixel):
            print('*', end ='')
        else:
            print(' ', end ='')
    print('')