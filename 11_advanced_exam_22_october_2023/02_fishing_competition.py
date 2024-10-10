GOAL_TONS = 20
ROWS = int(input())

ship_position = None
field = []
for i in range(ROWS):
    line = list(input())
    field.append(line)
    if 'S' in line:
        ship_position = [i, line.index('S')]
        field[i][line.index('S')] = '-'


def is_next_move_valid(current_position, current_direction, field_size):
    next_row = current_position[0] + direction_mapper[current_direction][0]
    next_col = current_position[1] + direction_mapper[current_direction][1]
    if 0 <= next_row < field_size and 0 <= next_col < field_size:
        return True
    return False


direction_mapper = {'up': (-1, 0),
                    'down': (1, 0),
                    'left': (0, -1),
                    'right': (0, 1)
                    }

total_catch = 0
is_dead = False
while True:
    direction = input()
    if direction == 'collect the nets':
        break
    if not is_next_move_valid(ship_position, direction, ROWS):
        if direction == 'up':
            ship_position[0] = ROWS - 1
        elif direction == 'down':
            ship_position[0] = 0
        elif direction == 'right':
            ship_position[1] = 0
        elif direction == 'left':
            ship_position[1] = ROWS - 1
    else:
        ship_position[0] += direction_mapper[direction][0]
        ship_position[1] += direction_mapper[direction][1]

    if field[ship_position[0]][ship_position[1]] == 'W':
        is_dead = True
        print(f'You fell into a whirlpool! The ship sank and you lost the fish you caught. '
              f'Last coordinates of the ship: [{ship_position[0]},{ship_position[1]}]')
        break

    elif field[ship_position[0]][ship_position[1]].isdigit():
        current_catch = int(field[ship_position[0]][ship_position[1]])
        total_catch += current_catch
        field[ship_position[0]][ship_position[1]] = '-'

    elif field[ship_position[0]][ship_position[1]] == '-':
        continue

if not is_dead:
    field[ship_position[0]][ship_position[1]] = 'S'
    if total_catch >= GOAL_TONS:
        print('Success! You managed to reach the quota!')
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! "
              f"You need {GOAL_TONS - total_catch} tons of fish more.")

    if total_catch > 0:
        print(f"Amount of fish caught: {total_catch} tons.")

    for sublist in field:
        print(''.join(sublist))
