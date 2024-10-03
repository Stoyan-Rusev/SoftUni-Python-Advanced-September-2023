size = int(input())
alice_position = []
tea_bags = 0
field = []
for r in range(size):
    field.append(input().split())
    for c in range(size):
        if field[r][c] == 'A':
            alice_position = [r, c]
            field[r][c] = '*'


directions = {'up': (-1, 0),
              'down': (1, 0),
              'left': (0, -1),
              'right': (0, 1)
              }


while True:
    current_row = alice_position[0]
    current_col = alice_position[1]
    direction = input()
    new_row = current_row + directions[direction][0]
    new_col = current_col + directions[direction][1]
    new_position = field[new_row][new_col]
    if new_position == 'R':
        field[new_row][new_col] = '*'
        print("Alice didn't make it to the tea party.")
        break
    elif new_row < 0 or new_row >= size or new_col < 0 or new_col >= size:
        print("Alice didn't make it to the tea party.")
        break
    elif new_position == '.':
        field[new_row][new_col] = '*'
        alice_position = [new_row, new_col]
    elif new_position == '*':
        alice_position = [new_row, new_col]
    else:
        tea_bags += int(new_position)
        field[new_row][new_col] = '*'
        alice_position = [new_row, new_col]
        if tea_bags >= 10:
            print("She did it! She went to the party.")
            break

[print(*sublist) for sublist in field]
