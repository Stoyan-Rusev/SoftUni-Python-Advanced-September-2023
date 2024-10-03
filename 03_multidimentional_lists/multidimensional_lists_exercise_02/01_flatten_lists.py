matrix = [[int(el) for el in sublist.split()] for sublist in input().split('|')]
final_result = []
for current_sublist in matrix[::-1]:
    final_result.extend(current_sublist)
print(*final_result)
