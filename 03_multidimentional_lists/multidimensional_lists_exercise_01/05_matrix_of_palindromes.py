rows, cols = [int(x) for x in input().split()]
# matrix = []
add_num = 0
for r in range(ord('a'), ord('a')+rows):
    sublist = []
    for c in range(ord('a'), ord('a')+cols):
        sublist.append(f"{chr(r)}{chr(c+add_num)}{chr(r)}")
    # matrix.append(sublist)
    add_num += 1
    print(*sublist)
