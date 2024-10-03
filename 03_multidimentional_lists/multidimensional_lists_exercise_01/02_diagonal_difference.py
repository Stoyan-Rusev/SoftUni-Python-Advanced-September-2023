rows = int(input())
matrix = [[int(el) for el in input().split()] for sublist in range(rows)]

primary_diagonal = []
secondary_diagonal = []
for i in range(rows):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][(rows-1)-i])
diff = abs(sum(primary_diagonal) - sum(secondary_diagonal))

print(diff)
