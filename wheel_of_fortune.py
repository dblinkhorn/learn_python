# wheel of fortune

import random
import time
import sys

# dictionary to store puzzles for select_puzzle() to choose from
puzzles = {
    1: "TODAY IS THE DAY",
    2: "EVERYONE LOVES PIZZA",
    3: "HAVE ONE ON ME",
    4: "HIDE AND SEEK",
    5: "LET THE FUN BEGIN",
    6: "DEATH AND TAXES",
    7: "TAKE ME TO YOUR LEADER",
    8: "MAN ON THE MOON",
    9: "ONLY TIME WILL TELL",
    10: "HAPPY BIRTHDAY TO YOU"
}


# function that selects a random puzzle from the puzzles dictionary
def select_puzzle(puzzles):
    global puzzle
    global letter_board
    puzzle = random.choice(list(puzzles.values()))

    # list to store blank spaces generated from randomly selected puzzle from puzzles dictionary
    letter_board = []

    # loop to build number of blanks on letter board from selected puzzle
    for character in range(len(puzzle)):
        if puzzle[character] not in " ":
            letter_board.append("_")
        if puzzle[character] in " ":
            letter_board.append(" ")
    return puzzle


# function that resets player winnings to $0
def bankrupt():
    print("\n    You now have \033[1m$0\033[0m. Better luck next spin!")
    global player_money
    player_money = 0


# variable to keep track of already-guessed letters
used_letters = []


# function to reveal successfully guessed letters on letter board
# only accepts already validated guess (letter is in the puzzle)
def reveal_letters(valid_guess):
    # for each hidden letter in the board (number based on characters in puzzle)
    for blank in range(len(letter_board)):
        # if that letter is equal to the player's guess
        if puzzle[blank] == valid_guess:
            # then change that blank to that letter, revealing the successfully guessed letter(s) on the letter board
            letter_board[blank] = valid_guess
    # prints out the letter board and reveals guessed letters
    print("        Current Letters\n"
          "        ---------------")
    print("        ", end="")
    print(*letter_board)


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


