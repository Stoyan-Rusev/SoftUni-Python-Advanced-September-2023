rows, cols = [int(x) for x in input().split()]
matrix = [[el for el in input().split()]for sublist in range(rows)]
identical_mtrx_counter = 0
for i in range(rows - 1):
    for j in range(cols - 1):
        first_el = matrix[i][j]
        next_el = matrix[i][j+1]
        bottom_el = matrix[i+1][j]
        diagonal_el = matrix[i+1][j+1]
        if first_el == next_el == bottom_el == diagonal_el:
            identical_mtrx_counter += 1
print(identical_mtrx_counter)
