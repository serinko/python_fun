"""See if your birthday is in Pi number"""

filename = 'pi_milion_decimals.txt'
with open(
        filename
) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Hello. \nDo you think your birthday is in the first 1000000 "
                 "decimals of Pi number?\n\n"
                 "Enter your birthday in the form ddmmyy: ")
if birthday in pi_string:
    print(
        "\nYour birthday appears in the first milion digits of pi!"
    )

else:
    print("\nIt seems it does not. Have a great day")
