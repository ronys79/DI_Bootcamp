# # f_name = "Rony"
# # l_name = "Serrato"
# # print(f_name, l_name)

# # Exercise 2

# # Place a comment next to each variable. The comments will:


# # Explain what each variable does
# # Find out the type of each
# # Format each variable into a print statement

# #For example,  
# # my_name = "Frank"  this line creates a name variable type: string 
# #print("My name is {}".format(my_name))

# # int - full number
# cars = 100 
# # float - decimanl number
# space_in_a_car = 4.0
# drivers = 30
# passengers = 90
# cars_not_driven = cars - drivers
# cars_driven = drivers
# carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car = passengers / cars_driven


# print(f"There are {cars} cars available.")
# print(f"There are only {drivers} drivers available.")
# print(f"There will be {cars_not_driven} empty cars today.")
# print(f"We can transport {carpool_capacity} people today.")
# print(f"We have {passengers} to carpool today.")
# print(f"We need to put about {average_passengers_per_car} in each car.")

# # print("There are", str(cars), "cars available.")
# # print("There are only", str(drivers), "drivers available.")
# # print("There will be", str(cars_not_driven), "empty cars today.")
# # print("We can transport", str(carpool_capacity), "people today.")
# # print("We have", str(passengers), "to carpool today.")
# # print("We need to put about", str(average_passengers_per_car),"in each car.")


# Exercise
# Ask the user for a number betwee 1 and 100

# If the number is a multiple of three, print "Fizz"

# If the number is a multiple of five, print "Buzz".

# If the number is a multiple is a multiples of both three and five, print "FizzBuzz" instead.

user_num = input("Please enter a number between 1 and 100: ")

if user_num.isalpha():
    print(f'"{user_num}" was your input, it is not a number, Goodbye')

elif int(user_num) > 0 and int(user_num) < 101:
    user_num = int(user_num)
    if user_num % 3 == 0 and user_num % 5 == 0:
        print("FizzBuzz")
    elif user_num % 3 == 0:
        print("fiz")
    elif user_num % 5 == 0:
        print("Buzz")
    else: 
        print("Sorry not divisible by 3 or 5")
elif int(user_num) > 100:
    print('You went over 100, goodbye')

else:
    print('You went below 0, you are unique, goodbye')
