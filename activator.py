"""A simple program to make a choice of a person for any given activity"""
from random import choice


class Activator:
    """User adds people to the list of"""

    def __init__(self):
        """Initiate atributes"""
        self.user_list = []

    def welcome_message(self):
        """ A simple function to welcome user"""
        message = \
            "\nHello, This program will hellp you to pick a " \
            "'volunteer' for any given activity."

        print(message)

    def add_users(self, users=[]):
        """Prmpts user to add list op people, and returns it."""
        self.user_list = users

        message = \
            "\nFirst of all enter the name of each person you want to choose " \
            "from, to carry a given activity."
        message += \
            "\nAfter each user press 'ENTER'. \nWhen finished, enter 'Q'."
        print(message)

        while True:
            prompt = "\n\nENTER NAME: "
            name = input(prompt)
            if name.lower() == 'q':
                break
            else:
                self.user_list.append(name)
                print(
                    f"=============================\nAdded {name.title()}."
                )
        print(
            "=============================\nThank you. The list of people"
            " was completed:"
        )
        for person in self.user_list:
            print(f"\t- {person.title()}")

        return self.user_list

    def add_activity(self):
        """Prompts user to describe the activity and returns it"""

        message = \
            "\n=============================\n\n\n\n"
        message_2 = "Please enter the activity. " \
                    "Try to describe it in a 3rd person singular, like: " \
                    "'will sing a song' or 'is the reponsible of the day'..."
        print(message)
        print(message_2)

        prompt = "=============================\nACTIVITY: "
        self.activity = input(prompt)

        return self.activity

    def choice(self):
        """Makes a random choice of a person and returns a winner"""
        self.winner = choice(self.user_list)
        return self.winner

    def print_results(self, activity, winner):
        """Displays the result"""
        self.activity = activity
        self.winner = winner

        print(
            "\n============================="
            "\n============================="
        )

        message = \
            f"The winner is ....... \n\n\n  " \
            f"! ! !   {self.winner.upper()}   ! ! ! "
        message_2 = \
            f"\n{self.winner.title()} {self.activity}. Congratulation!" \
            f"\n=============================\n"
        print(message)
        print(message_2)


activator = Activator()
activator.welcome_message()
activator.add_users()
activity = activator.add_activity()
winner = activator.choice()
activator.print_results(activity, winner)
