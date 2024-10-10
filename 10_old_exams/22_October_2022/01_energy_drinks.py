from collections import deque

MAX_CAFFEINE = 300
caffeine_drank = 0

milligrams_caffeine = deque(int(x) for x in input().split(', '))
energy_drinks = deque(int(x) for x in input().split(', '))

while milligrams_caffeine and energy_drinks:
    last_milligrams = milligrams_caffeine.pop()
    first_drink = energy_drinks.popleft()
    sum_ = last_milligrams * first_drink

    if sum_ + caffeine_drank <= MAX_CAFFEINE:
        caffeine_drank += sum_
    else:
        energy_drinks.append(first_drink)
        caffeine_drank -= 30
        if caffeine_drank < 0:
            caffeine_drank = 0

if energy_drinks:
    print(f'Drinks left: {", ".join(str(el) for el in energy_drinks)} ')
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {caffeine_drank} mg caffeine.")
