# Exercise 1 : Pets

# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Garfield(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# cat1 = Bengal('Furball', 1)
# cat2 = Cat('Tom', 2)
# cat3 = Cat('Tiger', 3)
# my_cats = [(cat1), (cat2), (cat3)]
# my_pets = Pets(my_cats)
# my_pets.walk()

# Exercise 2 : Dogs

# Create 3 dogs and run them through your class.

# class Dog:
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight

#     def bark(self):
#         print(f'{dog_name} is barking')

#     def run_speed(self):
#         running_speed = round(self.weight/self.age*10)
#         print(f' {self.name}\'s running speed is {running_speed}')
#         return running_speed

#     def fight(self, other_dog):
#         if other_dog[1] > self.run_speed():
#             print(f'{other_dog[0]} is the winner')
#         else:
#             print(f'{self.name} is the winner')


# ralph = Dog("Ralph", 5, 400)
# skipper = Dog('Skiper', 6, 300)
# ralph.run_speed()
# skipper.run_speed()
# skipper.fight([ralph.name, ralph.run_speed()])
# ralph.fight([skipper.name, skipper.run_speed()])

# Exercise 3 : Dogs Domesticated
# Instructions

# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other dogs (use *args). 
# The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.

# from dog import Dog

# def PetDog(Dog):
#     def __init__(self, name, age, weight, trained=False):
#         super().__init__(self, name, age, weight)
#         self.trained = trained
#     def train(self):
#         self.bark()
#         self.trained = True
#     def play(self, *agrs):
#         d_name = self.name
#         for d_name in args:
#             print(d_name)
#     def play(self, *agrs):
#         test = self.name
#         for test in agrs:
#             print(test)

# ralph = Dog("Ralph", 5, 400)
# skipper = Dog('Skiper', 6, 300)
# # def names(*agrs):
# #     for name in agrs:
# #         print(name)

# play()
# Add the following methods:
#     -train: prints the output of bark and switches the trained boolean to True

#     -play: takes a parameter which value is a few names of other dogs (use *args). 
#      The method should print the following string: “dog_names all play together”.    
#