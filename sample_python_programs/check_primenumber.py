def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, n-1):
        if n % i == 0:
            return False  # Not a prime number
    return True # Prime Number
print(check_prime(15))