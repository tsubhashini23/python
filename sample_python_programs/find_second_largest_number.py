def second_largest(number_list):
    new_list = set(number_list)
    sorted_list = sorted(new_list)
    return sorted_list[-2]
print(second_largest([2,1,3,10,8]))
    