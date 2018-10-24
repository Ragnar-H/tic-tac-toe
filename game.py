# coding=utf-8
def game_loop():
    # The game should run until we return
    game_turn = 0
    while True:
        print_board()

        #who's turn is it
        current_player = get_current_player(game_turn)
        print("It is " + current_player + "'s turn\n")

        coordinates = get_coordinates()

        place_token(current_player, coordinates[0], coordinates[1])

        if did_win(current_player):
            print('{} has won the game 🏅'.format(current_player))
            return

        elif is_board_full(game_turn):
            print("The game is over. No winners!")
            return

        else:
            print("Nobody has won yet, keep looping")
            game_turn += 1


BOARD = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]



def print_board():
    for row in BOARD:
        print(row)


def get_current_player(num):
    if num % 2 == 0:
        return "X"
    else:
        return "O"


def get_coordinates():
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


def is_valid_input(coordinate):
    if not coordinate.isdigit():
        return False
    # Note the int(coordinate).
    # We need to cast to Int before 
    if not int(coordinate) in range(0, len(BOARD)):
        return False

    # All is well
    return True


def place_token(token, x_coord, y_coord):
    BOARD[x_coord][y_coord] = token


def did_win(player):
    player_has_won = False
    for row in BOARD:
        if row[0] == player and row[1] == player and row[2] == player:
            player_has_won = True

    return player_has_won


def is_board_full(game_turn):
    return game_turn == len(BOARD)**2


def is_legal_move(token, x_coord, y_coord):
    # TODO this should probably be used somewhere...
    raise NotImplementedError


# Run the program
game_loop()
