numbers = tuple(float(x) for x in input().split())
unique_nums = []

for num in numbers:
    if num not in unique_nums:
        unique_nums.append(num)
        print(f'{num:.1f} - {numbers.count(num)} times')
