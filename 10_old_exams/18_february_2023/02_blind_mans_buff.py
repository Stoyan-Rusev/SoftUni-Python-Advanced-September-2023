ROWS, COLS = [int(x)for x in input().split(' ')]

b_position = None
field = []
for i in range(ROWS):
    line = input().split()
    field.append(line)
    if 'B' in line:
        b_position = (i, line.index('B'))
        field[i][line.index('B')] = '-'

print(f'Starting position: {b_position}')
for sublist in field:
    print(sublist)
print()

direction_mapper = {'up': (-1, 0),
                    'down': (1, 0),
                    'left': (0, -1),
                    'right': (0, 1)
                    }


def is_next_move_valid(current_position, current_direction, rows, cols):
    next_b_row = current_position[0] + direction_mapper[current_direction][0]
    next_b_col = current_position[1] + direction_mapper[current_direction][1]
    if 0 <= next_b_row < rows and 0 <= next_b_col < cols:
        return True
    return False


moves_made = 0
touched_players = 0
while True:
    direction = input()
    if direction == 'Finish':
        break
    if not is_next_move_valid(b_position, direction, ROWS, COLS):
        continue
    next_row = b_position[0] + direction_mapper[direction][0]
    next_col = b_position[1] + direction_mapper[direction][1]
    if field[next_row][next_col] == 'O':
        continue
    elif field[next_row][next_col] == '-':
        moves_made += 1
    elif field[next_row][next_col] == 'P':
        touched_players += 1
        moves_made += 1
        field[next_row][next_col] = '-'
        if touched_players == 3:
            break
    b_position = (next_row, next_col)
    print(f'Current position: {b_position}')
    print(f'Moves: {moves_made}, Touched players: {touched_players}')
    for sublist in field:
        print(sublist)
    print()

print(f'Game over!\nTouched opponents: {touched_players} Moves made: {moves_made}')
