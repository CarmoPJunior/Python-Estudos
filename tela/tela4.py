from tkinter import *
from PIL import ImageTk, Image
import glob

files = glob.glob('*.png')

class App:

    def __init__(self, root):

        self.l = Listbox(root, width = 50, height = 15)
        self.l.pack()
        self.l.bind('<<ListboxSelect>>', self.lol)

        self.c = Label(root)
        self.c.pack()

        for f in files:
            self.l.insert(END, f)

    def lol(self, evt):

        path = files[self.l.curselection()[0]]
        img = ImageTk.PhotoImage(Image.open(path))
        self.c.image = img           # save reference
        self.c.configure(image=img)  # configure the label
        self.c.pack()

root = Tk()
App(root)
root.mainloop()