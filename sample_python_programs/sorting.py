#Bubble sort: Bubble Sort works by repeatedly comparing adjacent elements and swapping them if they are in the wrong order.

def sorting(new_list):
    ln = len(new_list)
    # sorted_list = []
    for i in range(ln):
        for j in range(0, ln-i-1):
            if new_list[j] > new_list[j+1]:
                new_list[j], new_list[j+1] =  new_list[j+1], new_list[j]
                # print (new_list)
    return new_list

print(sorting([8,2,1,5,3,4]))
