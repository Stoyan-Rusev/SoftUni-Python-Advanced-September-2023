from collections import deque

fuel_sequence = deque(int(x) for x in input().split())
consumption_indexes = deque(int(x) for x in input().split())
needed_fuel = deque(int(x) for x in input().split())

reached_altitudes = []
current_altitude = 0
reach_the_top = False
while True:
    last_fuel_quantity = fuel_sequence.pop()
    first_consumption = consumption_indexes.popleft()
    result = last_fuel_quantity - first_consumption
    current_amount = needed_fuel.popleft()

    current_altitude += 1
    if result < current_amount:
        print(f'John did not reach: Altitude {current_altitude}')
        print('John failed to reach the top.')
        break
    else:
        print(f'John has reached: Altitude {current_altitude}')
        reached_altitudes.append(f'Altitude {current_altitude}')
        if not needed_fuel:
            reach_the_top = True
            break

if not reach_the_top:
    if current_altitude == 1:
        print("John didn't reach any altitude.")
    else:
        print(f"Reached altitudes: {', '.join(reached_altitudes)}")


elif reach_the_top:
    print('John has reached all the altitudes and managed to reach the top!')
