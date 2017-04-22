#   42. tkinter - images and text
#   install Pillow module, http://www.lfd.uci.edu/~gohlke/pythonlibs/
#   pip install pillow

from tkinter import *
from PIL import Image, ImageTk


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
        fileMenu.add_command(label='Save', command=self.client_exit)
        fileMenu.add_command(label='Exit', command=self.client_exit)
        menuBar.add_cascade(label='File', menu=fileMenu)
        editMenu = Menu(menuBar)
        editMenu.add_command(label='Show Image', command=self.showImg)
        editMenu.add_command(label='Show Text', command=self.showTxt)
        menuBar.add_cascade(label='Edit', menu=editMenu)
        #quitButton=Button(self, text='Quit', command=self.client_exit)
        #quitButton.place(x=0, y=0)

    def client_exit(self):
        exit()

    def showImg(self):
        load = Image.open('s42.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def showTxt(self):
        text = Label(self, text ='This is Python!')
        #text.place(x=0, y=0)
        text.pack()

root = Tk()
root.geometry('640x480')

app = Window(root)

root.mainloop()
