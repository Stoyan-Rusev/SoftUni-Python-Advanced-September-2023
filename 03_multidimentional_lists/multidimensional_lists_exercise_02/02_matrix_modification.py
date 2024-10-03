rows = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(rows)]
while True:
    command = input()
    if command == 'END':
        break

    command = command.split()
    action = command[0]
    row = int(command[1])
    col = int(command[2])
    num = int(command[3])

    if 0 <= row < rows and 0 <= col < len(matrix[row]):
        if action == 'Add':
            matrix[row][col] += num
        elif action == 'Subtract':
            matrix[row][col] -= num
    else:
        print('Invalid coordinates')

[print(*sublist) for sublist in matrix]
