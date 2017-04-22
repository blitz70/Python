# Flexible number of arguments

def add_numbers(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add_numbers(10,5))
print(add_numbers(1,3,5,11,50))
print(add_numbers(112,63,7723,125721))
