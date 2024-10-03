expression = input()
opening_parentheses_stack = []
for index, symbol in enumerate(expression):
    if symbol == '(':
        opening_parentheses_stack.append(int(index))
    elif symbol == ')':
        removed_index = int(opening_parentheses_stack.pop())
        print(expression[removed_index:index + 1])

