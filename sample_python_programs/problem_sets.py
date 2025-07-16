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