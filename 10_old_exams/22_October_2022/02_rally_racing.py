ROWS = int(input())
CAR_NUM = input()

message = ''
kilometers_driven = 0
tunnels_positions = []
car_position = [0, 0]

field = []
for i in range(ROWS):
    line = input().split()
    field.append(line)
    for el in line:
        if el == "T":
            tunnels_positions.append([i, line.index(el)])

while True:
    direction = input()
    if direction == 'End':
        field[car_position[0]][car_position[1]] = 'C'
        message = f'Racing car {CAR_NUM} DNF.'
        break

    if direction == 'up':
        car_position[0] -= 1
    elif direction == 'down':
        car_position[0] += 1
    elif direction == 'left':
        car_position[1] -= 1
    elif direction == 'right':
        car_position[1] += 1

    if field[car_position[0]][car_position[1]] == '.':
        kilometers_driven += 10
    elif field[car_position[0]][car_position[1]] == 'T':
        kilometers_driven += 30
        field[car_position[0]][car_position[1]] = '.'
        tunnels_positions.remove([car_position[0], car_position[1]])
        car_position = tunnels_positions[0]
        field[car_position[0]][car_position[1]] = '.'
    elif field[car_position[0]][car_position[1]] == 'F':
        kilometers_driven += 10
        field[car_position[0]][car_position[1]] = 'C'
        message = f'Racing car {CAR_NUM} finished the stage!'
        break
print(message)
print(f'Distance covered {kilometers_driven} km.')
for sublist in field:
    print(''.join(sublist))
