x = [1, 5, 2, 6, ]
y = [3, 4, 9, 8, ]
z = ["d", "b", "o", "s", ]
o = {"one": "d", 2: "b", "three": "o", 4: "s", }

[print(a, b, c) for a, b, c in zip(x, y, z)]
print(zip(x, y, z))
[print(i) for i in zip(x, y, z)]
print(list(zip(x, y, z)))
print(dict(zip(x, z)))
[print(a, b, c) for a, b, c in zip(x, y, o)]

print("note1")
[print(a, b, c) for a, b, c in zip(x, y, z)]
# print(a, b, c)
print()
for a, b, c in zip(x, y, z):
    print(a, b, c)
print("!", a, b, c)

print("note2")
[print(x, y, z) for x, y, z in zip(x, y, z)]
print(x, y, z)
for x, y, z in zip(x, y, z):
    print(x, y, z)
print("!", x, y, z)
