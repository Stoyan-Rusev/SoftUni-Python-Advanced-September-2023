num_lines = int(input())
parking_lot = set()
for line in range(num_lines):
    direction, plate = input().split(", ")
    if direction == 'IN':
        parking_lot.add(plate)
    elif direction == 'OUT':
        parking_lot.remove(plate)

if parking_lot:
    for car in parking_lot:
        print(car)
else:
    print('Parking Lot is Empty')
