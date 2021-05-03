# Exercise 1: Cats
# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. 
# Use the function previously created.

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# def oldest_cat(cat_list):
#     oldest_current_cat = cat_list[0]
#     for cat in cat_list:
#         if cat.age > oldest_current_cat.age:
#             oldest_current_cat = cat
#     return cat

# cat1 = Cat('Felix', 3)
# cat2 = Cat('Tom', 75)
# cat3 = Cat('Garfield', 42)
# all_cats = [cat1, cat2, cat3]
# oldest = oldest_cat(all_cats)
# print(f'The oldest cat is {oldest.name}, and is {oldest.age} years old.')

# Exercise 2 : Dogs

# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#     def bark(self):
#         print(f'{self.name} goes woof!')
#     def jump(self):
#         x= self.height*2
#         print(f'{self.name} jumps {x}')

# davids_dog = Dog("Rex", 50)
# print(davids_dog.name, davids_dog.height)
# davids_dog.bark()
# davids_dog.jump()

# Exercise 3 : Who’s The Song Producer?

# class Song():
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#     def sing_me_a_song(self):

        # for i in self.lyrics:
        #     for line in self.lyrics:
        #         print(line)

# lyric1 = Song(["There\'s a lady who\'s sure","all that glitters is gold", "and she\'s buying a stairway to heaven"])
# lyric1.sing_me_a_song()

# Exercise 4 : Afternoon At The Zoo

# class Zoo:
#     def __init__(self, zoo_name):
#         self.name = zoo_name
#         self.animals = []

#     def add_animal(self, new_animal):
#         if new_animal not in self.animals:
#             self.animals.append(new_animal)
#         print(self.animals)

#     def get_animals(self):
#         print(f'Number of animals is: {self.animals}')
    
#     def sell_animal(self, animal_sold):
#         self.animals.remove(animal_sold)

#     def sort_animals(self):
#         self.animals.sort()

#     def get_groups(self):
#         print(self.animals)


# ramat_gan = Zoo("London")
# ramat_gan.add_animal('Tiger')
# ramat_gan.add_animal('Sheep')
# ramat_gan.add_animal('Cat')
# ramat_gan.sell_animal('Tiger')
# ramat_gan.sort_animals()
# ramat_gan.get_groups()

# ***************************************************************
# *****CHAIM YOU ARE A LEGEND THANKS FOR EVERYTHING YOU DO!******
# ***************************************************************