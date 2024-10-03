from collections import deque

num_of_pumps = int(input())
pumps_counter = 0
initial_tank = 0
pumps_numbers = deque()
fuel_added = deque()
distances = deque()


for pump_num in range(num_of_pumps):
    fuel, distance_to_next_pump = [int(num) for num in input().split()]
    pumps_numbers.append(pump_num)
    fuel_added.append(fuel)
    distances.append(distance_to_next_pump)

# print(pumps_numbers)
# print(fuel_added)
# print(distances)

starting_pump_number = 0
while pumps_counter < num_of_pumps:
    current_num = pumps_numbers.popleft()
    current_fuel = fuel_added.popleft()
    current_distance = distances.popleft()
    initial_tank += current_fuel
    if initial_tank >= current_distance:
        initial_tank -= current_distance
        pumps_counter += 1
    else:
        pumps_counter = 0
        initial_tank -= 0
        starting_pump_number = current_num + 1
        if starting_pump_number == num_of_pumps + 1:
            starting_pump_number = 0

    pumps_numbers.append(current_num)
    fuel_added.append(current_fuel)
    distances.append(current_distance)
print(starting_pump_number)
