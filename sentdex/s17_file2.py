#   17. Appending Files

appendMe = '\nNew bit of information'

saveFile = open('exampleFile.txt','a')
saveFile.write(appendMe)
saveFile.close()
