#   Class method:
#   It can be called without object creation
#   Class methods are used when you want to work with the class itself (not instance-specific data). They receive the class as the first argument (cls) instead of the instance (self).
#   Use the annotation @classmethod to define the method
#   Class methods will also accept arguments at run time

class MyClass():
    
    @classmethod
    def class_method(cls, x, y):
        return x+y
    
    def instance_method(self):
        return "Instance Details"
    
obj = MyClass()

print(obj.instance_method())
    
print(MyClass.class_method(2,3))