# map: It is used to modify the elements in a list
# filter: It filters the values in a list based on a condition

# map
# numbers = [1,2,3,4,5,6]

# squared_numbers = map(lambda x:x*2, numbers)

# print(list(squared_numbers))

# numbers = [1,2,3,4,5,6]

class MapFunctionality():
       def __init__(self,numbers):
              # self.num = num
              self.numbers = numbers
       
       def calculate(self):
              return list(map(lambda num:num*2, self.numbers))
       
       
obj = MapFunctionality([1,2,3])
print(obj.calculate()) 