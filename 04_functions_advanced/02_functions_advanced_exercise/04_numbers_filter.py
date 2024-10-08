def even_odd_filter(**kwargs):
    for key, value in kwargs.items():
        if key == 'even':
            kwargs[key] = [x for x in value if x % 2 == 0]
        elif key == 'odd':
            kwargs[key] = [x for x in value if x % 2 != 0]
    return dict(sorted(kwargs.items(), key=lambda kvp: -len(kvp[1])))

    # sorted_kvp_list = sorted(kwargs.items(), key=lambda kvp: -len(kvp[1]))
    # sorted_dict = {}
    # for kv in sorted_kvp_list:
    #     sorted_dict[kv[0]] = kv[1]
    # return sorted_dict


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
