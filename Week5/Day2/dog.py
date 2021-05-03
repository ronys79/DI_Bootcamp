class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print(f'{dog_name} is barking')

    def run_speed(self):
        running_speed = round(self.weight/self.age*10)
        print(f' {self.name}\'s running speed is {running_speed}')
        return running_speed

    def fight(self, other_dog):
        if other_dog[1] > self.run_speed():
            print(f'{other_dog[0]} is the winner')
        else:
            print(f'{self.name} is the winner')