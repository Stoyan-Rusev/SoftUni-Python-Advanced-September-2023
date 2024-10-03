n = int(input())
matrix = [[int(num) for num in input().split(', ')] for inner_list in range(n)]

primary_diagonal = []
secondary_diagonal = []
for i in range(n):
    primary_diagonal.append(matrix[i][i])
for i in range(n):
    secondary_diagonal.append(matrix[i][-1 - i])

print(f"Primary diagonal: {', '.join([str(el) for el in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(el) for el in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
