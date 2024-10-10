with open('03_my_first_file.txt', 'w') as f:
    f.write('I just created my first file!')
print(f.closed)