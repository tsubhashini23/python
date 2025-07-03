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

def second_largest(nums):
    nums = list(set(nums))
    sorted_list =sorted(nums)
    # print(sorted_list[-2])
    return nums[-2]

print(second_largest([4,2,6,9]))
def greet(name):
    print("Hello,", name)

output = greet("Subha")  # Output: Hello, Subha
print(output)  




            
            

    

        