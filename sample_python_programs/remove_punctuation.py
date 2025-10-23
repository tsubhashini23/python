def remove_punctuation(name):
    name_list = list(name)
    new_list = []
    # print(name_list)
    ln = len(name_list)
    # print(ln)
    punctuation = "&,-"
    for i in range(ln):
            if name_list[i] not in punctuation:
                new_list.append(name_list[i])
    result = print(''.join(new_list))
    return result

remove_punctuation("s,ubha")


name = "madhu,sudhan"

punctuation_marks = ",.';:"

for c in name:
    if c in punctuation_marks:
        new_name = name.pop(c)
print(new_name)