# Square battlefield
ROWS = int(input())

submarine_location = None
field = []
for i in range(ROWS):
    line = list(input())
    field.append(line)
    if 'S' in line:
        submarine_location = [i, line.index('S')]
        field[submarine_location[0]][submarine_location[1]] = '-'

blown_mines = 0
target_hits = 0

while True:
    direction = input()

    if direction == 'up':
        submarine_location[0] -= 1
    elif direction == 'down':
        submarine_location[0] += 1
    elif direction == 'left':
        submarine_location[1] -= 1
    elif direction == 'right':
        submarine_location[1] += 1
    position_item = field[submarine_location[0]][submarine_location[1]]

    if position_item == '-':
        continue

    elif position_item == 'C':
        target_hits += 1
        if target_hits == 3:
            field[submarine_location[0]][submarine_location[1]] = 'S'
            break
        field[submarine_location[0]][submarine_location[1]] = '-'

    elif position_item == '*':
        blown_mines += 1
        if blown_mines == 3:
            field[submarine_location[0]][submarine_location[1]] = 'S'
            break
        field[submarine_location[0]][submarine_location[1]] = '-'

if target_hits == 3:
    print('Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
elif blown_mines == 3:
    print(f"Mission failed, U-9 disappeared! "
          f"Last known coordinates [{submarine_location[0]}, {submarine_location[1]}]!")
for sublist in field:
    print(f"{''.join(sublist)}")
