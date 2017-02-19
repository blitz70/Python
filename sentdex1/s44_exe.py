#   44. Deployment - cx freeze
#   install module : pip install cx_Freeze
#   build exe : python s44_exe.py build

from cx_Freeze import setup, Executable

setup(name='example'
      ,version='1.0'
      ,description='used tkinter'
      ,executables = [Executable('s37_parse.py')])
