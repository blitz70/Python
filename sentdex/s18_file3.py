#   18. Reading from Files

saveFile = open('exampleFile.txt','r')
#rd = saveFile.read()
#rd = saveFile.readline()
rd = saveFile.readlines()
saveFile.close()

print(rd)
