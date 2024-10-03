from collections import deque

kids_list = input().split()
toss_number = int(input())
kids_queue = deque(kids_list)
toss_counter = 0

while len(kids_queue) > 1:
    toss_counter += 1
    if toss_counter % toss_number == 0:
        removed_kid = kids_queue.popleft()
        print(f'Removed {removed_kid}')
    else:
        kids_queue.rotate(-1)

print(f'Last is {kids_queue[0]}')
