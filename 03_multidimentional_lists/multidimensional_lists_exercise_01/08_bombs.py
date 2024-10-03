size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]
bombs_coordinates = input().split()
alive_counter = 0
alive_sum = 0

for current_bomb in bombs_coordinates:
    row, col = [int(x) for x in current_bomb.split(',')]
    damage = matrix[row][col]
    # upper targets:
    if row - 1 >= 0:
        if matrix[row-1][col] > 0:
            matrix[row-1][col] -= damage
    if row - 1 >= 0 and col - 1 >= 0:
        if matrix[row-1][col-1] > 0:
            matrix[row-1][col-1] -= damage
    if row - 1 >= 0 and col + 1 < size:
        if matrix[row-1][col+1] > 0:
            matrix[row-1][col+1] -= damage
    # lower targets:
    if row + 1 < size:
        if matrix[row+1][col] > 0:
            matrix[row+1][col] -= damage
    if row + 1 < size and col - 1 >= 0:
        if matrix[row + 1][col - 1] > 0:
            matrix[row+1][col-1] -= damage
    if row + 1 < size and col + 1 < size:
        if matrix[row+1][col+1] > 0:
            matrix[row+1][col+1] -= damage
    # left and right targets:
    if col + 1 < size:
        if matrix[row][col+1] > 0:
            matrix[row][col+1] -= damage
    if col - 1 >= 0:
        if matrix[row][col-1] > 0:
            matrix[row][col-1] -= damage
    matrix[row][col] = 0
# counting alive targets:
for i in range(size):
    for j in range(size):
        if matrix[i][j] > 0:
            alive_counter += 1
            alive_sum += matrix[i][j]
print(f'Alive cells: {alive_counter}')
print(f'Sum: {alive_sum}')

for sublist in matrix:
    print(*sublist)

