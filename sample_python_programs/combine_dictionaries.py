#Merge dictionaries

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}

merged_dict = {}

iterable = set(dict1) | set(dict2)
print(iterable)

for key in iterable:
    merged_dict[key] = dict1.get(key, 0) + dict2.get(key, 0)
print(merged_dict.items())
print(sorted(merged_dict.items()))
print(dict(sorted(merged_dict.items())))


# Using dictionary unpacking operator (dict2 overwrites dict1): It “opens up” the dictionary into individual key–value pairs.
# Take all key–value pairs from dict1, then take all key–value pairs from dict2 and put them into a new dictionary.

print({**dict1, **dict2})

# Using update(),  (dict2 overwrites dict1)

new_dict = dict1.copy()
new_dict.update(dict2)
print(new_dict)


