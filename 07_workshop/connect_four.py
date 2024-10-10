def print_field(matrix):
    for line in matrix:
        print(line)
    print(f'\n')


def check_for_winner(matrix, starting_row_i, starting_col_i, current_player):
    symbol_counter = 1
    direction_mapper = ((-1, 0),  # UP
                        (-1, 1),  # UPRIGHT
                        (0, 1),  # RIGHT
                        (1, 1)  # DOWNRIGHT
                        )
    # Direction from mapper:
    for direction in direction_mapper:
        for row in range(ROWS):
            try:
                moving_row_index = starting_row_i
                moving_col_index = starting_col_i
                next_position = matrix[moving_row_index + direction[0]][moving_col_index + direction[1]]
                if next_position == current_player:
                    symbol_counter += 1
                    starting_row_i += direction[0]
                    starting_col_i += direction[1]
                    if symbol_counter == 4:
                        print(f'Player {player} wins')
                else:
                    break
            except IndexError:
                break
        # Opposite direction:
        for row in range(ROWS):
            try:
                moving_row_index = starting_row_i
                moving_col_index = starting_col_i
                next_position = matrix[moving_row_index - direction[0]][moving_col_index - direction[1]]
                if next_position == current_player:
                    symbol_counter += 1
                    starting_row_i -= direction[0]
                    starting_col_i -= direction[1]
                    if symbol_counter == 4:
                        print(f'Player {player} wins')
                else:
                    break
            except IndexError:
                break
        symbol_counter = 1


def filling_the_field(matrix, current_player, chosen_column):
    for row in range(ROWS, 0, -1):
        row_index = row - 1
        col_index = chosen_column - 1
        if matrix[row_index][col_index] == 0:
            matrix[row_index][col_index] = current_player
            check_for_winner(matrix, row_index, col_index, current_player)
            return True
    return False


# FIELD SIZE:
ROWS = 4
COLS = 4
field = [[0 for _ in range(COLS)] for sublist in range(ROWS)]

player = 1
while True:
    column = input(f'Player {player} choose a column: ')
    column = int(column)
    if column > COLS or column < 1:
        print("Chosen column out of range!")
        continue
    if not filling_the_field(field, player, column):
        continue

    print_field(field)
    player += 1
    player = 1 if player % 2 == 1 else 2
