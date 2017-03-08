#   59. Pickle
#   python object save+compression

import pickle

objSave = {
    'name':'blitz'
    ,'gender':'M'
    ,'age':'48'
    ,'job':'think tank'
    ,'height':'165'
    ,'weight':'67'
    }
print(objSave, ': before save')

with open('s59.pickle','wb') as saveFile:
    pickle.dump(objSave, saveFile)

loadFile = open('s59.pickle','rb')
objLoad = pickle.load(loadFile)
print(objSave, ': after load')
loadFile.close()
