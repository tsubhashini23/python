def find_duplicates(list):
    ln = len(list)
    duplicates = []
    # count = 0
    for i in range(ln):
        for j in range(i+1, ln):
            if list[i] == list[j] and list[i] not in duplicates:
                duplicates.append(list[i])
    return duplicates
                
                
print(find_duplicates([1,2,3,4,5,5,5,7,9,7,6,6,8,8]))
    