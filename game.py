# coding=utf-8
print("Let's play a game.\n")
BOARD = []


def create_board():
    # create the board
    while size > 3 or size < 5:
        try:
            size = int(input("What size should the game be? (3-5): "))
        except ValueError:
            print("Oops! seems like that is not a number. Try again...")
            continue
        if size < 3 or size > 5:
            print("Oops! seems like those numbers are not within limits. Try again...")
            continue
        break

    for i in range(size):
        BOARD.append([])
        for j in range(size):
            BOARD[i].append('_')


def game_loop():
    # The game should run until we return
    game_turn = 0
    while True:
        print_board()

        # who's turn is it
        current_player = get_current_player(game_turn)
        print("It is " + current_player + "'s turn\n")

        coordinates = get_coordinates()

        place_token(current_player, coordinates[0], coordinates[1])

        print(did_win(current_player))
        if did_win(current_player):
            print('{} has won the game 🏅'.format(current_player))
            return

        elif is_board_full(game_turn):
            print("The game is over. No winners!")
            return

        else:
            print("Nobody has won yet, keep looping")
            game_turn += 1


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

    if tokens_in_row == len(row):
        return True


def is_board_full(game_turn):
    return game_turn == len(BOARD)**2


def is_legal_move(token, x_coord, y_coord):
    # TODO this should probably be used somewhere...
    raise NotImplementedError


# Run the program
create_board()
game_loop()
