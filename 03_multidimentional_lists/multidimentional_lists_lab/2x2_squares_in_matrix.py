rows, cols = [int(num) for num in input().split()]
matrix = [input().split() for inner_list in range(rows)]
identical_squares_counter = 0
for i in range(rows - 1):
    for j in range(cols - 1):
        main_el = matrix[i][j]
        next_el = matrix[i][j + 1]
        down_el = matrix[i + 1][j]
        diagonal_el = matrix[i + 1][j + 1]
        if main_el == next_el == down_el == diagonal_el:
            identical_squares_counter += 1
print(identical_squares_counter)
