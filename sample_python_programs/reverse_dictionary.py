#Reversing key and value

sample_dict = {"a": 1, "b": 2, "c": 3}
new_dict = {}
for k, v in sample_dict.items():
    new_dict[v] = k
print(new_dict)



#Reverse like normal list

sample_dict = {"a": 1, "b": 2, "c": 3}
new_dict = dict(reversed(sample_dict.items()))
print(new_dict)