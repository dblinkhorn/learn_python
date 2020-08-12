# dice roller

import random
import sys

quantity = "\nEnter the number of dice to roll: "
sides = "\nEnter the number of sides the dice will have: "


# function to ensure user input is valid (less than 100 and an integer)
def get_value(prompt):
    # loop to check user input is good
    valid_input = False
    while not valid_input:
        try:
            # variable to store user input
            value = int(input(prompt))
            # checks to make sure input is between 1 and 100
            if value > 100 or value < 1:
                print("\nThe value must be between 1 and 100. Please try again.\n")
                continue
        except ValueError:
            print("\nYou must enter an integer. Please try again.\n")
        else:
            valid_input = True
    return value


# function to control program exit
def check_exit():
    confirmed = False
    while not confirmed:
        confirm = input("\nWould you like to roll again? Enter (Y)es or (N)o.: ")
        while confirm.upper() not in ('Y', 'N'):
            print("\nInvalid selection. Please try again.")
            break
        if confirm.upper() == "Y":
            confirmed = True
        elif confirm.upper() == "N":
            print("\nGoodbye!")
            sys.exit()
    return confirmed


print("\nPython Dice Roller")

# main program loop
while True:

    number_of_dice = get_value(quantity)
    number_of_sides = get_value(sides)
    rolls = []
    print("\nRolling...\n")

    # loop prints number of dice each with a random value within number of sides
    for die in range(number_of_dice):
        rolls.append(random.choice(range(1, number_of_sides+1)))

    total = str(sum(rolls))
    print(*rolls, sep=" + ", end="")
    print(" = " + str(total))

    check_exit()
