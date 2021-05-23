# from datetime import date

# def calculateAge(birthDate):
#     today = date.today()
#     age = today.year - birthDate.year -((today.month, today.day) <
#     (birthDate.month, birthDate.day))
#     return age

# # print(calculateAge(date(1997, 2, 3)), "years")

# birth_year = int(input("Enter Year of Birth "))
# birth_month = int(input("Enter Month of Birth "))
# birth_day = int(input("Enter day of Birth "))

# age = calculateAge(date(birth_year, birth_month, birth_day))
# candles_num = age % 10
# dashes_calc = int((18-candles_num)/2)
# dashes = '_' * dashes_calc

# print(age)

# def cake(candles,dash):
#     print('  ' + dash + 'i' * candles + dash + ' ')
#     print('  |   :H:a:p:p:y:  |')
#     print(' _|________________|_')
#     print(' |^^^^^^^^^^^^^^^^^^|')
#     print(' | :B:i:r:t:h:d:a:y:|')
#     print(' |                  |')
#     print(' ~~~~~~~~~~~~~~~~~~~~')

# cake(candles_num, dashes)

# Instructions
# Write a JavaScript program that recreates the pattern below.
# Do this challenge twice: first by using one loop, then by using two nested for loops (Nested means one inside the other - check out “nested for loops” on Google).
# Do this Daily Challenge by youself, without looking at the answers on the internet.
# *  
# * *  
# * * *  
# * * * *  
# * * * * *
# * * * * * *

# def add_star(n):
#     star.repeat(6)

star = '*'
counter = 7


while counter != 0:
    stars = star * counter
    counter -= 1
    print(stars)
