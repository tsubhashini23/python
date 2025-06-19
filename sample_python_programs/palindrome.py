# A palindrome is a word, number, or phrase that reads the same backward as forward.Both forward and backward should read the same
# s[::-1] reverses the string.
# s == s[::-1] compares original with reversed.
# f they match → it's a palindrome


def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("happy"))


def is_palindrome(m):
    
    m = m.lower().replace(" ", "")
    return m == m[::-1]

print(is_palindrome("Race Car"))