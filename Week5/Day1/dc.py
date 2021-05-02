# Instructions : Old MacDonald’s Farm
# Take a look at the following code and output!

# macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())

# Output:
# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!


# Create the code that is needed to recreate the code provided above. 

class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.quantity = []
    def add_animal(self, new_animal, quantity=1):
        self.animals.append(new_animal)
        self.quantity.append(quantity)

    def get_info(self):
        print(f'{self.name} farm has {self.animals} in quantity of{self.quantity} E-I-E-I-0!')
macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)


print(macdonald.get_info())

# 5. Test your code and make sure you get the same results as the example above.

# 6. Bonus: nicely line the text in columns as seen in the example above. Use string formatting.

# Expand The Farm
# *Add a method called get_animal_types to the Farm class. This method should return a sorted 
#     list of all the animal types (names) in the farm. With the example above, 
#     the list should be: ['cow', 'goat', 'sheep'].

# *Add another method to the Farm class called get_short_info. This method should return the 
#     following string: “McDonald’s farm has cows, goats and sheep.”. The method should call 
#     the get_animal_types function to get a list of the animals.