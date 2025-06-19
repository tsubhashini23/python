# generator:
# It is special function which returns an iterator and generates one value at a time using yield, rather than computing all values at once
# It uses yield instead of return
# It is used to handle infinite data.
# When called, it doesn’t execute immediately — it returns a generator object.
# Values are produced one at a time, only when asked (lazy evaluation).
# Memory-efficient: Doesn't store entire list in memory
# yield pauses the function and remembers its tate. The next we call, it resumes from where it left off

# range function:
# The range() function generates a sequence of numbers from start to just before stop, incrementing (or decrementing) by step.


def gen():
    yield 1
    yield 2

for i in gen():
    print(i)
    
# Sample countdown generator code using while :

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)
    
# # Sample code using for :
n = 5
for i in n:
    print(n)    
    n -= 1 
    
# Sample code using while :
n = 5
while n > 0:
    print(n)    
    n -= 1
    
# Sample code using range function :

for n in range(5, 0, -1):
    print(n)   
    
    
#What will happen when return is used:

def gen():
    return 1
    return 2  

for i in gen():
    print(i)
    
    #TypeError: 'int' object is not iterable will occur