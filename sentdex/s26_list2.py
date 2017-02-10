#   26. List Manipulation

x = [9,8,7,6,5,4,3,2,1,0,0]
print (x, 'original')

x.append(15)
print (x, 'append 15')

x.insert(1,99)
print (x, 'insert 99 at index 1')

x.remove(6) #use?
print (x, 'remove 6')

del x[2]
#x.remove(x[2])
print (x, 'remove index 2')

print (x[4:6], 'display index 4-5')

print(x.index(0), 'display index of 0') #use?

print (x.count(0), 'count 0s')

y = ['Janet','Jessy','성규','Kelly','Alice','Joe','Bob']
x.sort()
y.sort()
print (x, y, 'sort')