# function that controls all of the spin wheel logic
def spin_wheel():
    print("\nSpinning...\n")

    # adds a two second delay for dramatic anticipation!
    time.sleep(2)

    # variable spin set to a random value from wheel dictionary (random wheel slice)
    spin = random.choice(list(wheel.values()))

    # if wheel lands on bankrupt, player losses all their money
    if spin == "BANKRUPT":
        print("    Sorry, the wheel landed on: \033[1mBANKRUPT!\033[0m")
        bankrupt()
        # return None to get out of function and bring back main menu
        return

    # below, "\033[1m" begins bold text in the terminal, "\033[0m" ends it
    print(f"    The wheel landed on: \033[1m${spin}\033[0m.\n")

    # set player_money and used_letters to be preserved outside function scope
    global player_money
    global used_letters

    # guess consonant / buy vowel menu loop
    check_input = True
    while check_input:
        try:
            # spin menu options
            spin_choice = int(input("Choose an action:\n"
                                    "1. Guess a consonant\n"
                                    "2. Buy a vowel (Costs $500)\n"
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
                    # if the consonant hasn't been used then add it to the used_letters now
                    elif guess not in used_letters:
                        used_letters.append(guess)
                        consonant_prompt = False
                        check_input = False
            if spin_choice == 2:
                # checks to make sure user has the $500 to buy a vowel
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
                    # checks to see if vowel has already been used
                    elif guess in used_letters:
                        print("\n    You have already used that letter. Please try again.\n")
                        continue
                    # if the vowels hasn't been used then add it to the used_letters now
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

    # variable to store the count of correctly guessed letters in the puzzle
    number_correct = puzzle.count(valid_guess)

    # if statements to determine the outcome of the user's guess
    if number_correct > 1:
        print(f"\n    Congratulations! There are {str(int_to_str[number_correct])} {valid_guess.upper()}'s" + " in the "
              "puzzle.\n")
    elif number_correct == 0:
        print(f"\n    Sorry, there are no {valid_guess.upper()}'s in the puzzle.\n")
    else:
        print(f"\n    Congratulations! There is {str(int_to_str[number_correct])} {valid_guess.upper()}" + " in the "
              "puzzle.\n")
    reveal_letters(valid_guess)

    # print this if the guess was a consonant
    if valid_guess in consonants:
        # winnings equals wheel slice spin value times the number of correctly guessed letters in the puzzle
        player_money = player_money + (spin * number_correct)
        # tells the user how much they won this round and their current total winnings
        print(f"\n    You won \033[1m${spin * number_correct}\033[0m this round. You currently have \033[1m"
              f"${player_money}\033[0m "
              f"total.")

    # print this if the guess was a vowel
    elif valid_guess in vowels:
        player_money = player_money - 500
        print(f"\n    You purchased the vowel '{valid_guess}' for \033[1m$500\033[0m. You currently have \033[1m"
              f"${player_money}\033[0m total.")


# function to confirm if the user wants to quit
def menu_quit():
    invalid_input = True
    while invalid_input:
        confirmed_choice = input("\nAre you sure you want to quit? Enter (Y)es or (N)o: ")
        while confirmed_choice.upper() not in ('Y', 'N'):
            print("\n    Invalid selection. Enter 'Y' or 'N'.")
            break
        if confirmed_choice.upper() == "Y":
            print("\n    Thank you for playing. Goodbye!")
            sys.exit()
        elif confirmed_choice.upper() == "N":
            invalid_input = False


# function to display the main menu of the game
def main_menu():
    # loop to check the main menu inputs
    main_loop = True
    while main_loop:
        # sets variables player_money and puzzle to be preserved outside of function scope
        global used_letters
        global player_money
        global puzzle
        try:
            # main menu options
            menu_choice = int(input("\nChoose an action:\n"
                                    "1. Spin the wheel\n"
                                    "2. Solve the puzzle\n"
                                    "3. Exit the game\n"
                                    "\nEnter choice: "))
            if menu_choice == 1:
                spin_wheel()
            # logic for user guessing the puzzle
            elif menu_choice == 2:
                puzzle_guess = input("Enter your guess (include spaces, not case-sensitive): ").upper()
                if puzzle_guess == puzzle:
                    print("\n    Congratulations, you solved the puzzle!")
                    player_money += 1000
                    print(f"\n    You won \033[1m$1000\033[0m this round for solving the puzzle and earned a "
                          f"total of \033[1m${player_money}\033[0m this game.")
                    # reset player money for next round
                    player_money = 0
                    # reset used letters for next round
                    used_letters = []

                    # loop to check play again prompt input
                    confirm_replay = True
                    while confirm_replay:
                        # variable to store whether user wants to play another round or quit
                        play_again = input("\nWould you like to play again? Enter (Y)es or (N)o: ").upper()
                        while play_again not in ('Y', 'N'):
                            print("\n    Invalid selection. Enter 'Y' or 'N'.")
                            break
                        # if they want to play another round
                        if play_again == 'Y':
                            # reset the puzzle to a random puzzle from the puzzles dictionary for the new round
                            puzzle = select_puzzle(puzzles)
                            print("\nHere is the next puzzle...\n")
                            # display the new letter board
                            print(*letter_board)
                            # activate the main menu again
                            main_menu()

                        # logic if the user doesn't want to play again
                        if play_again == 'N':
                            check_quit = False
                            while not check_quit:
                                confirm_quit = input("Are you sure you want to quit? Enter (Y)es or (N)o: ").upper()
                                while confirm_quit not in ('Y', 'N'):
                                    print("\n    Invalid selection. Enter 'Y' or 'N'.\n")
                                    break
                                if confirm_quit == 'Y':
                                    print("\n    Thank you for playing. Goodbye!")
                                    sys.exit()

                                # if they say they don't want to quit after all,
                                # then it's as if they had said yes to original prompt to play again
                                # resets the puzzle anew, displays the new letter board, and activates the main menu
                                elif confirm_quit == 'N':
                                    puzzle = select_puzzle(puzzles)
                                    print("\nHere is the next puzzle...\n")
                                    print(*letter_board)
                                    main_menu()

                # if the user's guess is not correct
                elif puzzle_guess != puzzle:
                    print("\n    Sorry, that is not the correct answer.")
                    continue

            # if the user wants to quit
            elif menu_choice == 3:
                menu_quit()

            else:
                print("\n    Invalid selection. Enter '1' or '2'.")
                continue
        except ValueError:
            print("\n    Invalid selection. Enter '1' or '2'.")
            continue


# calls function to select a random puzzle from the puzzles dictionary
select_puzzle(puzzles)

# variable to store current player winnings
player_money = 0

# dictionary to store each slice of the wheel
wheel = {
    # activates a function that resets player's winnings to $0
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
# each list is used to validate the user input in spin_wheel()
consonants = list("BCDFGHJKLMNPQRSTVWXYZ")
vowels = list("AEIOU")

# welcome message/program title
print("\nWelcome to the WHEEL OF FORTUNE!\n")

# explain game rules
print("    RULES\n"
      "    -----\n"
      "    1. You will be awarded the wheel's spin value for each correctly guessed consonant in the puzzle.\n"
      "    2. You may buy a vowel for $500.\n"
      "    3. For each spin of the wheel there is a 1/12 chance of going bankrupt. (Lose all winnings)\n"
      "    4. You may attempt to solve the puzzle at any time. ($1000 bonus if successful)\n"
      "\n    \033[1mGood luck!\033[0m")

# prints blank, unrevealed puzzle for the user
print("\nHere is the puzzle...\n")
print(*letter_board)

# begins the game by executing the main menu
main_menu()

# spins the wheel!
spin_wheel()
