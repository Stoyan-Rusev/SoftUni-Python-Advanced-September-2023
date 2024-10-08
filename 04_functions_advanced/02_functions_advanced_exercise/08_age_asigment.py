def age_assignment(*args, **kwargs):
    name_age_dict = {}
    for name in args:
        name_age_dict[name] = kwargs[name[0]]
    sorted_name_age_list = sorted(name_age_dict.items(), key=lambda kvp: kvp[0])
    result = ''
    for name, age in sorted_name_age_list:
        result += f"{name} is {age} years old.\n"
    return result


print(age_assignment("Peter", "George", G=26, P=19))
