class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    num = float(input())
    if num < 0:
        raise ValueCannotBeNegative
