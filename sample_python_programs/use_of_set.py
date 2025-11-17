# set() is a built-in function in Python
# It is used to create a set, which is an unordered, mutable, and unindexed collection of unique elements
# Duplicates are automatically removed
# Elements are unordered (no indexing or slicing)
# Mutable – you can add or remove items
# Used for set operations like union, intersection, difference


# Remove duplicates from a list

# numbers_list = [1,2,2,3,3,4,5,6,6]
# new_numbers_list = set(numbers_list)
# print(new_numbers_list)
#
#
# #Use of join
#
# fruit_list = ['apple','banana','orange']
# print(",".join(fruit_list))
# print(type(",".join(fruit_list)))
#
#
# # Set operations
#
# a = set([1,2,3])
# b = set([3,4,5])
#
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
#
# #Check whether a value is in the list or not
#
# my_set = set([10,20,30,30])
# print(30 in my_set)
# print(40 in my_set)
#
# #Convert string to unique characters
# s = "subha"
# my_char_set = set(s)
# new_set = dict.fromkeys(s)
# print(my_char_set)
# print("New set as is:",new_set)
# print("Only the keys",new_set.keys())
# print("".join(new_set.keys()))
# print("New set as list",list(new_set))

# Mask numbers using pattern
num = "1234-5678-9123-4455"
num_list = list(num)
print(num_list)
ln = len(num_list)
print(ln)

numbers = ["0","1","2","3","4","5","6","7","8","9"]

for i in range(0, ln-4):
    if  num_list[i] in numbers:
        num_list[i] = "*"
print("".join(num_list))


