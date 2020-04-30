from tkinter import Tk

from .model import Model
from .view import View


class Controller:
    def __init__(self):
        self.root = Tk()
        self.model = Model()
        self.view = View(self.root, self.model)

    def run(self):
        self.root.title("Cardman")
        self.root.mainloop()
