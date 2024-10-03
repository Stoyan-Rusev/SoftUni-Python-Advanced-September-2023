size = int(input())
bunny_position = []
field = []
for rows in range(size):
    field.append(input().split())
    for cols in range(size):
        if field[rows][cols] == 'B':
            bunny_position = [rows, cols]

directions = {'up': (-1, 0),
              'down': (1, 0),
              'left': (0, -1),
              'right': (0, 1)
              }

best_direction = None
eggs_locations = []
best_eggs_sum = float('-inf')
for direction, value in directions.items():
    current_eggs_location = []
    current_eggs_sum = 0
    bunny_row = bunny_position[0]
    bunny_col = bunny_position[1]
    row_movement = value[0]
    col_movement = value[1]
    while True:
        if 0 <= bunny_row + row_movement < size and 0 <= bunny_col + col_movement < size:
            if field[bunny_row+row_movement][bunny_col+col_movement] != 'X':
                current_eggs_sum += int(field[bunny_row+row_movement][bunny_col+col_movement])
                current_eggs_location.append([bunny_row+row_movement, bunny_col+col_movement])
                bunny_row = bunny_row+row_movement
                bunny_col = bunny_col+col_movement
            else:
                break
        else:
            break
        if current_eggs_sum > best_eggs_sum:
            best_eggs_sum = current_eggs_sum
            eggs_locations = current_eggs_location
            best_direction = direction

print(best_direction)
[print(sublist) for sublist in eggs_locations]
print(best_eggs_sum)
