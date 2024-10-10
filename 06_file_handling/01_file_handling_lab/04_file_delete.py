import os

try:
    os.remove('03_my_first_file.txt')
except FileNotFoundError:
    print('File not found')
