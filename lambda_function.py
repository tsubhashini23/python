# lambda:
# It is an anonymous function defied using lamba keyword
# They are used to write small, one-line functions without using def
# This function can be used as parameter inside another functions like sorted(), map(), filter() etc
# No statements ike return, for are allowed inside



# class Addition():
    
# Constructor:
    # def __init__(self):
    #     self.data = lambda x, y: x + y
        
# Normal function:
    # def data(self,x,y):
    #     return x+y

# Lambda function:
# data = lambda x,y:x+y
    
# # obj = Addition()
# print("Result:", data(7,3))


#Used in sorted():

pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
pairs_sorted = sorted(pairs, key=lambda z: z[0])
print(pairs_sorted)

# z[1] refers to the number name in tuple which is a string.Python sorts strings alphabetically — meaning by ASCII/Unicode order, character by character.
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]    
pairs_sorted = sorted(pairs, key=lambda z: z[1])
print(pairs_sorted)



