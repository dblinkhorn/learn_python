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


# function to reveal successfully guessed letters on game board
def reveal_letters(valid_guess):
    # for each hidden letter in the board (number based on characters in secret_phrase)
    for blank in range(len(board)):
        # if that letter is equal to the player's guess
        if secret_phrase[blank] == valid_guess:
            # then change that blank to that letter, revealing the successful guess on the board
            board[blank] = valid_guess
    # prints out the game board and reveals guessed letters
    print("    Secret Phrase:\n")
    print("    ", end="")
    print(*board)

# dictionary to allow conversion of number_correct (an integer) to a word rather than a numeral
int_to_str = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten"
}


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

    # player money variable to store total player winnings
    global player_money

    # guess consonant / buy vowel menu loop
    check_input = True
    while check_input:
        try:
            # spin menu
            spin_choice = int(input("Choose an action:\n"
                           "1. Guess a consonant\n"
                           "2. Buy a vowel (Cost: $500)\n"
                           "\nEnter choice: "))

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
                if player_money < 500:
                    print("\n    Sorry, you don't have enough money to purchase a vowel yet. Try guessing a consonant "
                                                                                                          "instead.\n")
                    continue
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

            # if user choice neither 1 or 2 then show error message
            elif spin_choice not in (1, 2):
                print("\n    Invalid selection. Enter '1' or '2'.\n")
                continue

        except ValueError or TypeError:
            print("\n    Invalid selection. Enter a '1' or '2'.\n")
            continue

    # if user input passes all tests in spin_wheel(), set as valid_guess
    valid_guess = guess

    # variable to store count of guessed letters in phrase
    number_correct = secret_phrase.count(valid_guess)

    # if statements to reveal success of user letter
    if number_correct > 1:
        print(f"\n    Congratulations! There are {str(int_to_str[number_correct])} {valid_guess.upper()}'s" + "in the "
                                                                                                           "phrase.\n")
    elif number_correct == 0:
        print(f"\n    Sorry, there are no {valid_guess.upper()}'s in the phrase.\n")
    else:
        print(f"\n    Congratulations! There is {str(int_to_str[number_correct])} {valid_guess.upper()}" + " in the "
                                                                                                           "phrase.\n")
    reveal_letters(valid_guess)

    # print this if guess was a consonant
    if valid_guess in consonants:
        # winnings equals spin value times number of guessed letters in phrase
        player_money = player_money + (spin * number_correct)
        # tell user how much they won this round and current total winnings
        print(f"\n    You won ${spin * number_correct} this round. You now have \033[1m${player_money}\033[0m total.")

    # print this if guess was a vowel
    elif valid_guess in vowels:
        player_money = player_money - 500
        print(f"\n    You purchased the vowel '{valid_guess}' for \033[1m$500\033[0m. You now have \033[1m"
              f"${player_money}\033[0m total.")


# function to display main menu of game
def main_menu():
    # loop to check main menu input
    while True:
        try:
            # main menu
            menu_choice = int(input("\nChoose an action:\n"
                               "1. Spin the wheel\n"
                               "2. Exit the game\n"
                               "\nEnter choice: "))
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


# current secret phrase
secret_phrase = "TESTING ONE TWO THREE"

board = []

# loop to build number of blanks from secret_phrase
for character in range(len(secret_phrase)):
    if secret_phrase[character] not in " ":
        board.append("_")
    if secret_phrase[character] in " ":
        board.append(" ")

# variable to store current player winnings
player_money = 0

# dictionary to store each slice of the wheel
wheel = {
    # activates a function that removes all the player's money
    "Bankrupt": "BANKRUPT",
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

# welcome message/program title
print("\nWelcome to the WHEEL OF FORTUNE!\n")

# begins the game by executing the main menu
main_menu()

# spins the wheel!
spin_wheel()