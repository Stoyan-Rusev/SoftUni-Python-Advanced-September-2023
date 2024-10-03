rows = int(input())
matrix = []
for _ in range(rows):
    inner_list = []
    symbols = input()
    for symbol in symbols:
        inner_list.append(symbol)
    matrix.append(inner_list)

searched_symbol = input()
symbol_found = False
for row_index in range(rows):
    if symbol_found:
        break
    for col_index in range(rows):
        if matrix[row_index][col_index] == searched_symbol:
            print(f'({row_index}, {col_index})')
            symbol_found = True
            break
if not symbol_found:
    print(f'{searched_symbol} does not occur in the matrix')
