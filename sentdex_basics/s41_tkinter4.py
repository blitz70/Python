#   41. tkinter - menu

from tkinter import *


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title('GUI')
        self.pack(fill=BOTH, expand=1)
        menuBar = Menu(self.master)
        self.master.config(menu=menuBar)
        fileMenu = Menu(menuBar)
        fileMenu.add_command(label='New')
        fileMenu.add_command(label='Open')
        fileMenu.add_command(label='Save')
        fileMenu.add_command(label='Exit', command=self.client_exit)
        menuBar.add_cascade(label='File', menu=fileMenu)
        editMenu = Menu(menuBar)
        editMenu.add_command(label='Undo')
        editMenu.add_command(label='Redo')
        editMenu.add_command(label='Cut')
        editMenu.add_command(label='Copy')
        editMenu.add_command(label='Paste')
        menuBar.add_cascade(label='Edit', menu=editMenu)

    def client_exit(self):
        exit()

root = Tk()
root.geometry('400x300')

app = Window(root)

root.mainloop()