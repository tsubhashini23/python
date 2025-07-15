#Problem_1
print("#Problem_1 Answer")
x =[]
if x:
    print("Not Empty")
else:
    print("Empty")
    
#Problem_2
def fun():
    print("#Problem_2 Answer")
    print("Hello")
    return
    print("World")
fun()

#Problem_3:
class Car:
    print("#Problem_3 Answer")
    def __init__(self):
        self.name = "swift"
        self.maxSpeed = 150
        
c = Car()
c.name = "Wagon R"
c.maxSpeed = 135

print(c.name,c.maxSpeed)

#Problem_4:
class Student:
    print("#Problem_4 Answer: How to access private variable outside the class")
    def __init__(self,name,age):
        self.__name = name
        self.age = age

s = Student("Rohan",60)
print(s._Student__name)

# #Problem_5:
# class Student:
#     print("#Problem_5 Answer: Attribute Error as private variable is accessed outside the class")
#     def __init__(self,name,age):
#         self.__name = name
#         self.age = age

# s = Student("Rohan",60)
# print(s.__name)

#Problem_6:
def my_decorator(func):
    print("#Problem_6 Answer")
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@my_decorator
def greet():
    print("Hello!")

greet()