rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for sublist in range(rows)]

biggest_mtrx = None
max_sum = float('-inf')

for i in range(rows - 2):
    for j in range(cols - 2):
        first_row = matrix[i][j:j+3]
        second_row = matrix[i+1][j:j+3]
        third_row = matrix[i+2][j:j+3]
        current_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if current_sum > max_sum:
            max_sum = current_sum
            biggest_mtrx = [first_row, second_row, third_row]
print(f"Sum = {max_sum}")
for sublist in biggest_mtrx:
    print(*sublist)

