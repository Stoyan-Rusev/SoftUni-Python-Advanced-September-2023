from collections import deque

command = input()
customers = deque()
while command != 'End':
    if command == 'Paid':
        for line in range(len(customers)):
            customer = customers.popleft()
            print(customer)
        command = input()
        continue

    name = command
    customers.append(name)
    command = input()

print(f'{len(customers)} people remaining.')
