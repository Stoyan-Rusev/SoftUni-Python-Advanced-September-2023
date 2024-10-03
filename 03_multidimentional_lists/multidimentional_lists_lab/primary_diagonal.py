rol_col_num = int(input())
matrix = []
for _ in range(rol_col_num):
    sublist = [int(num) for num in input().split()]
    matrix.append(sublist)

diagonal_sum = 0
for row_index in range(rol_col_num):
    diagonal_sum += matrix[row_index][row_index]
print(diagonal_sum)
