"""A simple counter tracking your excercising sets"""


# TODO:
# Prompt user to enter name of the excercises
# Promt user how many sets they want to do
# Possibly series of sets - can be as an update
#
# Make a counter based on enter hits
# Print each round count
# Print stop message


class Counter:
    """A simple attempt to modelate a counter"""

    def __init__(self, excercise='', sets=None):
        """Initialize attributes in the given class"""
        self.excercise = excercise
        self.sets = sets

    def welcome_message(self):
        """Displays a welcome message"""
        welcome_message = \
            "\nHello.\nGood to see you excercise today. \
            \nThis simple program will keep track of your sets."
        print(welcome_message)

    def user_input_excercise(self):
        """Prompt user to input excercise"""

        prompt_excercise = \
            "\nPlease enter the excercise you want to keep a track of: "
        self.excercise = input(prompt_excercise)

        for x in range(1, 3):
            if not self.excercise:
                print(
                    "\n\nYour excercise was not defined."
                )
                aaself.excercise = input(prompt_excercise)

        if not self.excercise:
            print(
                "\n\n\n\n   ======\n\nYou failed to add an excercise. "
                "It may be better you don't excercise today."
                "\n\nTry again tomorrow!"
            )
            quit()

        else:
            print(
                f"\nThank you. {self.excercise.title()} added!"
            )

    def user_input_sets(self):
        """Prompt user to input number of sets"""

        prompt_sets = \
            "\nWhat is the target number of your sets today: "

        self.sets = input(prompt_sets)

        for x in range(1, 3):
            try:
                a = int(self.sets)
                if a < 1:
                    print(
                        "\n\nNumber of sets was not defined!."
                    )
                    a = input(prompt_sets)
            except:
                print(
                    "\n\nNumber of sets was not defined!."
                )
                self.sets = input(prompt_sets)

        try:
            a = int(self.sets)
            if a < 1:
                quit()


        except:
            print(
                "\n\n\n\n\t\t"
                "======\n\nYou failed to add a reasonable number. "
                "It may be better you don't excercise today."
                "\n\nTry again tomorrow!"
            )
            quit()

        if int(self.sets) == 1:
            print(
                "Do you really need a set counter for 1 set?"
                "\nAre you sure, you are OK to excercise?"
            )

        elif int(self.sets) > 10:
            print(
                f"The number of sets was set to {self.sets}. "
                f"That's a lot. Don't forget to keep the form."
            )

        else:
            print(
                f"\nThank you. {self.excercise.title()} added."
            )

    def counter(self):
        """Loops through the sets and prints a counting report every loop"""


athlete = Counter()
athlete.welcome_message()
athlete.user_input_excercise()
athlete.user_input_sets()
athlete.counter()
