import timeit

print(timeit.timeit("1+3", number=100000))
print(timeit.timeit("1+3", number=100000000))

print()
print(timeit.timeit('''
list1 = range(10000)

def div_by_five1(num):
    return num % 5 == 0

xyz = [i for i in list1 if div_by_five1(i)]
''', number=1000))

print(timeit.timeit('''
list1 = range(10000)

def div_by_five2(num):
    if num % 5 == 0:
        return True
    else:
        return False
xyz = [i for i in list1 if div_by_five2(i)]
''', number=1000))

print()
print(timeit.timeit('''
list1 = range(100000)

def div_by_five1(num):
    return num % 5 == 0

xyz = (i for i in list1 if div_by_five1(i))
''', number=1000))

print(timeit.timeit('''
list1 = range(100000)

def div_by_five1(num):
    return num % 5 == 0

xyz = [i for i in list1 if div_by_five1(i)]
''', number=1000))
