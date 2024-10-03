# {[()]} - Parentheses are balanced.
# (){}[] - Parentheses are balanced.
# {[(])} - Parentheses are NOT balanced.
from collections import deque
sequence = '{[()]}}'
opening_parentheses = deque()
for el in sequence:
    if el in ['(', '[', '{']:
        opening_parentheses.append(el)

    elif el == ')':
        if opening_parentheses.pop() != '(':
            print('NO')
            break
    elif el == ']':
        if opening_parentheses.pop() != '[':
            print('NO')
            break
    elif el == '}':
        if opening_parentheses.pop() != '{':
            print('NO')
            break

if not opening_parentheses:
    print('YES')

