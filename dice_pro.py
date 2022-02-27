from random import randrange


class User:
    """User's choice of sides of the dice"""

    def __init__(self, number=6):
        """Initialize the attributes of user number's choice"""
        self.number = number

    def user_choice(self):
        prompt = "\n\nPlease enter the number of sides, your die has."
        prompt += "Then press 'enter' to roll!"
        prompt += "\n\n\nNUMBER OF SIDES:      "
        self.number = input(prompt)
        self.number = int(self.number)
        x = self.number
        return x


class Dice:
    """A simple class modeling a dice"""

    def __init__(self, sides=6):
        """Initiates the attributes of a dice."""
        self.sides = sides

    def roll_dice(self):
        """A method randomizing the dice roll"""
        y = int(self.sides)
        if y <= 1:
            print("\n")
        else:
            x = randrange(1, y)
        return x

    def display_result(self):
        """Prints the results."""
        self.x = self.roll_dice()
        message = f"\n\nYour DICE roll result is {self.x}!"
        print(message)


user = User()
x = user.user_choice()
dice = Dice(x)
if x <= 1:
    print(f"\n\n\nYo! Which die has {x} side?!  WTF!!!")
else:
    dice.roll_dice()
    dice.display_result()
