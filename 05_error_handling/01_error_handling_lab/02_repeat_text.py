try:
    text = input()
    repeat = int(input())
    for _ in range(repeat):
        print(text, end='')

except ValueError:
    print("Variable times must be an integer")
