import random


# Welcome the user.
print("""
#================================#
| Welcome to  SHOOT  DICE!!!     |
| If u wanna try press 1 or if   |
| you're afraid of losing press 2|
#================================#
""")


# Ask the user to enter the data.
user_result = int(input('Put 1 2 3 4 5 6 or 0 for exit (^-^): '))


# Starts the game cycle.
while user_result != 0:
    comp_result = random.randint(1, 7)
    if user_result == comp_result:
        print('are you winning!')
        user_result = int(input('Put 1 2 3 4 5 6 or 0 for exit (^-^): '))
    elif user_result != comp_result:
        print("are you loser")
        user_result = int(input('Put 1 2 3 4 5 6 or 0 for exit (^-^): '))
