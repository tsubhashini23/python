
#   Changing the class variable using class name, will get reflected in all the instances(objects)
#   Changing the class variable using an instance(object), will get reflected only in that instance(object)
#   After changing the class variable(color) using an instance(obj1), again change the class variable using the class name and print the values of the class variable using obj1 and see. Only the value set using object(obj1) wll get displayed as Python created an instance variable color for obj1, this shadows/hides the class variable color for obj1 permanently, unless you delete it with del obj1.color

# __dict__  :
# is a built-in attribute that stores all instance variables of an object in a dictionary format.


class Bird():
    color = "Green"
    def __init__(self, name):
        self.name = name
        
        
obj1 = Bird("Parrot")
obj2 = Bird("Dove")

print(obj1.color)
print(obj2.color)
print(Bird.color)

obj1.color = "multicolor"

print(f" modified color using obj1: {obj1.color}")
print(f"color remains same for obj2 as modification happened using obj1: {obj2.color}")

Bird.color = "Red"
print(f"Color not modified as Python created an instance variable color for obj1: {obj1.color}")
print(f"color changed only for obj2 as it is still using class-level color: {obj2.color}")

print(obj1.__dict__)  # {'name': 'Parrot', 'color': 'multicolor'}
print(obj2.__dict__)  # {'name': 'Dove'}

del obj1.color

print(obj1.__dict__)  # {'name': 'Parrot', 'color': 'multicolor'}
print(obj2.__dict__)  # {'name': 'Dove'}

print(f"Red get reflected as the instance variable created using obj1.color is deleted. It uses the class color: {obj1.color}")
print(f"obj2 still uses class color: {obj2.color}")






