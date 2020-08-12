# random password generator

import random
import sys


# function to check whether user wants different sets of characters to be in the password
def check_options(character_set, set_name):
    # condition to control loop below
    get_option = False
    while not get_option:
        choice = input("\nWould you like to include " + str(set_name) + " in your password? (Y)es or (N)o.: ")
        choice = choice.upper()
        if choice == 'Y':
            characters.extend(character_set)
            get_option = True
        elif choice == 'N':
            get_option = True
        else:
            print("\nPlease type 'Y' or 'N' to confirm.")


# function to check if user wants to generate another password
def check_exit():
    confirmed = False
    while not confirmed:
        confirm = input("\nWould you like to create another password? (Y)es or (N)o).: ")
        while confirm.upper() not in ('Y', 'N'):
            print("\nInvalid selection. Please try again.")
            break
        if confirm.upper() == "Y":
            confirmed = True
        elif confirm.upper() == "N":
            print("\nGoodbye!")
            sys.exit()
    return confirmed


# display program name
print('Random Password Generator')

# while loop to control re-run of program based on user input below
stop_program = False
while not stop_program:

    # define list character-type variables
    characters = list('abcdefghijklmnopqrstuvwxyz')         # "default" character set
    uppercase = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('1234567890')
    specials = list('!@#$%^&*')


    check_options(uppercase, "uppercase letters")
    check_options(numbers, "numbers")
    check_options(specials, "special characters")

    # while loop to control max length of password
    proper_length = False
    while not proper_length:
        try:
            # define variable to store user input
            length = int(input('\nHow many characters would you like your password to contain? (Maximum: 32): '))

            # prompts that user length exceeds maximum
            if length > 32 or length <= 0:
                print('\nThe length must be between 1 and 32. Please specify a lower value.')
            # user input 32 or less so end loop
            elif length <= 32:
                proper_length = True
        except ValueError:
            print("\nPlease enter a number between 1 and 32.")

    # sets password to empty string by default
    password = ''

    # iterate over character set for user input length of password
    for char in range(length):
        # adds a random character from character set to password variable
        password += random.choice(characters)

    print('\n\nYour new password is: \n')

    # displays password to user
    print(password, '\n')

    check_exit()
