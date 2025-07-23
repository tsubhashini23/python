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
