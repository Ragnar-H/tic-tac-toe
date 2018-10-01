def game_loop():
    # The game should run until we return
    while True:
        print_board()

        current_player = get_current_player()

        coordinates = get_coordinates()

        place_token(current_player, coordinates[0], coordinates[1])

        if did_win(current_player):
            print('{} has won the game 🏅'.format(current_player))
            return

        elif is_board_full():
            # Game over baby
            print('The board is full and nobody won')
            return
        else:
            print("Nobody has won yet, keep looping")


BOARD = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]


def print_board():
    for row in BOARD:
        print(row)


def get_current_player():
    raise NotImplementedError


def get_coordinates():
    raise NotImplementedError


def place_token(token, x_coord, y_coord):
    raise NotImplementedError


def did_win(player):
    raise NotImplementedError


def is_board_full():
    raise NotImplementedError


def is_legal_move(token, x_coord, y_coord):
    raise NotImplementedError


# Run the program
game_loop()
