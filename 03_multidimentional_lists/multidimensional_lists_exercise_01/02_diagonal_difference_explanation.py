rows = int(input())
matrix = [[int(el) for el in input().split()] for sublist in range(rows)]

primary_diagonal = []
secondary_diagonal = []
for i in range(rows):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][(rows-1)-i])

primary_diagonal_as_str = []
for index, el in enumerate(primary_diagonal):
    if index == 0:
        primary_diagonal_as_str.append(str(el))
    else:
        if str(el).startswith('-'):
            primary_diagonal_as_str.append(f"({el})")
        else:
            primary_diagonal_as_str.append(str(el))

secondary_diagonal_as_str = []
for index, el in enumerate(secondary_diagonal):
    if index == 0:
        secondary_diagonal_as_str.append(str(el))
    else:
        if str(el).startswith('-'):
            secondary_diagonal_as_str.append(f"({el})")
        else:
            secondary_diagonal_as_str.append(str(el))
diff = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(f"Primary diagonal: sum = {' + '.join(primary_diagonal_as_str)} = {sum(primary_diagonal)}")
print(f"Secondary diagonal: sum = {' + '.join(secondary_diagonal_as_str)} = {sum(secondary_diagonal)}")
print(f"Difference: |{sum(primary_diagonal)} - {sum(secondary_diagonal)}| = {diff}")
