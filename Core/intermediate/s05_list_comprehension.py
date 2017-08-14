def div_by_five(num):
    return num % 5 == 0

list1 = [1, 5, 2, 22, 12, 9, 10, 16, 32, 55, 13]

print("normal")
five = []
for n in list1:
    if div_by_five(n):
        five.append(n)
print(five)

print("list comprehension")
five = [n for n in list1 if div_by_five(n)]
print(five)

print("generator")
five = (n for n in list1 if div_by_five(n))
for n in five:
    print(n)
five = (n for n in list1 if div_by_five(n))
[print(n) for n in five]
print(five)

print("normal")
for i in range(3):
    for ii in range(5):
        print(i, ii)

print("list comprehension")
# [print(i, ii) for ii in range(5) for i in range(3)]
# [[print(i, ii) for ii in range(5)] for i in range(3)]
# [[print(i, ii) for i in range(3)] for ii in range(5)]
five = [[i, ii] for i in range(3) for ii in range(5)]
print(five)

print("generator")
# five = ((i, ii) for i in range(5000) for ii in range(1000000))
# print(five)
# for i in five:
#     print(i)
# five = (((i, ii) for ii in range(1000000)) for i in range(5000))
# for i in five:
#     for ii in i:
#         print(ii)

xyz = (print(i) for i in range(5))
for i in xyz:
    pass
xyz2 = (print(i) for i in range(5))
[i for i in xyz2]