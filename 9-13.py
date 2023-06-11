from random import randint

class Die:
    def __init__(self):
        self.sided = 6

    def roll_die(self):
        number = randint(1,self.sided)
        print(number)
die1 = Die()
die1.roll_die() 