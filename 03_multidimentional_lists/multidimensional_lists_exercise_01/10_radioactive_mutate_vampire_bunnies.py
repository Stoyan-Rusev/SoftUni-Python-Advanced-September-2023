rows, cols = [int(x) for x in input().split()]

player_row = 0
player_col = 0

lair = []
for _ in range(rows):
    sublist = list(input())
    lair.append(sublist)
    if 'P' in sublist:
        player_col = sublist.index('P')
        player_row = lair.index(sublist)

directions = input()
for direction in directions:
    pass
