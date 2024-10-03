from collections import deque

rows, cols = [int(x) for x in input().split()]
matrix = [['' for _ in range(cols)] for _ in range(rows)]
snake = deque(input())

for i in range(rows):
    for j in range(cols):
        current_symbol = snake[0]
        if i % 2 == 0:
            matrix[i][j] = current_symbol
        else:
            matrix[i][cols-1-j] = current_symbol
        snake.rotate(-1)

[print(*sublist, sep="") for sublist in matrix]
