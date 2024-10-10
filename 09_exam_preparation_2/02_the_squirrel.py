# A square field
ROWS = int(input())
directions = [el for el in input().split(', ')]

message = ''
hazelnuts_collected = 0
squirrel_position = None
field = []
for i in range(ROWS):
    line = list(input())
    field.append(line)
    if 's' in line:
        squirrel_position = (i, line.index('s'))
        field[i][line.index('s')] = '*'

direction_mapper = {'up': (-1, 0),
                    'down': (1, 0),
                    'left': (0, -1),
                    'right': (0, 1)
                    }


def is_next_move_valid(current_position, direction, field_size):
    next_row = current_position[0] + direction_mapper[direction][0]
    next_col = current_position[1] + direction_mapper[direction][1]
    if 0 <= next_row < field_size and 0 <= next_col < field_size:
        return True
    return False


for current_direction in directions:
    if not is_next_move_valid(squirrel_position, current_direction, ROWS):
        message = 'The squirrel is out of the field.'
        break

    squirrel_row = squirrel_position[0] + direction_mapper[current_direction][0]
    squirrel_col = squirrel_position[1] + direction_mapper[current_direction][1]
    squirrel_position = (squirrel_row, squirrel_col)
    if field[squirrel_row][squirrel_col] == 't':
        message = 'Unfortunately, the squirrel stepped on a trap...'
        break
    elif field[squirrel_row][squirrel_col] == '*':
        continue
    elif field[squirrel_row][squirrel_col] == 'h':
        hazelnuts_collected += 1
        field[squirrel_row][squirrel_col] = '*'
        if hazelnuts_collected == 3:
            message = 'Good job! You have collected all hazelnuts!'
            break
else:
    message = 'There are more hazelnuts to collect.'

print(message)
print(f'Hazelnuts collected: {hazelnuts_collected}')
