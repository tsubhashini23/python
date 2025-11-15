sentence = "Hello how are you"



word_list = sentence.split(" ")
print(word_list)
# reversed_word_list = word_list[::-1]
# print(reversed_word_list)

# for word in word_list:
#     reversed_word_list.append(word)
# print(reversed_word_list)

ln = len(word_list)
new_list = []
for i in range(ln-1, -1, -1):
    new_list.append(word_list[i])
result = " ".join(new_list)
print(result)




