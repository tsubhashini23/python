# List comprehension is used to create list using single line
# It improves readability and performance when generating lists based on loops or conditions.

evens = [n for n in range(10) if n % 2 == 0]
print(evens)