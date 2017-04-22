#   61. exec

dataStr = '[9,8,7,6,5,4,3,2,1,0]'

dataList = exec(dataStr)
print(dataList)

exec("dataList2=[9,8,7,6,5,4,3,2,1,0]")
print(dataList2)
for dl in dataList2:
    print(dl)

exec("def test():print('this is from exec function')")
test()

exec('''
def test2():
    print('this is from')
    print('another exec function')
''')
test2()
