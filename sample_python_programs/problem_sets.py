# #Problem_1
# print("#Problem_1 Answer")
# x =[]
# if x:
#     print("Not Empty")
# else:
#     print("Empty")
    
# #Problem_2
# def fun():
#     print("#Problem_2 Answer")
#     print("Hello")
#     return
#     print("World")
# fun()

# #Problem_3:
# class Car:
#     print("#Problem_3 Answer")
#     def __init__(self):
#         self.name = "swift"
#         self.maxSpeed = 150
        
# c = Car()
# c.name = "Wagon R"
# c.maxSpeed = 135

# print(c.name,c.maxSpeed)

# #Problem_4:
# class Student:
#     print("#Problem_4 Answer: How to access private variable outside the class")
#     def __init__(self,name,age):
#         self.__name = name
#         self.age = age

# s = Student("Rohan",60)
# print(s._Student__name)

# # #Problem_5:
# # class Student:
# #     print("#Problem_5 Answer: Attribute Error as private variable is accessed outside the class")
# #     def __init__(self,name,age):
# #         self.__name = name
# #         self.age = age

# # s = Student("Rohan",60)
# # print(s.__name)

# #Problem_6:
# def my_decorator(func):
#     print("#Problem_6 Answer")
#     def wrapper():
#         print("Start")
#         func()
#         print("End")
#     return wrapper

# @my_decorator
# def greet():
#     print("Hello!")

# greet()

#Problem_7:
print("#Problem_7 Answer")
a = 1000 
b = 1000 
print(a is b)
print(id(a), id(b)) 

#Problem_8:
print("#Problem_8 Answer")
a= int("1000")  # Forces a new int object
b= int("1000")  # Forces another new int object

print(a is b)
print(a==b)
print(id(a), id(b))

#Problem_9:
print("#Problem_9 Answer")
import math
floor = math.floor(3.9)
print(floor)

#Problem_10:
print("#Problem_10 Answer")
a = '23'
b=2
c=a*b  # The * operator in python can be used to repeat a string when multiplied by an integer.
print(c)

#Problem_11:
print("#Problem_11 Answer")
def modify(x):
    x=x+5
    
a=10
modify(a)
print(a)

#Problem_12:
print("#Problem_12 Answer")
def modify(x):
    x=x+5
    
a=10
result = modify(a)
print(result)      #As the function does not return anything
print(a)

#Problem_13:
print("#Problem_13 Answer")
print(round(4.567,2))

#Problem_14:
print("#Problem_14 Answer")
d = {None:"value"}
print(d[None])

#Problem_15:
print("#Problem_15 Answer")

def fun(name,roll):
    a = 10
    print(name,roll)
    # return a 
    
print(fun(name = "subha",roll = 101))

#Problem_16:
print("#Problem_16 Answer")

x="i love python!"
print(x.capitalize())
print(x.upper())

#Problem_17:
print("#Problem_17 Answer")

x = 2,3
print(type(x))    
#In Python, comma-separated values (without brackets) are interpreted as a tuple.creates a tuple because of the comma, not parentheses.n Python, the comma , is the key syntax for a tuple.

#Problem_18:
print("#Problem_18 Answer")

def test():
    try:
        return "try"
    finally:
        return "finally"
    
print(test())
#try wants to return "try"
#But finally always executes, even if there’s a return, break, continue, or exception in the try.
#If finally also has a return, it overrides the try's return.

#Problem_19:
print("#Problem_19 Answer")
a=(1,2,[3,4])
b=a[:]   # Creates full slice (shallow copy)
b[2].append(5) # Modifies the shared list inside the tuple

print(a) # (1, 2, [3, 4, 5])  
print(b) # (1, 2, [3, 4, 5])
print(a is b)  # False (different tuples)
print(a==b)    # True (contents are equal)
print(id(a))
print(id(b))   #Ids are same
#Python may reuse immutable objects (like small ints, short strings, tuples)


#Problem_20:
print("#Problem_20 Answer")
a = [1, 2, 3, 4]
b = a[1:3]
print(a)  # [1, 2, 3, 4]  (unchanged)
print(b)  # [2, 3]
print(a is b)   # False (different list objects)
print(a==b)
print(id(a))
print(id(b)) #Ids are different


#Problem_21:
print("#Problem_21 Answer")

print(math.pow(2, 3))  
#you don’t need to import the math module to perform exponentiation because Python provides a built-in function and operator:
print(2 ** 3)  # Output: 8
print(pow(2, 3))

