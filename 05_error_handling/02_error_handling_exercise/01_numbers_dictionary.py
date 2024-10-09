numbers_dictionary = {}

# Filling the dictionary:
line = input()
while line != "Search":
    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print('The variable number must be an integer')
        print(numbers_dictionary)
    line = input()

# Printing dictionary elements:
line = input()
while line != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print('Number does not exist in dictionary')
        print(numbers_dictionary)
    line = input()

# Removing dictionary elements:
line = input()
while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
        print(numbers_dictionary)
    except KeyError:
        print('Number does not exist in dictionary')
        print(numbers_dictionary)
    line = input()
