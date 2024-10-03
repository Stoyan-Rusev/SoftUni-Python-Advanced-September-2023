def most_dangerous():
    top_knight_locations = []
    max_targets = 0
    for current_data in knights_positions:
        r = current_data[0]
        c = current_data[1]
        target_counter = 0
        # up:
        if r-2 >= 0 and c+1 < n:
            if field[r-2][c+1] == 'K':
                target_counter += 1
        if r-2 >= 0 and c-1 >= 0:
            if field[r-2][c-1] == 'K':
                target_counter += 1
        # down:
        if r+2 < n and c+1 < n:
            if field[r+2][c+1] == 'K':
                target_counter += 1
        if r+2 < n and c-1 >= 0:
            if field[r+2][c-1] == 'K':
                target_counter += 1
        # left:
        if c-2 >= 0 and r-1 >= 0:
            if field[r-1][c-2] == 'K':
                target_counter += 1
        if c-2 >= 0 and r+1 < n:
            if field[r+1][c-2] == 'K':
                target_counter += 1
        # right:
        if c+2 < n and r+1 < n:
            if field[r+1][c+2] == 'K':
                target_counter += 1
        if c+2 < n and r-1 >= 0:
            if field[r-1][c+2] == 'K':
                target_counter += 1

        if target_counter > max_targets:
            max_targets = target_counter
            top_knight_locations = [r, c]

    return top_knight_locations


n = int(input())
knights_positions = []
field = []
for row in range(n):
    current_row = list(input())
    field.append(current_row)
    for col in range(n):
        if current_row[col] == 'K':
            knights_positions.append([row, col])

counter = 0
while True:
    knight_to_remove = most_dangerous()
    if knight_to_remove:
        field[knight_to_remove[0]][knight_to_remove[1]] = "0"
        knights_positions.remove(knight_to_remove)
        counter += 1
    else:
        break
print(counter)
