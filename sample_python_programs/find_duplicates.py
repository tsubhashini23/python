# def find_duplicates(list):
#     ln = len(list)
#     duplicates = []
#     # count = 0
#     for i in range(ln):
#         for j in range(i+1, ln):
#             if list[i] == list[j] and list[i] not in duplicates:
#                 duplicates.append(list[i])
#     return duplicates
                
                
# print(find_duplicates([1,2,3,4,5,5,5,7,9,7,6,6,8,8]))


def find_duplicate_letters(name):
    updated_name = name.lower()
    input_list = list(updated_name)
    duplicate_letters = []
    ln = len(input_list)
    for i in range(ln):
        for j in range(i+1, ln):
            if input_list[i] == input_list[j] and input_list[i] not in duplicate_letters:
                duplicate_letters.append(input_list[i])
    return duplicate_letters
                
                
print(find_duplicate_letters("Subhashini"))
    