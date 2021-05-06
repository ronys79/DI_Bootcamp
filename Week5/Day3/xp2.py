# Exercise 1
# 
# from datetime import datetime
# def call_time():
#     date = datetime.now()
#     print(f'current time/date now is {date}')
# call_time()
# Exercise 2
# 
# from datetime import *
# def days_remaining():
#     today = datetime.now()
#     future = datetime(2022,1,1,)
#     # print(str(future - today))
#     print((future - today))
# days_remaining()

# Exercise 3
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice), 
# then display a message stating how many minutes the user has been alive.
from datetime import *
def alive():
    year= int(input("What year where you born?"))
    month=int(input("What month were you born?"))
    day=int(input("What day were you born?"))
    today = date.today()
    bday = date(year,month,day)
    answer = today - bday
    print(answer)
    print((today - bday)*1440)

alive()
