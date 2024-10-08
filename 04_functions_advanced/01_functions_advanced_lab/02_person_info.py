def get_info(name, town, age):
    return f"This is {name} from {town} and he is {age} years old"


dictionary = {'name': 'George',
              'age': '20',
              'town': 'Sofia'
              }
print(get_info(**dictionary))
