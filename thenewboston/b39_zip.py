# data structure, zip

first = ['John', 'Jane', '길동', '무개']
last = ['Doh', 'Doh', '홍', '김']

names = zip(first, last)
for name in names:
    print(name)

names = zip(first, last) #must do this
for first, last in names:
    print(first, last)
