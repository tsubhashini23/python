def flatten(nested_list):
    flat_list = []
    for sublist in nested_list:
        for subitem in sublist:
            flat_list.append(subitem)
    return flat_list

print(flatten([[1,2],[3,4]]))