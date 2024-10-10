ROWS, COLS = [int(x) for x in input().split(',')]

mouse_position = None
message = ''
cheeses = 0
field = []

for i in range(ROWS):
    current_line = list(input())
    field.append(current_line)
    for j, el in enumerate(current_line):
        if el == 'C':
            cheeses += 1
        elif el == 'M':
            mouse_position = (i, j)
            field[i][j] = '*'

direction_mapper = {'up': (-1, 0),
                    'down': (1, 0),
                    'left': (0, -1),
                    'right': (0, 1)
                    }


def locating_next_position(direction_, current_position):
    next_row_index = current_position[0]+direction_mapper[direction_][0]
    next_col_index = current_position[1]+direction_mapper[direction_][1]
    mouse_next_position = (next_row_index, next_col_index)
    return mouse_next_position


def is_next_position_valid(next_position_, rows, cols):
    if 0 <= next_position_[0] < rows and 0 <= next_position_[1] < cols:
        return True
    return False


while True:
    direction = input()
    if direction == 'danger':
        field[mouse_position[0]][mouse_position[1]] = 'M'
        message = 'Mouse will come back later!'
        break

    next_position = locating_next_position(direction, mouse_position)
    if is_next_position_valid(next_position, ROWS, COLS):
        row_index = next_position[0]
        col_index = next_position[1]
        if field[row_index][col_index] == 'C':
            cheeses -= 1
            field[row_index][col_index] = '*'
            if cheeses == 0:
                field[row_index][col_index] = 'M'
                message = 'Happy mouse! All the cheese is eaten, good night!'
                break
        elif field[row_index][col_index] == 'T':
            field[row_index][col_index] = 'M'
            message = 'Mouse is trapped!'
            break
        elif field[row_index][col_index] == '@':
            continue
    else:
        field[mouse_position[0]][mouse_position[1]] = 'M'
        message = 'No more cheese for tonight!'
        break
    mouse_position = next_position

print(message)
for sublist in field:
    print(''.join(sublist))
