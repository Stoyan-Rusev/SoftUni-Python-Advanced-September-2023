size = int(input())
directions = input().split()
field = [[el for el in input().split()] for _ in range(size)]

total_coals = 0
row_position = None
col_position = None
game_ended = False

for index, sublist in enumerate(field):
    if 's' in sublist:
        row_position = index
        col_position = sublist.index('s')
    total_coals += sublist.count('c')

for command in directions:
    if command == 'left':
        if col_position - 1 >= 0:
            col_position -= 1
    elif command == 'right':
        if col_position + 1 < size:
            col_position += 1
    elif command == 'up':
        if row_position - 1 >= 0:
            row_position -= 1
    elif command == 'down':
        if row_position + 1 < size:
            row_position += 1

    if field[row_position][col_position] == 'e':
        print(f"Game over! ({row_position}, {col_position})")
        game_ended = True
        break
    elif field[row_position][col_position] == 'c':
        field[row_position][col_position] = '*'
        total_coals -= 1
        if total_coals == 0:
            print(f'You collected all coal! ({row_position}, {col_position})')
            game_ended = True
            break

if not game_ended:
    print(f'{total_coals} pieces of coal left. ({row_position}, {col_position})')
