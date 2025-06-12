class Parent():
    def greet(sef):
        return "Hello parent"
    
    def __init__(self):
        print("Parent constructor is called")
    
class Child(Parent):
    
    # def __init__(self):
    #     print("Child constructor is called")
    
    def test(self):
        return "Hello child"
    
obj = Child()
print(obj.test())

        
        