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


#Palindrome Practice

def check_palindrome(name):
    result = ""
    for c in name:
        result = c + result
    if result == name:
        return True
    return False


print(check_palindrome("madam"))

#Break
def test_break(num):
    for i in range(5):
        if i == 2:
            break
        print(i)
        
test_break(5)

#Continue:
def test_continue(num):
    for i in range(num):
        if i == 3:
            continue
        print(i)

test_continue(5)

#While loop

def test_while(num):
    print("While loop")
    i = 0
    while i < num:
        print(i)
        i += 1
            
test_while(5)  


#For loop One

def test_forloop(num):
    print("For loop")
    for i in range(num):
        print(i)
test_forloop(5)
            
            
            
            
        

    
            


    



            
            

    

        