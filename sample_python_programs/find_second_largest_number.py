# def second_largest(number_list):
#     new_list = set(number_list)
#     sorted_list = sorted(new_list)
#     return sorted_list[-2]
# print(second_largest([2,1,3,10,8]))

given_list = [2,1,3,10,8]
new_list = set(given_list)
sorted_list = sorted(new_list)
print(f"Second largest number is {sorted_list[-2]}")
    