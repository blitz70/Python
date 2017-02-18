#   16. Writing to File

text = 'Sample Text to Save\nNew line!'

saveFile = open('s16.txt', 'w')
saveFile.write(text)
saveFile.close()
