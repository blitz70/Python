# binary operators

b1 = 50       # 110010
b2 = 25       # 011001
print(b1, bin(b1))
print(b2, bin(b2))

# binary and/or
b3 = b1 & b2  # 010000
b4 = b1 | b2  # 111011
print(b3, bin(b3))
print(b4, bin(b4))

# binary shift
b5 = 138      # 10001010
b6 = b5>>2    # 00100010
print(b5, bin(b5))
print(b6, bin(b6))
print(int('0b00100010', 2))
