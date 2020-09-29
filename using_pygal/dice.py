from random import randint

class Dice():
    """A class that represents a unique dice"""

    def __init__(self, num_sides=6):
        """Assumes the dice has 6 sides"""
        self.num_sides = num_sides


    def roll(self):
        """Returns a random value between 1 and the number of sides"""
        return randint(1, self.num_sides)
