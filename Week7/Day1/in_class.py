import random
import json
class Personna:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.strength = self.roll_dice()
        self.dexterity = self.roll_dice()
        self.constitution = self.roll_dice()
        self.intelligence = self.roll_dice()
        self.wisdom = self.roll_dice()
        self.charisma = self.roll_dice()
    @staticmethod
    def roll_dice():
        """rolling four 6-sided dice and return 
        the sum of the largest three dice"""
        rolled_numbers = []
        for number in range(0,4):
            rolled_numbers.append(random.randint(1,6))
        rolled_numbers.remove(min(rolled_numbers))
        return sum(rolled_numbers)
    def __repr__(self):
        return self.name
class Game():
    def __init__(self):
        self.num_of_players = int(input('how many players are playing?'))
        self.players = []
        for num in range(1, self.num_of_players + 1):
            print(f'______enter info for character #{num}______')
            self.add_player()
            print('\n')
    def add_player(self):
        name = input('Whats your characters name?')
        age = input('how old is your character?')
        player = Personna(name,age)
        self.players.append(player)
    def write_to_txt(self):
        write_string = f'''D&D char sheet
            total palyers: {len(self.players)}
            '''
        for index, player in enumerate(self.players):
            add_string = f'''
            ____ personna #{index+1} ____
            age: {player.age}
            name:{player.name}
            strength:{player.strength}
            dexterity:{player.dexterity}
            constitution:{player.constitution}
            intelligence:{player.intelligence}
            wisdom:{player.wisdom}
            charisma:{player.charisma}
            '''
            write_string += add_string
        with open('game_txt.txt', 'w') as f:
            f.write(write_string)
    def write_to_json(self):
        pass
g1 = Game()