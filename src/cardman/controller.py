from pathlib import Path
from tkinter import Tk

from .model import Model
from .view import View


class Controller:
    def __init__(self):
        self.root = Tk()
        self.model = Model()
        self.view = View(self.root, self.model)

        self.view.select_card_callback = self.select_card_callback
        self.view.select_template_callback = self.select_template_callback

    def run(self):
        self.root.title("Cardman")
        self.root.mainloop()

    def select_card_callback(self, card: Path):
        self.model.load_card_content(card)
        self.view.render_card_content()

    def select_template_callback(self, template: Path):
        print("Template is", template)
