import random
cpu_score = 0
user_score = 0

class Game():

    def __init__(self):
        self.user_choice = ""
        self.cpu_choice = ""
        self.cpu_score = 0
        self.user_score = 0
 
    def get_user_item(self):
        active = True
        while active:
            self.user_choice = input("Select (r)ock or (p)aper or (s)cissors")
            self.user_choice.lower()
            if self.user_choice == "r" or self.user_choice == "p" or self.user_choice == "s":
                # funct 
                active=False

    def get_cpu_choice(self):
        cpu_choice = ["r", "p", "s"]
        self.cpu_choice = random.choices(cpu_choice, k = 1)
        self.cpu_choice = ''.join(self.cpu_choice)
        return cpu_choice

    def get_game_result(self, user_choice, cpu_choice):
        if self.user_choice == 'r':
            if self.cpu_choice == 'r':
                print('Its a tie!')
            elif self.cpu_choice == 's':
                self.user_score +=1
                print('You WIN!')
            else:
                self.cpu_score += 1
                print('You lost!')

        elif self.user_choice == 'p':
            if self.cpu_choice == 'p':
                print('Its a tie!')
            elif self.cpu_choice == 'r':
                self.user_score +=1
                print('You WIN!')
            else:
                print('You lost!')
                self.cpu_score += 1

        elif self.user_choice == 's':
            if self.cpu_choice == 's':
                print('Its a tie!')
            elif self.cpu_choice == 'p':
                self.user_score +=1
                print('You WIN!')
            else:
                print('You lost!')
                self.cpu_score += 1
        return 

game1= Game()
game1.get_user_item()
game1.get_cpu_choice()
print(game1.user_choice)
print(game1.cpu_choice)
game1.get_game_result(game1.user_choice, game1.cpu_choice)
print(game1.cpu_score)
print(game1.user_score)

# play(self) – the function that will be called from outside the class (ie. from rock-paper-scissors.py). It will do 3 things:
# Get the user’s item (rock/paper/scissors) and remember it

# Get a random item for the computer (rock/paper/scissors) and remember it

# Determine the results of the game by comparing the user’s item and the computer’s item
# Print the output of the game; something like this: “You selected rock. The computer selected paper. You lose”, 
# “You selected scissors. The computer selected scissors. You drew!”

# Return the results of the game as a string: win;draw;loss;, where win means that the user has won, draw means the user 
# and the computer got the same item, and loss means that the user has lost.