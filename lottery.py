# Loading the lowercase alphabet to a list
from string import ascii_lowercase
from random import choice

alphabet = list(ascii_lowercase)
numbers = []
for i in range(1, 11):
    numbers.append(str(i))
pool = alphabet[:6] + numbers

print(
    "\n\nWELCOME TO THE LOTTERY!"
    "\nHere is a pool of 5 letters and 10 numbers, "
    "please choose 4 from this pool:  \n"
)

pool_strings_formatted = ', '.join(pool)

print(pool_strings_formatted)

print(
    "\nPlease choose a mix of 4 numbers or letters :"
)
prompt = "\nYOUR GUESS: "
prompt += "\n(prees enter after each one letter or number you enter):\t"

guess = []

for x in range(0, 4):
    x = input(prompt)
    guess.append(str(x))

guess_formatted = ', '.join(guess)

print(f"\n\nYour guess is: {guess_formatted}.")
enter = input("\n Press ENTER to see the results!")

lottery = []

for x in range(0, 4):
    x = choice(pool)
    lottery.append(x)

lottery_formatted = ', '.join(lottery)

print(
    f"\n------------------------------------\n"
    f"Here are the results of today lottery:\n\n\n"
    f"    - - - {lottery_formatted} - - - \n\n"
)

lost = []
for x in guess:
    if x not in lottery:
        print(f"Your guess {x} is not a winning one.")
        lost.append(x)

if lost:
    print(
        "\nYou did not win the lottery, but do not worry. "
        "There is so much richness in the life itself. "
        "Have a good day! "
    )
else:
    print("\n\n! ! ! ! !    Y O U   W O N    ! ! ! ! !\n\n\n")
