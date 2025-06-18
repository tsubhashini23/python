#   Class method:
#   Can access and modify class variables and other @classmethod(@classmethod).
#   Class methods are used when you want to work with the class itself (not instance-specific data). They receive the class as the first argument (cls) instead of the instance (self).
#   Use the decorator @classmethod to define the method
#   Class methods will also accept arguments at run time
#   Called on the class or an instance.

# Instance Method:
# Default method type.
# Takes self as the first argument.
# Can access and modify instance variables and methods.
# Called on an instance of the class.


# Static Method:
# Defined with the @staticmethod decorator.
# No self or cls parameter.
# Cannot access instance or class variables directly.
# Just like a regular function inside a class.
# Called on the class or an instance.

class MyClass():
    
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def class_method(cls, x, y):
        cls.class_method2()
        return x+y
    
    @classmethod
    def class_method2(cls):
        print("Inside class_method2")
    
    def instance_method(self):
        return "Instance Details"
    
    @staticmethod
    def static_method(a,b):
        print("Inside static method")
        return a**b
    
obj1 = MyClass("Aditya")
obj2 = MyClass("Jai")

print(obj1.instance_method())
    
print(f" Called using class name: {MyClass.class_method(2,3)}")
print(f" Called using class name obj1: {obj1.class_method(2,3)}")
print(f" Called using class name obj2: {obj2.class_method(2,3)}")


print(f" Called using class name: {MyClass.static_method(2,3)}")
print(f" Called using class name obj1: {obj1.static_method(2,3)}")
print(f" Called using class name obj2: {obj2.static_method(2,3)}")
