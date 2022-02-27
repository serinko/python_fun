"""
A simple program to make a user see how many lottery draws would it take,
 for their bet to win.
"""

# Loading the lowercase alphabet to a list
from string import ascii_lowercase
from random import choice

# Found online:
# function to compare lists
# def compare(l1, l2):
#     # here l1 and l2 must be lists
#     if len(l1) != len(l2):
#         return False
#     l1.sort()
#     l2.sort()
#     if l1 == l2:
#         return True
#     else:
#         return False

# # I will not use it, keeping it archived
# # My l1 and l2 len() will be == as it's in the code.


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

count = 0

while sorted(guess) != sorted(lottery):
    while len(lottery) > 0:
        lottery.pop()
    for x in range(0, 4):
        x = choice(pool)
        lottery.append(str(x))
    count += 1  # variable will increment every loop iteration
    lottery_formatted = ' - '.join(lottery)
    print(
        f"Draw number {count}; lottery draw:  {lottery_formatted}. ")

print(
    f"\n------------------------\nYOU FINALLY WON!!!"
    f"\n\nIt took {count} lottery draws for your guess to win.\n\n"
)
