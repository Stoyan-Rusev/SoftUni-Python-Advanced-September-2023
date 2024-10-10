ROWS, COLS = [int(x) for x in input().split()]

boy_starting_position = None
field = []
for i in range(ROWS):
    line = list(input())
    field.append(line)
    if 'B' in line:
        boy_starting_position = (i, line.index('B'))

direction_mapper = {'up': (-1, 0),
                    'down': (1, 0),
                    'left': (0, -1),
                    'right': (0, 1)
                    }


def is_next_position_valid(current_position, current_direction, rows, cols):
    next_row_i = current_position[0] + direction_mapper[current_direction][0]
    next_col_i = current_position[1] + direction_mapper[current_direction][1]
    if 0 <= next_row_i < rows and 0 <= next_col_i < cols:
        return True
    return False


message = ''
boy_current_position = boy_starting_position
while True:
    direction = input()
    if not is_next_position_valid(boy_current_position, direction, ROWS, COLS):
        field[boy_starting_position[0]][boy_starting_position[1]] = ' '
        message = 'The delivery is late. Order is canceled.'
        break
    row_i = boy_current_position[0] + direction_mapper[direction][0]
    col_i = boy_current_position[1] + direction_mapper[direction][1]

    if field[row_i][col_i] == '*':
        continue
    elif field[row_i][col_i] == 'P':
        print('Pizza is collected. 10 minutes for delivery.')
        field[row_i][col_i] = 'R'
    elif field[row_i][col_i] == '-':
        field[row_i][col_i] = '.'
    elif field[row_i][col_i] == 'A':
        field[row_i][col_i] = 'P'
        message = 'Pizza is delivered on time! Next order...'
        break
    boy_current_position = (row_i, col_i)

print(message)
for sublist in field:
    print(''.join(sublist))
