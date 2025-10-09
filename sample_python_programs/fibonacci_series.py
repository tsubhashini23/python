# A Fibonacci sequence is a series of numbers where, each number is the sum of the previous two numbers


def fibonacci(n):
    a = 0
    b = 1
    
    print(a, end = " ")
    print(b, end = " ")
    for i in range(n-2):
            c = a + b
            print(c, end = " ")
            a = b
            b = c
            
fibonacci(5)