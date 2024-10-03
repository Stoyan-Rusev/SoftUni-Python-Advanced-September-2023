n = int(input())
matrix = [[int(num) for num in input().split(' ')] for inner_list in range(n)]

primary_diagonal = []
secondary_diagonal = []
for i in range(n):
    primary_diagonal.append(matrix[i][i])
for i in range(n):
    secondary_diagonal.append(matrix[i][-1 - i])

result = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(result)
