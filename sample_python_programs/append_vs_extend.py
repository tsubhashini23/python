#Append

list1 = [1, 2, 3]
list1.append([4, 5])
print(list1)

#Extend

list1 = [1, 2, 3]
list1.extend([4, 5])
print(list1)


#Replace will work only with string and not with lists
str = "subha Madhusudhan"
new_str = str.replace(" ","_")
print(new_str)