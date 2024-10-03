rows, cols = [int(num) for num in input().split()]
matrix = [[int(num) for num in input().split()] for _ in range(rows)]
max_sum = float('-inf')
sub_matrix = []
for i in range(rows - 2):
    for j in range(cols - 2):
        first_line = matrix[i][j:j+3]
        second_line = matrix[i+1][j:j+3]
        third_line = matrix[i+2][j:j+3]
        current_sum = sum(first_line) + sum(second_line) + sum(third_line)
        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [first_line, second_line, third_line]
print(f'Sum = {max_sum}')
[print(*row) for row in sub_matrix]
