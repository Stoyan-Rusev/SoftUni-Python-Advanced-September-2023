def sorting_cheeses(**kwargs):
    sorted_list = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ''
    for current in sorted_list:
        result += f'{current[0]}\n'
        for quantity in sorted(current[1], reverse=True):
            result += f'{quantity}\n'
    return result
