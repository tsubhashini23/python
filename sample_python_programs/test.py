# def vowels_in_string(name):
#     vowel = "aeiouAEIOU"
#     count = 0
#     for c in name:
#         if c in vowel:
#             count =+ 1
#             print(f"Vowels in name: {c}")
#     return count
            
# print(f"Count: {vowels_in_string('subha')}")

# my_list = [1, 2, 2]
# my_tuple = (1, 2, 2)
# my_set = {1, 2, 2}

# print(my_list)  # [1, 2, 2]
# print(my_tuple) # (1, 2, 2)
# print(my_set)   # {1, 2}   ← duplicates removed

# def second_largest(nums):
#     nums = list(set(nums))
#     sorted_list =sorted(nums)
#     print(sorted_list[-2])
#     return nums[-2]

# print(second_largest([4,2,6,9]))
# def greet(name):
#     print("Hello,", name)

# output = greet("Subha")  # Output: Hello, Subha
# print(output)  


# fibonacci series practice

from functools import reduce
import math


def solve_fibonacci_series(num):
    result = [0,1]
    for i in range(0,num):
        if len(result) != num:
            result.append(result[i]+result[i+1])
    return result

print(solve_fibonacci_series(9))

#Factorial practice

def find_factorial(num):
    numbers = []
    for i in range(1, num+1):
        numbers.append(i)
    # result = math.prod(numbers)
    result = reduce(lambda x,y: x*y,numbers)
    return result
print(find_factorial(5))


    



            
            

    

        