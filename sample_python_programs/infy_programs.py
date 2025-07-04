
#Reverse a string without slicing
def reverse_string(name):
    result = ""
    for c in name:
        result = c + result
    return result

print(reverse_string("python"))


#Sum of all prime numbers
def prime_number(n):
    for i in range(2, n):
        if n%i == 0:
            return False #Not Prime
    return True #Prime

def find_sum_of_prime(num):
    result = []
    for i in range(2, num):
        if (prime_number(i)):
            result.append(i)
    final = sum(result)
    return final

print(find_sum_of_prime(15))


#Find all the consonants from a string

def find_consonants(data):
    new_data = data.lower()
    result = []
    vowels = "aeiouAEIOU"
    for c in new_data:
        if c not in vowels:
            result.append(c)
    final = print("".join(result))
    return final

find_consonants("subha")

            
    
