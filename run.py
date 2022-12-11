from random import randint

HIDDEN_BOARD = [[' ']*7 for x in range(6)]
GUESS_PATTERN = [[' ']*7 for x in range(6)]
let_to_nums={'A': 0,'B': 1, 'C': 2,'D': 3,'E': 4,'F': 5,'G': 6}


def input_details():
    """
    This function allows the user/player to enter a username.
    Inspired by Love Sandwiches CI project.
    """
    print('Please enter your username.')
    print('username must not contain numbers or/and special characters')
    print('Must be no longer than 6 characters')
    print("Example: Neocal etc.....\n")

    input("Enter your username here:\n")


input_details()