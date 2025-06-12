class Parent:
    def greet(self):
        return "Hello from parent"
    
class ChildOne(Parent):
    def child_greet(self):  
        return super().greet() + " : Hello from child One"
    
class ChildTwo(Parent):
    def baby_greet(self):  
        return super().child_greet() + " : Hello from child two"
    
obj_one = ChildOne()
print(obj_one.greet())
print(obj_one.child_greet())

obj_two = ChildTwo()
print(obj_two.baby_greet())





    
