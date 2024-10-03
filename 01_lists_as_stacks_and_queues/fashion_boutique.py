from collections import deque

clothes_values = deque([int(el) for el in input().split()])
capacity_of_a_rack = int(input())
racks_counter = 1
current_rack_value = 0
for _ in range(len(clothes_values)):
    current_item = clothes_values.pop()

    if current_rack_value + current_item < capacity_of_a_rack:
        current_rack_value += current_item

    elif current_rack_value + current_item == capacity_of_a_rack:
        if clothes_values:
            racks_counter += 1
            current_rack_value = 0

    elif current_rack_value + current_item > capacity_of_a_rack:
        racks_counter += 1
        current_rack_value = current_item

print(racks_counter)
