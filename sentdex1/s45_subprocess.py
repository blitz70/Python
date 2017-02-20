#   45. subprocess
#   doesn't work on IDLE

import subprocess

output = ''
_output = subprocess.check_output('python -V'
                                  , shell=True)
output += str(_output) + '\n\n'
_output = subprocess.check_output('python s34_sys.py "this is my" "first"'
                                  , shell=True)
output += str(_output) + '\n\n'
_output = subprocess.check_output('python s34_sys.py "this is my" "first"'
                                  , shell=True, universal_newlines=True)
output += str(_output) + '\n\n'
file = open('s45.txt','w')
file.write(output)
file.close()
