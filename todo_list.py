# to-do list

import sys

# variable to store to-do's as a list
todos = []


# function to add a new to-do
def add_todo(todos):
    new_todo = input("\nEnter new to-do: ")
    todos.append(new_todo)
    show_todos(todos)


# function to validate user input
def validate_input(user_action):
    valid_input = False
    while not valid_input:
        try:
            todo_selection = int(input(f"\nEnter the to-do to {user_action}: "))
            if todo_selection > len(todos) or todo_selection < 1:
                print("\nYou must enter a valid to-do number. Please try again.")
                continue
        except ValueError or IndexError:
            print("\nYou must enter a valid to-do number. Please try again.")
        else:
            valid_input = True
    return todo_selection


# function to confirm user choice, "edit" parameter is a conditional to control whether a message below gets printed.
def confirm_choice(proposed_action, no_message, yes_message=None, edit=False):
    confirmed = False
    while not confirmed:
        confirm = input(f"\nAre you sure you want to {proposed_action}? Type (Y)es or (N)o: ")
        while confirm.upper() not in ('Y', 'N'):
            print("\nInvalid selection. Please try again.")
            break
        if confirm.upper() == "Y":
            if edit is False:
                print(f"\n{yes_message}")
                confirmed = True
            elif edit is True:
                confirmed = True
        elif confirm.upper() == "N":
            print(f"\n{no_message}")
            confirmed = False
            break
    return confirmed


# function to edit an existing to-do
def edit_todo(todos):
    show_todos(todos)
    if todos:
        edit_selection = validate_input("edit")
        confirmed = confirm_choice("edit this to-do", "To-do was NOT edited.", None, True)
        # in confirmed variable, if confirm_choice function returned true, edit to-do
        if confirmed:
            todos[edit_selection-1] = str(input("\nNew text of to-do: "))
            show_todos(todos)


# function to delete an existing to-do
def delete_todo(todos):
    show_todos(todos)
    delete_selection = validate_input("delete")
    confirmed = confirm_choice("delete this to-do", "To-do NOT deleted.", "To-do DELETED.", False)
    # in confirmed variable, if confirm_choice function returned true, delete to-do
    if confirmed:
        todos.remove(todos[delete_selection-1])
    show_todos(todos)


# function to display all to-do's
def show_todos(todos):
    # prints a message if there are no to-do's
    if not todos:
        print("\nThere are currently no to-do's.")
    else:
        print("\nCurrent To-Do's:\n"
              "----------------")
        for todo in range(len(todos)):
            print(str(todo+1) + ". " + str(todos[todo]))


def menu_quit(self):
    invalid_input = True
    while invalid_input:
        confirmed_choice = input("\nAre you sure you want to quit? Type (Y)es or (N)o: ")
        while confirmed_choice.upper() not in ('Y', 'N'):
            print("\nInvalid selection. Please try again.")
            break
        if confirmed_choice.upper() == "Y":
            print("\nGoodbye!")
            sys.exit()
        elif confirmed_choice.upper() == "N":
            invalid_input = False


# program title/heading
print("\n---------------------\n"
      "| Python To-Do List |\n"
      "---------------------"
      )

# variable to store menu text
menu = ("\nMenu Options\n"
        "------------\n"
        "(A)dd a to-do\n"
        "(E)dit a to-do\n"
        "(D)elete a to-do\n"
        "(S)how all to-do's\n"
        "(Q)uit program"
        )

# dictionary to store menu options
menu_dict = {"A": add_todo,
             "E": edit_todo,
             "D": delete_todo,
             "S": show_todos,
             "Q": menu_quit
             }

# loop to keep program running
continue_program = True
while continue_program:

    print(menu)

    invalid_menu = "\nInvalid selection. Please try again."

    valid_menu = False
    while valid_menu == False:
        # variable to store user menu selection
        menu_action = input("\nSelect a menu option: ")

        if menu_action.upper() in ('A', 'E', 'D', 'S', 'Q'):
            break
        else:
            print(invalid_menu)

    menu_selection = menu_dict.get(menu_action.upper(), invalid_menu)

    # calls function by using [menu_action] as the key value from the menu_dict and (todos) as the argument
    menu_selection(todos)
