#   17. Appending Files

appendMe = '\nNew bit of information'

saveFile = open('s16.txt', 'a')
saveFile.write(appendMe)
saveFile.close()
