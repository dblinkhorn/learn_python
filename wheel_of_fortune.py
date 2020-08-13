# wheel of fortune

import random
import time
import sys


# function that resets player winnings to $0
def bankrupt():
    print("\n    You have now have \033[1m$0\033[0m. Better luck next spin!")
    global player_money
    player_money = 0

# variable to keep track of already-guessed letters
global used_letters
used_letters = []


# function to spin the wheel
def spin_wheel():
    print("\nSpinning...\n")

    # adds a two second delay for dramatic anticipation!
    time.sleep(2)

    # variable spin set to a random value from wheel dictionary
    spin = random.choice(list(wheel.values()))

    # if wheel lands on bankrupt, player losses all their money
    if spin == "BANKRUPT":
        print("    Sorry, the wheel landed on: \033[1mBANKRUPT!\033[0m")
        bankrupt()
        # return None to get out of function and bring back main menu
        return

        # Below, "\033[1m" starts bold text in the terminal, "\033[0m" finishes it
    print(f"    The wheel landed on: \033[1m${spin}\033[0m.\n")

    # guess consonant / buy vowel menu loop
    check_input = True
    while check_input:
        try:
            # spin menu
            spin_choice = int(input("Would you like to:\n"
                           "1. Guess a consonant\n"
                           "2. Buy a vowel (Cost: $500)\n"
                           "\nEnter '1' or '2': "))

            if spin_choice == 1:
                # loop to check consonant input
                consonant_prompt = True
                while consonant_prompt:
                    guess = input("Enter a consonant to guess: ").upper()
                    if guess not in consonants:
                        print("\n    You must enter a consonant. Please try again.\n")
                        continue
                    # checks to see if consonant has already been used
                    elif guess in used_letters:
                        print("\n    You have already used that letter. Please try again.\n")
                        continue
                    elif guess not in used_letters:
                        used_letters.append(guess)
                        consonant_prompt = False
                        check_input = False
            if spin_choice == 2:
                # loop to check vowel input
                vowel_prompt = True
                while vowel_prompt:
                    guess = input("Enter a vowel to guess: ").upper()
                    if guess not in vowels:
                        print("\n    You must enter a vowel. Please try again.\n")
                        continue
                    #checks to see if vowel has already been used
                    elif guess in used_letters:
                        print("\n    You have already used that letter. Please try again.\n")
                        continue
                    elif guess not in used_letters:
                        used_letters.append(guess)
                        vowel_prompt = False
                        check_input = False

            # if user choice neither 1 or 2 then raise error message
            elif spin_choice not in (1, 2):
                print("\n    Invalid selection. Enter '1' or '2'.\n")
                continue

        except ValueError or TypeError:
            print("\n    Invalid selection. Enter a '1' or '2'.\n")
            continue

    # if user input passes all tests above, change it to valid_input
    valid_guess = guess

    # variable to store count of guessed letters in phrase
    number_correct = secret_phrase.count(valid_guess)

    # if statements to reveal success of user letter
    if number_correct > 1:
        print(f"\n    Congratulations! There are \033[1m{number_correct}\033[0m {valid_guess.upper()}'s" + " in the "
                                                                                                       "phrase.")
    elif number_correct == 0:
        print(f"\n    Sorry, there are no {valid_guess.upper()}'s in the phrase.")
    else:
        print(f"\n    Congratulations! There is \033[1m{number_correct}\033[0m {valid_guess.upper()}" + " in the phrase.")

    # adjusts player money variable to award winnings
    global player_money
    # winnings equals spin value times number of guessed letters in phrase
    player_money = player_money + (spin * number_correct)
    # tell user how much they won this round and current total winnings
    print(f"\n    You won ${spin * number_correct} this round. You now have \033[1m${player_money}\033[0m total.")


# function to display main menu of game
def main_menu():
    # loop to check main menu input
    while True:
        try:
            # main menu
            menu_choice = int(input("\nWould you like to:\n"
                               "1. Spin the wheel\n"
                               "2. Exit the game\n"
                               "\nEnter '1 or '2': "))
            if menu_choice == 1:
                spin_wheel()
            # exits the game
            elif menu_choice == 2:
                print("\n    Thank you for playing! Goodbye.")
                sys.exit()
            else:
                print("\n    Invalid selection. Enter '1' or '2'.")
                continue
        except ValueError:
            print("\n    Invalid selection. Enter '1' or '2'.")
            continue

# variable to store current player winnings
player_money = 0

# dictionary to store each slice of the wheel
wheel = {
    "Bankrupt": "BANKRUPT",    # a function that removes all the player's money
    "$100": 100,
    "$200": 200,
    "$300": 300,
    "$400": 400,
    "$500": 500,
    "$600": 600,
    "$700": 700,
    "$800": 800,
    "$900": 900,
    "$1000": 1000,
    "$2000": 2000
}

# variables set to contain all possible letters
# each list used to validate user input in spin_wheel()
consonants = list("BCDFGHJKLMNPQRSTVWXYZ")
vowels = list("AEIOU")

# current secret phrase
secret_phrase = "TESTING"

# welcome message/program title
print("\nWelcome to the WHEEL OF FORTUNE!\n")

# begins the game by executing the main menu
main_menu()

# spins the wheel!
spin_wheel()