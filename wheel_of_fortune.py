# wheel of fortune program

# Musts:
# 1. Take user input and compare it to the secret phrase
# 2. Select a random wheel slice from the wheel
# 3. Keep track of total player money
# 4. Player must be able to buy vowels
# 5. Player must be able to guess the secret phrase at any time
# 6. Award player money based on number of correct letters in secret phrase and wheel slice value

import random
import time
import sys


# function that resets player_money to zero
def bankrupt():
    global player_money
    player_money = 0
    return player_money


# function that checks to see if the player already used a letter
def letter_check(letter):
    global consonants
    global vowels
    while True:
        if letter in list("ABCDEFGHIJKLMNOPQRSTUVWYX"):
            if letter in consonants:
                try:
                    consonants.remove(letter)
                    return letter
                    break
                except ValueError:
                    pass
            elif letter in vowels:
                try:
                    vowels.remove(letter)
                    return letter
                    break
                except ValueError:
                    pass
            else:
                print("\n    You have already used that letter. Please try again.\n")
                break
        else:
            print("\n    Invalid selection. Please try again.\n")
            break



# function to spin the wheel
def spin_wheel():
    print("\nSpinning...\n")
    #time.sleep(2)

    # variable spin set to a random value from wheel dictionary
    spin = random.choice(list(wheel.values()))
    # Below, "\033[1m" starts bold text in the terminal, "\033[0m" finishes it
    print(f"    The wheel landed on: \033[1m${spin}\033[0m.\n")
    while True:
        spin_choice = int(input("Would you like to:\n"
                       "1. Guess a consonant\n"
                       "2. Buy a vowel (Cost: $500)\n"
                       "\nSelect an action above: "))

        while spin_choice not in (1, 2):                            # FIX THIS, needs to re-execute spin choice prompt
            print("    Invalid selection. Please try again.\n")
            break
        if spin_choice == 1:
            guess = input("Enter a consonant to guess: ")
        elif spin_choice == 2:
            guess = input("Enter a vowel to buy: ")

        valid_guess = letter_check(guess.upper())
        if valid_guess is None:
            continue
        else:
            break

    number_correct = secret_phrase.count(valid_guess)
    if number_correct > 1:
        print(f"\n    Congratulations! There are \033[1m{number_correct}\033[0m {valid_guess.upper()}'s" + " in the "
                                                                                                       "phrase.")
    elif number_correct == 0:
        print(f"\n    Sorry, there are no {valid_guess.upper()}'s in the phrase.")
    else:
        print(f"\n    Congratulations! There is \033[1m{number_correct}\033[0m {valid_guess.upper()}" + " in the phrase.")

    global player_money
    player_money = player_money + (spin * number_correct)
    print(f"\n    You won ${spin * number_correct} this round. You now have \033[1m${player_money}\033[0m total.")


# function to display main menu of game
def play_game():
    while True:
        try:
            menu_choice = int(input("\nWould you like to:\n"
                               "1. Spin the wheel\n"
                               "2. Exit the game\n"
                               "\nSelect an action above: "))
            if menu_choice == 1:
                spin_wheel()
            elif menu_choice == 2:
                print("\n    Thank you for playing! Goodbye.")
                sys.exit()
            else:
                print("\n    Invalid selection. Please try again.")
                continue
        except ValueError:
            print("\n    Invalid selection. Please try again.")
            continue

player_money = 0

wheel = {
    "Bankrupt": bankrupt(),    # a function that removes all the player's money
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
# each list used to keep track of already-used letters by letter_check()
consonants = list("BCDFGHJKLMNPQRSTVWXYZ")
vowels = list("AEIOU")

secret_phrase = "TESTING"

print("\nWelcome to the WHEEL OF FORTUNE!\n")

play_game()
spin_wheel()

print(consonants)
print(vowels)