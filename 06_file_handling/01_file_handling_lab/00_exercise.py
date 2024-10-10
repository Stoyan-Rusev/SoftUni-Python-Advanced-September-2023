import os
WORKING_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(WORKING_DIR_PATH, '00_readme.txt')

print(WORKING_DIR_PATH)
print(file_path)

file = open(file_path, 'r')
file_two = open('00_readme_two.txt', 'r')

# file.write('Hello')
# file_two.write('\nHello')

print(file_two.readlines())
# for line in file_two.readlines():
#     print(line)
file.close()
file_two.close()
