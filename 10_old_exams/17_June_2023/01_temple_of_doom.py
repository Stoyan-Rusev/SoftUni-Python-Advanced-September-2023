from collections import deque

tools_queue = deque([int(num) for num in input().split()])
substances_stack = deque([int(num) for num in input().split()])
challenges = [int(num) for num in input().split()]

message = None

while True:
    tool = tools_queue.popleft()
    substance = substances_stack.pop()
    result = tool * substance

    if result in challenges:
        challenges.remove(result)
        if not challenges:
            message = 'Harry found an ostracon, which is dated to the 6th century BCE.'
            break
    else:
        tool += 1
        tools_queue.append(tool)

        substance -= 1
        if substance > 0:
            substances_stack.append(substance)

    if not tools_queue or not substances_stack:
        message = 'Harry is lost in the temple. Oblivion awaits him.'
        break

print(message)
if tools_queue:
    tools_queue = (str(el) for el in tools_queue)
    print('Tools: ' + ', '.join(tools_queue))
if substances_stack:
    substances_stack = (str(el) for el in substances_stack)
    print('Substances: ' + ', '.join(substances_stack))
if challenges:
    challenges = (str(el) for el in challenges)
    print('Challenges: ' + ', '.join(challenges))
