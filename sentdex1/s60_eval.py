#   60. eval

dataStr = '[9,8,7,6,5,4,3,2,1,0]'

dataList = eval(dataStr)
print(dataList)

print('='*10)
for dl in dataList:
    print(dl)

print('='*10)
for i in range(len(dataList)):
    print(dataList[i])

x = input('code:')
code = eval(input('code:'))
print(code)
