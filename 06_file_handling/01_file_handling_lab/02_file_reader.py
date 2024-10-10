import os
# var1:
WORKING_PATH = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(WORKING_PATH, '02_numbers.txt')
with open(file_path) as f:
    print(sum([int(el[0]) for el in f.readlines()]))
#  var2:
file = open("02_numbers.txt", 'r')
print(sum([int(el[0]) for el in file.readlines()]))