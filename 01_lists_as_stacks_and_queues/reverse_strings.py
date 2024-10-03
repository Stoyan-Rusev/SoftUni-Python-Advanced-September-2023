from collections import deque

string = deque(input())
reversed_string = ''
for line in range(len(string)):
    removed_char = string.pop()
    reversed_string += removed_char

print(reversed_string)
