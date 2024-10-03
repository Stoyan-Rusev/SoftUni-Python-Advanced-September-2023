from collections import deque

food_quantity = int(input())
orders_queue = deque([int(num) for num in input().split()])
print(max(orders_queue))

for _ in range(len(orders_queue)):
    order = orders_queue.popleft()
    if food_quantity >= order:
        food_quantity -= order
    else:
        orders_queue.appendleft(order)
        break

if orders_queue:
    print(f"Orders left: ", end='')
    print(*orders_queue)
else:
    print("Orders complete")
