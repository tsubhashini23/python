#Slicing

numbers = [6,1,3,9,5]
# print(sorted(numbers))
print(numbers[::-1])


text = "hello"
print(text[::-1])


#Reversed

numbers = [6,1,3,9,5]
print(list(reversed(numbers)))


text = "hello"
print(list(reversed(text)))

text = "hello"
print("".join(text))


sample_dict = {"a": 1, "b": 2, "c": 3}
print(dict(reversed(sample_dict.items())))
