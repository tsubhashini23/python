
def pattern_one(num):
    print("Pattern One")
    for i in range(num):
        for j in range(num):
            print("*", end=" ")
        print("\n")      
pattern_one(5)

def pattern_two(num):
    print("Pattern Two")
    for i in range(num):
        for j in range(i+1):
            print("*", end=" ")
        print("\n")    
pattern_two(5)

def pattern_three(num):
    print("Pattern Three")
    for i in range(num):
        for j in range(num):
            if j >= num-i-1:
                print("*", end = " ")
            else:
                print(" ", end = " ")   
        print("\n")    
pattern_three(5)

def pattern_four(num):
    print("Pattern Four")
    for i in range(num):
        for j in range(num-i-1): 
                    print(" ", end = "")   
        for k in range(i+1):
                    print("*", end = " ")
        print("\n")    
pattern_four(3)
        
        