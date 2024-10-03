from collections import deque
numbers = deque([int(num) for num in input().split()])
reversed_nums = deque()
for _ in range(len(numbers)):
    reversed_nums.append(numbers.pop())
print(*reversed_nums)
