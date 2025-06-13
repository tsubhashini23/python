# Self:
# 1. It is not a keyword, it is a convention in python
# 2. It refers to the current instance of the class
# 3. It must be the first parameter in the instance methods
# 4. No need to pass it explicitly when calling methods
# 5. It is used to access instance variables and methods inside the class
# 5. A variable attached to self (self.data), can be accessed across all the methods inside the class

# self.method_name will call the current class's method, to call the parent class method we use "super().method_name"

class Person():
    def __init__(self, name, place):
        self.name = name
        self.place = place
        
    def get_details(self):
        return (f"My name is {self.name} and I live in {self.place}")

obj = Person("Subha", "Chennai")
print(obj.get_details())