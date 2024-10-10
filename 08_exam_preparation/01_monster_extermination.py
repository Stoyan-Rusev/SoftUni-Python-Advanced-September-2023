from collections import deque

armor_values = deque(int(el) for el in input().split(','))
striking_impacts = deque(int(el) for el in input().split(','))

total_kills = 0
while armor_values and striking_impacts:
    current_armor = armor_values.popleft()
    current_impact = striking_impacts.pop()

    if current_impact >= current_armor:
        total_kills += 1
        current_impact -= current_armor
        if current_impact > 0:
            if striking_impacts:
                striking_impacts[-1] += current_impact
            else:
                striking_impacts.append(current_impact)

    elif current_impact < current_armor:
        current_armor -= current_impact
        armor_values.append(current_armor)

if not armor_values:
    print('All monsters have been killed!')
if not striking_impacts:
    print('The soldier has been defeated.')
print(f'Total monsters killed: {total_kills}')
