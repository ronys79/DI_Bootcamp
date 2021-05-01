# https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
# Python conditional statements and loops 44 excersices

# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, 
# between 1500 and 2700 (both included)

# number_list = []
# for number in range(1500,2701):
#     if (number%7==0) and (number%5==0):
#         number_list.append(str(number))
# print(','.join(number_list))

# nl=[]
# for x in range(1500, 2701):
#     if (x%7==0) and (x%5==0):
#         nl.append(str(x))
# print (','.join(nl))

# 2. Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius

# conversion_type = input('Type C or F for initial conversion: ')
# temperature = float(input('Enter the temperature to convert: '))

# if conversion_type.upper() == "C":
#     fahr = round((temperature * 9.0/5.0) + 32.0)
#     temperature = round(temperature)
#     print(f' {temperature} in Celsius is {fahr} in farenheit')

# elif conversion_type.upper() == "F":
#     cels = round((temperature - 32.0) * 5.0/9.0)
#     temperature = round(temperature)
#     print(f'{temperature} in Farenheit is {cels} in Celsius')

# 3. Write a Python program to guess a number between 1 to 9.
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until 
# the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

# from random import randint

# user_number = int(input('Please enter a number between 1 and 9: '))


# if user_number in range(1,11):
#     hidden_number = randint(0, 10)
#     print(type(hidden_number))
#     user_number = int(input('Please enter a number between 1 and 9: '))
#     while user_number != hidden_number:
#         print(type(user_number))
#         int(input('Please enter a number between 1 and 9: '))
#         print("try again")
#     print('You Win')


# ---- CHAIM I DONT KNOW HOW TO LOOP IN ABSTRACT THINKING TO MAKE ACII PATTERNS-----
# 4. Write a Python program to construct the following pattern, using a nested for loop.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

# n=5;
# for i in range(n):
#     for j in range(i):
#         print ('* ', end="")
#     print('')

# for i in range(n,0,-1):
#     for j in range(i):
#         print('* ', end="")
#     print('')

# 5. Write a Python program that accepts a word from the user and reverse it. Go to the editor
# Click me to see the sample solution
# my answer WRONG:
# user_word = list(input('Say a word to see its reverse order here: '))
# print(user_word)
# user_word.reverse()
# back_word = back.word.join(user_word)
# print(back_word)
# back_word = user_word.str()
# print(back_word)

# answer:
# word = input("Input a word to reverse: ")

# for char in range(len(word) - 1, -1, -1):
#   print(word[char], end="")

# 6. Write a Python program to count the number of even and odd numbers from a series of numbers.
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# even = 0
# odd = 0
# for number in numbers:
#     if number % 2 == 0:
#         even += 1
#     else:
#         odd +=1 
# print(f'Number of even numbers : {even}')
# print(f'Number of odd numbers : {odd}')

# 7. Write a Python program that prints each item and its corresponding type from the following list.
# Sample List : 

# datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

# for item in datalist:
#     print('Type of item', item, "is", type(item))

# 8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5

# numbers = [1,2,3,4,5,6]

# for number in numbers:
#     if number == 3 or number == 6:
#         continue
#     print(number, end=" ")

# 9. Write a Python program to get the Fibonacci series between 0 to 50. Go to the editor
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34

# a=0
# b=1

# for i in range(34):
#     while b < 34:
#         print(a)
#         c = a + b
#         a = b
#         b = c
#         print(c)

# 10. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
# Sample Output :
# fizzbuzz
# 1
# 2
# fizz
# 4
# buzz

# for fizzbuzz in range(51):
#     if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
#         print("fizzbuzz")
#         continue
#     elif fizzbuzz % 3 == 0:
#         print("fizz")
#         continue
#     elif fizzbuzz % 5 == 0:
#         print("buzz")
#         continue
#     print(fizzbuzz)

# 11. Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. Go to the editor
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1.
# -------- CHAIM: PLEASE EXPLAIN THIS -----------------------
# row_num = int(input("Input number of rows: "))
# col_num = int(input("Input number of columns: "))
# multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

# for row in range(row_num):
#     for col in range(col_num):
#         multi_list[row][col]= row*col

# print(multi_list)


# extra : print patterns:
num_rows = int(input("How many rows: "))
'prints single side pyramid'
# for row in range(1, num_rows +1):
#     for column in range(1, row+1):
#         print("*", end=" ")
#     print()
# "prints upside down pyramid"
# for row in range(num_rows, 0, -1):
#     for column in range(1, row+1):
#         print("*", end=" ")
#     print()

'prints single side pyramid'
for row in range(1, num_rows +1):
    for column in range(1, row+1):
        print("*", end=" ")
    print()
"prints upside down pyramid"
for row in range(num_rows-1, 0, -1):
    for column in range(1, row+1):
        print("*", end=" ")
    print()