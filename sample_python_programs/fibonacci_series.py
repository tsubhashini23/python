# A Fibonacci sequence is a series of numbers where, each number is the sum of the previous two numbers


def fibonacci(n):
    a = 1
    b = 2
    
    print(a)
    print(b)
    for _ in range(n-2):
            c = a + b
            print(c)
            a = b
            b = c
            
fibonacci(5)