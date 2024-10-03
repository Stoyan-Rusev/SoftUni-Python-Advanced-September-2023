rows, cols = [int(item) for item in input().split(', ')]
matrix = [[int(num) for num in input().split()] for row_i in range(rows)]

for col_index in range(cols):
    columns_sum = 0
    for row_index in range(rows):
        columns_sum += matrix[row_index][col_index]
    print(columns_sum)
