from collections import deque

ducks_dict = {'Darth Vader Ducky': 0,
              'Thor Ducky': 0,
              'Big Blue Rubber Ducky': 0,
              'Small Yellow Rubber Ducky': 0
              }

times = deque(int(x) for x in input().split())
tasks = deque(int(x) for x in input().split())

while times and tasks:
    current_time = times.popleft()
    current_task = tasks.pop()
    result = current_time * current_task

    if 0 <= result <= 60:
        ducks_dict['Darth Vader Ducky'] += 1
    elif 61 <= result <= 120:
        ducks_dict['Thor Ducky'] += 1
    elif 121 <= result <= 180:
        ducks_dict['Big Blue Rubber Ducky'] += 1
    elif 181 <= result <= 240:
        ducks_dict['Small Yellow Rubber Ducky'] += 1
    elif result > 240:
        current_task -= 2
        tasks.append(current_task)
        times.append(current_time)
print('Congratulations, all tasks have been completed! Rubber ducks rewarded:')
for key, value in ducks_dict.items():
    print(f'{key}: {value}')
