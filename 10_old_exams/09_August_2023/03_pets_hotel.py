def accommodate_new_pets(capacity, maximum_weight, *args):
    result = []
    accommodated_pets = {}

    for pet_type, pet_weight in args:
        if capacity <= 0:
            result.append('You did not manage to accommodate all pets!')
            break
        if pet_weight <= maximum_weight:
            if pet_type not in accommodated_pets.keys():
                accommodated_pets[pet_type] = 0
            accommodated_pets[pet_type] += 1
            capacity -= 1
    else:
        result.append(f'All pets are accommodated! Available capacity: {capacity}.')

    accommodated_pets = sorted(accommodated_pets.items(), key=lambda x: x[0])
    result.append('Accommodated pets:')
    for name, number in accommodated_pets:
        result.append(f'{name}: {number}')
    return '\n'.join(result)


print(accommodate_new_pets(
    2,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))

# print(accommodate_new_pets(
#     10,
#     10.0,
#     ("cat", 5.8),
#     ("dog", 10.5),
#     ("parrot", 0.8),
#     ("cat", 3.1),
# ))
#
# print(accommodate_new_pets(
#     2,
#     15.0,
#     ("dog", 10.0),
#     ("cat", 5.8),
#     ("cat", 2.7),
# ))
