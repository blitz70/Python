list1 = [i for i in range(50000000)]
print("List1", list1[-10:])

generator1 = (i for i in range(50000000))
print("Generator1", generator1)

list2 = [i for i in generator1]
print("List2", list2[:10])
