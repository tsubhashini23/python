# def check_prime(n):
#     if n <= 1:
#         print(f"{n} is not a prime number")
#         return
#     for i in range(2, n-1):
#         if n % i == 0:
#             print(f"{n} is not a prime number")  # Not a prime number
#             return
#     print(f"{n} is a prime number") # Prime Number
# check_prime(9)


def is_prime(n):
    if n <= 1:
        # print(f"{n} is not a prime number")
        return False
    for i in range(2, n-1):
        if n%i==0:
            # print(f"{n} is not a prime number")
            return False
    # print(f"{n} is a prime number")
    return True

prime_list = []
non_prime_list = []
for num in range(40, 62):
    if is_prime(num):
        prime_list.append(num)
    else:
        non_prime_list.append(num)

print("Prime numbers:", prime_list)
print("Non-prime numbers:", non_prime_list)