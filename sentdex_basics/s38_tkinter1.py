#   38. tkinter - basic windows

from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        #super().__init__()
        self.master = master

root = Tk()

app = Window(root)

root.mainloop()
'''
Tk().mainloop()
'''