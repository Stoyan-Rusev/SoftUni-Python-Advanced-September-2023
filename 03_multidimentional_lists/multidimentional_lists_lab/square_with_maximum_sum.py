rows, cols = [int(num) for num in input().split(', ')]
matrix = []
for row in range(rows):
    inner_list = [int(num) for num in input().split(', ')]
    matrix.append(inner_list)

max_sum = 0
row_index = None
col_index = None
for i in range(rows - 1):
    for j in range(cols - 1):
        square_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
        if square_sum > max_sum:
            max_sum = square_sum
            row_index = i
            col_index = j
print(f'{matrix[row_index][col_index]} {matrix[row_index][col_index + 1]}')
print(f'{matrix[row_index + 1][col_index]} {matrix[row_index + 1][col_index + 1]}')
print(max_sum)
