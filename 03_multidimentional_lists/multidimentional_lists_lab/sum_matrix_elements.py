rows, cols = [int(num) for num in input().split(', ')]
matrix = []
matrix_sum = 0
for row in range(rows):
    sublist = [int(num) for num in input().split(', ')]
    matrix_sum += sum(sublist)
    matrix.append(sublist)
print(matrix_sum)
print(matrix)
