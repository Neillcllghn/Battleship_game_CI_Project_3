from random import randint

HIDDEN_BOARD = [[' ']*7 for x in range(6)]
GUESS_PATTERN = [[' ']*7 for x in range(6)]
let_to_nums={'A': 0,'B': 1, 'C': 2,'D': 3,'E': 4,'F': 5,'G': 6}


def input_details():
    """
    This function allows the user/player to enter a username.
    Inspired by Love Sandwiches CI project.
    """
    while True:
        print('Please enter your username.')
        print('username must not contain numbers or/and special characters')
        print('Must be no longer than 6 characters')
        print("Example: Neocal etc.....\n")

        username = input("Enter your username here:\n")
        
        if validate_username(username):
            print(f'Hello {username}, Welcome to Battleship Madness!')
            break

def validate_username(values):
    """
    Validate the username being entered. So that it is exactly:
    1. Is 6 characters long.
    2. Contains no numbers or special characters.
    """
    if len(values) < 3 or len(values) > 6:
        print(f"username must be more than 3 and less than 6 characters long, you provided {len(values)}.")
        return False
    elif any(char.isnumeric() for char in values):
        print(f"the username {values} cannot be used, please don't use numbers.")
        return False
    elif not values.isalnum():
        print(f"the username {values} cannot be used, please don't use non-alphabetic characters.")
        return False

    return True

def print_board(board):
    """
    This creates the board.
    Credit for code goes to Knowledge Mavens - 
    How to Code Battleship in Python - Single Player Game.
    """
    print('  A B C D E F G')
    print(' ---------------')
    row_of_numbers = 1
    for row in board:
        print("%d|%s|" % (row_of_numbers, "|".join(row)))
        row_of_numbers += 1

def no_of_ships():
    """
    This is to allow the user to select the number of ships they want.
    Inspired by Knowledge Mavens - 
    How to Code Battleship in Python - Single Player Game.
    """
    ships = input('How many ships do you want to sink? Between 1-6 :\n')
    while not ships.isdigit() or int(ships) < 1 or int(ships) >= 6:
        print(f'You selected invaild {ships} number of ships, please try again')
        ships = input('How many ships do you want to sink? Between 1-6 :\n')
    return int(ships)


def new_game ():
    login_data = input_details()

new_game ()