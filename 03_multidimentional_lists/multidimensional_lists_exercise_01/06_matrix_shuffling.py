def are_coordinates_valid(row1, col1, row2, col2, mtrx_rows, mtrx_cols):
    if mtrx_rows > row1 >= 0 and mtrx_cols > col1 >= 0 and mtrx_rows > row2 >= 0 and mtrx_cols > col2 >= 0:
        return True
    return False


rows, cols = [int(x) for x in input().split()]
matrix = []
for i in range(rows):
    matrix.append(input().split())

command = input().split()
while command[0] != 'END':
    if command[0] == 'swap' and len(command) == 5:
        r1, c1, r2, c2 = [int(x) for x in command[1:]]
        if are_coordinates_valid(r1, c1, r2, c2, rows, cols):
            matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
            for sublist in matrix:
                print(*sublist)
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
    command = input().split()
