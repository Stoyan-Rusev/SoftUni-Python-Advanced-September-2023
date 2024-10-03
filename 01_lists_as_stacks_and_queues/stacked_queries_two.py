from collections import deque


def pushing_into_stack(some_stack: deque, item):
    some_stack.append(item)
    return some_stack


def deleting(some_stack: deque):
    if len(some_stack) > 0:
        some_stack.pop()
    return some_stack


def print_max_num(some_stack: deque):
    if len(some_stack) > 0:
        max_num = int(some_stack[0])
        for num in some_stack:
            if int(num) > int(max_num):
                max_num = num
        print(max_num)
    return some_stack


def print_min_num(some_stack: deque):
    if len(some_stack) > 0:
        min_num = int(some_stack[0])
        for num in some_stack:
            if int(num) < int(min_num):
                min_num = num
        print(min_num)
    return some_stack


my_stack = deque()
number_of_commands = int(input())
for line in range(number_of_commands):
    command = input().split()
    command_code = command[0]
    if command_code == '1':
        number = command[1]
        my_stack = pushing_into_stack(my_stack, number)

    elif command_code == '2':
        my_stack = deleting(my_stack)

    elif command_code == '3':
        my_stack = print_max_num(my_stack)

    elif command_code == '4':
        my_stack = print_min_num(my_stack)

# print(", ".join(my_stack))
final_result = []
for _ in range(len(my_stack)):
    final_result.append(my_stack.pop())
print(', '.join(final_result))
