from random import randrange


class Dice:
    """A simple class modeling a dice"""

    def __init__(self, sides=6):
        """Initiates the attributes of a dice."""
        self.sides = sides

    def roll_dice(self):
        """A method randomizing the dice roll"""
        x = randrange(1, 6)
        return x

    def display_result(self):
        """Prints the results."""
        self.x = self.roll_dice()
        message = f"\n\nYour DICE roll result is {self.x}!"
        print(message)


dice = Dice()
dice.roll_dice()
dice.display_result()
