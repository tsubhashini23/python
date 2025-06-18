# Polymorphism:
# The same method name behaves differently depending on the object’s class.
# polymorphism is most commonly achieved through method overriding in inheritance.

# Method Overriding:
# A child class defines a method with the same name as a method in its parent class.
# When called on an instance of the child class, the child version is executed (not the parent’s).

class Life():
    def getData(self):
        print("Happy Life")
        
class Family(Life):
    
    def __init__(self, name):
        self.name = name
        
    # def getData(self):
    #     print("Happy Family")
        
        
class Work(Family):
    
    def __init__(self, age):
        self.name = age
        
    # def getData(self):
    #     print("Happy work place")
        
obj = Work()
obj1 = Family()
obj2 = Life()
# obj.getData()
obj1.getData()