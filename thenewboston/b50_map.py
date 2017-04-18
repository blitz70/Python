# builtins : map()

def double_it(x):
    return x*2

list1 = [10, 45, 2, 67, 100]
print(list1)

list2 = []
for no in list1:
    list2.append(double_it(no))
print(list2)

list3 = list(map(double_it, list1))
print(list3)
