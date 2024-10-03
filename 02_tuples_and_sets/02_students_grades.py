students = {}

for _ in range(int(input())):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for key, value in students.items():
    formatted_grades = ' '.join([f'{grade:.2f}' for grade in value])
    print(f'{key} -> {formatted_grades} (avg: {sum(value)/len(value):.2f})')
