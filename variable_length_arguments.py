# Variable-Length-Arguments in python:
# Accepts any number of unnamed values (eg, *numbers_args , collects extra positional arguments as a tuple )
# Accepts any number of named arguments ( eg, **keyword_args, collects extra keyword arguments as a dictionary)

def get_details(*numbers, **value_pairs):
    print(f"Different sets of number: {numbers}")
    print(f"Different sets of key values pairs: {value_pairs}")
    
get_details(1,2,3,bird = "parrot", color = "multicolor")