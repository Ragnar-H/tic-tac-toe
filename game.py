# coding=utf-8
def game_loop():
    # The game should run until we return
    game_turn = 0
    while True:
        print_board()

        #who's turn is it
        current_player = get_current_player(game_turn)
        print("It is "+ current_player + "'s turn\n")

        coordinates = get_coordinates()

        place_token(current_player, coordinates[0], coordinates[1])

        if did_win(current_player):
            print('{} has won the game 🏅'.format(current_player))
            return

        elif is_board_full(game_turn) == True:
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
    x_coord = raw_input('Choose a column?\n')
    while not x_coord.isdigit():
        x_coord = raw_input('please input an integer?\n')
    while x_coord not in range(0,len(BOARD)):
        x_coord = int(raw_input('please select a valid column?\n'))

    y_coord = raw_input('Choose a row?\n')
    while not y_coord.isdigit():
        y_coord = raw_input('please input an integer?\n')
    while y_coord not in range(0,len(BOARD)):
        y_coord = int(raw_input('please select a valid row?\n'))
    return [x_coord, y_coord]


def place_token(token, x_coord, y_coord):
    BOARD[x_coord][y_coord] = token


def did_win(player):
    player_has_won = False
    for row in BOARD:
        if row[0] == player and row[1] == player and row[2] == player:
            player_has_won = True

    return player_has_won

def is_board_full(game_turn):
    if game_turn == len(BOARD)**2:
        return True
    else:
        return False


def is_legal_move(token, x_coord, y_coord):
    # TODO this should probably be used somewhere...
    raise NotImplementedError


# Run the program
game_loop()
