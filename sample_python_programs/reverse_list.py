#Reverse number list

def reverse_list(list):
        reversed_list = []
        ln = len(list)
        # print(ln)
        for i in range(ln-1, -1, -1):            
            if list[i] not in reversed_list:
                reversed_list.append(list[i])
        return reversed_list
    
print(reverse_list([30,2,3,4,5,6]))

#Reverse using EXTENDED SLICING method: list[::-1] (Start from the end of the sequence and move backward by 1 step until the beginning.”)
# start → not given → defaults to end of list if step is negative

# stop → not given → goes until the beginning (index -1) when stepping backwards

# step = -1 → this means "go backwards one element at a time"

def play_with_list(list):
    print("Sorted List:", sorted(list))
    print("Reversed List",list[::-1])
    
play_with_list([5,1,7,2,3])

#Reverse a string

def reverse_string(name):
    updated_name = name.lower()
    new_list = list(updated_name)
    ln = len(new_list)
    reversed_list = []
    for i in range(ln-1, -1, -1):
        reversed_list.append(new_list[i])
    result = print("".join(reversed_list))
    return result

reverse_string("dog")




    

    