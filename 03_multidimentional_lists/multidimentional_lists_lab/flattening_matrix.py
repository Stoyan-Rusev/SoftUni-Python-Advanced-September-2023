row = int(input())
matrix = [[int(el) for el in input().split(', ')] for i in range(row)]
flattened_matrix = []
for i in range(row):
    for el in matrix[i]:
        flattened_matrix.append(el)
print(flattened_matrix)
