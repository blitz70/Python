#   33. OS

import os, time

#os.system('ipconfig')
#os.makedirs('d:\\pythontest/dir1/dir2/dir3')

curDir = os.getcwd()
print(curDir)
print(os.listdir())
os.mkdir('d:\\pythontest')
time.sleep(5)
os.rename('d:/pythontest','d:/PYTHONTEST2')
time.sleep(5)
os.rmdir('d:/PYTHONTEST2')


