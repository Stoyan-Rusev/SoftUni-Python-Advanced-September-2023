from collections import deque

my_stack = deque()
for _ in range(int(input())):
    command = input()
    if command.startswith('1'):
        number = int(command.split()[1])
        my_stack.append(number)
    elif command == '2':
        if my_stack:
            my_stack.pop()
    elif command == '3':
        if my_stack:
            print(max(my_stack))
    elif command == '4':
        if my_stack:
            print(min(my_stack))

while my_stack:
    print(my_stack.pop(), end='')
    if my_stack:
        print(', ', end='')
