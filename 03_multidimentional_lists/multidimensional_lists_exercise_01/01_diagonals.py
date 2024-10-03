rows = int(input())
matrix = [[int(el) for el in input().split(', ')] for sublist in range(rows)]

if rows == 1:
    print('Primary diagonal: 1. Sum: 1')
    print('Secondary diagonal: 1. Sum: 1')

elif rows > 1:
    primary_diagonal = []
    for i in range(rows):
        primary_diagonal.append(matrix[i][i])
    print(f"Primary diagonal: {', '.join([str(num) for num in primary_diagonal])}. "
          f"Sum: {sum(primary_diagonal)}")

    secondary_diagonal = []
    for i in range(rows):
        last_index = len(matrix[1]) - 1
        secondary_diagonal.append(matrix[i][last_index - i])
    print(f"Secondary diagonal: {', '.join([str(num) for num in secondary_diagonal])}. "
          f"Sum: {sum(secondary_diagonal)}")
