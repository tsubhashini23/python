class Parent:
    def greet(self):
        return "Hello from parent"
    
class Child(Parent):
    def child_greet(self):  
        return super().greet() + " : Hello from child"
    
obj = Child()
print(obj.greet())
print(obj.child_greet())


    