#Problem_22:
print("#Problem_22 Answer")

a=[1,2]*2 #This does not mean nested multiplication — instead, it simply repeats the list [1, 2] two times
a[1]=3
print(a)

#Problem_23:
print("#Problem_23 Answer")
x=('1')
y=('1')
# This looks like a tuple, but it’s actually just a string in parentheses.
# In Python:
# Parentheses alone do not create a tuple.
# To create a 1-element tuple, you need a comma, like: ('1',)
# type(('1'))   ➞ <class 'str'>
# type(('1',))  ➞ <class 'tuple'>
z=('1',)
print(type(x), end = " ")
print(type(y), end = " ")
print(type(z), end = " ")

#Problem_23:
print("#Problem_23 Answer")
a=[1,2,3]
b=a
a.append(4)
print(b)

#Problem_24:
print("#Problem_24 Answer")
def test(a,b=2,c=3):
    return a+b+c
print(test(1))

#Problem_25:
print("#Problem_25 Answer")

print(round(45.8))
print(round(6352.898,2))
print(round(6352.898,5))
print(round(6352.898,1))

#Problem_26:
print("#Problem_26 Answer")
#*args allows a function to accept a variable number of positional arguments. 
#These arguments are captured as a tuple.
def findsum(a,b,*args):   # a = 1, b = 2, *args = (3,4,5)
    
    sm = 1
    for i in args:
        sm *= i
    return sm
    
z = findsum(1,2,3,4,5)
print(z)


#Interning is an optimization technique used by Python where identical immutable objects (like strings or small integers) are stored only once in memory to save space and improve performance.
#Problem_27:
print("#Problem_27 Answer")
#In Python, immutable objects like strings may be interned or cached for optimization.
#So, when you assign s = "abcd" and a = "abcd", Python may reuse the same memory location for both.
#Hence, id(s) == id(a) is likely True.
s = "abcd"
a= "abcd"

if id(s) == id(a):
    print("They are same")
else:
    print("They are not the same")
    
#Problem_28:
print("#Problem_28 Answer")
#If the string were dynamically created (e.g., using ''.join([...])), interning may not apply, and you might get "They are not the same".
s = "abcd"
a= ''.join(['a', 'b', 'c', 'd']) 

if id(s) == id(a):
    print("They are same")
else:
    print("They are not the same")
    
#Problem_29:
print("#Problem_29 Answer")
s = "abcd"
a= "efgh"

if id(s) == id(a):
    print("They are same")
else:
    print("They are not the same")
    
#Problem_30:
print("#Problem_30 Answer")
#s and a look the same, but they are two separate list objects created in memory.
#Lists are mutable, and Python never interns mutable objects.
s = [1,2,3]
a= [1,2,3]

if id(s) == id(a):
    print("They are same")
else:
    print("They are not the same")
    
# #Problem_31:
# print("#Problem_31 Answer")
# #Strings are immutable — once a string is created, you cannot change its individual characters. So error will occur
# s="abcd"
# s[0]='c'
# print(s)

#Problem_32:
print("#Problem_32 Answer")
#To change the first character to 'c', you can create a new string like this
#s[1:] gives the substring starting from index 1 (i.e., 'bcd')
#'c' + s[1:] → 'c' + 'bcd' → 'cbcd'
#Now s is updated to this new string 'cbcd'
s = "abcd"
s = 'c' + s[1:]  # Replace first character with 'c'
print(s)


#Problem_33:
print("#Problem_33 Answer")
import aiohttp
import asyncio

async def fetch_url(URL):
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            return response.status

status_code = asyncio.run(fetch_url("https://example.com"))
print("Status code:", status_code)

#Problem_34:
print("#Problem_34 Answer")
#Using two except blocks allows you to:
#Handle general ZeroDivisionError
#Handle your specific ZeroDenominatorError differently
#Due to the "except" order, if ZeroDenominatorError is raised, it will get caught by the first one (the general ZeroDivisionError), and the second one is never reached.
class ZeroDenominatorError(ZeroDivisionError):
    pass
try:
        a = 10
        b = 0
        if(b==0):
            raise ZeroDenominatorError()
        c = a/b
except ZeroDenominatorError:
        print('Zero Denominator Error occured',end ='')
except ZeroDivisionError:
        print('Zero Division Error occured',end= '')
else:
        print('else works')


z = ZeroDenominatorError()

