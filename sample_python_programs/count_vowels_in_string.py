def count_vowels(name):
    vowels = "aeiouAEIOU"
    count = 0
    for c in name:
        if c in vowels:
            count = count + 1
    return count
    
print(count_vowels("subhashini"))
    