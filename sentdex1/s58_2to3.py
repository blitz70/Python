#   58. 2to3
#   convert python 2 code to 3 code
#   python 2to3.py -w targetfile
#   -w : commit and backup, else show only
#   python c:\Program Files\Python36\Tools\scripts\2to3.py s58_2to3.py

import urllib.request, urllib.error, urllib.parse

try:
    x = urllib.request.urlopen('https://www.hackthissite.org').read()
    print(x)
except Exception as e:
    print(str(e))
