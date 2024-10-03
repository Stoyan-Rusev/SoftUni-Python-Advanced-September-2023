from collections import deque

initial_water = int(input())
people_waiting = deque()
name = input()

while name != 'Start':
    people_waiting.append(name)
    name = input()

command = input()
while command != 'End':
    if command.startswith('refill'):
        command = command.split()
        amount = int(command[1])
        initial_water += amount
    else:
        wanted_liters = int(command)
        if wanted_liters <= initial_water:
            person_name = people_waiting.popleft()
            initial_water -= wanted_liters
            print(f'{person_name} got water')
        else:
            person_name = people_waiting.popleft()
            print(f'{person_name} must wait')
    command = input()
print(f'{initial_water} liters left')
