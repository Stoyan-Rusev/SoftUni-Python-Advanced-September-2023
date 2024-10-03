# var 2
row = int(input())
matrix = [[int(el) for el in input().split(', ')] for i in range(row)]
flatten = []
flatten.extend(matrix)
print(flatten)
# var 3
row = int(input())
matrix = [[int(el) for el in input().split(', ')] for i in range(row)]
flatten = [num for sublist in matrix for num in sublist]
print(flatten)
