def operate(operator, *args):
    def summing():
        result = args[0]
        for index in range(1, len(args)):
            result += args[index]
        return result

    def subtract():
        result = args[0]
        for index in range(1, len(args)):
            result -= args[index]
        return result

    def multiply():
        result = args[0]
        for index in range(1, len(args)):
            result *= args[index]
        return result

    def divide():
        result = args[0]
        for index in range(1, len(args)):
            result /= args[index]
        return result

    if operator == '+':
        return summing()
    elif operator == '-':
        return subtract()
    elif operator == '*':
        return multiply()
    elif operator == '/':
        return divide()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))