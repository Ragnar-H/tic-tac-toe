# coding=utf-8
import random
print("Let's play a game.\n")

BOARD = []


def game_loop():
    # The game should run until we return
    game_turn = 0
    no_player = player_setting()

    create_board()
    while True:
        print_board()

        # who's turn is it
        current_player = get_current_player(game_turn)
        print("It is " + current_player + "'s turn\n")

        if no_player == 0:
            coordinates = ai_coordinates()
        elif no_player == 1 and current_player == "O":
            print("Computers turn")
            coordinates = ai_coordinates()
        else:
            coordinates = player_coordinates()

        place_token(current_player, coordinates[0], coordinates[1])

        if did_win(current_player):
            print('{} has won the game 🏅'.format(current_player))
            print_board()
            return

        elif is_board_full(game_turn):
            print("The game is over. No winners!")
            print_board()
            return

        else:
            print("Nobody has won yet, keep looping")
            game_turn += 1


def player_setting():
    player = raw_input("How many players? (0-2)")
    print(player)

    while not is_valid_input(player, 0, 2):
        player = raw_input("Please choose between 1 and 2 players?")

    player = int(player)
    return player


def create_board():
    # create the board
    size = raw_input("What size should the game be? (3-5): ")
    while not is_valid_input(size, 3, 6):
        size = raw_input("What size should the game be? (3-5): ")

    size = int(size)

    for i in range(size):
        BOARD.append([])
        for j in range(size):
            BOARD[i].append('_')


def print_board():
    for row in BOARD:
        print(row)


def get_current_player(num):
    if num % 2 == 0:
        return "X"
    else:
        return "O"


def player_coordinates():
    x_coord = raw_input('which column\n')
    while not is_valid_input(x_coord):
        x_coord = raw_input('please select a valid column?\n')
    y_coord = raw_input('which row?\n')
    while not is_valid_input(y_coord):
        y_coord = raw_input('please select a valid row?\n')

    # We know this is a valid input
    # Lets cast it to Int before we return it
    x_coord = int(x_coord)
    y_coord = int(y_coord)
    return [x_coord, y_coord]


def is_valid_input(input, min, max):
    if not input.isdigit():
        return False
    # Note the int(coordinate).
    # We need to cast to Int before
    if not int(input) in range(min, max):
        return False

    # All is well
    return True


def place_token(token, x_coord, y_coord):
    BOARD[x_coord][y_coord] = token


def did_win(player):
    player_has_won = False

    '#test rows'
    for row in BOARD:
        if same_token_in_row(player, row):
            player_has_won = True

    '#test column'
    for i in range(len(BOARD)):
            column = []
            for x in BOARD:
                column.append(x[i])
            if same_token_in_row(player, column):
                player_has_won = True

    '#test diagonal'
    x_test2 = []
    y_test2 = []
    for i in range(len(BOARD)):
        x_test = BOARD[i]
        x_test2.append(x_test[i])

        y_test = BOARD[i]
        y_test2.append(y_test[-(i+1)])

    if same_token_in_row(player, x_test2) or same_token_in_row(player, y_test2):
        player_has_won = True

    return player_has_won


def same_token_in_row(player, row):
    tokens_in_row = 0

    for y in row:
        if y == player:
            tokens_in_row += 1

    return tokens_in_row == len(row)


def is_board_full(game_turn):
    return game_turn == len(BOARD)**2


def is_legal_move(token, x_coord, y_coord):
    tic = BOARD[x_coord][y_coord]

    if tic == ' X ' or tic == ' O ':
        return False
    else:
        return True


def ai_coordinates():
    x_coord = random.randint(0, len(BOARD)-1)
    y_coord = random.randint(0, len(BOARD)-1)

    while not is_legal_move(x_coord, y_coord):
        x_coord = random.randint(0, len(BOARD)-1)
        y_coord = random.randint(0, len(BOARD)-1)

    return [x_coord, y_coord]
# Run the program
game_loop()
