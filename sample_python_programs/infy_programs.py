
#Reverse a string without slicing
def reverse_string(name):
    result = ""
    for c in name:
        result = c + result
    return result

print(reverse_string("python"))
