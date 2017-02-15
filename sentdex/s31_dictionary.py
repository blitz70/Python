#   31. Dictionaries

exDict = {'Jack':15,'Alice':12,'Bob':22,'Kevin':17}

print(exDict)
print(exDict['Jack'])
print(exDict)
exDict['Tim']=[14]
print(exDict)
exDict['Tim'].append('gray')
exDict['Tim'][0]=15
print(exDict)
del exDict['Tim']
print(exDict)

exDict2 = {'Jack':[15,'blond'],'Alice':[12,'black'],'Bob':[22,'brown'],'Kevin':[17,'red']}
print(exDict2)
print(exDict2['Jack'])
print(exDict2['Jack'][1])
