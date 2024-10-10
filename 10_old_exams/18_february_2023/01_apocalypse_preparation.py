from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = deque(int(x) for x in input().split())

items_dict = {'Patch': 0,
              'Bandage': 0,
              'MedKit': 0
              }

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()
    both_sum = current_medicament + current_textile

    if both_sum == 30:
        items_dict['Patch'] += 1
    elif both_sum == 40:
        items_dict['Bandage'] += 1
    elif both_sum == 100:
        items_dict['MedKit'] += 1
    elif both_sum > 100:
        items_dict['MedKit'] += 1
        medicaments[-1] += both_sum - 100
    else:
        current_medicament += 10
        medicaments.append(current_medicament)

if not textiles and not medicaments:
    print('Textiles and medicaments are both empty.')
elif not textiles:
    print('Textiles are empty.')
elif not medicaments:
    print('Medicaments are empty.')

created_items = []
for key, value in items_dict.items():
    if items_dict[key] > 0:
        created_items.append((key, value))

sorted_items = sorted(created_items, key=lambda x: (-x[1], x[0]))
for current_tuple in sorted_items:
    print(f'{current_tuple[0]} - {current_tuple[1]}')

if medicaments:
    print(f"Medicaments left: {', '.join([str(el) for el in reversed(medicaments)])}")
if textiles:
    print(f"Textiles left: {', '.join([str(el) for el in textiles])}")
