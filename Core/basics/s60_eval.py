#   60. eval
'''
[print('test') if False else print('hmm')]

'[1,5,6,2,3]'
print(eval(eval(x))[2])
'''

dataStr = '[9,8,7,6,5,4,3,2,1,0]'

dataList = eval(dataStr)
print(dataList)

print('='*10)
for dl in dataList:
    print(dl)

for i in range(len(dataList)):
    print(dataList[i])

x = input('x:')
code = eval(input('code:'))
print('code =',code)

#code = eval('x=10')
#print(code, x)

#code = eval('''
#def mycode():
#    print('hello')
#mycode()
#''')
#print(code)



